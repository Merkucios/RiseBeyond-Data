
# R3: реактивный подход к игровой логике


# Введение: один сценарий, два мира

Прежде чем погружаться в теорию, посмотрим на конкретную задачу глазами двух разработчиков — один пишет традиционно, другой использует R3.

**Сценарий:** система здоровья игрока. Нужно:

- Обновлять полоску HP при изменении здоровья
- Показывать предупреждение при HP < 30%
- Запускать звук и анимацию при смерти
- Дебаунсировать частые удары (дробью) чтобы не спамить звук
- Запрещать лечение мёртвого игрока

---

## До R3: Update, флаги, события



```csharp
// ──────────────────────────────────────────────────────────────────────
// PlayerHealthLegacy.cs
// Традиционный подход: события + флаги + Update
// ──────────────────────────────────────────────────────────────────────
public class PlayerHealthLegacy : MonoBehaviour
{
    [Header("Settings")]
    [SerializeField] private int maxHealth = 100;

    [Header("UI")]
    [SerializeField] private Slider      hpSlider;
    [SerializeField] private Image       hpFillImage;
    [SerializeField] private TMP_    hp;
    [SerializeField] private GameObject  deathPanel;
    [SerializeField] private GameObject  lowHpWarning;
    [SerializeField] private AudioSource damageAudio;

    // C# события
    public event Action<int> OnHealthChanged;
    public event Action       OnDeath;
    public event Action<int>  OnDamageTaken;

    // Флаги состояния
    private int   _currentHealth;
    private bool  _isDead;
    private bool  _isLowHp;
    private float _lastDamageTime;
    private float _lastSoundTime;          // для дебаунса звука
    private bool  _deathEventFired;        // чтобы событие смерти не дублировалось
    private bool  _wasLowHpLastFrame;      // чтобы не спамить предупреждение

    private const float SoundDebounceSeconds = 0.2f;
    private const float LowHpThreshold       = 0.3f;

    private void Awake()
    {
        _currentHealth = maxHealth;
        UpdateUI(); // первичная инициализация UI
    }

    private void Start()
    {
        // Подписываемся на собственные события (да, это выглядит странно)
        OnDeath        += HandleDeath;
        OnHealthChanged += HandleHealthChanged;
    }

    private void Update()
    {
        // Проверяем переход в состояние низкого HP каждый кадр
        bool isLowNow = (float)_currentHealth / maxHealth < LowHpThreshold
                        && _currentHealth > 0;

        // Нужен ручной diff чтобы не вызывать SetActive каждый кадр
        if (isLowNow != _wasLowHpLastFrame)
        {
            lowHpWarning.SetActive(isLowNow);
            _wasLowHpLastFrame = isLowNow;
        }

        // Здесь могла бы быть ещё дюжина подобных проверок...
    }

    public void TakeDamage(int amount)
    {
        if (_isDead) return;  // флаг-защита #1
        if (amount <= 0) return;

        int prevHealth = _currentHealth;
        _currentHealth = Mathf.Max(0, _currentHealth - amount);
        int actualDamage = prevHealth - _currentHealth;

        if (actualDamage <= 0) return;

        OnHealthChanged?.Invoke(_currentHealth);
        OnDamageTaken?.Invoke(actualDamage);

        // Дебаунс звука — руками
        if (Time.time - _lastSoundTime > SoundDebounceSeconds)
        {
            damageAudio.Play();
            _lastSoundTime = Time.time;
        }

        // Проверка смерти — руками, с флагом чтобы не стрелять дважды
        if (_currentHealth <= 0 && !_deathEventFired)
        {
            _deathEventFired = true;
            _isDead          = true;
            OnDeath?.Invoke();
        }
    }

    public void Heal(int amount)
    {
        if (_isDead)   return;  // флаг-защита #2
        if (amount <= 0) return;

        _currentHealth = Mathf.Min(maxHealth, _currentHealth + amount);
        OnHealthChanged?.Invoke(_currentHealth);
    }

    public void Revive(int hp)
    {
        _isDead          = false;  // сбрасываем флаг #1
        _deathEventFired = false;  // сбрасываем флаг #2
        _currentHealth   = Mathf.Clamp(hp, 1, maxHealth);
        OnHealthChanged?.Invoke(_currentHealth);
        deathPanel.SetActive(false);
    }

    private void HandleHealthChanged(int hp)
    {
        UpdateUI();
    }

    private void HandleDeath()
    {
        deathPanel.SetActive(true);
        // Запустить анимацию, отключить управление, etc.
    }

    private void UpdateUI()
    {
        float percent = (float)_currentHealth / maxHealth;

        hpSlider.value = percent;
        hp.    = $"{_currentHealth} / {maxHealth}";

        // Цвет — ручной if-else
        if      (percent > 0.6f) hpFillImage.color = Color.green;
        else if (percent > 0.3f) hpFillImage.color = Color.yellow;
        else                     hpFillImage.color = Color.red;
    }

    private void OnDestroy()
    {
        // Отписываемся вручную — а вдруг забудем?
        OnDeath         -= HandleDeath;
        OnHealthChanged -= HandleHealthChanged;
    }
}
```

**Что здесь не так:**



```csharp
Проблемы традиционного кода
├── Состояние размазано по флагам (_isDead, _deathEventFired, _wasLowHpLastFrame)
├── Логика в Update() — проверки каждый кадр вместо реакции на изменения
├── Дебаунс звука написан вручную через Time.time
├── UpdateUI() вызывается при КАЖДОМ изменении HP, пересчитывает всё
├── Возможна ошибка: забыли сбросить флаг при Revive -> смерть не сработает повторно
├── Подписки на события нужно отслеживать вручную -> риск утечки памяти
└── Добавить новое условие (напр. заморозка) = ещё один флаг и проверка в Update
```

---

## После R3: потоки, операторы, декларативность



```csharp
// ──────────────────────────────────────────────────────────────────────
// PlayerHealth.cs  (Модель данных)
// Чистая модель без зависимости от MonoBehaviour
// ──────────────────────────────────────────────────────────────────────
using System;
using R3;
using UnityEngine;

public class PlayerHealth : IDisposable
{
    // ── Первичное состояние ────────────────────────────────────────────
    public ReactiveProperty<int> CurrentHP { get; }
    public int MaxHP { get; }

    // ── Вычисляемые потоки (производные, не хранят отдельного состояния)
    public ReadOnlyReactiveProperty<float>        HealthPercent { get; }
    public ReadOnlyReactiveProperty<bool>         IsDead        { get; }
    public ReadOnlyReactiveProperty<HealthStatus> Status        { get; }

    // ── События ───────────────────────────────────────────────────────
    private readonly Subject<int> _onDamageTaken = new();
    public Observable<int> OnDamageTaken => _onDamageTaken;

    private readonly DisposableBag _disposables = new();

    public PlayerHealth(int maxHP = 100)
    {
        MaxHP     = maxHP;
        CurrentHP = new ReactiveProperty<int>(maxHP);

        // Все производные состояния — это просто трансформации CurrentHP.
        // Никаких отдельных флагов, никакой синхронизации вручную.
        HealthPercent = CurrentHP
            .Select(hp => Mathf.Clamp01((float)hp / MaxHP))
            .ToReadOnlyReactiveProperty();

        IsDead = CurrentHP
            .Select(hp => hp <= 0)
            .ToReadOnlyReactiveProperty();

        Status = CurrentHP
            .Select(hp => (float)hp / MaxHP switch
            {
                0f       => HealthStatus.Dead,
                <= 0.30f => HealthStatus.Critical,
                <= 0.60f => HealthStatus.Wounded,
                _        => HealthStatus.Healthy,
            })
            .ToReadOnlyReactiveProperty();

        // Регистрируем всё для освобождения одной командой
        CurrentHP    .AddTo(ref _disposables);
        HealthPercent.AddTo(ref _disposables);
        IsDead       .AddTo(ref _disposables);
        Status       .AddTo(ref _disposables);
    }

    public void TakeDamage(int amount)
    {
        if (amount <= 0 || IsDead.CurrentValue) return;

        int prev       = CurrentHP.Value;
        CurrentHP.Value = Mathf.Max(0, CurrentHP.Value - amount);
        int actual     = prev - CurrentHP.Value;

        if (actual > 0) _onDamageTaken.OnNext(actual);
    }

    public void Heal(int amount)
    {
        // IsDead.CurrentValue — читаем актуальное значение без флага
        if (amount <= 0 || IsDead.CurrentValue) return;
        CurrentHP.Value = Mathf.Min(MaxHP, CurrentHP.Value + amount);
    }

    public void Revive(int hp) =>
        CurrentHP.Value = Mathf.Clamp(hp, 1, MaxHP);
        // IsDead автоматически станет false — нет флага для сброса

    public void Dispose()
    {
        _disposables.Dispose();
        _onDamageTaken.Dispose();
    }
}

public enum HealthStatus { Healthy, Wounded, Critical, Dead }
```



```csharp
// ──────────────────────────────────────────────────────────────────────
// HealthView.cs  (Представление)
// Только подписки и UI-обновления, никакой логики
// ──────────────────────────────────────────────────────────────────────
using System;
using R3;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

public class HealthView : MonoBehaviour
{
    [SerializeField] private Slider     hpSlider;
    [SerializeField] private Image      hpFillImage;
    [SerializeField] private TMP_   hp;
    [SerializeField] private TMP_   status;
    [SerializeField] private GameObject deathPanel;
    [SerializeField] private GameObject lowHpWarning;
    [SerializeField] private AudioSource damageAudio;

    private static readonly Color ColorHealthy  = Color.green;
    private static readonly Color ColorWounded  = Color.yellow;
    private static readonly Color ColorCritical = Color.red;

    private DisposableBag _disposables = new();

    public void Bind(PlayerHealth model)
    {
        _disposables.Dispose();
        _disposables = new DisposableBag();

        // Слайдер и текст
        model.HealthPercent
            .Subscribe(p => hpSlider.value = p)
            .AddTo(ref _disposables);

        model.CurrentHP
            .Subscribe(hp => hp. = $"{hp} / {model.MaxHP}")
            .AddTo(ref _disposables);

        // Плавный цвет через двойной Lerp
        model.HealthPercent
            .Subscribe(p =>
            {
                hpFillImage.color = p < 0.5f
                    ? Color.Lerp(ColorCritical, ColorWounded, p * 2f)
                    : Color.Lerp(ColorWounded,  ColorHealthy, (p - 0.5f) * 2f);
            })
            .AddTo(ref _disposables);

        // Статус-текст — меняется только при смене статуса (DistinctUntilChanged внутри ReactiveProperty)
        model.Status
            .Subscribe(s => status. = s switch
            {
                HealthStatus.Healthy  => "HEALTHY",
                HealthStatus.Wounded  => "WOUNDED",
                HealthStatus.Critical => "CRITICAL!",
                HealthStatus.Dead     => "DEAD",
                _                    => ""
            })
            .AddTo(ref _disposables);

        // Панель смерти — декларативно, без флага
        model.IsDead
            .Subscribe(dead => deathPanel.SetActive(dead))
            .AddTo(ref _disposables);

        // Предупреждение — без Update, без diff вручную
        model.HealthPercent
            .Select(p => p is > 0f and < 0.3f)
            .DistinctUntilChanged()
            .Subscribe(show => lowHpWarning.SetActive(show))
            .AddTo(ref _disposables);

        // Дебаунс звука — оператором, не Time.time вручную
        model.OnDamageTaken
            .ThrottleFirst(
                TimeSpan.FromSeconds(0.2f),
                UnityTimeProvider.Update)
            .Subscribe(_ => damageAudio.Play())
            .AddTo(ref _disposables);
    }

    private void OnDestroy() => _disposables.Dispose();
}
```

**Что изменилось:**



```csharp
Было (традиционный подход)       Стало (R3)
─────────────────────────        ──────────────────────────────
_isDead            флаг    →     IsDead.CurrentValue   поток
_deathEventFired   флаг    →     Take(1) или Where      оператор
_wasLowHpLastFrame флаг    →     DistinctUntilChanged   оператор
_lastSoundTime     флаг    →     ThrottleFirst          оператор
Update() проверки  каждый кадр → Subscribe              реакция
UpdateUI() всё     перерисовывает → отдельные подписки  точечно
OnDestroy отписка  вручную     → DisposableBag.Dispose  автомат
```

---

# Часть I: Теория

## 1. Что такое реактивное программирование

Реактивное программирование — это парадигма, в которой **данные моделируются как потоки значений во времени**, а логика программы — как **декларативные трансформации этих потоков**.

Математически `IObservable<T>` — это асинхронный аналог `IEnumerable<T>`:



```csharp
                  Одно значение          Много значений
                 ┌──────────────────────┬──────────────────────┐
  Синхронно      │        T             │    IEnumerable<T>    │
                 ├──────────────────────┼──────────────────────┤
  Асинхронно     │      Task<T>         │   IObservable<T>     │
                 └──────────────────────┴──────────────────────┘
```

Каждый `IObservable<T>` посылает своим подписчикам три вида сигналов:



```csharp
OnNext(value)      — новое значение в потоке
OnErrorResume(ex)  — ошибка (в R3 НЕ убивает поток, в отличие от классического Rx)
OnCompleted()      — поток завершён, значений больше не будет
```

### Почему R3, а не UniRx или C# events



```csharp
                   C# events    UniRx       R3
                  ───────────  ─────────   ──────────────────────
Composability         ✗           ✓              ✓
Производительность   ✓✓          ⚠             ✓✓
async/await           ✗          ⚠ (частично)   ✓
Безопасные ошибки    ручная      опасная        ✓ (не убивают поток)
Unity lifecycle       ручная     ✓              ✓✓
Активная поддержка    —          ✗ (заморожен)  ✓ (2024)
ValueTask/Span        ✗          ✗              ✓
```

**Ключевое отличие R3 от UniRx:** в классическом Rx (и UniRx) исключение в `OnNext` завершает поток навсегда. В R3 ошибка обрабатывается через `OnErrorResume` и поток продолжает жить.



```csharp
// UniRx: одна ошибка — поток мёртв
Observable.EveryUpdate()
    .Subscribe(_ => MightThrow()); // NullReferenceException = конец подписки

// R3: ошибка логируется, поток живёт
Observable.EveryUpdate()
    .Subscribe(
        _ => MightThrow(),
        ex => Debug.LogError(ex) // лог и продолжение
    );
```

---

## 2. Observable: горячие и холодные потоки

**Холодный Observable** начинает производить значения только при подписке. Каждый подписчик получает независимую последовательность с самого начала.

**Горячий Observable** существует независимо от подписчиков. Новый подписчик получает только значения, испущенные после момента подписки.



```csharp
// ── ХОЛОДНЫЙ ──────────────────────────────────────────────────────────
// Каждый Subscribe запускает новую последовательность
var cold = Observable.Interval(TimeSpan.FromSeconds(1));

cold.Subscribe(x => Debug.Log($"A: {x}")); // A: 0, A: 1, A: 2 ...
// (через 2 секунды)
cold.Subscribe(x => Debug.Log($"B: {x}")); // B: 0, B: 1 ... (независимо!)

// ── ГОРЯЧИЙ ───────────────────────────────────────────────────────────
// Subject — всегда горячий
var hot = new Subject<int>();

hot.Subscribe(x => Debug.Log($"A: {x}"));
hot.OnNext(1); // A: 1
hot.OnNext(2); // A: 2

hot.Subscribe(x => Debug.Log($"B: {x}")); // B подписывается позже
hot.OnNext(3); // A: 3  B: 3  (B не видел 1 и 2)
```



```csharp
Холодный:  Подписчик A  ──0──1──2──3──4──►
           Подписчик B  ──0──1──2──3──4──►  (своя копия)

Горячий:   Источник     ──1──2──3──4──5──►
           Подписчик A  ──1──2──3──4──5──►  (подписался в начале)
           Подписчик B        ──3──4──5──►  (подписался позже)
```

### Фабричные методы создания Observable



```csharp
// Единственное значение и завершение
Observable.Return(42)

// Последовательность целых чисел
Observable.Range(start: 1, count: 10)

// Тикер с интервалом (0, 1, 2, 3, ...)
Observable.Interval(TimeSpan.FromSeconds(1), UnityTimeProvider.Update)

// Одноразовый таймер
Observable.Timer(TimeSpan.FromSeconds(5), UnityTimeProvider.Update)

// Поток без значений, никогда не завершается
Observable.Never<int>()

// Немедленное завершение без значений
Observable.Empty<int>()

// Ручное создание
Observable.Create<int>(observer =>
{
    observer.OnNext(1);
    observer.OnNext(2);
    observer.OnCompleted();
    return Disposable.Empty; // IDisposable для отписки
})

// Из async-метода
Observable.FromAsync(async ct =>
{
    var data = await LoadDataAsync(ct);
    return data;
})

// Из C# event
Observable.FromEvent<int>(
    h => someObject.OnValueChanged += h,
    h => someObject.OnValueChanged -= h
)

// Наблюдение за обычным свойством (polling каждый Update)
Observable.EveryValueChanged(transform, t => t.position)
```

---

## 3. ReactiveProperty — состояние как поток

`ReactiveProperty<T>` — это хранилище значения, которое **одновременно является Observable**. Текущее значение читается как обычное свойство, изменение автоматически уведомляет всех подписчиков.



```csharp
public class GameState : IDisposable
{
    // Первичное изменяемое состояние
    public ReactiveProperty<int>    Score      { get; } = new(0);
    public ReactiveProperty<int>    Level      { get; } = new(1);
    public ReactiveProperty<bool>   IsPaused   { get; } = new(false);

    // Производное состояние — автоматически обновляется
    public ReadOnlyReactiveProperty<string> ScoreDisplay { get; }
    public ReadOnlyReactiveProperty<bool>   IsHighScore  { get; }

    private const int HighScoreThreshold = 10_000;
    private readonly DisposableBag _bag = new();

    public GameState()
    {
        ScoreDisplay = Score
            .Select(s => $"SCORE: {s:N0}")
            .ToReadOnlyReactiveProperty(initialValue: "SCORE: 0");

        IsHighScore = Score
            .Select(s => s >= HighScoreThreshold)
            .ToReadOnlyReactiveProperty(initialValue: false);

        Score      .AddTo(ref _bag);
        Level      .AddTo(ref _bag);
        IsPaused   .AddTo(ref _bag);
        ScoreDisplay.AddTo(ref _bag);
        IsHighScore .AddTo(ref _bag);
    }

    public void AddScore(int points)
    {
        if (IsPaused.CurrentValue) return;
        Score.Value += points * Level.Value; // читаем как обычное поле
    }

    public void Dispose() => _bag.Dispose();
}
```

**Важно:** `ReactiveProperty<T>` по умолчанию включает `DistinctUntilChanged` — подписчик не получит уведомление если новое значение равно текущему.



```csharp
var prop = new ReactiveProperty<int>(5);
prop.Subscribe(x => Debug.Log(x)); // выведет: 5

prop.Value = 5;  // тихо, значение не изменилось
prop.Value = 10; // выведет: 10
prop.Value = 10; // тихо
prop.Value = 5;  // выведет: 5

// Принудительное уведомление без изменения значения:
prop.ForceNotify();
```

---

## 4. Subject: горячие потоки вручную

Subject — это одновременно `IObservable<T>` и `IObserver<T>`. Внешний код может публиковать в него значения, а другие — подписываться.



```csharp
// ── Subject<T> ──────────────────────────────────────────────────────
// Нет начального значения, нет истории
var subject = new Subject<string>();

subject.Subscribe(msg => Debug.Log($"Got: {msg}"));
subject.OnNext("Hello"); // Got: Hello

// ── BehaviorSubject<T> ──────────────────────────────────────────────
// Хранит последнее значение, новые подписчики получают его сразу
var behavior = new BehaviorSubject<int>(initialValue: 0);

behavior.OnNext(42);
behavior.Subscribe(x => Debug.Log(x)); // сразу выведет: 42
Debug.Log(behavior.Value);             // читаем без подписки: 42

// ── ReplaySubject<T> ────────────────────────────────────────────────
// Буферизует N последних значений, воспроизводит новым подписчикам
var replay = new ReplaySubject<int>(bufferSize: 3);

replay.OnNext(1);
replay.OnNext(2);
replay.OnNext(3);
replay.OnNext(4);
replay.OnNext(5);

// Поздний подписчик получит последние 3: 3, 4, 5
replay.Subscribe(x => Debug.Log(x));
```



```csharp
Тип              Начальное значение    Буфер истории    Применение
──────────────   ──────────────────    ─────────────    ─────────────────────────
Subject<T>             ✗                   0            Event bus, пользователь ввод
BehaviorSubject<T>     ✓ (задаётся)        1            Текущее состояние (≈ ReactiveProperty)
ReplaySubject<T>       ✗                   N            История действий, поздние подписчики
```

**Золотое правило инкапсуляции Subject:**



```csharp
public class WeaponSystem
{
    // Приватный — только этот класс публикует
    private readonly Subject<ShotEvent> _onShot = new();

    // Публичный — только для чтения подписчиками
    public Observable<ShotEvent> OnShot => _onShot;

    public void Fire() => _onShot.OnNext(new ShotEvent(this));
}
```

---

## 5. Управление подписками

Каждый вызов `.Subscribe()` возвращает `IDisposable`. Не вызвать `Dispose()` = утечка памяти и вызовы на уничтоженных объектах.



```csharp
public class EnemyController : MonoBehaviour
{
    // Контейнер всех подписок этого объекта
    private DisposableBag _disposables = new();

    private void Start()
    {
        // Вариант 1: AddTo с ref DisposableBag
        playerModel.Health
            .Subscribe(UpdateThreatLevel)
            .AddTo(ref _disposables);

        // Вариант 2: AddTo с MonoBehaviour (авто-освобождение при уничтожении)
        Observable.Interval(TimeSpan.FromSeconds(1))
            .Subscribe(_ => PatrolStep())
            .AddTo(this);

        // Вариант 3: прямое добавление в bag
        _disposables.Add(someOtherDisposable);
    }

    private void OnDestroy()
    {
        _disposables.Dispose(); // освобождает все сразу
    }
}
```

---

## 6. Интеграция с Unity

### Update и жизненный цикл как Observable



```csharp
using R3;
using R3.Triggers;

public class ReactiveMonoBehaviour : MonoBehaviour
{
    private void Start()
    {
        // Глобальный Update-поток
        Observable.EveryUpdate()
            .Subscribe(_ => GlobalTick());

        // Update только этого объекта
        this.UpdateAsObservable()
            .Where(_ => gameObject.activeInHierarchy)
            .Subscribe(_ => LocalTick())
            .AddTo(this);

        // Физика
        this.FixedUpdateAsObservable()
            .Subscribe(_ => PhysicsTick())
            .AddTo(this);

        // Lifecycle-события
        this.OnEnableAsObservable()
            .Subscribe(_ => OnBecameActive())
            .AddTo(this);

        this.OnTriggerEnterAsObservable()
            .Where(col => col.CompareTag("Enemy"))
            .Subscribe(col => HandleEnemyContact(col))
            .AddTo(this);

        this.OnBecameVisibleAsObservable()
            .Subscribe(_ => EnableRendering(true))
            .AddTo(this);
    }
}
```

### uGUI как Observable



```csharp
using R3;

public class GameUI : MonoBehaviour
{
    [SerializeField] private Button      fireButton;
    [SerializeField] private Slider      volumeSlider;
    [SerializeField] private TMP_InputField searchField;
    [SerializeField] private Toggle      muteToggle;

    private DisposableBag _disposables = new();

    private void Start()
    {
        // Button: ThrottleFirst защищает от двойного нажатия
        fireButton.OnClickAsObservable()
            .ThrottleFirst(TimeSpan.FromSeconds(0.5f), UnityTimeProvider.Update)
            .Subscribe(_ => Fire())
            .AddTo(ref _disposables);

        // Slider: Debounce — не сохранять при каждом пикселе движения
        volumeSlider.OnValueChangedAsObservable()
            .Debounce(TimeSpan.FromMilliseconds(200), UnityTimeProvider.Update)
            .Subscribe(v => AudioManager.SetVolume(v))
            .AddTo(ref _disposables);

        // InputField: поиск с задержкой
        searchField.OnValueChangedAsObservable()
            .Debounce(TimeSpan.FromMilliseconds(350), UnityTimeProvider.UpdateIgnoreTimeScale)
            .DistinctUntilChanged()
            .Where( => .Length == 0 || .Length >= 2)
            .Subscribe( => inventory.Filter())
            .AddTo(ref _disposables);

        // Toggle
        muteToggle.OnValueChangedAsObservable()
            .Subscribe(muted => AudioManager.SetMuted(muted))
            .AddTo(ref _disposables);
    }

    private void OnDestroy() => _disposables.Dispose();
}
```

### UnityTimeProvider — почему важно



```csharp
// ✗ Системное время — не реагирует на Time.timeScale
Observable.Interval(TimeSpan.FromSeconds(1), TimeProvider.System);

// ✓ Игровое время — масштабируется с Time.timeScale
Observable.Interval(TimeSpan.FromSeconds(1), UnityTimeProvider.Update);

// ✓ Реальное время — игнорирует паузу (для UI, таймаутов)
Observable.Interval(TimeSpan.FromSeconds(1), UnityTimeProvider.UpdateIgnoreTimeScale);

// ✓ Физическое время — для FixedUpdate-логики
Observable.Interval(TimeSpan.FromSeconds(0.02f), UnityTimeProvider.FixedUpdate);
```

---

# Часть II: Операторы

## Справочная таблица операторов R3

### Фильтрация

|Оператор|Сигнатура|Описание|Пример применения|
|---|---|---|---|
|`Where`|`Where(T -> bool)`|Пропускает элементы, удовлетворяющие предикату|Стрелять только если `canShoot`|
|`DistinctUntilChanged`|`DistinctUntilChanged()`|Пропускает дубли подряд|Обновлять UI только при реальном изменении|
|`Take`|`Take(int n)`|Берёт первые N элементов|Обработать смерть только один раз|
|`TakeWhile`|`TakeWhile(T -> bool)`|Берёт пока условие истинно|Слушать ввод пока не пауза|
|`Skip`|`Skip(int n)`|Пропустить первые N элементов|Игнорировать начальное значение|
|`SkipWhile`|`SkipWhile(T -> bool)`|Пропускать пока условие истинно|Начать обработку после загрузки|
|`First` / `FirstAsync`|`First()`|Первый элемент и завершение|Ждать первого подключения|
|`Last` / `LastAsync`|`Last()`|Последний элемент завершённого потока|Результат конечной последовательности|

### Трансформация

|Оператор|Сигнатура|Описание|Пример применения|
|---|---|---|---|
|`Select`|`Select(T -> R)`|Преобразует каждый элемент|HP `int` → процент `float`|
|`SelectMany`|`Select(T -> Observable<R>)` + flatten|Для каждого элемента создаёт Observable, все объединяет|Слушать смерть каждого врага|
|`Cast`|`Cast<R>()`|Приводит тип|`object` → конкретный тип|
|`OfType`|`OfType<R>()`|Фильтрует и приводит тип|Из потока событий выбрать нужный тип|
|`Scan`|`Scan(seed, (acc, T) -> acc)`|Накопительная свёртка|Подсчёт очков с нарастающим итогом|

### Объединение

|Оператор|Сигнатура|Описание|Пример применения|
|---|---|---|---|
|`Merge`|`Merge(obs1, obs2, ...)`|Объединяет потоки, элементы в порядке появления|WASD + геймпад в один поток ввода|
|`CombineLatest`|`CombineLatest(obs1, obs2, (a,b)->r)`|При изменении любого — комбинирует последние значения всех|Фильтр инвентаря: текст + тип|
|`Zip`|`Zip(obs1, obs2, (a,b)->r)`|Попарно соединяет элементы по позиции|Матчинг запрос-ответ|
|`WithLatestFrom`|`WithLatestFrom(other, (T, R)->out)`|При элементе из `this` — берёт последнее из `other`|Выстрел + текущее направление|
|`Amb`|`Amb(obs1, obs2)`|Побеждает тот поток, который первым выдаст элемент|Race condition: первый ответивший сервер|

### Время и частота

|Оператор|Сигнатура|Описание|Пример применения|
|---|---|---|---|
|`Debounce`|`Debounce(TimeSpan, TimeProvider)`|Ждёт паузу, испускает последнее|Поиск по тексту, автосохранение|
|`ThrottleFirst`|`ThrottleFirst(TimeSpan, TimeProvider)`|Первый элемент, игнорирует остальные N мс|Ограничить кулдаун выстрела|
|`ThrottleLast`|`ThrottleLast(TimeSpan, TimeProvider)`|Последний элемент за период|Финальное значение слайдера|
|`Sample`|`Sample(TimeSpan, TimeProvider)`|Берёт последнее значение каждые N мс|Снимок состояния раз в секунду|
|`Delay`|`Delay(TimeSpan, TimeProvider)`|Задерживает каждый элемент|Отложенный эффект|
|`Timeout`|`Timeout(TimeSpan, TimeProvider)`|Ошибка если нет значений за период|Таймаут сетевого запроса|
|`Buffer`|`Buffer(TimeSpan / count)`|Собирает элементы в пакеты|DPS за секунду, комбо-атаки|
|`Window`|`Window(TimeSpan / count)`|Как Buffer, но отдаёт Observable вместо списка|Скользящее окно событий|

### Переключение потоков

|Оператор|Сигнатура|Описание|Пример применения|
|---|---|---|---|
|`Switch`|На `Observable<Observable<T>>`|Отписывается от предыдущего, подписывается на новый|Поиск: новый запрос отменяет старый|
|`Catch`|`Catch<TException>(ex -> Observable<T>)`|Обрабатывает ошибку, возвращает альтернативу|Fallback на кэш при сетевой ошибке|
|`Retry`|`Retry(int count)`|Повторяет подписку при ошибке|Retry сетевого запроса N раз|
|`Finally`|`Finally(Action)`|Выполняется при завершении или ошибке|Скрыть спиннер загрузки|
|`OnErrorResume`|`OnErrorResume(Exception -> Observable<T>)`|Продолжает поток после ошибки|Логировать и продолжать|

### Утилиты

|Оператор|Сигнатура|Описание|Пример применения|
|---|---|---|---|
|`Do`|`Do(T -> void)`|Побочный эффект без изменения потока|Лог для дебага|
|`StartWith`|`StartWith(T value)`|Добавляет значение в начало|Начальное значение для CombineLatest|
|`Prepend`|`Prepend(T value)`|Синоним StartWith|—|
|`Append`|`Append(T value)`|Добавляет значение в конец|—|
|`DefaultIfEmpty`|`DefaultIfEmpty(T value)`|Если поток пуст — вернуть значение по умолчанию|Fallback значение|
|`Share`|`Share()`|Multicast: один источник, много подписчиков|Разделить дорогой Observable|
|`Publish`|`Publish()`|Ручной multicast с Connect()|Контролируемый запуск потока|

---

## Детальные примеры ключевых операторов

### Debounce vs ThrottleFirst: визуально



```csharp
Нажатия:      ──●─●─●───────●─●──────────●───────────►
              t1 t2 t3      t4 t5        t6

Debounce(1s): ──────────────────●─────────────●────────►
              (ждёт паузу 1с, испускает ПОСЛЕДНЕЕ: t3, t5)

ThrottleFirst(1s): ──●─────────────●──────────●────────►
              (первый, потом 1с тишина: t1, t4, t6)

ThrottleLast(1s):  ────────────────●──────────────●─────►
              (последнее за каждые 1с: t3 после первой 1с, t5 после второй)
```



```csharp
// Debounce: поиск — запрос только после паузы в вводе
searchField.OnValueChangedAsObservable()
    .Debounce(TimeSpan.FromMilliseconds(300), UnityTimeProvider.Update)
    .Subscribe( => Search());

// ThrottleFirst: кулдаун выстрела — первый выстрел проходит, остальные игнорируются
fireButton.OnClickAsObservable()
    .ThrottleFirst(TimeSpan.FromSeconds(0.5f), UnityTimeProvider.Update)
    .Subscribe(_ => Shoot());

// ThrottleLast: громкость — применяем только конечное положение слайдера
volumeSlider.OnValueChangedAsObservable()
    .ThrottleLast(TimeSpan.FromMilliseconds(100), UnityTimeProvider.Update)
    .Subscribe(v => ApplyVolume(v));
```

### CombineLatest: реактивный фильтр



```csharp
// Три независимых фильтра, работающих одновременно
var search  = searchField.OnValueChangedAsObservable().StartWith("");
var itemType    = typeDropdown.OnValueChangedAsObservable().StartWith(0);
var minRarity   = raritySlider.OnValueChangedAsObservable().StartWith(1f);

Observable.CombineLatest(search, itemType, minRarity,
    (, type, rarity) => (, type, (int)rarity))
    .Debounce(TimeSpan.FromMilliseconds(150), UnityTimeProvider.Update)
    .Subscribe(filters => ApplyFilters(filters., filters.type, filters.rarity))
    .AddTo(this);
```



```csharp
search:  ──"sw"──────────────"sword"──────────────────►
itemType:    ────────Weapon───────────────────────────────►
minRarity:   ─────────────────────────────3───────────────►
             ↓         ↓                   ↓
CombineLatest:──("sw",All,1)──("sw",Weapon,1)──("sword",Weapon,3)►
             ↓
Debounce:  ────────────────(применяем)──────────────(применяем)──►
```

### Switch: отмена предыдущего запроса



```csharp
// Каждый новый поисковый запрос отменяет предыдущий
searchField.OnValueChangedAsObservable()
    .Debounce(TimeSpan.FromMilliseconds(300), UnityTimeProvider.Update)
    .Select(query =>
        // Каждый запрос — новый Observable
        Observable.FromAsync(ct => SearchAPI(query, ct)))
    .Switch() // подписываемся только на ПОСЛЕДНИЙ Observable
    .Subscribe(
        results => ShowResults(results),
        error   => Debug.LogError(error)
    )
    .AddTo(this);
```

### Buffer: статистика и комбо



```csharp
// FPS-счётчик через Buffer
Observable.EveryUpdate()
    .Buffer(TimeSpan.FromSeconds(1f), UnityTimeProvider.Update)
    .Select(frames => frames.Count)
    .Subscribe(fps => fps. = $"FPS: {fps}")
    .AddTo(this);

// Комбо-атаки: удары за скользящее окно
attackInput.OnAttack
    .Buffer(TimeSpan.FromSeconds(1f), UnityTimeProvider.Update)
    .Where(hits => hits.Count > 0)
    .Select(hits => hits.Count)
    .Subscribe(comboCount =>
    {
        combo. = comboCount > 1 ? $"COMBO x{comboCount}!" : "";
    })
    .AddTo(this);
```

### Scan: накопительный счёт



```csharp
// Scan — как Aggregate, но выдаёт каждый промежуточный результат
enemyKillStream
    .Select(enemy => enemy.PointValue)
    .Scan(seed: 0, (total, points) => total + points)
    .Subscribe(totalScore => score. = $"{totalScore:N0}")
    .AddTo(this);

// Цепочка: убийство → очки с множителем уровня → накопление → UI
enemyKillStream
    .Select(enemy => enemy.BasePoints)
    .WithLatestFrom(levelStream, (points, level) => points * level)
    .Scan(0, (total, pts) => total + pts)
    .Select(score => $"SCORE: {score:N0}")
    .Subscribe( => score. = )
    .AddTo(this);
```

---

# Часть III: Практика

## Уровень 1 — Базовый: Система здоровья

**Задача:** реализовать `PlayerHealth` с `ReactiveProperty<int>` и `HealthView` с реактивной привязкой UI.

**Стартовый код:**



```csharp
// PlayerHealth.cs — заготовка
public class PlayerHealth : IDisposable
{
    // TODO 1: ReactiveProperty<int> CurrentHP (начальное = maxHP)
    // TODO 2: ReadOnlyReactiveProperty<float> HealthPercent
    // TODO 3: ReadOnlyReactiveProperty<bool> IsDead
    // TODO 4: ReadOnlyReactiveProperty<HealthStatus> Status
    
    private readonly Subject<int> _onDamageTaken = new();
    public Observable<int> OnDamageTaken => _onDamageTaken;
    
    public int MaxHP { get; }
    private readonly DisposableBag _disposables = new();

    public PlayerHealth(int maxHP = 100) { /* TODO */ }
    
    public void TakeDamage(int amount) { /* TODO */ }
    public void Heal(int amount)       { /* TODO */ }
    public void Revive(int hp)         { /* TODO */ }
    public void Dispose()              { /* TODO */ }
}
```



```csharp
// HealthView.cs — заготовка
public class HealthView : MonoBehaviour
{
    [SerializeField] private Slider     hpSlider;
    [SerializeField] private Image      hpFill;
    [SerializeField] private TMP_   hp;
    [SerializeField] private GameObject deathPanel;
    [SerializeField] private GameObject lowHpWarning;
    [SerializeField] private AudioSource damageAudio;

    private DisposableBag _disposables = new();

    public void Bind(PlayerHealth model)
    {
        // TODO A: hpSlider.value ← model.HealthPercent
        // TODO B: hpFill.color ← model.HealthPercent (красный→жёлтый→зелёный)
        // TODO C: hp. ← "{hp} / {maxHP}"
        // TODO D: deathPanel.SetActive ← model.IsDead
        // TODO E: lowHpWarning — HealthPercent < 0.3 и > 0
        // TODO F: damageAudio.Play() ← OnDamageTaken, ThrottleFirst 200ms
    }

    private void OnDestroy() => _disposables.Dispose();
}
```

**Критерии:**



```csharp
✓ CurrentHP — ReactiveProperty, не поле с event
✓ IsDead — ReadOnlyReactiveProperty, не флаг bool
✓ HealthView не имеет метода Update()
✓ deathPanel активируется через Subscribe, не через if в TakeDamage
✓ Дебаунс звука — через ThrottleFirst, не через Time.time
✓ При Dispose() все подписки освобождены
```

**Типичные ошибки:**



```csharp
// ✗ Обычное поле вместо ReactiveProperty
private int _currentHP; // нельзя подписаться

// ✗ Проверка в Update вместо Subscribe
private void Update()
{
    if (_model.IsDead.CurrentValue) // каждый кадр
        deathPanel.SetActive(true);
}

// ✗ Подписка без AddTo
model.HealthPercent.Subscribe(p => slider.value = p); // утечка памяти

// ✗ Бесконечный сброс при Revive
public void Revive(int hp)
{
    _isDead = false;          // флаг был, его нет
    _deathFired = false;      // ещё флаг, которого нет
    CurrentHP.Value = hp;     // IsDead автоматически станет false
}
```

---

## Уровень 2 — Средний: Комбо-атаки

**Задача:** система, которая считает комбо если между ударами не более 1 секунды, реактивно показывает счётчик и название комбо.

**Стартовый код:**



```csharp
public class ComboSystem : IDisposable
{
    public const float ComboWindowSeconds = 1f;

    public ReadOnlyReactiveProperty<ComboData> CurrentCombo  { get; private set; }
    public ReadOnlyReactiveProperty<bool>       IsComboActive { get; private set; }
    public Observable<ComboData> OnComboFinished { get; private set; }

    private readonly DisposableBag _disposables = new();

    // Подход А: Buffer
    public static ComboSystem CreateWithBuffer(Observable<Unit> attacks)
    {
        var sys = new ComboSystem();
        // TODO A1: attacks.Buffer(ComboWindowSeconds).Where(!empty).Select(count)
        // TODO A2: CurrentCombo = comboCount.Select(n => new ComboData(n))
        // TODO A3: IsComboActive = comboCount.Select(n => n > 1)
        // TODO A4: OnComboFinished = comboCount.Where(n > 1).Select(new ComboData)
        return sys;
    }

    // Подход Б: Накопительный счётчик + Debounce-сброс
    public static ComboSystem CreateWithAccumulator(Observable<Unit> attacks)
    {
        var sys = new ComboSystem();
        // TODO B1: var counter = new ReactiveProperty<int>(0)
        // TODO B2: attacks.Subscribe(_ => counter.Value++)
        // TODO B3: attacks.Debounce(1s) -> если counter > 1, OnComboFinished -> counter = 0
        // TODO B4: CurrentCombo = counter.Select(n => new ComboData(n))
        // TODO B5: IsComboActive = counter.Select(n => n > 1)
        return sys;
    }

    public void Dispose() => _disposables.Dispose();
}
```

**Критерии:**



```csharp
✓ Комбо сбрасывается при паузе > 1 секунды
✓ Оба подхода реализованы и сравнены
✓ OnComboFinished срабатывает до сброса счётчика
✓ UI обновляется реактивно, нет Update()
✓ UnityTimeProvider.Update использован везде (не TimeProvider.System)
```

**Типичные ошибки:**



```csharp
// ✗ Системное время вместо игрового
attacks.Debounce(TimeSpan.FromSeconds(1f), TimeProvider.System);
// При паузе игры (timeScale=0) сброс всё равно произойдёт

// ✗ Вложенная подписка — утечка
attacks.Subscribe(_ =>
{
    attacks.Debounce(...).Subscribe(_ => counter.Value = 0); // новая подписка каждый удар!
});

// ✗ Buffer без фильтра пустых буферов
attacks.Buffer(TimeSpan.FromSeconds(1f), UnityTimeProvider.Update)
    .Select(b => b.Count) // спамит нулями каждую секунду в тишине
    .Subscribe(...);

// ✗ Сброс ДО публикации события
counter.Value = 0;                          // сбросили
onFinished.OnNext(new ComboData(counter.Value)); // Count = 0!
```

---

## Уровень 3 — Продвинутый: Поиск по инвентарю

**Задача:** фильтрация списка предметов с Debounce на текстовый поиск и CombineLatest с фильтром по типу.

**Стартовый код:**



```csharp
public class InventoryFilter : IDisposable
{
    public static readonly TimeSpan SearchDebounce = TimeSpan.FromMilliseconds(300);

    // TODO 1: ReactiveProperty<string> Search = new("")
    // TODO 2: ReactiveProperty<ItemType> SelectedType = new(ItemType.All)
    // TODO 3: ReadOnlyReactiveProperty<List<InventoryItem>> FilteredItems
    // TODO 4: ReadOnlyReactiveProperty<int> TotalFound
    // TODO 5: ReadOnlyReactiveProperty<bool> IsSearching
    // TODO 6: ReadOnlyReactiveProperty<string> SearchSummary

    private readonly List<InventoryItem> _allItems;
    private readonly DisposableBag _disposables = new();

    public InventoryFilter(List<InventoryItem> allItems)
    {
        _allItems = allItems;

        // TODO 7: var debouncedSearch = Search.Debounce(...).StartWith("").DistinctUntilChanged()
        // TODO 8: var typeStream = SelectedType.DistinctUntilChanged()
        // TODO 9: FilteredItems = CombineLatest(debouncedSearch, typeStream, ApplyFilters)
        // TODO 10: TotalFound = FilteredItems.Select(list => list.Count)
        // TODO 11: IsSearching = CombineLatest(Search, SelectedType, (t,ty) => t!="" || ty!=All)
        // TODO 12: SearchSummary = CombineLatest(TotalFound, IsSearching, формат строки)
    }

    private List<InventoryItem> ApplyFilters(string , ItemType type)
    {
        var q = _allItems.AsEnumerable();
        if (type != ItemType.All)
            q = q.Where(i => i.Type == type);
        if (!string.IsNullOrWhiteSpace())
        {
            var low = .ToLowerInvariant();
            q = q.Where(i => i.Name.ToLowerInvariant().Contains(low));
        }
        return q.ToList();
    }

    public void Dispose() => _disposables.Dispose();
}
```

**Критерии:**



```csharp
✓ Фильтрация НЕ срабатывает при каждом символе (Debounce работает)
✓ StartWith("") в debouncedSearch — список виден сразу при открытии
✓ IsSearching использует Search без Debounce (спиннер появляется мгновенно)
✓ Оба фильтра работают одновременно через CombineLatest
✓ SearchSummary показывает корректные числа
✓ При очистке поиска список возвращается к полному
```

**Типичные ошибки:**



```csharp
// ✗ Забыт StartWith — список не отображается до первого ввода
var debouncedSearch = Search
    .Debounce(SearchDebounce, UnityTimeProvider.Update);
    // CombineLatest ждёт значения от ОБОИХ потоков
    // debouncedSearch не выдаст значение пока пользователь не начнёт вводить

// ✗ IsSearching через debounced поток — спиннер появляется с задержкой 300мс
IsSearching = Observable.CombineLatest(
    Search.Debounce(SearchDebounce, UnityTimeProvider.Update), // НЕТ
    SelectedType, ...);

// ✗ Бесконечный цикл при двусторонней привязке InputField
inputField.OnValueChangedAsObservable()
    .Subscribe( => filter.Search.Value = );
filter.Search
    .Subscribe( => inputField. = ); // -> OnValueChanged -> Search -> ...

// ✓ Правильно: SetWithoutNotify + Where-защита
filter.Search
    .Where( =>  != inputField.)
    .Subscribe( => inputField.SetWithoutNotify());
```

---

# Часть IV: Когда НЕ нужен R3

Реактивное программирование — мощный инструмент, но не серебряная пуля. Вот ситуации, когда традиционный подход лучше.

## Простые одноразовые проверки



```csharp
// ✗ Избыточно: Observable ради одной строки
Observable.EveryUpdate()
    .Where(_ => Input.GetKeyDown(KeyCode.Escape))
    .Subscribe(_ => PauseMenu.Toggle())
    .AddTo(this);

// ✓ Достаточно: прямая проверка в Update
private void Update()
{
    if (Input.GetKeyDown(KeyCode.Escape))
        PauseMenu.Toggle();
}
```

## Линейная последовательность без ветвлений



```csharp
// ✗ Искусственное усложнение
Observable.Return(enemyData)
    .Select(data => new Enemy(data))
    .Select(enemy => InitializeEnemy(enemy))
    .Subscribe(enemy => SpawnEnemy(enemy));

// ✓ Прямой код читается лучше
var enemy = new Enemy(enemyData);
InitializeEnemy(enemy);
SpawnEnemy(enemy);
```

## Высокочастотная физика без composability



```csharp
// ✗ Observable в FixedUpdate каждые 0.02с с созданием лямбд
this.FixedUpdateAsObservable()
    .Select(_ => rigidbody.velocity)
    .Subscribe(v => ApplyDrag(v))
    .AddTo(this);

// ✓ Прямой FixedUpdate без аллокаций
private void FixedUpdate()
{
    ApplyDrag(rigidbody.velocity);
}
```

## Командная работа с незнакомой технологией



```csharp
Если больше половины команды не знает Rx —
R3 превращается в барьер для code review и онбординга.
Введите R3 постепенно, начиная с изолированных модулей.
```

## Простые конечные автоматы



```csharp
// ✗ Реактивный конечный автомат с множеством Subject и переходов
// быстро становится нечитаемым

// ✓ Для простых FSM: enum + switch или паттерн State
private EnemyState _state = EnemyState.Patrol;

private void Update()
{
    _state = _state switch
    {
        EnemyState.Patrol  => UpdatePatrol(),
        EnemyState.Chase   => UpdateChase(),
        EnemyState.Attack  => UpdateAttack(),
        _                  => _state
    };
}
```

## Правило принятия решения



```csharp
Добавляет ли R3 реальную ценность в этом случае?
                    │
        ┌───────────┴───────────┐
       ДА                      НЕТ
        │                       │
  Нужна ли composability?    Используй
  (фильтрация, объединение,  традиционный
   временные операторы)       подход
        │
  ┌─────┴─────┐
 ДА          НЕТ
  │            │
Нужна ли    Нужно ли
реактивная  управлять
привязка    асинхрон-
данных?     ностью?
  │            │
 ДА           ДА
  │            │
  └────┬───────┘
       │
  Используй R3
```

---

# Часть V: Чеклист

## Архитектура



```csharp
□ Модель данных не зависит от MonoBehaviour
  └─ PlayerHealth, GameState и т.д. — чистые C# классы с IDisposable

□ Subject инкапсулированы: приватный Subject, публичный Observable
  └─ private Subject<T> _subject; public Observable<T> OnEvent => _subject;

□ ReactiveProperty для первичного состояния
  └─ ReadOnlyReactiveProperty для производного (через Select + ToReadOnlyReactiveProperty)

□ View-слой содержит только подписки и обновления UI
  └─ Никакой бизнес-логики в Subscribe, только присвоение значений UI
```

## Управление памятью



```csharp
□ Каждый Subscribe завершается .AddTo(ref _disposables) или .AddTo(this)
□ DisposableBag объявлен на уровне класса, не метода
□ OnDestroy вызывает _disposables.Dispose()
□ Все ReactiveProperty добавлены в DisposableBag через .AddTo(ref _disposables)
□ Subject явно освобождается в Dispose()
□ Нет Subscribe внутри Subscribe (вложенных подписок)
□ Нет создания Observable внутри Update()
```

## Правильное использование операторов



```csharp
□ Debounce использует UnityTimeProvider, не TimeProvider.System
□ ThrottleFirst/Debounce для ограничения частоты (не Time.time вручную)
□ DistinctUntilChanged перед дорогими операциями (UI, сеть)
□ CombineLatest: все потоки имеют StartWith или начальное значение
□ Switch используется для отмены предыдущих запросов (поиск, загрузка)
□ Buffer фильтрует пустые буферы через .Where(b => b.Count > 0)
```

## Качество кода



```csharp
□ Нет if-проверок флагов в Subscribe (логика в Where перед Subscribe)
□ Нет ручного управления состоянием (_isDead, _wasLowHp и т.д.)
□ Нет Update() в View-слое
□ Do() используется только для логирования/дебага, не для логики
□ Цепочки операторов форматированы вертикально для читаемости
□ Комментарии объясняют "почему", не "что"
```

## Код-ревью: красные флаги



```csharp
⛳ ReactiveProperty без AddTo в конструкторе
⛳ Subscribe без AddTo или AddTo(this)
⛳ TimeProvider.System в операторах времени
⛳ Логика в Subscribe вместо Where/Select
⛳ Subject.OnNext() вызывается из внешнего кода (не инкапсулирован)
⛳ new Observable/new Subject внутри метода Update()
⛳ CombineLatest без StartWith (список не появляется сразу)
⛳ Вложенный Subscribe (утечка подписок)
⛳ SetActive//value вычисляются в Select (должно быть в Subscribe)
```

---

# Ресурсы

## Официальная документация

|Ресурс|Описание|
|---|---|
|[github.com/Cysharp/R3](https://github.com/Cysharp/R3)|Репозиторий R3, README с полным API|
|[R3 Wiki](https://github.com/Cysharp/R3/wiki)|Официальная Wiki с примерами|
|[Rx.NET Documentation](https://learn.microsoft.com/en-us/previous-versions/dotnet/reactive-extensions/hh242985\(v=vs.103\))|Основы Rx, применимы к R3|

## Интерактивное обучение

|Ресурс|Описание|
|---|---|
|[RxMarbles](https://rxmarbles.com/)|Интерактивные диаграммы операторов|
|[ReactiveX Operators](https://reactivex.io/documentation/operators.html)|Полный справочник операторов Rx|
|[LearnRxJS](https://www.learnrxjs.io/)|Примеры на RxJS (концепции идентичны R3)|

## Смежные библиотеки Cysharp

|Библиотека|Описание|
|---|---|
|[UniTask](https://github.com/Cysharp/UniTask)|async/await для Unity, интегрируется с R3|
|[MessagePipe](https://github.com/Cysharp/MessagePipe)|Высокопроизводительный event bus, совместим с R3|
|[ZLogger](https://github.com/Cysharp/ZLogger)|Zero-allocation логгер от того же автора|

## Книги и статьи

|Ресурс|Описание|
|---|---|
|_"Reactive Programming with RxJava"_ — Nurkiewicz, Christensen|Лучшая книга по концепциям Rx (Java, но принципы универсальны)|
|_"Introduction to Rx"_ — Lee Campbell|Бесплатная онлайн-книга по Rx.NET|
|[Andre Staltz — Introduction to Reactive Programming](https://gist.github.com/staltz/868e7e9bc2a7b8c1f754)|Классическое введение в реактивный подход|

## Установка R3 в Unity



```csharp
// Вариант 1: Package Manager → Add package by git URL
https://github.com/Cysharp/R3.git?path=src/R3.Unity/Assets/R3.Unity

// Вариант 2: OpenUPM (рекомендуется)
openupm add com.cysharp.r3

// Вариант 3: Добавить в Packages/manifest.json
{
  "dependencies": {
    "com.cysharp.r3": "1.x.x"
  },
  "scopedRegistries": [
    {
      "name": "OpenUPM",
      "url": "https://package.openupm.com",
      "scopes": ["com.cysharp"]
    }
  ]
}
```

---

## Быстрый старт: минимальный рабочий пример



```csharp
// Установили R3 → создали скрипт → прикрепили к GameObject → запустили сцену
using R3;
using R3.Triggers;
using UnityEngine;

public class QuickStart : MonoBehaviour
{
    private void Start()
    {
        // Реактивное свойство
        var score = new ReactiveProperty<int>(0);

        // Подписка с автоуправлением через AddTo(this)
        score
            .Select(s => $"Score: {s}")
            .Subscribe( => Debug.Log())
            .AddTo(this);

        // Изменение значения — подписчики оповещены автоматически
        score.Value = 10;  // Score: 10
        score.Value = 20;  // Score: 20

        // Update через Observable
        this.UpdateAsObservable()
            .Where(_ => Input.GetKeyDown(KeyCode.Space))
            .Subscribe(_ => score.Value += 5)
            .AddTo(this);

        // Тикер раз в 2 секунды
        Observable.Interval(
                TimeSpan.FromSeconds(2f),
                UnityTimeProvider.Update)
            .Subscribe(tick => Debug.Log($"Tick #{tick}"))
            .AddTo(this);
    }
    // OnDestroy не нужен: AddTo(this) позаботится о подписках
}
```

---

_R3 — это не просто библиотека, это способ думать о данных как о потоках. Начните с одного `ReactiveProperty` вместо флага, добавьте один `Subscribe` вместо `Update`-проверки — и почувствуйте разницу. Остальное придёт с практикой_