## Содержание

- [Содержание](#%D0%A1%D0%BE%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D0%BD%D0%B8%D0%B5)
- [Введение](#%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5)
	- [История, которую вы уже знаете](#%D0%98%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F,%20%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D1%83%D1%8E%20%D0%B2%D1%8B%20%D1%83%D0%B6%D0%B5%20%D0%B7%D0%BD%D0%B0%D0%B5%D1%82%D0%B5)
	- [Что такое архитектура в контексте Unity](#%D0%A7%D1%82%D0%BE%20%D1%82%D0%B0%D0%BA%D0%BE%D0%B5%20%D0%B0%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D0%B2%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BA%D1%81%D1%82%D0%B5%20Unity)
	- [Принципы, которые мы будем соблюдать](#%D0%9F%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF%D1%8B,%20%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D1%8B%D0%B5%20%D0%BC%D1%8B%20%D0%B1%D1%83%D0%B4%D0%B5%D0%BC%20%D1%81%D0%BE%D0%B1%D0%BB%D1%8E%D0%B4%D0%B0%D1%82%D1%8C)
	- [Стек технологий](#%D0%A1%D1%82%D0%B5%D0%BA%20%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B9)
- [Структура папок](#%D0%A1%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D0%BF%D0%B0%D0%BF%D0%BE%D0%BA)
- [Слои архитектуры](#%D0%A1%D0%BB%D0%BE%D0%B8%20%D0%B0%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D1%8B)
	- [Диаграмма архитектуры](#%D0%94%D0%B8%D0%B0%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B0%20%D0%B0%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D1%8B)
	- [Правила взаимодействия слоёв](#%D0%9F%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0%20%D0%B2%D0%B7%D0%B0%D0%B8%D0%BC%D0%BE%D0%B4%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%B8%D1%8F%20%D1%81%D0%BB%D0%BE%D1%91%D0%B2)
- [Связываем паттерны вместе](#%D0%A1%D0%B2%D1%8F%D0%B7%D1%8B%D0%B2%D0%B0%D0%B5%D0%BC%20%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%D1%8B%20%D0%B2%D0%BC%D0%B5%D1%81%D1%82%D0%B5)
	- [1. ScriptableObject как Data Layer](#1.%20ScriptableObject%20%D0%BA%D0%B0%D0%BA%20Data%20Layer)
	- [2. State Machine для игровой логики](#2.%20State%20Machine%20%D0%B4%D0%BB%D1%8F%20%D0%B8%D0%B3%D1%80%D0%BE%D0%B2%D0%BE%D0%B9%20%D0%BB%D0%BE%D0%B3%D0%B8%D0%BA%D0%B8)
	- [3. Observer через R3](#3.%20Observer%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20R3)
	- [4. Factory + Object Pool](#4.%20Factory%20+%20Object%20Pool)
	- [5. UI Toolkit + DOTween для Presentation](#5.%20UI%20Toolkit%20+%20DOTween%20%D0%B4%D0%BB%D1%8F%20Presentation)
	- [6. Cinemachine для Camera Layer](#6.%20Cinemachine%20%D0%B4%D0%BB%D1%8F%20Camera%20Layer)
	- [7. Service Locator — связываем всё вместе](#7.%20Service%20Locator%20%E2%80%94%20%D1%81%D0%B2%D1%8F%D0%B7%D1%8B%D0%B2%D0%B0%D0%B5%D0%BC%20%D0%B2%D1%81%D1%91%20%D0%B2%D0%BC%D0%B5%D1%81%D1%82%D0%B5)
- [Пример потока данных](#%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80%20%D0%BF%D0%BE%D1%82%D0%BE%D0%BA%D0%B0%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)
	- [Диаграмма потока](#%D0%94%D0%B8%D0%B0%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B0%20%D0%BF%D0%BE%D1%82%D0%BE%D0%BA%D0%B0)
	- [Реализация полного потока](#%D0%A0%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%BF%D0%BE%D1%82%D0%BE%D0%BA%D0%B0)
	- [Тест потока — симуляция урона](#%D0%A2%D0%B5%D1%81%D1%82%20%D0%BF%D0%BE%D1%82%D0%BE%D0%BA%D0%B0%20%E2%80%94%20%D1%81%D0%B8%D0%BC%D1%83%D0%BB%D1%8F%D1%86%D0%B8%D1%8F%20%D1%83%D1%80%D0%BE%D0%BD%D0%B0)
- [Чек-лист](#%D0%A7%D0%B5%D0%BA-%D0%BB%D0%B8%D1%81%D1%82)
	- [10 пунктов готовности проекта к разработке](#10%20%D0%BF%D1%83%D0%BD%D0%BA%D1%82%D0%BE%D0%B2%20%D0%B3%D0%BE%D1%82%D0%BE%D0%B2%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0%20%D0%BA%20%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B5)
	- [Антипаттерны — что НЕ делать](#%D0%90%D0%BD%D1%82%D0%B8%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%D1%8B%20%E2%80%94%20%D1%87%D1%82%D0%BE%20%D0%9D%D0%95%20%D0%B4%D0%B5%D0%BB%D0%B0%D1%82%D1%8C)

---

## Введение

### История, которую вы уже знаете

Каждый разработчик игр проходит через одно и то же. Первая неделя — восторг: скрипты пишутся быстро, всё работает, прогресс ощутим. Через месяц начинается тихий ужас. `GameManager` превратился в класс на 800 строк. `PlayerController` знает о UI, звуке, сохранениях и магазине одновременно. Исправление одного бага создаёт три новых в совершенно неожиданных местах.



```csharp
Типичная эволюция проекта без архитектуры:

Неделя 1:   GameManager.cs (50 строк)   — "всё отлично!"
Неделя 4:   GameManager.cs (400 строк)  — "ну, бывает..."
Неделя 8:   GameManager.cs (1200 строк) — "не трогай, работает"
Неделя 12:  GameManager.cs (2800 строк) — *разработчик уволился*
```

Проблема не в том, что вы плохо программируете. Проблема в том, что **без архитектурного плана каждое решение оптимально локально, но катастрофично глобально**.

### Что такое архитектура в контексте Unity

Архитектура — это не абстрактная теория из учебников. Это ответы на конкретные вопросы:

- Где хранятся данные об игроке?
- Как UI узнаёт что HP изменилось?
- Кто отвечает за спавн врагов?
- Как переключиться между состояниями игры?
- Где граница между игровой логикой и визуализацией?

### Принципы, которые мы будем соблюдать



```csharp
SOLID в контексте Unity:
│
├── S — Single Responsibility
│   PlayerHealth считает HP, НЕ обновляет UI
│   HUDController обновляет UI, НЕ знает о физике
│
├── O — Open/Closed
│   Новые типы врагов через наследование EnemyBase
│   Не трогаем рабочий код при добавлении нового контента
│
├── L — Liskov Substitution
│   IInteractable — любой объект взаимодействия взаимозаменяем
│
├── I — Interface Segregation
│   IDamageable, IHealable — отдельно, не один большой интерфейс
│
└── D — Dependency Inversion
    PlayerController зависит от IDamageable, не от конкретного PlayerHealth
```

### Стек технологий

В этой статье мы строим архитектуру на основе:

|Инструмент|Роль в архитектуре|
|---|---|
|**ScriptableObject**|Data Layer — конфигурации и данные|
|**R3 (ReactiveX)**|Observer — связь между слоями|
|**State Machine**|Domain Layer — игровая логика|
|**Factory + Object Pool**|Infrastructure — создание объектов|
|**UI Toolkit**|Presentation Layer — интерфейс|
|**DOTween**|Presentation Layer — анимации|
|**Cinemachine**|Camera Layer — управление камерой|

---

## Структура папок

Хорошая структура папок — первый архитектурный документ проекта. Она отражает как вы думаете о своём коде.



```csharp
Assets/
│
├── _Project/                          ← ВСЁ в одной папке (легко найти)
│   │
│   ├── Art/                           ← Визуальные ресурсы
│   │   ├── Animations/
│   │   │   ├── Player/
│   │   │   └── Enemies/
│   │   ├── Materials/
│   │   ├── Models/
│   │   │   ├── Characters/
│   │   │   ├── Environment/
│   │   │   └── Props/
│   │   ├── Sprites/
│   │   │   ├── UI/
│   │   │   └── World/
│   │   └── VFX/
│   │       ├── Particles/
│   │       └── Shaders/
│   │
│   ├── Audio/                         ← Звуковые ресурсы
│   │   ├── Music/
│   │   ├── SFX/
│   │   └── Mixers/
│   │
│   ├── Data/                          ← ScriptableObject ассеты
│   │   ├── Characters/
│   │   │   ├── PlayerData.asset
│   │   │   └── Enemies/
│   │   │       ├── GoblinData.asset
│   │   │       └── BossData.asset
│   │   ├── Items/
│   │   │   ├── Weapons/
│   │   │   └── Consumables/
│   │   ├── Levels/
│   │   │   ├── Level01Config.asset
│   │   │   └── Level02Config.asset
│   │   └── Settings/
│   │       ├── GameSettings.asset
│   │       └── AudioSettings.asset
│   │
│   ├── Prefabs/                       ← Готовые объекты
│   │   ├── Characters/
│   │   │   ├── Player.prefab
│   │   │   └── Enemies/
│   │   ├── Environment/
│   │   ├── UI/
│   │   │   ├── HUD.prefab
│   │   │   └── Menus/
│   │   ├── VFX/
│   │   └── Pools/                     ← Пулы объектов
│   │
│   ├── Scenes/                        ← Сцены
│   │   ├── Bootstrap.unity            ← Инициализация (загружается первой)
│   │   ├── MainMenu.unity
│   │   ├── Gameplay.unity
│   │   └── _Sandbox.unity             ← Тестовая сцена
│   │
│   ├── Scripts/                       ← Весь C# код
│   │   │
│   │   ├── Infrastructure/            ← Слой инфраструктуры
│   │   │   ├── Bootstrap/
│   │   │   │   ├── GameBootstrap.cs
│   │   │   │   └── SceneLoader.cs
│   │   │   ├── DI/
│   │   │   │   └── ServiceLocator.cs
│   │   │   ├── Factories/
│   │   │   │   ├── EnemyFactory.cs
│   │   │   │   └── ProjectileFactory.cs
│   │   │   ├── Pools/
│   │   │   │   ├── ObjectPool.cs
│   │   │   │   └── PoolManager.cs
│   │   │   └── SaveSystem/
│   │   │       ├── ISaveService.cs
│   │   │       └── JsonSaveService.cs
│   │   │
│   │   ├── Domain/                    ← Слой бизнес-логики
│   │   │   ├── Characters/
│   │   │   │   ├── Player/
│   │   │   │   │   ├── PlayerHealth.cs
│   │   │   │   │   ├── PlayerMovement.cs
│   │   │   │   │   └── PlayerInventory.cs
│   │   │   │   └── Enemies/
│   │   │   │       ├── EnemyBase.cs
│   │   │   │       ├── EnemyAI.cs
│   │   │   │       └── BossEnemy.cs
│   │   │   ├── Combat/
│   │   │   │   ├── IDamageable.cs
│   │   │   │   ├── DamageCalculator.cs
│   │   │   │   └── StatusEffects/
│   │   │   ├── StateMachine/
│   │   │   │   ├── IState.cs
│   │   │   │   ├── StateMachine.cs
│   │   │   │   └── States/
│   │   │   │       ├── GameplayState.cs
│   │   │   │       ├── PauseState.cs
│   │   │   │       └── GameOverState.cs
│   │   │   └── Progression/
│   │   │       ├── ExperienceSystem.cs
│   │   │       └── LevelSystem.cs
│   │   │
│   │   ├── Data/                      ← Слой данных (SO + модели)
│   │   │   ├── ScriptableObjects/
│   │   │   │   ├── CharacterStatsSO.cs
│   │   │   │   ├── ItemDataSO.cs
│   │   │   │   ├── EnemyDataSO.cs
│   │   │   │   └── LevelConfigSO.cs
│   │   │   └── Models/
│   │   │       ├── PlayerModel.cs
│   │   │       └── InventoryModel.cs
│   │   │
│   │   ├── Presentation/              ← Слой представления
│   │   │   ├── HUD/
│   │   │   │   ├── HUDController.cs
│   │   │   │   └── HUDAnimator.cs
│   │   │   ├── Menus/
│   │   │   │   ├── MainMenuController.cs
│   │   │   │   └── PauseMenuController.cs
│   │   │   └── Camera/
│   │   │       ├── CameraManager.cs
│   │   │       └── CameraShakeController.cs
│   │   │
│   │   └── Shared/                    ← Общий код
│   │       ├── Extensions/
│   │       │   ├── Vector3Extensions.cs
│   │       │   └── StringExtensions.cs
│   │       ├── Interfaces/
│   │       │   ├── IDamageable.cs
│   │       │   ├── IInteractable.cs
│   │       │   └── IPoolable.cs
│   │       └── Utils/
│   │           ├── MathUtils.cs
│   │           └── CoroutineUtils.cs
│   │
│   └── UI/                            ← UI Toolkit ресурсы
│       ├── Documents/
│       │   ├── HUD.uxml
│       │   ├── MainMenu.uxml
│       │   └── PauseMenu.uxml
│       └── Styles/
│           ├── Variables.uss
│           ├── Common.uss
│           └── HUD.uss
│
└── Plugins/                           ← Внешние пакеты (не трогать)
    ├── DOTween/
    └── R3/
```

> **Правило именования:** Префикс `_` у папки `_Project` ставит её первой в списке — вы видите свой код до папок `Packages` и `Plugins`.

---

## Слои архитектуры

### Диаграмма архитектуры



```csharp
┌─────────────────────────────────────────────────────────────────┐
│                     PRESENTATION LAYER                          │
│                                                                 │
│   ┌─────────────────┐  ┌──────────────┐  ┌──────────────────┐  │
│   │   UI Toolkit    │  │   DOTween    │  │   Cinemachine    │  │
│   │  HUDController  │  │ Animations   │  │  CameraManager   │  │
│   │  MenuController │  │ Transitions  │  │  VirtualCameras  │  │
│   └────────┬────────┘  └──────┬───────┘  └────────┬─────────┘  │
│            │                 │                    │             │
└────────────┼─────────────────┼────────────────────┼────────────┘
             │      Читают ReactiveProperty          │
             │      Подписываются на Observable      │
             ▼                 ▼                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                       DOMAIN LAYER                              │
│                                                                 │
│   ┌──────────────┐  ┌─────────────┐  ┌──────────────────────┐  │
│   │ PlayerHealth │  │ StateMachine│  │    EnemyAI           │  │
│   │ (R3 Subject) │  │             │  │                      │  │
│   └──────┬───────┘  └──────┬──────┘  └──────────────────────┘  │
│          │                 │                                     │
│          └────── Observable<float> ──────────────────────────►  │
│                   Events, ReactiveProperty                      │
└──────────────────────────┬──────────────────────────────────────┘
                           │ Читает конфигурацию
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                        DATA LAYER                               │
│                                                                 │
│   ┌──────────────────┐  ┌──────────────┐  ┌─────────────────┐  │
│   │ CharacterStatsSO │  │  PlayerModel │  │  LevelConfigSO  │  │
│   │ (ScriptableObject│  │  (Plain C#)  │  │                 │  │
│   └──────────────────┘  └──────────────┘  └─────────────────┘  │
└──────────────────────────┬──────────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────────┐
│                    INFRASTRUCTURE LAYER                         │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────────────┐ │
│  │ ObjectPool   │  │EnemyFactory  │  │ServiceLocator / DI    │ │
│  │ (переиспольз │  │(создаёт      │  │(связывает все слои)   │ │
│  │  объектов)   │  │ врагов)      │  │                       │ │
│  └──────────────┘  └──────────────┘  └───────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### Правила взаимодействия слоёв



```csharp
✅ Разрешено:
Presentation → Domain   (читать состояние, подписываться)
Domain       → Data     (читать конфигурацию)
Infrastructure → все    (создавать, регистрировать)

❌ Запрещено:
Domain       → Presentation  (логика НЕ знает об UI)
Data         → Domain        (данные НЕ содержат логику)
Presentation → Presentation  (контроллеры не зависят друг от друга)
```

---

## Связываем паттерны вместе

### 1. ScriptableObject как Data Layer

ScriptableObject — идеальное хранилище для данных, которые:

- Настраиваются дизайнером без кода
- Не меняются в Runtime (конфигурации)
- Переиспользуются между объектами



```csharp
// Файл: Scripts/Data/ScriptableObjects/CharacterStatsSO.cs
using UnityEngine;

/// <summary>
/// Базовые характеристики персонажа.
/// Создаётся через: Assets → Create → Game → Character Stats
/// </summary>
[CreateAssetMenu(
    fileName = "NewCharacterStats",
    menuName = "Game/Data/Character Stats",
    order = 1
)]
public class CharacterStatsSO : ScriptableObject
{
    [Header("Основные характеристики")]
    [SerializeField, Min(1)] private float maxHealth = 100f;
    [SerializeField, Min(0)] private float defense = 0f;
    [SerializeField, Min(0.1f)] private float moveSpeed = 5f;

    [Header("Боевые характеристики")]
    [SerializeField, Min(0)] private float attackDamage = 10f;
    [SerializeField, Min(0.1f)] private float attackSpeed = 1f;
    [SerializeField, Min(0.1f)] private float attackRange = 1.5f;

    [Header("Прогрессия")]
    [SerializeField] private AnimationCurve healthPerLevel;
    [SerializeField] private AnimationCurve damagePerLevel;

    // Публичный доступ только для чтения
    public float MaxHealth => maxHealth;
    public float Defense => defense;
    public float MoveSpeed => moveSpeed;
    public float AttackDamage => attackDamage;
    public float AttackSpeed => attackSpeed;
    public float AttackRange => attackRange;

    /// <summary>Получить HP для заданного уровня</summary>
    public float GetHealthForLevel(int level)
    {
        if (healthPerLevel == null || healthPerLevel.length == 0)
            return maxHealth + (level - 1) * 20f;

        return healthPerLevel.Evaluate(level);
    }

    /// <summary>Получить урон для заданного уровня</summary>
    public float GetDamageForLevel(int level)
    {
        if (damagePerLevel == null || damagePerLevel.length == 0)
            return attackDamage + (level - 1) * 2f;

        return damagePerLevel.Evaluate(level);
    }

#if UNITY_EDITOR
    void OnValidate()
    {
        maxHealth = Mathf.Max(1f, maxHealth);
        moveSpeed = Mathf.Max(0.1f, moveSpeed);
        attackSpeed = Mathf.Max(0.1f, attackSpeed);
    }
#endif
}
```



```csharp
// Файл: Scripts/Data/ScriptableObjects/EnemyDataSO.cs
using UnityEngine;

[CreateAssetMenu(
    fileName = "NewEnemyData",
    menuName = "Game/Data/Enemy Data"
)]
public class EnemyDataSO : ScriptableObject
{
    [Header("Идентификация")]
    [SerializeField] private string enemyName = "Enemy";
    [SerializeField] private EnemyType enemyType;

    [Header("Характеристики")]
    [SerializeField] private CharacterStatsSO stats;

    [Header("Поведение")]
    [SerializeField, Min(0)] private float detectionRadius = 8f;
    [SerializeField, Min(0)] private float chaseRadius = 15f;
    [SerializeField, Min(0)] private float patrolRadius = 5f;

    [Header("Награда")]
    [SerializeField, Min(0)] private int experienceReward = 10;
    [SerializeField, Min(0)] private int coinReward = 5;

    [Header("Визуал")]
    [SerializeField] private GameObject prefab;
    [SerializeField] private Color healthBarColor = Color.red;

    // Свойства
    public string EnemyName => enemyName;
    public EnemyType EnemyType => enemyType;
    public CharacterStatsSO Stats => stats;
    public float DetectionRadius => detectionRadius;
    public float ChaseRadius => chaseRadius;
    public float PatrolRadius => patrolRadius;
    public int ExperienceReward => experienceReward;
    public int CoinReward => coinReward;
    public GameObject Prefab => prefab;
    public Color HealthBarColor => healthBarColor;
}

public enum EnemyType { Melee, Ranged, Boss, Elite }
```



```csharp
// Файл: Scripts/Data/ScriptableObjects/LevelConfigSO.cs
using UnityEngine;

[CreateAssetMenu(
    fileName = "NewLevelConfig",
    menuName = "Game/Data/Level Config"
)]
public class LevelConfigSO : ScriptableObject
{
    [Header("Основное")]
    [SerializeField] private string levelName;
    [SerializeField] private string sceneName;
    [SerializeField] private int levelIndex;

    [Header("Волны врагов")]
    [SerializeField] private WaveConfig[] waves;

    [Header("Условия победы")]
    [SerializeField] private WinCondition winCondition;
    [SerializeField] private float timeLimit = 300f;
    [SerializeField] private int killsRequired = 0;

    [Header("Музыка")]
    [SerializeField] private AudioClip backgroundMusic;
    [SerializeField] private AudioClip bossMusic;

    public string LevelName => levelName;
    public string SceneName => sceneName;
    public int LevelIndex => levelIndex;
    public WaveConfig[] Waves => waves;
    public WinCondition WinCondition => winCondition;
    public float TimeLimit => timeLimit;
    public AudioClip BackgroundMusic => backgroundMusic;
    public AudioClip BossMusic => bossMusic;
}

[System.Serializable]
public class WaveConfig
{
    public EnemyDataSO[] enemyTypes;
    public int count;
    public float spawnInterval;
    public float delayBeforeWave;
}

public enum WinCondition { KillAll, Survive, CollectItems, ReachGoal }
```

### 2. State Machine для игровой логики



```csharp
// Файл: Scripts/Domain/StateMachine/IState.cs

/// <summary>Интерфейс состояния</summary>
public interface IState
{
    void Enter();
    void Update();
    void FixedUpdate();
    void Exit();
}
```



```csharp
// Файл: Scripts/Domain/StateMachine/StateMachine.cs
using System;
using System.Collections.Generic;
using UnityEngine;

/// <summary>
/// Универсальная State Machine.
/// Используется для Game Flow, AI врагов, анимаций персонажа.
/// </summary>
public class StateMachine
{
    private IState _currentState;
    private IState _previousState;

    // История переходов для дебага
    private readonly List<string> _transitionHistory = new();
    private const int MAX_HISTORY = 20;

    public IState CurrentState => _currentState;
    public string CurrentStateName => _currentState?.GetType().Name ?? "None";

    // События
    public event Action<IState, IState> OnStateChanged; // (from, to)

    /// <summary>Установить начальное состояние</summary>
    public void Initialize(IState initialState)
    {
        _currentState = initialState;
        _currentState.Enter();
        LogTransition(null, initialState);
    }

    /// <summary>Перейти в новое состояние</summary>
    public void ChangeState(IState newState)
    {
        if (newState == null)
        {
            Debug.LogError("[StateMachine] Попытка перейти в null состояние!");
            return;
        }

        if (newState == _currentState)
        {
            Debug.LogWarning($"[StateMachine] Уже в состоянии {CurrentStateName}");
            return;
        }

        var previousState = _currentState;

        _currentState?.Exit();
        _previousState = _currentState;
        _currentState = newState;
        _currentState.Enter();

        LogTransition(previousState, newState);
        OnStateChanged?.Invoke(previousState, newState);
    }

    /// <summary>Вернуться в предыдущее состояние</summary>
    public void RevertToPreviousState()
    {
        if (_previousState == null)
        {
            Debug.LogWarning("[StateMachine] Нет предыдущего состояния");
            return;
        }

        ChangeState(_previousState);
    }

    public void Update() => _currentState?.Update();
    public void FixedUpdate() => _currentState?.FixedUpdate();

    private void LogTransition(IState from, IState to)
    {
        string entry = $"{from?.GetType().Name ?? "None"} → {to.GetType().Name}";

        _transitionHistory.Add(entry);

        if (_transitionHistory.Count > MAX_HISTORY)
            _transitionHistory.RemoveAt(0);

#if UNITY_EDITOR
        Debug.Log($"[StateMachine] {entry}");
#endif
    }

    public IReadOnlyList<string> GetTransitionHistory() => _transitionHistory;
}
```



```csharp
// Файл: Scripts/Domain/StateMachine/States/GameplayState.cs
using UnityEngine;

public class GameplayState : IState
{
    private readonly GameCon _con;

    public GameplayState(GameCon con)
    {
        _con = con;
    }

    public void Enter()
    {
        Debug.Log("▶ Геймплей начат");
        Time.timeScale = 1f;
        _con.Player.EnableInput();
        _con.HUD.Show();
        _con.CameraManager.ActivateGameplayCamera();
    }

    public void Update()
    {
        // Проверка условий победы/поражения
        if (_con.Player.IsDead)
        {
            _con.GameStateMachine.ChangeState(
                new GameOverState(_con, isVictory: false)
            );
        }
    }

    public void FixedUpdate() { }

    public void Exit()
    {
        _con.Player.DisableInput();
    }
}
```



```csharp
// Файл: Scripts/Domain/StateMachine/States/PauseState.cs
using UnityEngine;

public class PauseState : IState
{
    private readonly GameCon _con;

    public PauseState(GameCon con)
    {
        _con = con;
    }

    public void Enter()
    {
        Debug.Log("⏸ Пауза");
        Time.timeScale = 0f;
        _con.PauseMenu.Show();
        _con.HUD.Hide();
    }

    public void Update() { }
    public void FixedUpdate() { }

    public void Exit()
    {
        Time.timeScale = 1f;
        _con.PauseMenu.Hide();
        _con.HUD.Show();
    }
}
```



```csharp
// Файл: Scripts/Domain/StateMachine/States/GameOverState.cs
using UnityEngine;

public class GameOverState : IState
{
    private readonly GameCon _con;
    private readonly bool _isVictory;

    public GameOverState(GameCon con, bool isVictory)
    {
        _con = con;
        _isVictory = isVictory;
    }

    public void Enter()
    {
        Debug.Log(_isVictory ? "🏆 Победа!" : "💀 Поражение");
        Time.timeScale = 0.3f; // Slow motion на момент game over

        _con.GameOverScreen.Show(_isVictory);
        _con.CameraManager.ActivateGameOverCamera();

        // Сохраняем прогресс
        if (_isVictory)
            _con.SaveService.SaveProgress();
    }

    public void Update() { }
    public void FixedUpdate() { }

    public void Exit()
    {
        Time.timeScale = 1f;
    }
}
```

### 3. Observer через R3



```csharp
// Файл: Scripts/Domain/Characters/Player/PlayerHealth.cs
using System;
using R3;
using UnityEngine;

/// <summary>
/// Отвечает ТОЛЬКО за логику здоровья.
/// Не знает об UI, звуке, камере — только об HP.
/// </summary>
public class PlayerHealth : MonoBehaviour, IDamageable
{
    [SerializeField] private CharacterStatsSO stats;

    // === Реактивные свойства (Observable для подписчиков) ===

    // ReactiveProperty — хранит значение И уведомляет подписчиков
    private readonly ReactiveProperty<float> _currentHP = new(0f);
    private readonly ReactiveProperty<float> _maxHP = new(0f);

    // Subject — только для генерации событий (нет хранимого значения)
    private readonly Subject<DamageInfo> _onDamaged = new();
    private readonly Subject<HealInfo> _onHealed = new();
    private readonly Subject<Unit> _onDeath = new();
    private readonly Subject<Unit> _onRevive = new();

    // Публичный read-only доступ
    public ReadOnlyReactiveProperty<float> CurrentHP => _currentHP;
    public ReadOnlyReactiveProperty<float> MaxHP => _maxHP;
    public Observable<DamageInfo> OnDamaged => _onDamaged;
    public Observable<HealInfo> OnHealed => _onHealed;
    public Observable<Unit> OnDeath => _onDeath;
    public Observable<Unit> OnRevive => _onRevive;

    // Производное свойство: процент HP
    public ReadOnlyReactiveProperty<float> HPPercent { get; private set; }

    // Обычные свойства
    public bool IsDead { get; private set; }
    public bool IsInvincible { get; set; }

    // Управление подписками
    private readonly CompositeDisposable _disposables = new();

    void Awake()
    {
        InitializeHP();
    }

    void OnDestroy()
    {
        _disposables.Dispose();
        _onDamaged.Dispose();
        _onHealed.Dispose();
        _onDeath.Dispose();
        _onRevive.Dispose();
        _currentHP.Dispose();
        _maxHP.Dispose();
    }

    private void InitializeHP()
    {
        float maxHp = stats != null ? stats.MaxHealth : 100f;
        _maxHP.Value = maxHp;
        _currentHP.Value = maxHp;

        // HPPercent — вычисляется реактивно при изменении CurrentHP или MaxHP
        HPPercent = _currentHP
            .CombineLatest(_maxHP, (current, max) =>
                max > 0f ? Mathf.Clamp01(current / max) : 0f)
            .ToReadOnlyReactiveProperty()
            .AddTo(_disposables);
    }

    // === IDamageable ===

    public void TakeDamage(DamageInfo damage)
    {
        if (IsDead || IsInvincible) return;

        // Применяем защиту
        float actualDamage = CalculateActualDamage(damage.Amount);

        if (actualDamage <= 0f) return;

        float previousHP = _currentHP.Value;
        _currentHP.Value = Mathf.Max(0f, _currentHP.Value - actualDamage);

        var info = new DamageInfo(
            amount: actualDamage,
            rawAmount: damage.Amount,
            damageType: damage.DamageType,
            source: damage.Source,
            isCritical: damage.IsCritical
        );

        // Уведомляем всех подписчиков
        _onDamaged.OnNext(info);

        Debug.Log($"💥 Урон: {actualDamage:F1} " +
                  $"(HP: {previousHP:F0} → {_currentHP.Value:F0})");

        if (_currentHP.Value <= 0f)
            HandleDeath();
    }

    public void Heal(float amount)
    {
        if (IsDead) return;
        if (amount <= 0f) return;

        float previousHP = _currentHP.Value;
        _currentHP.Value = Mathf.Min(_maxHP.Value, _currentHP.Value + amount);
        float actualHeal = _currentHP.Value - previousHP;

        if (actualHeal > 0f)
        {
            _onHealed.OnNext(new HealInfo(actualHeal));
            Debug.Log($"💚 Лечение: +{actualHeal:F1} HP");
        }
    }

    public void SetMaxHP(float newMaxHP, bool healToFull = false)
    {
        _maxHP.Value = Mathf.Max(1f, newMaxHP);

        if (healToFull)
            _currentHP.Value = _maxHP.Value;
        else
            _currentHP.Value = Mathf.Min(_currentHP.Value, _maxHP.Value);
    }

    public void Revive(float hpPercent = 1f)
    {
        if (!IsDead) return;

        IsDead = false;
        _currentHP.Value = _maxHP.Value * Mathf.Clamp01(hpPercent);
        _onRevive.OnNext(Unit.Default);

        Debug.Log($"✨ Возрождение с {_currentHP.Value:F0} HP");
    }

    private float CalculateActualDamage(float rawDamage)
    {
        float defense = stats != null ? stats.Defense : 0f;
        return Mathf.Max(0f, rawDamage - defense);
    }

    private void HandleDeath()
    {
        if (IsDead) return;

        IsDead = true;
        _currentHP.Value = 0f;
        _onDeath.OnNext(Unit.Default);

        Debug.Log("💀 Игрок погиб");
    }
}

// Вспомогательные структуры данных
public readonly struct DamageInfo
{
    public readonly float Amount;
    public readonly float RawAmount;
    public readonly DamageType DamageType;
    public readonly GameObject Source;
    public readonly bool IsCritical;

    public DamageInfo(float amount, float rawAmount, DamageType damageType,
        GameObject source, bool isCritical)
    {
        Amount = amount;
        RawAmount = rawAmount;
        DamageType = damageType;
        Source = source;
        IsCritical = isCritical;
    }
}

public readonly struct HealInfo
{
    public readonly float Amount;
    public HealInfo(float amount) => Amount = amount;
}

public enum DamageType { Physical, Magic, Fire, Ice, True }

public interface IDamageable
{
    void TakeDamage(DamageInfo damage);
    void Heal(float amount);
    bool IsDead { get; }
}
```

### 4. Factory + Object Pool



```csharp
// Файл: Scripts/Infrastructure/Pools/ObjectPool.cs
using System;
using System.Collections.Generic;
using UnityEngine;

/// <summary>
/// Универсальный Object Pool.
/// Переиспользует объекты вместо Instantiate/Destroy.
/// </summary>
public class ObjectPool<T> where T : Component, IPoolable
{
    private readonly Queue<T> _pool = new();
    private readonly T _prefab;
    private readonly Transform _container;
    private readonly int _maxSize;

    // Статистика
    private int _totalCreated;
    private int _activeCount;

    public int ActiveCount => _activeCount;
    public int PooledCount => _pool.Count;
    public int TotalCreated => _totalCreated;

    public ObjectPool(T prefab, Transform container,
        int initialSize = 10, int maxSize = 100)
    {
        _prefab = prefab ?? throw new ArgumentNullException(nameof(prefab));
        _container = container;
        _maxSize = maxSize;

        // Предварительное заполнение пула
        Prewarm(initialSize);
    }

    private void Prewarm(int count)
    {
        for (int i = 0; i < count; i++)
        {
            var item = CreateNew();
            item.gameObject.SetActive(false);
            _pool.Enqueue(item);
        }
    }

    /// <summary>Получить объект из пула</summary>
    public T Get(Vector3 position, Quaternion rotation)
    {
        T item;

        if (_pool.Count > 0)
        {
            item = _pool.Dequeue();
        }
        else
        {
            if (_totalCreated >= _maxSize)
            {
                Debug.LogWarning($"[ObjectPool<{typeof(T).Name}>] " +
                                 $"Достигнут максимум ({_maxSize})!");
                return null;
            }

            item = CreateNew();
        }

        item.transform.SetPositionAndRotation(position, rotation);
        item.gameObject.SetActive(true);
        item.OnSpawnFromPool();
        _activeCount++;

        return item;
    }

    /// <summary>Вернуть объект в пул</summary>
    public void Return(T item)
    {
        if (item == null) return;

        item.OnReturnToPool();
        item.gameObject.SetActive(false);
        item.transform.SetParent(_container);
        _pool.Enqueue(item);
        _activeCount = Mathf.Max(0, _activeCount - 1);
    }

    private T CreateNew()
    {
        var go = UnityEngine.Object.Instantiate(_prefab, _container);
        go.name = $"{_prefab.name}_{_totalCreated}";
        _totalCreated++;
        return go;
    }

    /// <summary>Вернуть все активные объекты</summary>
    public void ReturnAll()
    {
        // Находим все активные объекты из этого пула
        var children = new List<T>();
        foreach (Transform child in _container)
        {
            if (child.gameObject.activeSelf &&
                child.TryGetComponent<T>(out var item))
            {
                children.Add(item);
            }
        }

        foreach (var item in children)
            Return(item);
    }
}

/// <summary>Интерфейс для объектов использующих пул</summary>
public interface IPoolable
{
    void OnSpawnFromPool();
    void OnReturnToPool();
}
```



```csharp
// Файл: Scripts/Infrastructure/Pools/PoolManager.cs
using System.Collections.Generic;
using UnityEngine;

/// <summary>
/// Менеджер всех пулов объектов в игре.
/// Единая точка доступа к пулам.
/// </summary>
public class PoolManager : MonoBehaviour
{
    [Header("Пулы")]
    [SerializeField] private PoolConfig[] poolConfigs;

    private readonly Dictionary<string, object> _pools = new();
    private Transform _poolContainer;

    void Awake()
    {
        _poolContainer = new GameObject("=== POOLS ===").transform;
        DontDestroyOnLoad(_poolContainer.gameObject);

        InitializePools();
    }

    private void InitializePools()
    {
        foreach (var config in poolConfigs)
        {
            if (config.prefab == null) continue;

            var component = config.prefab.GetComponent<IPoolable>();
            if (component == null)
            {
                Debug.LogError($"Prefab {config.prefab.name} " +
                               $"не реализует IPoolable!");
                continue;
            }

            var container = new GameObject($"Pool_{config.poolName}").transform;
            container.SetParent(_poolContainer);

            // Создаём пул через рефлексию (для generics)
            Debug.Log($"✅ Пул создан: {config.poolName} " +
                      $"(начальный размер: {config.initialSize})");
        }
    }

    [System.Serializable]
    public class PoolConfig
    {
        public string poolName;
        public GameObject prefab;
        public int initialSize = 10;
        public int maxSize = 100;
    }
}
```



```csharp
// Файл: Scripts/Infrastructure/Factories/EnemyFactory.cs
using UnityEngine;

/// <summary>
/// Фабрика врагов.
/// Знает КАК создавать врагов, но не знает ЗАЧЕМ.
/// </summary>
public class EnemyFactory : MonoBehaviour
{
    [SerializeField] private Transform enemyContainer;

    // Пулы для каждого типа врага
    private ObjectPool<EnemyBase> _meleePool;
    private ObjectPool<EnemyBase> _rangedPool;
    private ObjectPool<EnemyBase> _bossPool;

    [Header("Префабы")]
    [SerializeField] private EnemyBase meleePrefab;
    [SerializeField] private EnemyBase rangedPrefab;
    [SerializeField] private EnemyBase bossPrefab;

    void Awake()
    {
        InitializePools();
    }

    private void InitializePools()
    {
        if (meleePrefab != null)
            _meleePool = new ObjectPool<EnemyBase>(meleePrefab, enemyContainer, 10);

        if (rangedPrefab != null)
            _rangedPool = new ObjectPool<EnemyBase>(rangedPrefab, enemyContainer, 5);

        if (bossPrefab != null)
            _bossPool = new ObjectPool<EnemyBase>(bossPrefab, enemyContainer, 1, 3);
    }

    /// <summary>Создать врага на основе конфигурации</summary>
    public EnemyBase CreateEnemy(EnemyDataSO data, Vector3 position,
        Quaternion rotation = default)
    {
        if (data == null)
        {
            Debug.LogError("[EnemyFactory] EnemyDataSO == null!");
            return null;
        }

        ObjectPool<EnemyBase> pool = data.EnemyType switch
        {
            EnemyType.Melee => _meleePool,
            EnemyType.Ranged => _rangedPool,
            EnemyType.Boss => _bossPool,
            _ => _meleePool
        };

        if (pool == null)
        {
            Debug.LogError($"[EnemyFactory] Пул для {data.EnemyType} не создан!");
            return null;
        }

        var enemy = pool.Get(position, rotation);

        if (enemy != null)
        {
            enemy.Initialize(data, pool);
            Debug.Log($"👾 Создан враг: {data.EnemyName} в позиции {position}");
        }

        return enemy;
    }

    /// <summary>Вернуть врага в пул</summary>
    public void ReturnEnemy(EnemyBase enemy, EnemyType type)
    {
        ObjectPool<EnemyBase> pool = type switch
        {
            EnemyType.Melee => _meleePool,
            EnemyType.Ranged => _rangedPool,
            EnemyType.Boss => _bossPool,
            _ => _meleePool
        };

        pool?.Return(enemy);
    }
}
```

### 5. UI Toolkit + DOTween для Presentation



```csharp
// Файл: Scripts/Presentation/HUD/HUDController.cs
using System;
using System.Collections;
using DG.Tweening;
using R3;
using UnityEngine;
using UnityEngine.UIElements;

/// <summary>
/// Контроллер HUD.
/// Подписывается на PlayerHealth через R3.
/// Обновляет UI Toolkit элементы.
/// Анимирует через DOTween.
/// </summary>
public class HUDController : MonoBehaviour
{
    [Header("UI")]
    [SerializeField] private UIDocument uiDocument;

    [Header("Ссылки на игровые системы")]
    [SerializeField] private PlayerHealth playerHealth;

    // === Элементы UI Toolkit ===
    private ProgressBar _hpBar;
    private Label _hpLabel;
    private Label _coinLabel;
    private Label _scoreLabel;
    private VisualElement _damageFlash;
    private VisualElement _notificationPanel;
    private Label _notification;

    // === Управление подписками ===
    private readonly CompositeDisposable _disposables = new();
    private Coroutine _notificationCoroutine;

    // === DOTween ===
    private Tweener _hpBarTween;
    private Tweener _flashTween;

    // === Состояние ===
    private float _displayedHP;
    private int _coins;
    private int _score;

    void Awake()
    {
        InitializeUI();
    }

    void OnEnable()
    {
        if (playerHealth != null)
            SubscribeToPlayerHealth();
    }

    void OnDisable()
    {
        _disposables.Clear();
        _hpBarTween?.Kill();
        _flashTween?.Kill();
    }

    void OnDestroy()
    {
        _disposables.Dispose();
    }

    // ==============================
    //   Инициализация
    // ==============================

    private void InitializeUI()
    {
        var root = uiDocument.rootVisualElement;

        _hpBar = root.Q<ProgressBar>("hp-bar");
        _hpLabel = root.Q<Label>("hp-label");
        _coinLabel = root.Q<Label>("coin-label");
        _scoreLabel = root.Q<Label>("score-label");
        _damageFlash = root.Q("damage-flash-overlay");
        _notificationPanel = root.Q("notification-panel");
        _notification = root.Q<Label>("notification-");

        // Начальное состояние
        if (_damageFlash != null)
            _damageFlash.style.opacity = 0;

        if (_notificationPanel != null)
            _notificationPanel.style.display = DisplayStyle.None;
    }

    // ==============================
    //   Подписки на R3
    // ==============================

    private void SubscribeToPlayerHealth()
    {
        // HP изменилось — анимируем бар
        playerHealth.CurrentHP
            .Subscribe(hp => OnHPChanged(hp, playerHealth.MaxHP.Value))
            .AddTo(_disposables);

        // Получен урон — вспышка экрана
        playerHealth.OnDamaged
            .Subscribe(info => OnDamageReceived(info))
            .AddTo(_disposables);

        // Вылечились — зелёная вспышка
        playerHealth.OnHealed
            .Subscribe(info => OnHealReceived(info))
            .AddTo(_disposables);

        // Смерть
        playerHealth.OnDeath
            .Subscribe(_ => OnPlayerDeath())
            .AddTo(_disposables);

        // Критически мало HP — пульсация
        playerHealth.HPPercent
            .Where(pct => pct > 0f && pct <= 0.25f)
            .Subscribe(_ => StartCriticalHPEffect())
            .AddTo(_disposables);

        playerHealth.HPPercent
            .Where(pct => pct > 0.25f)
            .Subscribe(_ => StopCriticalHPEffect())
            .AddTo(_disposables);
    }

    // ==============================
    //   Обработчики событий
    // ==============================

    private void OnHPChanged(float currentHP, float maxHP)
    {
        UpdateHPBar(currentHP, maxHP);
        UpdateHPBarColor(currentHP / maxHP);
    }

    private void OnDamageReceived(DamageInfo info)
    {
        // Красная вспышка экрана
        PlayDamageFlash(Color.red, 0.3f);

        // Показываем урон числом
        if (info.IsCritical)
            ShowNotification($"💥 КРИТ! -{info.Amount:F0}");
    }

    private void OnHealReceived(HealInfo info)
    {
        PlayDamageFlash(new Color(0, 1, 0, 0.3f), 0.2f);
    }

    private void OnPlayerDeath()
    {
        ShowNotification("💀 Вы погибли...");
        PlayDamageFlash(Color.black, 1.5f);
    }

    // ==============================
    //   Обновление UI
    // ==============================

    private void UpdateHPBar(float currentHP, float maxHP)
    {
        if (_hpBar == null) return;

        // Убиваем предыдущий тween
        _hpBarTween?.Kill();

        float startValue = _displayedHP;
        float endValue = currentHP;

        // Анимируем изменение HP через DOTween
        // DOTween работает с float, обновляем UI через callback
        _hpBarTween = DOTween.To(
            getter: () => startValue,
            setter: value =>
            {
                startValue = value;
                _hpBar.value = value;
                _hpBar.highValue = maxHP;

                if (_hpLabel != null)
                    _hpLabel. = $"{(int)value} / {(int)maxHP}";
            },
            endValue: endValue,
            duration: 0.4f
        )
        .SetEase(Ease.OutCubic)
        .SetUpdate(true); // Работает даже при paused timeScale

        _displayedHP = currentHP;
    }

    private void UpdateHPBarColor(float hpPercent)
    {
        if (_hpBar == null) return;

        _hpBar.RemoveFromClassList("hp-bar--high");
        _hpBar.RemoveFromClassList("hp-bar--medium");
        _hpBar.RemoveFromClassList("hp-bar--low");
        _hpBar.RemoveFromClassList("hp-bar--critical");

        string colorClass = hpPercent switch
        {
            > 0.6f => "hp-bar--high",
            > 0.35f => "hp-bar--medium",
            > 0.15f => "hp-bar--low",
            _ => "hp-bar--critical"
        };

        _hpBar.AddToClassList(colorClass);
    }

    // ==============================
    //   Эффекты (DOTween)
    // ==============================

    private void PlayDamageFlash(Color color, float duration)
    {
        if (_damageFlash == null) return;

        _flashTween?.Kill();

        // DOTween анимирует opacity UI Toolkit элемента
        float opacity = 0f;

        _flashTween = DOTween.Sequence()
            .Append(DOTween.To(
                () => opacity,
                value =>
                {
                    opacity = value;
                    _damageFlash.style.opacity = value;
                    _damageFlash.style.backgroundColor = color;
                },
                endValue: 0.6f,
                duration: duration * 0.2f
            ).SetEase(Ease.OutQuad))
            .Append(DOTween.To(
                () => opacity,
                value =>
                {
                    opacity = value;
                    _damageFlash.style.opacity = value;
                },
                endValue: 0f,
                duration: duration * 0.8f
            ).SetEase(Ease.InQuad))
            .SetUpdate(true);
    }

    private Tween _criticalPulseTween;

    private void StartCriticalHPEffect()
    {
        if (_hpBar == null || _criticalPulseTween != null) return;

        float opacity = 1f;
        _criticalPulseTween = DOTween.To(
            () => opacity,
            value =>
            {
                opacity = value;
                _hpBar.style.opacity = value;
            },
            endValue: 0.4f,
            duration: 0.5f
        )
        .SetLoops(-1, LoopType.Yoyo)
        .SetEase(Ease.InOutSine)
        .SetUpdate(true);
    }

    private void StopCriticalHPEffect()
    {
        _criticalPulseTween?.Kill();
        _criticalPulseTween = null;
        if (_hpBar != null) _hpBar.style.opacity = 1f;
    }

    // ==============================
    //   Публичный API
    // ==============================

    public void UpdateCoins(int coins)
    {
        _coins = coins;
        if (_coinLabel != null)
            _coinLabel. = coins.ToString("N0");

        // Мини-анимация при добавлении монет
        AnimateLabel(_coinLabel);
    }

    public void UpdateScore(int score)
    {
        _score = score;
        if (_scoreLabel != null)
            _scoreLabel. = score.ToString("N0");
    }

    public void ShowNotification(string message, float duration = 2.5f)
    {
        if (_notificationCoroutine != null)
            StopCoroutine(_notificationCoroutine);

        _notificationCoroutine = StartCoroutine(
            NotificationCoroutine(message, duration)
        );
    }

    public void Show() => uiDocument.gameObject.SetActive(true);
    public void Hide() => uiDocument.gameObject.SetActive(false);

    // ==============================
    //   Вспомогательные методы
    // ==============================

    private void AnimateLabel(Label label)
    {
        if (label == null) return;

        float scale = 1f;
        DOTween.To(
            () => scale,
            value =>
            {
                scale = value;
                label.style.scale = new StyleScale(new Scale(
                    new Vector2(value, value)
                ));
            },
            endValue: 1.25f,
            duration: 0.1f
        )
        .SetEase(Ease.OutBack)
        .OnComplete(() =>
        {
            DOTween.To(
                () => scale,
                value =>
                {
                    scale = value;
                    label.style.scale = new StyleScale(new Scale(
                        new Vector2(value, value)
                    ));
                },
                endValue: 1f,
                duration: 0.15f
            ).SetEase(Ease.InBack);
        })
        .SetUpdate(true);
    }

    private IEnumerator NotificationCoroutine(string message, float duration)
    {
        if (_notificationPanel == null || _notification == null)
            yield break;

        _notification. = message;
        _notificationPanel.style.display = DisplayStyle.Flex;

        yield return null;
        _notificationPanel.AddToClassList("notification--visible");

        yield return new WaitForSecondsRealtime(duration);

        _notificationPanel.RemoveFromClassList("notification--visible");

        yield return new WaitForSecondsRealtime(0.35f);
        _notificationPanel.style.display = DisplayStyle.None;
    }
}
```

### 6. Cinemachine для Camera Layer



```csharp
// Файл: Scripts/Presentation/Camera/CameraManager.cs
using System.Collections;
using Cinemachine;
using R3;
using UnityEngine;

/// <summary>
/// Менеджер камеры.
/// Управляет Cinemachine Virtual Cameras.
/// Подписывается на игровые события для реакции.
/// </summary>
public class CameraManager : MonoBehaviour
{
    [Header("Виртуальные камеры")]
    [SerializeField] private CinemachineVirtualCamera gameplayCamera;
    [SerializeField] private CinemachineVirtualCamera bossCamera;
    [SerializeField] private CinemachineVirtualCamera deathCamera;
    [SerializeField] private CinemachineVirtualCamera gameOverCamera;

    [Header("Приоритеты")]
    [SerializeField] private int priorityInactive = 0;
    [SerializeField] private int priorityGameplay = 10;
    [SerializeField] private int priorityBoss = 20;
    [SerializeField] private int priorityDeath = 30;

    [Header("Игровые системы")]
    [SerializeField] private PlayerHealth playerHealth;

    // Noise компонент для тряски
    private CinemachineBasicMultiChannelPerlin _gameplayNoise;

    // Подписки
    private readonly CompositeDisposable _disposables = new();
    private Coroutine _shakeCoroutine;

    void Awake()
    {
        InitializeCameras();
    }

    void OnEnable()
    {
        if (playerHealth != null)
            SubscribeToEvents();
    }

    void OnDisable()
    {
        _disposables.Clear();
    }

    void OnDestroy()
    {
        _disposables.Dispose();
    }

    private void InitializeCameras()
    {
        // Устанавливаем начальные приоритеты
        SetAllPrioritiesInactive();
        if (gameplayCamera != null)
            gameplayCamera.Priority = priorityGameplay;

        // Получаем noise компонент
        _gameplayNoise = gameplayCamera?
            .GetCinemachineComponent<CinemachineBasicMultiChannelPerlin>();

        if (_gameplayNoise != null)
            _gameplayNoise.m_AmplitudeGain = 0f;
    }

    private void SubscribeToEvents()
    {
        // Получен урон → тряска камеры
        playerHealth.OnDamaged
            .Subscribe(info => OnDamageShake(info))
            .AddTo(_disposables);

        // Смерть → камера смерти
        playerHealth.OnDeath
            .Subscribe(_ => ActivateDeathCamera())
            .AddTo(_disposables);

        // Критически мало HP → лёгкое постоянное дрожание
        playerHealth.HPPercent
            .Subscribe(pct => UpdateAmbientShake(pct))
            .AddTo(_disposables);
    }

    // ==============================
    //   Camera Shake
    // ==============================

    /// <summary>Тряска камеры при получении урона</summary>
    private void OnDamageShake(DamageInfo info)
    {
        // Сила тряски зависит от урона
        float normalizedDamage = Mathf.Clamp01(info.Amount / 50f);
        float amplitude = Mathf.Lerp(0.5f, 3f, normalizedDamage);
        float duration = Mathf.Lerp(0.15f, 0.5f, normalizedDamage);

        if (info.IsCritical)
        {
            amplitude *= 1.5f;
            duration *= 1.3f;
        }

        ShakeCamera(amplitude, duration);
    }

    /// <summary>Фоновое дрожание при критическом HP</summary>
    private void UpdateAmbientShake(float hpPercent)
    {
        if (_gameplayNoise == null) return;

        // До 15% HP — лёгкое постоянное дрожание
        if (hpPercent <= 0.15f && hpPercent > 0f)
        {
            float intensity = Mathf.InverseLerp(0.15f, 0f, hpPercent);
            _gameplayNoise.m_AmplitudeGain =
                Mathf.Lerp(0f, 0.8f, intensity);
            _gameplayNoise.m_FrequencyGain = 1.5f;
        }
        else if (_shakeCoroutine == null)
        {
            // Сбрасываем ambient shake если нет активной тряски
            _gameplayNoise.m_AmplitudeGain = 0f;
        }
    }

    /// <summary>Запустить тряску с затуханием</summary>
    public void ShakeCamera(float amplitude, float duration, float frequency = 2f)
    {
        if (_shakeCoroutine != null)
            StopCoroutine(_shakeCoroutine);

        _shakeCoroutine = StartCoroutine(
            ShakeCoroutine(amplitude, frequency, duration)
        );
    }

    private IEnumerator ShakeCoroutine(float amplitude, float frequency, float duration)
    {
        if (_gameplayNoise == null) yield break;

        _gameplayNoise.m_AmplitudeGain = amplitude;
        _gameplayNoise.m_FrequencyGain = frequency;

        float elapsed = 0f;
        while (elapsed < duration)
        {
            elapsed += Time.deltaTime;
            float t = elapsed / duration;

            // Плавное затухание по кривой
            float currentAmplitude = amplitude * (1f - Mathf.Pow(t, 2f));
            _gameplayNoise.m_AmplitudeGain = currentAmplitude;

            yield return null;
        }

        _gameplayNoise.m_AmplitudeGain = 0f;
        _shakeCoroutine = null;
    }

    // ==============================
    //   Переключение камер
    // ==============================

    public void ActivateGameplayCamera()
    {
        SetAllPrioritiesInactive();
        if (gameplayCamera != null)
            gameplayCamera.Priority = priorityGameplay;
    }

    public void ActivateBossCamera()
    {
        if (bossCamera != null)
            bossCamera.Priority = priorityBoss;
    }

    public void DeactivateBossCamera()
    {
        if (bossCamera != null)
            bossCamera.Priority = priorityInactive;
    }

    public void ActivateDeathCamera()
    {
        SetAllPrioritiesInactive();
        if (deathCamera != null)
            deathCamera.Priority = priorityDeath;
    }

    public void ActivateGameOverCamera()
    {
        SetAllPrioritiesInactive();
        if (gameOverCamera != null)
            gameOverCamera.Priority = priorityDeath;
    }

    private void SetAllPrioritiesInactive()
    {
        void SetPriority(CinemachineVirtualCamera cam, int priority)
        {
            if (cam != null) cam.Priority = priority;
        }

        SetPriority(gameplayCamera, priorityInactive);
        SetPriority(bossCamera, priorityInactive);
        SetPriority(deathCamera, priorityInactive);
        SetPriority(gameOverCamera, priorityInactive);
    }
}
```

### 7. Service Locator — связываем всё вместе



```csharp
// Файл: Scripts/Infrastructure/DI/ServiceLocator.cs
using System;
using System.Collections.Generic;
using UnityEngine;

/// <summary>
/// Service Locator — простая альтернатива полноценному DI контейнеру.
/// Регистрирует сервисы и предоставляет к ним доступ.
///
/// Для больших проектов рассмотрите VContainer или Zenject.
/// </summary>
public class ServiceLocator
{
    private static ServiceLocator _instance;
    public static ServiceLocator Instance => _instance ??= new ServiceLocator();

    private readonly Dictionary<Type, object> _services = new();

    private ServiceLocator() { }

    /// <summary>Зарегистрировать сервис</summary>
    public void Register<T>(T service) where T : class
    {
        var type = typeof(T);

        if (_services.ContainsKey(type))
        {
            Debug.LogWarning($"[ServiceLocator] Сервис {type.Name} " +
                             $"уже зарегистрирован. Перезаписываю.");
        }

        _services[type] = service;
        Debug.Log($"[ServiceLocator] ✅ Зарегистрирован: {type.Name}");
    }

    /// <summary>Получить сервис (выбросит исключение если не найден)</summary>
    public T Get<T>() where T : class
    {
        var type = typeof(T);

        if (_services.TryGetValue(type, out var service))
            return (T)service;

        throw new InvalidOperationException(
            $"[ServiceLocator] Сервис {type.Name} не зарегистрирован! " +
            $"Убедитесь что Bootstrap.cs выполняется первым."
        );
    }

    /// <summary>Попробовать получить сервис (безопасно)</summary>
    public bool TryGet<T>(out T service) where T : class
    {
        var type = typeof(T);

        if (_services.TryGetValue(type, out var obj))
        {
            service = (T)obj;
            return true;
        }

        service = null;
        return false;
    }

    /// <summary>Отменить регистрацию сервиса</summary>
    public void Unregister<T>() where T : class
    {
        _services.Remove(typeof(T));
    }

    /// <summary>Очистить все сервисы (при смене сцены)</summary>
    public void Clear()
    {
        _services.Clear();
        Debug.Log("[ServiceLocator] Все сервисы очищены");
    }
}
```



```csharp
// Файл: Scripts/Infrastructure/Bootstrap/GameBootstrap.cs
using UnityEngine;

/// <summary>
/// Bootstrap — точка входа в игру.
/// Инициализирует все сервисы в правильном порядке.
/// Должен быть в сцене Bootstrap.unity которая загружается первой.
/// Порядок Script Execution: GameBootstrap должен быть первым.
/// </summary>
public class GameBootstrap : MonoBehaviour
{
    [Header("Ссылки на сервисы")]
    [SerializeField] private PlayerHealth playerHealth;
    [SerializeField] private HUDController hudController;
    [SerializeField] private CameraManager cameraManager;
    [SerializeField] private EnemyFactory enemyFactory;
    [SerializeField] private PoolManager poolManager;

    [Header("Контекст игры")]
    [SerializeField] private GameCon gameCon;

    void Awake()
    {
        // Настраиваем порядок инициализации
        InitializeServices();
        InitializeGameCon();
        InitializeStateMachine();

        Debug.Log("🚀 Bootstrap завершён — игра готова!");
    }

    private void InitializeServices()
    {
        var locator = ServiceLocator.Instance;

        // Регистрируем все сервисы
        locator.Register<PlayerHealth>(playerHealth);
        locator.Register<HUDController>(hudController);
        locator.Register<CameraManager>(cameraManager);
        locator.Register<EnemyFactory>(enemyFactory);
        locator.Register<PoolManager>(poolManager);
    }

    private void InitializeGameCon()
    {
        gameCon.Player = playerHealth.GetComponent<PlayerController>();
        gameCon.HUD = hudController;
        gameCon.CameraManager = cameraManager;
        gameCon.EnemyFactory = enemyFactory;
    }

    private void InitializeStateMachine()
    {
        gameCon.GameStateMachine = new StateMachine();
        gameCon.GameStateMachine.OnStateChanged += (from, to) =>
        {
            Debug.Log($"🎮 Game State: {from?.GetType().Name} → {to.GetType().Name}");
        };

        // Начинаем с gameplay
        gameCon.GameStateMachine.Initialize(new GameplayState(gameCon));
    }
}
```



```csharp
// Файл: Scripts/Infrastructure/Bootstrap/GameCon.cs
using UnityEngine;

/// <summary>
/// Контейнер зависимостей для State Machine.
/// Передаётся в каждое состояние как "контекст игры".
/// </summary>
[System.Serializable]
public class GameCon
{
    // Игровые системы
    public PlayerController Player;
    public HUDController HUD;
    public CameraManager CameraManager;
    public EnemyFactory EnemyFactory;

    // Меню
    public PauseMenuController PauseMenu;
    public GameOverScreenController GameOverScreen;

    // Сохранения
    public ISaveService SaveService;

    // State Machine (устанавливается в Bootstrap)
    [HideInInspector] public StateMachine GameStateMachine;
}
```

---

## Пример потока данных

Рассмотрим полный путь события: **игрок получает урон**.

### Диаграмма потока



```csharp
                    ПОТОК ДАННЫХ: ИГРОК ПОЛУЧАЕТ УРОН
                    ══════════════════════════════════

  [Враг/Ловушка]
       │
       │  enemy.Attack(player)
       ▼
  ┌─────────────────────────────────────────────────────┐
  │              DOMAIN LAYER                           │
  │                                                     │
  │  PlayerHealth.TakeDamage(damageInfo)                │
  │  ├── Вычисляет реальный урон (с учётом защиты)      │
  │  ├── Обновляет _currentHP.Value = 75f               │
  │  └── Генерирует события:                            │
  │      ├── _currentHP.OnNext(75f)         [ReactiveProperty]│
  │      └── _onDamaged.OnNext(damageInfo)  [Subject]   │
  └──────────────────┬──────────────────────────────────┘
                     │
          R3 Observable потоки
                     │
        ┌────────────┼────────────────┐
        │            │                │
        ▼            ▼                ▼
  ┌──────────┐ ┌──────────┐   ┌─────────────┐
  │   HUD    │ │  Camera  │   │   Audio     │
  │Controller│ │ Manager  │   │  Manager    │
  └────┬─────┘ └────┬─────┘   └──────┬──────┘
       │             │                │
       │             │                └── PlaySound(hitClip)
       │             │
       │             └── ShakeCamera(amplitude, duration)
       │                  └── CinemachinePerlin.AmplitudeGain = 2f
       │                      → Затухание за 0.3 сек
       │
       └── OnHPChanged(75, 100)
            │
            ├── [UI Toolkit] UpdateHPBar()
            │    └── DOTween анимирует hp-bar.value
            │        от 100 → 75 за 0.4 сек
            │        SetEase(OutCubic)
            │
            ├── [UI Toolkit] UpdateHPBarColor()
            │    └── AddToClassList("hp-bar--medium")
            │        → USS transition меняет цвет
            │
            └── PlayDamageFlash(Color.red)
                 └── DOTween анимирует opacity overlay
                     0 → 0.6 → 0 за 0.3 сек


  ПАРАЛЛЕЛЬНО (если HP < 25%):
  ─────────────────────────────
  HPPercent.Where(p => p <= 0.25f)
       │
       ├── HUDController → StartCriticalHPEffect()
       │    └── DOTween пульсация hp-bar opacity
       │
       └── CameraManager → UpdateAmbientShake(0.2f)
            └── CinemachinePerlin.AmplitudeGain = 0.4f
                (постоянное дрожание)
```

### Реализация полного потока



```csharp
// Файл: Scripts/Infrastructure/Bootstrap/GameSystemsConnector.cs
using R3;
using UnityEngine;

/// <summary>
/// Соединяет все игровые системы через R3 подписки.
/// Запускается в Bootstrap после инициализации всех сервисов.
///
/// Это единственное место где системы "знают" друг о друге.
/// PlayerHealth НЕ знает о HUDController.
/// HUDController НЕ знает о CameraManager.
/// Только этот класс знает обо всех и соединяет их.
/// </summary>
public class GameSystemsConnector : MonoBehaviour
{
    [Header("Сервисы")]
    [SerializeField] private PlayerHealth playerHealth;
    [SerializeField] private HUDController hudController;
    [SerializeField] private CameraManager cameraManager;
    [SerializeField] private AudioManager audioManager;

    private readonly CompositeDisposable _disposables = new();

    void OnEnable()
    {
        ConnectSystems();
    }

    void OnDisable()
    {
        _disposables.Clear();
    }

    void OnDestroy()
    {
        _disposables.Dispose();
    }

    private void ConnectSystems()
    {
        ConnectPlayerHealthToHUD();
        ConnectPlayerHealthToCamera();
        ConnectPlayerHealthToAudio();

        Debug.Log("🔗 Все системы соединены");
    }

    private void ConnectPlayerHealthToHUD()
    {
        if (playerHealth == null || hudController == null) return;

        // HP → HUD бар (с анимацией через DOTween внутри HUDController)
        playerHealth.CurrentHP
            .CombineLatest(playerHealth.MaxHP, (hp, max) => (hp, max))
            .Subscribe(tuple =>
                hudController.SetHP(tuple.hp, tuple.max))
            .AddTo(_disposables);

        // Урон → красная вспышка
        playerHealth.OnDamaged
            .Subscribe(info => hudController.ShowDamageFlash(info.IsCritical))
            .AddTo(_disposables);

        // Лечение → зелёная вспышка
        playerHealth.OnHealed
            .Subscribe(_ => hudController.ShowHealFlash())
            .AddTo(_disposables);

        // Смерть → game over экран
        playerHealth.OnDeath
            .Subscribe(_ => hudController.ShowDeathScreen())
            .AddTo(_disposables);

        // Критическое HP → уведомление (только один раз при переходе)
        playerHealth.HPPercent
            .Select(pct => pct <= 0.25f && pct > 0f)
            .DistinctUntilChanged()
            .Where(isCritical => isCritical)
            .Subscribe(_ => hudController.ShowNotification("⚠ Критическое здоровье!"))
            .AddTo(_disposables);
    }

    private void ConnectPlayerHealthToCamera()
    {
        if (playerHealth == null || cameraManager == null) return;

        // Урон → тряска камеры
        playerHealth.OnDamaged
            .Subscribe(info =>
            {
                float intensity = Mathf.Clamp01(info.Amount / 30f);
                float amplitude = Mathf.Lerp(0.8f, 3.5f, intensity);
                float duration = Mathf.Lerp(0.2f, 0.6f, intensity);

                cameraManager.ShakeCamera(amplitude, duration);
            })
            .AddTo(_disposables);

        // Смерть → камера смерти
        playerHealth.OnDeath
            .Subscribe(_ => cameraManager.ActivateDeathCamera())
            .AddTo(_disposables);

        // Критическое HP → ambient shake
        playerHealth.HPPercent
            .Subscribe(pct => cameraManager.SetAmbientShake(pct))
            .AddTo(_disposables);
    }

    private void ConnectPlayerHealthToAudio()
    {
        if (playerHealth == null || audioManager == null) return;

        // Урон → звук удара
        playerHealth.OnDamaged
            .Subscribe(info =>
            {
                if (info.IsCritical)
                    audioManager.PlaySFX("hit_critical");
                else
                    audioManager.PlaySFX("hit_normal");
            })
            .AddTo(_disposables);

        // Лечение → звук лечения
        playerHealth.OnHealed
            .Subscribe(_ => audioManager.PlaySFX("heal"))
            .AddTo(_disposables);

        // Смерть → смерть
        playerHealth.OnDeath
            .Subscribe(_ => audioManager.PlaySFX("player_death"))
            .AddTo(_disposables);

        // Критическое HP → тревожная музыка
        playerHealth.HPPercent
            .Select(pct => pct <= 0.25f && pct > 0f)
            .DistinctUntilChanged()
            .Subscribe(isCritical => audioManager.SetCriticalMode(isCritical))
            .AddTo(_disposables);
    }
}
```

### Тест потока — симуляция урона



```csharp
// Файл: Scripts/Debug/DamageFlowTester.cs
#if UNITY_EDITOR
using UnityEngine;

/// <summary>
/// Тестирует полный поток данных при уроне.
/// Только для разработки.
/// </summary>
public class DamageFlowTester : MonoBehaviour
{
    [SerializeField] private PlayerHealth playerHealth;

    [Header("Параметры теста")]
    [SerializeField] private float testDamage = 20f;
    [SerializeField] private float testHeal = 15f;
    [SerializeField] private bool isCritical = false;

    void Update()
    {
        // Числа для быстрого тестирования
        if (Input.GetKeyDown(KeyCode.Alpha1))
            SimulateDamage(testDamage, false);

        if (Input.GetKeyDown(KeyCode.Alpha2))
            SimulateDamage(testDamage * 2, true); // Критический

        if (Input.GetKeyDown(KeyCode.Alpha3))
            SimulateHeal(testHeal);

        if (Input.GetKeyDown(KeyCode.Alpha4))
            SimulateDeath();

        if (Input.GetKeyDown(KeyCode.Alpha5))
            SimulateRevive();
    }

    private void SimulateDamage(float amount, bool crit)
    {
        var info = new DamageInfo(
            amount: amount,
            rawAmount: amount,
            damageType: DamageType.Physical,
            source: gameObject,
            isCritical: crit
        );
        playerHealth?.TakeDamage(info);
        Debug.Log($"[TEST] 💥 Урон: {amount} (крит: {crit})");
    }

    private void SimulateHeal(float amount)
    {
        playerHealth?.Heal(amount);
        Debug.Log($"[TEST] 💚 Лечение: {amount}");
    }

    private void SimulateDeath()
    {
        var info = new DamageInfo(9999f, 9999f, DamageType.True, gameObject, false);
        playerHealth?.TakeDamage(info);
        Debug.Log("[TEST] 💀 Смерть");
    }

    private void SimulateRevive()
    {
        playerHealth?.Revive(0.5f);
        Debug.Log("[TEST] ✨ Возрождение");
    }

    void OnGUI()
    {
        GUILayout.BeginArea(new Rect(10, Screen.height - 120, 250, 110));
        GUILayout.Label("=== DAMAGE FLOW TESTER ===");
        GUILayout.Label("[1] Урон  [2] Крит  [3] Лечение");
        GUILayout.Label("[4] Смерть  [5] Возрождение");

        if (playerHealth != null)
        {
            GUILayout.Label($"HP: {playerHealth.CurrentHP.Value:F0}" +
                            $" / {playerHealth.MaxHP.Value:F0}");
            GUILayout.Label($"% : {playerHealth.HPPercent.Value:P0}");
        }

        GUILayout.EndArea();
    }
}
#endif
```

---

## Чек-лист

### 10 пунктов готовности проекта к разработке



```csharp
╔══════════════════════════════════════════════════════════════╗
║        ЧЕК-ЛИСТ АРХИТЕКТУРЫ UNITY ПРОЕКТА                   ║
║        Проверяйте перед началом активной разработки          ║
╚══════════════════════════════════════════════════════════════╝

□ 1. СТРУКТУРА ПАПОК
     ├── Создана папка _Project/ как корень всего кода
     ├── Разделены Scripts/Domain, Scripts/Presentation,
     │   Scripts/Infrastructure, Scripts/Data, Scripts/Shared
     ├── UI ресурсы в отдельной папке UI/Documents и UI/Styles
     └── Data ассеты в Data/ с разбивкой по типам

□ 2. СЛОИ АРХИТЕКТУРЫ ОПРЕДЕЛЕНЫ
     ├── Написан документ (даже в 10 строк): что в каком слое
     ├── Domain слой не имеет using UnityEngine.UIElements
     ├── Data слой не содержит игровой логики (только данные)
     └── Presentation не содержит бизнес-правил

□ 3. SCRIPTABLEOBJECT КОНФИГУРАЦИИ
     ├── Базовые CharacterStatsSO созданы для Player и Enemy
     ├── Все "магические числа" вынесены в SO ассеты
     ├── [CreateAssetMenu] настроен для удобного создания
     └── Дизайнер может менять баланс без открытия кода

□ 4. R3 (REACTIVE EXTENSIONS) НАСТРОЕН
     ├── Пакет R3 установлен и компилируется
     ├── CompositeDisposable используется во всех MonoBehaviour
     ├── Dispose вызывается в OnDestroy
     └── Нет подписок без соответствующей отписки

□ 5. STATE MACHINE ОПРЕДЕЛЕНА
     ├── Перечислены все состояния игры (Gameplay, Pause, etc.)
     ├── Написан базовый IState интерфейс
     ├── StateMachine класс создан и протестирован
     └── GameCon содержит все зависимости для состояний

□ 6. OBJECT POOL НАСТРОЕН
     ├── ObjectPool<T> реализован с IPoolable интерфейсом
     ├── Определены объекты которые будут пулиться (пули, враги)
     ├── PoolManager зарегистрирован в ServiceLocator
     └── Тест: нет Instantiate/Destroy в горячих путях кода

□ 7. UI TOOLKIT ПОДКЛЮЧЁН
     ├── Panel Settings ассет создан (Scale With Screen Size)
     ├── Базовый Variables.uss с цветами и размерами написан
     ├── HUD.uxml создан с правильными name атрибутами
     └── HUDController кэширует все ссылки на элементы в Awake

□ 8. CINEMACHINE НАСТРОЕН
     ├── CinemachineBrain на Main Camera
     ├── Минимум 2 Virtual Camera (gameplay + death/boss)
     ├── Default Blend настроен (EaseInOut, 1-2 сек)
     └── CameraManager зарегистрирован в ServiceLocator

□ 9. BOOTSTRAP СЦЕНА СОЗДАНА
     ├── Bootstrap.unity загружается первой (Build Settings)
     ├── GameBootstrap.cs инициализирует все сервисы
     ├── ServiceLocator регистрирует все зависимости
     └── GameSystemsConnector соединяет системы через R3

□ 10. ТЕСТОВАЯ СЦЕНА ГОТОВА
      ├── _Sandbox.unity создана для быстрых экспериментов
      ├── DamageFlowTester позволяет симулировать урон/лечение
      ├── #if UNITY_EDITOR обёртки на всём отладочном коде
      └── Полный поток "урон → HUD → камера" протестирован вручную

══════════════════════════════════════════════════════════════
  РЕЗУЛЬТАТ:  ___/10 пунктов выполнено

  0-3:  🔴 Стоп. Исправьте архитектуру до написания игрового кода
  4-6:  🟡 Можно начать, но технический долг накапливается быстро
  7-9:  🟢 Хорошая база. Следите за соблюдением правил слоёв
  10:   ✅ Проект готов к масштабной разработке
══════════════════════════════════════════════════════════════
```

### Антипаттерны — что НЕ делать



```csharp
// ❌ АНТИПАТТЕРН 1: God Object
public class GameManager : MonoBehaviour
{
    // 50 полей, 30 методов, знает обо всём
    public PlayerHealth playerHealth;
    public UIManager uiManager;
    public EnemySpawner spawner;
    public AudioManager audio;
    public SaveSystem save;
    // ... ещё 45 полей
}

// ❌ АНТИПАТТЕРН 2: Domain знает о Presentation
public class PlayerHealth : MonoBehaviour
{
    [SerializeField] private ProgressBar hpBar; // ← НЕЛЬЗЯ!

    public void TakeDamage(float damage)
    {
        _hp -= damage;
        hpBar.value = _hp; // ← Domain трогает UI — ЗАПРЕЩЕНО
    }
}

// ❌ АНТИПАТТЕРН 3: Строковые зависимости
void Update()
{
    // Опечатка компилятором не поймается
    GameObject.Find("PlayerHealthSystem")
        .GetComponent<PlayerHealth>()
        .TakeDamage(10f);
}

// ❌ АНТИПАТТЕРН 4: Утечка подписок
public class SomeController : MonoBehaviour
{
    void OnEnable()
    {
        playerHealth.OnDamaged  // Подписались...
            .Subscribe(OnDamage);
        // ...но нигде не отписались!
        // Объект уничтожен — подписка живёт
    }
}

// ✅ ПРАВИЛЬНО:
public class SomeController : MonoBehaviour
{
    private readonly CompositeDisposable _d = new();

    void OnEnable()
    {
        playerHealth.OnDamaged
            .Subscribe(OnDamage)
            .AddTo(_d); // Автоматическая отписка
    }

    void OnDisable() => _d.Clear();
    void OnDestroy() => _d.Dispose();
}
```

---

> **Итог:** Архитектура — это не про то чтобы написать "правильный" код. Это про то чтобы через полгода вы могли добавить нового босса, не сломав магазин. Добавить новый эффект урона, не переписывая камеру. Нанять второго разработчика, который разберётся в проекте за день, а не за неделю. Начните с чек-листа из 10 пунктов — и каждая следующая строчка кода будет ложиться на правильный фундамент