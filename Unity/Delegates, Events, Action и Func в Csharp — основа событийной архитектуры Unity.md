## Содержание

- [Введение](#%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5)
	- [Почему события критичны в Unity?](#%D0%9F%D0%BE%D1%87%D0%B5%D0%BC%D1%83%20%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D1%8B%20%D0%B2%20Unity?)
- [Delegate — основа](#Delegate%20%E2%80%94%20%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%B0)
	- [Что такое делегат?](#%D0%A7%D1%82%D0%BE%20%D1%82%D0%B0%D0%BA%D0%BE%D0%B5%20%D0%B4%D0%B5%D0%BB%D0%B5%D0%B3%D0%B0%D1%82?)
	- [Синтаксис объявления](#%D0%A1%D0%B8%D0%BD%D1%82%D0%B0%D0%BA%D1%81%D0%B8%D1%81%20%D0%BE%D0%B1%D1%8A%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F)
	- [Подписка на делегат](#%D0%9F%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%BA%D0%B0%20%D0%BD%D0%B0%20%D0%B4%D0%B5%D0%BB%D0%B5%D0%B3%D0%B0%D1%82)
	- [Альтернативные способы работы с делегатами](#%D0%90%D0%BB%D1%8C%D1%82%D0%B5%D1%80%D0%BD%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D1%8B%D0%B5%20%D1%81%D0%BF%D0%BE%D1%81%D0%BE%D0%B1%D1%8B%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B%20%D1%81%20%D0%B4%D0%B5%D0%BB%D0%B5%D0%B3%D0%B0%D1%82%D0%B0%D0%BC%D0%B8)
	- [Проверка подписчиков](#%D0%9F%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0%20%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D1%87%D0%B8%D0%BA%D0%BE%D0%B2)
- [Multicast Delegate](#Multicast%20Delegate)
	- [Принцип работы](#%D0%9F%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B)
	- [Множественная подписка](#%D0%9C%D0%BD%D0%BE%D0%B6%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F%20%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%BA%D0%B0)
	- [Порядок выполнения](#%D0%9F%D0%BE%D1%80%D1%8F%D0%B4%D0%BE%D0%BA%20%D0%B2%D1%8B%D0%BF%D0%BE%D0%BB%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F)
	- [Возвращаемые значения и multicast](#%D0%92%D0%BE%D0%B7%D0%B2%D1%80%D0%B0%D1%89%D0%B0%D0%B5%D0%BC%D1%8B%D0%B5%20%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B8%20multicast)
- [Event — безопасность и инкапсуляция](#Event%20%E2%80%94%20%D0%B1%D0%B5%D0%B7%D0%BE%D0%BF%D0%B0%D1%81%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%B8%20%D0%B8%D0%BD%D0%BA%D0%B0%D0%BF%D1%81%D1%83%D0%BB%D1%8F%D1%86%D0%B8%D1%8F)
	- [Проблема обычных делегатов](#%D0%9F%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0%20%D0%BE%D0%B1%D1%8B%D1%87%D0%BD%D1%8B%D1%85%20%D0%B4%D0%B5%D0%BB%D0%B5%D0%B3%D0%B0%D1%82%D0%BE%D0%B2)
	- [Event решает проблему](#Event%20%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D1%82%20%D0%BF%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D1%83)
	- [Синтаксис событий](#%D0%A1%D0%B8%D0%BD%D1%82%D0%B0%D0%BA%D1%81%D0%B8%D1%81%20%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9)
	- [Продвинутые возможности событий](#%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%BD%D1%83%D1%82%D1%8B%D0%B5%20%D0%B2%D0%BE%D0%B7%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9)
	- [События vs делегаты — сводная таблица](#%D0%A1%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F%20vs%20%D0%B4%D0%B5%D0%BB%D0%B5%D0%B3%D0%B0%D1%82%D1%8B%20%E2%80%94%20%D1%81%D0%B2%D0%BE%D0%B4%D0%BD%D0%B0%D1%8F%20%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0)
- [Action и Func](#Action%20%D0%B8%20Func)
	- [Зачем нужны Action и Func?](#%D0%97%D0%B0%D1%87%D0%B5%D0%BC%20%D0%BD%D1%83%D0%B6%D0%BD%D1%8B%20Action%20%D0%B8%20Func?)
	- [Action — для методов без возвращаемого значения](#Action%20%E2%80%94%20%D0%B4%D0%BB%D1%8F%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D0%BE%D0%B2%20%D0%B1%D0%B5%D0%B7%20%D0%B2%D0%BE%D0%B7%D0%B2%D1%80%D0%B0%D1%89%D0%B0%D0%B5%D0%BC%D0%BE%D0%B3%D0%BE%20%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D1%8F)
	- [Func — для методов с возвращаемым значением](#Func%20%E2%80%94%20%D0%B4%D0%BB%D1%8F%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D0%BE%D0%B2%20%D1%81%20%D0%B2%D0%BE%D0%B7%D0%B2%D1%80%D0%B0%D1%89%D0%B0%D0%B5%D0%BC%D1%8B%D0%BC%20%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%D0%BC)
	- [Практический пример с Action/Func в игре](#%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%20%D1%81%20Action/Func%20%D0%B2%20%D0%B8%D0%B3%D1%80%D0%B5)
- [Паттерн Observer](#%D0%9F%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%20Observer)
	- [Классическая реализация Observer](#%D0%9A%D0%BB%D0%B0%D1%81%D1%81%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F%20%D1%80%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20Observer)
	- [Современная реализация через события](#%D0%A1%D0%BE%D0%B2%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F)
	- [Сложный пример: система достижений](#%D0%A1%D0%BB%D0%BE%D0%B6%D0%BD%D1%8B%D0%B9%20%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80:%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D0%B4%D0%BE%D1%81%D1%82%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9)
	- [ScriptableObject как канал событий](#ScriptableObject%20%D0%BA%D0%B0%D0%BA%20%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB%20%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9)
- [Утечки памяти и отписка](#%D0%A3%D1%82%D0%B5%D1%87%D0%BA%D0%B8%20%D0%BF%D0%B0%D0%BC%D1%8F%D1%82%D0%B8%20%D0%B8%20%D0%BE%D1%82%D0%BF%D0%B8%D1%81%D0%BA%D0%B0)
	- [Почему важна отписка](#%D0%9F%D0%BE%D1%87%D0%B5%D0%BC%D1%83%20%D0%B2%D0%B0%D0%B6%D0%BD%D0%B0%20%D0%BE%D1%82%D0%BF%D0%B8%D1%81%D0%BA%D0%B0)
	- [Правильные паттерны отписки](#%D0%9F%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%D1%8B%20%D0%BE%D1%82%D0%BF%D0%B8%D1%81%D0%BA%D0%B8)
	- [Отладка утечек событий](#%D0%9E%D1%82%D0%BB%D0%B0%D0%B4%D0%BA%D0%B0%20%D1%83%D1%82%D0%B5%D1%87%D0%B5%D0%BA%20%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9)
	- [Сводная таблица паттернов отписки](#%D0%A1%D0%B2%D0%BE%D0%B4%D0%BD%D0%B0%D1%8F%20%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0%20%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%D0%BE%D0%B2%20%D0%BE%D1%82%D0%BF%D0%B8%D1%81%D0%BA%D0%B8)
- [Практическое задание](#%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5)
	- [Структура проекта](#%D0%A1%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
	- [Шаг 1: EventBus — центральная шина событий](#%D0%A8%D0%B0%D0%B3%201:%20EventBus%20%E2%80%94%20%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%88%D0%B8%D0%BD%D0%B0%20%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9)
	- [Шаг 2: PlayerHealth — источник событий](#%D0%A8%D0%B0%D0%B3%202:%20PlayerHealth%20%E2%80%94%20%D0%B8%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%20%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9)
	- [Шаг 3: GameManager — подписчик события](#%D0%A8%D0%B0%D0%B3%203:%20GameManager%20%E2%80%94%20%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D1%87%D0%B8%D0%BA%20%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F)
	- [Шаг 4: GameOverUI — подписчик в UI](#%D0%A8%D0%B0%D0%B3%204:%20GameOverUI%20%E2%80%94%20%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D1%87%D0%B8%D0%BA%20%D0%B2%20UI)
	- [Шаг 5: PlayerHealthUI — полоска здоровья](#%D0%A8%D0%B0%D0%B3%205:%20PlayerHealthUI%20%E2%80%94%20%D0%BF%D0%BE%D0%BB%D0%BE%D1%81%D0%BA%D0%B0%20%D0%B7%D0%B4%D0%BE%D1%80%D0%BE%D0%B2%D1%8C%D1%8F)
	- [Шаг 6: AudioEventHandler — звук через события](#%D0%A8%D0%B0%D0%B3%206:%20AudioEventHandler%20%E2%80%94%20%D0%B7%D0%B2%D1%83%D0%BA%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F)
	- [Шаг 7: EventBusDemo — финальная демонстрация](#%D0%A8%D0%B0%D0%B3%207:%20EventBusDemo%20%E2%80%94%20%D1%84%D0%B8%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%B4%D0%B5%D0%BC%D0%BE%D0%BD%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F)
	- [Ожидаемый вывод в консоли Unity](#%D0%9E%D0%B6%D0%B8%D0%B4%D0%B0%D0%B5%D0%BC%D1%8B%D0%B9%20%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%20%D0%B2%20%D0%BA%D0%BE%D0%BD%D1%81%D0%BE%D0%BB%D0%B8%20Unity)
- [Проверь себя](#%D0%9F%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D1%8C%20%D1%81%D0%B5%D0%B1%D1%8F)
	- [🟢 Базовый уровень](#%F0%9F%9F%A2%20%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B9%20%D1%83%D1%80%D0%BE%D0%B2%D0%B5%D0%BD%D1%8C)
	- [🟡 Средний уровень](#%F0%9F%9F%A1%20%D0%A1%D1%80%D0%B5%D0%B4%D0%BD%D0%B8%D0%B9%20%D1%83%D1%80%D0%BE%D0%B2%D0%B5%D0%BD%D1%8C)
	- [🔴 Продвинутый уровень](#%F0%9F%94%B4%20%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%BD%D1%83%D1%82%D1%8B%D0%B9%20%D1%83%D1%80%D0%BE%D0%B2%D0%B5%D0%BD%D1%8C)
- [Итоги](#%D0%98%D1%82%D0%BE%D0%B3%D0%B8)
	- [Что изучить дальше?](#%D0%A7%D1%82%D0%BE%20%D0%B8%D0%B7%D1%83%D1%87%D0%B8%D1%82%D1%8C%20%D0%B4%D0%B0%D0%BB%D1%8C%D1%88%D0%B5?)


---

## Введение

Представь ситуацию: игрок умирает. Что должно произойти в игре?



```csharp
❌ Жёсткие связи (плохо):
Player.Die() {
    UIManager.ShowGameOverScreen();
    AudioManager.PlayDeathSound();
    GameManager.SaveHighScore();
    CameraController.StartDeathAnimation();
    AchievementSystem.UnlockDeathAchievement();
    // Добавил новую систему? Иди в Player.Die() и меняй...
}
```

Проблемы этого подхода:

1. **Player знает обо всех системах** — нарушение инкапсуляции
2. **Жёсткие зависимости** — сложно тестировать и модифицировать
3. **Каждая новая система** требует изменения кода Player
4. **Невозможно отключить** отдельную систему без изменения Player



```csharp
✅ Событийная архитектура (хорошо):
Player.Die() {
    OnPlayerDied?.Invoke();  // Просто уведомляем, что игрок умер
}

// Отдельные системы сами решают, как реагировать:
UIManager      подписался на OnPlayerDied → показывает Game Over
AudioManager   подписался на OnPlayerDied → проигрывает звук смерти
GameManager    подписался на OnPlayerDied → сохраняет результат
```

### Почему события критичны в Unity?

|Сценарий|Без событий|С событиями|
|---|---|---|
|Сбор монеты|Player знает об UI и Sound|Coin уведомляет → кто хочет, реагирует|
|Уровень пройден|LevelManager знает обо всех системах|LevelManager уведомляет → системы сами решают|
|Взрыв бомбы|Bomb знает о всех объектах рядом|Bomb уведомляет → объекты проверяют дистанцию|
|Сохранение игры|SaveSystem обходит каждый класс|Отправляется событие → каждый сохраняется сам|

**События (Events)** основаны на **делегатах (Delegates)** — это механизм, позволяющий "подписываться" на уведомления и реагировать на них без жёстких связей между классами.

---

## Delegate — основа

### Что такое делегат?

**Делегат** — это тип данных, который хранит ссылки на методы. Можно думать о нём как о "указателе на функцию".



```csharp
// Объявление типа делегата
// Может хранить ссылку на любой метод с подходящей сигнатурой:
// - возвращает void
// - принимает один параметр типа int
public delegate void HealthChangedDelegate(int newHealth);
```

### Синтаксис объявления



```csharp
public class Player : MonoBehaviour
{
    [SerializeField] private int health = 100;

    // Объявляем делегат как поле класса
    public HealthChangedDelegate OnHealthChanged;

    public void TakeDamage(int damage)
    {
        health -= damage;
        
        // Вызов делегата (если кто-то подписан)
        OnHealthChanged?.Invoke(health);
    }
}
```

### Подписка на делегат



```csharp
public class HealthBar : MonoBehaviour
{
    [SerializeField] private Slider healthSlider;
    [SerializeField] private Player player;

    private void Start()
    {
        // Подписка: += привязывает метод к делегату
        player.OnHealthChanged += UpdateHealthBar;
    }

    private void UpdateHealthBar(int newHealth)
    {
        healthSlider.value = newHealth / 100f;
        Debug.Log($"Полоса здоровья обновлена: {newHealth}/100");
    }

    private void OnDestroy()
    {
        // Отписка: -= убирает метод из делегата
        if (player != null)
            player.OnHealthChanged -= UpdateHealthBar;
    }
}
```

### Альтернативные способы работы с делегатами



```csharp
public class DelegateExamples : MonoBehaviour
{
    // Объявление делегата
    public delegate void GameEventDelegate(string message);
    public GameEventDelegate OnGameEvent;

    private void Start()
    {
        // ═══ Способы подписки ═══

        // 1. Именованный метод
        OnGameEvent += ShowMessage;

        // 2. Анонимный метод
        OnGameEvent += delegate(string msg) 
        {
            Debug.Log($"Анонимный метод: {msg}");
        };

        // 3. Lambda-выражение
        OnGameEvent += (msg) => Debug.Log($"Lambda: {msg}");

        // 4. Прямое присвоение (перезаписывает всё!)
        OnGameEvent = ShowMessage; // Остальные подписки потеряны!

        // ═══ Способы вызова ═══

        // 1. Проверка на null + вызов
        if (OnGameEvent != null)
            OnGameEvent("Проверка перед вызовом");

        // 2. Безопасный вызов (C# 6.0+)
        OnGameEvent?.Invoke("Безопасный вызов");

        // 3. Прямой вызов (может выбросить NullReferenceException)
        // OnGameEvent("Опасно!"); // НЕ делай так!
    }

    private void ShowMessage(string message)
    {
        Debug.Log($"Именованный метод: {message}");
    }
}
```

### Проверка подписчиков



```csharp
public class DelegateInfo : MonoBehaviour
{
    public delegate void TestDelegate();
    public TestDelegate OnTest;

    private void Start()
    {
        // Подписываем несколько методов
        OnTest += Method1;
        OnTest += Method2;
        OnTest += Method3;

        // Проверяем информацию о делегате
        if (OnTest != null)
        {
            Delegate[] subscribers = OnTest.GetInvocationList();
            Debug.Log($"Подписчиков: {subscribers.Length}");

            foreach (Delegate d in subscribers)
            {
                Debug.Log($"Метод: {d.Method.Name}, Класс: {d.Target}");
            }
        }

        OnTest?.Invoke();
    }

    private void Method1() => Debug.Log("Метод 1 выполнен");
    private void Method2() => Debug.Log("Метод 2 выполнен");
    private void Method3() => Debug.Log("Метод 3 выполнен");
}
```

---

## Multicast Delegate

Один из главных плюсов делегатов — возможность **множественной подписки**. Один делегат может хранить ссылки на несколько методов и вызывать их все по очереди.

### Принцип работы



```csharp
public class CoinCollector : MonoBehaviour
{
    // Делегат для события сбора монеты
    public delegate void CoinCollectedDelegate(int coinValue);
    public CoinCollectedDelegate OnCoinCollected;

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            // Одно событие — много подписчиков
            OnCoinCollected?.Invoke(10);
            Destroy(gameObject);
        }
    }
}
```

### Множественная подписка



```csharp
public class ScoreManager : MonoBehaviour
{
    private int totalScore = 0;

    public void AddScore(int points)
    {
        totalScore += points;
        Debug.Log($"💰 Очки добавлены: +{points}. Общий счёт: {totalScore}");
    }
}

public class SoundManager : MonoBehaviour
{
    public void PlayCoinSound(int coinValue)
    {
        // Разные звуки в зависимости от ценности монеты
        string soundName = coinValue >= 50 ? "GoldCoin" : "SilverCoin";
        Debug.Log($"🔊 Проигрывается звук: {soundName}");
        // AudioSource.PlayOneShot(coinSounds[soundName]);
    }
}

public class UIManager : MonoBehaviour
{
    public void ShowCoinPopup(int coinValue)
    {
        Debug.Log($"✨ UI: Показан попап +{coinValue} монет");
        // Instantiate(coinPopupPrefab, screenPosition, Quaternion.identity);
    }
}
```



```csharp
public class GameInitializer : MonoBehaviour
{
    [SerializeField] private CoinCollector coin;
    [SerializeField] private ScoreManager scoreManager;
    [SerializeField] private SoundManager soundManager;
    [SerializeField] private UIManager uiManager;

    private void Start()
    {
        // Подписываем все системы на одно событие
        coin.OnCoinCollected += scoreManager.AddScore;     // Обновить счёт
        coin.OnCoinCollected += soundManager.PlayCoinSound; // Проиграть звук
        coin.OnCoinCollected += uiManager.ShowCoinPopup;    // Показать попап

        Debug.Log("Все системы подписаны на событие сбора монеты");
    }
}
```

**Результат при сборе монеты:**



```csharp
💰 Очки добавлены: +10. Общий счёт: 10
🔊 Проигрывается звук: SilverCoin
✨ UI: Показан попап +10 монет
```

### Порядок выполнения



```csharp
public class ExecutionOrderDemo : MonoBehaviour
{
    public delegate void OrderTestDelegate();
    public OrderTestDelegate OnOrderTest;

    private void Start()
    {
        OnOrderTest += First;
        OnOrderTest += Second;
        OnOrderTest += Third;

        Debug.Log("═══ Начинаем вызов делегата ═══");
        OnOrderTest?.Invoke();
        Debug.Log("═══ Вызов завершён ═══");
    }

    private void First()  => Debug.Log("1. Первый метод");
    private void Second() => Debug.Log("2. Второй метод");
    private void Third()  => Debug.Log("3. Третий метод");
}
```

**Вывод:**



```csharp
═══ Начинаем вызов делегата ═══
1. Первый метод
2. Второй метод
3. Третий метод
═══ Вызов завершён ═══
```

> ⚠️ **Важно:** методы вызываются в порядке подписки, но **не полагайся на это**! Если порядок важен — используй отдельные события или явную последовательность.

### Возвращаемые значения и multicast



```csharp
// Делегат с возвращаемым значением
public delegate bool CanPlayerActDelegate();
public CanPlayerActDelegate CanPlayerAct;

private void TestReturnValues()
{
    CanPlayerAct += () => true;   // Подписчик 1: разрешает
    CanPlayerAct += () => false;  // Подписчик 2: запрещает
    CanPlayerAct += () => true;   // Подписчик 3: разрешает

    // При multicast делегате возвращается значение ПОСЛЕДНЕГО метода!
    bool result = CanPlayerAct?.Invoke() ?? true;
    Debug.Log($"Результат: {result}"); // Вывод: "Результат: true"
}
```

> 💡 **Правило:** для multicast делегатов избегай возвращаемых значений. Используй `void` или обрабатывай результаты через параметры by ref.

---

## Event — безопасность и инкапсуляция

### Проблема обычных делегатов



```csharp
public class Player : MonoBehaviour
{
    public HealthChangedDelegate OnHealthChanged; // public делегат — опасно!
    
    private int health = 100;
}

public class EvilScript : MonoBehaviour
{
    [SerializeField] private Player player;

    private void Start()
    {
        // 😈 Злонамеренный код может:
        
        // 1. Обнулить всех подписчиков
        player.OnHealthChanged = null;
        
        // 2. Вызвать событие без причины
        player.OnHealthChanged?.Invoke(0);
        
        // 3. Подписать свой метод в начало списка
        player.OnHealthChanged = MyMethod + player.OnHealthChanged;
    }
    
    private void MyMethod(int health) => Debug.Log("Перехватил событие!");
}
```

### Event решает проблему



```csharp
public class Player : MonoBehaviour
{
    private int health = 100;

    // event — инкапсулированный делегат
    public event HealthChangedDelegate OnHealthChanged;

    public void TakeDamage(int damage)
    {
        health -= damage;
        OnHealthChanged?.Invoke(health); // Только владелец может вызвать
    }
}

public class SafeScript : MonoBehaviour
{
    [SerializeField] private Player player;

    private void Start()
    {
        // ✅ Можно подписываться
        player.OnHealthChanged += UpdateUI;
        
        // ✅ Можно отписываться
        player.OnHealthChanged -= UpdateUI;
        
        // ❌ Нельзя присваивать (ошибка компиляции)
        // player.OnHealthChanged = UpdateUI;
        
        // ❌ Нельзя вызывать извне (ошибка компиляции)
        // player.OnHealthChanged(50);
        
        // ❌ Нельзя обнулить (ошибка компиляции)
        // player.OnHealthChanged = null;
    }

    private void UpdateUI(int health) => Debug.Log($"UI: Здоровье {health}");
}
```

### Синтаксис событий

```csharp
public class EventSyntaxExamples : MonoBehaviour
{
    // ═══ Различные способы объявления событий ═══

    // 1. На основе кастомного делегата
    public delegate void HealthChangedDelegate(int newHealth);
    public event HealthChangedDelegate OnHealthChanged;

    // 2. На основе Action (встроенный делегат)
    public event System.Action OnPlayerDied;
    public event System.Action<int> OnScoreChanged;
    public event System.Action<string, float> OnMessageShown;

    // 3. На основе Func (с возвращаемым значением)
    public event System.Func<bool> OnCanPlayerMove;

    // 4. С кастомными EventArgs
    public event System.EventHandler<HealthEventArgs> OnHealthEvent;

    private void Start()
    {
        // Вызов событий (только изнутри класса-владельца)
        OnHealthChanged?.Invoke(75);
        OnPlayerDied?.Invoke();
        OnScoreChanged?.Invoke(1500);
        OnMessageShown?.Invoke("Level Complete!", 3f);

        // Для событий с возвращаемым значением
        bool canMove = OnCanPlayerMove?.Invoke() ?? true;
        
        // С EventArgs
        OnHealthEvent?.Invoke(this, new HealthEventArgs { Health = 75, MaxHealth = 100 });
    }
}

// Кастомный класс для передачи данных события
public class HealthEventArgs : System.EventArgs
{
    public int Health { get; set; }
    public int MaxHealth { get; set; }
    public float HealthPercent => (float)Health / MaxHealth;
}
```

### Продвинутые возможности событий



```csharp
public class AdvancedEventExample : MonoBehaviour
{
    // Событие с кастомными аксессорами (редко используется)
    private System.Action<int> healthChangedBackingField;
    
    public event System.Action<int> OnHealthChanged
    {
        add
        {
            healthChangedBackingField += value;
            Debug.Log($"Подписчик добавлен. Всего: {healthChangedBackingField?.GetInvocationList().Length ?? 0}");
        }
        remove
        {
            healthChangedBackingField -= value;
            Debug.Log($"Подписчик удалён. Всего: {healthChangedBackingField?.GetInvocationList().Length ?? 0}");
        }
    }

    public void TakeDamage(int damage)
    {
        // Вызов события через backing field
        healthChangedBackingField?.Invoke(100 - damage);
    }
}
```

### События vs делегаты — сводная таблица

|Характеристика|Delegate|Event|
|---|---|---|
|Подписка +=|✅ Да|✅ Да|
|Отписка -=|✅ Да|✅ Да|
|Присвоение =|✅ Да (опасно!)|❌ Ошибка компиляции|
|Вызов извне|✅ Да (опасно!)|❌ Ошибка компиляции|
|Инкапсуляция|❌ Нет|✅ Да|
|Безопасность|⚠️ Низкая|✅ Высокая|
|Использование|Callbacks, функциональщина|Уведомления, Observer|

---

## Action и Func

### Зачем нужны Action и Func?

Вместо создания кастомных делегатов для каждого случая, C# предоставляет готовые обобщённые типы:



```csharp
// ❌ Старый способ — много кода
public delegate void PlayerDiedDelegate();
public delegate void HealthChangedDelegate(int health);
public delegate void DamageDealtDelegate(int damage, string damageType);

// ✅ Новый способ — используем Action
public event System.Action OnPlayerDied;
public event System.Action<int> OnHealthChanged;
public event System.Action<int, string> OnDamageDealt;
```

### Action — для методов без возвращаемого значения



```csharp
public class ActionExamples : MonoBehaviour
{
    // Action без параметров (аналог delegate void MyDelegate())
    public event System.Action OnGameStarted;
    
    // Action с одним параметром
    public event System.Action<int> OnScoreChanged;
    
    // Action с двумя параметрами
    public event System.Action<int, string> OnDamageDealt;
    
    // Action с тремя параметрами
    public event System.Action<Vector3, float, bool> OnExplosion;
    
    // Action поддерживает до 16 параметров
    public event System.Action<int, int, int, int, int> OnCrazyEvent;

    private void Start()
    {
        // Подписки
        OnGameStarted += () => Debug.Log("Игра началась!");
        OnScoreChanged += (score) => Debug.Log($"Новый счёт: {score}");
        OnDamageDealt += (damage, type) => Debug.Log($"Урон: {damage} ({type})");
        OnExplosion += (pos, radius, isPowerful) => 
        {
            Debug.Log($"Взрыв в точке {pos}, радиус {radius}м");
            if (isPowerful) Debug.Log("Это был мощный взрыв!");
        };

        // Вызовы
        OnGameStarted?.Invoke();
        OnScoreChanged?.Invoke(1250);
        OnDamageDealt?.Invoke(50, "Fire");
        OnExplosion?.Invoke(Vector3.zero, 10f, true);
    }
}
```

### Func — для методов с возвращаемым значением



```csharp
public class FuncExamples : MonoBehaviour
{
    // Func<TResult> — без параметров, возвращает TResult
    public System.Func<bool> CanPlayerMove;
    
    // Func<T, TResult> — один параметр типа T, возвращает TResult
    public System.Func<int, string> GetPlayerRank;
    
    // Func<T1, T2, TResult> — два параметра, возвращает TResult
    public System.Func<int, int, int> CalculateDamage;
    
    // Func поддерживает до 16 параметров + возвращаемый тип
    public System.Func<int, string, float, Vector3, bool> ComplexCalculation;

    private void Start()
    {
        // Подписки на Func
        CanPlayerMove += () => true; // всегда можно двигаться
        GetPlayerRank += (score) => score > 1000 ? "Master" : "Novice";
        CalculateDamage += (baseDmg, multiplier) => baseDmg * multiplier;

        // Вызов Func и получение результатов
        bool canMove = CanPlayerMove?.Invoke() ?? false;
        Debug.Log($"Игрок может двигаться: {canMove}");

        string rank = GetPlayerRank?.Invoke(1500) ?? "Unknown";
        Debug.Log($"Ранг игрока: {rank}");

        int totalDamage = CalculateDamage?.Invoke(10, 3) ?? 0;
        Debug.Log($"Итоговый урон: {totalDamage}");
    }
}
```

### Практический пример с Action/Func в игре



```csharp
public class GameEventSystem : MonoBehaviour
{
    [Header("Игровые события")]
    // События без параметров
    public static event System.Action OnGamePaused;
    public static event System.Action OnGameResumed;
    public static event System.Action OnLevelCompleted;

    // События с параметрами
    public static event System.Action<int> OnPlayerLevelUp;           // новый уровень
    public static event System.Action<string> OnPlayerDied;          // причина смерти
    public static event System.Action<Vector3, float> OnExplosion;   // позиция, сила
    public static event System.Action<string, int> OnItemCollected; // название, количество

    // Запросы через Func (возвращают значения)
    public static System.Func<string, bool> CanUseItem;     // можно ли использовать предмет
    public static System.Func<Vector3, bool> CanMoveToPos;  // можно ли двигаться в точку
    public static System.Func<int> GetPlayerMoney;          // сколько денег у игрока

    // Методы для вызова событий
    public static void TriggerExplosion(Vector3 position, float power)
    {
        OnExplosion?.Invoke(position, power);
    }

    public static void PlayerLeveledUp(int newLevel)
    {
        OnPlayerLevelUp?.Invoke(newLevel);
    }

    public static void PlayerDied(string reason)
    {
        OnPlayerDied?.Invoke(reason);
    }

    // Методы для запросов
    public static bool CheckCanUseItem(string itemName)
    {
        return CanUseItem?.Invoke(itemName) ?? false;
    }

    public static bool CheckCanMoveTo(Vector3 position)
    {
        return CanMoveToPos?.Invoke(position) ?? true;
    }

    public static int GetCurrentMoney()
    {
        return GetPlayerMoney?.Invoke() ?? 0;
    }
}
```



```csharp
// Подписчики событий
public class UIManager : MonoBehaviour
{
    private void OnEnable()
    {
        GameEventSystem.OnPlayerLevelUp += ShowLevelUpPopup;
        GameEventSystem.OnPlayerDied += ShowGameOverScreen;
        GameEventSystem.OnItemCollected += UpdateInventoryUI;
    }

    private void OnDisable()
    {
        GameEventSystem.OnPlayerLevelUp -= ShowLevelUpPopup;
        GameEventSystem.OnPlayerDied -= ShowGameOverScreen;
        GameEventSystem.OnItemCollected -= UpdateInventoryUI;
    }

    private void ShowLevelUpPopup(int level)
    {
        Debug.Log($"✨ UI: Показ попапа повышения до уровня {level}");
    }

    private void ShowGameOverScreen(string reason)
    {
        Debug.Log($"💀 UI: Game Over. Причина: {reason}");
    }

    private void UpdateInventoryUI(string item, int count)
    {
        Debug.Log($"📦 UI: Предмет '{item}' x{count} добавлен в инвентарь");
    }
}
```

---

## Паттерн Observer

**Observer (Наблюдатель)** — один из самых важных паттернов в игровой разработке. События C# — это готовая реализация этого паттерна.

### Классическая реализация Observer



```csharp
// Интерфейс наблюдателя
public interface IPlayerObserver
{
    void OnPlayerHealthChanged(int newHealth);
    void OnPlayerDied();
}

// Наблюдаемый объект (Subject)
public class Player : MonoBehaviour
{
    private List<IPlayerObserver> observers = new List<IPlayerObserver>();
    private int health = 100;

    // Методы управления наблюдателями
    public void AddObserver(IPlayerObserver observer)
    {
        if (!observers.Contains(observer))
            observers.Add(observer);
    }

    public void RemoveObserver(IPlayerObserver observer)
    {
        observers.Remove(observer);
    }

    private void NotifyHealthChanged()
    {
        foreach (IPlayerObserver observer in observers)
        {
            observer.OnPlayerHealthChanged(health);
        }
    }

    private void NotifyPlayerDied()
    {
        foreach (IPlayerObserver observer in observers)
        {
            observer.OnPlayerDied();
        }
    }

    // Игровая логика
    public void TakeDamage(int damage)
    {
        health -= damage;
        NotifyHealthChanged();

        if (health <= 0)
        {
            NotifyPlayerDied();
        }
    }
}
```

### Современная реализация через события



```csharp
// То же самое, но через события — намного проще!
public class ModernPlayer : MonoBehaviour
{
    private int health = 100;

    // События вместо списка наблюдателей
    public event System.Action<int> OnHealthChanged;
    public event System.Action OnDied;

    public void TakeDamage(int damage)
    {
        health -= damage;
        OnHealthChanged?.Invoke(health);

        if (health <= 0)
        {
            OnDied?.Invoke();
        }
    }
}

// Наблюдатели просто подписываются на события
public class HealthBar : MonoBehaviour
{
    [SerializeField] private ModernPlayer player;
    [SerializeField] private Slider healthSlider;

    private void Start()
    {
        player.OnHealthChanged += UpdateHealthBar;
        player.OnDied += HideHealthBar;
    }

    private void UpdateHealthBar(int health)
    {
        healthSlider.value = health / 100f;
    }

    private void HideHealthBar()
    {
        healthSlider.gameObject.SetActive(false);
    }

    private void OnDestroy()
    {
        if (player != null)
        {
            player.OnHealthChanged -= UpdateHealthBar;
            player.OnDied -= HideHealthBar;
        }
    }
}
```

### Сложный пример: система достижений



```csharp
public class AchievementSystem : MonoBehaviour
{
    [System.Serializable]
    public class Achievement
    {
        public string name;
        public string description;
        public bool isUnlocked;
        public System.Action<AchievementSystem> condition;

        public Achievement(string name, string desc, System.Action<AchievementSystem> condition)
        {
            this.name = name;
            this.description = desc;
            this.condition = condition;
            this.isUnlocked = false;
        }
    }

    [Header("Статистика игрока")]
    public int enemiesKilled = 0;
    public int coinsCollected = 0;
    public int deathCount = 0;
    public float timePlayed = 0f;

    private List<Achievement> achievements = new List<Achievement>();
    
    public event System.Action<Achievement> OnAchievementUnlocked;

    private void Start()
    {
        InitializeAchievements();
        SubscribeToGameEvents();
    }

    private void InitializeAchievements()
    {
        achievements.Add(new Achievement(
            "First Blood", 
            "Убей первого врага",
            (system) => system.enemiesKilled >= 1
        ));

        achievements.Add(new Achievement(
            "Rich Man", 
            "Собери 100 монет",
            (system) => system.coinsCollected >= 100
        ));

        achievements.Add(new Achievement(
            "Veteran", 
            "Играй 1 час",
            (system) => system.timePlayed >= 3600f
        ));

        achievements.Add(new Achievement(
            "Immortal",
```

```csharp
        achievements.Add(new Achievement(
            "Immortal",
            "Пройди игру без единой смерти",
            (system) => system.deathCount == 0 && system.enemiesKilled >= 10
        ));

        achievements.Add(new Achievement(
            "Genocide",
            "Убей 100 врагов",
            (system) => system.enemiesKilled >= 100
        ));
    }

    private void SubscribeToGameEvents()
    {
        // Подписываемся на события игры через статический EventBus
        GameEventSystem.OnPlayerDied += (reason) =>
        {
            deathCount++;
            CheckAchievements();
        };

        GameEventSystem.OnItemCollected += (itemName, count) =>
        {
            if (itemName == "Coin") coinsCollected += count;
            CheckAchievements();
        };
    }

    public void RegisterEnemyKill()
    {
        enemiesKilled++;
        CheckAchievements();
    }

    private void Update()
    {
        timePlayed += Time.deltaTime;
    }

    private void CheckAchievements()
    {
        foreach (Achievement achievement in achievements)
        {
            if (!achievement.isUnlocked && achievement.condition(this))
            {
                achievement.isUnlocked = true;
                OnAchievementUnlocked?.Invoke(achievement);
                Debug.Log($"🏆 Достижение разблокировано: [{achievement.name}] — {achievement.description}");
            }
        }
    }

    private void OnDestroy()
    {
        // Отписка от статических событий обязательна!
        // (В данном случае — через lambda это сложно, лучше использовать именованные методы)
        // Подробнее об этом — в разделе про утечки памяти
    }
}
```

### ScriptableObject как канал событий

Популярный паттерн в Unity — использовать **ScriptableObject** как контейнер для событий. Это позволяет связывать объекты через Assets, не создавая прямых ссылок в сцене:



```csharp
// GameEvent.cs — ScriptableObject-событие
using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu(fileName = "GameEvent", menuName = "Events/Game Event")]
public class GameEvent : ScriptableObject
{
    private readonly List<System.Action> listeners = new List<System.Action>();

    // Вызвать событие
    public void Raise()
    {
        // Идём с конца, чтобы безопасно удалять во время итерации
        for (int i = listeners.Count - 1; i >= 0; i--)
        {
            listeners[i]?.Invoke();
        }
    }

    public void Subscribe(System.Action listener)
    {
        if (!listeners.Contains(listener))
            listeners.Add(listener);
    }

    public void Unsubscribe(System.Action listener)
    {
        listeners.Remove(listener);
    }
}
```



```csharp
// GameEventListener.cs — компонент-подписчик
using UnityEngine;
using UnityEngine.Events;

public class GameEventListener : MonoBehaviour
{
    [SerializeField] private GameEvent gameEvent;

    // UnityEvent позволяет настраивать реакцию прямо в Inspector
    [SerializeField] private UnityEvent response;

    private void OnEnable()
    {
        gameEvent.Subscribe(OnEventRaised);
    }

    private void OnDisable()
    {
        gameEvent.Unsubscribe(OnEventRaised);
    }

    private void OnEventRaised()
    {
        response?.Invoke();
    }
}
```



```csharp
// Использование в игровом коде
public class PlayerWithSOEvents : MonoBehaviour
{
    [Header("SO События")]
    [SerializeField] private GameEvent onPlayerDiedEvent;
    [SerializeField] private GameEvent onPlayerJumpedEvent;

    private int health = 100;

    public void TakeDamage(int damage)
    {
        health -= damage;
        if (health <= 0)
        {
            // Вызываем ScriptableObject-событие
            onPlayerDiedEvent.Raise();
        }
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            onPlayerJumpedEvent.Raise();
        }
    }
}
```

---

## Утечки памяти и отписка

### Почему важна отписка



```csharp
// ❌ ОПАСНЫЙ КОД — утечка памяти!
public class LeakyComponent : MonoBehaviour
{
    [SerializeField] private Player player;

    private void Start()
    {
        // Подписываемся, но никогда не отписываемся
        player.OnHealthChanged += UpdateUI;
        player.OnDied += HandlePlayerDeath;
    }

    private void UpdateUI(int health) { /* ... */ }
    private void HandlePlayerDeath() { /* ... */ }

    // OnDestroy НЕ вызывает отписку!
    // Когда LeakyComponent уничтожается:
    // - Объект удалён из сцены
    // - НО Player всё ещё хранит ссылку на методы уничтоженного объекта
    // - GC не может собрать LeakyComponent — на него есть ссылка!
    // - Методы мёртвого объекта будут вызываться снова и снова
}
```

**Что происходит без отписки:**



```csharp
1. PlayerComponent существует → LeakyComponent существует
2. LeakyComponent уничтожен → объект "мёртв", но...
3. Player.OnHealthChanged всё ещё хранит ссылку на LeakyComponent.UpdateUI
4. При следующем вызове OnHealthChanged:
   - Вызывается метод УНИЧТОЖЕННОГО объекта
   - Возможна ошибка: "MissingReferenceException"
   - Или тихая утечка памяти — GC не может освободить память
```

### Правильные паттерны отписки



```csharp
// ✅ Паттерн 1: OnDestroy — базовый подход
public class SafeComponent1 : MonoBehaviour
{
    [SerializeField] private Player player;

    private void Start()
    {
        player.OnHealthChanged += UpdateUI;
        player.OnDied += HandleDeath;
    }

    private void UpdateUI(int health)
    {
        Debug.Log($"UI обновлён: {health}");
    }

    private void HandleDeath()
    {
        Debug.Log("Обработка смерти игрока");
    }

    // OnDestroy вызывается при уничтожении объекта
    private void OnDestroy()
    {
        // Проверяем null — player мог быть уничтожен раньше нас
        if (player != null)
        {
            player.OnHealthChanged -= UpdateUI;
            player.OnDied -= HandleDeath;
        }

        Debug.Log("Компонент уничтожен, отписка выполнена.");
    }
}
```



```csharp
// ✅ Паттерн 2: OnEnable / OnDisable — для объектов, которые включаются/выключаются
public class SafeComponent2 : MonoBehaviour
{
    [SerializeField] private Player player;

    // OnEnable вызывается при активации объекта
    private void OnEnable()
    {
        if (player != null)
        {
            player.OnHealthChanged += UpdateUI;
            player.OnDied += HandleDeath;
            Debug.Log("Подписка выполнена (OnEnable)");
        }
    }

    // OnDisable вызывается при деактивации И при уничтожении
    private void OnDisable()
    {
        if (player != null)
        {
            player.OnHealthChanged -= UpdateUI;
            player.OnDied -= HandleDeath;
            Debug.Log("Отписка выполнена (OnDisable)");
        }
    }

    private void UpdateUI(int health) { /* ... */ }
    private void HandleDeath() { /* ... */ }
}
```



```csharp
// ✅ Паттерн 3: Статические события — особая осторожность!
public class SafeComponentWithStaticEvents : MonoBehaviour
{
    private void OnEnable()
    {
        // Статические события живут всё время работы приложения
        // Без отписки объект НИКОГДА не будет собран GC
        GameEventSystem.OnPlayerDied += HandlePlayerDied;
        GameEventSystem.OnLevelCompleted += HandleLevelCompleted;
    }

    private void OnDisable()
    {
        // Для статических событий отписка ОСОБЕННО критична
        GameEventSystem.OnPlayerDied -= HandlePlayerDied;
        GameEventSystem.OnLevelCompleted -= HandleLevelCompleted;
    }

    private void HandlePlayerDied(string reason)
    {
        Debug.Log($"Статическое событие: игрок умер. Причина: {reason}");
    }

    private void HandleLevelCompleted()
    {
        Debug.Log("Статическое событие: уровень пройден");
    }
}
```



```csharp
// ✅ Паттерн 4: CancellationToken / DisposableSubscription (продвинутый)
public class DisposableSubscription : System.IDisposable
{
    private System.Action unsubscribeAction;

    public DisposableSubscription(System.Action unsubscribeAction)
    {
        this.unsubscribeAction = unsubscribeAction;
    }

    public void Dispose()
    {
        unsubscribeAction?.Invoke();
        unsubscribeAction = null;
    }
}

public class SafeComponentAdvanced : MonoBehaviour
{
    [SerializeField] private Player player;

    // Храним все подписки
    private List<DisposableSubscription> subscriptions = new List<DisposableSubscription>();

    private void Start()
    {
        // Создаём подписки с возможностью отписки
        Subscribe(player.OnHealthChanged, UpdateUI);
        Subscribe(player.OnDied, HandleDeath);
    }

    private void Subscribe(System.Action<int> gameEvent, System.Action<int> handler)
    {
        gameEvent += handler;
        subscriptions.Add(new DisposableSubscription(() => gameEvent -= handler));
    }

    private void Subscribe(System.Action gameEvent, System.Action handler)
    {
        gameEvent += handler;
        subscriptions.Add(new DisposableSubscription(() => gameEvent -= handler));
    }

    private void OnDestroy()
    {
        // Отписываем всё одним вызовом
        foreach (var sub in subscriptions)
        {
            sub.Dispose();
        }
        subscriptions.Clear();
    }

    private void UpdateUI(int health) { /* ... */ }
    private void HandleDeath() { /* ... */ }
}
```

### Отладка утечек событий



```csharp
// Утилита для диагностики подписок
public static class EventDebugger
{
    public static void PrintSubscribers(System.Delegate eventDelegate, string eventName)
    {
        if (eventDelegate == null)
        {
            Debug.Log($"[EventDebugger] {eventName}: нет подписчиков");
            return;
        }

        Delegate[] subscribers = eventDelegate.GetInvocationList();
        Debug.Log($"[EventDebugger] {eventName}: {subscribers.Length} подписчик(ов)");

        foreach (Delegate subscriber in subscribers)
        {
            string targetName = subscriber.Target?.GetType().Name ?? "Static";
            string methodName = subscriber.Method.Name;
            bool isAlive = subscriber.Target != null;

            Debug.Log($"  → {targetName}.{methodName} | Живой: {isAlive}");
        }
    }
}

// Использование
public class EventLeakDetector : MonoBehaviour
{
    [SerializeField] private Player player;

    [ConMenu("Проверить подписчиков")]
    private void CheckSubscribers()
    {
        // Рефлексия для доступа к приватному backing field события
        var fieldInfo = typeof(Player).GetField(
            "OnHealthChanged",
            System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance
        );

        if (fieldInfo != null)
        {
            var eventDelegate = fieldInfo.GetValue(player) as System.Delegate;
            EventDebugger.PrintSubscribers(eventDelegate, "OnHealthChanged");
        }
    }
}
```

### Сводная таблица паттернов отписки

|Паттерн|Когда использовать|
|---|---|
|`OnDestroy`|Объект создаётся один раз и живёт до уничтожения|
|`OnEnable/OnDisable`|Объект часто включается/выключается|
|`OnDisable` для статических|Статические события — всегда через `OnDisable`|
|`IDisposable` паттерн|Сложные системы, много событий, тестирование|

---

## Практическое задание

Создадим **EventBus** — центральную шину событий, которую использует вся игра. По этому событию `OnPlayerDied` уведомим UI и GameManager.

### Структура проекта



```csharp
📁 Scripts/
  📁 Core/
    📄 EventBus.cs           ← центральная шина событий
  📁 Player/
    📄 PlayerHealth.cs       ← здоровье игрока
    📄 PlayerInput.cs        ← ввод игрока (для теста)
  📁 Managers/
    📄 GameManager.cs        ← управление игрой
  📁 UI/
    📄 GameOverUI.cs         ← экран смерти
    📄 PlayerHealthUI.cs     ← полоска здоровья
  📁 Audio/
    📄 AudioEventHandler.cs  ← звуковые эффекты
  📁 Demo/
    📄 EventBusDemo.cs       ← демонстрационный скрипт
```

### Шаг 1: EventBus — центральная шина событий



```csharp
// EventBus.cs
using UnityEngine;
using System;

/// <summary>
/// Центральная шина событий игры.
/// Все системы общаются через неё — без прямых ссылок друг на друга.
///
/// Принцип работы:
/// 1. Publisher вызывает событие через EventBus
/// 2. Все подписчики получают уведомление
/// 3. Каждый подписчик реагирует независимо
/// </summary>
public static class EventBus
{
    // ═══════════════════════════════════════════════════════
    // СОБЫТИЯ ИГРОКА
    // ═══════════════════════════════════════════════════════

    /// <summary>Игрок умер. Параметр — причина смерти.</summary>
    public static event Action<PlayerDeathData> OnPlayerDied;

    /// <summary>Здоровье игрока изменилось.</summary>
    public static event Action<float, float> OnPlayerHealthChanged; // current, max

    /// <summary>Игрок получил урон.</summary>
    public static event Action<float> OnPlayerDamaged;

    /// <summary>Игрок восстановил здоровье.</summary>
    public static event Action<float> OnPlayerHealed;

    /// <summary>Игрок собрал монету.</summary>
    public static event Action<int> OnCoinCollected;

    /// <summary>Счёт изменился.</summary>
    public static event Action<int> OnScoreChanged;

    // ═══════════════════════════════════════════════════════
    // СОБЫТИЯ ИГРЫ
    // ═══════════════════════════════════════════════════════

    /// <summary>Игра началась.</summary>
    public static event Action OnGameStarted;

    /// <summary>Игра поставлена на паузу.</summary>
    public static event Action OnGamePaused;

    /// <summary>Пауза снята.</summary>
    public static event Action OnGameResumed;

    /// <summary>Игра завершена (Game Over).</summary>
    public static event Action<GameOverData> OnGameOver;

    /// <summary>Уровень пройден.</summary>
    public static event Action<int> OnLevelCompleted; // номер уровня

    /// <summary>Новый рекорд установлен.</summary>
    public static event Action<int> OnNewHighScore;

    // ═══════════════════════════════════════════════════════
    // МЕТОДЫ ПУБЛИКАЦИИ СОБЫТИЙ (только здесь вызываем Invoke)
    // ═══════════════════════════════════════════════════════

    public static void PublishPlayerDied(PlayerDeathData data)
    {
        Debug.Log($"[EventBus] ► OnPlayerDied | Причина: {data.Reason}, " +
                  $"Очки: {data.FinalScore}, Время: {data.SurvivalTime:F1}с");
        OnPlayerDied?.Invoke(data);
    }

    public static void PublishPlayerHealthChanged(float current, float max)
    {
        OnPlayerHealthChanged?.Invoke(current, max);
    }

    public static void PublishPlayerDamaged(float amount)
    {
        Debug.Log($"[EventBus] ► OnPlayerDamaged | Урон: {amount}");
        OnPlayerDamaged?.Invoke(amount);
    }

    public static void PublishPlayerHealed(float amount)
    {
        Debug.Log($"[EventBus] ► OnPlayerHealed | Лечение: {amount}");
        OnPlayerHealed?.Invoke(amount);
    }

    public static void PublishCoinCollected(int value)
    {
        Debug.Log($"[EventBus] ► OnCoinCollected | Монета: {value}");
        OnCoinCollected?.Invoke(value);
    }

    public static void PublishScoreChanged(int newScore)
    {
        OnScoreChanged?.Invoke(newScore);
    }

    public static void PublishGameStarted()
    {
        Debug.Log("[EventBus] ► OnGameStarted");
        OnGameStarted?.Invoke();
    }

    public static void PublishGamePaused()
    {
        Debug.Log("[EventBus] ► OnGamePaused");
        OnGamePaused?.Invoke();
    }

    public static void PublishGameResumed()
    {
        Debug.Log("[EventBus] ► OnGameResumed");
        OnGameResumed?.Invoke();
    }

    public static void PublishGameOver(GameOverData data)
    {
        Debug.Log($"[EventBus] ► OnGameOver | Счёт: {data.FinalScore}, " +
                  $"Рекорд: {data.IsNewHighScore}");
        OnGameOver?.Invoke(data);
    }

    public static void PublishLevelCompleted(int levelNumber)
    {
        Debug.Log($"[EventBus] ► OnLevelCompleted | Уровень: {levelNumber}");
        OnLevelCompleted?.Invoke(levelNumber);
    }

    public static void PublishNewHighScore(int score)
    {
        Debug.Log($"[EventBus] ► OnNewHighScore | Рекорд: {score}");
        OnNewHighScore?.Invoke(score);
    }

    // ═══════════════════════════════════════════════════════
    // УТИЛИТЫ
    // ═══════════════════════════════════════════════════════

    /// <summary>
    /// Сбрасывает все подписки.
    /// Вызывать при загрузке новой сцены, чтобы избежать утечек.
    /// </summary>
    public static void ResetAllEvents()
    {
        OnPlayerDied = null;
        OnPlayerHealthChanged = null;
        OnPlayerDamaged = null;
        OnPlayerHealed = null;
        OnCoinCollected = null;
        OnScoreChanged = null;
        OnGameStarted = null;
        OnGamePaused = null;
        OnGameResumed = null;
        OnGameOver = null;
        OnLevelCompleted = null;
        OnNewHighScore = null;

        Debug.Log("[EventBus] Все события сброшены.");
    }
}

// ═══════════════════════════════════════════════════════════
// DATA TRANSFER OBJECTS (DTO) — данные, передаваемые с событиями
// ═══════════════════════════════════════════════════════════

/// <summary>Данные о смерти игрока.</summary>
[System.Serializable]
public class PlayerDeathData
{
    public string Reason;          // "Fell into the void", "Killed by Enemy", etc.
    public int FinalScore;         // счёт на момент смерти
    public float SurvivalTime;     // сколько секунд прожил игрок
    public int EnemiesKilled;      // сколько врагов убил
    public Vector3 DeathPosition;  // где умер

    public PlayerDeathData(string reason, int score, float time, int kills, Vector3 pos)
    {
        Reason = reason;
        FinalScore = score;
        SurvivalTime = time;
        EnemiesKilled = kills;
        DeathPosition = pos;
    }
}

/// <summary>Данные о завершении игры.</summary>
[System.Serializable]
public class GameOverData
{
    public int FinalScore;
    public bool IsNewHighScore;
    public float TotalTime;
    public int TotalEnemiesKilled;

    public GameOverData(int score, bool isHighScore, float time, int kills)
    {
        FinalScore = score;
        IsNewHighScore = isHighScore;
        TotalTime = time;
        TotalEnemiesKilled = kills;
    }
}
```

### Шаг 2: PlayerHealth — источник событий



```csharp
// PlayerHealth.cs
using UnityEngine;

/// <summary>
/// Компонент здоровья игрока.
/// Публикует события через EventBus — ничего не знает о подписчиках.
/// </summary>
public class PlayerHealth : MonoBehaviour
{
    [Header("Параметры здоровья")]
    [SerializeField] private float maxHealth = 100f;
    [SerializeField] private float currentHealth;

    [Header("Защита")]
    [SerializeField] private float armor = 0f;           // снижение урона (0-100%)
    [SerializeField] private float invincibleTime = 1f;  // время неуязвимости после удара

    [Header("Дебаг")]
    [SerializeField] private bool logAllDamage = true;

    // Публичные свойства
    public float CurrentHealth => currentHealth;
    public float MaxHealth => maxHealth;
    public float HealthPercent => currentHealth / maxHealth;
    public bool IsAlive => currentHealth > 0;

    // Приватное состояние
    private bool isInvincible = false;
    private bool isDead = false;
    private float survivalTimer = 0f;
    private int enemiesKilled = 0;  // передаётся в EventBus при смерти
    private int currentScore = 0;

    // ── Unity Lifecycle ──────────────────────────────────────

    private void Awake()
    {
        currentHealth = maxHealth;
    }

    private void Start()
    {
        // Сообщаем всем начальное состояние здоровья
        EventBus.PublishPlayerHealthChanged(currentHealth, maxHealth);

        // Подписываемся на события, которые влияют на наш счёт
        EventBus.OnCoinCollected += AddToScore;
    }

    private void Update()
    {
        if (IsAlive)
            survivalTimer += Time.deltaTime;
    }

    private void OnDestroy()
    {
        // Обязательная отписка!
        EventBus.OnCoinCollected -= AddToScore;
    }

    // ── Публичные методы ─────────────────────────────────────

    /// <summary>Нанести урон игроку.</summary>
    public void TakeDamage(float amount, string source = "Unknown")
    {
        // Проверки
        if (!IsAlive || isInvincible) return;

        // Применяем броню
        float actualDamage = amount * (1f - armor / 100f);
        actualDamage = Mathf.Max(0f, actualDamage);

        if (logAllDamage)
            Debug.Log($"[PlayerHealth] Урон от '{source}': {amount:F1} → " +
                      $"с учётом брони: {actualDamage:F1}");

        // Применяем урон
        currentHealth = Mathf.Max(0f, currentHealth - actualDamage);

        // Публикуем события
        EventBus.PublishPlayerDamaged(actualDamage);
        EventBus.PublishPlayerHealthChanged(currentHealth, maxHealth);

        // Запускаем неуязвимость
        StartCoroutine(InvincibilityCoroutine());

        // Проверяем смерть
        if (currentHealth <= 0f && !isDead)
        {
            Die(source);
        }
    }

    /// <summary>Восстановить здоровье игрока.</summary>
    public void Heal(float amount)
    {
        if (!IsAlive) return;

        float actualHeal = Mathf.Min(amount, maxHealth - currentHealth);
        currentHealth += actualHeal;

        Debug.Log($"[PlayerHealth] Лечение: +{actualHeal:F1} HP. Текущее: {currentHealth:F1}");

        EventBus.PublishPlayerHealed(actualHeal);
        EventBus.PublishPlayerHealthChanged(currentHealth, maxHealth);
    }

    /// <summary>Зарегистрировать убийство врага (для статистики).</summary>
    public void RegisterEnemyKill()
    {
        enemiesKilled++;
    }

    // ── Приватные методы ─────────────────────────────────────

    private void Die(string reason)
    {
        isDead = true;

        // Собираем данные о смерти
        PlayerDeathData deathData = new PlayerDeathData(
            reason: reason,
            score: currentScore,
            time: survivalTimer,
            kills: enemiesKilled,
            pos: transform.position
        );

        // Публикуем ОДНО событие — все подписчики сами разберутся что делать
        EventBus.PublishPlayerDied(deathData);

        Debug.Log($"[PlayerHealth] Игрок погиб. " +
                  $"Прожил: {survivalTimer:F1}с, Счёт: {currentScore}, " +
                  $"Убийств: {enemiesKilled}");
    }

    private void AddToScore(int coinValue)
    {
        currentScore += coinValue * 10;
        EventBus.PublishScoreChanged(currentScore);
    }

    private System.Collections.IEnumerator InvincibilityCoroutine()
    {
        isInvincible = true;
        yield return new WaitForSeconds(invincibleTime);
        isInvincible = false;
    }
}
```

### Шаг 3: GameManager — подписчик события



```csharp
// GameManager.cs
using UnityEngine;
using UnityEngine.SceneManagement;

/// <summary>
/// Управляет состоянием игры.
/// Подписывается на EventBus и реагирует на ключевые события.
/// </summary>
public class GameManager : MonoBehaviour
{
    public static GameManager Instance { get; private set; }

    [Header("Настройки")]
    [SerializeField] private float gameOverDelay = 2f;  // задержка перед Game Over
    [SerializeField] private string mainMenuScene = "MainMenu";
    [SerializeField] private string gameScene = "Game";

    [Header("Состояние игры")]
    [SerializeField] private int currentScore = 0;
    [SerializeField] private int highScore = 0;
    [SerializeField] private bool isGameOver = false;
    [SerializeField] private bool isPaused = false;

    // Публичные свойства
    public int CurrentScore => currentScore;
    public int HighScore => highScore;
    public bool IsGameOver => isGameOver;
    public bool IsPaused => isPaused;

    // ── Unity Lifecycle ──────────────────────────────────────

    private void Awake()
    {
        // Синглтон
        if (Instance != null && Instance != this)
        {
            Destroy(gameObject);
            return;
        }

        Instance = this;
        DontDestroyOnLoad(gameObject);

        // Загружаем рекорд
        highScore = PlayerPrefs.GetInt("HighScore", 0);
    }

    private void OnEnable()
    {
        // Подписываемся на все нужные события
        EventBus.OnPlayerDied     += HandlePlayerDied;
        EventBus.OnScoreChanged   += HandleScoreChanged;
        EventBus.OnGamePaused     += HandleGamePaused;
        EventBus.OnGameResumed    += HandleGameResumed;
        EventBus.OnLevelCompleted += HandleLevelCompleted;
    }

    private void OnDisable()
    {
        // Отписываемся — обязательно!
        EventBus.OnPlayerDied     -= HandlePlayerDied;
        EventBus.OnScoreChanged   -= HandleScoreChanged;
        EventBus.OnGamePaused     -= HandleGamePaused;
        EventBus.OnGameResumed    -= HandleGameResumed;
        EventBus.OnLevelCompleted -= HandleLevelCompleted;
    }

    // ── Обработчики событий ──────────────────────────────────

    private void HandlePlayerDied(PlayerDeathData data)
    {
        if (isGameOver) return;
        isGameOver = true;

        Debug.Log($"[GameManager] Игрок умер. Обрабатываем Game Over...");

        // Проверяем рекорд
        bool isNewHighScore = data.FinalScore > highScore;
        if (isNewHighScore)
        {
            highScore = data.FinalScore;
            PlayerPrefs.SetInt("HighScore", highScore);
            PlayerPrefs.Save();
            EventBus.PublishNewHighScore(highScore);
            Debug.Log($"[GameManager] Новый рекорд: {highScore}!");
        }

        // Составляем данные Game Over
        GameOverData gameOverData = new GameOverData(
            score: data.FinalScore,
            isHighScore: isNewHighScore,
            time: data.SurvivalTime,
            kills: data.EnemiesKilled
        );

        // С задержкой публикуем Game Over
        StartCoroutine(TriggerGameOverWithDelay(gameOverData));
    }

    private void HandleScoreChanged(int newScore)
    {
        currentScore = newScore;
        Debug.Log($"[GameManager] Счёт обновлён: {currentScore}");
    }

    private void HandleGamePaused()
    {
        isPaused = true;
        Time.timeScale = 0f;
        Debug.Log("[GameManager] Игра на паузе. timeScale = 0");
    }

    private void HandleGameResumed()
    {
        isPaused = false;
        Time.timeScale = 1f;
        Debug.Log("[GameManager] Пауза снята. timeScale = 1");
    }

    private void HandleLevelCompleted(int levelNumber)
    {
        Debug.Log($"[GameManager] Уровень {levelNumber} пройден! Загружаем следующий...");
        // SceneManager.LoadScene(nextLevelName);
    }

    // ── Публичные методы ─────────────────────────────────────

    public void PauseGame()
    {
        if (!isPaused && !isGameOver)
            EventBus.PublishGamePaused();
    }

    public void ResumeGame()
    {
        if (isPaused)
            EventBus.PublishGameResumed();
    }

    public void RestartGame()
    {
        Time.timeScale = 1f;
        isGameOver = false;
        currentScore = 0;
        EventBus.ResetAllEvents(); // очищаем все старые подписки
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }

    public void GoToMainMenu()
    {
        Time.timeScale = 1f;
        EventBus.ResetAllEvents();
        SceneManager.LoadScene(mainMenuScene);
    }

    // ── Корутины ─────────────────────────────────────────────

    private System.Collections.IEnumerator TriggerGameOverWithDelay(GameOverData data)
    {
        // Ждём перед показом Game Over (время для анимации смерти)
        yield return new WaitForSecondsRealtime(gameOverDelay);
        EventBus.PublishGameOver(data);
        Debug.Log("[GameManager] ► Game Over опубликован!");
    }
}
```

### Шаг 4: GameOverUI — подписчик в UI



```csharp
// GameOverUI.cs
using UnityEngine;
using UnityEngine.UI;
using System.Collections;

/// <summary>
/// Экран Game Over.
/// Подписывается на события и обновляет UI — ничего не знает об игровой логике.
/// </summary>
public class GameOverUI : MonoBehaviour
{
    [Header("Панели")]
    [SerializeField] private GameObject gameOverPanel;
    [SerializeField] private GameObject newHighScorePanel;

    [Header("Текстовые поля")]
    [SerializeField] private  finalScore;
    [SerializeField] private  highScore;
    [SerializeField] private  survivalTime;
    [SerializeField] private  enemiesKilled;
    [SerializeField] private  deathReason;

    [Header("Кнопки")]
    [SerializeField] private Button restartButton;
    [SerializeField] private Button mainMenuButton;

    [Header("Анимация")]
    [SerializeField] private Animator panelAnimator;
    [SerializeField] private float countUpDuration = 1.5f; // время счётчика очков

    // ── Unity Lifecycle ──────────────────────────────────────

    private void Awake()
    {
        // Скрываем панель при старте
        if (gameOverPanel != null)
            gameOverPanel.SetActive(false);

        if (newHighScorePanel != null)
            newHighScorePanel.SetActive(false);
    }

    private void OnEnable()
    {
        EventBus.OnGameOver       += HandleGameOver;
        EventBus.OnNewHighScore   += HandleNewHighScore;
    }

    private void OnDisable()
    {
        EventBus.OnGameOver       -= HandleGameOver;
        EventBus.OnNewHighScore   -= HandleNewHighScore;
    }

    private void Start()
    {
        // Привязываем кнопки
        restartButton?.onClick.AddListener(OnRestartClicked);
        mainMenuButton?.onClick.AddListener(OnMainMenuClicked);
    }

    private void OnDestroy()
    {
        // Удаляем слушатели кнопок
        restartButton?.onClick.RemoveListener(OnRestartClicked);
        mainMenuButton?.onClick.RemoveListener(OnMainMenuClicked);
    }

    // ── Обработчики событий ──────────────────────────────────

    private void HandleGameOver(GameOverData data)
    {
        Debug.Log("[GameOverUI] Показываем экран Game Over");

        // Показываем панель
        if (gameOverPanel != null)
            gameOverPanel.SetActive(true);

        // Запускаем анимацию появления
        panelAnimator?.SetTrigger("Show");

        // Заполняем данные
        FillGameOverData(data);

        // Запускаем счётчик очков с анимацией
        StartCoroutine(AnimateScoreCount(0, data.FinalScore));
    }

    private void HandleNewHighScore(int newScore)
    {
        Debug.Log($"[GameOverUI] Новый рекорд: {newScore}! Показываем панель рекорда.");

        if (newHighScorePanel != null)
            newHighScorePanel.SetActive(true);

        // Можно добавить: конфетти, анимацию, звук
    }

    // ── Приватные методы ─────────────────────────────────────

    private void FillGameOverData(GameOverData data)
    {
        // Форматируем время
        int minutes = (int)(data.TotalTime / 60);
        int seconds = (int)(data.TotalTime % 60);
        string timeFormatted = $"{minutes:D2}:{seconds:D2}";

        // Заполняем текстовые поля
        if (highScore != null)
            highScore. = $"Рекорд: {data.IsNewHighScore}";

        if (survivalTime != null)
            survivalTime. = $"Выжил: {timeFormatted}";

        if (enemiesKilled != null)
            enemiesKilled. = $"Врагов убито: {data.TotalEnemiesKilled}";

        Debug.Log($"[GameOverUI] Данные заполнены: Счёт={data.FinalScore}, " +
                  $"Время={timeFormatted}, Враги={data.TotalEnemiesKilled}");
    }

    private IEnumerator AnimateScoreCount(int from, int to)
    {
        float elapsed = 0f;

        while (elapsed < countUpDuration)
        {
            elapsed += Time.unscaledDeltaTime;
            float t = Mathf.Clamp01(elapsed / countUpDuration);

            // Easing: замедляем в конце
            float easedT = 1f - Mathf.Pow(1f - t, 3f);
            int currentValue = Mathf.RoundToInt(Mathf.Lerp(from, to, easedT));

            if (finalScore != null)
                finalScore. = $"Счёт: {currentValue:N0}";

            yield return null;
        }

        // Финальное значение
        if (finalScore != null)
            finalScore. = $"Счёт: {to:N0}";
    }

    // ── Обработчики кнопок ────────────────────────────────────

    private void OnRestartClicked()
    {
        Debug.Log("[GameOverUI] Кнопка Restart нажата");
        GameManager.Instance?.RestartGame();
    }

    private void OnMainMenuClicked()
    {
        Debug.Log("[GameOverUI] Кнопка Main Menu нажата");
        GameManager.Instance?.GoToMainMenu();
    }
}
```

### Шаг 5: PlayerHealthUI — полоска здоровья



```csharp
// PlayerHealthUI.cs
using UnityEngine;
using UnityEngine.UI;
using System.Collections;

/// <summary>
/// Отображает здоровье игрока в UI.
/// Подписана на события EventBus.
/// </summary>
public class PlayerHealthUI : MonoBehaviour
{
    [Header("Компоненты UI")]
    [SerializeField] private Slider healthSlider;
    [SerializeField] private Slider damageFlashSlider; // запаздывающая полоска
    [SerializeField] private  health;
    [SerializeField] private Image healthFillImage;

    [Header("Цвета полоски")]
    [SerializeField] private Color highHealthColor  = Color.green;
    [SerializeField] private Color midHealthColor   = Color.yellow;
    [SerializeField] private Color lowHealthColor   = Color.red;

    [Header("Анимация")]
    [SerializeField] private float damageFlashSpeed = 0.3f;
    [SerializeField] private float sliderLerpSpeed  = 5f;

    private float targetHealth = 1f;
    private Coroutine damageFlashCoroutine;

    // ── Unity Lifecycle ──────────────────────────────────────

    private void OnEnable()
    {
        EventBus.OnPlayerHealthChanged += HandleHealthChanged;
        EventBus.OnPlayerDamaged       += HandleDamaged;
        EventBus.OnPlayerDied          += HandlePlayerDied;
    }

    private void OnDisable()
    {
        EventBus.OnPlayerHealthChanged -= HandleHealthChanged;
        EventBus.OnPlayerDamaged       -= HandleDamaged;
        EventBus.OnPlayerDied          -= HandlePlayerDied;
    }

    private void Update()
    {
        // Плавное движение слайдера
        if (healthSlider != null)
        {
            healthSlider.value = Mathf.Lerp(
                healthSlider.value,
                targetHealth,
                Time.deltaTime * sliderLerpSpeed
            );
        }
    }

    // ── Обработчики событий ──────────────────────────────────

    private void HandleHealthChanged(float current, float max)
    {
        float percent = current / max;
        targetHealth = percent;

        // Обновляем текст
        if (health != null)
            health. = $"{Mathf.CeilToInt(current)} / {Mathf.CeilToInt(max)}";

        // Меняем цвет полоски
        UpdateHealthColor(percent);

        Debug.Log($"[HealthUI] HP обновлён: {current:F0}/{max:F0} ({percent:P0})");
    }

    private void HandleDamaged(float damage)
    {
        // Запускаем анимацию вспышки при уроне
        if (damageFlashCoroutine != null)
            StopCoroutine(damageFlashCoroutine);

        damageFlashCoroutine = StartCoroutine(DamageFlashCoroutine());
    }

    private void HandlePlayerDied(PlayerDeathData data)
    {
        Debug.Log("[HealthUI] Игрок умер — скрываем полоску здоровья");

        // Анимируем исчезновение
        StartCoroutine(FadeOutCoroutine());
    }

    // ── Приватные методы ─────────────────────────────────────

    private void UpdateHealthColor(float percent)
    {
        if (healthFillImage == null) return;

        Color targetColor;

        if (percent > 0.6f)
            targetColor = highHealthColor;
        else if (percent > 0.3f)
            targetColor = Color.Lerp(midHealthColor, highHealthColor, (percent - 0.3f) / 0.3f);
        else
            targetColor = Color.Lerp(lowHealthColor, midHealthColor, percent / 0.3f);

        healthFillImage.color = targetColor;
    }

    private IEnumerator DamageFlashCoroutine()
    {
        // Мгновенно сдвигаем вспышку-слайдер, потом плавно возвращаем
        if (damageFlashSlider != null)
        {
            yield return new WaitForSeconds(damageFlashSpeed);

            while (damageFlashSlider.value > targetHealth + 0.01f)
            {
                damageFlashSlider.value = Mathf.Lerp(
                    damageFlashSlider.value,
                    targetHealth,
                    Time.deltaTime * (sliderLerpSpeed * 0.5f)
                );
                yield return null;
            }

            damageFlashSlider.value = targetHealth;
        }
    }

    private IEnumerator FadeOutCoroutine()
    {
        CanvasGroup canvasGroup = GetComponent<CanvasGroup>();
        if (canvasGroup == null) yield break;

        float elapsed = 0f;
        float duration = 0.5f;

        while (elapsed < duration)
        {
            elapsed += Time.deltaTime;
            canvasGroup.alpha = Mathf.Lerp(1f, 0f, elapsed / duration);
            yield return null;
        }

        canvasGroup.alpha = 0f;
        gameObject.SetActive(false);
    }
}
```

### Шаг 6: AudioEventHandler — звук через события



```csharp
// AudioEventHandler.cs
using UnityEngine;

/// <summary>
/// Обрабатывает звуковые события через EventBus.
/// AudioManager не знает ничего об игровой логике — только слушает события.
/// </summary>
public class AudioEventHandler : MonoBehaviour
{
    [Header("Аудио клипы")]
    [SerializeField] private AudioClip playerDiedClip;
    [SerializeField] private AudioClip playerDamagedClip;
    [SerializeField] private AudioClip playerHealedClip;
    [SerializeField] private AudioClip coinCollectedClip;
    [SerializeField] private AudioClip levelCompletedClip;
    [SerializeField] private AudioClip newHighScoreClip;
    [SerializeField] private AudioClip gameOverMusicClip;

    [Header("Источники звука")]
    [SerializeField] private AudioSource sfxSource;
    [SerializeField] private AudioSource musicSource;

    [Header("Настройки")]
    [SerializeField] private float damagedVolume    = 1.0f;
    [SerializeField] private float coinVolume       = 0.7f;
    [SerializeField] private float diedVolume       = 1.0f;

    // ── Unity Lifecycle ──────────────────────────────────────

    private void OnEnable()
    {
        EventBus.OnPlayerDied      += HandlePlayerDied;
        EventBus.OnPlayerDamaged   += HandlePlayerDamaged;
        EventBus.OnPlayerHealed    += HandlePlayerHealed;
        EventBus.OnCoinCollected   += HandleCoinCollected;
        EventBus.OnLevelCompleted  += HandleLevelCompleted;
        EventBus.OnNewHighScore    += HandleNewHighScore;
        EventBus.OnGameOver        += HandleGameOver;
        EventBus.OnGamePaused      += HandleGamePaused;
        EventBus.OnGameResumed     += HandleGameResumed;
    }

    private void OnDisable()
    {
        EventBus.OnPlayerDied      -= HandlePlayerDied;
        EventBus.OnPlayerDamaged   -= HandlePlayerDamaged;
        EventBus.OnPlayerHealed    -= HandlePlayerHealed;
        EventBus.OnCoinCollected   -= HandleCoinCollected;
        EventBus.OnLevelCompleted  -= HandleLevelCompleted;
        EventBus.OnNewHighScore    -= HandleNewHighScore;
        EventBus.OnGameOver        -= HandleGameOver;
        EventBus.OnGamePaused      -= HandleGamePaused;
        EventBus.OnGameResumed     -= HandleGameResumed;
    }

    // ── Обработчики событий ──────────────────────────────────

    private void HandlePlayerDied(PlayerDeathData data)
    {
        PlaySFX(playerDiedClip, diedVolume);
        Debug.Log("[Audio] 🔊 Звук смерти игрока");
    }

    private void HandlePlayerDamaged(float amount)
    {
        PlaySFX(playerDamagedClip, damagedVolume);
    }

    private void HandlePlayerHealed(float amount)
    {
        PlaySFX(playerHealedClip, 0.8f);
    }

    private void HandleCoinCollected(int value)
    {
        // Высота звука зависит от ценности монеты
        float pitch = Mathf.Lerp(0.9f, 1.3f, value / 100f);
        PlaySFX(coinCollectedClip, coinVolume, pitch);
    }

    private void HandleLevelCompleted(int levelNumber)
    {
        PlaySFX(levelCompletedClip, 1f);
    }

    private void HandleNewHighScore(int score)
    {
        PlaySFX(newHighScoreClip, 1f);
    }

    private void HandleGameOver(GameOverData data)
    {
        // Останавливаем игровую музыку и включаем Game Over
        if (musicSource != null)
        {
            musicSource.Stop();
            if (gameOverMusicClip != null)
            {
                musicSource.clip = gameOverMusicClip;
                musicSource.Play();
            }
        }
    }

    private void HandleGamePaused()
    {
        // Замедляем музыку на паузе
        if (musicSource != null)
            musicSource.pitch = 0.8f;
    }

    private void HandleGameResumed()
    {
        if (musicSource != null)
            musicSource.pitch = 1f;
    }

    // ── Вспомогательные методы ────────────────────────────────

    private void PlaySFX(AudioClip clip, float volume = 1f, float pitch = 1f)
    {
        if (clip == null || sfxSource == null) return;

        sfxSource.pitch = pitch;
        sfxSource.PlayOneShot(clip, volume);
    }
}
```

### Шаг 7: EventBusDemo — финальная демонстрация



```csharp
// EventBusDemo.cs
using UnityEngine;
using System.Collections;

/// <summary>
/// Демонстрационный скрипт: имитирует игровой процесс
/// и показывает как работает EventBus.
/// Повесь на GameObject в сцене и нажми Play.
/// </summary>
public class EventBusDemo : MonoBehaviour
{
    [Header("Ссылки")]
    [SerializeField] private PlayerHealth playerHealth;

    [Header("Настройки демо")]
    [SerializeField] private bool autoRunDemo = true;
    [SerializeField] private float actionDelay = 0.8f;

    private void Start()
    {
        if (playerHealth == null)
        {
            // Создаём игрока программно, если не назначен
            GameObject playerGO = new GameObject("Player");
            playerHealth = playerGO.AddComponent<PlayerHealth>();
        }

        if (autoRunDemo)
            StartCoroutine(RunFullDemo());
    }

    private void Update()
    {
        // Ручное управление для теста
        if (Input.GetKeyDown(KeyCode.Alpha1))
            playerHealth.TakeDamage(20f, "Test Damage");

        if (Input.GetKeyDown(KeyCode.Alpha2))
            playerHealth.Heal(15f);

        if (Input.GetKeyDown(KeyCode.Alpha3))
            EventBus.PublishCoinCollected(10);

        if (Input.GetKeyDown(KeyCode.Alpha4))
            playerHealth.TakeDamage(200f, "Instant Kill (Test)");

        if (Input.GetKeyDown(KeyCode.P))
        {
            if (GameManager.Instance != null)
            {
                if (GameManager.Instance.IsPaused) GameManager.Instance.ResumeGame();
                else GameManager.Instance.PauseGame();
            }
        }
    }

    private IEnumerator RunFullDemo()
    {
        Debug.Log("╔════════════════════════════════════════════╗");
        Debug.Log("║          ДЕМОНСТРАЦИЯ EventBus              ║");
        Debug.Log("╚════════════════════════════════════════════╝");

        yield return new WaitForSeconds(actionDelay);

        // ── Начало игры ─────────────────────────────────────────
        Debug.Log("\n▶ Игра начинается...");
        EventBus.PublishGameStarted();

        yield return new WaitForSeconds(actionDelay);

        // ── Сбор монет ──────────────────────────────────────────
        Debug.Log("\n▶ Игрок собирает монеты...");
        EventBus.PublishCoinCollected(10);
        yield return new WaitForSeconds(actionDelay * 0.5f);
        EventBus.PublishCoinCollected(10);
        yield return new WaitForSeconds(actionDelay * 0.5f);
        EventBus.PublishCoinCollected(50);

        yield return new WaitForSeconds(actionDelay);

        // ── Получение урона ──────────────────────────────────────
        Debug.Log("\n▶ Игрок получает урон...");
        playerHealth.TakeDamage(30f, "Goblin");

        yield return new WaitForSeconds(actionDelay);

        playerHealth.TakeDamage(25f, "Orc");

        yield return new WaitForSeconds(actionDelay);

        // ── Лечение ──────────────────────────────────────────────
        Debug.Log("\n▶ Игрок использует зелье...");
        playerHealth.Heal(20f);

        yield return new WaitForSeconds(actionDelay);

        // ── Пауза ────────────────────────────────────────────────
        Debug.Log("\n▶ Игрок ставит паузу...");
        GameManager.Instance?.PauseGame();

        yield return new WaitForSecondsRealtime(actionDelay);

        Debug.Log("\n▶ Игрок снимает паузу...");
        GameManager.Instance?.ResumeGame();

        yield return new WaitForSeconds(actionDelay);

        // ── Убийство врагов ──────────────────────────────────────
        Debug.Log("\n▶ Игрок убивает врагов...");
        playerHealth.RegisterEnemyKill();
        playerHealth.RegisterEnemyKill();
        playerHealth.RegisterEnemyKill();

        yield return new WaitForSeconds(actionDelay);

        // ── Смерть игрока ────────────────────────────────────────
        Debug.Log("\n▶ Финальный удар — игрок умирает...");
        Debug.Log("   Следи за консолью — все подписчики получат уведомление!");
        playerHealth.TakeDamage(999f, "Dragon Boss");

        // После этого момента:
        // 1. PlayerHealth публикует OnPlayerDied
        // 2. GameManager получает событие → сохраняет рекорд → публикует OnGameOver
        // 3. GameOverUI получает OnGameOver → показывает экран
        // 4. PlayerHealthUI получает OnPlayerDied → скрывает полоску
        // 5. AudioEventHandler получает OnPlayerDied → проигрывает звук
        // 6. AchievementSystem получает OnPlayerDied → проверяет достижения

        Debug.Log("\n╔════════════════════════════════════════════╗");
        Debug.Log("║           ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА           ║");
        Debug.Log("║  Все системы сработали через EventBus!     ║");
        Debug.Log("╚════════════════════════════════════════════╝");
    }
}
```

### Ожидаемый вывод в консоли Unity



```csharp
╔════════════════════════════════════════════╗
║          ДЕМОНСТРАЦИЯ EventBus              ║
╚════════════════════════════════════════════╝

▶ Игра начинается...
[EventBus] ► OnGameStarted
[GameManager] Игра началась

▶ Игрок собирает монеты...
[EventBus] ► OnCoinCollected | Монета: 10
[Audio] 🔊 Звук монеты
[EventBus] ► OnCoinCollected | Монета: 10
[EventBus] ► OnCoinCollected | Монета: 50
[Audio] 🔊 Звук монеты (высокий тон)

▶ Игрок получает урон...
[PlayerHealth] Урон от 'Goblin': 30.0 → с учётом брони: 30.0
[EventBus] ► OnPlayerDamaged | Урон: 30
[HealthUI] HP обновлён: 70/100 (70%)
[Audio] 🔊 Звук получения урона

▶ Игрок использует зелье...
[PlayerHealth] Лечение: +20.0 HP. Текущее: 90.0
[EventBus] ► OnPlayerHealed | Лечение: 20
[HealthUI] HP обновлён: 90/100 (90%)

▶ Финальный удар — игрок умирает...
[PlayerHealth] Игрок погиб. Прожил: 4.2с, Счёт: 700, Убийств: 3
[EventBus] ► OnPlayerDied | Причина: Dragon Boss, Очки: 700, Время: 4.2с
[GameManager] Игрок умер. Обрабатываем Game Over...
[GameManager] Новый рекорд: 700!
[HealthUI] Игрок умер — скрываем полоску здоровья
[Audio] 🔊 Звук смерти игрока
[EventBus] ► OnNewHighScore | Рекорд: 700
[EventBus] ► OnGameOver | Счёт: 700, Рекорд: True
[GameOverUI] Показываем экран Game Over
[GameOverUI] Данные заполнены: Счёт=700, Время=00:04, Враги=3
```

---

## Проверь себя

### 🟢 Базовый уровень

**1.** Что выведет этот код?



```csharp
public class TestClass : MonoBehaviour
{
    public delegate void MessageDelegate(string message);
    public event MessageDelegate OnMessage;

    void Start()
    {
        OnMessage += (msg) => Debug.Log($"A: {msg}");
        OnMessage += (msg) => Debug.Log($"B: {msg}");
        OnMessage += (msg) => Debug.Log($"C: {msg}");

        OnMessage?.Invoke("Привет!");

        OnMessage -= (msg) => Debug.Log($"B: {msg}");
        OnMessage?.Invoke("Снова!");
    }
}
```

<details> <summary>Посмотреть ответ</summary>

**Первый вызов:**



```csharp
A: Привет!
B: Привет!
C: Привет!
```

**Второй вызов:**



```csharp
A: Снова!
B: Снова!
C: Снова!
```

**Почему B не отписался?** Lambda-выражения при каждом создании порождают **новый объект делегата**. Попытка отписать `(msg) => Debug.Log($"B: {msg}")` создаёт **новую** лямбду, которая не совпадает с той, что была подписана. Для корректной отписки нужно хранить ссылку на лямбду в переменной:



```csharp
// Правильная отписка лямбды:
MessageDelegate handlerB = (msg) => Debug.Log($"B: {msg}");
OnMessage += handlerB;
OnMessage -= handlerB; // теперь отпишется корректно
```

</details>

---

**2.** Найдите проблему в этом коде:



```csharp
public class EnemySpawner : MonoBehaviour
{
    public static event System.Action<int> OnEnemyKilled;

    public class EnemyCounter : MonoBehaviour
    {
        private int killCount = 0;

        private void Start()
        {
            EnemySpawner.OnEnemyKilled += HandleKill;
        }

        private void HandleKill(int reward)
        {
            killCount++;
            Debug.Log($"Убийство #{killCount}, награда: {reward}");
        }
    }
}
```


---

### 🟡 Средний уровень

**3.** В чём разница между `Action<int>` и `Func<int>`? Напишите пример использования каждого в контексте Unity.

- `Action<int>` — делегат, принимающий `int`, **не возвращающий** значение (`void`)
- `Func<int>` — делегат **без параметров**, **возвращающий** `int`


```csharp
// Action<int> — сообщить системам об изменении счёта (не ждём ответа)
public event System.Action<int> OnScoreChanged;

private void AddScore(int points)
{
    score += points;
    OnScoreChanged?.Invoke(score); // просто уведомляем
}

// Func<int> — запросить текущие деньги игрока (ждём ответ)
public System.Func<int> GetPlayerMoney;

private void Start()
{
    GetPlayerMoney = () => playerWallet.CurrentMoney;
}

private void OpenShop()
{
    int money = GetPlayerMoney?.Invoke() ?? 0;
    Debug.Log($"У игрока {money} монет");
}
```


---

**4.** Реализуйте систему таймера обратного отсчёта с событиями:

- Каждую секунду публикует `OnTimerTick(int secondsLeft)`
- При завершении публикует `OnTimerExpired`
- Можно запустить и остановить снаружи





```csharp
public class GameTimer : MonoBehaviour
{
    [SerializeField] private int startSeconds = 60;

    public event System.Action<int> OnTimerTick;
    public event System.Action OnTimerExpired;

    private int secondsLeft;
    private bool isRunning = false;
    private Coroutine timerCoroutine;

    public void StartTimer()
    {
        if (timerCoroutine != null) StopCoroutine(timerCoroutine);
        secondsLeft = startSeconds;
        isRunning = true;
        timerCoroutine = StartCoroutine(TimerCoroutine());
    }

    public void StopTimer()
    {
        isRunning = false;
        if (timerCoroutine != null)
        {
            StopCoroutine(timerCoroutine);
            timerCoroutine = null;
        }
    }

    private System.Collections.IEnumerator TimerCoroutine()
    {
        while (secondsLeft > 0 && isRunning)
        {
            OnTimerTick?.Invoke(secondsLeft);
            Debug.Log($"⏱ Осталось: {secondsLeft}с");
            yield return new WaitForSeconds(1f);
            secondsLeft--;
        }

        if (isRunning)
        {
            OnTimerTick?.Invoke(0);
            OnTimerExpired?.Invoke();
            Debug.Log("⏰ Время вышло!");
        }
    }
}

// Использование
public class TimerUser : MonoBehaviour
{
    [SerializeField] private GameTimer timer;

    private void OnEnable()
    {
        timer.OnTimerTick    += HandleTick;
        timer.OnTimerExpired += HandleExpired;
    }

    private void OnDisable()
    {
        timer.OnTimerTick    -= HandleTick;
        timer.OnTimerExpired -= HandleExpired;
    }

    private void HandleTick(int seconds)    => Debug.Log($"UI: {seconds}с");
    private void HandleExpired()            => Debug.Log("UI: Время вышло!");
}
```



---

### 🔴 Продвинутый уровень

**5.** Реализуйте типобезопасный `EventBus` с поддержкой произвольных типов событий через generics:



```csharp
Условие:
- EventBus.Subscribe<TEvent>(Action<TEvent> handler)
- EventBus.Unsubscribe<TEvent>(Action<TEvent> handler)
- EventBus.Publish<TEvent>(TEvent eventData)
- Работает с любым struct/class как типом события
```





```csharp
using System;
using System.Collections.Generic;
using UnityEngine;

public static class TypedEventBus
{
    // Словарь: тип события → список обработчиков
    private static readonly Dictionary<Type, Delegate> eventTable
        = new Dictionary<Type, Delegate>();

    public static void Subscribe<TEvent>(Action<TEvent> handler)
    {
        Type eventType = typeof(TEvent);

        if (eventTable.TryGetValue(eventType, out Delegate existing))
        {
            eventTable[eventType] = Delegate.Combine(existing, handler);
        }
        else
        {
            eventTable[eventType] = handler;
        }

        Debug.Log($"[TypedEventBus] Подписка на {eventType.Name}. " +
                  $"Подписчиков: {eventTable[eventType].GetInvocationList().Length}");
    }

    public static void Unsubscribe<TEvent>(Action<TEvent> handler)
    {
        Type eventType = typeof(TEvent);

        if (eventTable.TryGetValue(eventType, out Delegate existing))
        {
            Delegate result = Delegate.Remove(existing, handler);

            if (result == null)
                eventTable.Remove(eventType);
            else
                eventTable[eventType] = result;
        }
    }

    public static void Publish<TEvent>(TEvent eventData)
    {
        Type eventType = typeof(TEvent);

        if (eventTable.TryGetValue(eventType, out Delegate handler))
        {
            Debug.Log($"[TypedEventBus] Публикация {eventType.Name}");
            (handler as Action<TEvent>)?.Invoke(eventData);
        }
        else
        {
            Debug.Log($"[TypedEventBus] Нет подписчиков для {eventType.Name}");
        }
    }

    public static void Clear()
    {
        eventTable.Clear();
        Debug.Log("[TypedEventBus] Все события очищены");
    }
}

// ── Типы событий (struct — нет heap allocation) ──────────────
public struct PlayerDiedEvent
{
    public string Reason;
    public int Score;
    public float SurvivalTime;
}

public struct CoinCollectedEvent
{
    public int Value;
    public Vector3 Position;
}

public struct EnemyKilledEvent
{
    public string EnemyType;
    public int ExpReward;
}

// ── Использование ────────────────────────────────────────────
public class TypedEventBusDemo : MonoBehaviour
{
    private void OnEnable()
    {
        TypedEventBus.Subscribe<PlayerDiedEvent>(OnPlayerDied);
        TypedEventBus.Subscribe<CoinCollectedEvent>(OnCoinCollected);
        TypedEventBus.Subscribe<EnemyKilledEvent>(OnEnemyKilled);
    }

    private void OnDisable()
    {
        TypedEventBus.Unsubscribe<PlayerDiedEvent>(OnPlayerDied);
        TypedEventBus.Unsubscribe<CoinCollectedEvent>(OnCoinCollected);
        TypedEventBus.Unsubscribe<EnemyKilledEvent>(OnEnemyKilled);
    }

    private void Start()
    {
        // Публикуем события — строго типизированно!
        TypedEventBus.Publish(new PlayerDiedEvent
        {
            Reason = "Dragon",
            Score = 1500,
            SurvivalTime = 120f
        });

        TypedEventBus.Publish(new CoinCollectedEvent
        {
            Value = 25,
            Position = Vector3.zero
        });

        TypedEventBus.Publish(new EnemyKilledEvent
        {
            EnemyType = "Goblin",
            ExpReward = 50
        });
    }

    private void OnPlayerDied(PlayerDiedEvent e)
        => Debug.Log($"☠️  Игрок умер от {e.Reason}. Счёт: {e.Score}");

    private void OnCoinCollected(CoinCollectedEvent e)
        => Debug.Log($"💰 Монета {e.Value} в точке {e.Position}");

    private void OnEnemyKilled(EnemyKilledEvent e)
        => Debug.Log($"⚔️  Убит {e.EnemyType}, +{e.ExpReward} XP");
}
```



---

**6.** Бонусный вопрос: что такое **замыкание (closure)** и почему оно может вызвать неожиданное поведение при подписке в цикле?



```csharp
// Что выведет этот код?
public class ClosureDemo : MonoBehaviour
{
    private void Start()
    {
        List<System.Action> actions = new List<System.Action>();

        for (int i = 0; i < 3; i++)
        {
            actions.Add(() => Debug.Log($"Значение i = {i}"));
        }

        foreach (System.Action action in actions)
        {
            action();
        }
    }
}
```



**Вывод (неожиданный для многих):**



```csharp
Значение i = 3
Значение i = 3
Значение i = 3
```

**Почему?** Lambda захватывает **переменную** `i`, а не её **значение** в момент создания. К моменту вызова `action()` цикл уже завершён, `i == 3` — и все три лямбды выводят `3`.

**Исправление — создать локальную копию:**



```csharp
for (int i = 0; i < 3; i++)
{
    int capturedI = i; // локальная копия для каждой итерации
    actions.Add(() => Debug.Log($"Значение i = {capturedI}"));
}

// Теперь вывод:
// Значение i = 0
// Значение i = 1
// Значение i = 2
```

**Практическое применение в Unity:**



```csharp
// ❌ Все кнопки показывают уровень 3
for (int i = 0; i < buttons.Length; i++)
{
    buttons[i].onClick.AddListener(() => LoadLevel(i));
}

// ✅ Каждая кнопка показывает свой уровень
for (int i = 0; i < buttons.Length; i++)
{
    int levelIndex = i;
    buttons[i].onClick.AddListener(() => LoadLevel(levelIndex));
}
```



---

## Итоги



```csharp
✅ Delegate    — тип данных для хранения ссылок на методы
✅ Multicast   — один делегат может содержать много подписчиков
✅ Event       — инкапсулированный делегат: только += и -=, вызов только изнутри
✅ Action      — готовый делегат void без возвращаемого значения
✅ Func        — готовый делегат с возвращаемым значением
✅ Observer    — паттерн, реализованный через события C#
✅ Отписка     — обязательна в OnDisable/OnDestroy, особенно для статических событий
✅ EventBus    — центральная шина событий для слабосвязанной архитектуры
✅ Closure     — лямбды захватывают переменную, а не значение
```

### Что изучить дальше?
- **UnityEvent** — события, настраиваемые прямо в Inspector
- **UniRx / R3** — реактивное программирование в Unity
- **Zenject / VContainer** — dependency injection и signal bus
- **Паттерн Command** — события с возможностью отмены действий
- **Паттерн Mediator** — продвинутая версия EventBus