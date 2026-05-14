## Содержание

- [Введение](#%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5)
	- [Почему это важно в архитектуре игры?](#%D0%9F%D0%BE%D1%87%D0%B5%D0%BC%D1%83%20%D1%8D%D1%82%D0%BE%20%D0%B2%D0%B0%D0%B6%D0%BD%D0%BE%20%D0%B2%20%D0%B0%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D0%B5%20%D0%B8%D0%B3%D1%80%D1%8B?)
- [Базовый и производный класс](#%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B9%20%D0%B8%20%D0%BF%D1%80%D0%BE%D0%B8%D0%B7%D0%B2%D0%BE%D0%B4%D0%BD%D1%8B%D0%B9%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81)
	- [Синтаксис](#%D0%A1%D0%B8%D0%BD%D1%82%D0%B0%D0%BA%D1%81%D0%B8%D1%81)
	- [Наследование от MonoBehaviour в Unity](#%D0%9D%D0%B0%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BE%D1%82%20MonoBehaviour%20%D0%B2%20Unity)
	- [Что наследуется, а что нет?](#%D0%A7%D1%82%D0%BE%20%D0%BD%D0%B0%D1%81%D0%BB%D0%B5%D0%B4%D1%83%D0%B5%D1%82%D1%81%D1%8F,%20%D0%B0%20%D1%87%D1%82%D0%BE%20%D0%BD%D0%B5%D1%82?)
- [Ключевые слова: virtual, override, base, sealed](#%D0%9A%D0%BB%D1%8E%D1%87%D0%B5%D0%B2%D1%8B%D0%B5%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0:%20virtual,%20override,%20base,%20sealed)
	- [virtual — «разрешаю переопределить»](#virtual%20%E2%80%94%20%C2%AB%D1%80%D0%B0%D0%B7%D1%80%D0%B5%D1%88%D0%B0%D1%8E%20%D0%BF%D0%B5%D1%80%D0%B5%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B8%D1%82%D1%8C%C2%BB)
	- [override — «переопределяю метод родителя»](#override%20%E2%80%94%20%C2%AB%D0%BF%D0%B5%D1%80%D0%B5%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D1%8F%D1%8E%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%20%D1%80%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D1%8F%C2%BB)
	- [base — «обращаюсь к родителю»](#base%20%E2%80%94%20%C2%AB%D0%BE%D0%B1%D1%80%D0%B0%D1%89%D0%B0%D1%8E%D1%81%D1%8C%20%D0%BA%20%D1%80%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D1%8E%C2%BB)
	- [Конструкторы и base](#%D0%9A%D0%BE%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D0%BE%D1%80%D1%8B%20%D0%B8%20base)
	- [sealed — «запрещаю наследование»](#sealed%20%E2%80%94%20%C2%AB%D0%B7%D0%B0%D0%BF%D1%80%D0%B5%D1%89%D0%B0%D1%8E%20%D0%BD%D0%B0%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%C2%BB)
- [Полиморфизм](#%D0%9F%D0%BE%D0%BB%D0%B8%D0%BC%D0%BE%D1%80%D1%84%D0%B8%D0%B7%D0%BC)
	- [Практический пример](#%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80)
	- [Полиморфизм и GetComponent в Unity](#%D0%9F%D0%BE%D0%BB%D0%B8%D0%BC%D0%BE%D1%80%D1%84%D0%B8%D0%B7%D0%BC%20%D0%B8%20GetComponent%20%D0%B2%20Unity)
	- [Проверка типа: is и as](#%D0%9F%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0%20%D1%82%D0%B8%D0%BF%D0%B0:%20is%20%D0%B8%20as)
- [Абстрактные классы](#%D0%90%D0%B1%D1%81%D1%82%D1%80%D0%B0%D0%BA%D1%82%D0%BD%D1%8B%D0%B5%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D1%8B)
	- [Проблема: «неполный» базовый класс](#%D0%9F%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0:%20%C2%AB%D0%BD%D0%B5%D0%BF%D0%BE%D0%BB%D0%BD%D1%8B%D0%B9%C2%BB%20%D0%B1%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B9%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81)
	- [Синтаксис](#%D0%A1%D0%B8%D0%BD%D1%82%D0%B0%D0%BA%D1%81%D0%B8%D1%81)
	- [Производные классы обязаны реализовать абстрактные методы](#%D0%9F%D1%80%D0%BE%D0%B8%D0%B7%D0%B2%D0%BE%D0%B4%D0%BD%D1%8B%D0%B5%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D1%8B%20%D0%BE%D0%B1%D1%8F%D0%B7%D0%B0%D0%BD%D1%8B%20%D1%80%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%20%D0%B0%D0%B1%D1%81%D1%82%D1%80%D0%B0%D0%BA%D1%82%D0%BD%D1%8B%D0%B5%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D1%8B)
	- [Когда использовать абстрактный класс?](#%D0%9A%D0%BE%D0%B3%D0%B4%D0%B0%20%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%20%D0%B0%D0%B1%D1%81%D1%82%D1%80%D0%B0%D0%BA%D1%82%D0%BD%D1%8B%D0%B9%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81?)
- [Abstract class vs Interface](#Abstract%20class%20vs%20Interface)
	- [Ключевые различия](#%D0%9A%D0%BB%D1%8E%D1%87%D0%B5%D0%B2%D1%8B%D0%B5%20%D1%80%D0%B0%D0%B7%D0%BB%D0%B8%D1%87%D0%B8%D1%8F)
	- [Пример: когда что выбрать](#%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80:%20%D0%BA%D0%BE%D0%B3%D0%B4%D0%B0%20%D1%87%D1%82%D0%BE%20%D0%B2%D1%8B%D0%B1%D1%80%D0%B0%D1%82%D1%8C)
- [Практическое задание](#%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5)
	- [Задание: иерархия Character → Player / Enemy](#%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5:%20%D0%B8%D0%B5%D1%80%D0%B0%D1%80%D1%85%D0%B8%D1%8F%20Character%20%E2%86%92%20Player%20/%20Enemy)
	- [Character.cs — абстрактный базовый класс](#Character.cs%20%E2%80%94%20%D0%B0%D0%B1%D1%81%D1%82%D1%80%D0%B0%D0%BA%D1%82%D0%BD%D1%8B%D0%B9%20%D0%B1%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B9%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81)
	- [Player.cs — класс игрока](#Player.cs%20%E2%80%94%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%20%D0%B8%D0%B3%D1%80%D0%BE%D0%BA%D0%B0)
	- [Enemy.cs — класс врага](#Enemy.cs%20%E2%80%94%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%20%D0%B2%D1%80%D0%B0%D0%B3%D0%B0)
	- [BossEnemy.cs — босс (наследник Enemy)](#BossEnemy.cs%20%E2%80%94%20%D0%B1%D0%BE%D1%81%D1%81%20(%D0%BD%D0%B0%D1%81%D0%BB%D0%B5%D0%B4%D0%BD%D0%B8%D0%BA%20Enemy))
	- [CombatSystem.cs — демонстрация полиморфизма](#CombatSystem.cs%20%E2%80%94%20%D0%B4%D0%B5%D0%BC%D0%BE%D0%BD%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F%20%D0%BF%D0%BE%D0%BB%D0%B8%D0%BC%D0%BE%D1%80%D1%84%D0%B8%D0%B7%D0%BC%D0%B0)
	- [Ожидаемый вывод в консоли Unity](#%D0%9E%D0%B6%D0%B8%D0%B4%D0%B0%D0%B5%D0%BC%D1%8B%D0%B9%20%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%20%D0%B2%20%D0%BA%D0%BE%D0%BD%D1%81%D0%BE%D0%BB%D0%B8%20Unity)
- [Проверь себя](#%D0%9F%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D1%8C%20%D1%81%D0%B5%D0%B1%D1%8F)
	- [🟢 Базовый уровень](#%F0%9F%9F%A2%20%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B9%20%D1%83%D1%80%D0%BE%D0%B2%D0%B5%D0%BD%D1%8C)
	- [🟡 Средний уровень](#%F0%9F%9F%A1%20%D0%A1%D1%80%D0%B5%D0%B4%D0%BD%D0%B8%D0%B9%20%D1%83%D1%80%D0%BE%D0%B2%D0%B5%D0%BD%D1%8C)
	- [🔴 Продвинутый уровень](#%F0%9F%94%B4%20%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%BD%D1%83%D1%82%D1%8B%D0%B9%20%D1%83%D1%80%D0%BE%D0%B2%D0%B5%D0%BD%D1%8C)
- [Итоги](#%D0%98%D1%82%D0%BE%D0%B3%D0%B8)
	- [Что изучить дальше?](#%D0%A7%D1%82%D0%BE%20%D0%B8%D0%B7%D1%83%D1%87%D0%B8%D1%82%D1%8C%20%D0%B4%D0%B0%D0%BB%D1%8C%D1%88%D0%B5?)


---

## Введение

Представь, что ты разрабатываешь RPG. В игре есть **воин**, **маг**, **лучник** и **разбойник**. У каждого персонажа есть здоровье, урон, способность передвигаться и атаковать. Если писать каждый класс с нуля, ты будешь копировать одни и те же поля и методы снова и снова.

**Наследование** решает эту проблему: ты описываешь общую логику один раз в _базовом классе_ и расширяешь или изменяешь её в _производных классах_.

### Почему это важно в архитектуре игры?

|Без наследования|С наследованием|
|---|---|
|Дублирование кода|Общая логика — в одном месте|
|Сложно вносить изменения|Меняешь базовый класс — изменения везде|
|Труднее масштабировать|Легко добавить нового персонажа|
|Хаотичная структура|Чёткая иерархия классов|

Помимо наследования, мы рассмотрим **полиморфизм** — возможность вызывать одни и те же методы у разных объектов, получая разное поведение. Это основа гибкой игровой архитектуры.

---

## Базовый и производный класс

### Синтаксис

Производный класс указывает родителя через двоеточие `:`.



```csharp
// Базовый класс
public class Animal
{
    public string Name;

    public void Breathe()
    {
        Debug.Log($"{Name} дышит.");
    }
}

// Производный класс
public class Dog : Animal
{
    public void Bark()
    {
        Debug.Log($"{Name} лает: Гав!");
    }
}
```



```csharp
// Использование в Unity (например, в Start() любого MonoBehaviour)
Dog dog = new Dog();
dog.Name = "Рекс";   // поле унаследовано от Animal
dog.Breathe();        // метод унаследован от Animal
dog.Bark();           // собственный метод Dog
```

**Вывод в консоль:**



```csharp
Рекс дышит.
Рекс лает: Гав!
```

### Наследование от MonoBehaviour в Unity

Каждый скрипт в Unity — это уже пример наследования:



```csharp
// Unity-скрипт автоматически наследуется от MonoBehaviour
public class PlayerController : MonoBehaviour
{
    // MonoBehaviour даёт нам Start(), Update(), OnCollisionEnter() и т.д.
    void Start()
    {
        Debug.Log("Игрок создан!");
    }
}
```

Именно поэтому твои скрипты можно вешать на GameObject — `MonoBehaviour` содержит всю необходимую для этого логику.

### Что наследуется, а что нет?



```csharp
public class BaseClass
{
    public int PublicField = 1;          // ✅ наследуется
    protected int ProtectedField = 2;    // ✅ наследуется (только внутри иерархии)
    private int PrivateField = 3;        // ❌ НЕ наследуется
    
    public void PublicMethod() { }       // ✅ наследуется
    protected void ProtectedMethod() { } // ✅ наследуется
    private void PrivateMethod() { }     // ❌ НЕ наследуется
}
```

> **Правило:** `private` — это личное. `protected` — для семьи. `public` — для всех.

---

## Ключевые слова: virtual, override, base, sealed

### virtual — «разрешаю переопределить»

Ключевое слово `virtual` в базовом классе говорит: _«Этот метод можно переопределить в производном классе»_.



```csharp
public class Character : MonoBehaviour
{
    public string CharacterName = "Безымянный";
    public int Health = 100;

    // Метод помечен как virtual — производные классы могут его переопределить
    public virtual void Attack()
    {
        Debug.Log($"{CharacterName} атакует базовой атакой!");
    }

    public virtual void TakeDamage(int damage)
    {
        Health -= damage;
        Debug.Log($"{CharacterName} получил {damage} урона. HP: {Health}");
    }
}
```

### override — «переопределяю метод родителя»



```csharp
public class Warrior : Character
{
    public int SwordDamage = 50;

    // override говорит компилятору: "я заменяю виртуальный метод родителя"
    public override void Attack()
    {
        Debug.Log($"{CharacterName} атакует мечом на {SwordDamage} урона!");
    }
}
```

> ⚠️ **Важно:** нельзя написать `override` без `virtual` в родителе. Компилятор выдаст ошибку.

### base — «обращаюсь к родителю»

`base` позволяет вызвать метод или конструктор **родительского класса** из производного:



```csharp
public class Paladin : Character
{
    public int HolyDamage = 30;

    public override void Attack()
    {
        // Сначала выполняем базовую атаку из Character
        base.Attack();
        
        // Затем добавляем свою логику
        Debug.Log($"{CharacterName} также наносит {HolyDamage} святого урона!");
    }

    public override void TakeDamage(int damage)
    {
        // Паладин получает на 10 урона меньше благодаря святой броне
        int reducedDamage = Mathf.Max(0, damage - 10);
        Debug.Log($"Святая броня поглотила 10 урона!");
        
        // Вызываем родительский метод с уменьшенным уроном
        base.TakeDamage(reducedDamage);
    }
}
```

**Пример использования:**



```csharp
public class CombatDemo : MonoBehaviour
{
    void Start()
    {
        Paladin paladin = new Paladin();
        paladin.CharacterName = "Артас";
        
        paladin.Attack();
        // Вывод:
        // Артас атакует базовой атакой!
        // Артас также наносит 30 святого урона!
        
        paladin.TakeDamage(25);
        // Вывод:
        // Святая броня поглотила 10 урона!
        // Артас получил 15 урона. HP: 85
    }
}
```

### Конструкторы и base

`base` также используется для вызова конструктора родителя:



```csharp
public class Character
{
    public string Name;
    public int Health;

    // Конструктор базового класса
    public Character(string name, int health)
    {
        Name = name;
        Health = health;
        Debug.Log($"Создан персонаж: {Name}");
    }
}

public class Mage : Character
{
    public int Mana;

    // Вызываем конструктор родителя через base(...)
    public Mage(string name, int health, int mana) : base(name, health)
    {
        Mana = mana;
        Debug.Log($"Маг {Name} получил {Mana} маны");
    }
}
```



```csharp
// Создание объекта
Mage mage = new Mage("Гэндальф", 80, 200);
// Вывод:
// Создан персонаж: Гэндальф
// Маг Гэндальф получил 200 маны
```

### sealed — «запрещаю наследование»

`sealed` запрещает дальнейшее наследование от класса или переопределение метода:



```csharp
// Нельзя создать класс, унаследованный от FinalBoss
public sealed class FinalBoss : Character
{
    public override void Attack()
    {
        Debug.Log("Финальный босс наносит сокрушительный удар!");
    }
}

// ❌ Ошибка компиляции: нельзя наследоваться от sealed-класса
// public class SuperFinalBoss : FinalBoss { }
```

Метод тоже можно запечатать:



```csharp
public class Enemy : Character
{
    public override void Attack()
    {
        Debug.Log("Враг атакует!");
    }
    
    // Этот метод нельзя переопределить в классах-наследниках Enemy
    public sealed override void TakeDamage(int damage)
    {
        Debug.Log("Враги получают урон по общим правилам.");
        base.TakeDamage(damage);
    }
}
```

> 💡 **Когда использовать sealed?** Когда ты хочешь зафиксировать поведение и предотвратить случайные изменения. Это также даёт небольшой выигрыш в производительности, так как компилятор может оптимизировать вызовы.

---

## Полиморфизм

**Полиморфизм** (от греч. _много форм_) — это способность обращаться к объектам разных типов через общий интерфейс, получая при этом разное поведение.

### Практический пример

Представь: у тебя есть список всех персонажей на сцене. Ты хочешь вызвать `Attack()` у каждого — не зная заранее, кто именно атакует.



```csharp
public class Character : MonoBehaviour
{
    public string CharacterName;

    public virtual void Attack()
    {
        Debug.Log($"{CharacterName} атакует!");
    }
}

public class Knight : Character
{
    public override void Attack()
    {
        Debug.Log($"{CharacterName} атакует мечом — Клинок чести!");
    }
}

public class Archer : Character
{
    public override void Attack()
    {
        Debug.Log($"{CharacterName} выпускает стрелу — Точный выстрел!");
    }
}

public class Mage : Character
{
    public override void Attack()
    {
        Debug.Log($"{CharacterName} кастует заклинание — Огненный шар!");
    }
}
```



```csharp
public class BattleManager : MonoBehaviour
{
    void Start()
    {
        // Полиморфизм: список базового типа содержит объекты разных производных типов
        List<Character> party = new List<Character>
        {
            new Knight  { CharacterName = "Гарет"  },
            new Archer  { CharacterName = "Леголас" },
            new Mage    { CharacterName = "Мерлин"  }
        };

        Debug.Log("=== Начало раунда ===");

        // Один и тот же вызов — разное поведение у каждого объекта!
        foreach (Character character in party)
        {
            character.Attack();
        }
    }
}
```

**Вывод в консоль:**



```csharp
=== Начало раунда ===
Гарет атакует мечом — Клинок чести!
Леголас выпускает стрелу — Точный выстрел!
Мерлин кастует заклинание — Огненный шар!
```

Именно это и есть полиморфизм: **один вызов — разные реакции**.

### Полиморфизм и GetComponent в Unity

Полиморфизм активно используется в Unity при работе с компонентами:



```csharp
public class EffectManager : MonoBehaviour
{
    // Предположим, на объектах есть компоненты, унаследованные от BaseEffect
    public BaseEffect[] effects;

    void ApplyAllEffects(Character target)
    {
        // Не важно, какой именно эффект — вызываем единый метод
        foreach (BaseEffect effect in effects)
        {
            effect.Apply(target); // полиморфный вызов
        }
    }
}

public class BaseEffect : MonoBehaviour
{
    public virtual void Apply(Character target) { }
}

public class PoisonEffect : BaseEffect
{
    public override void Apply(Character target)
    {
        Debug.Log($"{target.CharacterName} отравлен!");
        // логика яда...
    }
}

public class HealEffect : BaseEffect
{
    public override void Apply(Character target)
    {
        target.Health += 20;
        Debug.Log($"{target.CharacterName} восстановил 20 HP!");
    }
}
```

### Проверка типа: is и as

Иногда нужно узнать реальный тип объекта за полиморфной ссылкой:



```csharp
void ProcessCharacter(Character character)
{
    // is — проверяет тип
    if (character is Mage)
    {
        Debug.Log("Это маг! Надеваем магический иммунитет.");
    }

    // as — пытается привести тип, возвращает null при неудаче
    Mage mage = character as Mage;
    if (mage != null)
    {
        Debug.Log($"Мана мага: {mage.Mana}");
    }

    // Современный синтаксис C# (pattern matching) — is + приведение сразу
    if (character is Archer archer)
    {
        Debug.Log($"Лучник! Дальность: {archer.Range}");
    }
}
```

---

## Абстрактные классы

### Проблема: «неполный» базовый класс

Иногда базовый класс не имеет смысла без конкретной реализации. Например, что делает _просто персонаж_ при атаке? Непонятно. Логику атаки определяет только конкретный тип персонажа.

Для таких ситуаций существуют **абстрактные классы**.

### Синтаксис



```csharp
// abstract — класс нельзя создать напрямую
public abstract class Character : MonoBehaviour
{
    public string CharacterName;
    public int Health;
    public int Damage;

    // Обычный метод — есть реализация, которую можно унаследовать
    public void TakeDamage(int amount)
    {
        Health -= amount;
        Debug.Log($"{CharacterName} получил {amount} урона! Осталось HP: {Health}");

        if (Health <= 0)
        {
            Die();
        }
    }

    // abstract метод — ОБЯЗАТЕЛЕН к реализации в производных классах
    // Здесь нет тела метода — только сигнатура!
    public abstract void Attack();

    // Ещё один абстрактный метод
    public abstract void UseSpecialAbility();

    // Виртуальный метод с базовой реализацией смерти
    protected virtual void Die()
    {
        Debug.Log($"{CharacterName} погиб!");
        gameObject.SetActive(false);
    }
}
```

### Производные классы обязаны реализовать абстрактные методы



```csharp
public class Player : Character
{
    public int ComboCount = 0;

    // ✅ Реализуем обязательный метод
    public override void Attack()
    {
        ComboCount++;
        Debug.Log($"{CharacterName} наносит удар #{ComboCount} на {Damage} урона!");
    }

    // ✅ Реализуем обязательный метод
    public override void UseSpecialAbility()
    {
        Debug.Log($"{CharacterName} активирует БЕРСЕРК! Урон удвоен!");
        Damage *= 2;
    }
    
    // Переопределяем смерть игрока — показываем экран проигрыша
    protected override void Die()
    {
        Debug.Log("GAME OVER");
        // GameManager.Instance.ShowGameOver();
        base.Die();
    }
}
```



```csharp
public class Enemy : Character
{
    public Transform Target; // цель (игрок)

    public override void Attack()
    {
        if (Target != null)
        {
            Debug.Log($"{CharacterName} атакует цель {Target.name} на {Damage} урона!");
        }
    }

    public override void UseSpecialAbility()
    {
        Debug.Log($"{CharacterName} призывает подкрепление!");
        // SpawnReinforcements();
    }
}
```



```csharp
// ❌ Ошибка! Нельзя создать экземпляр абстрактного класса
Character character = new Character(); // Cannot create an instance of the abstract class

// ✅ Можно создавать только конкретные производные классы
Player player = new Player();
Enemy enemy = new Enemy();

// ✅ Но хранить их можно в переменной базового типа (полиморфизм!)
Character anyCharacter = new Player();
```

### Когда использовать абстрактный класс?



```csharp
Используй abstract class, когда:
✅ Базовый класс не имеет смысла без конкретной реализации
✅ Нужно гарантировать, что все наследники реализуют определённые методы
✅ Есть общая логика (код), которую нужно переиспользовать
✅ Все классы в иерархии тесно связаны («является» — is-a)
```

---

## Abstract class vs Interface

Это частый вопрос на собеседованиях и важная тема в архитектуре.

### Ключевые различия

|Характеристика|Abstract Class|Interface|
|---|---|---|
|Создание экземпляра|❌ Нельзя|❌ Нельзя|
|Наследование|Только один класс|Несколько интерфейсов|
|Поля|✅ Есть|❌ Нет (только свойства)|
|Реализация методов|✅ Может быть|✅ С C# 8.0 (default impl.)|
|Конструктор|✅ Есть|❌ Нет|
|Модификаторы доступа|✅ Любые|public по умолчанию|
|Связь|«является» (is-a)|«умеет делать» (can-do)|

### Пример: когда что выбрать



```csharp
// АБСТРАКТНЫЙ КЛАСС: общая природа (все — персонажи)
public abstract class Character : MonoBehaviour
{
    public string Name;
    public int Health;
    
    public abstract void Attack();          // каждый атакует по-своему
    
    public void TakeDamage(int amount)      // общая логика для всех
    {
        Health -= amount;
    }
}

// ИНТЕРФЕЙС: дополнительная способность (не все умеют)
public interface IInteractable
{
    void Interact();        // можно взаимодействовать
    string GetHint();       // подсказка при наведении курсора
}

public interface ISaveable
{
    void Save();            // умеет сохраняться
    void Load();            // умеет загружаться
}

// Класс может наследоваться от одного абстрактного класса
// и реализовывать несколько интерфейсов
public class Player : Character, IInteractable, ISaveable
{
    public override void Attack()
    {
        Debug.Log($"{Name} атакует!");
    }

    // Реализация IInteractable
    public void Interact()
    {
        Debug.Log("Игрок взаимодействует с объектом");
    }

    public string GetHint()
    {
        return "Нажмите E для взаимодействия";
    }

    // Реализация ISaveable
    public void Save()
    {
        PlayerPrefs.SetString("PlayerName", Name);
        PlayerPrefs.SetInt("PlayerHealth", Health);
        Debug.Log("Игра сохранена!");
    }

    public void Load()
    {
        Name = PlayerPrefs.GetString("PlayerName");
        Health = PlayerPrefs.GetInt("PlayerHealth");
        Debug.Log("Игра загружена!");
    }
}

// NPC — тоже персонаж и тоже взаимодействуемый, но не сохраняется
public class NPC : Character, IInteractable
{
    public override void Attack() { /* NPC обычно не атакует */ }
    
    public void Interact()
    {
        Debug.Log("NPC говорит: Привет, путник!");
    }

    public string GetHint()
    {
        return "Нажмите E для разговора";
    }
}
```

> **Правило большого пальца:**
> 
> - Используй **абстрактный класс**, если классы тесно связаны и разделяют общий код.
> - Используй **интерфейс**, чтобы описать _способность_, которую могут иметь совершенно разные объекты.

---

## Практическое задание

Пришло время применить всё на практике! Создадим полноценную иерархию персонажей.

### Задание: иерархия Character → Player / Enemy

**Структура проекта:**



```csharp
📁 Scripts/
  📄 Character.cs      ← абстрактный базовый класс
  📄 Player.cs         ← производный класс игрока
  📄 Enemy.cs          ← производный класс врага
  📄 BossEnemy.cs      ← специальный враг-босс
  📄 CombatSystem.cs   ← система боя (демонстрация полиморфизма)
```

### Character.cs — абстрактный базовый класс



```csharp
using UnityEngine;

/// <summary>
/// Абстрактный базовый класс для всех персонажей игры.
/// Содержит общие данные и логику, а также контракт для производных классов.
/// </summary>
public abstract class Character : MonoBehaviour
{
    [Header("Основные характеристики")]
    public string CharacterName = "Unknown";
    public int MaxHealth = 100;
    public int Damage = 10;

    [Header("Состояние")]
    [SerializeField] protected int currentHealth;

    // Свойство для чтения текущего здоровья снаружи
    public int CurrentHealth => currentHealth;
    public bool IsAlive => currentHealth > 0;

    // -------------------------------------------------------
    // Инициализация
    // -------------------------------------------------------

    protected virtual void Awake()
    {
        currentHealth = MaxHealth;
    }

    // -------------------------------------------------------
    // Абстрактные методы — ОБЯЗАТЕЛЬНЫ к реализации
    // -------------------------------------------------------

    /// <summary>
    /// Логика атаки. Каждый персонаж атакует по-своему.
    /// </summary>
    public abstract void Attack();

    /// <summary>
    /// Особая способность персонажа.
    /// </summary>
    public abstract void UseSpecialAbility();

    // -------------------------------------------------------
    // Виртуальные методы — можно переопределить при желании
    // -------------------------------------------------------

    /// <summary>
    /// Получение урона. Может быть изменено (например, броня).
    /// </summary>
    public virtual void TakeDamage(int amount)
    {
        if (!IsAlive) return;

        currentHealth -= amount;
        currentHealth = Mathf.Clamp(currentHealth, 0, MaxHealth);

        Debug.Log($"⚔️  {CharacterName} получил {amount} урона. " +
                  $"HP: {currentHealth}/{MaxHealth}");

        if (!IsAlive)
        {
            Die();
        }
    }

    /// <summary>
    /// Восстановление здоровья.
    /// </summary>
    public virtual void Heal(int amount)
    {
        if (!IsAlive) return;

        currentHealth = Mathf.Min(currentHealth + amount, MaxHealth);
        Debug.Log($"💚 {CharacterName} восстановил {amount} HP. " +
                  $"HP: {currentHealth}/{MaxHealth}");
    }

    // -------------------------------------------------------
    // Общая логика смерти
    // -------------------------------------------------------

    protected virtual void Die()
    {
        Debug.Log($"💀 {CharacterName} погиб!");
    }

    // -------------------------------------------------------
    // Вспомогательные методы
    // -------------------------------------------------------

    public void PrintStats()
    {
        Debug.Log($"[{GetType().Name}] {CharacterName} | " +
                  $"HP: {currentHealth}/{MaxHealth} | DMG: {Damage}");
    }
}
```

### Player.cs — класс игрока



```csharp
using UnityEngine;

/// <summary>
/// Класс игрового персонажа.
/// Наследует Character, реализует Attack() и UseSpecialAbility().
/// </summary>
public class Player : Character
{
    [Header("Параметры игрока")]
    public int ComboMaxCount = 3;       // максимальное количество ударов в комбо
    public float DodgeChance = 0.2f;    // шанс уклонения (20%)
    public int RageMultiplier = 2;      // множитель урона в режиме ярости

    private int comboCounter = 0;
    private bool isRageActive = false;

    // -------------------------------------------------------
    // Реализация абстрактных методов
    // -------------------------------------------------------

    public override void Attack()
    {
        comboCounter++;
        int attackDamage = isRageActive ? Damage * RageMultiplier : Damage;

        Debug.Log($"🗡️  {CharacterName} наносит удар [{comboCounter}/{ComboMaxCount}] " +
                  $"на {attackDamage} урона!");

        // При завершении комбо — финишер
        if (comboCounter >= ComboMaxCount)
        {
            FinishCombo(attackDamage);
        }
    }

    public override void UseSpecialAbility()
    {
        if (isRageActive)
        {
            Debug.Log($"⚡ {CharacterName}: Режим ярости уже активен!");
            return;
        }

        isRageActive = true;
        Debug.Log($"😤 {CharacterName} входит в РЕЖИМ ЯРОСТИ! " +
                  $"Урон ×{RageMultiplier} на следующие {ComboMaxCount} атак!");
    }

    // -------------------------------------------------------
    // Переопределение виртуальных методов
    // -------------------------------------------------------

    public override void TakeDamage(int amount)
    {
        // Игрок может уклониться
        if (Random.value < DodgeChance)
        {
            Debug.Log($"💨 {CharacterName} уклонился от атаки!");
            return;
        }

        // Иначе — обычное получение урона
        base.TakeDamage(amount);
    }

    protected override void Die()
    {
        Debug.Log($"💔 {CharacterName} пал в бою... Игра окончена.");
        // Здесь можно вызвать: GameManager.Instance.ShowGameOver();
        base.Die();
    }

    // -------------------------------------------------------
    // Приватные методы
    // -------------------------------------------------------

    private void FinishCombo(int baseDamage)
    {
        int finisherDamage = baseDamage * 2;
        Debug.Log($"✨ КОМБО ЗАВЕРШЕНО! Финишер наносит {finisherDamage} урона!");
        comboCounter = 0;
        isRageActive = false;
    }
}
```

### Enemy.cs — класс врага



```csharp
using UnityEngine;

/// <summary>
/// Базовый класс врага.
/// Реализует поведение обычного противника.
/// </summary>
public class Enemy : Character
{
    [Header("Параметры врага")]
    public int ExperienceReward = 50;    // опыт за убийство
    public int GoldReward = 10;          // золото за убийство
    public float AggroRange = 5f;        // дистанция обнаружения игрока

    [Header("Ссылки")]
    public Transform PlayerTransform;    // назначается через Inspector или через Find

    // -------------------------------------------------------
    // Реализация абстрактных методов
    // -------------------------------------------------------

    public override void Attack()
    {
        Debug.Log($"👹 {CharacterName} атакует грубым ударом на {Damage} урона!");
    }

    public override void UseSpecialAbility()
    {
        // Враг издаёт боевой клич — повышает свой урон
        Damage = Mathf.RoundToInt(Damage * 1.5f);
        Debug.Log($"📣 {CharacterName} издаёт боевой клич! Урон увеличен до {Damage}!");
    }

    // -------------------------------------------------------
    // Переопределение смерти
    // -------------------------------------------------------

    protected override void Die()
    {
        Debug.Log($"💀 {CharacterName} уничтожен! " +
                  $"Получено: +{ExperienceReward} XP, +{GoldReward} золота.");
        // Здесь: PlayerStats.AddExperience(ExperienceReward);
        //        PlayerStats.AddGold(GoldReward);
        base.Die();
    }

    // -------------------------------------------------------
    // Логика ИИ (упрощённая)
    // -------------------------------------------------------

    protected virtual void Update()
    {
        if (!IsAlive || PlayerTransform == null) return;

        float distanceToPlayer = Vector3.Distance(
            transform.position, 
            PlayerTransform.position
        );

        if (distanceToPlayer <= AggroRange)
        {
            // Враг замечает игрока — можно добавить chase-логику
        }
    }
}
```

### BossEnemy.cs — босс (наследник Enemy)



```csharp
using UnityEngine;

/// <summary>
/// Враг-босс. Наследует Enemy и добавляет усиленное поведение.
/// Демонстрирует многоуровневое наследование.
/// </summary>
public class BossEnemy : Enemy
{
    [Header("Параметры босса")]
    public int PhaseCount = 2;          // количество фаз
    public float EnrageThreshold = 0.3f; // порог HP для ярости (30%)

    private int currentPhase = 1;
    private bool isEnraged = false;

    // -------------------------------------------------------
    // Переопределение атаки босса
    // -------------------------------------------------------

    public override void Attack()
    {
        if (isEnraged)
        {
            EnragedAttack();
        }
        else
        {
            // Используем базовую атаку врага, но с приставкой БОСС
            Debug.Log($"👾 БОСС {CharacterName} наносит мощный удар на {Damage} урона!");
        }
    }

    public override void UseSpecialAbility()
    {
        Debug.Log($"🌑 БОСС {CharacterName} активирует УЛЬТИМАТИВНЫЙ УДАР!");
        Debug.Log($"💥 Урон области: {Damage * 3} всем врагам!");
    }

    // -------------------------------------------------------
    // Переопределение получения урона (фазы)
    // -------------------------------------------------------

    public override void TakeDamage(int amount)
    {
        base.TakeDamage(amount);
        CheckPhaseTransition();
    }

    // -------------------------------------------------------
    // Переопределение смерти босса
    // -------------------------------------------------------

    protected override void Die()
    {
        Debug.Log("🏆 БОСС ПОВЕРЖЕН! Вы прошли уровень!");
        // Здесь: LevelManager.Instance.CompleteBossLevel();
        base.Die(); // вызовет Enemy.Die() → выдаст награды
    }

    // -------------------------------------------------------
    // Приватные методы
    // -------------------------------------------------------

    private void CheckPhaseTransition()
    {
        float healthPercent = (float)CurrentHealth / MaxHealth;

        if (!isEnraged && healthPercent <= EnrageThreshold)
        {
            EnterEnragedPhase();
        }
    }

    private void EnterEnragedPhase()
    {
        isEnraged = true;
        Damage *= 2;
        Debug.Log($"⚠️  {CharacterName} входит в ФАЗУ ЯРОСТИ! " +
                  $"Урон удвоен: {Damage}!");
    }

    private void EnragedAttack()
    {
        Debug.Log($"🔥 {CharacterName} [ЯРОСТЬ] обрушивает сокрушительный удар на {Damage}!");
        Debug.Log($"🔥 {CharacterName} [ЯРОСТЬ] также атакует дополнительно за {Damage / 2}!");
    }
}
```

### CombatSystem.cs — демонстрация полиморфизма



```csharp
using System.Collections.Generic;
using UnityEngine;

/// <summary>
/// Система боя. Демонстрирует полиморфизм:
/// работаем с Character, не зная точного типа объектов.
/// </summary>
public class CombatSystem : MonoBehaviour
{
    [Header("Участники боя")]
    public Player PlayerCharacter;
    public List<Enemy> Enemies;

    void Start()
    {
        RunCombatDemo();
    }

    void RunCombatDemo()
    {
        Debug.Log("╔══════════════════════════════╗");
        Debug.Log("║      ДЕМОНСТРАЦИЯ БОЯ        ║");
        Debug.Log("╚══════════════════════════════╝");

        // Настраиваем персонажей вручную для демо
        SetupCharacters();

        // Выводим статы всех персонажей (полиморфизм!)
        Debug.Log("\n📊 === НАЧАЛЬНЫЕ СТАТЫ ===");
        PrintAllStats();

        // Раунд 1: игрок атакует всех врагов
        Debug.Log("\n⚔️  === РАУНД 1: Атаки игрока ===");
        PlayerAttackPhase();

        // Раунд 2: враги атакуют игрока
        Debug.Log("\n👹 === РАУНД 2: Атаки врагов ===");
        EnemyAttackPhase();

        // Раунд 3: способности
        Debug.Log("\n✨ === РАУНД 3: Особые способности ===");
        SpecialAbilitiesPhase();

        // Итог
        Debug.Log("\n📊 === ФИНАЛЬНЫЕ СТАТЫ ===");
        PrintAllStats();
    }

    void SetupCharacters()
    {
        // Создаём игрока программно (в реальном проекте — через Inspector)
        if (PlayerCharacter == null)
        {
            GameObject playerGO = new GameObject("Player");
            PlayerCharacter = playerGO.AddComponent<Player>();
            PlayerCharacter.CharacterName = "Герой";
            PlayerCharacter.MaxHealth = 150;
            PlayerCharacter.Damage = 25;
        }

        // Создаём врагов, если не назначены
        if (Enemies == null || Enemies.Count == 0)
        {
            Enemies = new List<Enemy>();

            GameObject goblinGO = new GameObject("Goblin");
            Enemy goblin = goblinGO.AddComponent<Enemy>();
            goblin.CharacterName = "Гоблин";
            goblin.MaxHealth = 60;
            goblin.Damage = 15;
            goblin.ExperienceReward = 30;
            Enemies.Add(goblin);

            GameObject bossGO = new GameObject("DragonBoss");
            BossEnemy boss = bossGO.AddComponent<BossEnemy>();
            boss.CharacterName = "Древний дракон";
            boss.MaxHealth = 300;
            boss.Damage = 40;
            boss.ExperienceReward = 500;
            Enemies.Add(boss);
        }
    }

    void PrintAllStats()
    {
        // Полиморфизм: PlayerCharacter — это Character
        PlayerCharacter.PrintStats();

        // Enemies содержит Enemy и BossEnemy — оба являются Character
        foreach (Character character in Enemies)
        {
            character.PrintStats();
        }
    }

    void PlayerAttackPhase()
    {
        foreach (Enemy enemy in Enemies)
        {
            if (!enemy.IsAlive) continue;

            // Игрок атакует
            PlayerCharacter.Attack();
            // Враг получает урон
            enemy.TakeDamage(PlayerCharacter.Damage);

            Debug.Log("---");
        }
    }

    void EnemyAttackPhase()
    {
        foreach (Enemy enemy in Enemies)
        {
            if (!enemy.IsAlive) continue;

            // Полиморфизм: Attack() вызывает правильную версию (Enemy или BossEnemy)
            enemy.Attack();
            PlayerCharacter.TakeDamage(enemy.Damage);

            Debug.Log("---");
        }
    }

    void SpecialAbilitiesPhase()
    {
        // Полиморфизм: единый вызов UseSpecialAbility() у всех персонажей
        List<Character> allCharacters = new List<Character>();
        allCharacters.Add(PlayerCharacter);
        allCharacters.AddRange(Enemies);

        foreach (Character character in allCharacters)
        {
            if (character.IsAlive)
            {
                character.UseSpecialAbility();
            }
        }
    }
}
```

### Ожидаемый вывод в консоли Unity



```csharp
╔══════════════════════════════╗
║      ДЕМОНСТРАЦИЯ БОЯ        ║
╚══════════════════════════════╝

📊 === НАЧАЛЬНЫЕ СТАТЫ ===
[Player] Герой | HP: 150/150 | DMG: 25
[Enemy] Гоблин | HP: 60/60 | DMG: 15
[BossEnemy] Древний дракон | HP: 300/300 | DMG: 40

⚔️  === РАУНД 1: Атаки игрока ===
🗡️  Герой наносит удар [1/3] на 25 урона!
⚔️  Гоблин получил 25 урона. HP: 35/60
---
🗡️  Герой наносит удар [2/3] на 25 урона!
⚔️  Древний дракон получил 25 урона. HP: 275/300
---

👹 === РАУНД 2: Атаки врагов ===
👹 Гоблин атакует грубым ударом на 15 урона!
⚔️  Герой получил 15 урона. HP: 135/150
---
👾 БОСС Древний дракон наносит мощный удар на 40 урона!
⚔️  Герой получил 40 урона. HP: 95/150
---

✨ === РАУНД 3: Особые способности ===
😤 Герой входит в РЕЖИМ ЯРОСТИ! Урон ×2 на следующие 3 атак!
📣 Гоблин издаёт боевой клич! Урон увеличен до 22!
🌑 БОСС Древний дракон активирует УЛЬТИМАТИВНЫЙ УДАР!
💥 Урон области: 120 всем врагам!

📊 === ФИНАЛЬНЫЕ СТАТЫ ===
[Player] Герой | HP: 95/150 | DMG: 25
[Enemy] Гоблин | HP: 35/60 | DMG: 22
[BossEnemy] Древний дракон | HP: 275/300 | DMG: 40
```

---

## Проверь себя

### 🟢 Базовый уровень

**1.** Что произойдёт при запуске этого кода? Напишите вывод в консоль.



```csharp
public class Vehicle
{
    public string Model = "Базовая модель";
    
    public virtual void Drive()
    {
        Debug.Log($"{Model}: Едем по дороге.");
    }
}

public class SportsCar : Vehicle
{
    public override void Drive()
    {
        Debug.Log($"{Model}: Мчимся со скоростью 300 км/ч!");
    }
}

// В методе Start():
Vehicle car1 = new Vehicle { Model = "Обычная машина" };
Vehicle car2 = new SportsCar { Model = "Ferrari" };

car1.Drive();
car2.Drive();
```

<details> <summary>Посмотреть ответ</summary>



```csharp
Обычная машина: Едем по дороге.
Ferrari: Мчимся со скоростью 300 км/ч!
```

`car2` объявлен как `Vehicle`, но реально содержит `SportsCar`. Благодаря **полиморфизму** вызывается переопределённый метод `SportsCar.Drive()`.

</details>

---

**2.** Найдите **3 ошибки** в этом коде:



```csharp
public abstract class Weapon
{
    private int damage = 10;
    
    public abstract void Use();
    
    public abstract void Reload()
    {
        Debug.Log("Перезарядка...");
    }
}

public class Pistol : Weapon
{
    public void Use()
    {
        Debug.Log("Выстрел!");
    }
}

Weapon w = new Weapon();
```

<details> <summary>Посмотреть ответ</summary>

1. **`abstract` метод `Reload()` имеет тело** — абстрактные методы не могут иметь реализацию (уберите `{}` или уберите `abstract`)
2. **`Pistol.Use()` не помечен `override`** — при переопределении виртуального/абстрактного метода нужно написать `public override void Use()`
3. **`new Weapon()`** — нельзя создать экземпляр абстрактного класса

</details>

---

### 🟡 Средний уровень

**3.** Допишите класс `Archer`, чтобы он:

- Наследовался от `Character` (из практического задания)
- Имел поле `int ArrowCount = 10`
- В `Attack()` выпускал стрелу (уменьшал `ArrowCount` на 1), если стрелы есть, иначе — выводил «Стрелы закончились!»
- В `UseSpecialAbility()` выпускал сразу 3 стрелы за раз

<details> <summary>Посмотреть ответ</summary>



```csharp
public class Archer : Character
{
    public int ArrowCount = 10;

    public override void Attack()
    {
        if (ArrowCount > 0)
        {
            ArrowCount--;
            Debug.Log($"🏹 {CharacterName} выпускает стрелу! " +
                      $"Урон: {Damage}. Осталось стрел: {ArrowCount}");
        }
        else
        {
            Debug.Log($"❌ {CharacterName}: Стрелы закончились!");
        }
    }

    public override void UseSpecialAbility()
    {
        int arrowsToShoot = Mathf.Min(3, ArrowCount);
        
        if (arrowsToShoot == 0)
        {
            Debug.Log($"❌ {CharacterName}: Нет стрел для залпа!");
            return;
        }

        ArrowCount -= arrowsToShoot;
        int totalDamage = Damage * arrowsToShoot;
        Debug.Log($"🏹🏹🏹 {CharacterName} выпускает залп из {arrowsToShoot} стрел! " +
                  $"Суммарный урон: {totalDamage}. Осталось: {ArrowCount}");
    }
}
```

</details>

---

**4.** Объясните своими словами: **в чём разница между `virtual` и `abstract`?** Когда вы бы выбрали каждый из них?

<details> <summary>Посмотреть ответ</summary>

**`virtual`:** метод имеет реализацию по умолчанию, которую производные классы _могут_ переопределить, но не обязаны.

**`abstract`:** метод не имеет реализации. Производные классы _обязаны_ его реализовать.

**Выбор:**

- `virtual` — когда есть разумное поведение по умолчанию (например, базовый `TakeDamage` вычитает HP у всех)
- `abstract` — когда поведение принципиально различается и не имеет «общего варианта» (например, `Attack()` — у каждого персонажа своя атака)

</details>

---

### 🔴 Продвинутый уровень

**5.** Создайте систему с использованием **и** абстрактного класса, **и** интерфейса:



```csharp
Условие:
- Абстрактный класс Trap (ловушка) с полями: damage, isActive
- Абстрактный метод: Trigger()
- Интерфейс IResettable с методом Reset()
- Класс SpikeTrap (ловушка с шипами): при триггере наносит урон, при Reset() становится активной снова
- Класс FireTrap (огненная ловушка): наносит урон по области, НЕ реализует IResettable (одноразовая)
```

<details> <summary>Посмотреть ответ</summary>



```csharp
public interface IResettable
{
    void Reset();
}

public abstract class Trap : MonoBehaviour
{
    public int Damage = 20;
    public bool IsActive = true;

    public abstract void Trigger(Character target);

    protected void Deactivate()
    {
        IsActive = false;
        Debug.Log($"{GetType().Name} деактивирована.");
    }
}

public class SpikeTrap : Trap, IResettable
{
    public override void Trigger(Character target)
    {
        if (!IsActive) return;

        Debug.Log($"💥 Ловушка с шипами! {target.CharacterName} получает {Damage} урона!");
        target.TakeDamage(Damage);
        Deactivate();
    }

    public void Reset()
    {
        IsActive = true;
        Debug.Log("🔄 Ловушка с шипами перезаряжена и снова активна!");
    }
}

public class FireTrap : Trap
{
    public float Radius = 3f;

    public override void Trigger(Character target)
    {
        if (!IsActive) return;

        Debug.Log($"🔥 Огненная ловушка! Взрыв в радиусе {Radius}м! Урон: {Damage}");
        // В реальности: найти все объекты в радиусе и нанести урон
        target.TakeDamage(Damage);
        Deactivate(); // одноразовая — деактивируется навсегда
    }
    // Reset() НЕ реализован — FireTrap одноразовая
}

// Использование:
void DemoTraps()
{
    SpikeTrap spike = new GameObject().AddComponent<SpikeTrap>();
    FireTrap fire = new GameObject().AddComponent<FireTrap>();
    Player player = new GameObject().AddComponent<Player>();

    // Полиморфизм: работаем через базовый тип
    List<Trap> traps = new List<Trap> { spike, fire };
    
    foreach (Trap trap in traps)
    {
        trap.Trigger(player);
    }

    // Только SpikeTrap реализует IResettable
    foreach (Trap trap in traps)
    {
        if (trap is IResettable resettable)
        {
            resettable.Reset(); // вызывается только у SpikeTrap
        }
    }
}
```

</details>

---

**6.** Бонусный вопрос на понимание: что выведет этот код и почему?



```csharp
public class A
{
    public virtual void Print() => Debug.Log("A");
}

public class B : A
{
    public override void Print() => Debug.Log("B");
}

public class C : B
{
    public sealed override void Print() => Debug.Log("C");
}

public class D : C
{
    // Попытка переопределить Print()
    // public override void Print() => Debug.Log("D"); // ← раскомментируйте и проверьте
}

// В Start():
A obj1 = new B();
A obj2 = new C();
A obj3 = new D();

obj1.Print();
obj2.Print();
obj3.Print();
```

<details> <summary>Посмотреть ответ</summary>

**Вывод:**



```csharp
B
C
C
```

**Объяснение:**

- `obj1` — хранит `B`, вызывается `B.Print()` → `"B"`
- `obj2` — хранит `C`, вызывается `C.Print()` → `"C"`
- `obj3` — хранит `D`, но `D` не переопределяет `Print()` (это запрещено — `sealed` в `C`), поэтому вызывается унаследованный `C.Print()` → `"C"`

Если раскомментировать `override` в `D` — будет **ошибка компиляции**, потому что `C.Print()` помечен `sealed`.

</details>

---

## Итоги

Поздравляем! Ты изучил ключевые концепции ООП в контексте Unity:



```csharp
✅ Наследование   — переиспользование кода через иерархию классов
✅ virtual        — метод с реализацией, который можно переопределить
✅ override       — переопределение виртуального/абстрактного метода
✅ base           — обращение к родительскому классу или конструктору
✅ sealed         — запрет дальнейшего переопределения/наследования
✅ Полиморфизм    — один интерфейс, разное поведение
✅ abstract class — шаблон без конкретной реализации
✅ interface      — контракт способностей для разных классов
```

### Что изучить дальше?

- **Паттерн «Компонент»** — как Unity строит архитектуру через компоненты вместо глубокого наследования
- **Паттерн «Стратегия»** — замена наследования при определении поведения
- **ScriptableObject** — данные без наследования MonoBehaviour
- **Generics в C#** — обобщённое программирование для универсальных систем