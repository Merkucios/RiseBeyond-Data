# VContainer: чистая архитектура для Unity-проектов

## От Singleton Hell к чистому коду с Dependency Injection

## Содержание

- [1. Введение: боль разработчика Unity](#1.%20%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5:%20%D0%B1%D0%BE%D0%BB%D1%8C%20%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA%D0%B0%20Unity)
	- [1.1 Как начинается каждый проект](#1.1%20%D0%9A%D0%B0%D0%BA%20%D0%BD%D0%B0%D1%87%D0%B8%D0%BD%D0%B0%D0%B5%D1%82%D1%81%D1%8F%20%D0%BA%D0%B0%D0%B6%D0%B4%D1%8B%D0%B9%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82)
	- [1.2 Симптомы Singleton Hell](#1.2%20%D0%A1%D0%B8%D0%BC%D0%BF%D1%82%D0%BE%D0%BC%D1%8B%20Singleton%20Hell)
	- [1.3 Цена технического долга](#1.3%20%D0%A6%D0%B5%D0%BD%D0%B0%20%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B3%D0%BE%20%D0%B4%D0%BE%D0%BB%D0%B3%D0%B0)
- [2. Что такое Dependency Injection](#2.%20%D0%A7%D1%82%D0%BE%20%D1%82%D0%B0%D0%BA%D0%BE%D0%B5%20Dependency%20Injection)
	- [2.1 Проблема зависимостей в терминах](#2.1%20%D0%9F%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0%20%D0%B7%D0%B0%D0%B2%D0%B8%D1%81%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D0%B5%D0%B9%20%D0%B2%20%D1%82%D0%B5%D1%80%D0%BC%D0%B8%D0%BD%D0%B0%D1%85)
	- [2.2 Три принципа, которые делает DI](#2.2%20%D0%A2%D1%80%D0%B8%20%D0%BF%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF%D0%B0,%20%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D1%8B%D0%B5%20%D0%B4%D0%B5%D0%BB%D0%B0%D0%B5%D1%82%20DI)
	- [2.3 До DI и после DI: полный контраст](#2.3%20%D0%94%D0%BE%20DI%20%D0%B8%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%20DI:%20%D0%BF%D0%BE%D0%BB%D0%BD%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%B0%D1%81%D1%82)
	- [2.4 Тестируемость: конкретный пример](#2.4%20%D0%A2%D0%B5%D1%81%D1%82%D0%B8%D1%80%D1%83%D0%B5%D0%BC%D0%BE%D1%81%D1%82%D1%8C:%20%D0%BA%D0%BE%D0%BD%D0%BA%D1%80%D0%B5%D1%82%D0%BD%D1%8B%D0%B9%20%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80)
- [3. VContainer: быстро и просто](#3.%20VContainer:%20%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%20%D0%B8%20%D0%BF%D1%80%D0%BE%D1%81%D1%82%D0%BE)
	- [3.1 Установка](#3.1%20%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0)
	- [3.2 VContainer vs Zenject](#3.2%20VContainer%20vs%20Zenject)
	- [3.3 Способы регистрации](#3.3%20%D0%A1%D0%BF%D0%BE%D1%81%D0%BE%D0%B1%D1%8B%20%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D0%B8)
	- [3.4 Lifetime](#3.4%20Lifetime)
	- [3.5 EntryPoints: интеграция с Unity Game Loop](#3.5%20EntryPoints:%20%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F%20%D1%81%20Unity%20Game%20Loop)
	- [3.6 Инъекция в MonoBehaviour через [Inject]](#3.6%20%D0%98%D0%BD%D1%8A%D0%B5%D0%BA%D1%86%D0%B8%D1%8F%20%D0%B2%20MonoBehaviour%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20%5BInject%5D)
- [4. Ключевые концепции](#4.%20%D0%9A%D0%BB%D1%8E%D1%87%D0%B5%D0%B2%D1%8B%D0%B5%20%D0%BA%D0%BE%D0%BD%D1%86%D0%B5%D0%BF%D1%86%D0%B8%D0%B8)
	- [4.1 LifetimeScope: точка входа для DI](#4.1%20LifetimeScope:%20%D1%82%D0%BE%D1%87%D0%BA%D0%B0%20%D0%B2%D1%85%D0%BE%D0%B4%D0%B0%20%D0%B4%D0%BB%D1%8F%20DI)
	- [4.2 Вложенные Scopes](#4.2%20%D0%92%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5%20Scopes)
- [5. Диаграмма архитектуры](#5.%20%D0%94%D0%B8%D0%B0%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B0%20%D0%B0%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D1%8B)
- [6. Практические задания](#6.%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F)
	- [6.1 Задание 1 — Базовое: первый LifetimeScope](#6.1%20%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%201%20%E2%80%94%20%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D0%BE%D0%B5:%20%D0%BF%D0%B5%D1%80%D0%B2%D1%8B%D0%B9%20LifetimeScope)
		- [Стартовый код (нужно переписать)](#%D0%A1%D1%82%D0%B0%D1%80%D1%82%D0%BE%D0%B2%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%B4%20(%D0%BD%D1%83%D0%B6%D0%BD%D0%BE%20%D0%BF%D0%B5%D1%80%D0%B5%D0%BF%D0%B8%D1%81%D0%B0%D1%82%D1%8C))
		- [Требования к решению](#%D0%A2%D1%80%D0%B5%D0%B1%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%20%D0%BA%20%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D1%8E)
		- [Эталонное решение](#%D0%AD%D1%82%D0%B0%D0%BB%D0%BE%D0%BD%D0%BD%D0%BE%D0%B5%20%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D0%B5)
		- [Критерии приёмки](#%D0%9A%D1%80%D0%B8%D1%82%D0%B5%D1%80%D0%B8%D0%B8%20%D0%BF%D1%80%D0%B8%D1%91%D0%BC%D0%BA%D0%B8)
	- [6.2 Задание 2 — Средний: вложенные Scopes](#6.2%20%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%202%20%E2%80%94%20%D0%A1%D1%80%D0%B5%D0%B4%D0%BD%D0%B8%D0%B9:%20%D0%B2%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5%20Scopes)
		- [Архитектура](#%D0%90%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D0%B0)
		- [Стартовый код (скелет для заполнения)](#%D0%A1%D1%82%D0%B0%D1%80%D1%82%D0%BE%D0%B2%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%B4%20(%D1%81%D0%BA%D0%B5%D0%BB%D0%B5%D1%82%20%D0%B4%D0%BB%D1%8F%20%D0%B7%D0%B0%D0%BF%D0%BE%D0%BB%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F))
		- [Эталонное решение](#%D0%AD%D1%82%D0%B0%D0%BB%D0%BE%D0%BD%D0%BD%D0%BE%D0%B5%20%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D0%B5)
		- [Критерии приёмки](#%D0%9A%D1%80%D0%B8%D1%82%D0%B5%D1%80%D0%B8%D0%B8%20%D0%BF%D1%80%D0%B8%D1%91%D0%BC%D0%BA%D0%B8)
	- [6.3 Задание 3 — Продвинутое: Factory + Unit Tests](#6.3%20%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%203%20%E2%80%94%20%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%BD%D1%83%D1%82%D0%BE%D0%B5:%20Factory%20+%20Unit%20Tests)
		- [Архитектура фабрики](#%D0%90%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D1%84%D0%B0%D0%B1%D1%80%D0%B8%D0%BA%D0%B8)
		- [Эталонное решение](#%D0%AD%D1%82%D0%B0%D0%BB%D0%BE%D0%BD%D0%BD%D0%BE%D0%B5%20%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D0%B5)
		- [Unit-тесты без Unity](#Unit-%D1%82%D0%B5%D1%81%D1%82%D1%8B%20%D0%B1%D0%B5%D0%B7%20Unity)
		- [Критерии приёмки](#%D0%9A%D1%80%D0%B8%D1%82%D0%B5%D1%80%D0%B8%D0%B8%20%D0%BF%D1%80%D0%B8%D1%91%D0%BC%D0%BA%D0%B8)
- [7. Типичные ошибки при первом знакомстве с DI](#7.%20%D0%A2%D0%B8%D0%BF%D0%B8%D1%87%D0%BD%D1%8B%D0%B5%20%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D0%B8%20%D0%BF%D1%80%D0%B8%20%D0%BF%D0%B5%D1%80%D0%B2%D0%BE%D0%BC%20%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%D1%81%D1%82%D0%B2%D0%B5%20%D1%81%20DI)
	- [Ошибка 1: Контейнер как Service Locator](#%D0%9E%D1%88%D0%B8%D0%B1%D0%BA%D0%B0%201:%20%D0%9A%D0%BE%D0%BD%D1%82%D0%B5%D0%B9%D0%BD%D0%B5%D1%80%20%D0%BA%D0%B0%D0%BA%20Service%20Locator)
	- [Ошибка 2: Слишком толстый LifetimeScope](#%D0%9E%D1%88%D0%B8%D0%B1%D0%BA%D0%B0%202:%20%D0%A1%D0%BB%D0%B8%D1%88%D0%BA%D0%BE%D0%BC%20%D1%82%D0%BE%D0%BB%D1%81%D1%82%D1%8B%D0%B9%20LifetimeScope)
	- [Ошибка 3: Тяжёлая логика в конструкторе](#%D0%9E%D1%88%D0%B8%D0%B1%D0%BA%D0%B0%203:%20%D0%A2%D1%8F%D0%B6%D1%91%D0%BB%D0%B0%D1%8F%20%D0%BB%D0%BE%D0%B3%D0%B8%D0%BA%D0%B0%20%D0%B2%20%D0%BA%D0%BE%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D0%BE%D1%80%D0%B5)
	- [Ошибка 4: Captive Dependency](#%D0%9E%D1%88%D0%B8%D0%B1%D0%BA%D0%B0%204:%20Captive%20Dependency)
	- [Ошибка 5: Circular Dependency](#%D0%9E%D1%88%D0%B8%D0%B1%D0%BA%D0%B0%205:%20Circular%20Dependency)
	- [Ошибка 6: Неправильный Lifetime](#%D0%9E%D1%88%D0%B8%D0%B1%D0%BA%D0%B0%206:%20%D0%9D%D0%B5%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20Lifetime)
	- [Ошибка 7: Тестирование с зависимостью от UnityEngine](#%D0%9E%D1%88%D0%B8%D0%B1%D0%BA%D0%B0%207:%20%D0%A2%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%81%20%D0%B7%D0%B0%D0%B2%D0%B8%D1%81%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D1%8C%D1%8E%20%D0%BE%D1%82%20UnityEngine)
	- [Ошибка 8: Забыть зарегистрировать зависимость](#%D0%9E%D1%88%D0%B8%D0%B1%D0%BA%D0%B0%208:%20%D0%97%D0%B0%D0%B1%D1%8B%D1%82%D1%8C%20%D0%B7%D0%B0%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%20%D0%B7%D0%B0%D0%B2%D0%B8%D1%81%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D1%8C)
	- [Краткая шпаргалка ошибок](#%D0%9A%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F%20%D1%88%D0%BF%D0%B0%D1%80%D0%B3%D0%B0%D0%BB%D0%BA%D0%B0%20%D0%BE%D1%88%D0%B8%D0%B1%D0%BE%D0%BA)
- [8. Чеклист готовности проекта](#8.%20%D0%A7%D0%B5%D0%BA%D0%BB%D0%B8%D1%81%D1%82%20%D0%B3%D0%BE%D1%82%D0%BE%D0%B2%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
	- [Архитектура](#%D0%90%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D0%B0)
	- [Код](#%D0%9A%D0%BE%D0%B4)
	- [Тесты](#%D0%A2%D0%B5%D1%81%D1%82%D1%8B)
	- [Производительность](#%D0%9F%D1%80%D0%BE%D0%B8%D0%B7%D0%B2%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C)
- [9. Ресурсы для изучения](#9.%20%D0%A0%D0%B5%D1%81%D1%83%D1%80%D1%81%D1%8B%20%D0%B4%D0%BB%D1%8F%20%D0%B8%D0%B7%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D1%8F)
	- [Официальная документация](#%D0%9E%D1%84%D0%B8%D1%86%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D1%8F)
	- [Теория Dependency Injection](#%D0%A2%D0%B5%D0%BE%D1%80%D0%B8%D1%8F%20Dependency%20Injection)
	- [Unity и архитектура](#Unity%20%D0%B8%20%D0%B0%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D0%B0)
	- [Тестирование](#%D0%A2%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5)
	- [Смежные темы](#%D0%A1%D0%BC%D0%B5%D0%B6%D0%BD%D1%8B%D0%B5%20%D1%82%D0%B5%D0%BC%D1%8B)
- [Заключение](#%D0%97%D0%B0%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B5)


## 1. Введение: боль разработчика Unity

### 1.1 Как начинается каждый проект

День первый. Нужен менеджер звука. Решение очевидно:



```csharp
public class AudioManager : MonoBehaviour
{
    public static AudioManager Instance { get; private set; }

    private void Awake()
    {
        if (Instance != null) { Destroy(gameObject); return; }
        Instance = this;
        DontDestroyOnLoad(gameObject);
    }

    public void PlaySound(string sound) { /* ... */ }
}
```

Удобно. Работает. Через него подтягивается счёт, инвентарь, аналитика.  
Через месяц проект выглядит так:



```csharp
// Реальный код из коммерческого проекта (анонимизирован)
public class PlayerController : MonoBehaviour
{
    private void Start()
    {
        // Порядок вызовов критичен — поменяй местами и получи NullRef
        GameManager.Instance.RegisterPlayer(this);
        UIManager.Instance.SetupHUD(this);
        AudioManager.Instance.LoadPlayerSounds();
        InventoryManager.Instance.InitPlayer();
        QuestManager.Instance.CheckStartQuests();

        // "Защитное программирование" — симптом проблемы
        if (NetworkManager.Instance != null)
            NetworkManager.Instance.SyncPlayer();
    }

    public void CollectCoin()
    {
        // Изменилась логика — правим в двадцати местах
        InventoryManager.Instance.AddCoin();
        AudioManager.Instance.PlaySound("coin");
        UIManager.Instance.UpdateCoinDisplay();
        AnalyticsManager.Instance.Track("coin_collected");
        AchievementManager.Instance.CheckCoinAchievement();
        SaveManager.Instance.MarkDirty();
    }
}
```

### 1.2 Симптомы Singleton Hell

**Симптом 1: NullReferenceException в случайных местах**



```csharp
// Срабатывает только при определённом порядке загрузки сцен
// Воспроизводится один раз из десяти — идеальный баг для потери рассудка
AudioManager.Instance.PlaySound("click"); // Instance == null!
```

**Симптом 2: Нетестируемый код**



```csharp
// Как изолировать CalculateDamage от реального инвентаря в тесте?
public float CalculateDamage()
{
    var base_ = GameManager.Instance.PlayerStats.BaseDamage;
    var bonus = InventoryManager.Instance.HasItem("sword") ? 1.5f : 1f;
    return base_ * bonus;
    // Чтобы протестировать эту строку — нужна целая сцена Unity
}
```

**Симптом 3: Скрытые зависимости**



```csharp
// Что нужно этому классу для работы?
// Открываем код и считаем Instance-вызовы...
public class EnemyAI : MonoBehaviour
{
    // Зависит от 7 синглтонов — но это нигде не видно из сигнатуры
    private void Update()
    {
        var playerPos = GameManager.Instance.Player.transform.position;
        if (PatrolSystem.Instance.IsPatrolling(this)) { /* ... */ }
        AudioManager.Instance.PlayAmbient(/* ... */);
        // ...ещё четыре синглтона глубже в методах...
    }
}
```

**Симптом 4: Невозможность параллельной разработки**



```csharp
// Программист А меняет GameManager.Instance.PlayerData
// Программист Б одновременно меняет GameManager.Instance.PlayerData
// Результат: merge-конфликт в глобальном состоянии и часы дебаггинга
```

**Симптом 5: Script Execution Order как точка отказа**



```csharp
Project Settings → Script Execution Order:
  AudioManager:      -200
  GameManager:       -100
  InventoryManager:  -50
  PlayerController:  0

Добавляем новый менеджер → ломаем порядок → ищем баг три дня.
```

### 1.3 Цена технического долга

В проекте на 100k+ строк кода с Singleton-архитектурой реальные потери выглядят так:



```csharp
Метрика                    До DI          После DI
─────────────────────────────────────────────────
Время на новую фичу        5 дней         3 дня
Время на поиск бага        4 часа         1 час
Покрытие тестами           < 5%           > 60%
Конфликты при merge        Часто          Редко
Уверенность в изменениях   Низкая         Высокая
```

Если хоть один симптом знаком — читайте дальше.

---

## 2. Что такое Dependency Injection

### 2.1 Проблема зависимостей в терминах

**Зависимость** — это любой объект, который нужен классу для работы.  
**Tight coupling** — ситуация, когда класс сам создаёт или находит свои зависимости.  
**DI** — принцип: объект не создаёт зависимости, а получает их снаружи.



```csharp
// ────── Tight Coupling ──────────────────────────────────────────
public class PlayerService
{
    private readonly AudioManager _audio;      // конкретный класс
    private readonly ScoreSystem  _score;      // конкретный класс

    public PlayerService()
    {
        _audio = AudioManager.Instance;        // сам находит
        _score = new ScoreSystem();            // сам создаёт
        // Теперь PlayerService навсегда привязан к этим реализациям
    }
}

// ────── Dependency Injection ────────────────────────────────────
public class PlayerService
{
    private readonly IAudioManager _audio;     // интерфейс
    private readonly IScoreSystem  _score;     // интерфейс

    public PlayerService(IAudioManager audio, IScoreSystem score)
    {
        _audio = audio;                        // получает снаружи
        _score = score;                        // получает снаружи
        // Кто-то другой решает, какую реализацию передать
    }
}
```

### 2.2 Три принципа, которые делает DI



```csharp
┌─────────────────────────────────────────────────────────────────┐
│                    Dependency Injection                         │
│                                                                 │
│  1. ЯВНОСТЬ         Зависимости видны из сигнатуры конструктора │
│                                                                 │
│  2. ИНВЕРСИЯ        Класс зависит от абстракции (интерфейса),   │
│                     а не от конкретной реализации               │
│                                                                 │
│  3. ДЕЛЕГИРОВАНИЕ   Создание объектов — ответственность         │
│                     контейнера, не самого класса                │
└─────────────────────────────────────────────────────────────────┘
```

### 2.3 До DI и после DI: полный контраст



```csharp
// ══════════════════════════════════════════════════════════════
// ДО DI: Что видим при открытии кода
// ══════════════════════════════════════════════════════════════

public class EnemySpawner : MonoBehaviour
{
    [SerializeField] private GameObject _enemyPrefab;

    private void Start()
    {
        // Зависимости спрятаны внутри
        InvokeRepeating(nameof(Spawn), 0f, GameManager.Instance.SpawnRate);
    }

    private void Spawn()
    {
        var enemy = Instantiate(_enemyPrefab);
        AudioManager.Instance.PlaySound("spawn");
        UIManager.Instance.UpdateEnemyCount(++_count);
    }
    
    private int _count;
}
// Вопрос: от чего зависит EnemySpawner?
// Ответ: нужно читать весь код методов :(


// ══════════════════════════════════════════════════════════════
// ПОСЛЕ DI: Всё видно из заголовка класса
// ══════════════════════════════════════════════════════════════

public class EnemySpawner : IStartable, IDisposable
{
    // Зависимости явно объявлены — читаем конструктор и знаем всё
    private readonly IGameConfig   _config;
    private readonly IAudioManager _audio;
    private readonly IUIManager    _ui;
    private readonly IEnemyFactory _factory;

    private int   _count;
    private float _timer;

    public EnemySpawner(
        IGameConfig   config,
        IAudioManager audio,
        IUIManager    ui,
        IEnemyFactory factory)
    {
        _config  = config;
        _audio   = audio;
        _ui      = ui;
        _factory = factory;
    }

    public void Start() => _timer = 0f;

    public void Tick()
    {
        _timer += Time.deltaTime;
        if (_timer < _config.SpawnRate) return;

        _timer = 0f;
        _factory.CreateEnemy();
        _audio.PlaySound("spawn");
        _ui.UpdateEnemyCount(++_count);
    }

    public void Dispose() => _count = 0;
}
// Вопрос: от чего зависит EnemySpawner?
// Ответ: смотрим конструктор — IGameConfig, IAudioManager, IUIManager, IEnemyFactory
```

### 2.4 Тестируемость: конкретный пример



```csharp
// ────── Моки для тестирования ──────────────────────────────────
public class MockAudioManager : IAudioManager
{
    public List<string> Played { get; } = new();
    public void PlaySound(string s) => Played.Add(s);
}

public class MockUIManager : IUIManager
{
    public int LastEnemyCount { get; private set; }
    public void UpdateEnemyCount(int c) => LastEnemyCount = c;
}

public class MockEnemyFactory : IEnemyFactory
{
    public int CreatedCount { get; private set; }
    public void CreateEnemy() => CreatedCount++;
}

// ────── Тест без Unity, без сцены ──────────────────────────────
[Test]
public void EnemySpawner_AfterSpawnInterval_CreatesEnemyAndPlaysSound()
{
    // Arrange
    var audio   = new MockAudioManager();
    var ui      = new MockUIManager();
    var factory = new MockEnemyFactory();
    var config  = new GameConfig { SpawnRate = 5f };
    var spawner = new EnemySpawner(config, audio, ui, factory);

    spawner.Start();

    // Симулируем прошедшее время (не нужен Update Unity)
    SimulateTick(spawner, deltaTime: 5.1f);

    // Assert
    Assert.AreEqual(1,       factory.CreatedCount);
    Assert.AreEqual(1,       ui.LastEnemyCount);
    Assert.Contains("spawn", audio.Played);
}
// Выполняется за 2мс. Без сцены. Без Play Mode.
```

---

## 3. VContainer: быстро и просто

### 3.1 Установка



```csharp
Package Manager → Add package by URL:
https://github.com/hadashiA/VContainer.git?path=VContainer/Assets/VContainer

Или через OpenUPM:
openupm add com.hadashikick.vcontainer
```

### 3.2 VContainer vs Zenject



```csharp
Характеристика              Zenject        VContainer
──────────────────────────────────────────────────────
Резолв 1000 объектов        ~2.8 ms        ~0.4 ms
Размер библиотеки           ~300 KB        ~60 KB
IL2CPP (мобайл)             Проблемы       Оптимизирован
API                         Многословный   Лаконичный
Кривая обучения             Крутая         Пологая
Активность поддержки        Медленная      Высокая
```



```csharp
// ────── Zenject: несколько способов для одного и того же ───────
Container.Bind<IPlayerService>().To<PlayerService>().AsSingle().NonLazy();
Container.BindInterfacesAndSelfTo<PlayerService>().AsSingle();
Container.BindFactory<PlayerService, PlayerService.Factory>();

// ────── VContainer: один ясный способ ──────────────────────────
builder.Register<PlayerService>(Lifetime.Singleton).As<IPlayerService>();
```

### 3.3 Способы регистрации



```csharp
protected override void Configure(IContainerBuilder builder)
{
    // ── Чистый C# класс: VContainer создаст экземпляр ──────────
    builder.Register<ScoreSystem>(Lifetime.Singleton);

    // ── Через интерфейс ─────────────────────────────────────────
    builder.Register<ScoreSystem>(Lifetime.Singleton)
           .As<IScoreSystem>();

    // ── Через несколько интерфейсов ─────────────────────────────
    builder.Register<ScoreSystem>(Lifetime.Singleton)
           .As<IScoreSystem>()
           .As<IResettable>();

    // ── Готовый объект (ScriptableObject, конфиг) ───────────────
    builder.RegisterInstance(gameConfig);

    // ── MonoBehaviour из инспектора ─────────────────────────────
    builder.RegisterComponent(playerView);

    // ── MonoBehaviour из иерархии LifetimeScope ─────────────────
    builder.RegisterComponentInHierarchy<Camera>();

    // ── Создать новый GameObject с компонентом ──────────────────
    builder.RegisterComponentOnNewGameObject<AudioSource>(
        Lifetime.Singleton, "AudioSource_Main");
}
```

### 3.4 Lifetime



```csharp
// ── Singleton: один экземпляр на контейнер ──────────────────────
// Используйте для: менеджеров, сервисов с состоянием, репозиториев
builder.Register<AudioManager>(Lifetime.Singleton);

// Запрос A → создаёт AudioManager #1
// Запрос B → возвращает AudioManager #1 (тот же)
// Запрос C → возвращает AudioManager #1 (тот же)


// ── Transient: новый экземпляр при каждом запросе ───────────────
// Используйте для: команд (Command pattern), ViewModel для UI-ячеек
builder.Register<DamagePopup>(Lifetime.Transient);

// Запрос A → создаёт DamagePopup #1
// Запрос B → создаёт DamagePopup #2 (новый)
// Запрос C → создаёт DamagePopup #3 (новый)


// ── Scoped: один экземпляр на дочерний scope ────────────────────
// Используйте для: данных уровня, сессии боя, UI-экрана
builder.Register<LevelData>(Lifetime.Scoped);

// Scope "Level1": Запрос A → #1, Запрос B → #1 (тот же внутри scope)
// Scope "Level2": Запрос A → #2 (новый scope — новый объект)
```

### 3.5 EntryPoints: интеграция с Unity Game Loop



```csharp
// Интерфейсы жизненного цикла
public interface IStartable       { void Start();     } // как MonoBehaviour.Start
public interface ITickable        { void Tick();      } // как Update
public interface IFixedTickable   { void FixedTick(); } // как FixedUpdate
public interface ILateTickable    { void LateTick();  } // как LateUpdate
// + Post-версии: IPostTickable, IPostFixedTickable, IPostLateTickable
// System.IDisposable               Dispose()          // при уничтожении scope

// ────── Пример EntryPoint ───────────────────────────────────────
public class GameLoop : IStartable, ITickable, IFixedTickable, IDisposable
{
    private readonly IPlayerService _player;
    private readonly IEnemyManager  _enemies;

    public GameLoop(IPlayerService player, IEnemyManager enemies)
    {
        _player  = player;
        _enemies = enemies;
    }

    public void Start()     => _player.Initialize();
    public void Tick()      => _enemies.UpdateAI(Time.deltaTime);
    public void FixedTick() => _player.ApplyPhysics();
    public void Dispose()   => _enemies.Cleanup();
}

// ────── Регистрация ─────────────────────────────────────────────
builder.RegisterEntryPoint<GameLoop>();

// Порядок выполнения EntryPoints:
// Start: в порядке регистрации
// Tick: в порядке регистрации, каждый кадр
// Dispose: при уничтожении LifetimeScope
```

### 3.6 Инъекция в MonoBehaviour через [Inject]



```csharp
// MonoBehaviour не может принимать зависимости в конструктор
// [Inject] на методе — рекомендуемый способ
public class PlayerView : MonoBehaviour
{
    private IPlayerService _playerService;
    private IAudioManager  _audio;

    // VContainer вызовет этот метод автоматически
    [Inject]
    public void Construct(IPlayerService playerService, IAudioManager audio)
    {
        _playerService = playerService;
        _audio         = audio;
    }

    private void OnTriggerEnter(Collider other)
    {
        if (!other.CompareTag("Coin")) return;
        _playerService.CollectCoin();
        _audio.PlaySound("coin");
    }
}

// ────── Регистрация для инъекции ────────────────────────────────
public class GameLifetimeScope : LifetimeScope
{
    [SerializeField] private PlayerView _playerView;

    protected override void Configure(IContainerBuilder builder)
    {
        builder.Register<IPlayerService, PlayerService>(Lifetime.Singleton);
        builder.Register<IAudioManager,  AudioManager> (Lifetime.Singleton);

        // Регистрируем MonoBehaviour — VContainer инжектирует зависимости
        builder.RegisterComponent(_playerView);
    }
}
```

---

## 4. Ключевые концепции

### 4.1 LifetimeScope: точка входа для DI



```csharp
// LifetimeScope — это MonoBehaviour на GameObject в сцене
// Создайте пустой GameObject → добавьте компонент LifetimeScope
// Или унаследуйте собственный:

public class MainGameScope : LifetimeScope
{
    // SerializeField — единственный допустимый способ ссылок из инспектора
    [SerializeField] private GameConfig    _gameConfig;
    [SerializeField] private PlayerView    _playerView;
    [SerializeField] private UIRootView    _uiRoot;

    protected override void Configure(IContainerBuilder builder)
    {
        // Конфиги (готовые объекты)
        builder.RegisterInstance(_gameConfig);

        // MonoBehaviour компоненты из сцены
        builder.RegisterComponent(_playerView);
        builder.RegisterComponent(_uiRoot);

        // Чистые C# сервисы
        builder.Register<IPlayerService, PlayerService>(Lifetime.Singleton);
        builder.Register<IScoreSystem,   ScoreSystem>  (Lifetime.Singleton);
        builder.Register<IAudioManager,  AudioManager> (Lifetime.Singleton);

        // Точка входа в игровой цикл
        builder.RegisterEntryPoint<GameLoop>();
    }
}
```

### 4.2 Вложенные Scopes



```csharp
// ── Родительский Scope ─────────────────────────────────────────
public class RootScope : LifetimeScope
{
    protected override void Configure(IContainerBuilder builder)
    {
        // Сервисы, доступные ВЕЗДЕ в приложении
        builder.Register<IAudioManager,   AudioManager>  (Lifetime.Singleton);
        builder.Register<IInputService,   InputService>  (Lifetime.Singleton);
        builder.Register<ISettingsService,SettingsService>(Lifetime.Singleton);
    }
}

// ── Дочерний Scope: видит зависимости родителя ─────────────────
public class GameplayScope : LifetimeScope
{
    [SerializeField] private LevelConfig _levelConfig;

    protected override void Configure(IContainerBuilder builder)
    {
        builder.RegisterInstance(_levelConfig);

        // IAudioManager приходит из RootScope автоматически!
        builder.Register<IPlayerController, PlayerController>(Lifetime.Singleton);
        builder.Register<IEnemyFactory,     EnemyFactory>    (Lifetime.Singleton);

        builder.RegisterEntryPoint<GameplayLoop>();
    }
}

// ── Программное создание дочернего Scope ───────────────────────
public class SceneLoader
{
    private readonly LifetimeScope _rootScope;
    private LifetimeScope          _currentGameplayScope;

    public SceneLoader(LifetimeScope rootScope)
    {
        _rootScope = rootScope;
    }

    public void LoadLevel(LevelConfig config)
    {
        // Уничтожаем предыдущий — все IDisposable вызываются автоматически
        _currentGameplayScope?.Dispose();

        // Создаём дочерний с дополнительными регистрациями
        _currentGameplayScope = _rootScope.CreateChild(builder =>
        {
            builder.RegisterInstance(config);
            builder.Register<LevelData>           (Lifetime.Singleton);
            builder.Register<IEnemyFactory, EnemyFactory>(Lifetime.Singleton);
            builder.RegisterEntryPoint<GameplayLoop>();
        });
    }

    public void UnloadLevel()
    {
        _currentGameplayScope?.Dispose();
        _currentGameplayScope = null;
        // GameplayLoop.Dispose() вызовется автоматически
    }
}
```

---

## 5. Диаграмма архитектуры



```csharp
VContainer: Архитектура зависимостей в Unity-проекте
═══════════════════════════════════════════════════════════════════════════

 ┌──────────────────────────────────────────────────────────────────────┐
 │                        PROJECT SCOPE                                 │
 │                   (DontDestroyOnLoad, живёт всегда)                  │
 │                                                                      │
 │   ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐  │
 │   │   AudioService   │  │   InputService   │  │ SettingsService  │  │
 │   │   (Singleton)    │  │   (Singleton)    │  │   (Singleton)    │  │
 │   └──────────────────┘  └──────────────────┘  └──────────────────┘  │
 └───────────────────────────────┬──────────────────────────────────────┘
                                 │ родитель
           ┌─────────────────────┴───────────────────────┐
           │                                             │
           ▼                                             ▼
 ┌─────────────────────────────┐          ┌─────────────────────────────┐
 │       MAIN MENU SCOPE       │          │       GAMEPLAY SCOPE        │
 │   (активен на главном меню) │          │  (активен только в уровне)  │
 │                             │          │                             │
 │  ┌───────────────────────┐  │          │  ┌──────────────────────┐   │
 │  │  MainMenuPresenter    │  │          │  │   PlayerController   │   │
 │  │     (Singleton)       │  │          │  │     (Singleton)      │   │
 │  └───────────────────────┘  │          │  └──────────────────────┘   │
 │  ┌───────────────────────┐  │          │  ┌──────────────────────┐   │
 │  │  LevelSelectService   │  │          │  │    EnemyManager      │   │
 │  │     (Singleton)       │  │          │  │     (Singleton)      │   │
 │  └───────────────────────┘  │          │  └──────────────────────┘   │
 │                             │          │  ┌──────────────────────┐   │
 │  Видит из Project:          │          │  │     ScoreSystem      │   │
 │  ✓ AudioService             │          │  │     (Singleton)      │   │
 │  ✓ InputService             │          │  └──────────────────────┘   │
 │  ✓ SettingsService          │          │  ┌──────────────────────┐   │
 │                             │          │  │  ── EntryPoint ──    │   │
 └─────────────────────────────┘          │  │    GameplayLoop      │   │
                                          │  │  IStartable ✓        │   │
                                          │  │  ITickable  ✓        │   │
                                          │  │  IDisposable✓        │   │
                                          │  └──────────────────────┘   │
                                          │                             │
                                          │  Видит из Project:          │
                                          │  ✓ AudioService             │
                                          │  ✓ InputService             │
                                          │  ✓ SettingsService          │
                                          └──────────────┬──────────────┘
                                                         │ родитель
                                          ┌──────────────┴──────────────┐
                                          │         UI SCOPE            │
                                          │ (активен пока открыт экран) │
                                          │                             │
                                          │  ┌──────────────────────┐  │
                                          │  │  InventoryPresenter  │  │
                                          │  │     (Scoped)         │  │
                                          │  └──────────────────────┘  │
                                          │  ┌──────────────────────┐  │
                                          │  │   ItemGridViewModel  │  │
                                          │  │    (Transient)       │  │
                                          │  └──────────────────────┘  │
                                          │                             │
                                          │  Видит из Gameplay:         │
                                          │  ✓ PlayerController         │
                                          │  ✓ ScoreSystem             │
                                          │  Видит из Project:          │
                                          │  ✓ AudioService             │
                                          └─────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════

 DEPENDENCY FLOW (граф зависимостей для GameplayLoop)
 ─────────────────────────────────────────────────────

  GameplayLoop
    │
    ├──► IPlayerController ──► IInputService  (из Project Scope)
    │                    └──► IAudioService  (из Project Scope)
    │
    ├──► IEnemyManager ──► IEnemyFactory ──► IObjectResolver
    │                 └──► LevelData
    │
    └──► IScoreSystem

 Правило видимости:
 ┌─────────────────────────────────────────────┐
 │  Дочерний scope ВИДИТ зависимости родителя  │
 │  Родительский scope НЕ ВИДИТ дочерние       │
 └─────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════

 LIFETIME COMPARISON (поведение при резолве)
 ────────────────────────────────────────────

  Singleton                Transient               Scoped
  ─────────                ─────────               ──────
  Container                Container               Scope A
  │                        │                       │
  ├─ Resolve → [Obj#1]     ├─ Resolve → [Obj#1]    ├─ Resolve → [Obj#1]
  ├─ Resolve → [Obj#1] ←┐  ├─ Resolve → [Obj#2]    ├─ Resolve → [Obj#1] ←┐
  └─ Resolve → [Obj#1] ←┘  └─ Resolve → [Obj#3]    │                     │
       один и тот же              каждый раз         └─ всегда одинаков ──┘
                                  новый
                                                    Scope B
                                                    │
                                                    ├─ Resolve → [Obj#4]
                                                    └─ Resolve → [Obj#4] ←┐
                                                         другой, но         │
                                                         стабильный ────────┘

═══════════════════════════════════════════════════════════════════════════

 UNITY GAME LOOP INTEGRATION
 ────────────────────────────

  MonoBehaviour (стандартно)     EntryPoint (через VContainer)
  ──────────────────────────     ─────────────────────────────
  Awake()                        (контейнер строится)
  OnEnable()                     (зависимости инжектируются)
  Start()              ◄────     IStartable.Start()
  FixedUpdate()        ◄────     IFixedTickable.FixedTick()
  Update()             ◄────     ITickable.Tick()
  LateUpdate()         ◄────     ILateTickable.LateTick()
  OnDisable()
  OnDestroy()          ◄────     IDisposable.Dispose()

 VContainer гарантирует порядок:
 Start → затем Tick каждый кадр → Dispose при уничтожении Scope
```

---

## 6. Практические задания

### 6.1 Задание 1 — Базовое: первый LifetimeScope

**Сложность:** 🟢 Начинающий  
**Время:** 30–45 минут  
**Цель:** зарегистрировать сервисы, убедиться что Singleton разделяется между потребителями

#### Стартовый код (нужно переписать)



```csharp
// ❌ ЭТО НУЖНО ИСПРАВИТЬ ─────────────────────────────────────────

public class ScoreService : MonoBehaviour
{
    public static ScoreService Instance { get; private set; }
    public int Score { get; private set; }

    private void Awake()
    {
        if (Instance != null) { Destroy(gameObject); return; }
        Instance = this;
    }

    public void Add(int points) => Score += points;
    public void Reset()         => Score  = 0;
}

public class PlayerService : MonoBehaviour
{
    private int _health = 100;

    private void Start()
    {
        // Синглтон — жёсткая связь
        ScoreService.Instance.Reset();
    }

    public void CollectCoin()
    {
        ScoreService.Instance.Add(10);
    }

    public void TakeDamage(int dmg)
    {
        _health -= dmg;
        if (_health <= 0) GameManager.Instance.EndGame();
    }
}

public class GameManager : MonoBehaviour
{
    public static GameManager Instance { get; private set; }

    private void Awake()
    {
        if (Instance != null) { Destroy(gameObject); return; }
        Instance = this;
    }

    public void EndGame()
    {
        Debug.Log($"Game Over. Score: {ScoreService.Instance.Score}");
    }
}
```

#### Требования к решению



```csharp
1. Создать интерфейсы: IScoreService, IPlayerService, IGameManager
2. Убрать наследование от MonoBehaviour у всех трёх классов
3. Убрать все статические Instance
4. Добавить конструкторы с явными зависимостями
5. Создать GameLifetimeScope и зарегистрировать все сервисы
6. Создать EntryPoint GameEntryPoint : IStartable, ITickable
```

#### Эталонное решение



```csharp
// ── Интерфейсы ───────────────────────────────────────────────────

public interface IScoreService
{
    int  Score { get; }
    void Add(int points);
    void Reset();
}

public interface IPlayerService
{
    bool IsAlive { get; }
    void CollectCoin();
    void TakeDamage(int damage);
}

public interface IGameManager
{
    bool IsRunning { get; }
    void StartGame();
    void EndGame();
}

// ── Реализации ────────────────────────────────────────────────────

public class ScoreService : IScoreService
{
    public int Score { get; private set; }

    public void Add(int points)
    {
        Score += points;
        Debug.Log($"[Score] +{points} → {Score}");
    }

    public void Reset()
    {
        Score = 0;
        Debug.Log("[Score] Reset");
    }
}

public class PlayerService : IPlayerService
{
    private readonly IScoreService _score;

    private int _health;

    public bool IsAlive => _health > 0;

    // Зависимость явная — видна из конструктора
    public PlayerService(IScoreService score)
    {
        _score = score;
    }

    public void CollectCoin()
    {
        _score.Add(10);
        Debug.Log("[Player] Coin collected");
    }

    public void TakeDamage(int damage)
    {
        _health = Mathf.Max(0, _health - damage);
        Debug.Log($"[Player] Took {damage} dmg. HP: {_health}");
    }

    public void Initialize(int health = 100)
    {
        _health = health;
    }
}

public class GameManager : IGameManager
{
    private readonly IPlayerService _player;
    private readonly IScoreService  _score;

    public bool IsRunning { get; private set; }

    public GameManager(IPlayerService player, IScoreService score)
    {
        _player = player;
        _score  = score;
    }

    public void StartGame()
    {
        IsRunning = true;
        _score.Reset();
        Debug.Log("[Game] Started");
    }

    public void EndGame()
    {
        IsRunning = false;
        Debug.Log($"[Game] Over. Final score: {_score.Score}");
    }
}

// ── EntryPoint ────────────────────────────────────────────────────

public class GameEntryPoint : IStartable, ITickable
{
    private readonly IGameManager   _game;
    private readonly IPlayerService _player;

    private float _timer;

    public GameEntryPoint(IGameManager game, IPlayerService player)
    {
        _game   = game;
        _player = player;
    }

    public void Start()
    {
        _game.StartGame();
    }

    public void Tick()
    {
        if (!_game.IsRunning || !_player.IsAlive) return;

        // Симуляция: каждые 2 секунды подбираем монету
        _timer += Time.deltaTime;
        if (_timer < 2f) return;

        _timer = 0f;
        _player.CollectCoin();
    }
}

// ── LifetimeScope ─────────────────────────────────────────────────

public class GameLifetimeScope : LifetimeScope
{
    protected override void Configure(IContainerBuilder builder)
    {
        builder.Register<IScoreService,  ScoreService> (Lifetime.Singleton);
        builder.Register<IPlayerService, PlayerService>(Lifetime.Singleton);
        builder.Register<IGameManager,   GameManager>  (Lifetime.Singleton);

        builder.RegisterEntryPoint<GameEntryPoint>();
    }
}
```

#### Критерии приёмки



```csharp
✅ В логах "[Score] Reset" появляется ровно один раз при старте
✅ FindObjectOfType отсутствует во всём проекте (Ctrl+Shift+F для поиска)
✅ Статических Instance нет ни в одном классе
✅ PlayerService не знает о существовании GameManager
✅ Добавление нового сервиса не требует изменений в существующих классах
```

---

### 6.2 Задание 2 — Средний: вложенные Scopes

**Сложность:** 🟡 Средний  
**Время:** 60–90 минут  
**Цель:** реализовать RootScope и GameplayScope, убедиться что дочерний scope получает зависимости родителя и корректно освобождает ресурсы при уничтожении

#### Архитектура



```csharp
[RootScope]
│  AudioService   — Singleton, живёт всё время
│  InputService   — Singleton, живёт всё время
│
├─── [MainMenuScope]       — создаётся на главном меню
│        MainMenuController — EntryPoint
│
└─── [GameplayScope]       — создаётся при загрузке уровня
         PlayerController  — получает InputService из Root
         EnemySpawner      — получает AudioService из Root
         LevelData         — Singleton внутри scope
         GameplayLoop      — EntryPoint (IStartable, IDisposable)
```

#### Стартовый код (скелет для заполнения)



```csharp
// ── Заполните реализацию ─────────────────────────────────────────

public interface IAudioService
{
    void PlayMusic(string track);
    void PlaySfx(string sfx);
    void StopAll();
}

public interface IInputService
{
    Vector2 Move  { get; }
    bool    Jump  { get; }
    void    Enable();
    void    Disable();
}

public class LevelConfig : ScriptableObject
{
    [field: SerializeField] public int    Index       { get; private set; }
    [field: SerializeField] public int    MaxEnemies  { get; private set; }
    [field: SerializeField] public string MusicTrack  { get; private set; }
}

// TODO: реализуйте AudioService : IAudioService, IDisposable
// TODO: реализуйте InputService : IInputService, IDisposable
// TODO: реализуйте PlayerController (получает IInputService, IAudioService)
// TODO: реализуйте EnemySpawner (получает IAudioService, LevelConfig)
// TODO: реализуйте GameplayLoop : IStartable, ITickable, IDisposable
// TODO: реализуйте RootScope : LifetimeScope
// TODO: реализуйте GameplayScope : LifetimeScope
// TODO: реализуйте SceneLoader (создаёт и уничтожает GameplayScope)
```

#### Эталонное решение



```csharp
// ── Сервисы RootScope ─────────────────────────────────────────────

public class AudioService : IAudioService, IDisposable
{
    private bool _disposed;

    public AudioService() => Debug.Log("[Audio] Service created");

    public void PlayMusic(string track) => Debug.Log($"[Audio] Music: {track}");
    public void PlaySfx(string sfx)    => Debug.Log($"[Audio] SFX: {sfx}");
    public void StopAll()              => Debug.Log("[Audio] Stop all");

    public void Dispose()
    {
        if (_disposed) return;
        _disposed = true;
        StopAll();
        Debug.Log("[Audio] Disposed");
    }
}

public class InputService : IInputService, IDisposable
{
    private bool _enabled;

    public Vector2 Move => _enabled
        ? new Vector2(Input.GetAxisRaw("Horizontal"), Input.GetAxisRaw("Vertical"))
        : Vector2.zero;

    public bool Jump => _enabled && Input.GetButtonDown("Jump");

    public void Enable()
    {
        _enabled = true;
        Debug.Log("[Input] Enabled");
    }

    public void Disable()
    {
        _enabled = false;
        Debug.Log("[Input] Disabled");
    }

    public void Dispose()
    {
        Disable();
        Debug.Log("[Input] Disposed");
    }
}

// ── Сервисы GameplayScope ─────────────────────────────────────────

public class LevelData
{
    public int    Index      { get; }
    public int    MaxEnemies { get; }
    public string MusicTrack { get; }

    // VContainer автоматически инжектирует LevelConfig
    public LevelData(LevelConfig config)
    {
        Index      = config.Index;
        MaxEnemies = config.MaxEnemies;
        MusicTrack = config.MusicTrack;
        Debug.Log($"[LevelData] Loaded: Level {Index}");
    }
}

public class PlayerController
{
    // Зависимости из РАЗНЫХ scope — работает прозрачно
    private readonly IInputService _input; // из RootScope
    private readonly IAudioService _audio; // из RootScope

    public Vector3 Position { get; private set; }
    public int     Health   { get; private set; } = 100;

    public PlayerController(IInputService input, IAudioService audio)
    {
        _input = input;
        _audio = audio;
        Debug.Log("[Player] Controller created");
    }

    public void Tick(float dt)
    {
        if (Health <= 0) return;

        var dir = _input.Move;
        if (dir.sqrMagnitude > 0.01f)
            Position += new Vector3(dir.x, 0, dir.y) * 5f * dt;

        if (_input.Jump)
            _audio.PlaySfx("jump");
    }

    public void TakeDamage(int dmg)
    {
        Health = Mathf.Max(0, Health - dmg);
        _audio.PlaySfx("hurt");
    }
}

public class EnemySpawner
{
    private readonly IAudioService _audio; // из RootScope
    private readonly LevelData     _level; // из GameplayScope

    private float _timer;
    private int   _count;

    public EnemySpawner(IAudioService audio, LevelData level)
    {
        _audio = audio;
        _level = level;
        Debug.Log($"[Spawner] Ready. Max enemies: {_level.MaxEnemies}");
    }

    public void Tick(float dt)
    {
        if (_count >= _level.MaxEnemies) return;

        _timer += dt;
        if (_timer < 5f) return;

        _timer = 0f;
        _count++;
        _audio.PlaySfx("spawn");
        Debug.Log($"[Spawner] Enemy #{_count} spawned");
    }
}

// ── EntryPoint GameplayScope ──────────────────────────────────────

public class GameplayLoop : IStartable, ITickable, IDisposable
{
    private readonly PlayerController _player;
    private readonly EnemySpawner     _spawner;
    private readonly IAudioService    _audio;
    private readonly LevelData        _level;

    private bool _running;

    public GameplayLoop(
        PlayerController player,
        EnemySpawner     spawner,
        IAudioService    audio,
        LevelData        level)
    {
        _player  = player;
        _spawner = spawner;
        _audio   = audio;
        _level   = level;
    }

    public void Start()
    {
        _running = true;
        _audio.PlayMusic(_level.MusicTrack);
        Debug.Log($"[GameplayLoop] Level {_level.Index} started");
    }

    public void Tick()
    {
        if (!_running) return;
        _player.Tick(Time.deltaTime);
        _spawner.Tick(Time.deltaTime);

        if (_player.Health <= 0)
        {
            _running = false;
            Debug.Log("[GameplayLoop] Player died — game over");
        }
    }

    public void Dispose()
    {
        _running = false;
        _audio.StopAll();
        Debug.Log("[GameplayLoop] Level disposed");
        // IDisposable AudioService, InputService вызовутся scope'ом автоматически
    }
}

// ── Scopes ────────────────────────────────────────────────────────

public class RootScope : LifetimeScope
{
    protected override void Configure(IContainerBuilder builder)
    {
        Debug.Log("[RootScope] Configure");

        builder.Register<IAudioService, AudioService>(Lifetime.Singleton);
        builder.Register<IInputService, InputService>(Lifetime.Singleton);
        builder.Register<SceneLoader>               (Lifetime.Singleton);
    }
}

public class GameplayScope : LifetimeScope
{
    [SerializeField] private LevelConfig _levelConfig;

    protected override void Configure(IContainerBuilder builder)
    {
        Debug.Log("[GameplayScope] Configure");

        builder.RegisterInstance(_levelConfig);

        builder.Register<LevelData>           (Lifetime.Singleton);
        builder.Register<PlayerController>    (Lifetime.Singleton);
        builder.Register<EnemySpawner>        (Lifetime.Singleton);

        builder.RegisterEntryPoint<GameplayLoop>();
    }
}

// ── SceneLoader: управляет жизнью GameplayScope ───────────────────

public class SceneLoader : IDisposable
{
    private readonly LifetimeScope _root;
    private LifetimeScope          _gameplay;

    public SceneLoader(LifetimeScope root)
    {
        _root = root;
    }

    public void Load(LevelConfig config)
    {
        // Уничтожаем предыдущий scope если был
        _gameplay?.Dispose();

        // Создаём новый дочерний scope
        _gameplay = _root.CreateChild(builder =>
        {
            builder.RegisterInstance(config);
            builder.Register<LevelData>        (Lifetime.Singleton);
            builder.Register<PlayerController> (Lifetime.Singleton);
            builder.Register<EnemySpawner>     (Lifetime.Singleton);
            builder.RegisterEntryPoint<GameplayLoop>();
        });

        Debug.Log("[SceneLoader] Level loaded");
    }

    public void Unload()
    {
        _gameplay?.Dispose();
        _gameplay = null;
        Debug.Log("[SceneLoader] Level unloaded");
    }

    public void Dispose() => Unload();
}
```

#### Критерии приёмки



```csharp
✅ AudioService создаётся ОДИН РАЗ за сессию (проверить в логах)
✅ При Unload() в логах появляется "[GameplayLoop] Level disposed"
✅ При повторном Load() старый scope уничтожается перед созданием нового
✅ PlayerController получает InputService и AudioService из RootScope
✅ LevelData содержит данные из переданного LevelConfig
```

---

### 6.3 Задание 3 — Продвинутое: Factory + Unit Tests

**Сложность:** 🔴 Продвинутый  
**Время:** 90–120 минут  
**Цель:** реализовать фабрику для динамического создания объектов с DI и написать юнит-тесты без зависимости от Unity

#### Архитектура фабрики



```csharp
// Задача: EnemyFactory должна создавать врагов разных типов,
// при этом каждый враг получает инжектированные зависимости

IEnemyFactory
    └── EnemyFactory
            ├── Goblin  → IAudioService + IPlayerLocator + GoblinConfig
            ├── Orc     → IAudioService + IPlayerLocator + OrcConfig
            └── Boss    → IAudioService + IPlayerLocator + BossConfig
                              ↑                ↑               ↑
                         из Scope         из Scope       из EnemyLibrary
```

#### Эталонное решение



```csharp
// ── Базовая абстракция ────────────────────────────────────────────

public enum EnemyType { Goblin, Orc, Boss }

[Serializable]
public class EnemyConfig
{
    public EnemyType Type;
    public int       Health;
    public int       Damage;
    public float     Speed;
    public string    DeathSfx;
}

public interface IEnemy
{
    EnemyType Type    { get; }
    int       Health  { get; }
    bool      IsAlive { get; }
    void      TakeDamage(int damage);
    void      Tick(float dt);
}

public interface IPlayerLocator
{
    Vector3 Position { get; }
    bool    IsAlive  { get; }
}

public interface IEnemyFactory
{
    IEnemy Create(EnemyType type, Vector3 position);
    bool   CanSpawn { get; }
}

// ── Реализация врагов ─────────────────────────────────────────────

public abstract class EnemyBase : IEnemy
{
    protected readonly IAudioService  Audio;
    protected readonly IPlayerLocator Player;
    protected readonly EnemyConfig    Config;

    public abstract EnemyType Type { get; }
    public int  Health  { get; protected set; }
    public bool IsAlive => Health > 0;

    public Vector3 Position { get; set; }

    protected EnemyBase(IAudioService audio, IPlayerLocator player, EnemyConfig config)
    {
        Audio   = audio;
        Player  = player;
        Config  = config;
        Health  = config.Health;
    }

    public virtual void TakeDamage(int damage)
    {
        if (!IsAlive) return;
        Health = Mathf.Max(0, Health - damage);
        if (!IsAlive) Audio.PlaySfx(Config.DeathSfx);
    }

    public virtual void Tick(float dt)
    {
        if (!IsAlive || !Player.IsAlive) return;
        MoveToward(Player.Position, dt);
    }

    protected void MoveToward(Vector3 target, float dt)
    {
        var dir = (target - Position).normalized;
        Position += dir * Config.Speed * dt;
    }
}

public class GoblinEnemy : EnemyBase
{
    public override EnemyType Type => EnemyType.Goblin;

    private readonly float _baseSpeed;

    public GoblinEnemy(IAudioService audio, IPlayerLocator player, EnemyConfig config)
        : base(audio, player, config) => _baseSpeed = config.Speed;

    public override void Tick(float dt)
    {
        // Ускоряется при низком HP
        var ratio = (float)Health / Config.Health;
        Config.Speed = ratio < 0.3f ? _baseSpeed * 2f : _baseSpeed;
        base.Tick(dt);
    }
}

public class OrcEnemy : EnemyBase
{
    public override EnemyType Type => EnemyType.Orc;

    private readonly IRandomProvider _random;

    public OrcEnemy(IAudioService audio, IPlayerLocator player,
                    EnemyConfig config, IRandomProvider random)
        : base(audio, player, config) => _random = random;

    public override void TakeDamage(int damage)
    {
        // 30% шанс заблокировать
        if (_random.Value < 0.3f)
        {
            Audio.PlaySfx("orc_block");
            return;
        }
        base.TakeDamage(damage);
    }
}

public class BossEnemy : EnemyBase
{
    public override EnemyType Type => EnemyType.Boss;

    private bool _phase2;

    public BossEnemy(IAudioService audio, IPlayerLocator player, EnemyConfig config)
        : base(audio, player, config)
    {
        Audio.PlayMusic("boss_theme");
    }

    public override void TakeDamage(int damage)
    {
        base.TakeDamage(damage);

        if (!_phase2 && (float)Health / Config.Health < 0.5f)
        {
            _phase2      = true;
            Config.Speed *= 1.5f;
            Audio.PlaySfx("boss_rage");
            Debug.Log("[Boss] Phase 2!");
        }

        if (!IsAlive)
            Audio.PlayMusic("victory");
    }
}

// ── Интерфейс для инжектируемого рандома ─────────────────────────

public interface IRandomProvider
{
    float Value { get; }
}

public class UnityRandomProvider : IRandomProvider
{
    public float Value => Random.value;
}

// ── Фабрика ───────────────────────────────────────────────────────

[CreateAssetMenu(menuName = "Game/EnemyLibrary")]
public class EnemyLibrary : ScriptableObject
{
    [SerializeField] private EnemyConfig[] _configs;

    private Dictionary<EnemyType, EnemyConfig> _map;

    private void OnEnable()
    {
        _map = _configs.ToDictionary(c => c.Type);
    }

    public EnemyConfig Get(EnemyType type) => _map[type];
}

public class EnemyFactory : IEnemyFactory
{
    private readonly IObjectResolver _resolver;
    private readonly EnemyLibrary    _library;
    private readonly int             _maxEnemies;

    private readonly List<IEnemy> _alive = new();

    public bool CanSpawn => _alive.Count(e => e.IsAlive) < _maxEnemies;

    public EnemyFactory(IObjectResolver resolver, EnemyLibrary library, LevelData level)
    {
        _resolver   = resolver;
        _library    = library;
        _maxEnemies = level.MaxEnemies;
    }

    public IEnemy Create(EnemyType type, Vector3 position)
    {
        if (!CanSpawn) return null;

        var config = _library.Get(type);
        var enemy  = Instantiate(type, config);

        enemy.Position = position;
        _alive.Add(enemy);

        _alive.RemoveAll(e => !e.IsAlive);
        return enemy;
    }

    private IEnemy Instantiate(EnemyType type, EnemyConfig config)
    {
        // IObjectResolver инжектирует IAudioService и IPlayerLocator автоматически
        return type switch
        {
            EnemyType.Goblin => new GoblinEnemy(
                _resolver.Resolve<IAudioService>(),
                _resolver.Resolve<IPlayerLocator>(),
                config),

            EnemyType.Orc => new OrcEnemy(
                _resolver.Resolve<IAudioService>(),
                _resolver.Resolve<IPlayerLocator>(),
                config,
                _resolver.Resolve<IRandomProvider>()),

            EnemyType.Boss => new BossEnemy(
                _resolver.Resolve<IAudioService>(),
                _resolver.Resolve<IPlayerLocator>(),
                config),

            _ => throw new ArgumentException($"Unknown: {type}")
        };
    }
}

// ── Регистрация ───────────────────────────────────────────────────

public class GameplayScope : LifetimeScope
{
    [SerializeField] private EnemyLibrary _enemyLibrary;
    [SerializeField] private LevelConfig  _levelConfig;

    protected override void Configure(IContainerBuilder builder)
    {
        builder.RegisterInstance(_enemyLibrary);
        builder.RegisterInstance(_levelConfig);

        builder.Register<LevelData>                              (Lifetime.Singleton);
        builder.Register<IRandomProvider, UnityRandomProvider>   (Lifetime.Singleton);
        builder.Register<IPlayerLocator,  PlayerLocatorAdapter>  (Lifetime.Singleton);
        builder.Register<IEnemyFactory,   EnemyFactory>          (Lifetime.Singleton);

        builder.RegisterEntryPoint<GameplayLoop>();
    }
}
```

#### Unit-тесты без Unity



```csharp
// ── Моки ──────────────────────────────────────────────────────────

// Создайте папку Tests/Editor/ и добавьте assembly definition
// с галочкой "Editor" и без галочки "Any Platform"

public class MockAudio : IAudioService
{
    public List<string> Sfx   { get; } = new();
    public List<string> Music { get; } = new();

    public void PlaySfx(string sfx)    => Sfx.Add(sfx);
    public void PlayMusic(string track) => Music.Add(track);
    public void StopAll()               { }
}

public class MockPlayerLocator : IPlayerLocator
{
    public Vector3 Position { get; set; } = Vector3.zero;
    public bool    IsAlive  { get; set; } = true;
}

public class MockRandom : IRandomProvider
{
    public float Value { get; set; } = 0f;
}

public class MockEnemy : IEnemy
{
    public EnemyType Type    { get; }
    public int       Health  { get; private set; }
    public bool      IsAlive => Health > 0;

    public int DamageTaken { get; private set; }

    public MockEnemy(EnemyType type = EnemyType.Goblin, int health = 50)
    {
        Type   = type;
        Health = health;
    }

    public void TakeDamage(int d) { DamageTaken += d; Health -= d; }
    public void Tick(float dt)    { }
}

// ── Тесты ScoreService ────────────────────────────────────────────

[TestFixture]
public class ScoreServiceTests
{
    private ScoreService _svc;

    [SetUp]
    public void SetUp() => _svc = new ScoreService();

    [Test]
    public void InitialScore_IsZero() =>
        Assert.AreEqual(0, _svc.Score);

    [Test]
    public void Add_IncreasesScore()
    {
        _svc.Add(100);
        Assert.AreEqual(100, _svc.Score);
    }

    [Test]
    public void Add_Accumulates()
    {
        _svc.Add(100);
        _svc.Add(200);
        Assert.AreEqual(300, _svc.Score);
    }

    [Test]
    public void Reset_ClearsScore()
    {
        _svc.Add(500);
        _svc.Reset();
        Assert.AreEqual(0, _svc.Score);
    }

    [TestCase(100, 1, 100)]
    [TestCase(100, 2, 200)]
    [TestCase(50,  3, 150)]
    [TestCase(0,   5,   0)]
    public void Add_WithMultiplier(int pts, int mult, int expected)
    {
        _svc.SetMultiplier(mult);
        _svc.Add(pts);
        Assert.AreEqual(expected, _svc.Score);
    }
}

// ── Тесты GoblinEnemy ─────────────────────────────────────────────

[TestFixture]
public class GoblinEnemyTests
{
    private MockAudio         _audio;
    private MockPlayerLocator _player;
    private EnemyConfig       _cfg;

    [SetUp]
    public void SetUp()
    {
        _audio  = new MockAudio();
        _player = new MockPlayerLocator { IsAlive = true };
        _cfg    = new EnemyConfig
        {
            Type     = EnemyType.Goblin,
            Health   = 100,
            Speed    = 3f,
            DeathSfx = "goblin_death"
        };
    }

    [Test]
    public void Health_EqualsConfigHealth()
    {
        var g = new GoblinEnemy(_audio, _player, _cfg);
        Assert.AreEqual(100, g.Health);
    }

    [Test]
    public void TakeDamage_ReducesHealth()
    {
        var g = new GoblinEnemy(_audio, _player, _cfg);
        g.TakeDamage(40);
        Assert.AreEqual(60, g.Health);
    }

    [Test]
    public void FatalDamage_Dies()
    {
        var g = new GoblinEnemy(_audio, _player, _cfg);
        g.TakeDamage(9999);
        Assert.IsFalse(g.IsAlive);
        Assert.AreEqual(0, g.Health);
    }

    [Test]
    public void Death_PlaysDeathSfx()
    {
        var g = new GoblinEnemy(_audio, _player, _cfg);
        g.TakeDamage(9999);
        Assert.Contains("goblin_death", _audio.Sfx);
    }

    [Test]
    public void Dead_DoesNotTakeMoreDamage()
    {
        var g = new GoblinEnemy(_audio, _player, _cfg);
        g.TakeDamage(9999);
        var sfxCount = _audio.Sfx.Count;
        g.TakeDamage(100);
        Assert.AreEqual(0,        g.Health);
        Assert.AreEqual(sfxCount, _audio.Sfx.Count);
    }
}

// ── Тесты OrcEnemy (детерминированный рандом) ─────────────────────

[TestFixture]
public class OrcEnemyTests
{
    private MockAudio         _audio;
    private MockPlayerLocator _player;
    private MockRandom        _rng;
    private EnemyConfig       _cfg;

    [SetUp]
    public void SetUp()
    {
        _audio  = new MockAudio();
        _player = new MockPlayerLocator { IsAlive = true };
        _rng    = new MockRandom();
        _cfg    = new EnemyConfig { Type = EnemyType.Orc, Health = 200 };
    }

    [Test]
    public void Block_WhenRandomBelowThreshold()
    {
        _rng.Value = 0f; // Гарантированный блок
        var orc    = new OrcEnemy(_audio, _player, _cfg, _rng);
        orc.TakeDamage(50);

        Assert.AreEqual(200, orc.Health, "Should block — health unchanged");
        Assert.Contains("orc_block", _audio.Sfx);
    }

    [Test]
    public void NoBlock_WhenRandomAboveThreshold()
    {
        _rng.Value = 1f; // Гарантированный пропуск блока
        var orc    = new OrcEnemy(_audio, _player, _cfg, _rng);
        orc.TakeDamage(50);

        Assert.AreEqual(150, orc.Health, "Should not block — health reduced");
    }
}

// ── Тесты BossEnemy ───────────────────────────────────────────────

[TestFixture]
public class BossEnemyTests
{
    private MockAudio         _audio;
    private MockPlayerLocator _player;
    private EnemyConfig       _cfg;

    [SetUp]
    public void SetUp()
    {
        _audio  = new MockAudio();
        _player = new MockPlayerLocator { IsAlive = true };
        _cfg    = new EnemyConfig { Type = EnemyType.Boss, Health = 1000, Speed = 1f };
    }

    [Test]
    public void Spawn_PlaysBossTheme()
    {
        _ = new BossEnemy(_audio, _player, _cfg);
        Assert.Contains("boss_theme", _audio.Music);
    }

    [Test]
    public void Phase2_ActivatesAt50Percent()
    {
        var boss = new BossEnemy(_audio, _player, _cfg);
        boss.TakeDamage(510); // 49% HP

        Assert.Contains("boss_rage", _audio.Sfx);
    }

    [Test]
    public void Phase2_ActivatesOnlyOnce()
    {
        var boss = new BossEnemy(_audio, _player, _cfg);
        boss.TakeDamage(510);
        boss.TakeDamage(100);

        var rageCount = _audio.Sfx.Count(s => s == "boss_rage");
        Assert.AreEqual(1, rageCount);
    }

    [Test]
    public void Death_PlaysVictory()
    {
        var boss = new BossEnemy(_audio, _player, _cfg);
        boss.TakeDamage(9999);

        Assert.Contains("victory", _audio.Music);
    }
}
```

#### Критерии приёмки



```csharp
ФАБРИКА:
✅ EnemyFactory не использует new() для создания врагов напрямую
✅ IAudioService и IPlayerLocator инжектируются, не передаются вручную
✅ Нельзя создать больше MaxEnemies врагов одновременно

ТЕСТЫ (Window → General → Test Runner → EditMode):
✅ Все тесты зелёные без запуска сцены
✅ OrcEnemy: тест блока детерминирован (MockRandom, не Random.value)
✅ BossEnemy: Phase2 активируется ровно один раз
✅ ScoreService: параметризованные тесты покрывают граничные случаи
✅ Нет using UnityEngine.TestTools (не нужен для EditMode)
```

---

## 7. Типичные ошибки при первом знакомстве с DI

### Ошибка 1: Контейнер как Service Locator



```csharp
// ❌ АНТИПАТТЕРН — Service Locator
// Скрытые зависимости, нет преимуществ DI
public class PlayerService
{
    private readonly IObjectResolver _container;

    public PlayerService(IObjectResolver container)
    {
        _container = container;
    }

    public void Attack()
    {
        // Что нужно PlayerService? Неизвестно без чтения всех методов
        var audio = _container.Resolve<IAudioManager>();
        var vfx   = _container.Resolve<IVFXManager>();
        audio.PlaySfx("attack");
        vfx.SpawnEffect("slash");
    }
}

// ✅ ПРАВИЛЬНО — явные зависимости
public class PlayerService
{
    private readonly IAudioManager _audio;
    private readonly IVFXManager   _vfx;

    // Видно сразу: PlayerService нужны audio и vfx
    public PlayerService(IAudioManager audio, IVFXManager vfx)
    {
        _audio = audio;
        _vfx   = vfx;
    }

    public void Attack()
    {
        _audio.PlaySfx("attack");
        _vfx.SpawnEffect("slash");
    }
}

// IObjectResolver допустим ТОЛЬКО в фабриках
public class EnemyFactory
{
    private readonly IObjectResolver _resolver; // ← ок в фабрике

    public IEnemy Create(EnemyType type)
    {
        return _resolver.Resolve<IEnemy>(); // фабричная логика
    }
}
```

---

### Ошибка 2: Слишком толстый LifetimeScope



```csharp
// ❌ ПРОБЛЕМА: всё в одном месте, трудно поддерживать
public class GameScope : LifetimeScope
{
    protected override void Configure(IContainerBuilder builder)
    {
        // 50+ регистраций в одном методе Configure...
        builder.Register<AudioManager>    (Lifetime.Singleton);
        builder.Register<InputManager>    (Lifetime.Singleton);
        builder.Register<PlayerService>   (Lifetime.Singleton);
        builder.Register<EnemyManager>    (Lifetime.Singleton);
        builder.Register<UIManager>       (Lifetime.Singleton);
        builder.Register<InventoryService>(Lifetime.Singleton);
        builder.Register<QuestService>    (Lifetime.Singleton);
        // ...и ещё 40 строк
    }
}

// ✅ ПРАВИЛЬНО: метод-расширения для группировки
public static class ContainerBuilderExtensions
{
    public static IContainerBuilder AddAudio(this IContainerBuilder b)
    {
        b.Register<IAudioManager, AudioManager>(Lifetime.Singleton);
        b.Register<IMusicPlayer,  MusicPlayer> (Lifetime.Singleton);
        return b;
    }

    public static IContainerBuilder AddPlayer(this IContainerBuilder b)
    {
        b.Register<IPlayerService,    PlayerService>   (Lifetime.Singleton);
        b.Register<IPlayerController, PlayerController>(Lifetime.Singleton);
        return b;
    }

    public static IContainerBuilder AddEnemies(this IContainerBuilder b)
    {
        b.Register<IEnemyManager, EnemyManager>(Lifetime.Singleton);
        b.Register<IEnemyFactory, EnemyFactory>(Lifetime.Singleton);
        return b;
    }
}

public class GameScope : LifetimeScope
{
    protected override void Configure(IContainerBuilder builder)
    {
        builder
            .AddAudio()
            .AddPlayer()
            .AddEnemies();

        builder.RegisterEntryPoint<GameLoop>();
    }
}
```

---

### Ошибка 3: Тяжёлая логика в конструкторе



```csharp
// ❌ ПРОБЛЕМА: конструктор делает работу
// VContainer вызывает конструктор при ПОСТРОЕНИИ контейнера
// — всё это выполнится до Start любого MonoBehaviour
public class EnemySpawner
{
    public EnemySpawner(LevelConfig config)
    {
        // Долгие операции блокируют инициализацию контейнера
        LoadAllEnemyPrefabs();       // I/O операция
        InitializeObjectPool(100);   // выделение памяти
        RegisterSpawnPoints();       // поиск в сцене
        StartBackgroundPreload();    // запуск корутины? нет, мы не MonoBehaviour
    }
}

// ✅ ПРАВИЛЬНО: конструктор только сохраняет зависимости
public class EnemySpawner : IStartable
{
    private readonly LevelConfig _config;

    public EnemySpawner(LevelConfig config)
    {
        _config = config; // только сохраняем — мгновенно
    }

    // Тяжёлая инициализация — в Start, когда все зависимости готовы
    public void Start()
    {
        LoadAllEnemyPrefabs();
        InitializeObjectPool(100);
        RegisterSpawnPoints();
    }
}
```

---

### Ошибка 4: Captive Dependency



```csharp
// ❌ ПРОБЛЕМА: Singleton "захватывает" Transient
// SoundEffect помечен Transient, но будет создан ОДИН РАЗ
// и застрянет в Singleton навсегда
public class AudioManager  // Singleton
{
    private readonly SoundEffect _effect; // Transient — но это НЕ поможет

    public AudioManager(SoundEffect effect)
    {
        // SoundEffect создан при создании AudioManager
        // и больше не пересоздаётся — Transient бесполезен
        _effect = effect;
    }
}

// ✅ ПРАВИЛЬНО: Singleton хранит фабрику, не экземпляр
public class AudioManager  // Singleton
{
    private readonly Func<SoundEffect> _effectFactory;

    // Func<T> — VContainer автоматически создаёт фабрику для Transient
    public AudioManager(Func<SoundEffect> effectFactory)
    {
        _effectFactory = effectFactory;
    }

    public void PlayEffect()
    {
        var effect = _effectFactory(); // Новый Transient при каждом вызове
        effect.Play();
    }
}
```

---

### Ошибка 5: Circular Dependency



```csharp
// ❌ ПРОБЛЕМА: A зависит от B, B зависит от A
// VContainer выбросит исключение при построении контейнера
public class PlayerService
{
    public PlayerService(GameManager gm) { } // нужен GameManager
}

public class GameManager
{
    public GameManager(PlayerService ps) { } // нужен PlayerService
    // Circular dependency: PlayerService → GameManager → PlayerService
}

// ✅ РЕШЕНИЕ 1: общий посредник — разрывает цикл
public class GameEventBus
{
    public event Action PlayerDied;
    public event Action GameOver;
}

public class PlayerService
{
    public PlayerService(GameEventBus events)
    {
        // Подписывается на события, не зависит от GameManager
    }
}

public class GameManager
{
    public GameManager(GameEventBus events)
    {
        events.PlayerDied += OnPlayerDied; // Реагирует через события
    }
}

// ✅ РЕШЕНИЕ 2: Lazy<T> — откладывает резолв
public class PlayerService
{
    private readonly Lazy<GameManager> _gm;

    public PlayerService(Lazy<GameManager> gm)
    {
        _gm = gm; // GameManager создастся при первом обращении к _gm.Value
    }
}
```

---

### Ошибка 6: Неправильный Lifetime



```csharp
// ❌ ПРОБЛЕМА: LevelData как Singleton в ProjectScope
// При смене уровня данные НЕ СБРОСЯТСЯ — они живут вечно
public class ProjectScope : LifetimeScope
{
    protected override void Configure(IContainerBuilder builder)
    {
        builder.Register<LevelData>(Lifetime.Singleton); // ← ВЕЧНЫЙ LevelData!
    }
}

// ❌ ПРОБЛЕМА: AudioManager как Transient
// При каждом запросе — новый экземпляр, состояние не сохраняется
public class GameScope : LifetimeScope
{
    protected override void Configure(IContainerBuilder builder)
    {
        builder.Register<AudioManager>(Lifetime.Transient);
        // PlayerService и UIManager получат РАЗНЫЕ AudioManager!
    }
}

// ✅ ПРАВИЛЬНО: каждый объект в правильном scope

// ProjectScope — только то, что живёт всегда
builder.Register<IAudioManager,   AudioManager>  (Lifetime.Singleton);
builder.Register<IInputService,   InputService>  (Lifetime.Singleton);
builder.Register<ISettingsService,SettingsService>(Lifetime.Singleton);

// GameplayScope — только то, что живёт в течение сессии
builder.Register<LevelData>     (Lifetime.Singleton); // Singleton ВНУТРИ scope
builder.Register<EnemySpawner>  (Lifetime.Singleton);
builder.Register<ScoreSystem>   (Lifetime.Singleton);

// Transient — только для кратковременных объектов без состояния
builder.Register<DamagePopup>   (Lifetime.Transient);
builder.Register<PickupEffect>  (Lifetime.Transient);
```

---

### Ошибка 7: Тестирование с зависимостью от UnityEngine



```csharp
// ❌ ПРОБЛЕМА: тест зависит от UnityEngine
[Test]
public void ScoreService_Add()
{
    var svc = new ScoreService();
    svc.Add(100);
    // ScoreService внутри вызывает Debug.Log
    // В EditMode тестах это иногда падает или засоряет логи
    Assert.AreEqual(100, svc.Score);
}

// ❌ ПРОБЛЕМА: нетестируемый рандом
[Test]
public void OrcEnemy_CanBlock()
{
    var orc = CreateOrc();
    orc.TakeDamage(50);
    // Тест случайно провалится когда блока нет — нестабильный тест!
    Assert.AreEqual(200, orc.Health);
}

// ✅ РЕШЕНИЕ: инжектируемый логгер и рандом

// Заменяем Debug.Log на интерфейс
public interface IGameLogger { void Log(string msg); }
public class UnityLogger : IGameLogger { public void Log(string m) => Debug.Log(m); }
public class NullLogger   : IGameLogger { public void Log(string m) { } }

// Заменяем Random.value на интерфейс
public interface IRandomProvider { float Value { get; } }
public class UnityRandom : IRandomProvider { public float Value => Random.value; }
public class FixedRandom  : IRandomProvider { public float Value { get; set; } }

// Теперь тест детерминирован
[Test]
public void OrcEnemy_AlwaysBlocks_WhenRandomIsZero()
{
    var rng = new FixedRandom { Value = 0f }; // Гарантированный блок
    var orc = new OrcEnemy(_audio, _player, _cfg, rng);
    orc.TakeDamage(50);
    Assert.AreEqual(200, orc.Health);
}

[Test]
public void OrcEnemy_NeverBlocks_WhenRandomIsOne()
{
    var rng = new FixedRandom { Value = 1f }; // Гарантированный пропуск
    var orc = new OrcEnemy(_audio, _player, _cfg, rng);
    orc.TakeDamage(50);
    Assert.AreEqual(150, orc.Health);
}
```

---

### Ошибка 8: Забыть зарегистрировать зависимость



```csharp
// ❌ Забыли зарегистрировать IScoreSystem
protected override void Configure(IContainerBuilder builder)
{
    builder.Register<IPlayerService, PlayerService>(Lifetime.Singleton);
    // builder.Register<IScoreSystem, ScoreSystem>(Lifetime.Singleton); ← ЗАБЫЛИ
}

// PlayerService в конструкторе ожидает IScoreSystem
// VContainer выбросит: "VContainer.VContainerException: Unable to resolve IScoreSystem"
// Ошибка только в рантайме — неудобно

// ✅ Группируйте регистрации, чтобы не терять зависимости
public static class PlayerInstaller
{
    public static IContainerBuilder AddPlayerSystems(this IContainerBuilder b)
    {
        // PlayerService и все его зависимости — в одном месте
        b.Register<IScoreSystem,  ScoreSystem> (Lifetime.Singleton); // зависимость
        b.Register<IPlayerService, PlayerService>(Lifetime.Singleton); // потребитель
        return b;
    }
}
```

---

### Краткая шпаргалка ошибок



```csharp
Ошибка                      Симптом                  Решение
──────────────────────────────────────────────────────────────────────
Service Locator             Скрытые зависимости      Явный конструктор
Толстый LifetimeScope       Нечитаемый Configure     Installer-методы
Логика в конструкторе       Медленный старт          Перенести в Start()
Captive Dependency          Transient ведёт как SI   Func<T> вместо T
Circular Dependency         Exception при старте     EventBus или Lazy<T>
Неверный Lifetime           Потеря/дублирование      Scope-диаграмма
Нетестируемый рандом        Нестабильные тесты       IRandomProvider
Незарегистрированный тип    Exception в рантайме     Installer-группировка
```

---

## 8. Чеклист готовности проекта

### Архитектура



```csharp
РЕГИСТРАЦИЯ
□ Все зависимости зарегистрированы в LifetimeScope.Configure()
□ Нет RegisterInstance для объектов, которые должны пересоздаваться
□ Singleton используется для stateful сервисов и менеджеров
□ Transient используется только для кратковременных объектов
□ Scoped используется для данных конкретного уровня / UI-экрана
□ Configure() разбит на Installer-методы если больше 15 регистраций

ЗАВИСИМОСТИ
□ Все зависимости объявлены в конструкторе (не в Awake / Start)
□ Нет FindObjectOfType в продуктовом коде (Ctrl+Shift+F)
□ Нет статических синглтонов (найти через "static Instance")
□ Нет прямых вызовов Container.Resolve() вне фабрик
□ MonoBehaviour получают зависимости через [Inject] метод

SCOPES
□ ProjectScope содержит только глобальные, всегда нужные сервисы
□ GameplayScope создаётся и уничтожается с уровнем
□ UI Scopes создаются при открытии экрана, уничтожаются при закрытии
□ Дочерний scope не дублирует регистрации родительского
□ Dispose() вызывается при уничтожении scope (проверить в логах)
```

### Код



```csharp
ЧИСТОТА
□ Бизнес-логика не содержит using VContainer (кроме [Inject])
□ Интерфейсы определены для всех тестируемых сервисов
□ Конструкторы не содержат бизнес-логику (только присваивание)
□ IDisposable реализован для объектов с ресурсами

ENTRYPOINTS
□ Используются IStartable / ITickable вместо MonoBehaviour где возможно
□ IDisposable.Dispose() освобождает все ресурсы EntryPoint
□ Порядок инициализации не зависит от Script Execution Order
```

### Тесты



```csharp
ПОКРЫТИЕ
□ Все сервисы с бизнес-логикой покрыты EditMode тестами
□ Тесты не зависят от UnityEngine (нет TestRunner RuntimeMode)
□ Нет тестов с Random.value (заменить на IRandomProvider)
□ Каждый тест проверяет одну вещь (один Assert на тест)
□ Mock-объекты реализованы для всех интерфейсов-зависимостей

ЗАПУСК
□ Все тесты зелёные в Window → General → Test Runner → EditMode
□ Время выполнения тестового набора < 1 секунды
□ Тесты не зависят от порядка выполнения
```

### Производительность



```csharp
РАНТАЙМ
□ VContainerSettings назначен в Edit → Project Settings → VContainer
□ IL2CPP: проверена работа на мобильном устройстве (не только Editor)
□ Не используется Resolve<T>() в горячих путях (Update, FixedUpdate)
□ Все Transient объекты с IDisposable корректно освобождаются
```

---

## 9. Ресурсы для изучения

### Официальная документация



```csharp
VContainer GitHub
https://github.com/hadashiA/VContainer

VContainer Документация (EN)
https://vcontainer.hadashikick.jp/

VContainer Benchmark (сравнение производительности)
https://github.com/hadashiA/VContainer#benchmark
```

### Теория Dependency Injection



```csharp
Martin Fowler — Inversion of Control Containers and DI pattern
https://martinfowler.com/articles/injection.html
Обязательное чтение. Основополагающая статья по теме.

Microsoft — Dependency injection in .NET
https://docs.microsoft.com/en-us/dotnet/core/extensions/dependency-injection
Подробное объяснение концепций на примерах .NET.

SOLID Principles — Robert C. Martin
"Clean Architecture" (книга)
Почему DI — следствие принципа D из SOLID (Dependency Inversion).
```

### Unity и архитектура



```csharp
Unity Game Architecture with Scriptable Objects — Ryan Hipple (GDC 2017)
https://youtu.be/raQ3iHhE_Kk
Альтернативный взгляд на архитектуру Unity-проектов.

Zenject Documentation (для сравнения)
https://github.com/modesttree/Zenject
Полезно для понимания общих концепций DI в Unity.

Game Programming Patterns — Robert Nystrom (бесплатно онлайн)
https://gameprogrammingpatterns.com/
Паттерны Command, Observer, Service Locator — понять чем DI лучше.
```

### Тестирование



```csharp
Unity Test Framework Documentation
https://docs.unity3d.com/Packages/com.unity.test-framework@latest

NUnit Documentation
https://docs.nunit.org/
Документация по фреймворку тестирования.

"Working Effectively with Legacy Code" — Michael Feathers (книга)
Как тестировать код с жёсткими связями и как их разрывать.
```

### Смежные темы



```csharp
UniRx (Reactive Extensions for Unity)
https://github.com/neuecc/UniRx
Хорошо сочетается с DI для реактивного программирования.

UniTask
https://github.com/Cysharp/UniTask
Async/await для Unity — часто используется вместе с VContainer.

R3 (следующее поколение UniRx)
https://github.com/Cysharp/R3
Современная замена UniRx.
```

---

## Заключение

Dependency Injection — это не серебряная пуля и не обязательный элемент каждого проекта. Это инструмент, который решает конкретные проблемы: скрытые зависимости, нетестируемый код, хрупкую инициализацию. В прототипах и game jams синглтоны вполне оправданы. В командных проектах с длинным горизонтом поддержки — VContainer окупается уже через месяц.

Путь к чистой архитектуре не происходит за один день. Начните с малого:



```csharp
Шаг 1: Определите зависимости явно в конструкторах
        (уберите FindObjectOfType хотя бы в одном классе)

Шаг 2: Введите интерфейсы для ключевых сервисов
        (начните с AudioManager и PlayerService)

Шаг 3: Создайте первый LifetimeScope
        (зарегистрируйте 3–5 сервисов)

Шаг 4: Напишите первый юнит-тест
        (без Unity, за 5 секунд)

Шаг 5: Добавьте вложенные Scopes по мере роста проекта
        (когда почувствуете что нужно)
```

Код с правильно настроенным DI — это код, который **говорит правду**: его зависимости видны, поведение предсказуемо, изменения локальны. Именно такой код отличает проект, который развивается годами, от проекта, который переписывают с нуля каждые полгода