## Содержание

- [1. Введение — проблема сильной связности {#введение}](#1.%20%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%E2%80%94%20%D0%BF%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0%20%D1%81%D0%B8%D0%BB%D1%8C%D0%BD%D0%BE%D0%B9%20%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%7B#%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%7D)
	- [😱 Как это выглядит без паттерна](#%F0%9F%98%B1%20%D0%9A%D0%B0%D0%BA%20%D1%8D%D1%82%D0%BE%20%D0%B2%D1%8B%D0%B3%D0%BB%D1%8F%D0%B4%D0%B8%D1%82%20%D0%B1%D0%B5%D0%B7%20%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%D0%B0)
	- [Что здесь не так?](#%D0%A7%D1%82%D0%BE%20%D0%B7%D0%B4%D0%B5%D1%81%D1%8C%20%D0%BD%D0%B5%20%D1%82%D0%B0%D0%BA?)
	- [✅ Как должно быть](#%E2%9C%85%20%D0%9A%D0%B0%D0%BA%20%D0%B4%D0%BE%D0%BB%D0%B6%D0%BD%D0%BE%20%D0%B1%D1%8B%D1%82%D1%8C)
- [2. Теория паттерна {#теория}](#2.%20%D0%A2%D0%B5%D0%BE%D1%80%D0%B8%D1%8F%20%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%D0%B0%20%7B#%D1%82%D0%B5%D0%BE%D1%80%D0%B8%D1%8F%7D)
	- [Определение](#%D0%9E%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)
	- [Участники паттерна](#%D0%A3%D1%87%D0%B0%D1%81%D1%82%D0%BD%D0%B8%D0%BA%D0%B8%20%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%D0%B0)
	- [Ключевые роли](#%D0%9A%D0%BB%D1%8E%D1%87%D0%B5%D0%B2%D1%8B%D0%B5%20%D1%80%D0%BE%D0%BB%D0%B8)
	- [Схема взаимодействия (словами)](#%D0%A1%D1%85%D0%B5%D0%BC%D0%B0%20%D0%B2%D0%B7%D0%B0%D0%B8%D0%BC%D0%BE%D0%B4%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%B8%D1%8F%20(%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D0%BC%D0%B8))
- [3. Реализация через C# Events и Delegates {#-events}](#3.%20%D0%A0%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20C#%20Events%20%D0%B8%20Delegates%20%7B#-events%7D)
	- [Базовые понятия](#%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B5%20%D0%BF%D0%BE%D0%BD%D1%8F%D1%82%D0%B8%D1%8F)
	- [Реализация PlayerHealth с событиями](#%D0%A0%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20PlayerHealth%20%D1%81%20%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F%D0%BC%D0%B8)
	- [Подписчик: HealthBarUI](#%D0%9F%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D1%87%D0%B8%D0%BA:%20HealthBarUI)
	- [Подписчик: AchievementSystem](#%D0%9F%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D1%87%D0%B8%D0%BA:%20AchievementSystem)
	- [Подписчик: SoundManager](#%D0%9F%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D1%87%D0%B8%D0%BA:%20SoundManager)
	- [Визуализация результата](#%D0%92%D0%B8%D0%B7%D1%83%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D0%B0)
	- [⚠️ Типичные ошибки с C# Events](#%E2%9A%A0%EF%B8%8F%20%D0%A2%D0%B8%D0%BF%D0%B8%D1%87%D0%BD%D1%8B%D0%B5%20%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D0%B8%20%D1%81%20C#%20Events)
- [4. Реализация через ScriptableObject Events {#scriptableobject-events}](#4.%20%D0%A0%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20ScriptableObject%20Events%20%7B#scriptableobject-events%7D)
	- [В чём преимущество?](#%D0%92%20%D1%87%D1%91%D0%BC%20%D0%BF%D1%80%D0%B5%D0%B8%D0%BC%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%BE?)
	- [Шаг 1: Базовый GameEvent ScriptableObject](#%D0%A8%D0%B0%D0%B3%201:%20%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B9%20GameEvent%20ScriptableObject)
	- [Шаг 2: Универсальное событие с параметром](#%D0%A8%D0%B0%D0%B3%202:%20%D0%A3%D0%BD%D0%B8%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5%20%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B5%20%D1%81%20%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D0%BE%D0%BC)
	- [Шаг 3: Компонент-слушатель для GameEvent](#%D0%A8%D0%B0%D0%B3%203:%20%D0%9A%D0%BE%D0%BC%D0%BF%D0%BE%D0%BD%D0%B5%D0%BD%D1%82-%D1%81%D0%BB%D1%83%D1%88%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%20%D0%B4%D0%BB%D1%8F%20GameEvent)
	- [Шаг 4: PlayerHealth с ScriptableObject Events](#%D0%A8%D0%B0%D0%B3%204:%20PlayerHealth%20%D1%81%20ScriptableObject%20Events)
	- [Шаг 5: Подписчики для ScriptableObject Events](#%D0%A8%D0%B0%D0%B3%205:%20%D0%9F%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D1%87%D0%B8%D0%BA%D0%B8%20%D0%B4%D0%BB%D1%8F%20ScriptableObject%20Events)
	- [Структура проекта с SO Events](#%D0%A1%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0%20%D1%81%20SO%20Events)
	- [Преимущество: тестирование в редакторе](#%D0%9F%D1%80%D0%B5%D0%B8%D0%BC%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%BE:%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%B2%20%D1%80%D0%B5%D0%B4%D0%B0%D0%BA%D1%82%D0%BE%D1%80%D0%B5)
- [5. Реализация через R3 {#r3}](#5.%20%D0%A0%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20R3%20%7B#r3%7D)
	- [Концепция реактивного программирования](#%D0%9A%D0%BE%D0%BD%D1%86%D0%B5%D0%BF%D1%86%D0%B8%D1%8F%20%D1%80%D0%B5%D0%B0%D0%BA%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F)
	- [Основные типы R3](#%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5%20%D1%82%D0%B8%D0%BF%D1%8B%20R3)
	- [Реализация PlayerHealth с R3](#%D0%A0%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20PlayerHealth%20%D1%81%20R3)
	- [Подписчики с R3](#%D0%9F%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D1%87%D0%B8%D0%BA%D0%B8%20%D1%81%20R3)
	- [Мощь операторов R3](#%D0%9C%D0%BE%D1%89%D1%8C%20%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BE%D0%B2%20R3)
	- [AddTo — магия автоотписки в Unity](#AddTo%20%E2%80%94%20%D0%BC%D0%B0%D0%B3%D0%B8%D1%8F%20%D0%B0%D0%B2%D1%82%D0%BE%D0%BE%D1%82%D0%BF%D0%B8%D1%81%D0%BA%D0%B8%20%D0%B2%20Unity)
- [6. Сравнение трёх подходов {#сравнение}](#6.%20%D0%A1%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%82%D1%80%D1%91%D1%85%20%D0%BF%D0%BE%D0%B4%D1%85%D0%BE%D0%B4%D0%BE%D0%B2%20%7B#%D1%81%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%7D)
	- [Таблица сравнения](#%D0%A2%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0%20%D1%81%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F)
	- [Плюсы и минусы](#%D0%9F%D0%BB%D1%8E%D1%81%D1%8B%20%D0%B8%20%D0%BC%D0%B8%D0%BD%D1%83%D1%81%D1%8B)
	- [Когда что выбирать?](#%D0%9A%D0%BE%D0%B3%D0%B4%D0%B0%20%D1%87%D1%82%D0%BE%20%D0%B2%D1%8B%D0%B1%D0%B8%D1%80%D0%B0%D1%82%D1%8C?)
- [7. Практическое задание {#практика}](#7.%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%7B#%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0%7D)
	- [Задание: Система очков](#%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5:%20%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D0%BE%D1%87%D0%BA%D0%BE%D0%B2)
	- [ScoreManager](#ScoreManager)
	- [ScoreUI — отображение очков](#ScoreUI%20%E2%80%94%20%D0%BE%D1%82%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BE%D1%87%D0%BA%D0%BE%D0%B2)
	- [AchievementSystem — система достижений](#AchievementSystem%20%E2%80%94%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D0%B4%D0%BE%D1%81%D1%82%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9)
	- [Тестирование системы](#%D0%A2%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B)
	- [Граф зависимостей системы](#%D0%93%D1%80%D0%B0%D1%84%20%D0%B7%D0%B0%D0%B2%D0%B8%D1%81%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D0%B5%D0%B9%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B)
	- [Расширение без изменения ScoreManager](#%D0%A0%D0%B0%D1%81%D1%88%D0%B8%D1%80%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B1%D0%B5%D0%B7%20%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F%20ScoreManager)
- [✅ Проверь себя {#проверь-себя}](#%E2%9C%85%20%D0%9F%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D1%8C%20%D1%81%D0%B5%D0%B1%D1%8F%20%7B#%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D1%8C-%D1%81%D0%B5%D0%B1%D1%8F%7D)
	- [Теоретические вопросы](#%D0%A2%D0%B5%D0%BE%D1%80%D0%B5%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%B2%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D1%8B)
	- [Практические задания](#%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F)
	- [Чек-лист хорошей реализации Observer](#%D0%A7%D0%B5%D0%BA-%D0%BB%D0%B8%D1%81%D1%82%20%D1%85%D0%BE%D1%80%D0%BE%D1%88%D0%B5%D0%B9%20%D1%80%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8%20Observer)
	- [Краткое резюме](#%D0%9A%D1%80%D0%B0%D1%82%D0%BA%D0%BE%D0%B5%20%D1%80%D0%B5%D0%B7%D1%8E%D0%BC%D0%B5)

---

## 1. Введение — проблема сильной связности {#введение}

Представь типичную сцену в Unity-проекте. У тебя есть `PlayerHealth`, и когда здоровье игрока меняется, нужно обновить:

- UI-полоску здоровья
- Систему достижений
- Звуковой менеджер
- Эффекты частиц
- Систему сохранений

### 😱 Как это выглядит без паттерна



```csharp
// ❌ Плохо — PlayerHealth знает о ВСЕХ системах
public class PlayerHealth : MonoBehaviour
{
    [SerializeField] private HealthBar healthBar;
    [SerializeField] private AchievementSystem achievements;
    [SerializeField] private SoundManager soundManager;
    [SerializeField] private ParticleSystem damageEffect;
    [SerializeField] private SaveSystem saveSystem;

    private int _currentHealth = 100;

    public void TakeDamage(int damage)
    {
        _currentHealth -= damage;

        // Вынужден вручную вызывать каждую систему
        healthBar.UpdateHealthBar(_currentHealth);
        achievements.CheckHealthAchievements(_currentHealth);
        soundManager.PlayDamageSound();
        damageEffect.Play();
        saveSystem.SaveCurrentHealth(_currentHealth);

        // А если добавится новая система? Снова лезем сюда!
    }
}
```

### Что здесь не так?

|Проблема|Описание|
|---|---|
|**Жёсткая связность**|`PlayerHealth` напрямую зависит от 5+ классов|
|**Нарушение SRP**|Один класс отвечает за здоровье И за оповещение всех систем|
|**Хрупкость**|Удаление любого компонента из инспектора = NullReferenceException|
|**Масштабируемость**|Добавление новой системы требует изменения `PlayerHealth`|
|**Тестируемость**|Невозможно тестировать `PlayerHealth` изолированно|

### ✅ Как должно быть

`PlayerHealth` не должен знать _ничего_ о тех, кто хочет узнать об изменении здоровья. Он просто **публикует событие**, а подписчики сами решают, что делать. Это и есть суть паттерна **Observer**.

---

## 2. Теория паттерна {#теория}

### Определение

> **Observer** (Наблюдатель) — поведенческий паттерн проектирования, который создаёт механизм подписки, позволяющий одним объектам следить и реагировать на события, происходящие в других объектах.

### Участники паттерна



```csharp
┌─────────────────────────────────────────────────────────┐
│                       SUBJECT                           │
│              (Издатель / Observable)                    │
│                                                         │
│  - Хранит список подписчиков                           │
│  - Предоставляет Subscribe() и Unsubscribe()           │
│  - Вызывает Notify() при изменении состояния           │
└───────────────────────┬─────────────────────────────────┘
                        │  уведомляет
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
   ┌──────────┐  ┌──────────┐  ┌──────────┐
   │OBSERVER 1│  │OBSERVER 2│  │OBSERVER 3│
   │  (UI)    │  │(Звук)    │  │(Ачивки)  │
   │          │  │          │  │          │
   │ Update() │  │ Update() │  │ Update() │
   └──────────┘  └──────────┘  └──────────┘
```

### Ключевые роли

**Subject (Субъект / Издатель)**

- Хранит актуальное состояние
- Ведёт список подписчиков
- Уведомляет подписчиков при изменении

**Observer (Наблюдатель / Подписчик)**

- Реализует интерфейс обновления
- Подписывается на Subject
- Реагирует на уведомления

### Схема взаимодействия (словами)



```csharp
1. Observer регистрирует себя в Subject через Subscribe()
2. Subject меняет своё состояние (например, health = 50)
3. Subject вызывает Notify() и проходит по списку Observer'ов
4. Каждый Observer получает вызов Update(newValue)
5. Observer самостоятельно решает, что делать с данными
6. При уничтожении Observer отписывается через Unsubscribe()
```

---

## 3. Реализация через C# Events и Delegates {#-events}

Это самый нативный способ реализации Observer в C#. Встроен в язык, не требует сторонних библиотек.

### Базовые понятия



```csharp
// Delegate — это тип, описывающий сигнатуру метода
public delegate void HealthChangedDelegate(int newHealth, int maxHealth);

// Action<T> — готовый делегат из System, принимает параметры, не возвращает значение
// Action<int, int> эквивалентен нашему HealthChangedDelegate

// event — ключевое слово, ограничивающее делегат:
// - только Subscribe (+=) и Unsubscribe (-=) снаружи класса
// - только класс-владелец может вызвать (invoke) событие
```

### Реализация PlayerHealth с событиями



```csharp
using System;
using UnityEngine;

public class PlayerHealth : MonoBehaviour
{
    // Объявление события с передачей текущего и максимального здоровья
    public event Action<int, int> OnHealthChanged;
    
    // Событие без параметров — просто факт смерти
    public event Action OnPlayerDied;

    [SerializeField] private int maxHealth = 100;
    private int _currentHealth;

    public int CurrentHealth => _currentHealth;
    public int MaxHealth => maxHealth;

    private void Awake()
    {
        _currentHealth = maxHealth;
    }

    public void TakeDamage(int damage)
    {
        if (_currentHealth <= 0) return;

        _currentHealth = Mathf.Max(0, _currentHealth - damage);
        
        // Уведомляем ВСЕХ подписчиков одной строкой
        // Оператор ?. защищает от вызова, если подписчиков нет (null)
        OnHealthChanged?.Invoke(_currentHealth, maxHealth);

        if (_currentHealth <= 0)
        {
            OnPlayerDied?.Invoke();
        }
    }

    public void Heal(int amount)
    {
        _currentHealth = Mathf.Min(maxHealth, _currentHealth + amount);
        OnHealthChanged?.Invoke(_currentHealth, maxHealth);
    }
}
```

### Подписчик: HealthBarUI



```csharp
using UnityEngine;
using UnityEngine.UI;

public class HealthBarUI : MonoBehaviour
{
    [SerializeField] private Slider healthSlider;
    [SerializeField] private PlayerHealth playerHealth;

    private void OnEnable()
    {
        // Подписываемся при включении объекта
        playerHealth.OnHealthChanged += HandleHealthChanged;
    }

    private void OnDisable()
    {
        // ⚠️ ВАЖНО: всегда отписывайся, чтобы избежать утечек памяти
        playerHealth.OnHealthChanged -= HandleHealthChanged;
    }

    private void HandleHealthChanged(int current, int max)
    {
        // Просто обновляем UI — никакой логики PlayerHealth здесь нет
        healthSlider.value = (float)current / max;
    }
}
```

### Подписчик: AchievementSystem



```csharp
using UnityEngine;

public class AchievementSystem : MonoBehaviour
{
    [SerializeField] private PlayerHealth playerHealth;

    private void OnEnable()
    {
        playerHealth.OnHealthChanged += CheckHealthAchievements;
        playerHealth.OnPlayerDied    += UnlockDeathAchievement;
    }

    private void OnDisable()
    {
        playerHealth.OnHealthChanged -= CheckHealthAchievements;
        playerHealth.OnPlayerDied    -= UnlockDeathAchievement;
    }

    private void CheckHealthAchievements(int current, int max)
    {
        float percent = (float)current / max;
        
        if (percent <= 0.1f)
        {
            Debug.Log("🏆 Достижение: На волосок от смерти!");
        }
    }

    private void UnlockDeathAchievement()
    {
        Debug.Log("💀 Достижение: Первая смерть");
    }
}
```

### Подписчик: SoundManager



```csharp
using UnityEngine;

public class SoundManager : MonoBehaviour
{
    [SerializeField] private PlayerHealth playerHealth;
    [SerializeField] private AudioClip damageSound;
    [SerializeField] private AudioClip deathSound;
    
    private AudioSource _audioSource;
    private int _previousHealth;

    private void Awake()
    {
        _audioSource = GetComponent<AudioSource>();
    }

    private void OnEnable()
    {
        _previousHealth = playerHealth.CurrentHealth;
        playerHealth.OnHealthChanged += HandleHealthChanged;
        playerHealth.OnPlayerDied    += HandlePlayerDied;
    }

    private void OnDisable()
    {
        playerHealth.OnHealthChanged -= HandleHealthChanged;
        playerHealth.OnPlayerDied    -= HandlePlayerDied;
    }

    private void HandleHealthChanged(int current, int max)
    {
        if (current < _previousHealth)
        {
            _audioSource.PlayOneShot(damageSound);
        }
        _previousHealth = current;
    }

    private void HandlePlayerDied()
    {
        _audioSource.PlayOneShot(deathSound);
    }
}
```

### Визуализация результата



```csharp
PlayerHealth                    Подписчики
    │
    │  OnHealthChanged?.Invoke(50, 100)
    │─────────────────────────────────► HealthBarUI.HandleHealthChanged(50, 100)
    │                                        → slider.value = 0.5f
    │─────────────────────────────────► AchievementSystem.CheckHealthAchievements(50, 100)
    │                                        → проверка условий
    │─────────────────────────────────► SoundManager.HandleHealthChanged(50, 100)
    │                                        → воспроизведение звука
    │
    │  PlayerHealth НИЧЕГО не знает об этих классах!
```

### ⚠️ Типичные ошибки с C# Events



```csharp
// ❌ Ошибка 1: Забыть отписаться
private void OnEnable()
{
    target.OnHealthChanged += HandleHealthChanged;
    // Если объект уничтожен, но не отписан — утечка памяти и ошибки!
}

// ❌ Ошибка 2: Подписываться в Start вместо OnEnable/OnDisable
// Если объект отключится и включится — подписка задублируется!

// ❌ Ошибка 3: Вызвать событие снаружи класса
// playerHealth.OnHealthChanged(50, 100); // Ошибка компиляции!
// playerHealth.OnHealthChanged = null;   // Тоже ошибка!
// Только += и -= доступны снаружи благодаря ключевому слову event

// ✅ Правильный паттерн: OnEnable/OnDisable для подписки
private void OnEnable()  => target.OnSomeEvent += HandleEvent;
private void OnDisable() => target.OnSomeEvent -= HandleEvent;
```

---

## 4. Реализация через ScriptableObject Events {#scriptableobject-events}

Этот подход популяризировал Ryan Hipple на GDC 2017. Идея: **событие — это ассет**, который живёт независимо от сцены.

### В чём преимущество?



```csharp
C# Events:                    ScriptableObject Events:
PlayerHealth ──► HealthBarUI  GameEvent(Asset) ──► HealthBarUI
                              ▲
                  PlayerHealth──┘
                  
Зависимость между конкретными объектами   Зависимость только от ассета
```

### Шаг 1: Базовый GameEvent ScriptableObject



```csharp
using System.Collections.Generic;
using UnityEngine;

// Событие без параметров
[CreateAssetMenu(menuName = "Events/Game Event")]
public class GameEvent : ScriptableObject
{
    // Список всех подписчиков
    private readonly List<GameEventListener> _listeners = new();

    // Вызов события — уведомить всех слушателей
    public void Raise()
    {
        // Идём с конца, чтобы безопасно обрабатывать отписку во время итерации
        for (int i = _listeners.Count - 1; i >= 0; i--)
        {
            _listeners[i].OnEventRaised();
        }
    }

    public void RegisterListener(GameEventListener listener)
    {
        if (!_listeners.Contains(listener))
            _listeners.Add(listener);
    }

    public void UnregisterListener(GameEventListener listener)
    {
        _listeners.Remove(listener);
    }
}
```

### Шаг 2: Универсальное событие с параметром



```csharp
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;

// Базовый класс для типизированных событий
public abstract class GameEvent<T> : ScriptableObject
{
    private readonly List<System.Action<T>> _listeners = new();

    public void Raise(T value)
    {
        for (int i = _listeners.Count - 1; i >= 0; i--)
        {
            _listeners[i]?.Invoke(value);
        }
    }

    public void Subscribe(System.Action<T> listener)
    {
        if (!_listeners.Contains(listener))
            _listeners.Add(listener);
    }

    public void Unsubscribe(System.Action<T> listener)
    {
        _listeners.Remove(listener);
    }
}

// Конкретное событие для здоровья
[CreateAssetMenu(menuName = "Events/Health Event")]
public class HealthEvent : GameEvent<(int current, int max)> { }

// Конкретное событие для очков
[CreateAssetMenu(menuName = "Events/Score Event")]  
public class ScoreEvent : GameEvent<int> { }

// Конкретное событие для строк (например, сообщений)
[CreateAssetMenu(menuName = "Events/String Event")]
public class StringEvent : GameEvent<string> { }
```

### Шаг 3: Компонент-слушатель для GameEvent



```csharp
using UnityEngine;
using UnityEngine.Events;

// Компонент, который прослушивает GameEvent и вызывает UnityEvent
public class GameEventListener : MonoBehaviour
{
    [Tooltip("Какое событие слушать")]
    [SerializeField] private GameEvent gameEvent;

    [Tooltip("Что делать при событии")]
    [SerializeField] private UnityEvent response;

    private void OnEnable()
    {
        gameEvent.RegisterListener(this);
    }

    private void OnDisable()
    {
        gameEvent.UnregisterListener(this);
    }

    // Вызывается из GameEvent.Raise()
    public void OnEventRaised()
    {
        response?.Invoke();
    }
}
```

### Шаг 4: PlayerHealth с ScriptableObject Events



```csharp
using UnityEngine;

public class PlayerHealthSO : MonoBehaviour
{
    [Header("Events")]
    [SerializeField] private HealthEvent onHealthChanged;
    [SerializeField] private GameEvent onPlayerDied;

    [Header("Settings")]
    [SerializeField] private int maxHealth = 100;

    private int _currentHealth;

    private void Awake()
    {
        _currentHealth = maxHealth;
    }

    public void TakeDamage(int damage)
    {
        if (_currentHealth <= 0) return;

        _currentHealth = Mathf.Max(0, _currentHealth - damage);
        
        // Поднимаем событие-ассет — оно само уведомит всех подписчиков
        onHealthChanged?.Raise((_currentHealth, maxHealth));

        if (_currentHealth <= 0)
        {
            onPlayerDied?.Raise();
        }
    }
}
```

### Шаг 5: Подписчики для ScriptableObject Events



```csharp
using UnityEngine;
using UnityEngine.UI;

public class HealthBarUISO : MonoBehaviour
{
    [SerializeField] private Slider healthSlider;
    
    // Ссылка на ассет события, а не на конкретный объект PlayerHealth!
    [SerializeField] private HealthEvent healthEvent;

    private void OnEnable()
    {
        healthEvent.Subscribe(HandleHealthChanged);
    }

    private void OnDisable()
    {
        healthEvent.Unsubscribe(HandleHealthChanged);
    }

    private void HandleHealthChanged((int current, int max) data)
    {
        healthSlider.value = (float)data.current / data.max;
    }
}
```

### Структура проекта с SO Events



```csharp
Assets/
├── Events/                     ← Ассеты событий
│   ├── OnHealthChanged.asset   ← HealthEvent ScriptableObject
│   ├── OnPlayerDied.asset      ← GameEvent ScriptableObject  
│   └── OnScoreChanged.asset    ← ScoreEvent ScriptableObject
│
├── Scripts/
│   ├── Events/
│   │   ├── GameEvent.cs
│   │   ├── GameEvent_T.cs
│   │   └── GameEventListener.cs
│   │
│   ├── Player/
│   │   └── PlayerHealthSO.cs   ← Знает только об ассете события
│   │
│   └── UI/
│       └── HealthBarUISO.cs    ← Знает только об ассете события
```

### Преимущество: тестирование в редакторе



```csharp
// Можно добавить кнопку в инспектор для тестирования
#if UNITY_EDITOR
using UnityEditor;

[CustomEditor(typeof(GameEvent))]
public class GameEventEditor : Editor
{
    public override void OnInspectorGUI()
    {
        base.OnInspectorGUI();
        
        var gameEvent = (GameEvent)target;
        
        if (GUILayout.Button("▶ Raise Event (Test)"))
        {
            gameEvent.Raise();
        }
    }
}
#endif
```

---

## 5. Реализация через R3 {#r3}

> ### 📦 Подключение пакета R3
> 
> **R3** — современная реализация Reactive Extensions для Unity (наследник UniRx).
> 
> **Установка через Package Manager:**
> 
> 
> 
> ```csharp
> https://github.com/Cysharp/R3.git?path=src/R3.Unity/Assets/R3.Unity
> ```
> 
> Или через `openupm`:
> 
> Bash
> 
> ```csharp
> openupm add com.cysharp.r3
> ```
> 
> **Зависимости:** R3 также требует пакет `com.cysharp.r3` (core library).  
> Подробнее: [github.com/Cysharp/R3](https://github.com/Cysharp/R3)

### Концепция реактивного программирования



```csharp
Традиционный подход:       Реактивный подход:
                           
int health = 100;          ReactiveProperty<int> health = new(100);
                           
// Вручную обновляем UI    // UI автоматически реагирует на изменения
UpdateUI(health);          health.Subscribe(v => UpdateUI(v));
                           
// Что-то меняет health    // Что-то меняет health
health = 50;               health.Value = 50; // → UI обновится сам!
UpdateUI(health); // ← нужно помнить
```

### Основные типы R3



```csharp
// ReactiveProperty<T> — значение, которое можно наблюдать
// Subject<T>          — ручное управление потоком событий
// Observable<T>       — поток данных (только для чтения)
// CompositeDisposable — контейнер для управления подписками
```

### Реализация PlayerHealth с R3



```csharp
using R3;
using UnityEngine;

public class PlayerHealthR3 : MonoBehaviour
{
    [SerializeField] private int maxHealth = 100;

    // ReactiveProperty — это и хранилище значения, и Observable одновременно
    private readonly ReactiveProperty<int> _currentHealth = new(100);

    // Публикуем только для чтения — никто не сможет изменить снаружи
    public ReadOnlyReactiveProperty<int> CurrentHealth => _currentHealth;
    public int MaxHealth => maxHealth;

    // Subject для событий без возвращаемого значения (смерть игрока)
    private readonly Subject<Unit> _onPlayerDied = new();
    public Observable<Unit> OnPlayerDied => _onPlayerDied;

    private void Awake()
    {
        _currentHealth.Value = maxHealth;
    }

    public void TakeDamage(int damage)
    {
        if (_currentHealth.Value <= 0) return;

        _currentHealth.Value = Mathf.Max(0, _currentHealth.Value - damage);

        if (_currentHealth.Value <= 0)
        {
            // Отправляем событие в поток
            _onPlayerDied.OnNext(Unit.Default);
        }
    }

    public void Heal(int amount)
    {
        _currentHealth.Value = Mathf.Min(maxHealth, _currentHealth.Value + amount);
    }

    private void OnDestroy()
    {
        // Важно: завершаем потоки при уничтожении объекта
        _currentHealth.Dispose();
        _onPlayerDied.Dispose();
    }
}
```

### Подписчики с R3



```csharp
using R3;
using UnityEngine;
using UnityEngine.UI;

public class HealthBarR3 : MonoBehaviour
{
    [SerializeField] private Slider healthSlider;
    [SerializeField] private PlayerHealthR3 playerHealth;

    // CompositeDisposable собирает все подписки для одновременной отмены
    private CompositeDisposable _disposables = new();

    private void OnEnable()
    {
        playerHealth.CurrentHealth
            // Преобразуем int в float-процент прямо в цепочке
            .Select(hp => (float)hp / playerHealth.MaxHealth)
            // Подписываемся — каждое новое значение обновит слайдер
            .Subscribe(percent => healthSlider.value = percent)
            // Добавляем в контейнер для последующей отписки
            .AddTo(_disposables);
    }

    private void OnDisable()
    {
        // Отписываемся от всего одной строкой
        _disposables.Clear();
    }

    private void OnDestroy()
    {
        _disposables.Dispose();
    }
}
```

### Мощь операторов R3



```csharp
using R3;
using UnityEngine;

public class AdvancedHealthObserver : MonoBehaviour
{
    [SerializeField] private PlayerHealthR3 playerHealth;

    private CompositeDisposable _disposables = new();

    private void OnEnable()
    {
        // Пример 1: Реагировать только когда здоровье падает ниже 30%
        playerHealth.CurrentHealth
            .Where(hp => (float)hp / playerHealth.MaxHealth < 0.3f)
            .Subscribe(_ => ShowLowHealthWarning())
            .AddTo(_disposables);

        // Пример 2: Реагировать только на изменение (пропустить одинаковые)
        playerHealth.CurrentHealth
            .DistinctUntilChanged()
            .Subscribe(hp => Debug.Log($"Здоровье изменилось: {hp}"))
            .AddTo(_disposables);

        // Пример 3: Объединить два потока — здоровье И смерть
        Observable.Merge(
            playerHealth.CurrentHealth.Select(_ => "HP изменилось"),
            playerHealth.OnPlayerDied.Select(_ => "Игрок умер")
        )
        .Subscribe(msg => Debug.Log(msg))
        .AddTo(_disposables);

        // Пример 4: Задержка — сообщение через 2 секунды после смерти
        playerHealth.OnPlayerDied
            .Delay(TimeSpan.FromSeconds(2), TimeProvider.System)
            .Subscribe(_ => ShowRespawnScreen())
            .AddTo(_disposables);

        // Пример 5: Throttle — обновлять UI не чаще раза в 100мс
        playerHealth.CurrentHealth
            .ThrottleLast(TimeSpan.FromMilliseconds(100), TimeProvider.System)
            .Subscribe(hp => UpdateExpensiveUI(hp))
            .AddTo(_disposables);
    }

    private void OnDisable() => _disposables.Clear();
    private void OnDestroy()  => _disposables.Dispose();

    private void ShowLowHealthWarning()   => Debug.Log("⚠️ Мало здоровья!");
    private void ShowRespawnScreen()      => Debug.Log("💀 Экран возрождения");
    private void UpdateExpensiveUI(int hp) => Debug.Log($"UI обновлён: {hp}");
}
```

### AddTo — магия автоотписки в Unity



```csharp
using R3;
using UnityEngine;

public class AutoDisposeExample : MonoBehaviour
{
    private void Start()
    {
        var health = GetComponent<PlayerHealthR3>();
        
        // Вариант 1: AddTo(this) — подписка живёт пока жив MonoBehaviour
        health.CurrentHealth
            .Subscribe(hp => Debug.Log(hp))
            .AddTo(this); // ← автоматически отпишется при Destroy(gameObject)

        // Вариант 2: AddTo(gameObject) — аналогично
        health.CurrentHealth
            .Subscribe(hp => Debug.Log(hp))
            .AddTo(gameObject);
            
        // ⚠️ AddTo(this) работает только с MonoBehaviour
        // Для обычных C# классов используй CompositeDisposable
    }
}
```

---

## 6. Сравнение трёх подходов {#сравнение}

### Таблица сравнения

|Критерий|C# Events|ScriptableObject Events|R3 / Reactive|
|---|---|---|---|
|**Простота освоения**|⭐⭐⭐⭐⭐ Очень легко|⭐⭐⭐⭐ Легко|⭐⭐ Сложно|
|**Зависимость между объектами**|Средняя (нужна ссылка)|Низкая (ссылка на ассет)|Средняя (нужна ссылка)|
|**Работа между сценами**|❌ Нет|✅ Да (ассет)|❌ Нет|
|**Тестирование в редакторе**|❌ Сложно|✅ Кнопка Raise|⚠️ Частично|
|**Операторы (filter, map...)**|❌ Нет|❌ Нет|✅ Богатый API|
|**Управление временем**|❌ Нет|❌ Нет|✅ Delay, Throttle|
|**Производительность**|✅ Отличная|✅ Хорошая|⚠️ Накладные расходы|
|**Внешние зависимости**|✅ Нет|✅ Нет|❌ Пакет R3|
|**Отладка**|⚠️ Средняя|✅ Легко (инспектор)|⚠️ Сложно|
|**Работа с UI**|✅ Хорошо|✅ Хорошо|✅ Отлично (биндинг)|
|**Подходит для**|Простые проекты|Средние проекты|Сложная логика|

### Плюсы и минусы



```csharp
C# Events ✅ Плюсы:          C# Events ❌ Минусы:
─────────────────────────    ─────────────────────────
• Встроен в C#               • Нужна прямая ссылка на Publisher
• Нет зависимостей           • Нет операторов трансформации
• Высокая производительность • Сложно тестировать изолированно
• Понятен любому C# разработчику  • Нет работы со временем


SO Events ✅ Плюсы:          SO Events ❌ Минусы:
─────────────────────────    ─────────────────────────
• Работают между сценами     • Больше файлов (ассеты)
• Тестируемы из инспектора   • Нет типобезопасности "из коробки"
• Нулевая связность          • Сложнее передать сложный тип данных
• Дизайнеры могут настраивать • Нужен шаблонный код


R3 ✅ Плюсы:                 R3 ❌ Минусы:
─────────────────────────    ─────────────────────────
• Мощные операторы           • Внешняя зависимость
• Композиция потоков         • Высокий порог вхождения
• Временны́е операторы        • Сложная отладка
• Элегантный код             • Избыточно для простых задач
```

### Когда что выбирать?



```csharp
Небольшой проект / прототип?
    └─► C# Events — просто и эффективно

Средний проект / команда дизайнеров?
    └─► ScriptableObject Events — гибкость и работа между сценами

Большой проект / сложная логика / много async?
    └─► R3 — максимальная мощь
    
Можно комбинировать! SO Events для глобальных событий
+ C# Events для локальной коммуникации внутри системы
```

---

## 7. Практическое задание {#практика}

### Задание: Система очков

Реализуй систему очков, где:

- `ScoreManager` — **публикует** `OnScoreChanged`
- `ScoreUI` — **подписывается** и отображает очки
- `AchievementSystem` — **подписывается** и выдаёт достижения

### ScoreManager



```csharp
using System;
using UnityEngine;

/// <summary>
/// Управляет очками игрока и уведомляет подписчиков об изменениях
/// </summary>
public class ScoreManager : MonoBehaviour
{
    // Синглтон для удобного доступа (опционально)
    public static ScoreManager Instance { get; private set; }

    // Событие: передаёт текущие очки
    public event Action<int> OnScoreChanged;
    
    // Событие: достигнут новый рекорд
    public event Action<int> OnNewHighScore;

    private int _currentScore;
    private int _highScore;

    public int CurrentScore => _currentScore;
    public int HighScore => _highScore;

    private void Awake()
    {
        // Простой синглтон
        if (Instance != null && Instance != this)
        {
            Destroy(gameObject);
            return;
        }
        Instance = this;
        
        // Загружаем рекорд из PlayerPrefs
        _highScore = PlayerPrefs.GetInt("HighScore", 0);
    }

    /// <summary>
    /// Добавляет очки и уведомляет всех подписчиков
    /// </summary>
    public void AddScore(int points)
    {
        if (points <= 0) return;

        _currentScore += points;
        
        // Проверяем рекорд
        if (_currentScore > _highScore)
        {
            _highScore = _currentScore;
            PlayerPrefs.SetInt("HighScore", _highScore);
            OnNewHighScore?.Invoke(_highScore);
        }

        // Уведомляем всех одним вызовом
        OnScoreChanged?.Invoke(_currentScore);
        
        Debug.Log($"[ScoreManager] Очки: {_currentScore} (+{points})");
    }

    /// <summary>
    /// Сбрасывает очки (например, при перезапуске)
    /// </summary>
    public void ResetScore()
    {
        _currentScore = 0;
        OnScoreChanged?.Invoke(_currentScore);
    }
}
```

### ScoreUI — отображение очков



```csharp
using TMPro;
using UnityEngine;

/// <summary>
/// Отображает текущие очки и рекорд
/// </summary>
public class ScoreUI : MonoBehaviour
{
    [Header("UI Elements")]
    [SerializeField] private MeshProUGUI currentScore;
    [SerializeField] private MeshProUGUI highScore;
    [SerializeField] private Animator scoreAnimator; // Для анимации при очках

    private static readonly int AnimationTrigger = Animator.StringToHash("ScoreAdded");

    private void OnEnable()
    {
        // Подписываемся на оба события
        ScoreManager.Instance.OnScoreChanged  += HandleScoreChanged;
        ScoreManager.Instance.OnNewHighScore  += HandleNewHighScore;
        
        // Сразу отображаем текущее значение (на случай позднего включения)
        HandleScoreChanged(ScoreManager.Instance.CurrentScore);
    }

    private void OnDisable()
    {
        // Проверяем Instance на null (может быть уничтожен раньше)
        if (ScoreManager.Instance == null) return;
        
        ScoreManager.Instance.OnScoreChanged -= HandleScoreChanged;
        ScoreManager.Instance.OnNewHighScore -= HandleNewHighScore;
    }

    private void HandleScoreChanged(int newScore)
    {
        currentScore. = $"Очки: {newScore:N0}";
        
        // Запускаем анимацию, если она задана
        scoreAnimator?.SetTrigger(AnimationTrigger);
    }

    private void HandleNewHighScore(int newHighScore)
    {
        highScore. = $"Рекорд: {newHighScore:N0}";
        
        Debug.Log($"[ScoreUI] 🌟 Новый рекорд: {newHighScore}");
    }
}
```

### AchievementSystem — система достижений



```csharp
using System.Collections.Generic;
using UnityEngine;

/// <summary>
/// Выдаёт достижения на основе набранных очков
/// </summary>
public class AchievementSystem : MonoBehaviour
{
    [System.Serializable]
    public class Achievement
    {
        public string name;
        public string description;
        public int requiredScore;
        [HideInInspector] public bool isUnlocked;
    }

    [Header("Achievements")]
    [SerializeField] private List<Achievement> achievements = new()
    {
        new Achievement { name = "Первые шаги",   description = "Набери 100 очков",   requiredScore = 100   },
        new Achievement { name = "Начинающий",    description = "Набери 500 очков",   requiredScore = 500   },
        new Achievement { name = "Опытный",       description = "Набери 1000 очков",  requiredScore = 1000  },
        new Achievement { name = "Мастер очков",  description = "Набери 5000 очков",  requiredScore = 5000  },
        new Achievement { name = "Легенда",       description = "Набери 10000 очков", requiredScore = 10000 },
    };

    private void OnEnable()
    {
        ScoreManager.Instance.OnScoreChanged += CheckAchievements;
    }

    private void OnDisable()
    {
        if (ScoreManager.Instance == null) return;
        ScoreManager.Instance.OnScoreChanged -= CheckAchievements;
    }

    private void CheckAchievements(int currentScore)
    {
        foreach (var achievement in achievements)
        {
            // Пропускаем уже разблокированные
            if (achievement.isUnlocked) continue;

            if (currentScore >= achievement.requiredScore)
            {
                UnlockAchievement(achievement);
            }
        }
    }

    private void UnlockAchievement(Achievement achievement)
    {
        achievement.isUnlocked = true;
        
        Debug.Log($"🏆 Достижение разблокировано: [{achievement.name}] — {achievement.description}");
        
        // Здесь можно показать UI-всплывашку, сохранить и т.д.
        // AchievementSystem не знает о ScoreManager — только подписывается!
    }
}
```

### Тестирование системы



```csharp
using UnityEngine;

/// <summary>
/// Тестовый компонент — имитирует набор очков
/// </summary>
public class ScoreTestDriver : MonoBehaviour
{
    [SerializeField] private int scorePerClick = 100;
    [SerializeField] private KeyCode addScoreKey  = KeyCode.Space;
    [SerializeField] private KeyCode resetScoreKey = KeyCode.R;

    private void Update()
    {
        if (Input.GetKeyDown(addScoreKey))
        {
            ScoreManager.Instance.AddScore(scorePerClick);
        }

        if (Input.GetKeyDown(resetScoreKey))
        {
            ScoreManager.Instance.ResetScore();
            Debug.Log("[Test] Очки сброшены");
        }
    }
    
    // Для тестирования из Inspector
    [ConMenu("Add 100 Score")]
    private void TestAddScore()  => ScoreManager.Instance.AddScore(100);
    
    [ConMenu("Add 1000 Score")]
    private void TestAddBigScore() => ScoreManager.Instance.AddScore(1000);
}
```

### Граф зависимостей системы



```csharp
                    ┌───────────────────┐
                    │   ScoreManager    │
                    │                   │
                    │ + OnScoreChanged  │
                    │ + OnNewHighScore   │
                    └────────┬──────────┘
                             │ публикует события
              ┌──────────────┼──────────────────┐
              │              │                  │
              ▼              ▼                  ▼
    ┌──────────────┐  ┌───────────────┐  ┌────────────────┐
    │   ScoreUI    │  │AchievementSys │  │  (любой        │
    │              │  │               │  │   будущий      │
    │ Обновляет    │  │ Выдаёт        │  │   подписчик)   │
    │ текст на     │  │ достижения    │  │                │
    │ экране       │  │ при порогах   │  │                │
    └──────────────┘  └───────────────┘  └────────────────┘
    
    ScoreManager НЕ ЗНАЕТ о существовании этих классов!
```

### Расширение без изменения ScoreManager



```csharp
// Добавляем новую систему — не трогаем ScoreManager!
public class MultiplayerSync : MonoBehaviour
{
    private void OnEnable()
    {
        ScoreManager.Instance.OnScoreChanged += SyncScoreToServer;
    }
    
    private void OnDisable()
    {
        ScoreManager.Instance.OnScoreChanged -= SyncScoreToServer;
    }
    
    private void SyncScoreToServer(int score)
    {
        // Отправляем на сервер...
        Debug.Log($"[Network] Синхронизация очков: {score}");
    }
}
```

---

## ✅ Проверь себя {#проверь-себя}

### Теоретические вопросы

**1.** Что такое "сильная связность" (tight coupling) и почему она проблема?

> _Подсказка: подумай, что произойдёт если ты переименуешь метод в одном классе, который вызывается напрямую из 10 других классов._

**2.** Чем отличается `event` от обычного `delegate` в C#? Что именно запрещает `event`?

> _Подсказка: попробуй написать `someObject.OnEvent()` и `someObject.OnEvent = null` снаружи класса._

**3.** Почему важно отписываться от событий в `OnDisable`, а не только в `OnDestroy`?

> _Подсказка: объект может быть отключён (SetActive(false)) но не уничтожен._

**4.** В чём главное преимущество ScriptableObject Events перед C# Events при работе с несколькими сценами?

**5.** Что делает оператор `.Where()` в цепочке R3? Приведи пример использования.

---

### Практические задания

**Задание 1 — Лёгкое:** Добавь к `ScoreManager` событие `OnScoreReset` и подпишись на него в `ScoreUI`, чтобы сбрасывать отображение.

**Задание 2 — Среднее:** Переделай систему здоровья из раздела 3 на **ScriptableObject Events**. Создай ассеты `OnHealthChanged.asset` и `OnPlayerDied.asset`.

**Задание 3 — Сложное:** Реализуй систему очков через **R3**: используй `ReactiveProperty<int>` для хранения очков и добавь оператор, который публикует только каждое 10-е изменение (`Where(score => score % 10 == 0)`).

**Задание 4 — Архитектурное:** Спроектируй систему событий для игры с такими требованиями:

- Игрок подбирает монеты → обновляется UI и звук
- Игрок умирает → UI, звук, сохранение, аналитика
- Уровень завершён → переход на следующий, сохранение, достижения

_Нарисуй граф зависимостей и выбери подходящий тип событий для каждого случая._

---

### Чек-лист хорошей реализации Observer



```csharp
✅ Publisher не знает о конкретных Subscriber'ах
✅ Подписка происходит в OnEnable, отписка в OnDisable
✅ Проверяется null перед вызовом события (?.Invoke)
✅ При уничтожении объекта происходит отписка
✅ Нет дублирующихся подписок (проверяй Contains или используй -=)
✅ Событие передаёт только необходимые данные
✅ Названия событий начинаются с On... (OnHealthChanged, OnPlayerDied)
✅ Новые подписчики могут быть добавлены без изменения Publisher'а
```

---

### Краткое резюме



```csharp
Observer Pattern:
    "Не звони мне, я сам позвоню" 
    — Publisher говорит всем Subscriber'ам

Три подхода в Unity:
┌─────────────────┬────────────────────┬─────────────────────┐
│   C# Events     │  SO Events         │  R3                 │
│   Быстро,       │  Гибко,            │  Мощно,             │
│   просто,       │  работает между    │  с операторами,     │
│   для начала    │  сценами           │  для сложных задач  │
└─────────────────┴────────────────────┴─────────────────────┘

Золотое правило: начни с C# Events,
переходи к SO Events когда нужна изоляция между сценами,
добавляй R3 когда нужна реактивность и операторы.
```

---

_Удачи в практике! Паттерн Observer — один из самых используемых в разработке игр. Освоив его, ты сделаешь свой код значительно чище и поддерживаемее. 🎮_