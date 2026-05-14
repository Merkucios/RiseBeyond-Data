## Содержание
- [Введение](#%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5)
	- [Что такое интерфейс?](#%D0%A7%D1%82%D0%BE%20%D1%82%D0%B0%D0%BA%D0%BE%D0%B5%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81?)
	- [Зачем интерфейсы нужны в играх?](#%D0%97%D0%B0%D1%87%D0%B5%D0%BC%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%D1%8B%20%D0%BD%D1%83%D0%B6%D0%BD%D1%8B%20%D0%B2%20%D0%B8%D0%B3%D1%80%D0%B0%D1%85?)
- [Синтаксис интерфейса](#%D0%A1%D0%B8%D0%BD%D1%82%D0%B0%D0%BA%D1%81%D0%B8%D1%81%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%D0%B0)
	- [Объявление интерфейса](#%D0%9E%D0%B1%D1%8A%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%D0%B0)
	- [Реализация интерфейса](#%D0%A0%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%D0%B0)
	- [Свойства в интерфейсе](#%D0%A1%D0%B2%D0%BE%D0%B9%D1%81%D1%82%D0%B2%D0%B0%20%D0%B2%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%D0%B5)
	- [События в интерфейсе](#%D0%A1%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F%20%D0%B2%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%D0%B5)
	- [Default-реализация (C# 8.0+)](#Default-%D1%80%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20(C#%208.0+))
- [Интерфейс vs Абстрактный класс](#%D0%98%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%20vs%20%D0%90%D0%B1%D1%81%D1%82%D1%80%D0%B0%D0%BA%D1%82%D0%BD%D1%8B%D0%B9%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81)
	- [Когда что выбирать?](#%D0%9A%D0%BE%D0%B3%D0%B4%D0%B0%20%D1%87%D1%82%D0%BE%20%D0%B2%D1%8B%D0%B1%D0%B8%D1%80%D0%B0%D1%82%D1%8C?)
	- [Наглядный пример выбора](#%D0%9D%D0%B0%D0%B3%D0%BB%D1%8F%D0%B4%D0%BD%D1%8B%D0%B9%20%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%20%D0%B2%D1%8B%D0%B1%D0%BE%D1%80%D0%B0)
- [Несколько интерфейсов](#%D0%9D%D0%B5%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%D0%BE%D0%B2)
	- [Объявление нескольких интерфейсов](#%D0%9E%D0%B1%D1%8A%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%B5%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%B8%D1%85%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%D0%BE%D0%B2)
	- [Реализация всех интерфейсов](#%D0%A0%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B2%D1%81%D0%B5%D1%85%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%D0%BE%D0%B2)
	- [Работа через разные интерфейсы](#%D0%A0%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20%D1%80%D0%B0%D0%B7%D0%BD%D1%8B%D0%B5%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%D1%8B)
	- [Разрешение конфликта имён](#%D0%A0%D0%B0%D0%B7%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BA%D0%BE%D0%BD%D1%84%D0%BB%D0%B8%D0%BA%D1%82%D0%B0%20%D0%B8%D0%BC%D1%91%D0%BD)
- [Интерфейсы в Unity](#%D0%98%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%D1%8B%20%D0%B2%20Unity)
	- [IDamageable — всё, что можно повредить](#IDamageable%20%E2%80%94%20%D0%B2%D1%81%D1%91,%20%D1%87%D1%82%D0%BE%20%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE%20%D0%BF%D0%BE%D0%B2%D1%80%D0%B5%D0%B4%D0%B8%D1%82%D1%8C)
	- [IInteractable — всё, с чем можно взаимодействовать](#IInteractable%20%E2%80%94%20%D0%B2%D1%81%D1%91,%20%D1%81%20%D1%87%D0%B5%D0%BC%20%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE%20%D0%B2%D0%B7%D0%B0%D0%B8%D0%BC%D0%BE%D0%B4%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%BE%D0%B2%D0%B0%D1%82%D1%8C)
	- [ICollectible — всё, что можно подобрать](#ICollectible%20%E2%80%94%20%D0%B2%D1%81%D1%91,%20%D1%87%D1%82%D0%BE%20%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE%20%D0%BF%D0%BE%D0%B4%D0%BE%D0%B1%D1%80%D0%B0%D1%82%D1%8C)
- [Практическое задание](#%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5)
	- [Структура проекта](#%D0%A1%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
	- [Шаг 1: Интерфейс IDamageable](#%D0%A8%D0%B0%D0%B3%201:%20%D0%98%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%20IDamageable)
	- [Шаг 2: Класс Player](#%D0%A8%D0%B0%D0%B3%202:%20%D0%9A%D0%BB%D0%B0%D1%81%D1%81%20Player)
	- [Шаг 3: Класс Enemy](#%D0%A8%D0%B0%D0%B3%203:%20%D0%9A%D0%BB%D0%B0%D1%81%D1%81%20Enemy)
	- [Шаг 4: Класс Barrel](#%D0%A8%D0%B0%D0%B3%204:%20%D0%9A%D0%BB%D0%B0%D1%81%D1%81%20Barrel)
	- [Шаг 5: DestructibleWall — четвёртый объект для демонстрации](#%D0%A8%D0%B0%D0%B3%205:%20DestructibleWall%20%E2%80%94%20%D1%87%D0%B5%D1%82%D0%B2%D1%91%D1%80%D1%82%D1%8B%D0%B9%20%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%20%D0%B4%D0%BB%D1%8F%20%D0%B4%D0%B5%D0%BC%D0%BE%D0%BD%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D0%B8)
	- [Шаг 6: RaycastWeapon — оружие, которое ничего не знает о типах](#%D0%A8%D0%B0%D0%B3%206:%20RaycastWeapon%20%E2%80%94%20%D0%BE%D1%80%D1%83%D0%B6%D0%B8%D0%B5,%20%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D0%BE%D0%B5%20%D0%BD%D0%B8%D1%87%D0%B5%D0%B3%D0%BE%20%D0%BD%D0%B5%20%D0%B7%D0%BD%D0%B0%D0%B5%D1%82%20%D0%BE%20%D1%82%D0%B8%D0%BF%D0%B0%D1%85)
	- [Шаг 7: DemoScene — сборка сцены и тест](#%D0%A8%D0%B0%D0%B3%207:%20DemoScene%20%E2%80%94%20%D1%81%D0%B1%D0%BE%D1%80%D0%BA%D0%B0%20%D1%81%D1%86%D0%B5%D0%BD%D1%8B%20%D0%B8%20%D1%82%D0%B5%D1%81%D1%82)
	- [Ожидаемый вывод](#%D0%9E%D0%B6%D0%B8%D0%B4%D0%B0%D0%B5%D0%BC%D1%8B%D0%B9%20%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4)
- [Проверь себя](#%D0%9F%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D1%8C%20%D1%81%D0%B5%D0%B1%D1%8F)
	- [🟢 Базовый уровень](#%F0%9F%9F%A2%20%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B9%20%D1%83%D1%80%D0%BE%D0%B2%D0%B5%D0%BD%D1%8C)
	- [🟡 Средний уровень](#%F0%9F%9F%A1%20%D0%A1%D1%80%D0%B5%D0%B4%D0%BD%D0%B8%D0%B9%20%D1%83%D1%80%D0%BE%D0%B2%D0%B5%D0%BD%D1%8C)
	- [🔴 Продвинутый уровень](#%F0%9F%94%B4%20%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%BD%D1%83%D1%82%D1%8B%D0%B9%20%D1%83%D1%80%D0%BE%D0%B2%D0%B5%D0%BD%D1%8C)
- [Итоги](#%D0%98%D1%82%D0%BE%D0%B3%D0%B8)
	- [Что изучить дальше?](#%D0%A7%D1%82%D0%BE%20%D0%B8%D0%B7%D1%83%D1%87%D0%B8%D1%82%D1%8C%20%D0%B4%D0%B0%D0%BB%D1%8C%D1%88%D0%B5?)


---

## Введение

Представь ситуацию: игрок стреляет из оружия. Пуля летит и попадает в... что-то. Это может быть **враг**, **бочка**, **стена**, **дерево** или **другой игрок**. Как написать код пули так, чтобы он работал для всех этих объектов, не зная заранее, во что она попадёт?

Наивное решение выглядит так:



```csharp
// ❌ Плохо: пуля знает обо всех возможных типах объектов
void OnCollisionEnter(Collision collision)
{
    Player player = collision.gameObject.GetComponent<Player>();
    if (player != null) { player.TakeDamage(10); return; }

    Enemy enemy = collision.gameObject.GetComponent<Enemy>();
    if (enemy != null) { enemy.TakeDamage(10); return; }

    Barrel barrel = collision.gameObject.GetComponent<Barrel>();
    if (barrel != null) { barrel.TakeDamage(10); return; }

    // Добавил новый объект? Придёшь сюда снова...
    // И снова... И снова...
}
```

Каждый раз, добавляя новый объект в игру, ты вынужден изменять код пули. Это нарушает принцип **Open/Closed** (открыт для расширения, закрыт для изменения).

**Правильное решение — интерфейс:**



```csharp
// ✅ Хорошо: пуля знает только об интерфейсе
void OnCollisionEnter(Collision collision)
{
    IDamageable damageable = collision.gameObject.GetComponent<IDamageable>();
    if (damageable != null)
    {
        damageable.TakeDamage(10f);
        // Всё. Не важно, кто это — враг, бочка или дерево.
    }
}
```

### Что такое интерфейс?

**Интерфейс** — это контракт. Он описывает _что_ объект умеет делать, но не _как_ именно он это делает.

Если класс реализует интерфейс, он **гарантирует**, что содержит все методы и свойства, объявленные в этом интерфейсе.



```csharp
Интерфейс — это как розетка в стене.
Любой прибор с вилкой подходящего формата может подключиться.
Розетке не важно, что именно подключено — чайник, телевизор или телефон.
Главное — соответствие контракту.
```

### Зачем интерфейсы нужны в играх?

|Сценарий|Без интерфейса|С интерфейсом|
|---|---|---|
|Пуля наносит урон|Проверяем каждый тип отдельно|`GetComponent<IDamageable>()`|
|Игрок нажимает E|`if Player? if NPC? if Door?`|`GetComponent<IInteractable>()`|
|Магнит притягивает предметы|Список конкретных типов|`GetComponent<ICollectible>()`|
|Сохранение объектов|Знаем каждый класс|`GetComponent<ISaveable>()`|

---

## Синтаксис интерфейса

### Объявление интерфейса



```csharp
// Интерфейсы принято называть с заглавной буквы I
public interface IDamageable
{
    // Методы в интерфейсе:
    // - НЕТ модификатора доступа (по умолчанию public)
    // - НЕТ тела метода (только сигнатура)
    // - НЕТ ключевого слова abstract (оно подразумевается)
    void TakeDamage(float amount);
    void Die();
}
```

### Реализация интерфейса

Класс реализует интерфейс через двоеточие `:` — так же, как наследование:



```csharp
public class Enemy : MonoBehaviour, IDamageable
{
    public float Health = 100f;

    // Реализация метода интерфейса
    // Слово override здесь НЕ нужно (интерфейс — не класс)
    public void TakeDamage(float amount)
    {
        Health -= amount;
        Debug.Log($"Враг получил {amount} урона! HP: {Health}");

        if (Health <= 0)
        {
            Die();
        }
    }

    public void Die()
    {
        Debug.Log("Враг уничтожен!");
        Destroy(gameObject);
    }
}
```

> ⚠️ **Важно:** если класс объявляет реализацию интерфейса, но не реализует **все** его методы — будет ошибка компиляции. Это и есть суть контракта.

### Свойства в интерфейсе

Интерфейс может содержать не только методы, но и **свойства**:



```csharp
public interface ICharacterStats
{
    // Свойство только для чтения
    float MaxHealth { get; }

    // Свойство для чтения и записи
    float CurrentHealth { get; set; }

    // Метод
    bool IsAlive();
}
```



```csharp
public class Player : MonoBehaviour, ICharacterStats
{
    [SerializeField] private float maxHealth = 100f;
    [SerializeField] private float currentHealth;

    // Реализация свойства только для чтения
    public float MaxHealth => maxHealth;

    // Реализация свойства для чтения и записи
    public float CurrentHealth
    {
        get => currentHealth;
        set => currentHealth = Mathf.Clamp(value, 0, maxHealth);
    }

    public bool IsAlive() => currentHealth > 0;

    private void Awake()
    {
        currentHealth = maxHealth;
    }
}
```

### События в интерфейсе



```csharp
public interface IDamageable
{
    void TakeDamage(float amount);

    // Событие тоже можно объявить в интерфейсе
    event System.Action<float> OnDamageTaken;
    event System.Action OnDied;
}
```



```csharp
public class Shield : MonoBehaviour, IDamageable
{
    public float Durability = 50f;

    // Реализация событий
    public event System.Action<float> OnDamageTaken;
    public event System.Action OnDied;

    public void TakeDamage(float amount)
    {
        Durability -= amount;
        OnDamageTaken?.Invoke(amount); // уведомляем подписчиков

        if (Durability <= 0)
        {
            OnDied?.Invoke();
            Destroy(gameObject);
        }
    }
}
```

### Default-реализация (C# 8.0+)

Начиная с C# 8.0, интерфейс может содержать реализацию по умолчанию:



```csharp
public interface ILoggable
{
    string GetName();

    // Метод с реализацией по умолчанию
    void Log()
    {
        // Классы могут использовать эту реализацию или переопределить её
        Debug.Log($"[LOG] {GetName()} — {System.DateTime.Now}");
    }
}
```

> 💡 **Совет:** в Unity (особенно в старых версиях проектов) default-реализации могут быть недоступны из-за версии .NET. Используйте эту возможность осторожно и проверяйте настройки проекта в **Edit → Project Settings → Player → Api Compatibility Level**.

---

## Интерфейс vs Абстрактный класс

Это один из самых частых вопросов при изучении ООП. Вот исчерпывающая таблица:

|Характеристика|Interface|Abstract Class|
|---|---|---|
|Создание экземпляра|❌ Нельзя|❌ Нельзя|
|Количество на класс|✅ Неограниченно|⚠️ Только один|
|Поля (переменные)|❌ Нельзя|✅ Можно|
|Конструктор|❌ Нет|✅ Есть|
|Реализация методов|⚠️ Только default (C# 8+)|✅ Можно|
|Модификаторы доступа|❌ Все публичные|✅ Любые|
|Наследование|Реализация (`IFoo`)|Наследование (`: Foo`)|
|Связь с объектом|«умеет делать» (can-do)|«является» (is-a)|
|Производительность|Чуть медленнее*|Немного быстрее*|
|Версионирование|Сложнее менять|Проще добавлять методы|

> * Разница в производительности минимальна и в 99% случаев несущественна.

### Когда что выбирать?



```csharp
Выбирай ИНТЕРФЕЙС, когда:
✅ Разные несвязанные классы должны иметь одно поведение
   (Бочка, Игрок и Враг — все IDamageable, но не связаны наследованием)
✅ Нужно реализовать несколько "способностей" у одного класса
✅ Хочешь описать контракт без привязки к реализации
✅ Работаешь с dependency injection / тестированием

Выбирай АБСТРАКТНЫЙ КЛАСС, когда:
✅ Классы тесно связаны и разделяют общий код
   (Knight, Mage, Archer — все Character, у всех есть Health, Move())
✅ Нужны общие поля или конструктор
✅ Хочешь дать базовую реализацию с возможностью переопределения
✅ Иерархия: "X является Y" (Knight is a Character)
```

### Наглядный пример выбора



```csharp
// АБСТРАКТНЫЙ КЛАСС: все персонажи — это Character
// У них всех есть Health, они все умеют двигаться
public abstract class Character : MonoBehaviour
{
    protected float health;
    protected float speed;

    public abstract void Attack();

    public virtual void Move(Vector3 direction)
    {
        transform.Translate(direction * speed * Time.deltaTime);
    }
}

// ИНТЕРФЕЙСЫ: дополнительные способности
// Не все персонажи умеют всё это

public interface IDamageable    // можно получить урон
{
    void TakeDamage(float amount);
}

public interface IInteractable  // можно взаимодействовать
{
    void Interact(Player player);
    string GetInteractionHint();
}

public interface ISaveable      // можно сохранить
{
    void Save();
    void Load();
}

// Knight — персонаж, получает урон, сохраняется
public class Knight : Character, IDamageable, ISaveable
{
    public override void Attack() => Debug.Log("Удар мечом!");
    public void TakeDamage(float amount) { health -= amount; }
    public void Save() { /* ... */ }
    public void Load() { /* ... */ }
}

// Chest — НЕ персонаж, но с ним можно взаимодействовать
public class Chest : MonoBehaviour, IInteractable
{
    public void Interact(Player player)   => Debug.Log("Сундук открыт!");
    public string GetInteractionHint()    => "Нажмите E, чтобы открыть";
}

// Barrel — НЕ персонаж, но его можно повредить
public class Barrel : MonoBehaviour, IDamageable
{
    private float durability = 30f;
    public void TakeDamage(float amount)
    {
        durability -= amount;
        if (durability <= 0) Destroy(gameObject);
    }
}
```

---

## Несколько интерфейсов

Один из главных плюсов интерфейсов — класс может реализовать **любое количество** интерфейсов одновременно.

### Объявление нескольких интерфейсов



```csharp
// Базовые интерфейсы
public interface IDamageable
{
    float Health { get; }
    void TakeDamage(float amount);
}

public interface IHealable
{
    void Heal(float amount);
}

public interface IInteractable
{
    void Interact(Player interactor);
    string GetInteractionHint();
}

public interface ISaveable
{
    void Save(string saveKey);
    void Load(string saveKey);
}

public interface IHighlightable
{
    void Highlight(bool isHighlighted);
}
```

### Реализация всех интерфейсов



```csharp
// NPC реализует сразу несколько интерфейсов
public class NPC : MonoBehaviour, IDamageable, IHealable, IInteractable, ISaveable, IHighlightable
{
    [SerializeField] private float maxHealth = 80f;
    [SerializeField] private float currentHealth;
    [SerializeField] private string npcName = "NPC";

    private MeshRenderer meshRenderer;
    private static readonly Color highlightColor = Color.yellow;
    private Color originalColor;

    private void Awake()
    {
        currentHealth = maxHealth;
        meshRenderer = GetComponent<MeshRenderer>();
        if (meshRenderer != null)
            originalColor = meshRenderer.material.color;
    }

    // ── IDamageable ──────────────────────────────────────────
    public float Health => currentHealth;

    public void TakeDamage(float amount)
    {
        currentHealth = Mathf.Max(0, currentHealth - amount);
        Debug.Log($"{npcName} получил {amount} урона. HP: {currentHealth}/{maxHealth}");
    }

    // ── IHealable ────────────────────────────────────────────
    public void Heal(float amount)
    {
        currentHealth = Mathf.Min(maxHealth, currentHealth + amount);
        Debug.Log($"{npcName} восстановил {amount} HP. HP: {currentHealth}/{maxHealth}");
    }

    // ── IInteractable ────────────────────────────────────────
    public void Interact(Player interactor)
    {
        Debug.Log($"{npcName} говорит: Привет, {interactor.name}! Чем могу помочь?");
        // Открыть диалог, квест и т.д.
    }

    public string GetInteractionHint() => $"Поговорить с {npcName}";

    // ── ISaveable ────────────────────────────────────────────
    public void Save(string saveKey)
    {
        PlayerPrefs.SetFloat($"{saveKey}_health", currentHealth);
        PlayerPrefs.SetString($"{saveKey}_name", npcName);
        Debug.Log($"NPC {npcName} сохранён.");
    }

    public void Load(string saveKey)
    {
        currentHealth = PlayerPrefs.GetFloat($"{saveKey}_health", maxHealth);
        npcName = PlayerPrefs.GetString($"{saveKey}_name", npcName);
        Debug.Log($"NPC {npcName} загружен. HP: {currentHealth}");
    }

    // ── IHighlightable ───────────────────────────────────────
    public void Highlight(bool isHighlighted)
    {
        if (meshRenderer == null) return;
        meshRenderer.material.color = isHighlighted ? highlightColor : originalColor;
    }
}
```

### Работа через разные интерфейсы



```csharp
public class SystemsDemo : MonoBehaviour
{
    public NPC npc;

    void Start()
    {
        // Одни и те же объект — но разные системы видят только нужный интерфейс

        // Система боя работает только с IDamageable
        IDamageable damageable = npc;
        damageable.TakeDamage(20f);

        // Система лечения работает только с IHealable
        IHealable healable = npc;
        healable.Heal(10f);

        // Система взаимодействия работает только с IInteractable
        IInteractable interactable = npc;
        Debug.Log(interactable.GetInteractionHint());

        // Система подсветки работает только с IHighlightable
        IHighlightable highlightable = npc;
        highlightable.Highlight(true);
    }
}
```

### Разрешение конфликта имён

Если два интерфейса содержат методы с **одинаковыми именами**, нужна явная реализация:



```csharp
public interface ILogger
{
    void Log(); // логировать данные объекта
}

public interface IPrintable
{
    void Log(); // печатать в консоль
}

public class DataObject : ILogger, IPrintable
{
    private string data = "Секретные данные";

    // Явная реализация для ILogger
    void ILogger.Log()
    {
        Debug.Log($"[LOGGER] Записываю в файл: {data}");
    }

    // Явная реализация для IPrintable
    void IPrintable.Log()
    {
        Debug.Log($"[PRINT] Вывожу на экран: {data}");
    }
}
```



```csharp
// При явной реализации — только через тип интерфейса
DataObject obj = new DataObject();
// obj.Log(); // ❌ Ошибка — неоднозначность

ILogger logger = obj;
logger.Log();       // ✅ "[LOGGER] Записываю в файл: Секретные данные"

IPrintable printable = obj;
printable.Log();    // ✅ "[PRINT] Вывожу на экран: Секретные данные"
```

---

## Интерфейсы в Unity

Рассмотрим три главных интерфейса, которые встречаются в большинстве Unity-проектов.

### IDamageable — всё, что можно повредить



```csharp
/// <summary>
/// Реализуют все объекты, которые могут получать урон.
/// </summary>
public interface IDamageable
{
    float MaxHealth { get; }
    float CurrentHealth { get; }
    bool IsAlive { get; }

    void TakeDamage(float amount, DamageType damageType = DamageType.Physical);
}

// Типы урона — дополнительный контекст
public enum DamageType
{
    Physical,
    Fire,
    Ice,
    Poison,
    Magic
}
```



```csharp
public class Enemy : MonoBehaviour, IDamageable
{
    [SerializeField] private float maxHealth = 100f;
    private float currentHealth;

    public float MaxHealth     => maxHealth;
    public float CurrentHealth => currentHealth;
    public bool IsAlive        => currentHealth > 0;

    private void Awake() => currentHealth = maxHealth;

    public void TakeDamage(float amount, DamageType damageType = DamageType.Physical)
    {
        // Огненные враги устойчивы к огню
        if (damageType == DamageType.Fire)
        {
            amount *= 0.5f;
            Debug.Log("Враг устойчив к огню! Урон снижен.");
        }

        currentHealth -= amount;
        Debug.Log($"Враг получил {amount} урона [{damageType}]. HP: {currentHealth}");

        if (!IsAlive)
        {
            Debug.Log("Враг уничтожен!");
            Destroy(gameObject);
        }
    }
}
```

### IInteractable — всё, с чем можно взаимодействовать



```csharp
/// <summary>
/// Реализуют все объекты, с которыми игрок может взаимодействовать (клавиша E).
/// </summary>
public interface IInteractable
{
    /// <summary>Может ли игрок сейчас взаимодействовать с объектом?</summary>
    bool CanInteract(Player player);

    /// <summary>Выполнить взаимодействие.</summary>
    void Interact(Player player);

    /// <summary>Подсказка на экране при наведении.</summary>
    string GetInteractionHint();
}
```



```csharp
// Дверь — взаимодействуемый объект
public class Door : MonoBehaviour, IInteractable
{
    [SerializeField] private bool isLocked = false;
    [SerializeField] private bool isOpen = false;
    [SerializeField] private string requiredKeyName = "GoldKey";

    public bool CanInteract(Player player)
    {
        // Заперта — проверяем наличие ключа у игрока
        if (isLocked)
            return player.HasItem(requiredKeyName);

        return true;
    }

    public void Interact(Player player)
    {
        if (isLocked)
        {
            player.RemoveItem(requiredKeyName);
            isLocked = false;
            Debug.Log("Дверь разблокирована ключом!");
        }

        isOpen = !isOpen;
        // Анимация открытия/закрытия
        GetComponent<Animator>()?.SetBool("IsOpen", isOpen);
        Debug.Log(isOpen ? "Дверь открыта." : "Дверь закрыта.");
    }

    public string GetInteractionHint()
    {
        if (isLocked) return $"[E] Использовать {requiredKeyName}";
        return isOpen ? "[E] Закрыть дверь" : "[E] Открыть дверь";
    }
}
```



```csharp
// Система взаимодействия игрока — использует только IInteractable
public class InteractionSystem : MonoBehaviour
{
    [SerializeField] private float interactionRange = 2.5f;
    [SerializeField] private Player player;
    [SerializeField] private UnityEngine.UI. hint;

    private IInteractable currentTarget;

    private void Update()
    {
        LookForInteractable();

        if (currentTarget != null && Input.GetKeyDown(KeyCode.E))
        {
            if (currentTarget.CanInteract(player))
            {
                currentTarget.Interact(player);
            }
            else
            {
                Debug.Log("Не могу взаимодействовать сейчас.");
            }
        }
    }

    private void LookForInteractable()
    {
        // Raycast вперёд от камеры
        Ray ray = Camera.main.ScreenPointToRay(new Vector3(Screen.width / 2, Screen.height / 2));

        if (Physics.Raycast(ray, out RaycastHit hit, interactionRange))
        {
            // GetComponent работает с интерфейсами!
            IInteractable interactable = hit.collider.GetComponent<IInteractable>();

            if (interactable != null)
            {
                currentTarget = interactable;

                // Показываем подсказку
                if (hint != null)
                    hint. = interactable.GetInteractionHint();

                return;
            }
        }

        // Ничего не нашли
        currentTarget = null;
        if (hint != null)
            hint. = "";
    }
}
```

### ICollectible — всё, что можно подобрать



```csharp
/// <summary>
/// Реализуют все подбираемые объекты: монеты, зелья, оружие.
/// </summary>
public interface ICollectible
{
    string ItemName { get; }
    bool CanCollect(Player player);
    void Collect(Player player);
}
```



```csharp
// Монета
public class Coin : MonoBehaviour, ICollectible
{
    [SerializeField] private int value = 10;

    public string ItemName => $"Монета ({value})";

    public bool CanCollect(Player player) => true; // монету всегда можно подобрать

    public void Collect(Player player)
    {
        player.AddGold(value);
        Debug.Log($"Подобрано: {ItemName}. Всего золота: {player.Gold}");
        Destroy(gameObject);
    }
}

// Зелье здоровья
public class HealthPotion : MonoBehaviour, ICollectible
{
    [SerializeField] private float healAmount = 30f;

    public string ItemName => "Зелье здоровья";

    // Нельзя подобрать, если здоровье полное
    public bool CanCollect(Player player)
    {
        return player.CurrentHealth < player.MaxHealth;
    }

    public void Collect(Player player)
    {
        player.Heal(healAmount);
        Debug.Log($"Использовано: {ItemName}. Восстановлено {healAmount} HP.");
        Destroy(gameObject);
    }
}
```



```csharp
// Система подбора предметов — использует только ICollectible
public class PickupSystem : MonoBehaviour
{
    [SerializeField] private float pickupRadius = 1.5f;
    [SerializeField] private Player player;

    private void Update()
    {
        // Ищем все коллайдеры в радиусе
        Collider[] colliders = Physics.OverlapSphere(transform.position, pickupRadius);

        foreach (Collider col in colliders)
        {
            ICollectible collectible = col.GetComponent<ICollectible>();

            if (collectible != null && collectible.CanCollect(player))
            {
                collectible.Collect(player);
            }
        }
    }
}
```

---

## Практическое задание

Создадим полноценную систему: игрок стреляет лучом, луч попадает в объект, и если объект реализует `IDamageable` — он получает урон. При этом код стрельбы **ничего не знает** о конкретном типе объекта.

### Структура проекта



```csharp
📁 Scripts/
  📁 Interfaces/
    📄 IDamageable.cs
    📄 IInteractable.cs
  📁 Characters/
    📄 Player.cs
    📄 Enemy.cs
  📁 Objects/
    📄 Barrel.cs
    📄 DestructibleWall.cs
  📁 Weapons/
    📄 RaycastWeapon.cs
  📁 UI/
    📄 DamagePopup.cs
```

### Шаг 1: Интерфейс IDamageable



```csharp
// IDamageable.cs
using UnityEngine;

/// <summary>
/// Контракт для всех объектов, которые могут получать урон.
/// Реализуй этот интерфейс — и объект автоматически станет
/// совместим со всеми системами, работающими с IDamageable.
/// </summary>
public interface IDamageable
{
    /// <summary>Текущее здоровье объекта.</summary>
    float CurrentHealth { get; }

    /// <summary>Максимальное здоровье объекта.</summary>
    float MaxHealth { get; }

    /// <summary>Жив ли объект.</summary>
    bool IsAlive { get; }

    /// <summary>
    /// Нанести урон объекту.
    /// </summary>
    /// <param name="amount">Количество урона (всегда положительное).</param>
    void TakeDamage(float amount);

    /// <summary>Событие: вызывается при получении урона.</summary>
    event System.Action<float> OnDamageTaken;

    /// <summary>Событие: вызывается при уничтожении объекта.</summary>
    event System.Action OnDestroyed;
}
```

### Шаг 2: Класс Player



```csharp
// Player.cs
using UnityEngine;

public class Player : MonoBehaviour, IDamageable
{
    [Header("Характеристики игрока")]
    [SerializeField] private float maxHealth = 150f;
    [SerializeField] private float currentHealth;
    [SerializeField] private int gold = 0;

    // ── IDamageable ──────────────────────────────────────────
    public float MaxHealth     => maxHealth;
    public float CurrentHealth => currentHealth;
    public bool IsAlive        => currentHealth > 0;

    public event System.Action<float> OnDamageTaken;
    public event System.Action OnDestroyed;

    // ── Публичные свойства ───────────────────────────────────
    public int Gold => gold;

    // ── Unity Lifecycle ──────────────────────────────────────
    private void Awake()
    {
        currentHealth = maxHealth;
    }

    // ── IDamageable реализация ───────────────────────────────
    public void TakeDamage(float amount)
    {
        if (!IsAlive) return;

        // Игрок получает на 10% меньше урона (базовая броня)
        float actualDamage = amount * 0.9f;
        currentHealth = Mathf.Max(0, currentHealth - actualDamage);

        Debug.Log($"🛡️  [ИГРОК] Получил {actualDamage:F1} урона. HP: {currentHealth:F0}/{maxHealth}");

        OnDamageTaken?.Invoke(actualDamage);

        if (!IsAlive)
        {
            Die();
        }
    }

    // ── Публичные методы ─────────────────────────────────────
    public void Heal(float amount)
    {
        currentHealth = Mathf.Min(maxHealth, currentHealth + amount);
    }

    public void AddGold(int amount)
    {
        gold += amount;
    }

    public bool HasItem(string itemName)
    {
        // Упрощённая проверка инвентаря
        return false;
    }

    public void RemoveItem(string itemName) { }

    // ── Приватные методы ─────────────────────────────────────
    private void Die()
    {
        Debug.Log("💔 ИГРОК ПОГИБ — GAME OVER");
        OnDestroyed?.Invoke();
        // GameManager.Instance.GameOver();
    }
}
```

### Шаг 3: Класс Enemy



```csharp
// Enemy.cs
using UnityEngine;

public class Enemy : MonoBehaviour, IDamageable
{
    [Header("Характеристики врага")]
    [SerializeField] private string enemyName = "Гоблин";
    [SerializeField] private float maxHealth = 80f;
    [SerializeField] private float currentHealth;
    [SerializeField] private int expReward = 50;

    [Header("Визуальная обратная связь")]
    [SerializeField] private Renderer bodyRenderer;
    private Color originalColor;

    // ── IDamageable ──────────────────────────────────────────
    public float MaxHealth     => maxHealth;
    public float CurrentHealth => currentHealth;
    public bool IsAlive        => currentHealth > 0;

    public event System.Action<float> OnDamageTaken;
    public event System.Action OnDestroyed;

    // ── Unity Lifecycle ──────────────────────────────────────
    private void Awake()
    {
        currentHealth = maxHealth;

        if (bodyRenderer != null)
            originalColor = bodyRenderer.material.color;
    }

    // ── IDamageable реализация ───────────────────────────────
    public void TakeDamage(float amount)
    {
        if (!IsAlive) return;

        currentHealth = Mathf.Max(0, currentHealth - amount);

        Debug.Log($"👹 [{enemyName}] Получил {amount:F1} урона. HP: {currentHealth:F0}/{maxHealth}");

        // Мигание красным при уроне
        StartCoroutine(FlashRed());

        OnDamageTaken?.Invoke(amount);

        if (!IsAlive)
        {
            Die();
        }
    }

    // ── Приватные методы ─────────────────────────────────────
    private void Die()
    {
        Debug.Log($"💀 [{enemyName}] уничтожен! +{expReward} опыта");
        OnDestroyed?.Invoke();
        // PlayerStats.AddExperience(expReward);
        Destroy(gameObject, 0.1f);
    }

    private System.Collections.IEnumerator FlashRed()
    {
        if (bodyRenderer == null) yield break;

        bodyRenderer.material.color = Color.red;
        yield return new WaitForSeconds(0.1f);
        bodyRenderer.material.color = originalColor;
    }
}
```

### Шаг 4: Класс Barrel



```csharp
// Barrel.cs
using UnityEngine;

/// <summary>
/// Бочка — разрушаемый объект окружения.
/// Реализует IDamageable, хотя не является персонажем.
/// Именно для таких случаев и нужен интерфейс, а не наследование!
/// </summary>
public class Barrel : MonoBehaviour, IDamageable
{
    [Header("Характеристики бочки")]
    [SerializeField] private float maxDurability = 30f;
    [SerializeField] private float currentDurability;

    [Header("Взрыв")]
    [SerializeField] private bool isExplosive = false;
    [SerializeField] private float explosionRadius = 4f;
    [SerializeField] private float explosionDamage = 50f;
    [SerializeField] private GameObject explosionVFX;

    // ── IDamageable ──────────────────────────────────────────
    // Переиспользуем термины интерфейса, но семантически это "прочность"
    public float MaxHealth     => maxDurability;
    public float CurrentHealth => currentDurability;
    public bool IsAlive        => currentDurability > 0;

    public event System.Action<float> OnDamageTaken;
    public event System.Action OnDestroyed;

    // ── Unity Lifecycle ──────────────────────────────────────
    private void Awake()
    {
        currentDurability = maxDurability;
    }

    // ── IDamageable реализация ───────────────────────────────
    public void TakeDamage(float amount)
    {
        if (!IsAlive) return;

        currentDurability = Mathf.Max(0, currentDurability - amount);

        Debug.Log($"🛢️  [БОЧКА] Получила {amount:F1} урона. Прочность: " +
                  $"{currentDurability:F0}/{maxDurability}");

        OnDamageTaken?.Invoke(amount);

        if (!IsAlive)
        {
            Destroy();
        }
    }

    // ── Приватные методы ─────────────────────────────────────
    private void Destroy()
    {
        Debug.Log("💥 [БОЧКА] Разрушена!");
        OnDestroyed?.Invoke();

        if (isExplosive)
        {
            Explode();
        }

        // Спавн обломков, партиклов и т.д.
        if (explosionVFX != null)
            Instantiate(explosionVFX, transform.position, Quaternion.identity);

        Destroy(gameObject);
    }

    private void Explode()
    {
        Debug.Log($"💣 Взрыв! Радиус: {explosionRadius}м, урон: {explosionDamage}");

        // Находим всех в радиусе взрыва
        Collider[] colliders = Physics.OverlapSphere(transform.position, explosionRadius);

        foreach (Collider col in colliders)
        {
            // Интерфейс: нам не важно КТО в радиусе — важно, что объект IDamageable
            IDamageable damageable = col.GetComponent<IDamageable>();

            if (damageable != null && damageable != (IDamageable)this)
            {
                // Урон уменьшается с расстоянием
                float distance = Vector3.Distance(transform.position, col.transform.position);
                float falloff = 1f - (distance / explosionRadius);
                float finalDamage = explosionDamage * falloff;

                damageable.TakeDamage(finalDamage);
            }
        }
    }
}
```

### Шаг 5: DestructibleWall — четвёртый объект для демонстрации



```csharp
// DestructibleWall.cs
using UnityEngine;

/// <summary>
/// Разрушаемая стена. Демонстрирует, что IDamageable работает
/// с любым объектом, независимо от его природы.
/// </summary>
public class DestructibleWall : MonoBehaviour, IDamageable
{
    [Header("Характеристики стены")]
    [SerializeField] private float maxHealth = 200f;
    [SerializeField] private float currentHealth;
    [SerializeField] private int cracksStages = 3; // стадии разрушения

    private int currentCrackStage = 0;

    // ── IDamageable ──────────────────────────────────────────
    public float MaxHealth     => maxHealth;
    public float CurrentHealth => currentHealth;
    public bool IsAlive        => currentHealth > 0;

    public event System.Action<float> OnDamageTaken;
    public event System.Action OnDestroyed;

    private void Awake() => currentHealth = maxHealth;

    public void TakeDamage(float amount)
    {
        if (!IsAlive) return;

        currentHealth = Mathf.Max(0, currentHealth - amount);

        Debug.Log($"🧱 [СТЕНА] Получила {amount:F1} урона. HP: {currentHealth:F0}/{maxHealth}");

        UpdateCrackStage();
        OnDamageTaken?.Invoke(amount);

        if (!IsAlive)
        {
            Debug.Log("🧱 [СТЕНА] Разрушена!");
            OnDestroyed?.Invoke();
            Destroy(gameObject);
        }
    }

    private void UpdateCrackStage()
    {
        float healthPercent = currentHealth / maxHealth;
        int newStage = cracksStages - Mathf.CeilToInt(healthPercent * cracksStages);

        if (newStage != currentCrackStage)
        {
            currentCrackStage = newStage;
            Debug.Log($"🧱 [СТЕНА] Стадия разрушения: {currentCrackStage}/{cracksStages}");
            // Менять материал/текстуру в зависимости от стадии
        }
    }
}
```

### Шаг 6: RaycastWeapon — оружие, которое ничего не знает о типах



```csharp
// RaycastWeapon.cs
using UnityEngine;

/// <summary>
/// Оружие на основе Raycast.
/// КЛЮЧЕВОЙ МОМЕНТ: этот класс ничего не знает о Player, Enemy или Barrel.
/// Он работает только с интерфейсом IDamageable.
/// Добавь в игру сколько угодно новых объектов — оружие НЕ НУЖНО МЕНЯТЬ.
/// </summary>
public class RaycastWeapon : MonoBehaviour
{
    [Header("Параметры оружия")]
    [SerializeField] private float damage = 25f;
    [SerializeField] private float range = 50f;
    [SerializeField] private float fireRate = 0.5f;  // выстрелов в секунду

    [Header("Визуальные эффекты")]
    [SerializeField] private LineRenderer bulletTrail;
    [SerializeField] private ParticleSystem muzzleFlash;
    [SerializeField] private Camera playerCamera;

    [Header("Слои объектов")]
    [SerializeField] private LayerMask hitLayers = ~0; // все слои по умолчанию

    private float lastFireTime;

    // ── Стрельба ─────────────────────────────────────────────
    private void Update()
    {
        if (Input.GetMouseButton(0) && CanFire())
        {
            Fire();
        }
    }

    private bool CanFire()
    {
        return Time.time - lastFireTime >= 1f / fireRate;
    }

    private void Fire()
    {
        lastFireTime = Time.time;

        // Определяем начало луча
        Ray ray = playerCamera != null
            ? playerCamera.ViewportPointToRay(new Vector3(0.5f, 0.5f, 0f))
            : new Ray(transform.position, transform.forward);

        Debug.Log($"🔫 Выстрел! Дальность: {range}м, Урон: {damage}");

        // Визуальные эффекты
        muzzleFlash?.Play();

        // ── RAYCAST ───────────────────────────────────────────
        if (Physics.Raycast(ray, out RaycastHit hit, range, hitLayers))
        {
            Debug.Log($"🎯 Луч попал в объект: '{hit.collider.gameObject.name}' " +
                      $"(тип: {hit.collider.gameObject.GetType().Name})");

            // ╔═══════════════════════════════════════════════════╗
            // ║  ГЛАВНЫЙ МОМЕНТ — ПОЛИМОРФИЗМ ЧЕРЕЗ ИНТЕРФЕЙС    ║
            // ║                                                   ║
            // ║  Мы не знаем, Player это, Enemy или Barrel.       ║
            // ║  Спрашиваем: "Ты реализуешь IDamageable?"        ║
            // ║  Если да — наносим урон. Всё.                    ║
            // ╚═══════════════════════════════════════════════════╝
            IDamageable damageable = hit.collider.GetComponent<IDamageable>();

            if (damageable != null)
            {
                damageable.TakeDamage(damage);
                ShowHitMarker(true);  // попали в уязвимую цель
            }
            else
            {
                Debug.Log($"ℹ️  Объект '{hit.collider.gameObject.name}' " +
                          $"не реализует IDamageable — урон не нанесён.");
                ShowHitMarker(false); // попали в неуязвимый объект
            }

            // Отрисовка трассера
            DrawBulletTrail(ray.origin, hit.point);
        }
        else
        {
            Debug.Log("💨 Промах — луч не попал ни в один объект.");
            DrawBulletTrail(ray.origin, ray.origin + ray.direction * range);
        }
    }

    // ── Отображение трассера ──────────────────────────────────
    private void DrawBulletTrail(Vector3 start, Vector3 end)
    {
        if (bulletTrail == null) return;

        bulletTrail.SetPosition(0, start);
        bulletTrail.SetPosition(1, end);
        StartCoroutine(HideTrailAfterDelay(0.05f));
    }

    private System.Collections.IEnumerator HideTrailAfterDelay(float delay)
    {
        yield return new WaitForSeconds(delay);
        if (bulletTrail != null)
        {
            bulletTrail.SetPosition(0, Vector3.zero);
            bulletTrail.SetPosition(1, Vector3.zero);
        }
    }

    // ── Маркер попадания ──────────────────────────────────────
    private void ShowHitMarker(bool isVulnerable)
    {
        // В реальном проекте — показать UI элемент
        Debug.Log(isVulnerable ? "✅ Цель уязвима — урон нанесён!" : "⬜ Объект неуязвим.");
    }
}
```

### Шаг 7: DemoScene — сборка сцены и тест



```csharp
// DemoScene.cs — скрипт для демонстрации всей системы в Start()
using System.Collections.Generic;
using UnityEngine;

public class DemoScene : MonoBehaviour
{
    [Header("Объекты сцены")]
    [SerializeField] private Player player;
    [SerializeField] private Enemy enemy;
    [SerializeField] private Barrel barrel;
    [SerializeField] private DestructibleWall wall;

    private void Start()
    {
        RunDemo();
    }

    private void RunDemo()
    {
        Debug.Log("╔═══════════════════════════════════════╗");
        Debug.Log("║  ДЕМОНСТРАЦИЯ ИНТЕРФЕЙСА IDamageable  ║");
        Debug.Log("╚═══════════════════════════════════════╝\n");

        // ─────────────────────────────────────────────────────
        // Собираем ВСЕ объекты в один список по интерфейсу.
        // Обрати внимание: Player, Enemy, Barrel, Wall —
        // совершенно разные классы, но все реализуют IDamageable
        // ─────────────────────────────────────────────────────
        List<IDamageable> allDamageables = new List<IDamageable>
        {
            player,   // Character
            enemy,    // Character
            barrel,   // Prop
            wall      // Environment
        };

        // Подписываемся на события каждого объекта
        foreach (IDamageable damageable in allDamageables)
        {
            // Замыкание: сохраняем ссылку на текущий объект
            IDamageable captured = damageable;
            captured.OnDamageTaken += (dmg) => OnAnyDamageTaken(captured, dmg);
            captured.OnDestroyed   += () => OnAnyDestroyed(captured);
        }

        Debug.Log("── Статистика до атаки ──────────────────");
        PrintStats(allDamageables);

        Debug.Log("\n── Наносим урон всем объектам ───────────");

        // Главная демонстрация:
        // Один и тот же код наносит урон ВСЕМ объектам,
        // независимо от их типа!
        float[] damageValues = { 20f, 35f, 15f, 60f };

        for (int i = 0; i < allDamageables.Count; i++)
        {
            if (allDamageables[i].IsAlive)
            {
                allDamageables[i].TakeDamage(damageValues[i]);
            }
        }

        Debug.Log("\n── Статистика после атаки ───────────────");
        PrintStats(allDamageables);

        Debug.Log("\n── Имитация стрельбы через Raycast ──────");
        SimulateRaycastHit(allDamageables);
    }

    private void PrintStats(List<IDamageable> damageables)
    {
        foreach (IDamageable d in damageables)
        {
            string typeName = d.GetType().Name;
            string status = d.IsAlive ? "живой" : "уничтожен";
            Debug.Log($"  [{typeName,-18}] HP: {d.CurrentHealth,6:F1} / {d.MaxHealth,-6:F1} | {status}");
        }
    }

    private void SimulateRaycastHit(List<IDamageable> damageables)
    {
        Debug.Log("Луч летит и попадает в случайный объект...");

        // Имитируем попадание в случайный объект
        int randomIndex = Random.Range(0, damageables.Count);
        IDamageable target = damageables[randomIndex];

        if (target.IsAlive)
        {
            Debug.Log($"🎯 Попадание в: {target.GetType().Name}");
            // Код НЕ ЗНАЕТ конкретный тип — только интерфейс
            target.TakeDamage(40f);
        }
        else
        {
            Debug.Log($"Объект уже уничтожен, луч проходит насквозь.");
        }
    }

    // ── Обработчики событий ───────────────────────────────────
    private void OnAnyDamageTaken(IDamageable source, float damage)
    {
        // Здесь можно: показать попап с цифрой урона, обновить UI и т.д.
        string typeName = source.GetType().Name;
        float percent = source.CurrentHealth / source.MaxHealth * 100f;
        Debug.Log($"  [EVENT] {typeName} получил {damage:F1} урона. " +
                  $"Осталось HP: {percent:F0}%");
    }

    private void OnAnyDestroyed(IDamageable source)
    {
        Debug.Log($"  [EVENT] {source.GetType().Name} уничтожен! " +
                  $"Уведомляем все заинтересованные системы...");
    }
}
```

### Ожидаемый вывод



```csharp
╔═══════════════════════════════════════╗
║  ДЕМОНСТРАЦИЯ ИНТЕРФЕЙСА IDamageable  ║
╚═══════════════════════════════════════╝

── Статистика до атаки ──────────────────
  [Player            ] HP:  150.0 / 150.0 | живой
  [Enemy             ] HP:   80.0 / 80.0  | живой
  [Barrel            ] HP:   30.0 / 30.0  | живой
  [DestructibleWall  ] HP:  200.0 / 200.0 | живой

── Наносим урон всем объектам ───────────
🛡️  [ИГРОК] Получил 18.0 урона. HP: 132/150
  [EVENT] Player получил 18.0 урона. Осталось HP: 88%
👹 [Гоблин] Получил 35.0 урона. HP: 45/80
  [EVENT] Enemy получил 35.0 урона. Осталось HP: 56%
🛢️  [БОЧКА] Получила 15.0 урона. Прочность: 15/30
  [EVENT] Barrel получил 15.0 урона. Осталось HP: 50%
🧱 [СТЕНА] Получила 60.0 урона. HP: 140/200
🧱 [СТЕНА] Стадия разрушения: 1/3
  [EVENT] DestructibleWall получил 60.0 урона. Осталось HP: 70%

── Статистика после атаки ───────────────
  [Player            ] HP:  132.0 / 150.0 | живой
  [Enemy             ] HP:   45.0 / 80.0  | живой
  [Barrel            ] HP:   15.0 / 30.0  | живой
  [DestructibleWall  ] HP:  140.0 / 200.0 | живой

── Имитация стрельбы через Raycast ──────
Луч летит и попадает в случайный объект...
🎯 Попадание в: Enemy
👹 [Гоблин] Получил 40.0 урона. HP: 5/80
  [EVENT] Enemy получил 40.0 урона. Осталось HP: 6%
```

---

## Проверь себя

### 🟢 Базовый уровень

**1.** Что выведет этот код? Будет ли ошибка компиляции?



```csharp
public interface IMovable
{
    void Move(Vector3 direction);
    float Speed { get; }
}

public class Car : IMovable
{
    public float Speed => 60f;

    public void Move(Vector3 direction)
    {
        Debug.Log($"Машина едет со скоростью {Speed}");
    }
}

public class Boat : IMovable
{
    public float Speed => 15f;

    public void Move(Vector3 direction)
    {
        Debug.Log($"Лодка плывёт со скоростью {Speed}");
    }
}

// В Start():
List<IMovable> vehicles = new List<IMovable> { new Car(), new Boat() };
foreach (IMovable v in vehicles)
{
    v.Move(Vector3.forward);
}
```

<details> <summary>Посмотреть ответ</summary>

Ошибки компиляции **нет**. Вывод:



```csharp
Машина едет со скоростью 60
Лодка плывёт со скоростью 15
```

Это классический полиморфизм через интерфейс: список типа `IMovable` содержит разные объекты, но мы обращаемся к ним через единый контракт.

</details>

---

**2.** Найдите **все ошибки** в этом коде:



```csharp
public interface IAttackable
{
    private int damage = 10;  // поле

    void Attack();

    void Defend()             // метод с телом
    {
        Debug.Log("Защита!");
    }
}

public class Soldier : IAttackable
{
    public override void Attack()
    {
        Debug.Log("Солдат атакует!");
    }
}

IAttackable s = new IAttackable();
```

<details> <summary>Посмотреть ответ</summary>

**Ошибка 1:** `private int damage = 10` — в интерфейсе **нельзя объявлять поля**. Только свойства, методы, события.

**Ошибка 2:** `void Defend() { ... }` — метод с реализацией в интерфейсе допустим только с **C# 8.0+** (default interface methods). В более ранних версиях — ошибка.

**Ошибка 3:** `public override void Attack()` — в реализации интерфейса **не нужно** слово `override`. Правильно: `public void Attack()`.

**Ошибка 4:** `new IAttackable()` — **нельзя создать экземпляр интерфейса**.

</details>

---

### 🟡 Средний уровень

**3.** Реализуйте интерфейс `IInteractable` для класса `Lever` (рычаг):

- При взаимодействии переключает состояние (`isOn` / `isOff`)
- `GetInteractionHint()` возвращает разный текст в зависимости от состояния
- При активации отправляет сообщение в Debug.Log и вызывает Unity Event

<details> <summary>Посмотреть ответ</summary>



```csharp
using UnityEngine;
using UnityEngine.Events;

public class Lever : MonoBehaviour, IInteractable
{
    [SerializeField] private bool isOn = false;
    [SerializeField] private UnityEvent onActivated;
    [SerializeField] private UnityEvent onDeactivated;

    public bool CanInteract(Player player) => true;

    public void Interact(Player player)
    {
        isOn = !isOn;

        if (isOn)
        {
            Debug.Log("🔛 Рычаг включён!");
            onActivated?.Invoke();
        }
        else
        {
            Debug.Log("🔴 Рычаг выключен!");
            onDeactivated?.Invoke();
        }

        // Анимация поворота рычага
        GetComponent<Animator>()?.SetBool("IsOn", isOn);
    }

    public string GetInteractionHint()
    {
        return isOn ? "[E] Выключить рычаг" : "[E] Включить рычаг";
    }
}
```

</details>

---

**4.** Объясните разницу между этими двумя вариантами. Какой правильный и почему?



```csharp
// Вариант A
public class EnemySpawner : MonoBehaviour
{
    public Enemy enemy;

    void DealDamage(float amount)
    {
        enemy.TakeDamage(amount);
    }
}

// Вариант B
public class EnemySpawner : MonoBehaviour
{
    public IDamageable target;

    void DealDamage(float amount)
    {
        target.TakeDamage(amount);
    }
}
```

<details> <summary>Посмотреть ответ</summary>

**Вариант B правильный.** Вот почему:

**Вариант A** жёстко связан с типом `Enemy`. Если понадобится наносить урон `Barrel` или `Player` — придётся менять класс `EnemySpawner`.

**Вариант B** работает с интерфейсом `IDamageable`. Это значит:

- `target` может быть `Enemy`, `Player`, `Barrel` или **любым будущим классом**, реализующим `IDamageable`
- `EnemySpawner` **не нужно менять** при добавлении новых типов объектов
- Код следует принципу **Dependency Inversion** — зависим от абстракции, а не от конкретного класса

</details>

---

### 🔴 Продвинутый уровень

**5.** Создайте систему сохранения на основе интерфейса `ISaveable`:



```csharp
Условие:
- Интерфейс ISaveable: методы Save(string key) и Load(string key)
- Класс SaveSystem: находит все объекты на сцене, реализующие ISaveable,
  и сохраняет/загружает их через PlayerPrefs
- Класс PlayerData : ISaveable — сохраняет позицию и здоровье
- Класс EnemyData : ISaveable — сохраняет позицию и состояние (живой/мёртвый)
```

<details> <summary>Посмотреть ответ</summary>



```csharp
// Интерфейс
public interface ISaveable
{
    void Save(string key);
    void Load(string key);
}

// Система сохранения — ничего не знает о конкретных классах
public class SaveSystem : MonoBehaviour
{
    private MonoBehaviour[] allObjects;

    public void SaveAll()
    {
        allObjects = FindObjectsOfType<MonoBehaviour>();
        int savedCount = 0;

        foreach (MonoBehaviour obj in allObjects)
        {
            if (obj is ISaveable saveable)
            {
                string key = $"{obj.GetType().Name}_{obj.GetInstanceID()}";
                saveable.Save(key);
                savedCount++;
            }
        }

        PlayerPrefs.Save();
        Debug.Log($"✅ Сохранено объектов: {savedCount}");
    }

    public void LoadAll()
    {
        allObjects = FindObjectsOfType<MonoBehaviour>();
        int loadedCount = 0;

        foreach (MonoBehaviour obj in allObjects)
        {
            if (obj is ISaveable saveable)
            {
                string key = $"{obj.GetType().Name}_{obj.GetInstanceID()}";
                saveable.Load(key);
                loadedCount++;
            }
        }

        Debug.Log($"📂 Загружено объектов: {loadedCount}");
    }
}

// Данные игрока
public class PlayerData : MonoBehaviour, ISaveable
{
    private float health = 100f;

    public void Save(string key)
    {
        PlayerPrefs.SetFloat($"{key}_health", health);
        PlayerPrefs.SetFloat($"{key}_posX", transform.position.x);
        PlayerPrefs.SetFloat($"{key}_posY", transform.position.y);
        PlayerPrefs.SetFloat($"{key}_posZ", transform.position.z);
        Debug.Log($"💾 PlayerData сохранён: HP={health}, pos={transform.position}");
    }

    public void Load(string key)
    {
        health = PlayerPrefs.GetFloat($"{key}_health", 100f);
        float x = PlayerPrefs.GetFloat($"{key}_posX", 0f);
        float y = PlayerPrefs.GetFloat($"{key}_posY", 0f);
        float z = PlayerPrefs.GetFloat($"{key}_posZ", 0f);
        transform.position = new Vector3(x, y, z);
        Debug.Log($"📂 PlayerData загружен: HP={health}, pos={transform.position}");
    }
}

// Данные врага
public class EnemyData : MonoBehaviour, ISaveable
{
    private bool isAlive = true;

    public void Save(string key)
    {
        PlayerPrefs.SetInt($"{key}_alive", isAlive ? 1 : 0);
        PlayerPrefs.SetFloat($"{key}_posX", transform.position.x);
        PlayerPrefs.SetFloat($"{key}_posZ", transform.position.z);
        Debug.Log($"💾 EnemyData сохранён: alive={isAlive}");
    }

    public void Load(string key)
    {
        isAlive = PlayerPrefs.GetInt($"{key}_alive", 1) == 1;
        float x = PlayerPrefs.GetFloat($"{key}_posX", transform.position.x);
        float z = PlayerPrefs.GetFloat($"{key}_posZ", transform.position.z);
        transform.position = new Vector3(x, transform.position.y, z);
        gameObject.SetActive(isAlive);
        Debug.Log($"📂 EnemyData загружен: alive={isAlive}");
    }
}
```

</details>

---

**6.** Бонус — вопрос на понимание. Почему этот код **не скомпилируется**, и как его исправить?



```csharp
public interface IUsable
{
    void Use();
}

public class MedKit : MonoBehaviour, IUsable
{
    public void Use() => Debug.Log("Аптечка использована!");
}

public class Grenade : MonoBehaviour, IUsable
{
    public void Use() => Debug.Log("Граната брошена!");
}

// В Update():
IUsable currentItem = GetEquippedItem();

// Пытаемся получить имя объекта
Debug.Log(currentItem.name); // ???
```

<details> <summary>Посмотреть ответ</summary>

**Проблема:** `IUsable` не содержит свойство `name`. Компилятор видит переменную типа `IUsable` и знает только то, что описано в интерфейсе.

**Варианты исправления:**



```csharp
// Вариант 1: добавить имя в интерфейс
public interface IUsable
{
    string ItemName { get; }
    void Use();
}

// Вариант 2: приведение типа (если знаем, что это MonoBehaviour)
MonoBehaviour mono = currentItem as MonoBehaviour;
if (mono != null)
    Debug.Log(mono.name);

// Вариант 3: pattern matching
if (currentItem is MonoBehaviour mb)
    Debug.Log(mb.name);

// Вариант 4: расширить интерфейс (наследование интерфейсов)
public interface IUsableItem : IUsable
{
    string ItemName { get; }
}
```

**Лучший вариант** для Unity — добавить нужные данные в интерфейс (Вариант 1), чтобы не зависеть от конкретных типов реализации.

</details>

---

## Итоги



```csharp
✅ Интерфейс — контракт: "что умеет делать", а не "кто такой"
✅ GetComponent<IInterface>() — работает в Unity для любого типа
✅ Один класс — множество интерфейсов (в отличие от наследования)
✅ Интерфейс не знает о реализации — реализация знает об интерфейсе
✅ IDamageable, IInteractable, ICollectible — три кита Unity-разработки
✅ Raycast + интерфейс = код, который не нужно менять при добавлении новых объектов
```

### Что изучить дальше?

- **Паттерн «Наблюдатель»** — события и интерфейсы вместе
- **Dependency Injection в Unity** — Zenject / VContainer
- **ScriptableObject + интерфейсы** — гибкая система предметов
- **SOLID принципы** — почему интерфейсы делают код поддерживаемым