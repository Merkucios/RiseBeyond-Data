
## Содержание
- [Введение](#%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5)
	- [Что не так со старым Input Manager](#%D0%A7%D1%82%D0%BE%20%D0%BD%D0%B5%20%D1%82%D0%B0%D0%BA%20%D1%81%D0%BE%20%D1%81%D1%82%D0%B0%D1%80%D1%8B%D0%BC%20Input%20Manager)
	- [Что такое New Input System](#%D0%A7%D1%82%D0%BE%20%D1%82%D0%B0%D0%BA%D0%BE%D0%B5%20New%20Input%20System)
- [Установка](#%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0)
	- [Шаг 1 — Package Manager](#%D0%A8%D0%B0%D0%B3%201%20%E2%80%94%20Package%20Manager)
	- [Шаг 2 — Переключение Backend](#%D0%A8%D0%B0%D0%B3%202%20%E2%80%94%20%D0%9F%D0%B5%D1%80%D0%B5%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20Backend)
	- [Шаг 3 — Проверка установки](#%D0%A8%D0%B0%D0%B3%203%20%E2%80%94%20%D0%9F%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0%20%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B8)
- [Input Actions Asset](#Input%20Actions%20Asset)
	- [Структура ассета](#%D0%A1%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D0%B0%D1%81%D1%81%D0%B5%D1%82%D0%B0)
	- [Создание через Editor](#%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20Editor)
	- [Разбор редактора Input Actions](#%D0%A0%D0%B0%D0%B7%D0%B1%D0%BE%D1%80%20%D1%80%D0%B5%D0%B4%D0%B0%D0%BA%D1%82%D0%BE%D1%80%D0%B0%20Input%20Actions)
	- [Создание Action Map через код](#%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20Action%20Map%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20%D0%BA%D0%BE%D0%B4)
	- [Bindings — привязки к устройствам](#Bindings%20%E2%80%94%20%D0%BF%D1%80%D0%B8%D0%B2%D1%8F%D0%B7%D0%BA%D0%B8%20%D0%BA%20%D1%83%D1%81%D1%82%D1%80%D0%BE%D0%B9%D1%81%D1%82%D0%B2%D0%B0%D0%BC)
	- [Composite Bindings — составные привязки](#Composite%20Bindings%20%E2%80%94%20%D1%81%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D0%BD%D1%8B%D0%B5%20%D0%BF%D1%80%D0%B8%D0%B2%D1%8F%D0%B7%D0%BA%D0%B8)
- [Типы Actions](#%D0%A2%D0%B8%D0%BF%D1%8B%20Actions)
	- [Button — кнопочное действие](#Button%20%E2%80%94%20%D0%BA%D0%BD%D0%BE%D0%BF%D0%BE%D1%87%D0%BD%D0%BE%D0%B5%20%D0%B4%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%B8%D0%B5)
	- [Value — непрерывное значение](#Value%20%E2%80%94%20%D0%BD%D0%B5%D0%BF%D1%80%D0%B5%D1%80%D1%8B%D0%B2%D0%BD%D0%BE%D0%B5%20%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B5)
	- [PassThrough — сквозное значение](#PassThrough%20%E2%80%94%20%D1%81%D0%BA%D0%B2%D0%BE%D0%B7%D0%BD%D0%BE%D0%B5%20%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B5)
	- [Сравнительная таблица типов](#%D0%A1%D1%80%D0%B0%D0%B2%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0%20%D1%82%D0%B8%D0%BF%D0%BE%D0%B2)
- [Player Input Component](#Player%20Input%20Component)
	- [Добавление компонента](#%D0%94%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BA%D0%BE%D0%BC%D0%BF%D0%BE%D0%BD%D0%B5%D0%BD%D1%82%D0%B0)
	- [Notification Mode: Send Messages](#Notification%20Mode:%20Send%20Messages)
	- [Notification Mode: Invoke Unity Events](#Notification%20Mode:%20Invoke%20Unity%20Events)
	- [Notification Mode: Invoke C# Events](#Notification%20Mode:%20Invoke%20C#%20Events)
- [Чтение Input через C#](#%D0%A7%D1%82%D0%B5%D0%BD%D0%B8%D0%B5%20Input%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20C#)
	- [Генерация C# класса из Input Actions Asset](#%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F%20C#%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B0%20%D0%B8%D0%B7%20Input%20Actions%20Asset)
	- [Структура сгенерированного класса](#%D0%A1%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D1%81%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B0)
	- [Использование сгенерированного класса](#%D0%98%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%81%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B0)
	- [CallbackCon — детальная информация о событии](#CallbackCon%20%E2%80%94%20%D0%B4%D0%B5%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F%20%D0%BE%20%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B8)
	- [Прямое чтение состояния (Polling)](#%D0%9F%D1%80%D1%8F%D0%BC%D0%BE%D0%B5%20%D1%87%D1%82%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F%20(Polling))
- [Поддержка нескольких устройств](#%D0%9F%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%BA%D0%B0%20%D0%BD%D0%B5%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%B8%D1%85%20%D1%83%D1%81%D1%82%D1%80%D0%BE%D0%B9%D1%81%D1%82%D0%B2)
	- [Автоматическое определение устройства](#%D0%90%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%83%D1%81%D1%82%D1%80%D0%BE%D0%B9%D1%81%D1%82%D0%B2%D0%B0)
	- [Получение иконок кнопок по устройству](#%D0%9F%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B8%D0%BA%D0%BE%D0%BD%D0%BE%D0%BA%20%D0%BA%D0%BD%D0%BE%D0%BF%D0%BE%D0%BA%20%D0%BF%D0%BE%20%D1%83%D1%81%D1%82%D1%80%D0%BE%D0%B9%D1%81%D1%82%D0%B2%D1%83)
	- [Переназначение клавиш (Rebinding)](#%D0%9F%D0%B5%D1%80%D0%B5%D0%BD%D0%B0%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BA%D0%BB%D0%B0%D0%B2%D0%B8%D1%88%20(Rebinding))
- [Практическое задание](#%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5)
	- [Шаг 1 — Input Actions Asset](#%D0%A8%D0%B0%D0%B3%201%20%E2%80%94%20Input%20Actions%20Asset)
	- [Шаг 2 — Интерфейс взаимодействия](#%D0%A8%D0%B0%D0%B3%202%20%E2%80%94%20%D0%98%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%20%D0%B2%D0%B7%D0%B0%D0%B8%D0%BC%D0%BE%D0%B4%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%B8%D1%8F)
	- [Шаг 3 — Компонент движения](#%D0%A8%D0%B0%D0%B3%203%20%E2%80%94%20%D0%9A%D0%BE%D0%BC%D0%BF%D0%BE%D0%BD%D0%B5%D0%BD%D1%82%20%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F)
	- [Шаг 4 — Система взаимодействия](#%D0%A8%D0%B0%D0%B3%204%20%E2%80%94%20%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D0%B2%D0%B7%D0%B0%D0%B8%D0%BC%D0%BE%D0%B4%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%B8%D1%8F)
	- [Шаг 5 — Главный PlayerController](#%D0%A8%D0%B0%D0%B3%205%20%E2%80%94%20%D0%93%D0%BB%D0%B0%D0%B2%D0%BD%D1%8B%D0%B9%20PlayerController)
	- [Шаг 6 — Пример интерактивного объекта](#%D0%A8%D0%B0%D0%B3%206%20%E2%80%94%20%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%B0)
	- [Шаг 7 — Input System Debugger](#%D0%A8%D0%B0%D0%B3%207%20%E2%80%94%20Input%20System%20Debugger)
- [Проверь себя](#%D0%9F%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D1%8C%20%D1%81%D0%B5%D0%B1%D1%8F)
	- [Теоретические вопросы](#%D0%A2%D0%B5%D0%BE%D1%80%D0%B5%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%B2%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D1%8B)
	- [Практические задания](#%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F)
	- [Чеклист при использовании New Input System](#%D0%A7%D0%B5%D0%BA%D0%BB%D0%B8%D1%81%D1%82%20%D0%BF%D1%80%D0%B8%20%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B8%20New%20Input%20System)


---

## Введение

### Что не так со старым Input Manager

Если вы работали с Unity больше нескольких месяцев, вы наверняка писали что-то подобное:



```csharp
// ❌ Старый способ — Input Manager (Legacy)
void Update()
{
    // Жёстко прибито к конкретным клавишам
    float horizontal = Input.GetAxis("Horizontal");
    float vertical = Input.GetAxis("Vertical");

    if (Input.GetKeyDown(KeyCode.Space))
    {
        Jump();
    }

    if (Input.GetButtonDown("Fire1"))
    {
        Attack();
    }
}
```

На первый взгляд всё выглядит нормально. Но когда проект растёт, начинаются проблемы:



```csharp
Проблемы старого Input Manager:
│
├── 🎮 Геймпад — отдельная головная боль
│   Каждый геймпад имеет разные оси и кнопки
│   PS4: крест = joystick button 0
│   Xbox: A = joystick button 0
│   Nintendo: A = joystick button 1 (!)
│   Нужно писать разный код для каждого контроллера
│
├── 🔧 Нет горячей замены устройства
│   Подключили геймпад во время игры?
│   Придётся перезапускать или писать костыли
│
├── 📱 Мобильные устройства
│   Тач-ввод полностью отдельная система
│   Input.GetAxis не работает для свайпов
│
├── 🧪 Тестирование
│   Невозможно симулировать ввод в Unit-тестах
│   Input.GetKey нельзя вызвать без реального ввода
│
├── 🔄 Переназначение клавиш
│   Хотите дать игроку настроить управление?
│   Придётся писать всё с нуля — сериализация, UI, применение
│
├── 👥 Локальный мультиплеер
│   Два геймпада — два игрока?
│   Input Manager вообще не думал об этом
│
└── ⚡ Производительность
    Input.GetAxis опрашивается каждый кадр
    Даже если ничего не нажато — проверка идёт
```

### Что такое New Input System

**New Input System** — официальный пакет Unity, переосмысливший работу с вводом с нуля. Ключевые идеи:

1. **Абстракция от устройства** — вы работаете с _действиями_ (Actions), а не с конкретными клавишами
2. **Event-driven** — код реагирует на события, а не опрашивает состояние каждый кадр
3. **Единая система для всех устройств** — клавиатура, мышь, геймпад, тач — одно API
4. **Переназначение из коробки** — встроенная поддержка rebinding
5. **Тестируемость** — можно симулировать ввод программно



```csharp
Старый подход (Polling):          Новый подход (Event-driven):

Update() {                         OnJump(InputAction.CallbackCon ctx)
  if(GetKeyDown(Space))            {
    Jump();  ← каждый кадр           Jump();  ← только при нажатии
}                                  }
```

---

## Установка

### Шаг 1 — Package Manager

Перейдите в **Window → Package Manager**, выберите **Unity Registry** и найдите **Input System**.



```csharp
Window → Package Manager → Unity Registry → Input System → Install
```

### Шаг 2 — Переключение Backend

После установки Unity спросит, хотите ли вы переключиться на новый Input System. Нажмите **Yes** — редактор перезапустится.

Если диалог не появился, перейдите вручную:



```csharp
Edit → Project Settings → Player → Other Settings → Active Input Handling
```



```csharp
Active Input Handling:
├── Input Manager (Old)    ← только старый
├── Input System Package   ← только новый ✅ рекомендуется для новых проектов
└── Both                   ← оба одновременно (для миграции)
```

> **Совет для миграции:** Если у вас уже есть проект на старом Input Manager, выберите **Both** — это позволит постепенно переходить, не ломая существующий код.

### Шаг 3 — Проверка установки



```csharp
// Если это компилируется — всё установлено корректно
using UnityEngine.InputSystem;

public class InputSystemCheck : MonoBehaviour
{
    void Start()
    {
        // Список всех подключённых устройств
        foreach (var device in InputSystem.devices)
        {
            Debug.Log($"Устройство: {device.name} | Тип: {device.GetType().Name}");
        }
    }
}
```

---

## Input Actions Asset

**Input Actions Asset** — сердце New Input System. Это ScriptableObject-подобный ассет, в котором вы декларативно описываете всё управление игры.

### Структура ассета



```csharp
PlayerInputActions.inputactions
│
├── Action Map: "Player"          ← контекст геймплея
│   ├── Action: "Move"            ← движение
│   │   ├── Binding: WASD (Keyboard)
│   │   ├── Binding: Left Stick (Gamepad)
│   │   └── Binding: Touch (Touchscreen)
│   │
│   ├── Action: "Jump"            ← прыжок
│   │   ├── Binding: Space (Keyboard)
│   │   └── Binding: Button South (Gamepad) ← A/Крест
│   │
│   └── Action: "Interact"        ← взаимодействие
│       ├── Binding: E (Keyboard)
│       └── Binding: Button West (Gamepad)  ← X/Квадрат
│
├── Action Map: "UI"              ← контекст меню
│   ├── Action: "Navigate"
│   ├── Action: "Submit"
│   └── Action: "Cancel"
│
└── Action Map: "Vehicle"         ← контекст транспорта
    ├── Action: "Throttle"
    ├── Action: "Steering"
    └── Action: "Brake"
```

### Создание через Editor



```csharp
Project Window → ПКМ → Create → Input Actions
```

Назовите файл `PlayerInputActions`. Двойной клик открывает редактор.

### Разбор редактора Input Actions



```csharp
┌─────────────────────────────────────────────────────────┐
│  Action Maps    │    Actions        │    Bindings        │
│─────────────────│───────────────────│────────────────────│
│  + Player       │  + Move      [2D] │  WASD Composite    │
│    UI           │    Jump   [Button]│  Space <Keyboard>  │
│    Vehicle      │    Interact[Butt] │  ButtonSouth<Gmpd> │
│                 │    Look      [2D] │                    │
│  [+] Add Map    │  [+] Add Action   │  [+] Add Binding   │
└─────────────────────────────────────────────────────────┘
```

### Создание Action Map через код



```csharp
using UnityEngine;
using UnityEngine.InputSystem;

public class InputActionsBuilder : MonoBehaviour
{
    void CreateInputActionsRuntime()
    {
        // Создание Input Actions полностью в коде
        // (обычно не нужно — используйте ассет)
        var inputActions = new InputActionAsset();

        // Создаём Action Map
        var playerMap = inputActions.AddActionMap("Player");

        // Добавляем Action для движения
        var moveAction = playerMap.AddAction(
            "Move",
            InputActionType.Value
        );

        // Добавляем привязки
        moveAction.AddCompositeBinding("2DVector")
            .With("Up", "<Keyboard>/w")
            .With("Down", "<Keyboard>/s")
            .With("Left", "<Keyboard>/a")
            .With("Right", "<Keyboard>/d");

        moveAction.AddBinding("<Gamepad>/leftStick");

        // Action для прыжка
        var jumpAction = playerMap.AddAction(
            "Jump",
            InputActionType.Button
        );
        jumpAction.AddBinding("<Keyboard>/space");
        jumpAction.AddBinding("<Gamepad>/buttonSouth");

        // Активируем
        playerMap.Enable();
    }
}
```

### Bindings — привязки к устройствам

Привязки записываются в специальном синтаксисе путей:



```csharp
Синтаксис пути: <ТипУстройства>/имяКонтрола

Клавиатура:
"<Keyboard>/space"          ← Пробел
"<Keyboard>/w"              ← W
"<Keyboard>/leftShift"      ← Left Shift
"<Keyboard>/escape"         ← Escape
"<Keyboard>/f"              ← F

Мышь:
"<Mouse>/leftButton"        ← ЛКМ
"<Mouse>/rightButton"       ← ПКМ
"<Mouse>/middleButton"      ← Колёсико (нажатие)
"<Mouse>/delta"             ← Движение мыши (Vector2)
"<Mouse>/scroll"            ← Прокрутка колёсика

Геймпад (кросс-платформенно):
"<Gamepad>/buttonSouth"     ← A (Xbox) / Крест (PS) / B (Nintendo)
"<Gamepad>/buttonEast"      ← B (Xbox) / Кружок (PS) / A (Nintendo)
"<Gamepad>/buttonWest"      ← X (Xbox) / Квадрат (PS) / Y (Nintendo)
"<Gamepad>/buttonNorth"     ← Y (Xbox) / Треугольник (PS) / X (Nintendo)
"<Gamepad>/leftStick"       ← Левый стик (Vector2)
"<Gamepad>/rightStick"      ← Правый стик (Vector2)
"<Gamepad>/leftTrigger"     ← Левый триггер (float 0-1)
"<Gamepad>/rightTrigger"    ← Правый триггер
"<Gamepad>/dpad"            ← D-Pad (Vector2)
"<Gamepad>/leftShoulder"    ← LB / L1
"<Gamepad>/rightShoulder"   ← RB / R1

Xbox конкретно:
"<XInputController>/buttonSouth"  ← только Xbox контроллер

PS конкретно:
"<DualShockGamepad>/buttonSouth"  ← только DualShock
```

### Composite Bindings — составные привязки

Для движения WASD нужна составная привязка **2D Vector Composite**:



```csharp
2D Vector Composite:
├── Up:    W / ↑ стрелка
├── Down:  S / ↓ стрелка
├── Left:  A / ← стрелка
└── Right: D / → стрелка
Результат: Vector2 (-1..1, -1..1)

1D Axis Composite:
├── Positive: D
└── Negative: A
Результат: float (-1..1)

Button With One Modifier:
├── Modifier: Left Ctrl
└── Button: Z
Результат: срабатывает только при Ctrl+Z

Button With Two Modifiers:
├── Modifier1: Left Ctrl
├── Modifier2: Left Shift
└── Button: Z
Результат: Ctrl+Shift+Z
```

---

## Типы Actions

Каждый Action имеет тип, который определяет что именно он возвращает и когда срабатывает.

### Button — кнопочное действие



```csharp
Button Action:
├── Возвращает: float (0 или 1)
├── performed:  срабатывает при нажатии (pressed)
├── canceled:   срабатывает при отпускании
└── started:    срабатывает в начале нажатия

Примеры использования:
- Прыжок
- Атака
- Взаимодействие
- Открыть меню
```



```csharp
using UnityEngine;
using UnityEngine.InputSystem;

public class ButtonActionExample : MonoBehaviour
{
    private InputAction _jumpAction;

    void Awake()
    {
        _jumpAction = new InputAction(
            "Jump",
            InputActionType.Button
        );
        _jumpAction.AddBinding("<Keyboard>/space");
        _jumpAction.AddBinding("<Gamepad>/buttonSouth");
    }

    void OnEnable()
    {
        _jumpAction.Enable();

        // performed — кнопка нажата и прошла порог срабатывания
        _jumpAction.performed += OnJumpPerformed;

        // started — кнопка только начала нажиматься
        _jumpAction.started += OnJumpStarted;

        // canceled — кнопка отпущена
        _jumpAction.canceled += OnJumpCanceled;
    }

    void OnDisable()
    {
        _jumpAction.performed -= OnJumpPerformed;
        _jumpAction.started -= OnJumpStarted;
        _jumpAction.canceled -= OnJumpCanceled;
        _jumpAction.Disable();
    }

    private void OnJumpPerformed(InputAction.CallbackCon ctx)
    {
        // ctx.ReadValue<float>() вернёт 1.0f
        Debug.Log($"Прыжок! Значение: {ctx.ReadValue<float>()}");
        // Здесь выполняем прыжок
    }

    private void OnJumpStarted(InputAction.CallbackCon ctx)
    {
        // Кнопка начала нажиматься — полезно для заряжаемых атак
        Debug.Log("Кнопка прыжка начала нажиматься");
    }

    private void OnJumpCanceled(InputAction.CallbackCon ctx)
    {
        // Кнопка отпущена — полезно для переменной высоты прыжка
        Debug.Log("Кнопка прыжка отпущена");
    }
}
```

### Value — непрерывное значение



```csharp
Value Action:
├── Возвращает: float, Vector2, Vector3, Quaternion и др.
├── performed:  срабатывает при изменении значения
├── canceled:   значение вернулось к default (0, Vector2.zero)
└── started:    значение начало меняться от default

Примеры использования:
- Движение (Vector2 от стика/WASD)
- Поворот камеры (Vector2 от мыши/правого стика)
- Газ/тормоз в гонках (float от триггера)
- Зум камеры (float от колёсика)
```



```csharp
using UnityEngine;
using UnityEngine.InputSystem;

public class ValueActionExample : MonoBehaviour
{
    private InputAction _moveAction;
    private InputAction _lookAction;

    // Текущие значения — читаем в Update
    private Vector2 _moveInput;
    private Vector2 _lookInput;

    void Awake()
    {
        // Движение — Vector2
        _moveAction = new InputAction(
            "Move",
            InputActionType.Value,
            expectedControlType: "Vector2"
        );

        _moveAction.AddCompositeBinding("2DVector")
            .With("Up", "<Keyboard>/w")
            .With("Down", "<Keyboard>/s")
            .With("Left", "<Keyboard>/a")
            .With("Right", "<Keyboard>/d");

        _moveAction.AddBinding("<Gamepad>/leftStick");

        // Взгляд — Vector2
        _lookAction = new InputAction(
            "Look",
            InputActionType.Value,
            expectedControlType: "Vector2"
        );
        _lookAction.AddBinding("<Mouse>/delta");
        _lookAction.AddBinding("<Gamepad>/rightStick");
    }

    void OnEnable()
    {
        _moveAction.Enable();
        _lookAction.Enable();

        // Value: performed срабатывает при каждом изменении
        _moveAction.performed += ctx =>
            _moveInput = ctx.ReadValue<Vector2>();

        // canceled: значение вернулось к нулю
        _moveAction.canceled += ctx =>
            _moveInput = Vector2.zero;

        _lookAction.performed += ctx =>
            _lookInput = ctx.ReadValue<Vector2>();

        _lookAction.canceled += ctx =>
            _lookInput = Vector2.zero;
    }

    void OnDisable()
    {
        _moveAction.Disable();
        _lookAction.Disable();
    }

    void Update()
    {
        // Используем кэшированные значения в Update
        if (_moveInput != Vector2.zero)
        {
            transform.Translate(
                new Vector3(_moveInput.x, 0, _moveInput.y) *
                Time.deltaTime * 5f
            );
        }
    }
}
```

### PassThrough — сквозное значение



```csharp
PassThrough Action:
├── Похож на Value, но БЕЗ фильтрации конкурирующих устройств
├── Если нажать W на клавиатуре и наклонить стик одновременно —
│   Value вернёт последнее значение одного устройства
│   PassThrough вернёт значения от ОБОИХ устройств
├── performed:  срабатывает при ЛЮБОМ изменении от ЛЮБОГО устройства
└── Использование:
    - Системы с несколькими указателями (мультитач)
    - Отслеживание нескольких игроков на одном устройстве
    - Дебаг-системы
```



```csharp
using UnityEngine;
using UnityEngine.InputSystem;

public class PassThroughExample : MonoBehaviour
{
    private InputAction _touchAction;

    void Awake()
    {
        // PassThrough для отслеживания всех касаний
        _touchAction = new InputAction(
            "Touch",
            InputActionType.PassThrough,
            expectedControlType: "Touch"
        );
        _touchAction.AddBinding("<Touchscreen>/touch*/press");
    }

    void OnEnable()
    {
        _touchAction.Enable();

        // Срабатывает для КАЖДОГО касания независимо
        _touchAction.performed += ctx =>
        {
            // Определяем какой палец
            var control = ctx.control;
            Debug.Log($"Касание от: {control.path}");
        };
    }

    void OnDisable()
    {
        _touchAction.Disable();
    }
}
```

### Сравнительная таблица типов

|Характеристика|Button|Value|PassThrough|
|---|---|---|---|
|Тип возвращаемого значения|float (0/1)|Любой|Любой|
|При конкурентных устройствах|Последнее|Последнее|Все|
|performed при удержании|❌|✅ (если меняется)|✅|
|Основное применение|Нажатия|Аналоговый ввод|Мультитач|

---

## Player Input Component

**Player Input** — компонент Unity, который автоматически связывает Input Actions Asset с объектом игрока. Он берёт на себя управление Action Maps и диспетчеризацию событий.

### Добавление компонента



```csharp
Выберите объект Player → Add Component → Input → Player Input
```



```csharp
Player Input Component
├── Actions              ← ваш .inputactions ассет
├── Default Map          ← какой Action Map активен по умолчанию ("Player")
├── Notification Mode    ← как уведомлять о событиях (см. ниже)
│   ├── Send Messages
│   ├── Broadcast Messages
│   ├── Invoke Unity Events    ← через Inspector (drag & drop)
│   └── Invoke C# Events       ← через код ✅
└── UI Input Module      ← для UI навигации
```

### Notification Mode: Send Messages



```csharp
using UnityEngine;
using UnityEngine.InputSystem;

/// <summary>
/// Режим Send Messages:
/// Player Input вызывает методы с именем On{ActionName} на этом объекте.
/// Методы ДОЛЖНЫ называться точно так же как Action в ассете.
/// </summary>
public class SendMessagesExample : MonoBehaviour
{
    private Vector2 _moveInput;
    private Rigidbody _rb;

    void Awake()
    {
        _rb = GetComponent<Rigidbody>();
    }

    // Метод вызывается автоматически при событии Action "Move"
    // Имя метода: On + имя Action
    void OnMove(InputValue value)
    {
        _moveInput = value.Get<Vector2>();
    }

    // Action "Jump"
    void OnJump(InputValue value)
    {
        if (value.isPressed)
        {
            _rb.AddForce(Vector3.up * 5f, ForceMode.Impulse);
        }
    }

    // Action "Interact"
    void OnInteract(InputValue value)
    {
        if (value.isPressed)
        {
            Debug.Log("Взаимодействие!");
        }
    }

    void FixedUpdate()
    {
        var movement = new Vector3(_moveInput.x, 0, _moveInput.y);
        _rb.MovePosition(_rb.position + movement * 5f * Time.fixedDeltaTime);
    }
}
```

### Notification Mode: Invoke Unity Events

Этот режим позволяет подключать методы прямо в Inspector через drag & drop — удобно для простых случаев и прототипов.



```csharp
using UnityEngine;
using UnityEngine.InputSystem;

/// <summary>
/// Invoke Unity Events:
/// В Inspector появляются UnityEvent поля для каждого Action.
/// Перетащите метод в поле события.
/// </summary>
public class UnityEventsExample : MonoBehaviour
{
    private Vector2 _moveInput;

    // Эти методы подключаются в Inspector через поля событий
    public void OnMove(InputAction.CallbackCon con)
    {
        _moveInput = con.ReadValue<Vector2>();
    }

    public void OnJump(InputAction.CallbackCon con)
    {
        // con.phase показывает фазу действия
        if (con.phase == InputActionPhase.Performed)
        {
            Debug.Log("Прыжок через Unity Event!");
        }
    }
}
```

### Notification Mode: Invoke C# Events

Наиболее гибкий и рекомендуемый режим для сложных проектов:



```csharp
using UnityEngine;
using UnityEngine.InputSystem;

public class EventsExample : MonoBehaviour
{
    private PlayerInput _playerInput;

    void Awake()
    {
        _playerInput = GetComponent<PlayerInput>();
    }

    void OnEnable()
    {
        // Подписываемся на C# события PlayerInput
        _playerInput.onActionTriggered += OnActionTriggered;
    }

    void OnDisable()
    {
        _playerInput.onActionTriggered -= OnActionTriggered;
    }

    private void OnActionTriggered(InputAction.CallbackCon con)
    {
        // Определяем какой Action сработал
        switch (con.action.name)
        {
            case "Move":
                HandleMove(con);
                break;
            case "Jump":
                HandleJump(con);
                break;
            case "Interact":
                HandleInteract(con);
                break;
        }
    }

    private void HandleMove(InputAction.CallbackCon ctx)
    {
        if (ctx.performed || ctx.canceled)
        {
            var value = ctx.ReadValue<Vector2>();
            Debug.Log($"Движение: {value}");
        }
    }

    private void HandleJump(InputAction.CallbackCon ctx)
    {
        if (ctx.performed)
        {
            Debug.Log("Прыжок!");
        }
    }

    private void HandleInteract(InputAction.CallbackCon ctx)
    {
        if (ctx.performed)
        {
            Debug.Log("Взаимодействие!");
        }
    }
}
```

---

## Чтение Input через C#

### Генерация C# класса из Input Actions Asset

Это один из самых мощных инструментов New Input System. Вместо строковых имён ("Move", "Jump") вы получаете **типобезопасный** C# класс с автодополнением.

**Как сгенерировать:**



```csharp
1. Выберите файл PlayerInputActions.inputactions в Project
2. В Inspector установите флажок: "Generate C# Class"
3. Укажите:
   - Class Name: PlayerInputActions (имя генерируемого класса)
   - Namespace: (опционально, например: Game.Input)
   - File Path: Assets/Scripts/Input/ (куда сохранить)
4. Нажмите "Apply"
```

Unity сгенерирует файл `PlayerInputActions.cs` — полноценный C# класс.

### Структура сгенерированного класса



```csharp
// АВТОГЕНЕРАЦИЯ — не редактировать вручную!
// Файл: Assets/Scripts/Input/PlayerInputActions.cs

// Сгенерированный класс реализует несколько интерфейсов
public class PlayerInputActions : IInputActionCollection2, IDisposable
{
    // Сам ассет
    public InputActionAsset asset { get; }

    // Доступ к Action Maps как к свойствам
    public PlayerActions Player { get; }
    public UIActions UI { get; }

    // Структура для Action Map "Player"
    public struct PlayerActions
    {
        // Каждый Action доступен как свойство
        public InputAction Move { get; }
        public InputAction Jump { get; }
        public InputAction Interact { get; }
        public InputAction Look { get; }

        // Удобные методы
        public void Enable();
        public void Disable();
    }

    // Методы управления
    public void Enable();
    public void Disable();
    public void Dispose();
}
```

### Использование сгенерированного класса



```csharp
using UnityEngine;
using UnityEngine.InputSystem;

public class PlayerControllerGenerated : MonoBehaviour
{
    // Экземпляр сгенерированного класса
    private PlayerInputActions _inputActions;

    // Кэшированные значения
    private Vector2 _moveInput;
    private Vector2 _lookInput;

    void Awake()
    {
        // Создаём экземпляр
        _inputActions = new PlayerInputActions();
    }

    void OnEnable()
    {
        // Активируем нужный Action Map
        _inputActions.Player.Enable();

        // Подписываемся на события — ТИПОБЕЗОПАСНО, с автодополнением
        _inputActions.Player.Move.performed += OnMovePerformed;
        _inputActions.Player.Move.canceled += OnMoveCanceled;

        _inputActions.Player.Jump.performed += OnJumpPerformed;

        _inputActions.Player.Look.performed += OnLookPerformed;
        _inputActions.Player.Look.canceled += OnLookCanceled;

        _inputActions.Player.Interact.performed += OnInteractPerformed;
    }

    void OnDisable()
    {
        // ВАЖНО: всегда отписываться!
        _inputActions.Player.Move.performed -= OnMovePerformed;
        _inputActions.Player.Move.canceled -= OnMoveCanceled;

        _inputActions.Player.Jump.performed -= OnJumpPerformed;

        _inputActions.Player.Look.performed -= OnLookPerformed;
        _inputActions.Player.Look.canceled -= OnLookCanceled;

        _inputActions.Player.Interact.performed -= OnInteractPerformed;

        _inputActions.Player.Disable();
    }

    void OnDestroy()
    {
        // Освобождаем ресурсы
        _inputActions.Dispose();
    }

    // Обработчики
    private void OnMovePerformed(InputAction.CallbackCon ctx)
        => _moveInput = ctx.ReadValue<Vector2>();

    private void OnMoveCanceled(InputAction.CallbackCon ctx)
        => _moveInput = Vector2.zero;

    private void OnJumpPerformed(InputAction.CallbackCon ctx)
    {
        Debug.Log("🦘 Прыжок!");
        // Perform jump logic
    }

    private void OnLookPerformed(InputAction.CallbackCon ctx)
        => _lookInput = ctx.ReadValue<Vector2>();

    private void OnLookCanceled(InputAction.CallbackCon ctx)
        => _lookInput = Vector2.zero;

    private void OnInteractPerformed(InputAction.CallbackCon ctx)
        => Debug.Log("🤝 Взаимодействие!");

    void Update()
    {
        // Движение
        if (_moveInput != Vector2.zero)
        {
            transform.Translate(
                new Vector3(_moveInput.x, 0, _moveInput.y) *
                5f * Time.deltaTime
            );
        }
    }
}
```

### CallbackCon — детальная информация о событии



```csharp
private void OnActionCallback(InputAction.CallbackCon ctx)
{
    // === Фаза действия ===
    InputActionPhase phase = ctx.phase;
    // Started   — начало (кнопка чуть нажата / стик отклонился)
    // Performed — выполнено (прошло threshold / нажато)
    // Canceled  — отменено (отпущено / стик вернулся)
    // Waiting   — ожидание (не активно)
    // Disabled  — отключено

    bool isStarted = ctx.started;    // phase == Started
    bool isPerformed = ctx.performed; // phase == Performed
    bool isCanceled = ctx.canceled;   // phase == Canceled

    // === Чтение значений ===
    float floatValue = ctx.ReadValue<float>();
    Vector2 vector2Value = ctx.ReadValue<Vector2>();
    Vector3 vector3Value = ctx.ReadValue<Vector3>();

    // === Информация о контроле ===
    InputControl control = ctx.control;
    string controlPath = control.path;    // "/Gamepad/buttonSouth"
    string controlName = control.name;    // "buttonSouth"

    // === Информация об устройстве ===
    InputDevice device = ctx.control.device;
    bool isGamepad = device is Gamepad;
    bool isKeyboard = device is Keyboard;
    bool isMouse = device is Mouse;

    if (device is Gamepad gamepad)
    {
        Debug.Log($"Геймпад: {gamepad.name}");
    }

    // === Временные метки ===
    double time = ctx.time;           // время события (секунды)
    double startTime = ctx.startTime; // время начала действия

    // Длительность удержания кнопки
    double duration = ctx.time - ctx.startTime;

    // === Информация об Action ===
    InputAction action = ctx.action;
    string actionName = action.name;   // "Jump"
    string mapName = action.actionMap.name; // "Player"
}
```

### Прямое чтение состояния (Polling)

Иногда нужно читать состояние в Update, а не через события:



```csharp
using UnityEngine;
using UnityEngine.InputSystem;

public class PollingExample : MonoBehaviour
{
    private PlayerInputActions _input;

    void Awake()
    {
        _input = new PlayerInputActions();
        _input.Player.Enable();
    }

    void Update()
    {
        // Прямое чтение текущего значения Action
        Vector2 moveInput = _input.Player.Move.ReadValue<Vector2>();

        // Проверка нажатия (аналог GetKeyDown для кнопок)
        bool jumpPressed = _input.Player.Jump.WasPressedThisFrame();
        bool jumpReleased = _input.Player.Jump.WasReleasedThisFrame();

        // Проверка удержания
        bool jumpHeld = _input.Player.Jump.IsPressed();

        if (jumpPressed)
            Debug.Log("Прыжок нажат в этом кадре");

        if (jumpHeld)
            Debug.Log($"Кнопка прыжка удерживается");

        if (jumpReleased)
            Debug.Log("Прыжок отпущен в этом кадре");

        // Движение
        transform.Translate(
            new Vector3(moveInput.x, 0, moveInput.y) *
            5f * Time.deltaTime
        );
    }

    void OnDestroy()
    {
        _input.Dispose();
    }
}
```

---

## Поддержка нескольких устройств

### Автоматическое определение устройства



```csharp
using UnityEngine;
using UnityEngine.InputSystem;

public class MultiDeviceSupport : MonoBehaviour
{
    private PlayerInputActions _input;

    [Header("UI подсказки")]
    [SerializeField] private GameObject keyboardHints;
    [SerializeField] private GameObject gamepadHints;

    void Awake()
    {
        _input = new PlayerInputActions();
        _input.Enable();
    }

    void OnEnable()
    {
        // Подписываемся на событие смены активного устройства
        InputSystem.onActionChange += OnActionChange;

        // Событие подключения/отключения устройства
        InputSystem.onDeviceChange += OnDeviceChange;
    }

    void OnDisable()
    {
        InputSystem.onActionChange -= OnActionChange;
        InputSystem.onDeviceChange -= OnDeviceChange;
    }

    void OnDestroy()
    {
        _input.Dispose();
    }

    private void OnActionChange(object obj, InputActionChange change)
    {
        // Отслеживаем какое устройство последним использовалось
        if (change == InputActionChange.ActionPerformed)
        {
            if (obj is InputAction action)
            {
                var device = action.activeControl?.device;
                UpdateControlHints(device);
            }
        }
    }

    private void OnDeviceChange(InputDevice device, InputDeviceChange change)
    {
        switch (change)
        {
            case InputDeviceChange.Added:
                Debug.Log($"✅ Устройство подключено: {device.name}");
                if (device is Gamepad)
                    ShowGamepadHints();
                break;

            case InputDeviceChange.Removed:
                Debug.Log($"❌ Устройство отключено: {device.name}");
                if (device is Gamepad)
                    ShowKeyboardHints();
                break;
        }
    }

    private void UpdateControlHints(InputDevice device)
    {
        if (device == null) return;

        if (device is Gamepad)
            ShowGamepadHints();
        else if (device is Keyboard || device is Mouse)
            ShowKeyboardHints();
    }

    private void ShowGamepadHints()
    {
        if (keyboardHints) keyboardHints.SetActive(false);
        if (gamepadHints) gamepadHints.SetActive(true);
        Debug.Log("🎮 Показываем подсказки для геймпада");
    }

    private void ShowKeyboardHints()
    {
        if (keyboardHints) keyboardHints.SetActive(true);
        if (gamepadHints) gamepadHints.SetActive(false);
        Debug.Log("⌨️ Показываем подсказки для клавиатуры");
    }
}
```

### Получение иконок кнопок по устройству



```csharp
using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.InputSystem.Utilities;

public class ControlIconProvider : MonoBehaviour
{
    private PlayerInputActions _input;
    private PlayerInput _playerInput;

    void Awake()
    {
        _input = new PlayerInputActions();
        _playerInput = GetComponent<PlayerInput>();
    }

    /// <summary>
    /// Получить название привязки для отображения игроку
    /// </summary>
    public string GetBindingDisplayName(string actionName, string actionMapName = "Player")
    {
        var action = _input.asset.FindAction($"{actionMapName}/{actionName}");
        if (action == null) return "???";

        // Получаем все привязки
        var bindings = action.bindings;

        // Определяем текущее устройство
        var currentDevice = GetCurrentDevice();

        // Ищем привязку для текущего устройства
        foreach (var binding in bindings)
        {
            if (IsBindingForDevice(binding, currentDevice))
            {
                return InputControlPath.ToHumanReadableString(
                    binding.effectivePath,
                    InputControlPath.HumanReadableStringOptions.OmitDevice
                );
            }
        }

        // Fallback — возвращаем первую привязку
        if (bindings.Count > 0)
        {
            return InputControlPath.ToHumanReadableString(
                bindings[0].effectivePath,
                InputControlPath.HumanReadableStringOptions.OmitDevice
            );
        }

        return "???";
    }

    private InputDevice GetCurrentDevice()
    {
        if (_playerInput != null && _playerInput.devices.Count > 0)
            return _playerInput.devices[0];

        // Проверяем доступные устройства
        if (Gamepad.current != null) return Gamepad.current;
        if (Keyboard.current != null) return Keyboard.current;

        return null;
    }

    private bool IsBindingForDevice(InputBinding binding, InputDevice device)
    {
        if (device == null) return false;
        if (binding.isComposite || binding.isPartOfComposite) return false;

        string path = binding.effectivePath;

        return device switch
        {
            Gamepad => path.StartsWith("<Gamepad>") ||
                       path.StartsWith("<DualShock") ||
                       path.StartsWith("<XInput"),
            Keyboard => path.StartsWith("<Keyboard>"),
            Mouse => path.StartsWith("<Mouse>"),
            _ => false
        };
    }

    // Пример использования:
    // string jumpKey = GetBindingDisplayName("Jump");
    // hintLabel. = $"Нажмите [{jumpKey}] для прыжка";
}
```

### Переназначение клавиш (Rebinding)



```csharp
using System.Collections;
using UnityEngine;
using UnityEngine.InputSystem;

public class RebindingController : MonoBehaviour
{
    private PlayerInputActions _input;
    private InputActionRebindingExtensions.RebindingOperation _rebindOperation;

    void Awake()
    {
        _input = new PlayerInputActions();
        _input.Enable();

        // Загружаем сохранённые переназначения
        LoadBindings();
    }

    void OnDestroy()
    {
        // Завершаем операцию если ещё идёт
        _rebindOperation?.Cancel();
        _rebindOperation?.Dispose();
        _input.Dispose();
    }

    /// <summary>
    /// Начать переназначение кнопки
    /// </summary>
    public void StartRebinding(string actionName, int bindingIndex = 0)
    {
        var action = _input.asset.FindAction(actionName);
        if (action == null)
        {
            Debug.LogError($"Action '{actionName}' не найден!");
            return;
        }

        // Отключаем на время переназначения
        action.Disable();

        // Начинаем интерактивное переназначение
        _rebindOperation = action
            .PerformInteractiveRebinding(bindingIndex)
            .WithControlsExcluding("<Mouse>/position")  // Исключаем движение мыши
            .WithControlsExcluding("<Mouse>/delta")
            .WithCancelingThrough("<Keyboard>/escape")  // Отмена по Escape
            .OnMatchWaitForAnother(0.1f)                // Ждём 0.1с для подтверждения
            .OnComplete(operation => RebindComplete(action, operation))
            .OnCancel(operation => RebindCanceled(action, operation))
            .Start();

        Debug.Log($"⌨️ Ожидаю нажатия для '{actionName}'...");
    }

    private void RebindComplete(
        InputAction action,
        InputActionRebindingExtensions.RebindingOperation operation)
    {
        Debug.Log($"✅ Переназначено: {action.name} = " +
                  $"{action.bindings[operation.selectedBindingIndex].effectivePath}");

        operation.Dispose();
        action.Enable();

        // Сохраняем
        SaveBindings();
    }

    private void RebindCanceled(
        InputAction action,
        InputActionRebindingExtensions.RebindingOperation operation)
    {
        Debug.Log("❌ Переназначение отменено");
        operation.Dispose();
        action.Enable();
    }

    /// <summary>Сброс привязок к умолчаниям</summary>
    public void ResetToDefaults()
    {
        _input.asset.RemoveAllBindingOverrides();
        SaveBindings();
        Debug.Log("🔄 Привязки сброшены к умолчаниям");
    }

    private void SaveBindings()
    {
        // Сериализуем все переопределения в JSON
        string overrides = _input.asset.SaveBindingOverridesAsJson();
        PlayerPrefs.SetString("InputBindings", overrides);
        PlayerPrefs.Save();
        Debug.Log("💾 Привязки сохранены");
    }

    private void LoadBindings()
    {
        if (PlayerPrefs.HasKey("InputBindings"))
        {
            string overrides = PlayerPrefs.GetString("InputBindings");
            _input.asset.LoadBindingOverridesFromJson(overrides);
            Debug.Log("📂 Привязки загружены");
        }
    }
}
```

---

## Практическое задание

Создадим полноценный `PlayerController` с движением, прыжком, взаимодействием и поддержкой клавиатуры и геймпада одновременно.

### Шаг 1 — Input Actions Asset

Создайте файл `PlayerInputActions.inputactions` со следующей структурой:



```csharp
Action Map: Player
│
├── Move (Value, Vector2)
│   ├── [Composite] WASD 2D Vector
│   │   ├── Up:    W + UpArrow
│   │   ├── Down:  S + DownArrow
│   │   ├── Left:  A + LeftArrow
│   │   └── Right: D + RightArrow
│   └── [Binding] <Gamepad>/leftStick
│
├── Jump (Button)
│   ├── <Keyboard>/space
│   └── <Gamepad>/buttonSouth
│
├── Interact (Button)
│   ├── <Keyboard>/e
│   └── <Gamepad>/buttonWest
│
├── Look (Value, Vector2)
│   ├── <Mouse>/delta
│   └── <Gamepad>/rightStick
│
├── Sprint (Button)
│   ├── <Keyboard>/leftShift
│   └── <Gamepad>/leftStickPress
│
└── Pause (Button)
    ├── <Keyboard>/escape
    └── <Gamepad>/start
```

После создания — включите **Generate C# Class** и нажмите **Apply**.

### Шаг 2 — Интерфейс взаимодействия



```csharp
// Файл: Assets/Scripts/Interfaces/IInteractable.cs
/// <summary>
/// Интерфейс для объектов с которыми можно взаимодействовать
/// </summary>
public interface IInteractable
{
    /// <summary>Взаимодействовать с объектом</summary>
    void Interact(PlayerController player);

    /// <summary>Текст подсказки для игрока</summary>
    string InteractionHint { get; }
}
```

### Шаг 3 — Компонент движения



```csharp
// Файл: Assets/Scripts/Player/PlayerMovement.cs
using UnityEngine;

[RequireComponent(typeof(CharacterController))]
public class PlayerMovement : MonoBehaviour
{
    [Header("Движение")]
    [SerializeField] private float walkSpeed = 5f;
    [SerializeField] private float sprintSpeed = 9f;
    [SerializeField] private float acceleration = 15f;
    [SerializeField] private float deceleration = 20f;

    [Header("Прыжок")]
    [SerializeField] private float jumpHeight = 2f;
    [SerializeField] private float gravity = -20f;
    [SerializeField] private int maxJumpCount = 2;  // Двойной прыжок

    [Header("Камера")]
    [SerializeField] private Transform cameraTransform;
    [SerializeField] private float lookSensitivityMouse = 0.15f;
    [SerializeField] private float lookSensitivityGamepad = 150f;
    [SerializeField] private float verticalLookLimit = 85f;

    // Компоненты
    private CharacterController _controller;

    // Состояние движения
    private Vector3 _currentVelocity;
    private Vector3 _verticalVelocity;
    private float _cameraVerticalAngle;
    private int _jumpsRemaining;

    // Входные данные (устанавливаются из PlayerController)
    private Vector2 _moveInput;
    private Vector2 _lookInput;
    private bool _isSprinting;
    private bool _isGamepadLook;

    public bool IsGrounded => _controller.isGrounded;
    public Vector3 Velocity => _controller.velocity;

    void Awake()
    {
        _controller = GetComponent<CharacterController>();

        if (cameraTransform == null)
        {
            var cam = GetComponentInChildren<Camera>();
            if (cam != null) cameraTransform = cam.transform;
        }
    }

    void Start()
    {
        Cursor.lockState = CursorLockMode.Locked;
        Cursor.visible = false;
    }

    void Update()
    {
        HandleGravityAndJumpState();
        HandleHorizontalMovement();
        HandleCameraRotation();
    }

    private void HandleGravityAndJumpState()
    {
        if (_controller.isGrounded)
        {
            // Сбрасываем вертикальную скорость при нахождении на земле
            if (_verticalVelocity.y < -2f)
                _verticalVelocity.y = -2f;

            // Восстанавливаем прыжки
            _jumpsRemaining = maxJumpCount;
        }

        // Применяем гравитацию
        _verticalVelocity.y += gravity * Time.deltaTime;
    }

    private void HandleHorizontalMovement()
    {
        float targetSpeed = _isSprinting ? sprintSpeed : walkSpeed;

        // Вектор движения в мировых координатах (относительно камеры)
        Vector3 inputDirection = Vector3.zero;

        if (_moveInput != Vector2.zero)
        {
            // Направление относительно поворота камеры
            Vector3 forward = cameraTransform != null
                ? Vector3.ProjectOnPlane(cameraTransform.forward, Vector3.up).normalized
                : transform.forward;

            Vector3 right = cameraTransform != null
                ? Vector3.ProjectOnPlane(cameraTransform.right, Vector3.up).normalized
                : transform.right;

            inputDirection = (forward * _moveInput.y + right * _moveInput.x).normalized;
        }

        // Плавное ускорение и замедление
        Vector3 targetVelocity = inputDirection * targetSpeed;
        float smoothFactor = inputDirection == Vector3.zero ? deceleration : acceleration;

        _currentVelocity = Vector3.MoveTowards(
            _currentVelocity,
            targetVelocity,
            smoothFactor * Time.deltaTime
        );

        // Применяем движение
        Vector3 motion = (_currentVelocity + _verticalVelocity) * Time.deltaTime;
        _controller.Move(motion);

        // Поворачиваем персонажа в направлении движения
        if (_currentVelocity.magnitude > 0.1f)
        {
            Quaternion targetRotation = Quaternion.LookRotation(_currentVelocity);
            transform.rotation = Quaternion.Slerp(
                transform.rotation,
                targetRotation,
                15f * Time.deltaTime
            );
        }
    }

    private void HandleCameraRotation()
    {
        if (_lookInput == Vector2.zero || cameraTransform == null) return;

        float sensitivity = _isGamepadLook
            ? lookSensitivityGamepad * Time.deltaTime
            : lookSensitivityMouse;

        // Горизонтальное вращение — поворачиваем transform игрока
        // (только если камера за плечом, а не от третьего лица)
        // transform.Rotate(Vector3.up * _lookInput.x * sensitivity);

        // Вертикальное вращение камеры
        _cameraVerticalAngle -= _lookInput.y * sensitivity;
        _cameraVerticalAngle = Mathf.Clamp(
            _cameraVerticalAngle,
            -verticalLookLimit,
            verticalLookLimit
        );
        cameraTransform.localEulerAngles = Vector3.right * _cameraVerticalAngle;
    }

    // === Публичный API ===

    public void SetMoveInput(Vector2 input) => _moveInput = input;
    public void SetLookInput(Vector2 input, bool isGamepad = false)
    {
        _lookInput = input;
        _isGamepadLook = isGamepad;
    }
    public void SetSprinting(bool isSprinting) => _isSprinting = isSprinting;

    public bool TryJump()
    {
        if (_jumpsRemaining <= 0) return false;

        // Физика прыжка: v = sqrt(2 * g * h)
        _verticalVelocity.y = Mathf.Sqrt(jumpHeight * -2f * gravity);
        _jumpsRemaining--;

        Debug.Log($"🦘 Прыжок! Осталось: {_jumpsRemaining}");
        return true;
    }
}
```

### Шаг 4 — Система взаимодействия



```csharp
// Файл: Assets/Scripts/Player/PlayerInteractionSystem.cs
using UnityEngine;

public class PlayerInteractionSystem : MonoBehaviour
{
    [Header("Настройки")]
    [SerializeField] private float interactionDistance = 2.5f;
    [SerializeField] private LayerMask interactionLayerMask;
    [SerializeField] private Transform raycastOrigin;

    [Header("UI")]
    [SerializeField] private GameObject interactionHintUI;
    [SerializeField] private UnityEngine.UI. hint;

    private PlayerController _player;
    private IInteractable _currentInteractable;

    void Awake()
    {
        _player = GetComponent<PlayerController>();
        if (raycastOrigin == null) raycastOrigin = transform;
    }

    void Update()
    {
        DetectInteractable();
    }

    private void DetectInteractable()
    {
        Ray ray = new Ray(raycastOrigin.position, raycastOrigin.forward);

        IInteractable detected = null;

        if (Physics.Raycast(ray, out RaycastHit hit,
            interactionDistance, interactionLayerMask))
        {
            detected = hit.collider.GetComponent<IInteractable>();
        }

        // Обновляем текущую цель
        if (detected != _currentInteractable)
        {
            _currentInteractable = detected;
            UpdateHintUI();
        }
    }

    private void UpdateHintUI()
    {
        bool hasTarget = _currentInteractable != null;

        if (interactionHintUI != null)
            interactionHintUI.SetActive(hasTarget);

        if (hasTarget && hint != null)
            hint. = _currentInteractable.InteractionHint;
    }

    public void TryInteract()
    {
        if (_currentInteractable == null)
        {
            Debug.Log("Нет объекта для взаимодействия");
            return;
        }

        Debug.Log($"✅ Взаимодействие с: {(_currentInteractable as MonoBehaviour)?.name}");
        _currentInteractable.Interact(_player);
    }

    void OnDrawGizmosSelected()
    {
        // Визуализация луча взаимодействия в Editor
        if (raycastOrigin == null) return;

        Gizmos.color = _currentInteractable != null ? Color.green : Color.yellow;
        Gizmos.DrawRay(raycastOrigin.position,
            raycastOrigin.forward * interactionDistance);

        if (_currentInteractable != null)
        {
            Gizmos.DrawWireSphere(
                ((_currentInteractable as MonoBehaviour)?.transform.position
                    ?? raycastOrigin.position),
                0.3f
            );
        }
    }
}
```

### Шаг 5 — Главный PlayerController



```csharp
// Файл: Assets/Scripts/Player/PlayerController.cs
using UnityEngine;
using UnityEngine.InputSystem;

/// <summary>
/// Главный контроллер игрока.
/// Принимает ввод через New Input System и делегирует логику
/// специализированным компонентам.
/// </summary>
[RequireComponent(typeof(PlayerMovement))]
[RequireComponent(typeof(PlayerInteractionSystem))]
public class PlayerController : MonoBehaviour
{
    // ==============================
    //   Компоненты
    // ==============================

    private PlayerInputActions _input;
    private PlayerMovement _movement;
    private PlayerInteractionSystem _interaction;

    // ==============================
    //   Состояние
    // ==============================

    private bool _isPaused;

    // Определяем тип последнего устройства ввода
    private enum ControlScheme { KeyboardMouse, Gamepad }
    private ControlScheme _currentScheme = ControlScheme.KeyboardMouse;

    // ==============================
    //   Инициализация
    // ==============================

    void Awake()
    {
        _movement = GetComponent<PlayerMovement>();
        _interaction = GetComponent<PlayerInteractionSystem>();

        // Создаём Input Actions
        _input = new PlayerInputActions();
    }

    void OnEnable()
    {
        EnablePlayerInput();
    }

    void OnDisable()
    {
        DisablePlayerInput();
    }

    void OnDestroy()
    {
        _input.Dispose();
    }

    // ==============================
    //   Управление Input
    // ==============================

    private void EnablePlayerInput()
    {
        _input.Player.Enable();

        // Движение — Value (Vector2)
        _input.Player.Move.performed += OnMovePerformed;
        _input.Player.Move.canceled += OnMoveCanceled;

        // Взгляд — Value (Vector2)
        _input.Player.Look.performed += OnLookPerformed;
        _input.Player.Look.canceled += OnLookCanceled;

        // Прыжок — Button
        _input.Player.Jump.performed += OnJumpPerformed;

        // Взаимодействие — Button
        _input.Player.Interact.performed += OnInteractPerformed;

        // Бег — Button (hold)
        _input.Player.Sprint.performed += OnSprintStarted;
        _input.Player.Sprint.canceled += OnSprintEnded;

        // Пауза — Button
        _input.Player.Pause.performed += OnPausePerformed;
    }

    private void DisablePlayerInput()
    {
        _input.Player.Move.performed -= OnMovePerformed;
        _input.Player.Move.canceled -= OnMoveCanceled;

        _input.Player.Look.performed -= OnLookPerformed;
        _input.Player.Look.canceled -= OnLookCanceled;

        _input.Player.Jump.performed -= OnJumpPerformed;

        _input.Player.Interact.performed -= OnInteractPerformed;

        _input.Player.Sprint.performed -= OnSprintStarted;
        _input.Player.Sprint.canceled -= OnSprintEnded;

        _input.Player.Pause.performed -= OnPausePerformed;

        _input.Player.Disable();
    }

    // ==============================
    //   Обработчики Input событий
    // ==============================

    private void OnMovePerformed(InputAction.CallbackCon ctx)
    {
        UpdateControlScheme(ctx);
        _movement.SetMoveInput(ctx.ReadValue<Vector2>());
    }

    private void OnMoveCanceled(InputAction.CallbackCon ctx)
    {
        _movement.SetMoveInput(Vector2.zero);
    }

    private void OnLookPerformed(InputAction.CallbackCon ctx)
    {
        UpdateControlScheme(ctx);
        bool isGamepad = _currentScheme == ControlScheme.Gamepad;
        _movement.SetLookInput(ctx.ReadValue<Vector2>(), isGamepad);
    }

    private void OnLookCanceled(InputAction.CallbackCon ctx)
    {
        _movement.SetLookInput(Vector2.zero);
    }

    private void OnJumpPerformed(InputAction.CallbackCon ctx)
    {
        if (_isPaused) return;
        UpdateControlScheme(ctx);

        bool jumped = _movement.TryJump();

        if (jumped)
        {
            // Здесь можно воспроизвести анимацию, звук и т.д.
            OnJumpExecuted();
        }
        else
        {
            Debug.Log("❌ Прыжок недоступен (нет зарядов)");
        }
    }

    private void OnInteractPerformed(InputAction.CallbackCon ctx)
    {
        if (_isPaused) return;
        UpdateControlScheme(ctx);

        _interaction.TryInteract();
    }

    private void OnSprintStarted(InputAction.CallbackCon ctx)
    {
        _movement.SetSprinting(true);
        Debug.Log("🏃 Бег начат");
    }

    private void OnSprintEnded(InputAction.CallbackCon ctx)
    {
        _movement.SetSprinting(false);
        Debug.Log("🚶 Бег завершён");
    }

    private void OnPausePerformed(InputAction.CallbackCon ctx)
    {
        TogglePause();
    }

    // ==============================
    //   Игровая логика
    // ==============================

    private void OnJumpExecuted()
    {
        // Событие для других систем (анимации, звука, частиц)
        Debug.Log($"🦘 Прыжок выполнен! Схема: {_currentScheme}");

        // Например:
        // _animator?.SetTrigger("Jump");
        // _audioSource?.PlayOneShot(jumpClip);
    }

    private void TogglePause()
    {
        _isPaused = !_isPaused;
        Time.timeScale = _isPaused ? 0f : 1f;

        // При паузе — переключаем Action Map
        if (_isPaused)
        {
            _input.Player.Disable();
            _input.UI.Enable();
            Cursor.lockState = CursorLockMode.None;
            Cursor.visible = true;
            Debug.Log("⏸ Пауза");
        }
        else
        {
            _input.UI.Disable();
            _input.Player.Enable();
            Cursor.lockState = CursorLockMode.Locked;
            Cursor.visible = false;
            Debug.Log("▶ Продолжить");
        }
    }

    // ==============================
    //   Определение устройства
    // ==============================

    private void UpdateControlScheme(InputAction.CallbackCon ctx)
    {
        var device = ctx.control.device;
        var newScheme = device is Gamepad
            ? ControlScheme.Gamepad
            : ControlScheme.KeyboardMouse;

        if (newScheme != _currentScheme)
        {
            _currentScheme = newScheme;
            OnControlSchemeChanged(newScheme);
        }
    }

    private void OnControlSchemeChanged(ControlScheme newScheme)
    {
        Debug.Log($"🎮 Схема управления: {newScheme}");

        // Здесь обновляем UI подсказки
        // UIManager.Instance?.UpdateControlHints(newScheme == ControlScheme.Gamepad);
    }

    // ==============================
    //   Публичный API
    // ==============================

    public bool IsPaused => _isPaused;
    public bool IsGamepadActive => _currentScheme == ControlScheme.Gamepad;

    /// <summary>
    /// Полностью заблокировать ввод (например, во время катсцены)
    /// </summary>
    public void LockInput()
    {
        _input.Disable();
        Debug.Log("🔒 Ввод заблокирован");
    }

    /// <summary>
    /// Разблокировать ввод
    /// </summary>
    public void UnlockInput()
    {
        _input.Player.Enable();
        Debug.Log("🔓 Ввод разблокирован");
    }

    // ==============================
    //   Отладка
    // ==============================

#if UNITY_EDITOR
    void OnGUI()
    {
        var style = new GUIStyle(GUI.skin.label)
        {
            fontSize = 14,
            normal = { Color = Color.white }
        };

        GUILayout.BeginArea(new Rect(10, 10, 300, 200));
        GUILayout.Label($"Схема: {_currentScheme}", style);
        GUILayout.Label($"Пауза: {_isPaused}", style);
        GUILayout.Label($"На земле: {_movement.IsGrounded}", style);
        GUILayout.Label($"Скорость: {_movement.Velocity.magnitude:F1}", style);
        GUILayout.EndArea();
    }
#endif
}
```

### Шаг 6 — Пример интерактивного объекта



```csharp
// Файл: Assets/Scripts/World/InteractableChest.cs
using UnityEngine;

public class InteractableChest : MonoBehaviour, IInteractable
{
    [Header("Настройки")]
    [SerializeField] private int coinsInside = 50;
    [SerializeField] private bool isOpen = false;

    [Header("Анимация")]
    [SerializeField] private Animator chestAnimator;

    public string InteractionHint => isOpen
        ? "Сундук пуст"
        : $"[E] Открыть сундук ({coinsInside} монет)";

    public void Interact(PlayerController player)
    {
        if (isOpen)
        {
            Debug.Log("📦 Сундук уже открыт и пуст");
            return;
        }

        OpenChest();
    }

    private void OpenChest()
    {
        isOpen = true;
        Debug.Log($"📦 Сундук открыт! Получено {coinsInside} монет");

        // Анимация открытия
        chestAnimator?.SetTrigger("Open");

        // Добавляем монеты игроку
        // PlayerInventory.Instance?.AddCoins(coinsInside);

        // Эффекты
        // ParticleSystem.Play();
        // AudioSource.PlayClipAtPoint(openSound, transform.position);
    }
}
```

### Шаг 7 — Input System Debugger



```csharp
// Файл: Assets/Scripts/Debug/InputDebugger.cs
using UnityEngine;
using UnityEngine.InputSystem;

/// <summary>
/// Дебаг-утилита — показывает состояние всех Input устройств
/// Только для разработки, уберите перед релизом
/// </summary>
public class InputDebugger : MonoBehaviour
{
    [Header("Настройки отображения")]
    [SerializeField] private bool showKeyboard = true;
    [SerializeField] private bool showGamepad = true;
    [SerializeField] private bool showMouse = false;

    private GUIStyle _labelStyle;
    private GUIStyle _headerStyle;

    void OnGUI()
    {
        InitStyles();

        float x = Screen.width - 320f;
        float y = 10f;
        float width = 310f;

        GUILayout.BeginArea(new Rect(x, y, width, Screen.height - 20f));

        if (showKeyboard && Keyboard.current != null)
            DrawKeyboardDebug();

        if (showGamepad && Gamepad.current != null)
            DrawGamepadDebug();

        if (showMouse && Mouse.current != null)
            DrawMouseDebug();

        GUILayout.EndArea();
    }

    private void DrawKeyboardDebug()
    {
        var kb = Keyboard.current;

        GUILayout.Label("⌨️ КЛАВИАТУРА", _headerStyle);
        GUILayout.Label($"W: {kb.wKey.isPressed} | " +
                        $"A: {kb.aKey.isPressed} | " +
                        $"S: {kb.sKey.isPressed} | " +
                        $"D: {kb.dKey.isPressed}", _labelStyle);
        GUILayout.Label($"Space: {kb.spaceKey.isPressed}", _labelStyle);
        GUILayout.Label($"E: {kb.eKey.isPressed}", _labelStyle);
        GUILayout.Label($"Shift: {kb.leftShiftKey.isPressed}", _labelStyle);
        GUILayout.Space(5);
    }

    private void DrawGamepadDebug()
    {
        var gp = Gamepad.current;

        GUILayout.Label("🎮 ГЕЙМПАД: " + gp.name, _headerStyle);
        GUILayout.Label($"Left Stick: {gp.leftStick.ReadValue():F2}",
            _labelStyle);
        GUILayout.Label($"Right Stick: {gp.rightStick.ReadValue():F2}",
            _labelStyle);
        GUILayout.Label($"South (A/✕): {gp.buttonSouth.isPressed} | " +
                        $"West (X/□): {gp.buttonWest.isPressed}", _labelStyle);
        GUILayout.Label($"LT: {gp.leftTrigger.ReadValue():F2} | " +
                        $"RT: {gp.rightTrigger.ReadValue():F2}", _labelStyle);
        GUILayout.Space(5);
    }

    private void DrawMouseDebug()
    {
        var mouse = Mouse.current;

        GUILayout.Label("🖱️ МЫШЬ", _headerStyle);
        GUILayout.Label($"Position: {mouse.position.ReadValue():F0}",
            _labelStyle);
        GUILayout.Label($"Delta: {mouse.delta.ReadValue():F2}",
            _labelStyle);
        GUILayout.Label($"LMB: {mouse.leftButton.isPressed} | " +
                        $"RMB: {mouse.rightButton.isPressed}", _labelStyle);
        GUILayout.Space(5);
    }

    private void InitStyles()
    {
        if (_labelStyle != null) return;

        _labelStyle = new GUIStyle(GUI.skin.label)
        {
            fontSize = 12,
            normal = { Color = Color.white },
            wordWrap = true
        };

        _headerStyle = new GUIStyle(_labelStyle)
        {
            fontSize = 13,
            fontStyle = FontStyle.Bold,
            normal = { Color = Color.yellow }
        };
    }
}
```

---

## Проверь себя

### Теоретические вопросы

**1.** В чём принципиальное отличие event-driven подхода New Input System от polling в старом Input Manager?

> _Ожидаемый ответ:_ Старый `Input.GetKey()` проверяется **каждый кадр** в `Update()` независимо от того, нажата кнопка или нет. New Input System использует **события** — код в `OnJumpPerformed()` вызывается **только** когда произошло нажатие. Это экономит ресурсы и делает код чище: логика не смешана с циклом обновления.

---

**2.** Чем отличаются `performed`, `started` и `canceled` для Button Action?

> _Ожидаемый ответ:_
> 
> - `started` — кнопка **начала** нажиматься (значение превысило порог начала)
> - `performed` — кнопка **нажата** полностью (прошла порог срабатывания)
> - `canceled` — кнопка **отпущена** (значение вернулось к нулю)
> 
> Для простых нажатий используют `performed`. `started`/`canceled` нужны для зарядки атаки, переменной высоты прыжка и т.д.

---

**3.** Зачем нужен сгенерированный C# класс из Input Actions Asset? Чем он лучше строковых имён?

> _Ожидаемый ответ:_ Сгенерированный класс даёт **типобезопасность** и **автодополнение**. Вместо `_input.asset.FindAction("Playr/Jmp")` (опечатка обнаружится только в Runtime) — `_input.Player.Jump` (ошибка в имени обнаружится на **этапе компиляции**). Также сгенерированный класс быстрее, потому что не ищет Action по строке каждый раз.

---

**4.** Что произойдёт если не вызвать `_inputActions.Dispose()` в `OnDestroy`?

> _Ожидаемый ответ:_ **Утечка памяти и нативных ресурсов.** Input System использует нативные буферы для хранения состояния устройств. Без `Dispose()` эти буферы не освобождаются. Также могут остаться **висячие подписки на события**, которые будут вызываться на уже уничтоженных объектах, вызывая исключения `MissingReferenceException`.

---

**5.** Вы хотите при входе в диалог с NPC переключить управление: отключить движение игрока, включить навигацию по меню диалога. Как это сделать через Input System?

> _Ожидаемый ответ:_ Через переключение **Action Maps**. В `.inputactions` ассете создать два Action Map: `Player` (движение, прыжок) и `Dialogue` (Next, Skip, Exit). При начале диалога:
> 
> 
> 
> ```csharp
> _input.Player.Disable();
> _input.Dialogue.Enable();
> ```
> 
> При завершении — наоборот. Это гарантирует что кнопки не будут обрабатываться одновременно обеими системами.

---

### Практические задания

**Задание 1** ⭐

Добавьте в `PlayerController` действие `Attack` (ЛКМ + `buttonEast` геймпада) с тремя фазами:

- `started` — начать замах
- `performed` — нанести удар
- `canceled` — прервать если кнопка отпущена до `performed`

---

**Задание 2** ⭐⭐

Реализуйте **переменную высоту прыжка**: если игрок отпускает кнопку прыжка раньше — персонаж прыгает ниже. Подсказка: в `canceled` если `_verticalVelocity.y > 0` — умножьте её на `0.5f`.

---

**Задание 3** ⭐⭐⭐

Создайте систему **простого переназначения клавиш**:

- Кнопка в UI запускает `StartRebinding("Jump")`
- Во время ожидания показывает текст "Нажмите любую кнопку..."
- После назначения сохраняет в `PlayerPrefs` и обновляет текст подсказки
- Кнопка "Сброс" возвращает умолчания

---

**Задание 4** ⭐⭐⭐⭐

Реализуйте **локальный мультиплеер** для двух игроков:

- Используйте `PlayerInputManager` компонент
- Игрок 1: клавиатура (WASD + Space)
- Игрок 2: геймпад (стик + A)
- При подключении второго геймпада автоматически создаётся второй персонаж через `PlayerInputManager.EnableJoining()`

---

### Чеклист при использовании New Input System



```csharp
✅ Active Input Handling переключён на "Input System Package"
✅ Input Actions Asset создан и настроен
✅ Для всех Actions назначены привязки минимум для 2 устройств
✅ C# класс сгенерирован (Generate C# Class → Apply)
✅ _inputActions.Dispose() вызывается в OnDestroy
✅ Отписка от всех событий в OnDisable (не только в OnDestroy)
✅ Нет вызовов Q<T>() в Update для поиска Action (только кэш)
✅ Action Maps переключаются при смене контекста (геймплей / меню / диалог)
✅ Переназначения сохраняются через SaveBindingOverridesAsJson
✅ Отладочные OnGUI методы обёрнуты в #if UNITY_EDITOR
```

---

> **Итог:** New Input System — это значительный шаг вперёд по сравнению с Legacy Input Manager. Ключевые концепции просты: **Actions** абстрагируют управление от устройств, **события** заменяют постоянный опрос в `Update()`, а **сгенерированный C# класс** делает код типобезопасным и удобным для рефакторинга. Один раз настроив Input Actions Asset, вы автоматически получаете поддержку клавиатуры, геймпада и мобильного тача без изменения игровой логики.