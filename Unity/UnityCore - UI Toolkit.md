## Содержание

- [Введение](#%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5)
	- [История вопроса](#%D0%98%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F%20%D0%B2%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D0%B0)
	- [Сравнительная таблица](#%D0%A1%D1%80%D0%B0%D0%B2%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0)
	- [Когда использовать что](#%D0%9A%D0%BE%D0%B3%D0%B4%D0%B0%20%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%20%D1%87%D1%82%D0%BE)
- [Структура папок](#%D0%A1%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D0%BF%D0%B0%D0%BF%D0%BE%D0%BA)
- [Создание UI Document](#%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20UI%20Document)
	- [Шаг 1 — Создание UXML файла](#%D0%A8%D0%B0%D0%B3%201%20%E2%80%94%20%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20UXML%20%D1%84%D0%B0%D0%B9%D0%BB%D0%B0)
	- [Шаг 2 — Создание UI Document компонента на сцене](#%D0%A8%D0%B0%D0%B3%202%20%E2%80%94%20%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20UI%20Document%20%D0%BA%D0%BE%D0%BC%D0%BF%D0%BE%D0%BD%D0%B5%D0%BD%D1%82%D0%B0%20%D0%BD%D0%B0%20%D1%81%D1%86%D0%B5%D0%BD%D0%B5)
	- [Шаг 3 — Создание Panel Settings](#%D0%A8%D0%B0%D0%B3%203%20%E2%80%94%20%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20Panel%20Settings)
	- [Шаг 4 — UI Builder (визуальный редактор)](#%D0%A8%D0%B0%D0%B3%204%20%E2%80%94%20UI%20Builder%20(%D0%B2%D0%B8%D0%B7%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D1%80%D0%B5%D0%B4%D0%B0%D0%BA%D1%82%D0%BE%D1%80))
- [UXML](#UXML)
	- [Базовая структура UXML файла](#%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D1%8F%20%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0%20UXML%20%D1%84%D0%B0%D0%B9%D0%BB%D0%B0)
	- [Основные атрибуты элементов](#%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5%20%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%82%D1%8B%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2)
	- [VisualElement — базовый контейнер](#VisualElement%20%E2%80%94%20%D0%B1%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%B9%D0%BD%D0%B5%D1%80)
	- [Label — текстовый элемент](#Label%20%E2%80%94%20%D1%82%D0%B5%D0%BA%D1%81%D1%82%D0%BE%D0%B2%D1%8B%D0%B9%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82)
	- [Button — кнопка](#Button%20%E2%80%94%20%D0%BA%D0%BD%D0%BE%D0%BF%D0%BA%D0%B0)
	- [ProgressBar — полоса прогресса](#ProgressBar%20%E2%80%94%20%D0%BF%D0%BE%D0%BB%D0%BE%D1%81%D0%B0%20%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B0)
	- [Field — поле ввода](#Field%20%E2%80%94%20%D0%BF%D0%BE%D0%BB%D0%B5%20%D0%B2%D0%B2%D0%BE%D0%B4%D0%B0)
	- [Полный пример UXML — простое меню](#%D0%9F%D0%BE%D0%BB%D0%BD%D1%8B%D0%B9%20%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%20UXML%20%E2%80%94%20%D0%BF%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%B5%20%D0%BC%D0%B5%D0%BD%D1%8E)
- [USS](#USS)
	- [Базовый синтаксис USS](#%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B9%20%D1%81%D0%B8%D0%BD%D1%82%D0%B0%D0%BA%D1%81%D0%B8%D1%81%20USS)
	- [CSS-переменные в USS](#CSS-%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5%20%D0%B2%20USS)
	- [Псевдоклассы — интерактивность](#%D0%9F%D1%81%D0%B5%D0%B2%D0%B4%D0%BE%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D1%8B%20%E2%80%94%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D1%81%D1%82%D1%8C)
	- [Полный USS файл для HUD](#%D0%9F%D0%BE%D0%BB%D0%BD%D1%8B%D0%B9%20USS%20%D1%84%D0%B0%D0%B9%D0%BB%20%D0%B4%D0%BB%D1%8F%20HUD)
	- [Отличия USS от CSS](#%D0%9E%D1%82%D0%BB%D0%B8%D1%87%D0%B8%D1%8F%20USS%20%D0%BE%D1%82%20CSS)
- [Подключение через ](#%D0%9F%D0%BE%D0%B4%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20)
	- [Получение корневого элемента](#%D0%9F%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BA%D0%BE%D1%80%D0%BD%D0%B5%D0%B2%D0%BE%D0%B3%D0%BE%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D0%B0)
	- [Query — поиск элементов](#Query%20%E2%80%94%20%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2)
	- [Кэширование ссылок на элементы](#%D0%9A%D1%8D%D1%88%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%81%D1%81%D1%8B%D0%BB%D0%BE%D0%BA%20%D0%BD%D0%B0%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B)
- [Работа с элементами](#%D0%A0%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%20%D1%81%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BC%D0%B8)
	- [RegisterCallback — подписка на события](#RegisterCallback%20%E2%80%94%20%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%BA%D0%B0%20%D0%BD%D0%B0%20%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F)
	- [Управление классами и стилями](#%D0%A3%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B0%D0%BC%D0%B8%20%D0%B8%20%D1%81%D1%82%D0%B8%D0%BB%D1%8F%D0%BC%D0%B8)
- [Flex Layout](#Flex%20Layout)
	- [Основы Flexbox в USS](#%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B%20Flexbox%20%D0%B2%20USS)
	- [Практические примеры макетов](#%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B%20%D0%BC%D0%B0%D0%BA%D0%B5%D1%82%D0%BE%D0%B2)
- [Практическое задание](#%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5)
	- [Шаг 1 — UXML разметка HUD](#%D0%A8%D0%B0%D0%B3%201%20%E2%80%94%20UXML%20%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%82%D0%BA%D0%B0%20HUD)
	- [Шаг 2 — USS стили HUD](#%D0%A8%D0%B0%D0%B3%202%20%E2%80%94%20USS%20%D1%81%D1%82%D0%B8%D0%BB%D0%B8%20HUD)
	- [Шаг 3 — Модель данных с R3 ReactiveProperty](#%D0%A8%D0%B0%D0%B3%203%20%E2%80%94%20%D0%9C%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85%20%D1%81%20R3%20ReactiveProperty)
	- [Шаг 4 — HUD Controller (View)](#%D0%A8%D0%B0%D0%B3%204%20%E2%80%94%20HUD%20Controller%20(View))
	- [Шаг 5 — Пример интеграции с игровой логикой](#%D0%A8%D0%B0%D0%B3%205%20%E2%80%94%20%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80%20%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8%20%D1%81%20%D0%B8%D0%B3%D1%80%D0%BE%D0%B2%D0%BE%D0%B9%20%D0%BB%D0%BE%D0%B3%D0%B8%D0%BA%D0%BE%D0%B9)
- [Проверь себя](#%D0%9F%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D1%8C%20%D1%81%D0%B5%D0%B1%D1%8F)
	- [Теоретические вопросы](#%D0%A2%D0%B5%D0%BE%D1%80%D0%B5%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%B2%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D1%8B)
	- [Практические задания](#%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F)
	- [Чеклист перед сдачей проекта](#%D0%A7%D0%B5%D0%BA%D0%BB%D0%B8%D1%81%D1%82%20%D0%BF%D0%B5%D1%80%D0%B5%D0%B4%20%D1%81%D0%B4%D0%B0%D1%87%D0%B5%D0%B9%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)


---

## Введение

### История вопроса

Unity долгое время имел только одну систему UI — **Canvas (uGUI)**. Она работала, но имела фундаментальные проблемы: всё строилось на GameObject-ах, каждая кнопка — это отдельный объект в иерархии, производительность падала при сотнях элементов, а масштабирование под разные разрешения превращалось в боль.

**UI Toolkit** (ранее UIElements) — это современная система UI в Unity, вдохновлённая веб-технологиями. Вместо GameObject-иерархии — декларативная разметка через XML. Вместо компонентов со свойствами — CSS-подобные стили.

### Сравнительная таблица

|Критерий|Canvas (uGUI)|UI Toolkit|
|---|---|---|
|Технология|GameObject + компоненты|UXML + USS (XML/CSS-подход)|
|Производительность|Падает при сотнях элементов|Оптимизирован для большого числа элементов|
|Редактирование стилей|Через Inspector|USS файлы (как CSS)|
|Анимация UI|Animator / DOTween|Transitions в USS + C#|
|Мировой UI (3D)|✅ World Space Canvas|⚠️ Ограниченная поддержка|
|Runtime поддержка|✅ Полная|✅ Полная (Unity 2021.2+)|
|Editor расширения|IMGUI / EditorGUILayout|✅ Рекомендуется UI Toolkit|
|Обучаемость|Проще для новичков|Требует знания XML/CSS концепций|
|Переиспользование стилей|Сложно|✅ USS темы и переменные|

### Когда использовать что



```csharp
Используйте Canvas (uGUI) если:
├── Проект уже использует uGUI и рефакторинг не оправдан
├── Нужен UI в мировом пространстве (World Space — хэлсбары над врагами)
├── Команда не знакома с веб-технологиями
└── Простой проект с небольшим количеством UI элементов

Используйте UI Toolkit если:
├── Новый проект с нуля
├── Сложные, многоэкранные интерфейсы (главное меню, инвентарь)
├── Нужно переиспользовать стили между экранами
├── Разработка Editor-расширений (инструменты, окна)
├── Команда знакома с HTML/CSS
└── Важна производительность при большом числе элементов
```

> **Важно:** Начиная с Unity 2021.2, UI Toolkit полностью поддерживается в Runtime. В более ранних версиях — только для Editor UI.

---

## Структура папок

Хорошо организованный проект с UI Toolkit имеет чёткую структуру. Придерживайтесь её с самого начала:



```csharp
Assets/
└── UI/
    ├── Documents/              ← UXML файлы (разметка)
    │   ├── HUD.uxml
    │   ├── MainMenu.uxml
    │   ├── PauseMenu.uxml
    │   ├── Inventory.uxml
    │   └── Components/        ← переиспользуемые компоненты
    │       ├── HealthBar.uxml
    │       ├── ItemSlot.uxml
    │       └── DialogBox.uxml
    │
    ├── Styles/                 ← USS файлы (стили)
    │   ├── Variables.uss       ← CSS-переменные (цвета, размеры)
    │   ├── Common.uss          ← общие стили
    │   ├── HUD.uss
    │   ├── MainMenu.uss
    │   └── Themes/
    │       ├── Dark.uss
    │       └── Light.uss
    │
    ├── Fonts/                  ← шрифты (Font Asset)
    │   ├── MainFont.ttf
    │   └── IconFont.ttf
    │
    ├── Images/                 ← спрайты для UI
    │   ├── Icons/
    │   ├── Backgrounds/
    │   └── Buttons/
    │
    └── Scripts/                ← C# контроллеры для UI
        ├── HUDController.cs
        ├── MainMenuController.cs
        └── PauseMenuController.cs
```

---

## Создание UI Document

### Шаг 1 — Создание UXML файла

В Project окне: **правая кнопка мыши → Create → UI Toolkit → UI Document**

Это создаст файл с расширением `.uxml`.

### Шаг 2 — Создание UI Document компонента на сцене



```csharp
1. Создайте пустой GameObject: GameObject → Create Empty
2. Назовите его "UIDocument" или "HUD"
3. Add Component → UI → UI Document
```

Компонент **UI Document** имеет следующие параметры:



```csharp
UI Document (Component)
├── Panel Settings    ← обязательный ассет, управляет рендерингом
│   ├── Scale Mode: Scale With Screen Size
│   ├── Reference Resolution: 1920x1080
│   └── Screen Match Mode: Match Width Or Height
│
├── Source Asset      ← UXML файл (ваш интерфейс)
│
└── Sort Order: 0     ← порядок отрисовки (как Layer Order в Canvas)
```

### Шаг 3 — Создание Panel Settings

**Create → UI Toolkit → Panel Settings Asset**



```csharp
Panel Settings
├── Theme Style Sheet     ← базовая USS тема (UnityDefaultRuntimeTheme)
├── Target ure        ← если нужно рендерить в Renderure
├── Scale Mode
│   ├── Constant Pixel Size  — фиксированный размер в пикселях
│   ├── Constant Physical Size — фиксированный физический размер
│   └── Scale With Screen Size — масштабировать под экран ✅ рекомендуется
├── Scale: 1
├── Reference Resolution: 1920 x 1080
└── Screen Match Mode: Match Width Or Height (0.5)
```

### Шаг 4 — UI Builder (визуальный редактор)

Откройте визуальный редактор: **Window → UI Toolkit → UI Builder**



```csharp
UI Builder Layout:
┌─────────────────────────────────────────────────────┐
│  StyleSheets │ Hierarchy │      Viewport      │ Inspector │
│              │           │                    │           │
│  .uss файлы  │ Дерево    │  Предпросмотр UI   │ Свойства  │
│              │ элементов │                    │ элемента  │
│              │           │                    │           │
│  Library     │           │                    │           │
│  (элементы   │           │                    │           │
│   для вставки│           │                    │           │
└─────────────────────────────────────────────────────┘
```

---

## UXML

**UXML** (Unity XML) — это язык разметки для описания структуры UI. Если вы знакомы с HTML, синтаксис покажется очень знакомым.

### Базовая структура UXML файла

XML

```csharp
<?xml version="1.0" encoding="utf-8"?>
<!-- Корневой элемент всегда UXML -->
<ui:UXML
    xmlns:ui="UnityEngine.UIElements"
    xmlns:uie="UnityEditor.UIElements"
    xsi="http://www.w3.org/2001/XMLSchema-instance"
    engine="UnityEngine.UIElements"
    editor="UnityEditor.UIElements"
    noNamespaceSchemaLocation="../../UIElementsSchema/UIElements.xsd"
    editor-extension-mode="False">

    <!-- Подключение стилей -->
    <Style src="project://database/Assets/UI/Styles/HUD.uss" />

    <!-- Корневой контейнер -->
    <ui:VisualElement name="root" class="root-container">

        <!-- Ваши элементы здесь -->

    </ui:VisualElement>

</ui:UXML>
```

### Основные атрибуты элементов

XML

```csharp
<!-- Каждый элемент может иметь: -->
<ui:VisualElement
    name="my-element"          <!-- уникальный ID (как id в HTML) -->
    class="class1 class2"      <!-- CSS классы (через пробел) -->
    style="color: red;"        <!-- инлайн стили -->
    tooltip="Подсказка"        <!-- всплывающая подсказка -->
    focusable="true"           <!-- может получать фокус -->
    picking-mode="Position"    <!-- реакция на клики: Position/Ignore -->
    usage-hints="DynamicColor" <!-- подсказки для оптимизации -->
/>
```

### VisualElement — базовый контейнер

`VisualElement` — это строительный блок UI Toolkit. Аналог `<div>` в HTML.

XML

```csharp
<?xml version="1.0" encoding="utf-8"?>
<ui:UXML xmlns:ui="UnityEngine.UIElements">

    <!-- Простой контейнер -->
    <ui:VisualElement name="panel" class="panel">

        <!-- Вложенные элементы -->
        <ui:VisualElement name="header" class="header">
            <!-- заголовок -->
        </ui:VisualElement>

        <ui:VisualElement name="content" class="content">
            <!-- содержимое -->
        </ui:VisualElement>

        <ui:VisualElement name="footer" class="footer">
            <!-- подвал -->
        </ui:VisualElement>

    </ui:VisualElement>

</ui:UXML>
```

### Label — текстовый элемент

XML

```csharp
<!-- Базовый Label -->
<ui:Label
    name="title-label"
    ="Привет, мир!"
    class="title"
/>

<!-- Label с переносом строк -->
<ui:Label
    name="description"
    ="Длинный текст описания который может переноситься на следующую строку"
    class="description"
    style="white-space: normal;"
/>

<!-- Label для динамических значений (текст обновляется из кода) -->
<ui:Label name="coin-counter" ="💰 0" class="counter-label"/>
<ui:Label name="score-label" ="Счёт: 0" class="score-label"/>
```

### Button — кнопка

XML

```csharp
<!-- Простая кнопка -->
<ui:Button
    name="pause-button"
    ="⏸ Пауза"
    class="btn btn-primary"
/>

<!-- Кнопка без текста (иконка) -->
<ui:Button name="close-button" class="btn-icon">
    <!-- Вложенный элемент-иконка -->
    <ui:VisualElement class="icon icon-close"/>
</ui:Button>

<!-- Кнопка с текстом и иконкой -->
<ui:Button name="play-button" class="btn btn-large">
    <ui:VisualElement class="icon icon-play"/>
    <ui:Label ="Играть" class="btn-label"/>
</ui:Button>

<!-- Кнопка-переключатель -->
<ui:Toggle
    name="music-toggle"
    label="Музыка"
    class="settings-toggle"
    value="true"
/>
```

### ProgressBar — полоса прогресса

XML

```csharp
<!-- HP бар -->
<ui:ProgressBar
    name="hp-bar"
    title="HP"
    value="100"
    high-value="100"
    low-value="0"
    class="hp-bar"
/>

<!-- Бар опыта -->
<ui:ProgressBar
    name="exp-bar"
    title=""
    value="0"
    high-value="1000"
    class="exp-bar"
/>

<!-- Кастомный составной бар (для большего контроля) -->
<ui:VisualElement name="custom-bar-container" class="bar-container">
    <ui:VisualElement name="custom-bar-fill" class="bar-fill"/>
    <ui:Label name="custom-bar-label" ="100 / 100" class="bar-label"/>
</ui:VisualElement>
```

### Field — поле ввода

XML

```csharp
<!-- Обычный Field -->
<ui:Field
    name="player-name-field"
    label="Имя игрока"
    value="Герой"
    class="input-field"
    max-length="20"
/>

<!-- Поле для пароля -->
<ui:Field
    name="password-field"
    label="Пароль"
    is-password-field="true"
    class="input-field"
/>

<!-- Многострочное поле -->
<ui:Field
    name="description-field"
    label="Описание"
    multiline="true"
    class="input-field area"
    style="height: 100px;"
/>

<!-- Числовые поля -->
<ui:IntegerField
    name="quantity-field"
    label="Количество"
    value="1"
    class="input-field"
/>

<ui:FloatField
    name="speed-field"
    label="Скорость"
    value="5.0"
    class="input-field"
/>
```

### Полный пример UXML — простое меню

XML

```csharp
<?xml version="1.0" encoding="utf-8"?>
<ui:UXML xmlns:ui="UnityEngine.UIElements">

    <Style src="project://database/Assets/UI/Styles/MainMenu.uss"/>

    <!-- Главный контейнер -->
    <ui:VisualElement name="main-container" class="main-container">

        <!-- Фоновое изображение -->
        <ui:VisualElement name="background" class="menu-background"/>

        <!-- Центральная панель -->
        <ui:VisualElement name="menu-panel" class="menu-panel">

            <!-- Логотип / Заголовок -->
            <ui:VisualElement name="logo-container" class="logo-container">
                <ui:Label name="game-title" ="МОЯ ИГРА" class="game-title"/>
                <ui:Label name="game-subtitle" ="Приключение начинается" class="subtitle"/>
            </ui:VisualElement>

            <!-- Кнопки меню -->
            <ui:VisualElement name="buttons-container" class="buttons-container">

                <ui:Button name="btn-play" ="▶ Играть" class="menu-btn menu-btn--primary"/>
                <ui:Button name="btn-continue" ="↺ Продолжить" class="menu-btn"/>
                <ui:Button name="btn-settings" ="⚙ Настройки" class="menu-btn"/>
                <ui:Button name="btn-quit" ="✕ Выход" class="menu-btn menu-btn--danger"/>

            </ui:VisualElement>

            <!-- Версия игры -->
            <ui:Label name="version-label" ="v1.0.0" class="version-label"/>

        </ui:VisualElement>

    </ui:VisualElement>

</ui:UXML>
```

---

## USS

**USS** (Unity Style Sheets) — это система стилей, вдохновлённая CSS. Если вы знаете CSS — освоите USS за час. Синтаксис почти идентичен, но есть ряд отличий.

### Базовый синтаксис USS

CSS

```csharp
/* Файл: Assets/UI/Styles/Common.uss */

/* ========================
   Селекторы
======================== */

/* По имени элемента (#name как в CSS) */
#hp-bar {
    width: 200px;
    height: 20px;
}

/* По классу (.class как в CSS) */
.menu-btn {
    font-size: 18px;
    margin: 5px;
    padding: 10px 20px;
}

/* По типу элемента */
Button {
    cursor: link;
}

Label {
    -unity-font-style: bold;
}

/* Вложенные селекторы */
.menu-panel .menu-btn {
    width: 250px;
}

/* Несколько классов одновременно */
.btn.btn--primary {
    background-color: rgb(52, 152, 219);
}
```

### CSS-переменные в USS

CSS

```csharp
/* Файл: Assets/UI/Styles/Variables.uss */

/* Переменные объявляются в :root */
:root {
    /* Цветовая палитра */
    --color-primary: rgb(52, 152, 219);
    --color-primary-dark: rgb(41, 128, 185);
    --color-secondary: rgb(46, 204, 113);
    --color-danger: rgb(231, 76, 60);
    --color-danger-dark: rgb(192, 57, 43);
    --color-warning: rgb(243, 156, 18);
    --color-dark: rgb(20, 20, 30);
    --color-dark-transparent: rgba(20, 20, 30, 0.85);
    --color-: rgb(236, 240, 241);
    --color--secondary: rgb(149, 165, 166);

    /* Размеры */
    --font-size-small: 12px;
    --font-size-normal: 16px;
    --font-size-large: 24px;
    --font-size-title: 48px;

    /* Отступы */
    --spacing-xs: 4px;
    --spacing-sm: 8px;
    --spacing-md: 16px;
    --spacing-lg: 24px;
    --spacing-xl: 40px;

    /* Скругления */
    --border-radius-sm: 4px;
    --border-radius-md: 8px;
    --border-radius-lg: 16px;
    --border-radius-full: 100px;
}
```

### Псевдоклассы — интерактивность

CSS

```csharp
/* Файл: Assets/UI/Styles/Buttons.uss */

/* Базовая кнопка */
.menu-btn {
    background-color: var(--color-primary);
    color: var(--color-);
    font-size: var(--font-size-large);
    border-radius: var(--border-radius-md);
    border-width: 0;
    padding: 12px 32px;
    margin: 6px 0;
    width: 280px;

    /* Плавные переходы */
    transition-property: background-color, scale;
    transition-duration: 0.15s;
    transition-timing-function: ease-out;
}

/* :hover — курсор над кнопкой */
.menu-btn:hover {
    background-color: var(--color-primary-dark);
    scale: 1.02;
}

/* :active — кнопка нажата */
.menu-btn:active {
    background-color: rgb(31, 97, 141);
    scale: 0.98;
}

/* :focus — кнопка в фокусе (Tab навигация) */
.menu-btn:focus {
    border-width: 2px;
    border-color: white;
}

/* :disabled — кнопка недоступна */
.menu-btn:disabled {
    background-color: rgb(100, 100, 100);
    color: rgb(160, 160, 160);
    opacity: 0.6;
}

/* :checked — для Toggle элементов */
.settings-toggle:checked {
    background-color: var(--color-secondary);
}

/* Кнопка опасного действия */
.menu-btn--danger {
    background-color: var(--color-danger);
}

.menu-btn--danger:hover {
    background-color: var(--color-danger-dark);
}
```

### Полный USS файл для HUD

CSS

```csharp
/* Файл: Assets/UI/Styles/HUD.uss */

/* Импорт переменных */
@import url("Variables.uss");

/* ========================
   Корневой контейнер
======================== */
.hud-root {
    width: 100%;
    height: 100%;
    position: absolute;

    /* Flexbox для позиционирования */
    flex-direction: column;
    justify-content: space-between;
    padding: var(--spacing-md);
}

/* ========================
   Верхняя панель HUD
======================== */
.hud-top-panel {
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-start;
}

/* ========================
   Блок здоровья (левый верхний угол)
======================== */
.health-container {
    flex-direction: column;
    min-width: 250px;
}

.health-label {
    color: var(--color-);
    font-size: var(--font-size-small);
    margin-bottom: var(--spacing-xs);
    -unity-font-style: bold;
}

/* Стили для ProgressBar */
.hp-bar {
    width: 250px;
    height: 22px;
    border-radius: var(--border-radius-full);
    border-width: 2px;
    border-color: rgba(0, 0, 0, 0.5);
}

/* Фон прогресс-бара */
.hp-bar > .unity-progress-bar__background {
    background-color: rgba(0, 0, 0, 0.4);
    border-radius: var(--border-radius-full);
}

/* Заполненная часть прогресс-бара */
.hp-bar > .unity-progress-bar__progress {
    background-color: var(--color-danger);
    border-radius: var(--border-radius-full);

    /* Переход при изменении HP */
    transition-property: width;
    transition-duration: 0.3s;
    transition-timing-function: ease-out;
}

/* Текст внутри прогресс-бара */
.hp-bar > .unity-progress-bar__title {
    color: white;
    font-size: 11px;
    -unity-font-style: bold;
}

/* ========================
   Счётчик монет (правый верхний угол)
======================== */
.coin-container {
    flex-direction: row;
    align-items: center;
    background-color: var(--color-dark-transparent);
    padding: var(--spacing-sm) var(--spacing-md);
    border-radius: var(--border-radius-full);
}

.coin-icon {
    width: 24px;
    height: 24px;
    margin-right: var(--spacing-xs);
    /* background-image задаётся через C# или инлайн */
}

.coin-label {
    color: var(--color-warning);
    font-size: var(--font-size-large);
    -unity-font-style: bold;
}

/* ========================
   Кнопка паузы
======================== */
.pause-button {
    width: 48px;
    height: 48px;
    border-radius: var(--border-radius-md);
    background-color: var(--color-dark-transparent);
    border-width: 1px;
    border-color: rgba(255, 255, 255, 0.2);
    font-size: 22px;
    color: white;

    transition-property: background-color, scale;
    transition-duration: 0.1s;
}

.pause-button:hover {
    background-color: rgba(255, 255, 255, 0.15);
    scale: 1.1;
}

.pause-button:active {
    scale: 0.9;
}

/* ========================
   Нижняя панель HUD
======================== */
.hud-bottom-panel {
    flex-direction: row;
    justify-content: flex-end;
    align-items: flex-end;
}

/* ========================
   Уведомления / Флэш-сообщения
======================== */
.notification {
    position: absolute;
    top: 30%;
    left: 50%;
    translate: -50% 0;
    background-color: var(--color-dark-transparent);
    padding: var(--spacing-md) var(--spacing-xl);
    border-radius: var(--border-radius-lg);
    border-width: 1px;
    border-color: var(--color-primary);
    opacity: 0;

    transition-property: opacity;
    transition-duration: 0.3s;
}

.notification--visible {
    opacity: 1;
}

.notification__ {
    color: var(--color-);
    font-size: var(--font-size-large);
    -unity--align: upper-center;
}
```

### Отличия USS от CSS

CSS

```csharp
/* В CSS это работает, в USS — нет или по-другому */

/* ❌ USS не поддерживает */
/* display: grid */
/* -shadow */
/* box-shadow (только border) */
/* animation @keyframes (только transition) */

/* ✅ USS специфичные свойства */

.element {
    /* Unity-специфичные свойства с префиксом -unity- */
    -unity-font-style: bold;           /* жирный, курсив */
    -unity--align: upper-center;   /* выравнивание текста */
    -unity-background-scale-mode: stretch-to-fill; /* масштаб фона */
    -unity-overflow-clip-box: content-box;

    /* Позиционирование */
    position: absolute;   /* absolute или relative */
    left: 10px;
    top: 10px;

    /* Размеры могут быть в px, %, или auto */
    width: 100%;
    height: auto;
    min-width: 100px;
    max-width: 500px;

    /* Цвета: rgb(), rgba(), #hex, или именованные Unity-цвета */
    background-color: rgb(52, 152, 219);
    color: rgba(255, 255, 255, 0.8);
    border-color: #2ecc71;

    /* Изображения */
    background-image: url("project://database/Assets/UI/Images/bg.png");
}
```

---

## Подключение через 

### Получение корневого элемента



```csharp
using UnityEngine;
using UnityEngine.UIElements;

public class MenuController : MonoBehaviour
{
    // Ссылка на компонент UI Document
    [SerializeField] private UIDocument uiDocument;

    // Корневой элемент — точка входа ко всему UI
    private VisualElement _root;

    void Awake()
    {
        // Способ 1: через SerializeField (рекомендуется)
        _root = uiDocument.rootVisualElement;

        // Способ 2: найти на объекте
        var doc = GetComponent<UIDocument>();
        _root = doc.rootVisualElement;
    }
}
```

### Query — поиск элементов



```csharp
using UnityEngine;
using UnityEngine.UIElements;

public class UIQueryExamples : MonoBehaviour
{
    [SerializeField] private UIDocument uiDocument;
    private VisualElement _root;

    void Awake()
    {
        _root = uiDocument.rootVisualElement;

        FindElementsExamples();
    }

    void FindElementsExamples()
    {
        // === Поиск по имени (name="...") ===

        // Q<T>() — найти первый элемент типа T с именем
        var hpBar = _root.Q<ProgressBar>("hp-bar");
        var coinLabel = _root.Q<Label>("coin-counter");
        var pauseBtn = _root.Q<Button>("pause-button");

        // Q() без типа — возвращает VisualElement
        var container = _root.Q("health-container");

        // === Поиск по классу ===
        var primaryBtn = _root.Q<Button>(className: "menu-btn--primary");

        // === Поиск нескольких элементов (QueryAll) ===
        // Возвращает UQueryBuilder — ленивый запрос
        var allButtons = _root.Query<Button>().ToList();
        var menuButtons = _root.Query<Button>(className: "menu-btn").ToList();
        var allLabels = _root.Query<Label>().ToList();

        // === Итерация ===
        _root.Query<Button>().ForEach(btn => {
            Debug.Log($"Кнопка: {btn.name}");
        });

        // === Поиск внутри элемента ===
        var panel = _root.Q("menu-panel");
        var btnInsidePanel = panel?.Q<Button>("btn-play");

        // === Безопасный поиск с проверкой ===
        var label = _root.Q<Label>("score-label");
        if (label == null)
        {
            Debug.LogError("Элемент 'score-label' не найден! " +
                           "Проверьте name в UXML.");
            return;
        }

        label. = "Счёт: 100";
    }
}
```

### Кэширование ссылок на элементы



```csharp
using UnityEngine;
using UnityEngine.UIElements;

/// <summary>
/// Правильный подход: кэшировать ссылки в Awake/OnEnable,
/// НЕ вызывать Q() каждый кадр
/// </summary>
public class HUDView : MonoBehaviour
{
    [SerializeField] private UIDocument uiDocument;

    // Кэшированные ссылки на элементы UI
    // Объявляем с подчёркивания для приватных полей
    private ProgressBar _hpBar;
    private Label _coinLabel;
    private Label _scoreLabel;
    private Button _pauseButton;
    private VisualElement _notification;
    private Label _notification;

    void Awake()
    {
        var root = uiDocument.rootVisualElement;
        CacheElements(root);
    }

    private void CacheElements(VisualElement root)
    {
        // Получаем все ссылки один раз при инициализации
        _hpBar = root.Q<ProgressBar>("hp-bar");
        _coinLabel = root.Q<Label>("coin-counter");
        _scoreLabel = root.Q<Label>("score-label");
        _pauseButton = root.Q<Button>("pause-button");
        _notification = root.Q("notification");
        _notification = root.Q<Label>("notification-");

        ValidateElements();
    }

    private void ValidateElements()
    {
        // В разработке проверяем что всё найдено
#if UNITY_EDITOR
        if (_hpBar == null) Debug.LogError("[HUDView] hp-bar не найден!");
        if (_coinLabel == null) Debug.LogError("[HUDView] coin-counter не найден!");
        if (_scoreLabel == null) Debug.LogError("[HUDView] score-label не найден!");
        if (_pauseButton == null) Debug.LogError("[HUDView] pause-button не найден!");
#endif
    }

    // Публичные методы для обновления UI
    public void SetHP(float current, float max)
    {
        if (_hpBar == null) return;
        _hpBar.value = current;
        _hpBar.highValue = max;
        _hpBar.title = $"{(int)current} / {(int)max}";
    }

    public void SetCoins(int coins)
    {
        if (_coinLabel == null) return;
        _coinLabel. = $"💰 {coins}";
    }

    public void SetScore(int score)
    {
        if (_scoreLabel == null) return;
        _scoreLabel. = $"Счёт: {score:N0}";
    }
}
```

---

## Работа с элементами

### RegisterCallback — подписка на события



```csharp
using UnityEngine;
using UnityEngine.UIElements;

public class EventHandlingExamples : MonoBehaviour
{
    [SerializeField] private UIDocument uiDocument;

    void Awake()
    {
        var root = uiDocument.rootVisualElement;
        RegisterEvents(root);
    }

    void RegisterEvents(VisualElement root)
    {
        // === Button.clicked — самый простой способ для кнопок ===
        var playButton = root.Q<Button>("btn-play");
        playButton.clicked += OnPlayButtonClicked;

        // === RegisterCallback — универсальный способ ===

        // Клик мышью
        var pauseBtn = root.Q<Button>("pause-button");
        pauseBtn.RegisterCallback<ClickEvent>(OnPauseClicked);

        // Наведение курсора
        var anyElement = root.Q("health-container");
        anyElement.RegisterCallback<MouseEnterEvent>(OnMouseEnter);
        anyElement.RegisterCallback<MouseLeaveEvent>(OnMouseLeave);

        // Нажатие клавиши
        root.RegisterCallback<KeyDownEvent>(OnKeyDown);

        // Изменение значения Field
        var nameField = root.Q<Field>("player-name");
        nameField?.RegisterCallback<ChangeEvent<string>>(OnNameChanged);

        // Изменение значения Toggle
        var musicToggle = root.Q<Toggle>("music-toggle");
        musicToggle?.RegisterCallback<ChangeEvent<bool>>(OnMusicToggled);

        // Изменение значения IntegerField
        var quantityField = root.Q<IntegerField>("quantity");
        quantityField?.RegisterCallback<ChangeEvent<int>>(OnQuantityChanged);

        // Фокус и потеря фокуса
        var inputField = root.Q<Field>("search-field");
        inputField?.RegisterCallback<FocusEvent>(OnFieldFocused);
        inputField?.RegisterCallback<BlurEvent>(OnFieldBlurred);

        // Указатель (универсально для мыши и тач)
        var card = root.Q("item-card");
        card?.RegisterCallback<PointerDownEvent>(OnPointerDown);
        card?.RegisterCallback<PointerUpEvent>(OnPointerUp);
        card?.RegisterCallback<PointerMoveEvent>(OnPointerMove);
    }

    // Обработчики событий
    private void OnPlayButtonClicked()
    {
        Debug.Log("▶ Играть нажата!");
        // GameManager.Instance.StartGame();
    }

    private void OnPauseClicked(ClickEvent evt)
    {
        Debug.Log($"⏸ Пауза! Позиция клика: {evt.localPosition}");
        evt.StopPropagation(); // Остановить всплытие события
    }

    private void OnMouseEnter(MouseEnterEvent evt)
    {
        // Подсветка при наведении
        var target = evt.target as VisualElement;
        target?.AddToClassList("hovered");
    }

    private void OnMouseLeave(MouseLeaveEvent evt)
    {
        var target = evt.target as VisualElement;
        target?.RemoveFromClassList("hovered");
    }

    private void OnKeyDown(KeyDownEvent evt)
    {
        if (evt.keyCode == KeyCode.Escape)
        {
            Debug.Log("ESC нажат");
        }
    }

    private void OnNameChanged(ChangeEvent<string> evt)
    {
        Debug.Log($"Имя изменено: '{evt.previousValue}' → '{evt.newValue}'");

        // Валидация
        if (evt.newValue.Length > 20)
        {
            var field = evt.target as Field;
            field?.SetValueWithoutNotify(evt.previousValue); // Откат
        }
    }

    private void OnMusicToggled(ChangeEvent<bool> evt)
    {
        Debug.Log($"Музыка: {(evt.newValue ? "включена" : "выключена")}");
        // AudioManager.Instance.SetMusicEnabled(evt.newValue);
    }

    private void OnQuantityChanged(ChangeEvent<int> evt)
    {
        int clamped = Mathf.Clamp(evt.newValue, 1, 99);
        if (clamped != evt.newValue)
        {
            (evt.target as IntegerField)?.SetValueWithoutNotify(clamped);
        }
    }

    private void OnFieldFocused(FocusEvent evt)
    {
        (evt.target as VisualElement)?.AddToClassList("focused");
    }

    private void OnFieldBlurred(BlurEvent evt)
    {
        (evt.target as VisualElement)?.RemoveFromClassList("focused");
    }

    private void OnPointerDown(PointerDownEvent evt)
    {
        Debug.Log($"Нажатие: кнопка {evt.button}, позиция {evt.localPosition}");
    }

    private void OnPointerUp(PointerUpEvent evt) { }

    private void OnPointerMove(PointerMoveEvent evt)
    {
        Debug.Log($"Движение указателя: {evt.deltaPosition}");
    }
}
```

### Управление классами и стилями



```csharp
using UnityEngine;
using UnityEngine.UIElements;

public class StyleManipulation : MonoBehaviour
{
    [SerializeField] private UIDocument uiDocument;
    private VisualElement _panel;

    void Awake()
    {
        _panel = uiDocument.rootVisualElement.Q("menu-panel");
    }

    void ManipulateStyles()
    {
        // === Работа с классами ===
        _panel.AddToClassList("panel--active");
        _panel.RemoveFromClassList("panel--hidden");
        _panel.ToggleInClassList("panel--highlighted");
        bool hasClass = _panel.ClassListContains("panel--active");

        // === Инлайн стили (IStyle) ===
        // Изменение через style property
        _panel.style.backgroundColor = new Color(0.2f, 0.2f, 0.3f, 0.9f);
        _panel.style.width = 300;
        _panel.style.height = new StyleLength(StyleKeyword.Auto);
        _panel.style.display = DisplayStyle.Flex;    // показать
        _panel.style.display = DisplayStyle.None;    // скрыть (как display:none)
        _panel.style.visibility = Visibility.Hidden; // скрыть (место сохраняется)
        _panel.style.opacity = 0.5f;

        // Позиционирование
        _panel.style.position = Position.Absolute;
        _panel.style.left = 10;
        _panel.style.top = 10;

        // Flexbox
        _panel.style.flexDirection = FlexDirection.Row;
        _panel.style.justifyContent = Justify.Center;
        _panel.style.alignItems = Align.Center;

        // Шрифт
        _panel.style.fontSize = 18;
        _panel.style.color = Color.white;
        _panel.style.unityFontStyleAndWeight = FontStyle.Bold;

        // === Динамическое добавление/удаление элементов ===
        var newLabel = new Label("Новый текст");
        newLabel.AddToClassList("dynamic-label");
        _panel.Add(newLabel);

        // Удаление
        _panel.Remove(newLabel);

        // Очистка всех дочерних элементов
        _panel.Clear();
    }

    // Пример: анимированное появление через USS transitions
    public void ShowPanel()
    {
        _panel.style.display = DisplayStyle.Flex;

        // Небольшая задержка чтобы display успел примениться
        _panel.schedule.Execute(() => {
            _panel.AddToClassList("panel--visible");
        }).StartingIn(10); // 10ms
    }

    public void HidePanel()
    {
        _panel.RemoveFromClassList("panel--visible");

        // Скрыть после завершения CSS transition (300ms)
        _panel.schedule.Execute(() => {
            _panel.style.display = DisplayStyle.None;
        }).StartingIn(300);
    }
}
```

---

## Flex Layout

UI Toolkit использует **Flexbox** для построения макетов. Это та же система что в CSS/веб-разработке.

### Основы Flexbox в USS

CSS

```csharp
/* Файл: Assets/UI/Styles/Layout.uss */

/* ========================
   Flex контейнер
======================== */
.flex-container {
    /* Активировать flex (по умолчанию в UI Toolkit — уже flex) */
    display: flex;

    /* Направление */
    flex-direction: row;         /* горизонтально (по умолчанию) */
    /* flex-direction: column;  */ /* вертикально */
    /* flex-direction: row-reverse; */
    /* flex-direction: column-reverse; */

    /* Выравнивание по главной оси */
    justify-content: flex-start;   /* к началу */
    /* justify-content: flex-end;     к концу */
    /* justify-content: center;       по центру */
    /* justify-content: space-between; с промежутками */
    /* justify-content: space-around;  с отступами */

    /* Выравнивание по поперечной оси */
    align-items: stretch;    /* растянуть (по умолчанию) */
    /* align-items: flex-start; */
    /* align-items: flex-end; */
    /* align-items: center; */

    /* Перенос строк */
    flex-wrap: nowrap;   /* без переноса (по умолчанию) */
    /* flex-wrap: wrap;  с переносом */
}

/* ========================
   Flex дочерние элементы
======================== */
.flex-item {
    /* Рост: занять свободное пространство */
    flex-grow: 1;    /* 0 = не расти, 1 = расти пропорционально */

    /* Сжатие: уменьшаться при нехватке места */
    flex-shrink: 0;  /* 0 = не сжиматься, 1 = сжиматься */

    /* Базовый размер */
    flex-basis: auto;  /* auto, 100px, 50% */

    /* Сокращение: grow shrink basis */
    flex: 1 0 auto;

    /* Выравнивание конкретного элемента */
    align-self: center;
}
```

### Практические примеры макетов

CSS

```csharp
/* ========================
   Горизонтальный тулбар
======================== */
.toolbar {
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    padding: 8px 16px;
    background-color: rgba(0, 0, 0, 0.8);
    height: 60px;
}

.toolbar__left {
    flex-direction: row;
    align-items: center;
    flex: 1 0 auto;
}

.toolbar__center {
    flex-direction: row;
    align-items: center;
    justify-content: center;
    flex: 2 0 auto;
}

.toolbar__right {
    flex-direction: row;
    align-items: center;
    justify-content: flex-end;
    flex: 1 0 auto;
}

/* ========================
   Сетка карточек (wrap)
======================== */
.cards-grid {
    flex-direction: row;
    flex-wrap: wrap;
    padding: 16px;
}

.card {
    width: 200px;
    height: 250px;
    margin: 8px;
    background-color: rgba(255, 255, 255, 0.1);
    border-radius: 8px;

    /* Карточка сама по себе flex контейнер */
    flex-direction: column;
    justify-content: space-between;
    padding: 16px;
}

/* ========================
   Полноэкранный layout
======================== */
.full-screen-layout {
    position: absolute;
    left: 0;
    top: 0;
    right: 0;
    bottom: 0;
    flex-direction: column;
}

.full-screen-layout__header {
    height: 60px;
    flex-shrink: 0;  /* Не сжимать header */
}

.full-screen-layout__content {
    flex-grow: 1;    /* Занять всё доступное пространство */
    overflow: hidden;
}

.full-screen-layout__footer {
    height: 80px;
    flex-shrink: 0;
}

/* ========================
   Центрирование элемента
======================== */
.centered-container {
    width: 100%;
    height: 100%;
    align-items: center;
    justify-content: center;
}

/* ========================
   Адаптивный HUD
======================== */
.hud-root {
    position: absolute;
    left: 0;
    top: 0;
    right: 0;
    bottom: 0;
    flex-direction: column;
    justify-content: space-between;
    padding: 16px;
}

.hud-top-row {
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-start;
}

.hud-bottom-row {
    flex-direction: row;
    justify-content: flex-end;
    align-items: flex-end;
}
```

---

## Практическое задание

Создадим полноценный HUD экран с HP баром, счётчиком монет, кнопкой паузы и подключим всё к C# с использованием **R3 ReactiveProperty** для реактивного обновления данных.

### Шаг 1 — UXML разметка HUD

XML

```csharp
<?xml version="1.0" encoding="utf-8"?>
<!-- Файл: Assets/UI/Documents/HUD.uxml -->
<ui:UXML xmlns:ui="UnityEngine.UIElements">

    <!-- Подключаем стили -->
    <Style src="project://database/Assets/UI/Styles/Variables.uss"/>
    <Style src="project://database/Assets/UI/Styles/HUD.uss"/>

    <!-- Корневой контейнер HUD -->
    <ui:VisualElement name="hud-root" class="hud-root">

        <!-- ===== ВЕРХНЯЯ ПАНЕЛЬ ===== -->
        <ui:VisualElement name="hud-top-panel" class="hud-top-panel">

            <!-- Левый блок: HP бар -->
            <ui:VisualElement name="health-block" class="health-block">

                <!-- Иконка и имя персонажа -->
                <ui:VisualElement name="player-info" class="player-info">
                    <ui:VisualElement name="player-avatar" class="player-avatar"/>
                    <ui:Label name="player-name-label" ="Герой" class="player-name"/>
                </ui:VisualElement>

                <!-- HP прогресс-бар -->
                <ui:ProgressBar
                    name="hp-bar"
                    title="❤ 100 / 100"
                    value="100"
                    high-value="100"
                    low-value="0"
                    class="hp-bar"
                />

                <!-- Бонусные щиты / эффекты -->
                <ui:VisualElement name="status-effects" class="status-effects">
                    <!-- Заполняется динамически из C# -->
                </ui:VisualElement>

            </ui:VisualElement>

            <!-- Центральный блок: кнопка паузы -->
            <ui:VisualElement name="center-block" class="center-block">
                <ui:Button
                    name="pause-button"
                    ="⏸"
                    class="pause-button"
                    tooltip="Пауза (ESC)"
                />
            </ui:VisualElement>

            <!-- Правый блок: монеты и счёт -->
            <ui:VisualElement name="stats-block" class="stats-block">

                <!-- Счётчик монет -->
                <ui:VisualElement name="coin-container" class="coin-container">
                    <ui:VisualElement name="coin-icon" class="coin-icon"/>
                    <ui:Label name="coin-label" ="0" class="coin-label"/>
                </ui:VisualElement>

                <!-- Счёт -->
                <ui:VisualElement name="score-container" class="score-container">
                    <ui:Label name="score-title" ="СЧЁТ" class="score-title"/>
                    <ui:Label name="score-label" ="0" class="score-label"/>
                </ui:VisualElement>

            </ui:VisualElement>

        </ui:VisualElement>

        <!-- ===== НИЖНЯЯ ПАНЕЛЬ (опционально) ===== -->
        <ui:VisualElement name="hud-bottom-panel" class="hud-bottom-panel">

            <!-- Панель быстрого доступа к предметам -->
            <ui:VisualElement name="hotbar" class="hotbar">
                <ui:VisualElement name="hotbar-slot-1" class="hotbar-slot hotbar-slot--active">
                    <ui:Label name="slot-1-count" ="x3" class="slot-count"/>
                </ui:VisualElement>
                <ui:VisualElement name="hotbar-slot-2" class="hotbar-slot">
                    <ui:Label name="slot-2-count" ="" class="slot-count"/>
                </ui:VisualElement>
                <ui:VisualElement name="hotbar-slot-3" class="hotbar-slot">
                    <ui:Label name="slot-3-count" ="" class="slot-count"/>
                </ui:VisualElement>
            </ui:VisualElement>

        </ui:VisualElement>

        <!-- ===== УВЕДОМЛЕНИЕ (скрыто по умолчанию) ===== -->
        <ui:VisualElement name="notification-panel" class="notification-panel">
            <ui:Label name="notification-" ="" class="notification-"/>
        </ui:VisualElement>

    </ui:VisualElement>

</ui:UXML>
```

### Шаг 2 — USS стили HUD

CSS

```csharp
/* Файл: Assets/UI/Styles/HUD.uss */
@import url("Variables.uss");

/* ========================
   Корень
======================== */
.hud-root {
    position: absolute;
    left: 0; top: 0; right: 0; bottom: 0;
    flex-direction: column;
    justify-content: space-between;
    padding: 16px;
}

/* ========================
   Верхняя панель
======================== */
.hud-top-panel {
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-start;
}

/* ========================
   Блок здоровья
======================== */
.health-block {
    flex-direction: column;
    min-width: 280px;
}

.player-info {
    flex-direction: row;
    align-items: center;
    margin-bottom: 6px;
}

.player-avatar {
    width: 36px;
    height: 36px;
    border-radius: 18px;
    background-color: rgba(255, 255, 255, 0.2);
    border-width: 2px;
    border-color: rgba(255, 255, 255, 0.5);
    margin-right: 8px;
}

.player-name {
    color: white;
    font-size: 14px;
    -unity-font-style: bold;
}

/* HP Bar */
.hp-bar {
    width: 280px;
    height: 24px;
    border-radius: 12px;
    border-width: 2px;
    border-color: rgba(0, 0, 0, 0.5);
}

.hp-bar > .unity-progress-bar__background {
    background-color: rgba(0, 0, 0, 0.5);
    border-radius: 10px;
}

.hp-bar > .unity-progress-bar__progress {
    background-color: rgb(231, 76, 60);
    border-radius: 10px;
    transition-property: width;
    transition-duration: 0.4s;
    transition-timing-function: ease-out;
}

/* Состояния HP бара по классам */
.hp-bar--high > .unity-progress-bar__progress {
    background-color: rgb(46, 204, 113);
}

.hp-bar--medium > .unity-progress-bar__progress {
    background-color: rgb(243, 156, 18);
}

.hp-bar--low > .unity-progress-bar__progress {
    background-color: rgb(231, 76, 60);
}

.hp-bar--critical > .unity-progress-bar__progress {
    background-color: rgb(192, 57, 43);
}

.hp-bar > .unity-progress-bar__title {
    color: white;
    font-size: 11px;
    -unity-font-style: bold;
    -unity--align: upper-center;
}

/* ========================
   Центральный блок
======================== */
.center-block {
    align-items: center;
    justify-content: flex-start;
}

.pause-button {
    width: 48px;
    height: 48px;
    border-radius: 8px;
    background-color: rgba(0, 0, 0, 0.5);
    border-width: 1px;
    border-color: rgba(255, 255, 255, 0.2);
    color: white;
    font-size: 20px;
    transition-property: background-color, scale;
    transition-duration: 0.12s;
}

.pause-button:hover {
    background-color: rgba(255, 255, 255, 0.2);
    scale: 1.08;
}

.pause-button:active {
    scale: 0.92;
}

/* ========================
   Блок статистики (монеты/счёт)
======================== */
.stats-block {
    flex-direction: column;
    align-items: flex-end;
}

.coin-container {
    flex-direction: row;
    align-items: center;
    background-color: rgba(0, 0, 0, 0.5);
    padding: 6px 14px;
    border-radius: 20px;
    margin-bottom: 8px;
}

.coin-icon {
    width: 20px;
    height: 20px;
    background-color: rgb(243, 156, 18);
    border-radius: 10px;
    margin-right: 8px;
}

.coin-label {
    color: rgb(243, 156, 18);
    font-size: 20px;
    -unity-font-style: bold;
    min-width: 60px;
    -unity--align: upper-right;
}

/* Анимация при изменении монет */
.coin-label--pulse {
    scale: 1.2;
    color: rgb(255, 215, 0);
    transition-property: scale, color;
    transition-duration: 0.15s;
}

.score-container {
    flex-direction: column;
    align-items: flex-end;
    background-color: rgba(0, 0, 0, 0.5);
    padding: 6px 14px;
    border-radius: 8px;
}

.score-title {
    color: rgba(255, 255, 255, 0.6);
    font-size: 10px;
    -unity-font-style: bold;
    -unity--align: upper-right;
}

.score-label {
    color: white;
    font-size: 22px;
    -unity-font-style: bold;
    -unity--align: upper-right;
}

/* ========================
   Нижняя панель / Хотбар
======================== */
.hud-bottom-panel {
    flex-direction: row;
    justify-content: center;
    align-items: flex-end;
}

.hotbar {
    flex-direction: row;
    background-color: rgba(0, 0, 0, 0.6);
    padding: 6px;
    border-radius: 12px;
    border-width: 1px;
    border-color: rgba(255, 255, 255, 0.15);
}

.hotbar-slot {
    width: 56px;
    height: 56px;
    background-color: rgba(255, 255, 255, 0.05);
    border-width: 1px;
    border-color: rgba(255, 255, 255, 0.2);
    border-radius: 8px;
    margin: 3px;
    justify-content: flex-end;
    align-items: flex-end;
    padding: 2px;
}

.hotbar-slot--active {
    border-color: rgb(243, 156, 18);
    background-color: rgba(243, 156, 18, 0.15);
}

.slot-count {
    color: white;
    font-size: 11px;
    -unity-font-style: bold;
}

/* ========================
   Уведомления
======================== */
.notification-panel {
    position: absolute;
    left: 50%;
    top: 25%;
    translate: -50% 0;
    background-color: rgba(0, 0, 0, 0.8);
    padding: 12px 32px;
    border-radius: 8px;
    border-width: 1px;
    border-color: rgba(255, 255, 255, 0.3);
    opacity: 0;
    transition-property: opacity;
    transition-duration: 0.3s;
}

.notification-panel--visible {
    opacity: 1;
}

.notification- {
    color: white;
    font-size: 18px;
    -unity--align: upper-center;
}
```

### Шаг 3 — Модель данных с R3 ReactiveProperty



```csharp
// Файл: Assets/UI/Scripts/PlayerHUDModel.cs
using R3;
using UnityEngine;

/// <summary>
/// Модель данных HUD.
/// ReactiveProperty автоматически уведомляет подписчиков при изменении.
/// </summary>
public class PlayerHUDModel
{
    // HP
    public ReactiveProperty<float> CurrentHP { get; } = new(100f);
    public ReactiveProperty<float> MaxHP { get; } = new(100f);

    // Монеты и счёт
    public ReactiveProperty<int> Coins { get; } = new(0);
    public ReactiveProperty<int> Score { get; } = new(0);

    // Производное свойство — процент HP (ReadOnlyReactiveProperty)
    public ReadOnlyReactiveProperty<float> HPPercent { get; }

    public PlayerHUDModel()
    {
        // HPPercent вычисляется автоматически при изменении HP
        HPPercent = CurrentHP
            .CombineLatest(MaxHP, (current, max) =>
                max > 0 ? current / max : 0f)
            .ToReadOnlyReactiveProperty();
    }

    // Методы изменения данных
    public void TakeDamage(float damage)
    {
        CurrentHP.Value = Mathf.Max(0, CurrentHP.Value - damage);
    }

    public void Heal(float amount)
    {
        CurrentHP.Value = Mathf.Min(MaxHP.Value, CurrentHP.Value + amount);
    }

    public void AddCoins(int amount)
    {
        Coins.Value += amount;
        Score.Value += amount * 10; // монеты дают очки
    }

    public void AddScore(int points)
    {
        Score.Value += points;
    }
}
```

### Шаг 4 — HUD Controller (View)



```csharp
// Файл: Assets/UI/Scripts/HUDController.cs
using System;
using System.Collections;
using R3;
using UnityEngine;
using UnityEngine.UIElements;

/// <summary>
/// Контроллер HUD — связывает UI Toolkit с данными через R3.
/// Паттерн MVP: этот класс — View + Presenter.
/// </summary>
public class HUDController : MonoBehaviour
{
    [Header("UI")]
    [SerializeField] private UIDocument uiDocument;

    [Header("Настройки")]
    [SerializeField] private float notificationDuration = 2.5f;

    // === Ссылки на элементы UI ===
    private ProgressBar _hpBar;
    private Label _coinLabel;
    private Label _scoreLabel;
    private Button _pauseButton;
    private VisualElement _notificationPanel;
    private Label _notification;

    // === Модель данных ===
    private PlayerHUDModel _model;

    // === Управление подписками (IDisposable) ===
    private CompositeDisposable _disposables = new();

    // === Состояние ===
    private Coroutine _notificationCoroutine;
    private int _previousCoins;

    void Awake()
    {
        // Инициализируем модель
        _model = new PlayerHUDModel();

        // Находим элементы UI
        InitializeUI();
    }

    void OnEnable()
    {
        // Подписываемся на изменения данных
        SubscribeToModel();
    }

    void OnDisable()
    {
        // Отписываемся при деактивации объекта
        _disposables.Clear();
    }

    void OnDestroy()
    {
        _disposables.Dispose();
    }

    // =============================
    //   Инициализация UI
    // =============================

    private void InitializeUI()
    {
        var root = uiDocument.rootVisualElement;

        // Кэшируем ссылки на элементы
        _hpBar = root.Q<ProgressBar>("hp-bar");
        _coinLabel = root.Q<Label>("coin-label");
        _scoreLabel = root.Q<Label>("score-label");
        _pauseButton = root.Q<Button>("pause-button");
        _notificationPanel = root.Q("notification-panel");
        _notification = root.Q<Label>("notification-");

        // Регистрируем события кнопок
        _pauseButton?.RegisterCallback<ClickEvent>(OnPauseClicked);

        // Клавиша ESC как пауза
        root.RegisterCallback<KeyDownEvent>(OnKeyDown);
        root.focusable = true;
        root.Focus();

        ValidateElements();
    }

    private void ValidateElements()
    {
#if UNITY_EDITOR
        void Warn(string name) =>
            Debug.LogWarning($"[HUDController] Элемент '{name}' не найден в UXML!");

        if (_hpBar == null) Warn("hp-bar");
        if (_coinLabel == null) Warn("coin-label");
        if (_scoreLabel == null) Warn("score-label");
        if (_pauseButton == null) Warn("pause-button");
#endif
    }

    // =============================
    //   Подписки на ReactiveProperty
    // =============================

    private void SubscribeToModel()
    {
        // Подписка на HP — обновляем бар и его цвет
        _model.CurrentHP
            .Subscribe(hp => UpdateHPBar(hp, _model.MaxHP.Value))
            .AddTo(_disposables);

        _model.MaxHP
            .Subscribe(maxHp => UpdateHPBar(_model.CurrentHP.Value, maxHp))
            .AddTo(_disposables);

        // Подписка на монеты — обновляем счётчик с анимацией
        _model.Coins
            .Subscribe(coins => UpdateCoins(coins))
            .AddTo(_disposables);

        // Подписка на счёт
        _model.Score
            .Subscribe(score => UpdateScore(score))
            .AddTo(_disposables);

        // Подписка на HP% — уведомление при критическом HP
        _model.HPPercent
            .Where(pct => pct <= 0.25f && pct > 0f)  // 25% и ниже
            .DistinctUntilChanged()                    // только при изменении
            .Subscribe(_ => ShowNotification("⚠ Критическое здоровье!"))
            .AddTo(_disposables);

        // Смерть
        _model.HPPercent
            .Where(pct => pct <= 0f)
            .First()
            .Subscribe(_ => OnPlayerDeath())
            .AddTo(_disposables);
    }

    // =============================
    //   Обновление элементов UI
    // =============================

    private void UpdateHPBar(float currentHP, float maxHP)
    {
        if (_hpBar == null) return;

        // Обновляем значения
        _hpBar.value = currentHP;
        _hpBar.highValue = maxHP;
        _hpBar.title = $"❤ {(int)currentHP} / {(int)maxHP}";

        // Обновляем цвет бара в зависимости от процента HP
        float percent = maxHP > 0 ? currentHP / maxHP : 0f;
        UpdateHPBarColor(percent);
    }

    private void UpdateHPBarColor(float hpPercent)
    {
        if (_hpBar == null) return;

        // Убираем все классы состояний
        _hpBar.RemoveFromClassList("hp-bar--high");
        _hpBar.RemoveFromClassList("hp-bar--medium");
        _hpBar.RemoveFromClassList("hp-bar--low");
        _hpBar.RemoveFromClassList("hp-bar--critical");

        // Добавляем нужный класс
        string colorClass = hpPercent switch
        {
            > 0.6f => "hp-bar--high",
            > 0.35f => "hp-bar--medium",
            > 0.15f => "hp-bar--low",
            _ => "hp-bar--critical"
        };

        _hpBar.AddToClassList(colorClass);
    }

    private void UpdateCoins(int coins)
    {
        if (_coinLabel == null) return;

        _coinLabel. = coins.ToString("N0");

        // Анимация при увеличении монет
        if (coins > _previousCoins)
        {
            AnimateCoinLabel();
        }

        _previousCoins = coins;
    }

    private void AnimateCoinLabel()
    {
        if (_coinLabel == null) return;

        // Добавляем класс анимации
        _coinLabel.AddToClassList("coin-label--pulse");

        // Убираем через 200ms (длительность transition в USS)
        _coinLabel.schedule.Execute(() => {
            _coinLabel.RemoveFromClassList("coin-label--pulse");
        }).StartingIn(200);
    }

    private void UpdateScore(int score)
    {
        if (_scoreLabel == null) return;
        _scoreLabel. = score.ToString("N0");
    }

    // =============================
    //   Уведомления
    // =============================

    public void ShowNotification(string message)
    {
        if (_notificationPanel == null || _notification == null) return;

        // Останавливаем предыдущее уведомление
        if (_notificationCoroutine != null)
        {
            StopCoroutine(_notificationCoroutine);
        }

        _notificationCoroutine = StartCoroutine(
            ShowNotificationCoroutine(message)
        );
    }

    private IEnumerator ShowNotificationCoroutine(string message)
    {
        // Устанавливаем текст
        _notification. = message;

        // Показываем (через класс — USS transition анимирует opacity)
        _notificationPanel.style.display = DisplayStyle.Flex;

        yield return null; // Ждём один кадр для применения display

        _notificationPanel.AddToClassList("notification-panel--visible");

        // Ждём
        yield return new WaitForSeconds(notificationDuration);

        // Скрываем
        _notificationPanel.RemoveFromClassList("notification-panel--visible");

        // Ждём окончания transition (0.3s из USS)
        yield return new WaitForSeconds(0.35f);

        _notificationPanel.style.display = DisplayStyle.None;
    }

    // =============================
    //   Обработчики событий
    // =============================

    private void OnPauseClicked(ClickEvent evt)
    {
        Debug.Log("⏸ Пауза нажата!");
        // PauseManager.Instance?.TogglePause();
        ShowNotification("⏸ Игра на паузе");
    }

    private void OnKeyDown(KeyDownEvent evt)
    {
        if (evt.keyCode == KeyCode.Escape)
        {
            OnPauseClicked(null);
        }
    }

    private void OnPlayerDeath()
    {
        Debug.Log("💀 Игрок погиб");
        ShowNotification("💀 Вы погибли...");
        // GameManager.Instance?.OnPlayerDeath();
    }

    // =============================
    //   Публичный API (вызывается из игровой логики)
    // =============================

    /// <summary>Нанести урон игроку</summary>
    public void TakeDamage(float damage)
    {
        _model.TakeDamage(damage);
    }

    /// <summary>Вылечить игрока</summary>
    public void Heal(float amount)
    {
        _model.Heal(amount);
    }

    /// <summary>Добавить монеты</summary>
    public void AddCoins(int amount)
    {
        _model.AddCoins(amount);
        ShowNotification($"💰 +{amount} монет!");
    }

    /// <summary>Добавить очки</summary>
    public void AddScore(int points)
    {
        _model.AddScore(points);
    }

    /// <summary>Установить максимальное HP</summary>
    public void SetMaxHP(float maxHP)
    {
        _model.MaxHP.Value = maxHP;
        _model.CurrentHP.Value = maxHP;
    }

    // =============================
    //   Тестирование в Editor
    // =============================

#if UNITY_EDITOR
    void Update()
    {
        // Тестовые горячие клавиши
        if (Input.GetKeyDown(KeyCode.Q))
            TakeDamage(15f);

        if (Input.GetKeyDown(KeyCode.E))
            Heal(20f);

        if (Input.GetKeyDown(KeyCode.C))
            AddCoins(50);

        if (Input.GetKeyDown(KeyCode.Alpha1))
            SetMaxHP(100f);
    }
#endif
}
```

### Шаг 5 — Пример интеграции с игровой логикой



```csharp
// Файл: Assets/Scripts/Player/PlayerHealth.cs
using R3;
using UnityEngine;

/// <summary>
/// Компонент здоровья игрока.
/// Сообщает HUD контроллеру об изменениях через прямую ссылку.
/// Альтернатива: использовать общую модель данных или EventBus.
/// </summary>
public class PlayerHealth : MonoBehaviour
{
    [Header("Настройки")]
    [SerializeField] private float maxHP = 100f;
    [SerializeField] private float currentHP;

    [Header("Ссылки")]
    [SerializeField] private HUDController hudController;

    // Публичные свойства для внешнего доступа
    public float CurrentHP => currentHP;
    public float MaxHP => maxHP;
    public bool IsAlive => currentHP > 0;

    // Событие для других систем
    public event Action<float> OnDamaged;
    public event Action OnDeath;

    void Awake()
    {
        currentHP = maxHP;

        // Если HUD не назначен — ищем на сцене
        if (hudController == null)
        {
            hudController = FindObjectOfType<HUDController>();
        }
    }

    void Start()
    {
        // Инициализируем HUD начальными значениями
        hudController?.SetMaxHP(maxHP);
    }

    public void TakeDamage(float damage)
    {
        if (!IsAlive) return;

        float actualDamage = Mathf.Max(0, damage);
        currentHP = Mathf.Max(0, currentHP - actualDamage);

        // Обновляем HUD
        hudController?.TakeDamage(actualDamage);

        OnDamaged?.Invoke(actualDamage);

        if (!IsAlive)
        {
            OnDeath?.Invoke();
        }
    }

    public void Heal(float amount)
    {
        if (!IsAlive) return;

        float actualHeal = Mathf.Min(amount, maxHP - currentHP);
        currentHP += actualHeal;

        hudController?.Heal(actualHeal);
    }

    // Тестирование столкновений
    private void OnTriggerEnter(Collider other)
    {
        if (other.TryGetComponent<CoinPickup>(out var coin))
        {
            hudController?.AddCoins(coin.Value);
            hudController?.AddScore(coin.Value * 10);
            Destroy(other.gameObject);
        }
    }
}

/// <summary>Заглушка для монеты (для компиляции примера)</summary>
public class CoinPickup : MonoBehaviour
{
    public int Value = 10;
}
```

---

## Проверь себя

### Теоретические вопросы

**1.** В чём главное архитектурное отличие UI Toolkit от Canvas (uGUI)?

> _Ожидаемый ответ:_ Canvas строится на **GameObject-иерархии** — каждый элемент это объект на сцене с компонентами. UI Toolkit использует **виртуальное дерево элементов** (VisualElement tree), не связанное с GameObject иерархией, описываемое через UXML и стилизуемое через USS. Это близко к веб-подходу HTML + CSS.

---

**2.** Что такое `rootVisualElement` и как его получить?

> _Ожидаемый ответ:_ `rootVisualElement` — это корневой `VisualElement` дерева UI конкретного UI Document. Через него можно получить доступ ко всем элементам через `Q<T>()` и `Query<T>()`. Получается через: `GetComponent<UIDocument>().rootVisualElement`.

---

**3.** Чем `Q<Button>("my-btn")` отличается от `Query<Button>("my-btn").First()`?

> _Ожидаемый ответ:_ `Q<T>()` — сокращённая запись, возвращает **первый найденный** элемент или `null`. `Query<T>()` возвращает `UQueryBuilder` — **ленивый запрос**, который вычисляется при вызове `.ToList()`, `.First()`, `.ForEach()`. Для поиска одного элемента предпочтительнее `Q<T>()` как более лаконичный вариант.

---

**4.** Как скрыть элемент в UI Toolkit, сохранив место в layout? А как скрыть без сохранения места?

> _Ожидаемый ответ:_
> 
> - **Сохранить место:** `element.style.visibility = Visibility.Hidden;` (аналог CSS `visibility: hidden`)
> - **Убрать из layout:** `element.style.display = DisplayStyle.None;` (аналог CSS `display: none`)

---

**5.** Что такое `CompositeDisposable` и почему важно вызывать `.Dispose()` при уничтожении объекта?

> _Ожидаемый ответ:_ `CompositeDisposable` — контейнер для хранения подписок R3/Rx. При вызове `.Dispose()` он отписывается от всех хранящихся подписок. Без этого подписки продолжат существовать в памяти после уничтожения объекта, что приводит к **утечкам памяти** и ошибкам при попытке обновить уже уничтоженные UI элементы.

---

### Практические задания

**Задание 1** ⭐

Создайте UXML файл с простой формой регистрации:

- `Field` для имени пользователя
- `Field` для email (type="email")
- Кнопка "Зарегистрироваться"
- Валидация: кнопка заблокирована если имя короче 3 символов

---

**Задание 2** ⭐⭐

Напишите USS стили для инвентарной сетки:

- Контейнер с flex-wrap
- Слоты 64x64px с эффектами `:hover` и `:active`
- Цветовая индикация редкости предмета (обычный/редкий/эпический) через модификаторы классов
- Плавные transitions для всех интерактивных состояний

---

**Задание 3** ⭐⭐⭐

Расширьте HUD из практического задания:

- Добавьте анимированное уведомление "+50 монет" которое появляется в месте подбора и улетает вверх
- Реализуйте через USS transition + `schedule.Execute()`
- Поддержка очереди уведомлений (если несколько монет подобраны быстро)

---

**Задание 4** ⭐⭐⭐⭐

Создайте переиспользуемый компонент `HealthBarComponent`:

- Собственный UXML шаблон (через `<Template>` и `<Instance>`)
- Параметризуемый цвет и размер через USS переменные
- Используется в HUD для игрока И над врагами (в World Space через `RuntimePanelUtils`)

---

### Чеклист перед сдачей проекта



```csharp
✅ UXML файлы имеют корректный xmlns namespace
✅ Все name атрибуты уникальны в пределах документа
✅ USS переменные объявлены в Variables.uss и импортированы
✅ Ссылки на элементы кэшируются в Awake/OnEnable, не в Update
✅ Все подписки добавлены в CompositeDisposable
✅ CompositeDisposable.Dispose() вызывается в OnDestroy
✅ Нет прямого изменения style в Update (только через классы или по событию)
✅ UI Document имеет назначенный Panel Settings ассет
✅ Panel Settings настроен на Scale With Screen Size
✅ Все интерактивные элементы имеют :hover и :active состояния в USS
✅ Элементы валидируются в Awake с понятными сообщениями об ошибках
```

---

> **Итог:** UI Toolkit — это современный и производительный способ создания интерфейсов в Unity. Разделение структуры (UXML), стилей (USS) и логики (C#) делает проект масштабируемым и удобным в поддержке. Связка с R3 ReactiveProperty позволяет строить реактивные интерфейсы, которые автоматически обновляются при изменении данных — без ручного отслеживания состояний и лишних вызовов в `Update()`.