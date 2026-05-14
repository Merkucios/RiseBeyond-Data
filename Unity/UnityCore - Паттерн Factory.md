## Содержание

- [1. Введение — проблема прямого Instantiate {#введение}](#1.%20%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%E2%80%94%20%D0%BF%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0%20%D0%BF%D1%80%D1%8F%D0%BC%D0%BE%D0%B3%D0%BE%20Instantiate%20%7B#%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%7D)
	- [Как выглядит проблемный код](#%D0%9A%D0%B0%D0%BA%20%D0%B2%D1%8B%D0%B3%D0%BB%D1%8F%D0%B4%D0%B8%D1%82%20%D0%BF%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%BD%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%B4)
	- [Цепочка проблем](#%D0%A6%D0%B5%D0%BF%D0%BE%D1%87%D0%BA%D0%B0%20%D0%BF%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC)
	- [Что нарушает такой подход](#%D0%A7%D1%82%D0%BE%20%D0%BD%D0%B0%D1%80%D1%83%D1%88%D0%B0%D0%B5%D1%82%20%D1%82%D0%B0%D0%BA%D0%BE%D0%B9%20%D0%BF%D0%BE%D0%B4%D1%85%D0%BE%D0%B4)
	- [Что даёт паттерн Factory](#%D0%A7%D1%82%D0%BE%20%D0%B4%D0%B0%D1%91%D1%82%20%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%20Factory)
- [2. Simple Factory — статический метод создания {#simple-factory}](#2.%20Simple%20Factory%20%E2%80%94%20%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%20%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F%20%7B#simple-factory%7D)
	- [Базовая архитектура](#%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D1%8F%20%D0%B0%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D0%B0)
	- [Реализация Simple Factory](#%D0%A0%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20Simple%20Factory)
	- [Использование Simple Factory](#%D0%98%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20Simple%20Factory)
	- [Ограничения Simple Factory](#%D0%9E%D0%B3%D1%80%D0%B0%D0%BD%D0%B8%D1%87%D0%B5%D0%BD%D0%B8%D1%8F%20Simple%20Factory)
- [3. Factory Method — абстрактная фабрика через наследование {#factory-method}](#3.%20Factory%20Method%20%E2%80%94%20%D0%B0%D0%B1%D1%81%D1%82%D1%80%D0%B0%D0%BA%D1%82%D0%BD%D0%B0%D1%8F%20%D1%84%D0%B0%D0%B1%D1%80%D0%B8%D0%BA%D0%B0%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20%D0%BD%D0%B0%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%7B#factory-method%7D)
	- [Диаграмма паттерна](#%D0%94%D0%B8%D0%B0%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B0%20%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%D0%B0)
	- [Реализация](#%D0%A0%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F)
	- [Использование Factory Method](#%D0%98%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20Factory%20Method)
	- [Когда использовать Factory Method](#%D0%9A%D0%BE%D0%B3%D0%B4%D0%B0%20%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%20Factory%20Method)
- [4. Abstract Factory — семейства объектов {#abstract-factory}](#4.%20Abstract%20Factory%20%E2%80%94%20%D1%81%D0%B5%D0%BC%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%B0%20%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BE%D0%B2%20%7B#abstract-factory%7D)
	- [Концепция семейств](#%D0%9A%D0%BE%D0%BD%D1%86%D0%B5%D0%BF%D1%86%D0%B8%D1%8F%20%D1%81%D0%B5%D0%BC%D0%B5%D0%B9%D1%81%D1%82%D0%B2)
	- [Реализация Abstract Factory](#%D0%A0%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20Abstract%20Factory)
	- [Использование Abstract Factory](#%D0%98%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20Abstract%20Factory)
- [5. Фабрика + ScriptableObject для конфигурации {#scriptableobject}](#5.%20%D0%A4%D0%B0%D0%B1%D1%80%D0%B8%D0%BA%D0%B0%20+%20ScriptableObject%20%D0%B4%D0%BB%D1%8F%20%D0%BA%D0%BE%D0%BD%D1%84%D0%B8%D0%B3%D1%83%D1%80%D0%B0%D1%86%D0%B8%D0%B8%20%7B#scriptableobject%7D)
	- [Данные врага в ScriptableObject](#%D0%94%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D0%B2%D1%80%D0%B0%D0%B3%D0%B0%20%D0%B2%20ScriptableObject)
	- [Универсальный компонент врага](#%D0%A3%D0%BD%D0%B8%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BC%D0%BF%D0%BE%D0%BD%D0%B5%D0%BD%D1%82%20%D0%B2%D1%80%D0%B0%D0%B3%D0%B0)
	- [Фабрика на основе ScriptableObject](#%D0%A4%D0%B0%D0%B1%D1%80%D0%B8%D0%BA%D0%B0%20%D0%BD%D0%B0%20%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%B5%20ScriptableObject)
	- [Настройка в Unity Editor](#%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0%20%D0%B2%20Unity%20Editor)
- [6. Фабрика + Object Pool — комбинирование паттернов {#pool-factory}](#6.%20%D0%A4%D0%B0%D0%B1%D1%80%D0%B8%D0%BA%D0%B0%20+%20Object%20Pool%20%E2%80%94%20%D0%BA%D0%BE%D0%BC%D0%B1%D0%B8%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%D0%BE%D0%B2%20%7B#pool-factory%7D)
	- [Архитектура связки](#%D0%90%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D1%81%D0%B2%D1%8F%D0%B7%D0%BA%D0%B8)
	- [Реализация PooledEnemyFactory](#%D0%A0%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20PooledEnemyFactory)
	- [Использование связки Factory + Pool](#%D0%98%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%81%D0%B2%D1%8F%D0%B7%D0%BA%D0%B8%20Factory%20+%20Pool)
- [7. Практическое задание: EnemyFactory {#практика}](#7.%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5:%20EnemyFactory%20%7B#%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0%7D)
	- [Полная структура проекта](#%D0%9F%D0%BE%D0%BB%D0%BD%D0%B0%D1%8F%20%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
	- [GameEvents — система событий](#GameEvents%20%E2%80%94%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9)
	- [Полная реализация EnemyFactory (финальная версия)](#%D0%9F%D0%BE%D0%BB%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20EnemyFactory%20(%D1%84%D0%B8%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%8F))
	- [WaveSystem — финальная версия](#WaveSystem%20%E2%80%94%20%D1%84%D0%B8%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%8F)
	- [Debug UI для тестирования](#Debug%20UI%20%D0%B4%D0%BB%D1%8F%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F)
- [8. Проверь себя {#проверка}](#8.%20%D0%9F%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D1%8C%20%D1%81%D0%B5%D0%B1%D1%8F%20%7B#%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0%7D)
	- [Теоретические вопросы](#%D0%A2%D0%B5%D0%BE%D1%80%D0%B5%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%B2%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D1%8B)
	- [Практические задания](#%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F)
	- [Чеклист финального проекта](#%D0%A7%D0%B5%D0%BA%D0%BB%D0%B8%D1%81%D1%82%20%D1%84%D0%B8%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
- [Итоги](#%D0%98%D1%82%D0%BE%D0%B3%D0%B8)


---

## 1. Введение — проблема прямого Instantiate {#введение}

Представьте типичный проект: у вас есть десятки скриптов, и в каждом разбросаны вызовы `Instantiate`. Враги создаются в `WaveManager`, пули — в `Shooter`, эффекты — в `CombatSystem`. Всё работает, пока не приходит время изменить логику создания объектов.

### Как выглядит проблемный код



```csharp
// ❌ ПЛОХО: логика создания размазана по всему проекту

// В WaveManager.cs
public class WaveManager : MonoBehaviour
{
    [SerializeField] private GameObject goblinPrefab;
    [SerializeField] private GameObject orcPrefab;
    [SerializeField] private GameObject trollPrefab;

    public void SpawnEnemy(string enemyType)
    {
        GameObject enemy = null;

        // Прямая привязка к конкретным типам!
        if (enemyType == "Goblin")
        {
            enemy = Instantiate(goblinPrefab);
            enemy.GetComponent<Enemy>().health = 50f;
            enemy.GetComponent<Enemy>().speed = 5f;
            enemy.GetComponent<Enemy>().damage = 10f;
        }
        else if (enemyType == "Orc")
        {
            enemy = Instantiate(orcPrefab);
            enemy.GetComponent<Enemy>().health = 150f;
            enemy.GetComponent<Enemy>().speed = 3f;
            enemy.GetComponent<Enemy>().damage = 25f;
        }
        else if (enemyType == "Troll")
        {
            enemy = Instantiate(trollPrefab);
            enemy.GetComponent<Enemy>().health = 400f;
            enemy.GetComponent<Enemy>().speed = 1.5f;
            enemy.GetComponent<Enemy>().damage = 50f;
        }
    }
}

// В BossRoom.cs — ДУБЛИРОВАНИЕ той же логики!
public class BossRoom : MonoBehaviour
{
    [SerializeField] private GameObject trollPrefab;

    public void SpawnBoss()
    {
        // Та же магия цифр, скопированная из другого файла
        var troll = Instantiate(trollPrefab);
        troll.GetComponent<Enemy>().health = 400f; // А вдруг уже изменили?
        troll.GetComponent<Enemy>().speed = 1.5f;
        troll.GetComponent<Enemy>().damage = 50f;
    }
}
```

### Цепочка проблем



```csharp
Добавить нового врага "Dragon":
  → Найти ВСЕ места с if/else цепочками (забудешь половину)
  → Добавить новый if-блок в каждое место
  → Не забыть задать все параметры (copy-paste ошибки)
  → Протестировать каждое место отдельно

Изменить здоровье Orc с 150 на 200:
  → Найти ВСЕ места где создаётся Orc
  → Изменить в каждом месте
  → Молиться что не пропустил ни одного места
```

### Что нарушает такой подход

|Принцип SOLID|Нарушение|
|---|---|
|**Single Responsibility**|`WaveManager` отвечает и за волны, и за создание/настройку врагов|
|**Open/Closed**|Добавление врага требует изменения существующих классов|
|**Dependency Inversion**|Высокоуровневые модули зависят от конкретных классов (Goblin, Orc)|

### Что даёт паттерн Factory



```csharp
БЕЗ фабрики:                    С фабрикой:
WaveManager ──→ Goblin           WaveManager ──→ IEnemy
WaveManager ──→ Orc                              ↑
WaveManager ──→ Troll            EnemyFactory ───┤── Goblin
BossRoom    ──→ Troll            (одно место)    ├── Orc
                                                 └── Troll
```

---

## 2. Simple Factory — статический метод создания {#simple-factory}

**Simple Factory** (не является классическим GoF-паттерном, но широко используется) — это класс с одним статическим методом, который принимает параметр и возвращает нужный объект.

### Базовая архитектура



```csharp
// Базовый интерфейс для всех врагов
public interface IEnemy
{
    string Name { get; }
    float Health { get; set; }
    float Speed { get; }
    float Damage { get; }
    
    void Initialize(Vector3 position);
    void TakeDamage(float damage);
}

// Тип врага — добавить нового = добавить значение в enum
public enum EnemyType
{
    Goblin,
    Orc,
    Troll,
    Dragon
}
```



```csharp
// Конкретные реализации врагов
public class Goblin : MonoBehaviour, IEnemy
{
    public string Name => "Goblin";
    public float Health { get; set; }
    public float Speed => 5f;
    public float Damage => 10f;

    public void Initialize(Vector3 position)
    {
        transform.position = position;
        Health = 50f;
        // Специфичная инициализация гоблина
    }

    public void TakeDamage(float damage)
    {
        Health -= damage;
        if (Health <= 0) Die();
    }

    private void Die()
    {
        // Логика смерти гоблина
        Destroy(gameObject);
    }
}

public class Orc : MonoBehaviour, IEnemy
{
    public string Name => "Orc";
    public float Health { get; set; }
    public float Speed => 3f;
    public float Damage => 25f;

    public void Initialize(Vector3 position)
    {
        transform.position = position;
        Health = 150f;
    }

    public void TakeDamage(float damage)
    {
        Health -= damage;
        if (Health <= 0) Die();
    }

    private void Die() => Destroy(gameObject);
}

public class Troll : MonoBehaviour, IEnemy
{
    public string Name => "Troll";
    public float Health { get; set; }
    public float Speed => 1.5f;
    public float Damage => 50f;

    // Уникальная особенность тролля — регенерация
    [SerializeField] private float regenRate = 5f;

    public void Initialize(Vector3 position)
    {
        transform.position = position;
        Health = 400f;
        StartCoroutine(RegenerateHealth());
    }

    public void TakeDamage(float damage)
    {
        Health -= damage;
        if (Health <= 0) Die();
    }

    private System.Collections.IEnumerator RegenerateHealth()
    {
        while (Health > 0)
        {
            yield return new WaitForSeconds(1f);
            Health = Mathf.Min(Health + regenRate, 400f);
        }
    }

    private void Die() => Destroy(gameObject);
}
```

### Реализация Simple Factory



```csharp
// SimpleEnemyFactory.cs
using UnityEngine;

/// <summary>
/// Simple Factory — централизованное место создания врагов.
/// Вся логика "кого и как создавать" сосредоточена здесь.
/// </summary>
public static class SimpleEnemyFactory
{
    // Префабы хранятся в Resources или инжектируются снаружи
    private const string PREFABS_PATH = "Prefabs/Enemies/";

    /// <summary>
    /// Создать врага по типу на указанной позиции
    /// </summary>
    public static IEnemy Create(EnemyType type, Vector3 position)
    {
        GameObject prefab = LoadPrefab(type);
        
        if (prefab == null)
        {
            Debug.LogError($"[SimpleEnemyFactory] Префаб для {type} не найден!");
            return null;
        }

        GameObject instance = Object.Instantiate(prefab, position, Quaternion.identity);
        IEnemy enemy = instance.GetComponent<IEnemy>();

        if (enemy == null)
        {
            Debug.LogError($"[SimpleEnemyFactory] Компонент IEnemy не найден на префабе {type}!");
            Object.Destroy(instance);
            return null;
        }

        enemy.Initialize(position);
        return enemy;
    }

    /// <summary>
    /// Загрузка префаба из Resources
    /// </summary>
    private static GameObject LoadPrefab(EnemyType type)
    {
        string prefabName = type switch
        {
            EnemyType.Goblin => "GoblinEnemy",
            EnemyType.Orc    => "OrcEnemy",
            EnemyType.Troll  => "TrollEnemy",
            EnemyType.Dragon => "DragonEnemy",
            _ => throw new System.ArgumentException($"Неизвестный тип: {type}")
        };

        return Resources.Load<GameObject>($"{PREFABS_PATH}{prefabName}");
    }
}
```

### Использование Simple Factory



```csharp
// WaveManager.cs — теперь ничего не знает о конкретных типах врагов!
public class WaveManager : MonoBehaviour
{
    [SerializeField] private Transform[] spawnPoints;

    public void SpawnWave(EnemyType[] enemyTypes)
    {
        for (int i = 0; i < enemyTypes.Length; i++)
        {
            Vector3 spawnPos = spawnPoints[i % spawnPoints.Length].position;
            
            // Один вызов — не важно, кого именно создавать
            IEnemy enemy = SimpleEnemyFactory.Create(enemyTypes[i], spawnPos);
            
            if (enemy != null)
            {
                Debug.Log($"Заспавнен {enemy.Name} с HP: {enemy.Health}");
            }
        }
    }
}

// BossRoom.cs — тоже не знает о Troll напрямую
public class BossRoom : MonoBehaviour
{
    public void SpawnBoss()
    {
        var boss = SimpleEnemyFactory.Create(EnemyType.Troll, transform.position);
        Debug.Log($"Босс создан: {boss.Name}");
    }
}
```

### Ограничения Simple Factory



```csharp
Simple Factory хорош для старта, но имеет проблему:
при добавлении нового типа нужно менять сам класс фабрики.

Нарушает Open/Closed Principle:
EnemyType.Dragon → нужно добавить case в switch SimpleEnemyFactory
                   (изменяем существующий код)

Решение → Factory Method
```

---

## 3. Factory Method — абстрактная фабрика через наследование {#factory-method}

**Factory Method** выносит логику создания объекта в переопределяемый метод. Базовый класс определяет _когда_ создавать, подклассы определяют _что_ создавать.

### Диаграмма паттерна



```csharp
   EnemySpawner (abstract)
   ├── CreateEnemy() — abstract (Factory Method)
   ├── SpawnAtPoint()
   └── SpawnWave()
         │
         ├── GoblinSpawner
         │   └── CreateEnemy() → new Goblin()
         │
         ├── OrcSpawner
         │   └── CreateEnemy() → new Orc()
         │
         └── TrollSpawner
             └── CreateEnemy() → new Troll()
```

### Реализация



```csharp
// Абстрактный базовый спавнер
public abstract class EnemySpawner : MonoBehaviour
{
    [Header("Общие настройки спавна")]
    [SerializeField] protected Transform[] spawnPoints;
    [SerializeField] protected float spawnInterval = 2f;
    [SerializeField] protected int maxEnemies = 10;

    private List<IEnemy> _activeEnemies = new();
    private Coroutine _spawnCoroutine;

    // ★ Factory Method — подклассы ОБЯЗАНЫ переопределить этот метод
    protected abstract IEnemy CreateEnemy(Vector3 position);

    // Базовая логика спавна — одинакова для всех
    public void StartSpawning()
    {
        _spawnCoroutine = StartCoroutine(SpawnLoop());
    }

    public void StopSpawning()
    {
        if (_spawnCoroutine != null)
            StopCoroutine(_spawnCoroutine);
    }

    private IEnumerator SpawnLoop()
    {
        while (true)
        {
            if (_activeEnemies.Count < maxEnemies)
            {
                SpawnOne();
            }
            yield return new WaitForSeconds(spawnInterval);
        }
    }

    protected void SpawnOne()
    {
        Vector3 position = GetRandomSpawnPoint();
        
        // Вызываем Factory Method — не знаем кого именно создадим
        IEnemy enemy = CreateEnemy(position);
        
        if (enemy != null)
        {
            _activeEnemies.Add(enemy);
            OnEnemySpawned(enemy);
        }
    }

    // Хук (hook) — подклассы могут переопределить для доп. логики
    protected virtual void OnEnemySpawned(IEnemy enemy)
    {
        Debug.Log($"[{GetType().Name}] Создан: {enemy.Name}");
    }

    protected Vector3 GetRandomSpawnPoint()
    {
        if (spawnPoints == null || spawnPoints.Length == 0)
            return transform.position;
        
        return spawnPoints[Random.Range(0, spawnPoints.Length)].position;
    }

    public void RemoveEnemy(IEnemy enemy)
    {
        _activeEnemies.Remove(enemy);
    }

    public int ActiveEnemyCount => _activeEnemies.Count;
}
```



```csharp
// Конкретные фабрики — каждая знает только о своём типе врага

public class GoblinSpawner : EnemySpawner
{
    [SerializeField] private Goblin goblinPrefab;

    protected override IEnemy CreateEnemy(Vector3 position)
    {
        var goblin = Instantiate(goblinPrefab, position, Quaternion.identity);
        goblin.Initialize(position);
        return goblin;
    }

    protected override void OnEnemySpawned(IEnemy enemy)
    {
        base.OnEnemySpawned(enemy);
        // Специфичная логика для гоблинов — например, боевой клич
        Debug.Log("Гоблины атакуют! Визг!");
    }
}

public class OrcSpawner : EnemySpawner
{
    [SerializeField] private Orc orcPrefab;
    [SerializeField] private bool spawnWithShield = false;

    protected override IEnemy CreateEnemy(Vector3 position)
    {
        var orc = Instantiate(orcPrefab, position, Quaternion.identity);
        orc.Initialize(position);
        
        // Специфичная настройка орков
        if (spawnWithShield)
        {
            // Добавляем щит — логика только здесь, не размазана по коду
            orc.gameObject.AddComponent<ShieldComponent>()
               .Initialize(50f);
        }
        
        return orc;
    }
}

public class TrollSpawner : EnemySpawner
{
    [SerializeField] private Troll trollPrefab;
    [SerializeField] private float bossHealthMultiplier = 1f;

    protected override IEnemy CreateEnemy(Vector3 position)
    {
        var troll = Instantiate(trollPrefab, position, Quaternion.identity);
        troll.Initialize(position);
        
        // Можем модифицировать при создании
        troll.Health *= bossHealthMultiplier;
        
        return troll;
    }
}
```

### Использование Factory Method



```csharp
// Код, работающий с любым спавнером — не знает конкретного типа
public class LevelManager : MonoBehaviour
{
    // Ссылка на АБСТРАКТНЫЙ тип — можно подставить любой спавнер
    [SerializeField] private EnemySpawner enemySpawner;

    private void Start()
    {
        // Не важно, какой именно спавнер подключён в инспекторе
        enemySpawner.StartSpawning();
    }

    private void OnWaveComplete()
    {
        enemySpawner.StopSpawning();
        Debug.Log($"Волна завершена. Активных врагов: {enemySpawner.ActiveEnemyCount}");
    }
}
```

### Когда использовать Factory Method



```csharp
✅ Используйте Factory Method когда:
- Разные типы спавнеров нужны в разных сценах
- Логика спавна общая, но тип объекта — разный
- Хотите добавлять новые типы без изменения базового класса

✅ Добавление Dragon:
1. Создать DragonSpawner : EnemySpawner
2. Переопределить CreateEnemy()
3. Подключить в Inspector
— Существующий код НЕ меняется!
```

---

## 4. Abstract Factory — семейства объектов {#abstract-factory}

**Abstract Factory** — это фабрика фабрик. Она группирует связанные объекты в **семейства** и гарантирует их совместимость. В играх это идеально подходит для создания тематических наборов: объекты одной фракции, биома, уровня сложности.

### Концепция семейств



```csharp
Фракция "Лес":          Фракция "Подземелье":
┌─────────────┐         ┌─────────────────┐
│ ForestGoblin│         │ DungeonGoblin   │
│ ForestOrc   │         │ DungeonOrc      │
│ ForestBoss  │         │ DungeonBoss     │
│ ForestTrap  │         │ DungeonTrap     │
└─────────────┘         └─────────────────┘

Гарантия: объекты одной фракции всегда совместимы между собой.
```

### Реализация Abstract Factory



```csharp
// Интерфейсы для каждого типа объектов семейства
public interface IEnemyUnit
{
    string FactionName { get; }
    void Initialize(Vector3 position);
}

public interface IEnemyBoss
{
    string BossName { get; }
    float BossHealth { get; }
    void Initialize(Vector3 position);
    void ActivatePhase2();
}

public interface IEnvironmentTrap
{
    void Activate();
    void Deactivate();
    float DamagePerSecond { get; }
}

// ★ Интерфейс Abstract Factory — семейство объектов
public interface IFactionFactory
{
    string FactionName { get; }
    
    IEnemyUnit CreateGrunt(Vector3 position);      // Рядовой враг
    IEnemyUnit CreateElite(Vector3 position);      // Элитный враг
    IEnemyBoss CreateBoss(Vector3 position);       // Босс
    IEnvironmentTrap CreateTrap(Vector3 position); // Ловушка
}
```



```csharp
// Конкретные объекты фракции "Лес"
public class ForestGrunt : MonoBehaviour, IEnemyUnit
{
    public string FactionName => "Forest";
    
    public void Initialize(Vector3 position)
    {
        transform.position = position;
        // Лесной grunt специфика: маскировка в деревьях
        GetComponent<SpriteRenderer>().color = new Color(0.2f, 0.6f, 0.2f);
    }
}

public class ForestElite : MonoBehaviour, IEnemyUnit
{
    public string FactionName => "Forest";
    
    public void Initialize(Vector3 position)
    {
        transform.position = position;
        // Элитный — с луком и усиленной атакой
    }
}

public class ForestBoss : MonoBehaviour, IEnemyBoss
{
    public string BossName => "Ancient Treant";
    public float BossHealth => 2000f;
    
    public void Initialize(Vector3 position)
    {
        transform.position = position;
    }
    
    public void ActivatePhase2()
    {
        // Фаза 2: призывает лесных духов
        Debug.Log("Treant активирует лесных духов!");
    }
}

public class ForestTrap : MonoBehaviour, IEnvironmentTrap
{
    public float DamagePerSecond => 15f;
    
    public void Activate()   => gameObject.SetActive(true);
    public void Deactivate() => gameObject.SetActive(false);
}
```



```csharp
// Конкретные объекты фракции "Подземелье"
public class DungeonGrunt : MonoBehaviour, IEnemyUnit
{
    public string FactionName => "Dungeon";
    
    public void Initialize(Vector3 position)
    {
        transform.position = position;
        // Подземный grunt: светобоязнь, атакует только в темноте
    }
}

public class DungeonElite : MonoBehaviour, IEnemyUnit
{
    public string FactionName => "Dungeon";
    
    public void Initialize(Vector3 position)
    {
        transform.position = position;
        // Элитный подземный: невидимость в тени
    }
}

public class DungeonBoss : MonoBehaviour, IEnemyBoss
{
    public string BossName => "Shadow Overlord";
    public float BossHealth => 3000f;
    
    public void Initialize(Vector3 position)
    {
        transform.position = position;
    }
    
    public void ActivatePhase2()
    {
        // Фаза 2: телепортация и клоны
        Debug.Log("Shadow Overlord создаёт клонов!");
    }
}

public class DungeonTrap : MonoBehaviour, IEnvironmentTrap
{
    public float DamagePerSecond => 30f;
    
    public void Activate()   => gameObject.SetActive(true);
    public void Deactivate() => gameObject.SetActive(false);
}
```



```csharp
// ★ Конкретные фабрики — каждая создаёт СОВМЕСТИМОЕ семейство

[CreateAssetMenu(menuName = "Factories/Forest Factory")]
public class ForestFactionFactory : ScriptableObject, IFactionFactory
{
    public string FactionName => "Forest";

    [Header("Префабы лесной фракции")]
    [SerializeField] private ForestGrunt gruntPrefab;
    [SerializeField] private ForestElite elitePrefab;
    [SerializeField] private ForestBoss  bossPrefab;
    [SerializeField] private ForestTrap  trapPrefab;

    public IEnemyUnit CreateGrunt(Vector3 position)
    {
        var obj = Instantiate(gruntPrefab, position, Quaternion.identity);
        obj.Initialize(position);
        return obj;
    }

    public IEnemyUnit CreateElite(Vector3 position)
    {
        var obj = Instantiate(elitePrefab, position, Quaternion.identity);
        obj.Initialize(position);
        return obj;
    }

    public IEnemyBoss CreateBoss(Vector3 position)
    {
        var obj = Instantiate(bossPrefab, position, Quaternion.identity);
        obj.Initialize(position);
        return obj;
    }

    public IEnvironmentTrap CreateTrap(Vector3 position)
    {
        var obj = Instantiate(trapPrefab, position, Quaternion.identity);
        return obj;
    }
}

[CreateAssetMenu(menuName = "Factories/Dungeon Factory")]
public class DungeonFactionFactory : ScriptableObject, IFactionFactory
{
    public string FactionName => "Dungeon";

    [Header("Префабы подземной фракции")]
    [SerializeField] private DungeonGrunt gruntPrefab;
    [SerializeField] private DungeonElite elitePrefab;
    [SerializeField] private DungeonBoss  bossPrefab;
    [SerializeField] private DungeonTrap  trapPrefab;

    public IEnemyUnit CreateGrunt(Vector3 position)
    {
        var obj = Instantiate(gruntPrefab, position, Quaternion.identity);
        obj.Initialize(position);
        return obj;
    }

    public IEnemyUnit CreateElite(Vector3 position)
    {
        var obj = Instantiate(elitePrefab, position, Quaternion.identity);
        obj.Initialize(position);
        return obj;
    }

    public IEnemyBoss CreateBoss(Vector3 position)
    {
        var obj = Instantiate(bossPrefab, position, Quaternion.identity);
        obj.Initialize(position);
        return obj;
    }

    public IEnvironmentTrap CreateTrap(Vector3 position)
    {
        var obj = Instantiate(trapPrefab, position, Quaternion.identity);
        return obj;
    }
}
```

### Использование Abstract Factory



```csharp
// LevelBuilder — не знает ничего о конкретных фракциях!
public class LevelBuilder : MonoBehaviour
{
    // Подставляем нужную фабрику через Inspector или код
    [SerializeField] private ScriptableObject factionFactoryAsset;
    
    private IFactionFactory _factory;

    private void Awake()
    {
        // Получаем фабрику через интерфейс
        _factory = factionFactoryAsset as IFactionFactory;
        
        if (_factory == null)
        {
            Debug.LogError("Фабрика не реализует IFactionFactory!");
        }
    }

    public void BuildLevel(Vector3[] gruntPositions,
                           Vector3[] elitePositions,
                           Vector3   bossPosition,
                           Vector3[] trapPositions)
    {
        Debug.Log($"Строим уровень для фракции: {_factory.FactionName}");

        // Создаём рядовых врагов
        foreach (var pos in gruntPositions)
            _factory.CreateGrunt(pos);

        // Создаём элитных врагов
        foreach (var pos in elitePositions)
            _factory.CreateElite(pos);

        // Создаём ловушки
        foreach (var pos in trapPositions)
        {
            var trap = _factory.CreateTrap(pos);
            trap.Activate();
        }

        // Создаём босса
        var boss = _factory.CreateBoss(bossPosition);
        Debug.Log($"Босс уровня: {boss.BossName} с HP: {boss.BossHealth}");
    }

    // Переключение фракции (например, при смене биома)
    public void SwitchFaction(IFactionFactory newFactory)
    {
        _factory = newFactory;
        Debug.Log($"Фракция переключена на: {_factory.FactionName}");
    }
}
```

---

## 5. Фабрика + ScriptableObject для конфигурации {#scriptableobject}

`ScriptableObject` идеально подходит для хранения конфигурации врагов: данные отделены от кода, настраиваются в Editor без программирования, переиспользуются между сценами.

### Данные врага в ScriptableObject



```csharp
// EnemyConfig.cs
using UnityEngine;

[CreateAssetMenu(fileName = "EnemyConfig", menuName = "Game/Enemy Config")]
public class EnemyConfig : ScriptableObject
{
    [Header("Основные параметры")]
    public string enemyName = "Unknown Enemy";
    public EnemyType enemyType;
    public GameObject prefab;

    [Header("Характеристики")]
    [Min(1f)] public float maxHealth = 100f;
    [Min(0f)] public float moveSpeed = 3f;
    [Min(0f)] public float damage = 10f;
    [Min(0f)] public float attackRange = 1.5f;
    [Min(0f)] public float attackCooldown = 1f;

    [Header("Награда за убийство")]
    [Min(0)]  public int experienceReward = 10;
    [Min(0)]  public int goldReward = 5;

    [Header("Визуальные настройки")]
    public Color tintColor = Color.white;
    public float scale = 1f;
    public RuntimeAnimatorController animatorController;

    [Header("Звуки")]
    public AudioClip spawnSound;
    public AudioClip deathSound;
    public AudioClip attackSound;

    [Header("Спецспособности")]
    public bool canFly = false;
    public bool isInvisible = false;
    public bool hasSelfHeal = false;
    [Range(0f, 100f)] public float selfHealPercent = 10f;

    // Удобный метод для отладки
    public override string ToString() =>
        $"{enemyName} (HP:{maxHealth}, SPD:{moveSpeed}, DMG:{damage})";
}
```

### Универсальный компонент врага



```csharp
// Enemy.cs — единый компонент, настраиваемый через EnemyConfig
using UnityEngine;
using UnityEngine.AI;

[RequireComponent(typeof(NavMeshAgent))]
[RequireComponent(typeof(Animator))]
public class Enemy : MonoBehaviour, IEnemy
{
    // Конфиг — задаётся фабрикой, не через Inspector
    private EnemyConfig _config;
    private NavMeshAgent _agent;
    private Animator _animator;
    private AudioSource _audioSource;
    private SpriteRenderer _renderer;

    private float _currentHealth;
    private bool _isDead;

    // IEnemy реализация
    public string Name => _config?.enemyName ?? "Unknown";
    public float Health
    {
        get => _currentHealth;
        set => _currentHealth = Mathf.Clamp(value, 0, _config.maxHealth);
    }
    public float Speed  => _config?.moveSpeed ?? 0f;
    public float Damage => _config?.damage ?? 0f;

    private void Awake()
    {
        _agent       = GetComponent<NavMeshAgent>();
        _animator    = GetComponent<Animator>();
        _audioSource = GetComponent<AudioSource>();
        _renderer    = GetComponent<SpriteRenderer>();
    }

    /// <summary>
    /// Инициализация через конфиг — вызывается фабрикой
    /// </summary>
    public void Setup(EnemyConfig config)
    {
        _config = config;
        ApplyConfig();
    }

    private void ApplyConfig()
    {
        if (_config == null) return;

        // Применяем все параметры из конфига
        _currentHealth = _config.maxHealth;
        _isDead = false;

        // NavMeshAgent
        _agent.speed = _config.moveSpeed;
        _agent.stoppingDistance = _config.attackRange;

        // Визуальные настройки
        transform.localScale = Vector3.one * _config.scale;

        if (_renderer != null)
            _renderer.color = _config.tintColor;

        // Аниматор
        if (_config.animatorController != null)
            _animator.runtimeAnimatorController = _config.animatorController;

        // Спавн-звук
        if (_config.spawnSound != null)
            _audioSource.PlayOneShot(_config.spawnSound);

        // Спецспособности
        if (_config.canFly)
            EnableFlight();

        if (_config.hasSelfHeal)
            StartCoroutine(SelfHealRoutine());

        gameObject.name = $"{_config.enemyName}_{GetInstanceID()}";
    }

    public void Initialize(Vector3 position)
    {
        transform.position = position;
        _isDead = false;
    }

    public void TakeDamage(float damage)
    {
        if (_isDead) return;

        _currentHealth -= damage;
        _animator.SetTrigger("Hit");

        if (_currentHealth <= 0)
            Die();
    }

    private void Die()
    {
        if (_isDead) return;
        _isDead = true;

        _agent.enabled = false;
        _animator.SetTrigger("Death");

        if (_config?.deathSound != null)
            _audioSource.PlayOneShot(_config.deathSound);

        // Выдаём награду
        GameEvents.OnEnemyKilled?.Invoke(_config.experienceReward, _config.goldReward);

        Destroy(gameObject, 2f);
    }

    private void EnableFlight()
    {
        _agent.baseOffset = 2f; // Летим над землёй
    }

    private System.Collections.IEnumerator SelfHealRoutine()
    {
        while (!_isDead)
        {
            yield return new WaitForSeconds(5f);
            float healAmount = _config.maxHealth * (_config.selfHealPercent / 100f);
            Health = Mathf.Min(_currentHealth + healAmount, _config.maxHealth);
        }
    }
}
```

### Фабрика на основе ScriptableObject



```csharp
// EnemyFactory.cs — фабрика, работающая с конфигами
using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu(fileName = "EnemyFactory", menuName = "Game/Enemy Factory")]
public class EnemyFactory : ScriptableObject
{
    [Header("Каталог конфигураций")]
    [SerializeField] private List<EnemyConfig> enemyConfigs = new();

    // Словарь для быстрого поиска по типу
    private Dictionary<EnemyType, EnemyConfig> _configCache;

    private void OnEnable()
    {
        BuildCache();
    }

    private void BuildCache()
    {
        _configCache = new Dictionary<EnemyType, EnemyConfig>();

        foreach (var config in enemyConfigs)
        {
            if (config == null) continue;

            if (_configCache.ContainsKey(config.enemyType))
            {
                Debug.LogWarning($"[EnemyFactory] Дублирующийся тип: {config.enemyType}. " +
                               $"Используется первый найденный.");
                continue;
            }

            _configCache[config.enemyType] = config;
        }
    }

    /// <summary>
    /// Создать врага по типу на позиции
    /// </summary>
    public Enemy Create(EnemyType type, Vector3 position, Transform parent = null)
    {
        var config = GetConfig(type);
        if (config == null) return null;

        if (config.prefab == null)
        {
            Debug.LogError($"[EnemyFactory] Префаб не задан в конфиге: {config.enemyName}");
            return null;
        }

        var instance = Instantiate(config.prefab, position, Quaternion.identity, parent);
        var enemy = instance.GetComponent<Enemy>();

        if (enemy == null)
        {
            Debug.LogError($"[EnemyFactory] Компонент Enemy не найден на: {config.prefab.name}");
            Destroy(instance);
            return null;
        }

        // ★ Передаём конфиг — вся настройка происходит здесь
        enemy.Setup(config);
        enemy.Initialize(position);

        return enemy;
    }

    /// <summary>
    /// Получить конфиг без создания объекта (для превью, UI и т.д.)
    /// </summary>
    public EnemyConfig GetConfig(EnemyType type)
    {
        if (_configCache == null) BuildCache();

        if (_configCache.TryGetValue(type, out var config))
            return config;

        Debug.LogError($"[EnemyFactory] Конфиг для типа {type} не найден!");
        return null;
    }

    /// <summary>
    /// Все доступные типы врагов
    /// </summary>
    public IEnumerable<EnemyType> AvailableTypes => _configCache?.Keys;

    /// <summary>
    /// Проверить, зарегистрирован ли тип
    /// </summary>
    public bool HasConfig(EnemyType type)
    {
        if (_configCache == null) BuildCache();
        return _configCache.ContainsKey(type);
    }
}
```

### Настройка в Unity Editor



```csharp
Создание ресурсов:
1. ПКМ в Project → Create → Game → Enemy Config
   Создайте: GoblinConfig, OrcConfig, TrollConfig, DragonConfig
   
2. ПКМ в Project → Create → Game → Enemy Factory
   Добавьте все конфиги в список enemyConfigs

3. В каждом EnemyConfig настройте:
   ├── Enemy Name: "Goblin"
   ├── Enemy Type: Goblin
   ├── Prefab: [ваш префаб]
   ├── Max Health: 50
   ├── Move Speed: 5
   ├── Damage: 10
   └── ... остальные параметры

Использование:
[SerializeField] private EnemyFactory enemyFactory;
// Перетащите EnemyFactory.asset в это поле
```

---

## 6. Фабрика + Object Pool — комбинирование паттернов {#pool-factory}

Объединим `Factory` и `Object Pool`: фабрика отвечает за _конфигурацию_ объектов, пул — за _управление памятью_. Результат — система без аллокаций и без жёсткой привязки к типам.

### Архитектура связки



```csharp
           ┌─────────────────────────────────────┐
           │      PooledEnemyFactory              │
           │                                      │
           │  Create(EnemyType) ─────────────┐   │
           │                                 ▼   │
           │  ┌──────────┐    ┌──────────────────┤
           │  │EnemyConfig│    │  ObjectPool<Enemy>│
           │  │(SO Data)  │    │  ┌──────────────┐│
           │  └──────────┘    │  │ Enemy (inactive)││
           │        │         │  │ Enemy (inactive)││
           │        └─────────►  │ Enemy (active)  ││
           │  Setup(config)   │  └──────────────┘│
           │                  └──────────────────┘│
           └─────────────────────────────────────┘
```

### Реализация PooledEnemyFactory



```csharp
// PooledEnemyFactory.cs
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Pool;

public class PooledEnemyFactory : MonoBehaviour
{
    public static PooledEnemyFactory Instance { get; private set; }

    [Header("Конфигурация")]
    [SerializeField] private EnemyFactory enemyFactory; // SO с конфигами
    [SerializeField] private int defaultPoolSize = 20;
    [SerializeField] private int maxPoolSize = 100;

    // Отдельный пул для каждого типа врага
    private Dictionary<EnemyType, ObjectPool<Enemy>> _pools = new();
    private Dictionary<EnemyType, Transform> _containers = new();

    private void Awake()
    {
        if (Instance != null && Instance != this)
        {
            Destroy(gameObject);
            return;
        }
        Instance = this;
        DontDestroyOnLoad(gameObject);
    }

    /// <summary>
    /// Получить врага из пула (или создать нового)
    /// </summary>
    public Enemy Get(EnemyType type, Vector3 position)
    {
        var pool = GetOrCreatePool(type);
        var enemy = pool.Get();

        if (enemy != null)
        {
            // Переприменяем конфиг (сброс состояния)
            var config = enemyFactory.GetConfig(type);
            enemy.Setup(config);
            enemy.Initialize(position);
        }

        return enemy;
    }

    /// <summary>
    /// Вернуть врага в пул
    /// </summary>
    public void Release(EnemyType type, Enemy enemy)
    {
        if (_pools.TryGetValue(type, out var pool))
        {
            pool.Release(enemy);
        }
        else
        {
            Debug.LogWarning($"[PooledEnemyFactory] Пул для {type} не найден!");
            Destroy(enemy.gameObject);
        }
    }

    private ObjectPool<Enemy> GetOrCreatePool(EnemyType type)
    {
        if (!_pools.TryGetValue(type, out var pool))
        {
            pool = CreatePool(type);
            _pools[type] = pool;
        }
        return pool;
    }

    private ObjectPool<Enemy> CreatePool(EnemyType type)
    {
        // Контейнер для объектов этого пула
        var container = new GameObject($"[EnemyPool] {type}").transform;
        container.SetParent(transform);
        _containers[type] = container;

        var config = enemyFactory.GetConfig(type);
        if (config == null)
        {
            Debug.LogError($"[PooledEnemyFactory] Нет конфига для {type}!");
            return null;
        }

        return new ObjectPool<Enemy>(
            createFunc: () => CreateEnemyInstance(config, container),

            actionOnGet: enemy =>
            {
                enemy.gameObject.SetActive(true);
                enemy.transform.SetParent(null);
            },

            actionOnRelease: enemy =>
            {
                enemy.gameObject.SetActive(false);
                enemy.transform.SetParent(container);
                enemy.transform.localPosition = Vector3.zero;
            },

            actionOnDestroy: enemy => Destroy(enemy.gameObject),

            collectionCheck: Debug.isDebugBuild,
            defaultCapacity: defaultPoolSize,
            maxSize: maxPoolSize
        );
    }

    private Enemy CreateEnemyInstance(EnemyConfig config, Transform container)
    {
        if (config.prefab == null) return null;

        var instance = Instantiate(config.prefab, container);
        var enemy = instance.GetComponent<Enemy>();

        if (enemy == null)
        {
            Debug.LogError($"Нет компонента Enemy на {config.prefab.name}!");
            Destroy(instance);
            return null;
        }

        // Добавляем компонент для самостоятельного возврата
        var poolReturn = instance.AddComponent<EnemyPoolReturn>();
        poolReturn.Initialize(config.enemyType, this);

        instance.SetActive(false);
        return enemy;
    }

    /// <summary>
    /// Прогрев пулов (вызывать в начале уровня)
    /// </summary>
    public void PrewarmAll(int countPerType = 10)
    {
        if (enemyFactory == null) return;

        foreach (var type in enemyFactory.AvailableTypes)
        {
            Prewarm(type, countPerType);
        }
    }

    public void Prewarm(EnemyType type, int count)
    {
        var pool = GetOrCreatePool(type);
        var temp = new List<Enemy>(count);

        for (int i = 0; i < count; i++)
        {
            var enemy = pool.Get();
            if (enemy != null) temp.Add(enemy);
        }

        foreach (var enemy in temp)
        {
            pool.Release(enemy);
        }

        Debug.Log($"[PooledEnemyFactory] Прогрет пул {type}: {count} объектов");
    }

    /// <summary>
    /// Статистика всех пулов
    /// </summary>
    public void PrintStats()
    {
        foreach (var kvp in _pools)
        {
            var pool = kvp.Value;
            Debug.Log($"Пул [{kvp.Key}]: " +
                     $"Всего={pool.CountAll}, " +
                     $"Активных={pool.CountActive}, " +
                     $"В пуле={pool.CountInactive}");
        }
    }

    private void OnDestroy()
    {
        foreach (var pool in _pools.Values)
        {
            pool?.Dispose();
        }
        _pools.Clear();
    }
}

/// <summary>
/// Компонент для автоматического возврата в пул
/// </summary>
public class EnemyPoolReturn : MonoBehaviour
{
    private EnemyType _type;
    private PooledEnemyFactory _factory;

    public void Initialize(EnemyType type, PooledEnemyFactory factory)
    {
        _type = type;
        _factory = factory;
    }

    public void ReturnToPool()
    {
        var enemy = GetComponent<Enemy>();
        _factory?.Release(_type, enemy);
    }
}
```

### Использование связки Factory + Pool



```csharp
// WaveSystem.cs — использует фабрику + пул прозрачно
public class WaveSystem : MonoBehaviour
{
    [System.Serializable]
    public struct WaveConfig
    {
        public EnemyType enemyType;
        public int count;
        public float spawnDelay;
    }

    [SerializeField] private WaveConfig[] waves;
    [SerializeField] private Transform[] spawnPoints;

    private void Start()
    {
        // Прогреваем пулы до начала волн
        PooledEnemyFactory.Instance.PrewarmAll(15);
        StartCoroutine(RunWaves());
    }

    private IEnumerator RunWaves()
    {
        foreach (var wave in waves)
        {
            yield return StartCoroutine(SpawnWave(wave));
            yield return new WaitForSeconds(3f); // Пауза между волнами
        }
    }

    private IEnumerator SpawnWave(WaveConfig wave)
    {
        for (int i = 0; i < wave.count; i++)
        {
            var spawnPoint = spawnPoints[Random.Range(0, spawnPoints.Length)];

            // Один вызов — фабрика + пул работают вместе
            var enemy = PooledEnemyFactory.Instance.Get(wave.enemyType, spawnPoint.position);

            if (enemy != null)
            {
                Debug.Log($"Заспавнен {enemy.Name} из пула");
            }

            yield return new WaitForSeconds(wave.spawnDelay);
        }
    }
}
```

---

## 7. Практическое задание: EnemyFactory {#практика}

Создадим полноценную систему со всеми элементами: enum типов, ScriptableObject конфиги, фабрика с пулом, события и UI.

### Полная структура проекта



```csharp
Assets/
├── Scripts/
│   ├── Enemies/
│   │   ├── IEnemy.cs
│   │   ├── Enemy.cs
│   │   └── EnemyPoolReturn.cs
│   ├── Factory/
│   │   ├── EnemyType.cs
│   │   ├── EnemyConfig.cs
│   │   ├── EnemyFactory.cs
│   │   └── PooledEnemyFactory.cs
│   ├── Systems/
│   │   ├── WaveSystem.cs
│   │   └── GameEvents.cs
│   └── UI/
│       └── FactoryDebugUI.cs
├── ScriptableObjects/
│   ├── Factories/
│   │   └── MainEnemyFactory.asset
│   └── Enemies/
│       ├── GoblinConfig.asset
│       ├── OrcConfig.asset
│       ├── TrollConfig.asset
│       └── DragonConfig.asset
└── Prefabs/
    └── Enemies/
        ├── GoblinEnemy.prefab
        ├── OrcEnemy.prefab
        ├── TrollEnemy.prefab
        └── DragonEnemy.prefab
```

### GameEvents — система событий



```csharp
// GameEvents.cs
using System;
using UnityEngine;

public static class GameEvents
{
    // (exp, gold) → вызывается при смерти врага
    public static Action<int, int> OnEnemyKilled;

    // Тип врага, позиция → вызывается при спавне
    public static Action<EnemyType, Vector3> OnEnemySpawned;

    // Номер волны → вызывается при старте волны
    public static Action<int> OnWaveStarted;

    // → вызывается когда все волны пройдены
    public static Action OnAllWavesCompleted;
}
```

### Полная реализация EnemyFactory (финальная версия)



```csharp
// EnemyFactory.cs — финальная версия с валидацией и расширенным API
using System.Collections.Generic;
using System.Linq;
using UnityEngine;

[CreateAssetMenu(fileName = "EnemyFactory", menuName = "Game/Enemy Factory")]
public class EnemyFactory : ScriptableObject
{
    [Header("Конфигурации врагов")]
    [SerializeField] private List<EnemyConfig> configs = new();

    [Header("Настройки по умолчанию")]
    [SerializeField] private EnemyType defaultEnemyType = EnemyType.Goblin;

    private Dictionary<EnemyType, EnemyConfig> _cache;

    private void OnEnable() => RebuildCache();

    private void OnValidate() => RebuildCache();

    private void RebuildCache()
    {
        _cache = new Dictionary<EnemyType, EnemyConfig>();

        foreach (var config in configs)
        {
            if (config == null) continue;

            if (_cache.ContainsKey(config.enemyType))
            {
                Debug.LogWarning($"[EnemyFactory] Дубликат типа {config.enemyType} " +
                               $"в фабрике {name}. Пропускаем.");
                continue;
            }
            _cache[config.enemyType] = config;
        }
    }

    // ─── Основные методы создания ───────────────────────────────────────

    /// <summary>
    /// Создать врага по типу
    /// </summary>
    public Enemy Create(EnemyType type, Vector3 position,
                        Quaternion rotation = default,
                        Transform parent = null)
    {
        var config = GetConfig(type);
        if (config == null) return null;

        return InstantiateEnemy(config, position, rotation, parent);
    }

    /// <summary>
    /// Создать врага с модификацией параметров через callback
    /// </summary>
    public Enemy Create(EnemyType type, Vector3 position,
                        System.Action<Enemy> modifier)
    {
        var enemy = Create(type, position);

        if (enemy != null && modifier != null)
        {
            modifier(enemy);
        }

        return enemy;
    }

    /// <summary>
    /// Создать случайного врага из доступных типов
    /// </summary>
    public Enemy CreateRandom(Vector3 position)
    {
        if (_cache == null || _cache.Count == 0)
        {
            Debug.LogError("[EnemyFactory] Нет доступных конфигов!");
            return null;
        }

        var randomType = _cache.Keys.ElementAt(Random.Range(0, _cache.Count));
        return Create(randomType, position);
    }

    /// <summary>
    /// Создать несколько врагов одного типа
    /// </summary>
    public List<Enemy> CreateBatch(EnemyType type,
                                   Vector3[] positions)
    {
        var result = new List<Enemy>(positions.Length);

        foreach (var pos in positions)
        {
            var enemy = Create(type, pos);
            if (enemy != null) result.Add(enemy);
        }

        return result;
    }

    // ─── Вспомогательные методы ─────────────────────────────────────────

    private Enemy InstantiateEnemy(EnemyConfig config,
                                   Vector3 position,
                                   Quaternion rotation,
                                   Transform parent)
    {
        if (config.prefab == null)
        {
            Debug.LogError($"[EnemyFactory] Нет префаба в конфиге: {config.enemyName}");
            return null;
        }

        var go = Instantiate(config.prefab, position, rotation, parent);
        var enemy = go.GetComponent<Enemy>();

        if (enemy == null)
        {
            Debug.LogError($"[EnemyFactory] Нет компонента Enemy на {config.prefab.name}");
            Destroy(go);
            return null;
        }

        enemy.Setup(config);
        enemy.Initialize(position);

        // Уведомляем систему событий
        GameEvents.OnEnemySpawned?.Invoke(config.enemyType, position);

        return enemy;
    }

    public EnemyConfig GetConfig(EnemyType type)
    {
        if (_cache == null) RebuildCache();

        if (_cache.TryGetValue(type, out var config))
            return config;

        Debug.LogError($"[EnemyFactory] Конфиг для {type} не зарегистрирован в {name}!");
        return null;
    }

    public bool HasConfig(EnemyType type)
    {
        if (_cache == null) RebuildCache();
        return _cache.ContainsKey(type);
    }

    public IReadOnlyCollection<EnemyType> AvailableTypes =>
        _cache?.Keys ?? System.Array.Empty<EnemyType>();

    public EnemyConfig DefaultConfig => GetConfig(defaultEnemyType);

    // ─── Редакторная валидация ──────────────────────────────────────────

#if UNITY_EDITOR
    [ConMenu("Validate All Configs")]
    private void ValidateAllConfigs()
    {
        int valid = 0, invalid = 0;

        foreach (var config in configs)
        {
            if (config == null)
            {
                Debug.LogError("[EnemyFactory] Null конфиг в списке!");
                invalid++;
                continue;
            }

            if (config.prefab == null)
            {
                Debug.LogError($"[EnemyFactory] Нет префаба: {config.enemyName}");
                invalid++;
            }
            else if (config.prefab.GetComponent<Enemy>() == null)
            {
                Debug.LogError($"[EnemyFactory] Нет Enemy компонента: {config.enemyName}");
                invalid++;
            }
            else
            {
                valid++;
            }
        }

        Debug.Log($"[EnemyFactory] Валидация: ✅ {valid} корректных, ❌ {invalid} с ошибками");
    }
#endif
}
```

### WaveSystem — финальная версия



```csharp
// WaveSystem.cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class WaveSystem : MonoBehaviour
{
    [System.Serializable]
    public class EnemyEntry
    {
        public EnemyType type;
        [Min(1)] public int count = 1;
        [Min(0f)] public float spawnDelay = 0.5f;
    }

    [System.Serializable]
    public class Wave
    {
        public string waveName = "Wave";
        public List<EnemyEntry> enemies = new();
        [Min(0f)] public float timeBeforeNextWave = 5f;
    }

    [Header("Данные волн")]
    [SerializeField] private List<Wave> waves;

    [Header("Точки спавна")]
    [SerializeField] private Transform[] spawnPoints;

    [Header("Ссылки")]
    [SerializeField] private PooledEnemyFactory pooledFactory;

    private int _currentWave = 0;
    private int _activeEnemies = 0;

    private void OnEnable()
    {
        GameEvents.OnEnemyKilled += HandleEnemyKilled;
    }

    private void OnDisable()
    {
        GameEvents.OnEnemyKilled -= HandleEnemyKilled;
    }

    private void Start()
    {
        // Прогреваем пулы перед началом
        pooledFactory.PrewarmAll(10);
        StartCoroutine(RunAllWaves());
    }

    private IEnumerator RunAllWaves()
    {
        for (int i = 0; i < waves.Count; i++)
        {
            _currentWave = i;
            yield return StartCoroutine(RunWave(waves[i]));

            // Ждём пока все враги умрут или таймаут
            float waitTimeout = 30f;
            float elapsed = 0f;
            while (_activeEnemies > 0 && elapsed < waitTimeout)
            {
                elapsed += Time.deltaTime;
                yield return null;
            }

            if (i < waves.Count - 1)
            {
                Debug.Log($"Пауза перед волной {i + 2}...");
                yield return new WaitForSeconds(waves[i].timeBeforeNextWave);
            }
        }

        GameEvents.OnAllWavesCompleted?.Invoke();
        Debug.Log("Все волны завершены!");
    }

    private IEnumerator RunWave(Wave wave)
    {
        Debug.Log($"Начало волны: {wave.waveName}");
        GameEvents.OnWaveStarted?.Invoke(_currentWave);

        foreach (var entry in wave.enemies)
        {
            for (int i = 0; i < entry.count; i++)
            {
                SpawnEnemy(entry.type);
                yield return new WaitForSeconds(entry.spawnDelay);
            }
        }
    }

    private void SpawnEnemy(EnemyType type)
    {
        if (spawnPoints == null || spawnPoints.Length == 0)
        {
            Debug.LogError("[WaveSystem] Нет точек спавна!");
            return;
        }

        var point = spawnPoints[Random.Range(0, spawnPoints.Length)];
        var enemy = pooledFactory.Get(type, point.position);

        if (enemy != null)
        {
            _activeEnemies++;
        }
    }

    private void HandleEnemyKilled(int exp, int gold)
    {
        _activeEnemies = Mathf.Max(0, _activeEnemies - 1);
    }
}
```

### Debug UI для тестирования



```csharp
// FactoryDebugUI.cs
using UnityEngine;

public class FactoryDebugUI : MonoBehaviour
{
    [SerializeField] private PooledEnemyFactory factory;
    [SerializeField] private Transform spawnPoint;
    [SerializeField] private EnemyFactory enemyFactory;

    private void OnGUI()
    {
        GUILayout.BeginArea(new Rect(10, 10, 220, 400));
        GUILayout.BeginVertical("box");

        GUILayout.Label("=== Enemy Factory Debug ===");

        if (enemyFactory != null)
        {
            foreach (var type in enemyFactory.AvailableTypes)
            {
                GUILayout.BeginHorizontal();

                if (GUILayout.Button($"Spawn {type}", GUILayout.Width(130)))
                {
                    var pos = spawnPoint != null
                        ? spawnPoint.position
                        : Vector3.zero;

                    factory.Get(type, pos);
                }

                var config = enemyFactory.GetConfig(type);
                if (config != null)
                {
                    GUILayout.Label($"HP:{config.maxHealth}", GUILayout.Width(70));
                }

                GUILayout.EndHorizontal();
            }
        }

        GUILayout.Space(10);

        if (GUILayout.Button("Print Pool Stats"))
        {
            factory.PrintStats();
        }

        if (GUILayout.Button("Prewarm All (x10)"))
        {
            factory.PrewarmAll(10);
        }

        GUILayout.EndVertical();
        GUILayout.EndArea();
    }
}
```

---

## 8. Проверь себя {#проверка}

### Теоретические вопросы

**1.** В чём главное отличие Simple Factory от Factory Method?

<details> <summary>Ответ</summary>

**Simple Factory** — это статический (или обычный) класс с методом `Create()`, который содержит `if/switch` для выбора типа. При добавлении нового типа нужно **изменять** этот класс — нарушается Open/Closed Principle.

**Factory Method** — это абстрактный метод в базовом классе, который переопределяется в подклассах. Каждый подкласс знает только о своём типе объекта. Добавление нового типа = создание нового подкласса, **без изменения** существующих классов. Соблюдается Open/Closed Principle.

</details>

---

**2.** Когда Abstract Factory предпочтительнее Factory Method?

<details> <summary>Ответ</summary>

Abstract Factory нужна когда объекты создаются **семействами** — группами связанных объектов, которые должны быть совместимы между собой. Примеры:

- Враги + боссы + ловушки одной фракции (все "лесные" или все "подземные")
- UI-компоненты в одном визуальном стиле (кнопки, слайдеры, панели)
- Звуки + визуальные эффекты + партиклы для конкретного оружия

Factory Method подходит когда создаётся **один тип** объектов разных вариантов. Abstract Factory — когда нужно гарантировать **совместимость** нескольких связанных типов.

</details>

---

**3.** Почему ScriptableObject хорошо сочетается с фабрикой?

<details> <summary>Ответ</summary>

ScriptableObject решает несколько проблем:

1. **Отделение данных от кода**: параметры врагов настраиваются дизайнером в Editor без программирования
2. **Единый источник правды**: изменение параметров в одном SO автоматически применяется везде где он используется
3. **Переиспользование**: один SO можно использовать в разных сценах, фабриках, системах
4. **Версионирование**: SO хранятся как asset-файлы, удобно отслеживать изменения в Git
5. **Расширяемость**: можно создавать новые конфиги без изменения кода фабрики

</details>

---

**4.** Что произойдёт при `Release()` объекта в пул, если `collectionCheck = true` и объект уже находится в пуле?

<details> <summary>Ответ</summary>

Будет выброшено исключение `InvalidOperationException: Trying to release an object that has already been released to the pool.` Это намеренное поведение для выявления двойных возвратов во время разработки. В продакшн-сборке рекомендуется использовать флаг `_isReleased` в самом объекте и проверять его перед вызовом `Release()`.

</details>

---

**5.** Как фабрика убирает зависимость от конкретных классов?

<details> <summary>Ответ</summary>

Без фабрики клиентский код содержит `new Goblin()` или `Instantiate(goblinPrefab)` — прямую зависимость от конкретного класса `Goblin`. Это означает, что `WaveManager` "знает" о `Goblin`.

С фабрикой `WaveManager` вызывает `factory.Create(EnemyType.Goblin, pos)` и получает обратно `IEnemy`. Он знает только об интерфейсе `IEnemy` и перечислении `EnemyType`. Если класс `Goblin` переименуют, переделают или заменят — `WaveManager` не нужно менять. Зависимость инвертирована: и `WaveManager`, и `Goblin` зависят от абстракции `IEnemy`, а не друг от друга.

</details>

---

### Практические задания

**Задание 1: Базовое** 🟢

Добавьте нового врага `Skeleton` в существующую систему:

- Создайте `SkeletonConfig.asset` со своими параметрами
- Добавьте `EnemyType.Skeleton` в enum
- Добавьте конфиг в `EnemyFactory`
- Убедитесь, что `WaveSystem` может спавнить скелетов **без изменения кода**

---

**Задание 2: Среднее** 🟡

Реализуйте **модификаторы врагов** через паттерн Decorator поверх фабрики:



```csharp
// Подсказка: обёртка меняет параметры после создания
public class EliteEnemyDecorator : IEnemy
{
    private readonly IEnemy _wrapped;
    private const float ELITE_MULTIPLIER = 2f;

    public EliteEnemyDecorator(IEnemy enemy)
    {
        _wrapped = enemy;
        _wrapped.Health *= ELITE_MULTIPLIER;
    }

    // Делегируем все методы к _wrapped
    public string Name => $"Elite {_wrapped.Name}";
    public float Health
    {
        get => _wrapped.Health;
        set => _wrapped.Health = value;
    }
    // ... остальные члены интерфейса
}
```

---

**Задание 3: Продвинутое** 🔴

Реализуйте **фабрику с весовым рандомом** (Weighted Random Factory):



```csharp
// Врага создавать случайно, но с учётом весов
// Goblin: вес 60 → 60% шанс
// Orc:    вес 30 → 30% шанс
// Troll:  вес 10 → 10% шанс

[System.Serializable]
public struct WeightedEnemyEntry
{
    public EnemyType type;
    [Min(1)] public int weight;
}

public class WeightedEnemyFactory : MonoBehaviour
{
    [SerializeField] private WeightedEnemyEntry[] entries;
    [SerializeField] private EnemyFactory factory;

    public IEnemy CreateWeighted(Vector3 position)
    {
        // Ваша реализация взвешенного рандома...
    }
}
```

---

**Задание 4: Найди архитектурную проблему** 🔴

Что неправильно в этом коде? Найдите все нарушения принципов и предложите исправление:



```csharp
public class EnemySpawnSystem : MonoBehaviour
{
    public void SpawnEnemy(int level)
    {
        if (level < 5)
        {
            var go = Resources.Load<GameObject>("Goblin");
            var enemy = Instantiate(go).GetComponent<Goblin>();
            enemy.health = 50 * level;
            enemy.speed = 3f;
        }
        else if (level < 10)
        {
            var go = Resources.Load<GameObject>("Orc");
            var enemy = Instantiate(go).GetComponent<Orc>();
            enemy.health = 100 * level;
            enemy.speed = 2f;
        }
        else
        {
            var go = Resources.Load<GameObject>("Troll");
            var enemy = Instantiate(go).GetComponent<Troll>();
            enemy.health = 300 * level;
            enemy.speed = 1f;
        }
    }
}
```

<details> <summary>Разбор ошибок</summary>

**Проблема 1 — Нарушение SRP:**  
`EnemySpawnSystem` отвечает за логику спавна, загрузку ресурсов, AND настройку параметров врагов. Три разные ответственности в одном классе.

**Проблема 2 — Нарушение OCP:**  
При добавлении нового врага нужно редактировать этот метод. Добавление `Dragon` = модификация существующего кода.

**Проблема 3 — Жёсткие зависимости:**  
Прямое использование `Goblin`, `Orc`, `Troll` — зависимость от конкретных классов. Рефакторинг класса врага сломает этот код.

**Проблема 4 — Resources.Load в рантайме:**  
Строковые пути к ресурсам — хрупкий подход. Переименование файла сломает код. Не обнаруживается на этапе компиляции.

**Проблема 5 — Магические числа:**  
`50 * level`, `100 * level`, `300 * level` — параметры захардкожены, нельзя настроить без изменения кода.

**Правильный подход:**



```csharp
// ✅ Всё что нужно знать системе спавна:
public class CorrectSpawnSystem : MonoBehaviour
{
    [SerializeField] private EnemyFactory factory;

    public void SpawnForLevel(int level)
    {
        EnemyType type = level < 5  ? EnemyType.Goblin :
                         level < 10 ? EnemyType.Orc    :
                                      EnemyType.Troll;
        // Один вызов, никакой логики настройки
        factory.Create(type, transform.position);
    }
}
```

Параметры — в ScriptableObject. Создание — в фабрике. Выбор типа — в этом классе. Каждый отвечает за своё.

</details>

---

### Чеклист финального проекта

- [ ]  `EnemyType` — enum с минимум 4 типами
- [ ]  `EnemyConfig` — ScriptableObject с параметрами
- [ ]  `IEnemy` — интерфейс, клиентский код зависит только от него
- [ ]  `EnemyFactory` — ScriptableObject-фабрика, читает конфиги
- [ ]  `PooledEnemyFactory` — комбинирует Factory + ObjectPool
- [ ]  `WaveSystem` — не содержит `if/switch` по типу врага
- [ ]  Добавление нового типа врага не требует изменения `WaveSystem`
- [ ]  Нет аллокаций в рантайме (проверено в Profiler)
- [ ]  `collectionCheck` включён в Debug-сборке
- [ ]  Все магические числа вынесены в `EnemyConfig`

---

## Итоги

|Паттерн|Когда применять|Сложность|
|---|---|---|
|**Simple Factory**|Один тип объектов, небольшой проект|⭐|
|**Factory Method**|Разные стратегии создания, наследование|⭐⭐|
|**Abstract Factory**|Семейства совместимых объектов|⭐⭐⭐|
|**Factory + SO**|Данные отдельно от кода, настройка в Editor|⭐⭐|
|**Factory + Pool**|Производительность + гибкость архитектуры|⭐⭐⭐|

Фабричные паттерны решают фундаментальную проблему: **кто несёт ответственность за создание объектов и знание об их типах**. Перенося эту ответственность в одно место, мы получаем код, который легко расширять, тестировать и поддерживать.

> 💡 **Следующий шаг**: Изучите паттерн **Service Locator** и **Dependency Injection** (через Zenject/VContainer) — они дополняют фабрики, решая вопрос доступа к зависимостям без жёстких связей между системами