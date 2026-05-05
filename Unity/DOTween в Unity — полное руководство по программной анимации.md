## Содержание

- [Введение — зачем DOTween когда есть Animator](#%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%E2%80%94%20%D0%B7%D0%B0%D1%87%D0%B5%D0%BC%20DOTween%20%D0%BA%D0%BE%D0%B3%D0%B4%D0%B0%20%D0%B5%D1%81%D1%82%D1%8C%20Animator)
	- [Сравнение подходов](#%D0%A1%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BF%D0%BE%D0%B4%D1%85%D0%BE%D0%B4%D0%BE%D0%B2)
	- [Когда использовать DOTween](#%D0%9A%D0%BE%D0%B3%D0%B4%D0%B0%20%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%20DOTween)
	- [Когда Animator лучше](#%D0%9A%D0%BE%D0%B3%D0%B4%D0%B0%20Animator%20%D0%BB%D1%83%D1%87%D1%88%D0%B5)
- [Установка и настройка](#%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0%20%D0%B8%20%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0)
	- [Шаг 1: Установка из Asset Store](#%D0%A8%D0%B0%D0%B3%201:%20%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0%20%D0%B8%D0%B7%20Asset%20Store)
	- [Шаг 2: Первоначальная настройка](#%D0%A8%D0%B0%D0%B3%202:%20%D0%9F%D0%B5%D1%80%D0%B2%D0%BE%D0%BD%D0%B0%D1%87%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0)
	- [Шаг 3: Глобальные настройки DOTween](#%D0%A8%D0%B0%D0%B3%203:%20%D0%93%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B8%20DOTween)
	- [Шаг 4: Проверка установки](#%D0%A8%D0%B0%D0%B3%204:%20%D0%9F%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0%20%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B8)
- [Базовые твины](#%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B5%20%D1%82%D0%B2%D0%B8%D0%BD%D1%8B)
	- [DOMove — перемещение](#DOMove%20%E2%80%94%20%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D0%B5)
	- [DORotate — вращение](#DORotate%20%E2%80%94%20%D0%B2%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D0%B5)
	- [DOScale — масштабирование](#DOScale%20%E2%80%94%20%D0%BC%D0%B0%D1%81%D1%88%D1%82%D0%B0%D0%B1%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5)
	- [DOFade — прозрачность](#DOFade%20%E2%80%94%20%D0%BF%D1%80%D0%BE%D0%B7%D1%80%D0%B0%D1%87%D0%BD%D0%BE%D1%81%D1%82%D1%8C)
	- [Параметры твина — fluent API](#%D0%9F%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B%20%D1%82%D0%B2%D0%B8%D0%BD%D0%B0%20%E2%80%94%20fluent%20API)
- [Easing функции](#Easing%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8)
	- [Как читать названия Ease](#%D0%9A%D0%B0%D0%BA%20%D1%87%D0%B8%D1%82%D0%B0%D1%82%D1%8C%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%20Ease)
	- [Визуальное объяснение словами](#%D0%92%D0%B8%D0%B7%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5%20%D0%BE%D0%B1%D1%8A%D1%8F%D1%81%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D0%BC%D0%B8)
	- [Практические рекомендации](#%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8)
	- [Все значения Ease enum](#%D0%92%D1%81%D0%B5%20%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D1%8F%20Ease%20enum)
- [Callbacks](#Callbacks)
	- [Основные callbacks](#%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5%20callbacks)
	- [Практический пример: загрузка уровня](#%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80:%20%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B0%20%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F)
	- [OnUpdate для отслеживания значений](#OnUpdate%20%D0%B4%D0%BB%D1%8F%20%D0%BE%D1%82%D1%81%D0%BB%D0%B5%D0%B6%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%20%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B9)
- [Sequences](#Sequences)
	- [Создание Sequence](#%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20Sequence)
	- [Разница между Append и Join](#%D0%A0%D0%B0%D0%B7%D0%BD%D0%B8%D1%86%D0%B0%20%D0%BC%D0%B5%D0%B6%D0%B4%D1%83%20Append%20%D0%B8%20Join)
	- [Глобальные настройки для Sequence](#%D0%93%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B8%20%D0%B4%D0%BB%D1%8F%20Sequence)
- [DOTween с UI](#DOTween%20%D1%81%20UI)
	- [DOAnchorPos — движение UI элементов](#DOAnchorPos%20%E2%80%94%20%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20UI%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2)
	- [DOColor — изменение цвета UI](#DOColor%20%E2%80%94%20%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%86%D0%B2%D0%B5%D1%82%D0%B0%20UI)
	- [MeshPro](#MeshPro)
	- [CanvasGroup для работы с группами UI](#CanvasGroup%20%D0%B4%D0%BB%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B%20%D1%81%20%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D0%B0%D0%BC%D0%B8%20UI)
- [Loops](#Loops)
	- [Типы LoopType](#%D0%A2%D0%B8%D0%BF%D1%8B%20LoopType)
	- [Практические примеры зацикливания](#%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B%20%D0%B7%D0%B0%D1%86%D0%B8%D0%BA%D0%BB%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F)
- [Управление твинами](#%D0%A3%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%82%D0%B2%D0%B8%D0%BD%D0%B0%D0%BC%D0%B8)
	- [Методы управления на экземпляре](#%D0%9C%D0%B5%D1%82%D0%BE%D0%B4%D1%8B%20%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%BD%D0%B0%20%D1%8D%D0%BA%D0%B7%D0%B5%D0%BC%D0%BF%D0%BB%D1%8F%D1%80%D0%B5)
	- [DOKill — правильная очистка памяти](#DOKill%20%E2%80%94%20%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%BE%D1%87%D0%B8%D1%81%D1%82%D0%BA%D0%B0%20%D0%BF%D0%B0%D0%BC%D1%8F%D1%82%D0%B8)
	- [SetLink — автоматическое управление жизнью твина](#SetLink%20%E2%80%94%20%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5%20%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B6%D0%B8%D0%B7%D0%BD%D1%8C%D1%8E%20%D1%82%D0%B2%D0%B8%D0%BD%D0%B0)
	- [Глобальные операции над несколькими твинами](#%D0%93%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8%20%D0%BD%D0%B0%D0%B4%20%D0%BD%D0%B5%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%B8%D0%BC%D0%B8%20%D1%82%D0%B2%D0%B8%D0%BD%D0%B0%D0%BC%D0%B8)
- [Практическое задание](#%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5)
	- [Структура сцены](#%D0%A1%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D1%81%D1%86%D0%B5%D0%BD%D1%8B)
	- [Полный код анимации главного меню](#%D0%9F%D0%BE%D0%BB%D0%BD%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%B4%20%D0%B0%D0%BD%D0%B8%D0%BC%D0%B0%D1%86%D0%B8%D0%B8%20%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%BC%D0%B5%D0%BD%D1%8E)
	- [Вспомогательный класс: эффект кнопки при нажатии](#%D0%92%D1%81%D0%BF%D0%BE%D0%BC%D0%BE%D0%B3%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81:%20%D1%8D%D1%84%D1%84%D0%B5%D0%BA%D1%82%20%D0%BA%D0%BD%D0%BE%D0%BF%D0%BA%D0%B8%20%D0%BF%D1%80%D0%B8%20%D0%BD%D0%B0%D0%B6%D0%B0%D1%82%D0%B8%D0%B8)
	- [Подключение в Inspector](#%D0%9F%D0%BE%D0%B4%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20Inspector)
- [Проверь себя](#%D0%9F%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D1%8C%20%D1%81%D0%B5%D0%B1%D1%8F)
	- [📝 Теоретические вопросы](#%F0%9F%93%9D%20%D0%A2%D0%B5%D0%BE%D1%80%D0%B5%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%B2%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D1%8B)
	- [💻 Практические задания](#%F0%9F%92%BB%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F)
	- [🔍 Найди ошибки в коде](#%F0%9F%94%8D%20%D0%9D%D0%B0%D0%B9%D0%B4%D0%B8%20%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D0%B8%20%D0%B2%20%D0%BA%D0%BE%D0%B4%D0%B5)
	- [✅ Ответы на вопрос "Найди ошибки"](#%E2%9C%85%20%D0%9E%D1%82%D0%B2%D0%B5%D1%82%D1%8B%20%D0%BD%D0%B0%20%D0%B2%D0%BE%D0%BF%D1%80%D0%BE%D1%81%20%22%D0%9D%D0%B0%D0%B9%D0%B4%D0%B8%20%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D0%B8%22)
	- [📚 Что изучить дальше](#%F0%9F%93%9A%20%D0%A7%D1%82%D0%BE%20%D0%B8%D0%B7%D1%83%D1%87%D0%B8%D1%82%D1%8C%20%D0%B4%D0%B0%D0%BB%D1%8C%D1%88%D0%B5)


---

## Введение — зачем DOTween когда есть Animator

Unity Animator — мощный инструмент. Он позволяет создавать сложные анимационные графы, управлять состояниями персонажей, смешивать анимации. Но у него есть одна фундаментальная проблема: **он создан для работы с заранее подготовленными данными**.

Представь задачу: при клике на карточку товара нужно плавно переместить её в центр экрана, увеличить и сделать полупрозрачным фон. Координаты центра зависят от разрешения экрана, которое ты не знаешь заранее. В Animator это решается через код и AnimatorController с кучей параметров. Это громоздко.

### Сравнение подходов

|Критерий|Unity Animator|DOTween|
|---|---|---|
|Анимация по динамическим данным|Сложно|Легко|
|Настройка через Inspector|Удобно|Через код|
|Анимация персонажей|Отлично|Не для этого|
|Анимация UI|Избыточно|Идеально|
|Скорость написания кода|Медленно|Быстро|
|Читаемость кода|Плохая|Хорошая|

### Когда использовать DOTween

- **UI-анимации**: появление меню, кнопок, панелей
- **Анимация по данным**: движение к точке, которую вычисляет игровая логика
- **Процедурные эффекты**: покачивание объекта, пульсация, тряска камеры
- **Цепочки действий**: "подожди 0.5 секунды, потом переместись, потом исчезни"
- **Прототипирование**: быстро проверить идею без создания Animation Clip

### Когда Animator лучше

- Сложная скелетная анимация персонажей
- State Machine с множеством переходов
- Blend Trees для плавного смешивания движений

DOTween — это **tweening библиотека**. Tween (от слова "between") — это интерполяция значения из одной точки в другую за определённое время. Именно это DOTween и делает, но с огромным количеством удобных инструментов поверх.

---

## Установка и настройка

### Шаг 1: Установка из Asset Store

1. Открой **Window → Asset Store** (или перейди на [assetstore.unity.com](https://assetstore.unity.com/))
2. Найди **"DOTween (HOTween v2)"** от Demigiant
3. Нажми **Add to My Assets**, затем **Open in Unity**
4. В Package Manager нажми **Download**, затем **Import**

> **Бесплатная версия** включает всё необходимое для большинства проектов. **DOTween Pro** добавляет визуальный редактор и работу с путями (Path).

### Шаг 2: Первоначальная настройка

После импорта автоматически откроется окно настройки. Если оно не появилось:

**Tools → Demigiant → DOTween Utility Panel**

В открывшемся окне:

1. Нажми кнопку **"Setup DOTween..."** — это создаст файлы настроек
    
2. Выбери модули, которые хочешь использовать:
    
    - ✅ **Audio** — анимация AudioSource
    - ✅ **Physics** — работа с Rigidbody
    - ✅ **UI** — работа с компонентами Unity UI (обязательно!)
    - ✅ **MeshPro** — если используешь TMP
3. Нажми **"Apply"**
    

### Шаг 3: Глобальные настройки DOTween

Ты можешь настроить DOTween через код при старте приложения:



```csharp
using UnityEngine;
using DG.Tweening;

public class AppInitializer : MonoBehaviour
{
    void Awake()
    {
        // Максимальное количество одновременных твинов (по умолчанию 200)
        DOTween.SetTweensCapacity(tweenersCapacity: 500, sequencesCapacity: 100);
        
        // Глобальный Ease по умолчанию для всех твинов
        DOTween.defaultEaseType = Ease.OutQuad;
        
        // Поведение при смене Time.timeScale
        DOTween.defaultTimeScaleIndependent = false;
        
        // Включить логи (только для разработки!)
        DOTween.showUnityEditorReport = true;
    }
}
```

### Шаг 4: Проверка установки

Создай тестовый скрипт:



```csharp
using UnityEngine;
using DG.Tweening; // Главное пространство имён

public class DOTweenTest : MonoBehaviour
{
    void Start()
    {
        // Если это компилируется — DOTween установлен корректно
        transform.DOMoveX(5f, 2f);
        Debug.Log("DOTween работает!");
    }
}
```

Прикрепи его к любому объекту на сцене и запусти. Объект должен плавно переместиться по X на 5 единиц за 2 секунды.

---

## Базовые твины

Каждый метод DOTween следует паттерну:



```csharp
DO[Действие](целевое_значение, длительность)
```

Это **методы расширения** (extension methods) — они добавляются к существующим компонентам Unity. Поэтому ты пишешь `transform.DOMove(...)` вместо `DOTween.Move(transform, ...)`.

### DOMove — перемещение



```csharp
using UnityEngine;
using DG.Tweening;

public class MovementExamples : MonoBehaviour
{
    void Start()
    {
        // Переместить объект в мировую точку (2, 3, 0) за 1.5 секунды
        transform.DOMove(new Vector3(2f, 3f, 0f), 1.5f);
        
        // Переместить только по оси X
        transform.DOMoveX(10f, 1f);
        
        // Переместить только по оси Y
        transform.DOMoveY(5f, 1f);
        
        // Переместить только по оси Z
        transform.DOMoveZ(-3f, 1f);
        
        // Локальное перемещение (relative to parent)
        transform.DOLocalMove(new Vector3(0f, 2f, 0f), 1f);
        
        // Перемещение ОТНОСИТЕЛЬНО текущей позиции (не к точке, а НА величину)
        // Второй параметр true = "snapping" — привязка к целым числам
        transform.DOMove(new Vector3(1f, 0f, 0f), 1f, snapping: false);
    }
}
```

> ⚠️ **Важно:** По умолчанию DOMove перемещает объект **к абсолютной позиции**, а не на относительное расстояние. Чтобы двигать относительно — используй `SetRelative()`.



```csharp
// Переместить объект на 3 единицы вправо ОТНОСИТЕЛЬНО текущей позиции
transform.DOMoveX(3f, 1f).SetRelative();
```

### DORotate — вращение



```csharp
using UnityEngine;
using DG.Tweening;

public class RotationExamples : MonoBehaviour
{
    void Start()
    {
        // Повернуть к углам Эйлера (0, 180, 0) за 1 секунду
        transform.DORotate(new Vector3(0f, 180f, 0f), 1f);
        
        // Режимы вращения — очень важный параметр!
        
        // Fast — кратчайший путь (по умолчанию)
        transform.DORotate(new Vector3(0f, 270f, 0f), 1f, RotateMode.Fast);
        
        // WorldAxisAdd — добавить к мировому вращению
        transform.DORotate(new Vector3(0f, 360f, 0f), 2f, RotateMode.WorldAxisAdd);
        
        // LocalAxisAdd — добавить к локальному вращению
        transform.DORotate(new Vector3(0f, 0f, 360f), 2f, RotateMode.LocalAxisAdd);
        
        // Через Quaternion
        transform.DORotateQuaternion(Quaternion.Euler(0f, 90f, 0f), 1f);
        
        // Бесконечное вращение на 360 градусов (для спиннеров, лоадеров)
        transform.DORotate(new Vector3(0f, 0f, 360f), 2f, RotateMode.LocalAxisAdd)
                 .SetLoops(-1, LoopType.Restart);
    }
    
    void OnDestroy()
    {
        // Всегда убивай твины при уничтожении объекта!
        DOTween.Kill(this);
    }
}
```

### DOScale — масштабирование



```csharp
using UnityEngine;
using DG.Tweening;

public class ScaleExamples : MonoBehaviour
{
    void Start()
    {
        // Масштабировать до (2, 2, 2) за 0.5 секунды
        transform.DOScale(new Vector3(2f, 2f, 2f), 0.5f);
        
        // Удобный вариант для равномерного масштаба
        transform.DOScale(2f, 0.5f);
        
        // Масштабировать только по одной оси
        transform.DOScaleX(1.5f, 0.3f);
        transform.DOScaleY(0.5f, 0.3f);
        transform.DOScaleZ(2f, 0.3f);
        
        // Эффект "пульсации" — масштаб туда-обратно
        transform.DOScale(1.2f, 0.3f)
                 .SetLoops(-1, LoopType.Yoyo);
        
        // Эффект появления с нуля (pop-in анимация)
        transform.localScale = Vector3.zero;
        transform.DOScale(1f, 0.4f).SetEase(Ease.OutBack);
    }
    
    void OnDestroy()
    {
        DOTween.Kill(this);
    }
}
```

### DOFade — прозрачность

Для работы с прозрачностью через DOTween нужны специфические компоненты:



```csharp
using UnityEngine;
using DG.Tweening;

public class FadeExamples : MonoBehaviour
{
    [SerializeField] private SpriteRenderer spriteRenderer;
    [SerializeField] private Renderer meshRenderer;
    [SerializeField] private CanvasGroup canvasGroup;
    
    void Start()
    {
        // SpriteRenderer — прозрачность спрайта
        spriteRenderer.DOFade(0f, 1f); // затухание до нуля
        spriteRenderer.DOFade(1f, 1f); // появление
        
        // Изменение цвета целиком (включая альфа)
        spriteRenderer.DOColor(Color.red, 1f);
        
        // MeshRenderer (3D объекты)
        // Материал должен поддерживать прозрачность!
        meshRenderer.material.DOFade(0f, 1f);
        
        // CanvasGroup — лучший способ для UI
        // Управляет прозрачностью всей группы UI элементов
        canvasGroup.DOFade(0f, 0.5f); // скрыть
        canvasGroup.DOFade(1f, 0.5f); // показать
    }
    
    void OnDestroy()
    {
        DOTween.Kill(this);
    }
}
```

> 💡 **Совет:** Для UI рекомендуется использовать `CanvasGroup.DOFade()` вместо работы с отдельными `Image.color`. Это позволяет управлять прозрачностью целой панели одним твином.

### Параметры твина — fluent API

DOTween использует **fluent interface** — ты можешь цепочкой вызывать настройки:



```csharp
using UnityEngine;
using DG.Tweening;

public class FluentAPIExample : MonoBehaviour
{
    void Start()
    {
        transform
            .DOMoveY(5f, 1f)           // Переместить по Y за 1 сек
            .SetEase(Ease.OutBounce)    // Установить тип easing
            .SetDelay(0.5f)             // Задержка перед стартом
            .SetLoops(3, LoopType.Yoyo) // 3 повторения туда-обратно
            .SetSpeedBased()            // Время = скорость, не длительность
            .SetId("myTween")           // Идентификатор для поиска
            .SetUpdate(true)            // Использовать unscaled time
            .OnComplete(() => Debug.Log("Готово!"));
    }
    
    void OnDestroy()
    {
        DOTween.Kill(this);
    }
}
```

---

## Easing функции

Easing — это **кривая скорости** изменения значения. Без easing всё движется с постоянной скоростью — механически и неприятно. С easing движение становится живым.

### Как читать названия Ease

Каждое название состоит из двух частей:



```csharp
[Тип кривой][Направление применения]
```

**Типы кривых:**

- `Linear` — прямая линия, постоянная скорость
- `Sine` — синусоидальная, мягкая
- `Quad` — квадратичная, заметное ускорение
- `Cubic` — кубическая, сильнее Quad
- `Quart` — четвёртая степень
- `Quint` — пятая степень, очень резкая
- `Expo` — экспоненциальная, очень резкий старт/финиш
- `Circ` — круговая, похожа на Expo
- `Back` — "перелёт" за цель, потом возврат
- `Elastic` — пружинный эффект
- `Bounce` — отскок как мячик

**Направления:**

- `In` — кривая применяется в начале (медленный старт)
- `Out` — кривая применяется в конце (медленный финиш)
- `InOut` — кривая в начале и в конце (медленный старт И финиш)

### Визуальное объяснение словами



```csharp
Linear:
▓▓▓▓▓▓▓▓▓▓  — равномерно, без изменений скорости

EaseInQuad:
▓░░░░░▓▓▓▓  — начинает медленно, разгоняется к концу

EaseOutQuad:
▓▓▓▓▓░░░░░  — начинает быстро, замедляется к концу (САМЫЙ ЧАСТЫЙ ДЛЯ UI)

EaseInOutQuad:
▓░░░░░░░▓▓  — медленно, ускоряется, снова замедляется

EaseOutBounce:
▓▓▓▓▓▓ ↓ bounce bounce bounce — прилетает и отскакивает

EaseOutBack:
▓▓▓▓▓▓▓▓▓▓→← — перелетает цель и возвращается

EaseOutElastic:
▓▓▓▓▓▓▓~波~  — растягивается пружиной
```

### Практические рекомендации



```csharp
using UnityEngine;
using DG.Tweening;

public class EasingExamples : MonoBehaviour
{
    void Start()
    {
        // UI кнопки и панели — OutQuad или OutCubic
        // Объекты "прилетают" в кадр и плавно останавливаются
        transform.DOMove(Vector3.zero, 0.4f).SetEase(Ease.OutQuad);
        
        // Появление объекта из нуля (pop) — OutBack или OutElastic
        // Объект немного "переувеличивается" и возвращается к норме
        transform.DOScale(1f, 0.5f).SetEase(Ease.OutBack);
        
        // Объект падает или приземляется — OutBounce
        // Имитирует физику отскока
        transform.DOMoveY(0f, 0.8f).SetEase(Ease.OutBounce);
        
        // Уход объекта с экрана — InQuad или InCubic
        // Медленно начинает и быстро улетает
        transform.DOMoveX(-20f, 0.3f).SetEase(Ease.InQuad);
        
        // Пружина — InElastic
        transform.DOScale(0f, 0.4f).SetEase(Ease.InElastic);
        
        // Пользовательская кривая через AnimationCurve
        AnimationCurve customCurve = AnimationCurve.EaseInOut(0, 0, 1, 1);
        transform.DOMoveX(5f, 1f).SetEase(customCurve);
    }
    
    void OnDestroy()
    {
        DOTween.Kill(this);
    }
}
```

### Все значения Ease enum



```csharp
// Полный список доступных значений Ease
public enum Ease
{
    Unset,
    Linear,
    InSine, OutSine, InOutSine,
    InQuad, OutQuad, InOutQuad,
    InCubic, OutCubic, InOutCubic,
    InQuart, OutQuart, InOutQuart,
    InQuint, OutQuint, InOutQuint,
    InExpo, OutExpo, InOutExpo,
    InCirc, OutCirc, InOutCirc,
    InBack, OutBack, InOutBack,
    InElastic, OutElastic, InOutElastic,
    InBounce, OutBounce, InOutBounce,
    Flash, InFlash, OutFlash, InOutFlash,
    INTERNAL_Zero, INTERNAL_Custom
}
```

---

## Callbacks

Callbacks — это функции, которые вызываются в определённые моменты жизни твина. Они делают DOTween настоящим инструментом для построения игровой логики.

### Основные callbacks



```csharp
using UnityEngine;
using DG.Tweening;

public class CallbackExamples : MonoBehaviour
{
    void Start()
    {
        Tween myTween = transform
            .DOMoveX(5f, 2f)
            
            // Вызывается один раз перед первым обновлением
            .OnStart(() =>
            {
                Debug.Log("Твин начался!");
            })
            
            // Вызывается каждый кадр во время работы твина
            .OnUpdate(() =>
            {
                // Здесь можно отслеживать прогресс
                float progress = myTween.ElapsedPercentage();
                Debug.Log($"Прогресс: {progress:P0}");
            })
            
            // Вызывается при завершении (один раз)
            .OnComplete(() =>
            {
                Debug.Log("Твин завершён!");
                // Запустить следующее действие
                StartNextAnimation();
            })
            
            // Вызывается при уничтожении твина (Kill или завершение)
            .OnKill(() =>
            {
                Debug.Log("Твин уничтожен!");
            })
            
            // Вызывается при каждом повторении (для SetLoops)
            .OnStepComplete(() =>
            {
                Debug.Log("Один шаг цикла завершён!");
            })
            
            // Вызывается при перемотке (Rewind)
            .OnRewind(() =>
            {
                Debug.Log("Твин перемотан!");
            });
    }
    
    void StartNextAnimation()
    {
        transform.DOScale(2f, 0.5f);
    }
    
    void OnDestroy()
    {
        DOTween.Kill(this);
    }
}
```

### Практический пример: загрузка уровня



```csharp
using UnityEngine;
using UnityEngine.SceneManagement;
using DG.Tweening;

public class LevelLoader : MonoBehaviour
{
    [SerializeField] private CanvasGroup fadePanel;
    [SerializeField] private string sceneName;
    
    public void LoadLevel()
    {
        // Сначала затемняем экран, потом загружаем сцену
        fadePanel.DOFade(1f, 0.5f)
            .SetEase(Ease.InQuad)
            .OnComplete(() =>
            {
                SceneManager.LoadScene(sceneName);
            });
    }
    
    void Awake()
    {
        // При старте — убираем затемнение
        fadePanel.alpha = 1f;
        fadePanel.DOFade(0f, 0.5f).SetDelay(0.2f);
    }
    
    void OnDestroy()
    {
        DOTween.Kill(this);
    }
}
```

### OnUpdate для отслеживания значений



```csharp
using UnityEngine;
using DG.Tweening;
using TMPro;

public class CounterAnimation : MonoBehaviour
{
    [SerializeField] private MeshProUGUI score;
    
    public void AnimateScore(int fromValue, int toValue)
    {
        // DOTween умеет анимировать любые float значения
        float currentValue = fromValue;
        
        DOTween.To(
            getter: () => currentValue,
            setter: value => 
            {
                currentValue = value;
                score. = Mathf.RoundToInt(value).ToString("N0");
            },
            endValue: toValue,
            duration: 1.5f
        )
        .SetEase(Ease.OutQuad)
        .OnComplete(() => Debug.Log($"Очки: {toValue}"));
    }
    
    void OnDestroy()
    {
        DOTween.Kill(this);
    }
}
```

---

## Sequences

Sequence — это контейнер для твинов. Он позволяет выстраивать **последовательные** (один за другим) и **параллельные** (одновременно) анимации.

### Создание Sequence



```csharp
using UnityEngine;
using DG.Tweening;

public class SequenceBasics : MonoBehaviour
{
    void Start()
    {
        // Всегда создавай Sequence через DOTween.Sequence()
        Sequence sequence = DOTween.Sequence();
        
        // Append — добавить твин ПОСЛЕ предыдущего (последовательно)
        sequence.Append(transform.DOMoveX(3f, 1f));
        sequence.Append(transform.DOMoveY(2f, 0.5f));
        sequence.Append(transform.DOScale(2f, 0.3f));
        
        // Join — добавить твин ПАРАЛЛЕЛЬНО с предыдущим Append
        sequence.Append(transform.DOMoveX(0f, 1f));
        sequence.Join(transform.DOFade(0f, 1f)); // Запустится одновременно с DOMoveX выше
        
        // Insert — добавить твин в конкретный момент времени (в секундах)
        sequence.Insert(0.5f, transform.DORotate(new Vector3(0f, 180f, 0f), 0.5f));
        
        // AppendInterval — пауза между анимациями
        sequence.AppendInterval(0.5f);
        sequence.Append(transform.DOScale(1f, 0.3f));
        
        // AppendCallback — вызвать функцию в нужный момент
        sequence.AppendCallback(() => Debug.Log("Середина анимации!"));
        
        // InsertCallback — вызвать функцию в конкретное время
        sequence.InsertCallback(1.5f, () => Debug.Log("1.5 секунды прошло"));
    }
    
    void OnDestroy()
    {
        DOTween.Kill(this);
    }
}
```

### Разница между Append и Join



```csharp
using UnityEngine;
using DG.Tweening;

public class AppendVsJoin : MonoBehaviour
{
    [SerializeField] private Transform cube1;
    [SerializeField] private Transform cube2;
    [SerializeField] private Transform cube3;
    
    void Start()
    {
        // ПОСЛЕДОВАТЕЛЬНО: сначала cube1, потом cube2, потом cube3
        Sequence sequential = DOTween.Sequence();
        sequential.Append(cube1.DOMoveX(5f, 1f)); // 0 - 1 сек
        sequential.Append(cube2.DOMoveX(5f, 1f)); // 1 - 2 сек
        sequential.Append(cube3.DOMoveX(5f, 1f)); // 2 - 3 сек
        
        // ПАРАЛЛЕЛЬНО: все три одновременно
        Sequence parallel = DOTween.Sequence();
        parallel.Append(cube1.DOMoveX(5f, 1f)); // 0 - 1 сек
        parallel.Join(cube2.DOMoveX(5f, 1f));   // тоже 0 - 1 сек
        parallel.Join(cube3.DOMoveX(5f, 1f));   // тоже 0 - 1 сек
        
        // КОМБИНАЦИЯ: cube1 и cube2 вместе, потом cube3
        Sequence combo = DOTween.Sequence();
        combo.Append(cube1.DOMoveX(5f, 1f)); // 0 - 1 сек
        combo.Join(cube2.DOMoveY(3f, 0.5f)); // тоже 0 - 0.5 сек
        combo.Append(cube3.DOScale(2f, 0.5f)); // 1 - 1.5 сек (после cube1)
    }
    
    void OnDestroy()
    {
        DOTween.Kill(this);
    }
}
```

### Глобальные настройки для Sequence



```csharp
using UnityEngine;
using DG.Tweening;

public class SequenceSettings : MonoBehaviour
{
    void Start()
    {
        Sequence sequence = DOTween.Sequence()
            .Append(transform.DOMoveX(5f, 1f))
            .Append(transform.DOMoveY(3f, 0.5f))
            
            // Все настройки применяются ко всей последовательности!
            .SetDelay(1f)                    // Задержка перед стартом всей sequence
            .SetLoops(3, LoopType.Yoyo)      // 3 повторения туда-обратно
            .SetEase(Ease.InOutQuad)         // Ease для всей последовательности
            .SetId("mainMenuSequence")       // ID для управления
            .OnComplete(() => Debug.Log("Sequence завершена!"));
    }
    
    void OnDestroy()
    {
        DOTween.Kill(this);
    }
}
```

---

## DOTween с UI

Для работы с UI убедись, что в DOTween Utility Panel активирован модуль **UI**. Импортируй пространство имён:



```csharp
using DG.Tweening;
// Для UI работ дополнительный using не нужен,
// методы расширения уже доступны для UI компонентов
```

### DOAnchorPos — движение UI элементов

`RectTransform.DOAnchorPos` — это **главный метод для движения UI**. Используй именно его, а не `DOMove` для Canvas элементов.



```csharp
using UnityEngine;
using DG.Tweening;

public class UIMovement : MonoBehaviour
{
    [SerializeField] private RectTransform panel;
    [SerializeField] private RectTransform button;
    
    void Start()
    {
        // Переместить панель к anchoredPosition (0, 0)
        panel.DOAnchorPos(Vector2.zero, 0.5f);
        
        // Только по одной оси
        panel.DOAnchorPosX(100f, 0.3f);
        panel.DOAnchorPosY(-50f, 0.3f);
        
        // Движение из-за экрана
        Vector2 hiddenPosition = new Vector2(0f, -Screen.height);
        Vector2 visiblePosition = new Vector2(0f, 0f);
        
        panel.anchoredPosition = hiddenPosition;
        panel.DOAnchorPos(visiblePosition, 0.5f).SetEase(Ease.OutCubic);
        
        // Эффект "тряски" кнопки при ошибке
        button.DOShakeAnchorPos(duration: 0.3f, strength: 20f, vibrato: 10);
    }
    
    void OnDestroy()
    {
        DOTween.Kill(this);
    }
}
```

### DOColor — изменение цвета UI



```csharp
using UnityEngine;
using UnityEngine.UI;
using DG.Tweening;

public class UIColorExamples : MonoBehaviour
{
    [SerializeField] private Image backgroundImage;
    [SerializeField] private Image iconImage;
    [SerializeField] private Button button;
    
    void Start()
    {
        // Изменить цвет Image
        backgroundImage.DOColor(Color.red, 0.5f);
        
        // Изменить только прозрачность Image
        iconImage.DOFade(0f, 1f); // исчезнуть
        iconImage.DOFade(1f, 1f); // появиться
        
        // Мигание
        iconImage.DOFade(0f, 0.3f).SetLoops(-1, LoopType.Yoyo);
        
        // Эффект наведения на кнопку
        Color normalColor = Color.white;
        Color hoverColor = new Color(0.8f, 0.9f, 1f);
        
        button.image.DOColor(hoverColor, 0.15f);
        button.image.DOColor(normalColor, 0.15f);
    }
    
    void OnDestroy()
    {
        DOTween.Kill(this);
    }
}
```

### MeshPro



```csharp
using UnityEngine;
using DG.Tweening;
using TMPro;

public class MeshProExamples : MonoBehaviour
{
    [SerializeField] private MeshProUGUI title;
    [SerializeField] private MeshProUGUI subtitle;
    
    void Start()
    {
        // Изменить цвет текста
        title.DOColor(Color.yellow, 1f);
        
        // Изменить прозрачность текста
        title.DOFade(0f, 0.5f);
        title.DOFade(1f, 0.5f);
        
        // Анимация набора текста — эффект печатной машинки
        subtitle. = "";
        string full = "Добро пожаловать в игру!";
        
        // DOTween.To для анимации счётчика символов
        DOTween.To(
            () => 0f,
            value => subtitle. = full.Substring(0, Mathf.RoundToInt(value)),
            full.Length,
            full.Length * 0.05f // 0.05 сек на символ
        ).SetEase(Ease.Linear);
        
        // Изменение размера шрифта
        title.DOFontSize(72f, 0.5f);
    }
    
    void OnDestroy()
    {
        DOTween.Kill(this);
    }
}
```

### CanvasGroup для работы с группами UI



```csharp
using UnityEngine;
using DG.Tweening;

public class UIPanel : MonoBehaviour
{
    [SerializeField] private CanvasGroup canvasGroup;
    
    // Показать панель
    public void Show(float duration = 0.3f)
    {
        gameObject.SetActive(true);
        canvasGroup.alpha = 0f;
        canvasGroup.interactable = false;
        canvasGroup.blocksRaycasts = true;
        
        canvasGroup.DOFade(1f, duration)
            .OnComplete(() =>
            {
                canvasGroup.interactable = true;
            });
    }
    
    // Скрыть панель
    public void Hide(float duration = 0.3f)
    {
        canvasGroup.interactable = false;
        
        canvasGroup.DOFade(0f, duration)
            .OnComplete(() =>
            {
                canvasGroup.blocksRaycasts = false;
                gameObject.SetActive(false);
            });
    }
    
    void OnDestroy()
    {
        DOTween.Kill(this);
    }
}
```

---

## Loops

Зацикливание позволяет повторять твин заданное количество раз с разным поведением.

### Типы LoopType



```csharp
using UnityEngine;
using DG.Tweening;

public class LoopExamples : MonoBehaviour
{
    void Start()
    {
        // SetLoops(количество, тип)
        // Количество -1 = бесконечно
        
        // Restart — каждый раз начинает с начального значения
        // A -> B, A -> B, A -> B, ...
        transform.DOMoveX(5f, 1f).SetLoops(-1, LoopType.Restart);
        
        // Yoyo — туда и обратно
        // A -> B -> A -> B -> A -> ...
        transform.DOMoveX(5f, 1f).SetLoops(-1, LoopType.Yoyo);
        
        // Incremental — каждый раз ДОБАВЛЯЕТ к предыдущему значению
        // Позиция растёт: 0 -> 5 -> 10 -> 15 -> ...
        transform.DOMoveX(5f, 1f).SetLoops(-1, LoopType.Incremental);
        
        // Конкретное количество повторений
        transform.DOScale(1.2f, 0.3f).SetLoops(6, LoopType.Yoyo); // 3 качания туда-обратно
        
        // OnStepComplete вызывается после каждого повторения
        transform.DOMoveX(5f, 1f)
            .SetLoops(5, LoopType.Restart)
            .OnStepComplete(() => Debug.Log("Шаг завершён!"))
            .OnComplete(() => Debug.Log("Все 5 шагов завершены!"));
    }
    
    void OnDestroy()
    {
        DOTween.Kill(this);
    }
}
```

### Практические примеры зацикливания



```csharp
using UnityEngine;
using DG.Tweening;

public class PracticalLoops : MonoBehaviour
{
    [SerializeField] private Transform loadingSpinner;
    [SerializeField] private Transform breathingIcon;
    [SerializeField] private Transform bouncingBall;
    
    void Start()
    {
        // Спиннер загрузки — бесконечное вращение
        loadingSpinner.DORotate(
            new Vector3(0f, 0f, -360f), 
            1f, 
            RotateMode.LocalAxisAdd
        ).SetLoops(-1, LoopType.Restart).SetEase(Ease.Linear);
        
        // "Дышащая" иконка — пульсация масштаба
        breathingIcon.DOScale(1.1f, 1.5f)
            .SetLoops(-1, LoopType.Yoyo)
            .SetEase(Ease.InOutSine);
        
        // Прыгающий мяч — движение вверх-вниз с отскоком
        bouncingBall.DOMoveY(3f, 0.8f)
            .SetLoops(-1, LoopType.Yoyo)
            .SetEase(Ease.OutBounce);
    }
    
    void OnDestroy()
    {
        DOTween.Kill(this);
    }
}
```

---

## Управление твинами

### Методы управления на экземпляре



```csharp
using UnityEngine;
using DG.Tweening;

public class TweenControl : MonoBehaviour
{
    private Tween moveTween;
    private Sequence mySequence;
    
    void Start()
    {
        // Сохраняй ссылку на твин для управления им
        moveTween = transform.DOMoveX(10f, 3f);
        
        // Проверить статус
        Debug.Log($"Активен: {moveTween.IsActive()}");
        Debug.Log($"Играет: {moveTween.IsPlaying()}");
        Debug.Log($"Завершён: {moveTween.IsComplete()}");
    }
    
    public void PauseTween()
    {
        moveTween.Pause();
        // Или: DOTween.Pause("myId");
    }
    
    public void PlayTween()
    {
        moveTween.Play();
        // Или: DOTween.Play("myId");
    }
    
    public void TogglePause()
    {
        moveTween.TogglePause();
    }
    
    public void RestartTween()
    {
        // Перезапустить с начала
        moveTween.Restart();
        // Или: DOTween.Restart("myId");
    }
    
    public void RewindTween()
    {
        // Перемотать к начальному состоянию
        moveTween.Rewind();
    }
    
    public void FlipTween()
    {
        // Инвертировать направление (вперёд <-> назад)
        moveTween.Flip();
    }
    
    public void GotoPosition()
    {
        // Перейти к конкретному времени (в секундах)
        moveTween.Goto(1.5f, andPlay: true);
    }
    
    public void KillTween()
    {
        // Уничтожить твин
        // complete: true — сначала выполнить до конца
        moveTween.Kill(complete: false);
    }
    
    void OnDestroy()
    {
        // Уничтожить все твины, привязанные к этому объекту
        DOTween.Kill(this);
    }
}
```

### DOKill — правильная очистка памяти

Это **критически важный момент**. Если объект уничтожается, а его твины продолжают работать — получаешь ошибку `MissingReferenceException`.



```csharp
using UnityEngine;
using DG.Tweening;

public class SafeTweenUsage : MonoBehaviour
{
    void Start()
    {
        // Метод 1: Привязка к gameObject (рекомендуется)
        transform.DOMoveX(5f, 1f).SetTarget(gameObject);
        
        // Метод 2: Привязка через SetId
        transform.DOScale(2f, 1f).SetId("myObjectTween");
        
        // Метод 3: Автоматическая очистка через SetLink
        // Твин автоматически убьётся при деактивации gameObject
        transform.DORotate(Vector3.up * 180f, 2f)
                 .SetLink(gameObject, LinkBehaviour.KillOnDisable);
    }
    
    void OnDisable()
    {
        // Остановить твины когда объект деактивирован
        DOTween.Kill(gameObject, complete: false);
    }
    
    void OnDestroy()
    {
        // ВСЕГДА добавляй это! Убивает все твины этого объекта
        DOTween.Kill(this);
        // Альтернатива:
        // transform.DOKill();
        // gameObject.DOKill(); // если использовал SetTarget(gameObject)
    }
}
```

### SetLink — автоматическое управление жизнью твина



```csharp
using UnityEngine;
using DG.Tweening;

public class SetLinkExample : MonoBehaviour
{
    void Start()
    {
        // LinkBehaviour определяет, что происходит с твином
        // когда GameObject меняет состояние
        
        transform.DOMoveX(5f, 2f).SetLink(gameObject, LinkBehaviour.KillOnDisable);
        // Убить при Disable
        
        transform.DOScale(2f, 2f).SetLink(gameObject, LinkBehaviour.PauseOnDisable);
        // Поставить на паузу при Disable, возобновить при Enable
        
        transform.DORotate(Vector3.up * 90f, 2f)
                 .SetLink(gameObject, LinkBehaviour.KillOnDestroy);
        // Убить при Destroy (поведение по умолчанию)
    }
    
    // OnDestroy можно не писать если используешь SetLink с KillOnDestroy,
    // но хорошей практикой считается писать всегда
    void OnDestroy()
    {
        DOTween.Kill(this);
    }
}
```

### Глобальные операции над несколькими твинами



```csharp
using UnityEngine;
using DG.Tweening;

public class GlobalTweenManagement : MonoBehaviour
{
    void Start()
    {
        // Назначить ID
        transform.DOMoveX(5f, 2f).SetId("group1");
        transform.DOScale(2f, 2f).SetId("group1");
        transform.DORotate(Vector3.up * 90f, 2f).SetId("group2");
    }
    
    public void PauseAll()
    {
        DOTween.PauseAll();
    }
    
    public void PlayAll()
    {
        DOTween.PlayAll();
    }
    
    public void KillAll()
    {
        DOTween.KillAll();
    }
    
    public void PauseGroup()
    {
        // Пауза всех твинов с ID "group1"
        DOTween.Pause("group1");
    }
    
    public void KillGroup()
    {
        DOTween.Kill("group1");
    }
    
    // Получить информацию
    public void PrintInfo()
    {
        Debug.Log($"Всего твинов: {DOTween.TotalActiveTweens()}");
        Debug.Log($"Играющих: {DOTween.TotalPlayingTweens()}");
        Debug.Log($"Поставленных на паузу: {DOTween.TotalPausedTweens()}");
    }
    
    void OnDestroy()
    {
        DOTween.Kill(this);
    }
}
```

---

## Практическое задание

Создадим анимацию появления главного меню. Заголовок влетает сверху, кнопки появляются снизу с задержкой каждая.

### Структура сцены



```csharp
Canvas
├── MainMenuPanel (Panel)
│   ├── Title (MeshPro)
│   ├── ButtonsContainer (Vertical Layout Group)
│   │   ├── PlayButton (Button)
│   │   ├── SettingsButton (Button)
│   │   └── QuitButton (Button)
│   └── BackgroundImage (Image)
```

### Полный код анимации главного меню



```csharp
using UnityEngine;
using UnityEngine.UI;
using DG.Tweening;
using TMPro;

public class MainMenuAnimator : MonoBehaviour
{
    [Header("Элементы UI")]
    [SerializeField] private RectTransform title;
    [SerializeField] private RectTransform[] buttons;        // Массив кнопок
    [SerializeField] private CanvasGroup backgroundOverlay;   // Фон с затемнением
    [SerializeField] private CanvasGroup mainPanel;          // Вся панель меню
    
    [Header("Настройки анимации")]
    [SerializeField] private float titleFlyDuration = 0.7f;
    [SerializeField] private float buttonDelay = 0.15f;     // Задержка между кнопками
    [SerializeField] private float buttonDuration = 0.5f;
    [SerializeField] private float initialDelay = 0.3f;     // Задержка перед стартом
    
    [Header("Позиции")]
    [SerializeField] private float titleHiddenOffsetY = 300f; // Насколько выше экрана
    [SerializeField] private float buttonHiddenOffsetY = -200f; // Насколько ниже экрана
    
    // Хранить ссылку на Sequence для управления
    private Sequence _introSequence;
    
    void Awake()
    {
        // Скрываем все элементы ДО запуска анимации
        PrepareInitialState();
    }
    
    void Start()
    {
        // Запускаем анимацию появления
        PlayIntroAnimation();
    }
    
    private void PrepareInitialState()
    {
        // Скрываем фон
        if (backgroundOverlay != null)
        {
            backgroundOverlay.alpha = 0f;
        }
        
        // Убираем заголовок наверх
        Vector2 titleStartPos = new Vector2(
            title.anchoredPosition.x,
            title.anchoredPosition.y + titleHiddenOffsetY
        );
        title.anchoredPosition = titleStartPos;
        
        // Скрываем заголовок (прозрачный)
        CanvasGroup titleCanvasGroup = title.GetComponent<CanvasGroup>();
        if (titleCanvasGroup != null) titleCanvasGroup.alpha = 0f;
        
        // Убираем кнопки вниз и делаем прозрачными
        foreach (RectTransform button in buttons)
        {
            CanvasGroup buttonCG = button.GetComponent<CanvasGroup>();
            if (buttonCG != null) buttonCG.alpha = 0f;
            
            button.anchoredPosition = new Vector2(
                button.anchoredPosition.x,
                button.anchoredPosition.y + buttonHiddenOffsetY
            );
        }
    }
    
    public void PlayIntroAnimation()
    {
        // Убиваем предыдущую анимацию если она есть
        _introSequence?.Kill();
        
        // Создаём новую Sequence
        _introSequence = DOTween.Sequence();
        
        // Шаг 1: Небольшая пауза перед стартом
        _introSequence.AppendInterval(initialDelay);
        
        // Шаг 2: Появление фонового затемнения
        if (backgroundOverlay != null)
        {
            _introSequence.Append(
                backgroundOverlay.DOFade(1f, 0.4f).SetEase(Ease.OutQuad)
            );
        }
        
        // Шаг 3: Заголовок влетает сверху
        // Параллельно с его движением — появление прозрачности
        CanvasGroup titleCG = title.GetComponent<CanvasGroup>();
        
        _introSequence.Append(
            title.DOAnchorPosY(
                title.anchoredPosition.y - titleHiddenOffsetY + titleHiddenOffsetY,
                titleFlyDuration
            )
            .SetEase(Ease.OutCubic)
        );
        
        // Если есть CanvasGroup — проявляем параллельно с движением
        if (titleCG != null)
        {
            _introSequence.Join(
                titleCG.DOFade(1f, titleFlyDuration * 0.7f).SetEase(Ease.OutQuad)
            );
        }
        
        // Шаг 4: Небольшая пауза после заголовка
        _introSequence.AppendInterval(0.1f);
        
        // Шаг 5: Кнопки появляются снизу с задержкой между каждой
        for (int i = 0; i < buttons.Length; i++)
        {
            RectTransform button = buttons[i];
            CanvasGroup buttonCG = button.GetComponent<CanvasGroup>();
            
            // Целевая позиция (текущая + смещение, которое добавили в PrepareInitialState)
            Vector2 targetPos = new Vector2(
                button.anchoredPosition.x,
                button.anchoredPosition.y - buttonHiddenOffsetY
            );
            
            // Движение кнопки вверх
            _introSequence.Append(
                button.DOAnchorPos(targetPos, buttonDuration).SetEase(Ease.OutBack)
            );
            
            // Появление прозрачности параллельно с движением
            if (buttonCG != null)
            {
                _introSequence.Join(
                    buttonCG.DOFade(1f, buttonDuration * 0.8f).SetEase(Ease.OutQuad)
                );
            }
            
            // Задержка перед следующей кнопкой (кроме последней)
            if (i < buttons.Length - 1)
            {
                _introSequence.AppendInterval(buttonDelay);
            }
        }
        
        // Финальный callback
        _introSequence.OnComplete(() =>
        {
            Debug.Log("Анимация главного меню завершена!");
            // Здесь можно, например, включить интерактивность кнопок
        });
        
        // Запустить
        _introSequence.Play();
    }
    
    // Анимация выхода из меню (например, при нажатии кнопки Play)
    public void PlayOutroAnimation(System.Action onComplete = null)
    {
        // Убиваем вступительную анимацию если она ещё идёт
        _introSequence?.Kill();
        
        Sequence outroSequence = DOTween.Sequence();
        
        // Кнопки уходят вниз быстро
        for (int i = buttons.Length - 1; i >= 0; i--)
        {
            RectTransform button = buttons[i];
            CanvasGroup buttonCG = button.GetComponent<CanvasGroup>();
            
            Vector2 hiddenPos = new Vector2(
                button.anchoredPosition.x,
                button.anchoredPosition.y + buttonHiddenOffsetY
            );
            
            outroSequence.Append(
                button.DOAnchorPos(hiddenPos, 0.2f).SetEase(Ease.InQuad)
            );
            
            if (buttonCG != null)
            {
                outroSequence.Join(
                    buttonCG.DOFade(0f, 0.2f)
                );
            }
            
            outroSequence.AppendInterval(0.05f);
        }
        
        // Заголовок улетает вверх
        outroSequence.Append(
            title.DOAnchorPosY(
                title.anchoredPosition.y + titleHiddenOffsetY, 
                0.4f
            ).SetEase(Ease.InCubic)
        );
        
        // Фон гаснет
        if (backgroundOverlay != null)
        {
            outroSequence.Join(
                backgroundOverlay.DOFade(0f, 0.4f)
            );
        }
        
        outroSequence.OnComplete(() =>
        {
            onComplete?.Invoke();
        });
    }
    
    void OnDestroy()
    {
        // Критически важно! Убиваем все твины этого объекта
        DOTween.Kill(this);
        // Также убиваем Sequence явно для надёжности
        _introSequence?.Kill();
    }
}
```

### Вспомогательный класс: эффект кнопки при нажатии



```csharp
using UnityEngine;
using UnityEngine.EventSystems;
using DG.Tweening;

public class ButtonPressEffect : MonoBehaviour, IPointerDownHandler, IPointerUpHandler, IPointerEnterHandler, IPointerExitHandler
{
    [SerializeField] private float pressScale = 0.92f;
    [SerializeField] private float hoverScale = 1.05f;
    [SerializeField] private float animDuration = 0.1f;
    
    private Vector3 _originalScale;
    
    void Awake()
    {
        _originalScale = transform.localScale;
    }
    
    public void OnPointerEnter(PointerEventData eventData)
    {
        transform.DOScale(_originalScale * hoverScale, animDuration)
                 .SetEase(Ease.OutQuad);
    }
    
    public void OnPointerExit(PointerEventData eventData)
    {
        transform.DOScale(_originalScale, animDuration)
                 .SetEase(Ease.OutQuad);
    }
    
    public void OnPointerDown(PointerEventData eventData)
    {
        transform.DOScale(_originalScale * pressScale, animDuration)
                 .SetEase(Ease.OutQuad);
    }
    
    public void OnPointerUp(PointerEventData eventData)
    {
        transform.DOScale(_originalScale, animDuration)
                 .SetEase(Ease.OutBack);
    }
    
    void OnDestroy()
    {
        DOTween.Kill(this);
    }
}
```

### Подключение в Inspector

1. Создай `Canvas` → `Panel` → добавь дочерние объекты по структуре выше
2. На `MainMenuPanel` добавь компонент `MainMenuAnimator`
3. Перетащи ссылки в поля Inspector:
    - `Title ` → объект с MeshPro заголовком
    - `Buttons` → заполни массив тремя кнопками
    - `Background Overlay` → CanvasGroup на подложке
4. На каждую кнопку добавь компонент `ButtonPressEffect`
5. Настрой параметры анимации по вкусу

---

## Проверь себя

Ответь на вопросы и выполни задания. Это поможет закрепить материал.

---

### 📝 Теоретические вопросы

**1.** Чем `DOAnchorPos` отличается от `DOMove` для UI элементов? Почему важно использовать именно `DOAnchorPos`?

**2.** Объясни разницу между `Append` и `Join` в Sequence. Что произойдёт если использовать только `Join` без предшествующего `Append`?

**3.** Что означает `SetLoops(-1, LoopType.Yoyo)`? Как остановить такой бесконечный твин?

**4.** Почему обязательно нужно вызывать `DOTween.Kill(this)` в методе `OnDestroy`? Что произойдёт если этого не сделать?

**5.** В чём разница между `Ease.InQuad` и `Ease.OutQuad`? Какой из них лучше подходит для анимации появления UI элемента и почему?

---

### 💻 Практические задания

**Задание 1: Анимация монеты**

Создай скрипт `CoinCollectEffect`, который при вызове метода `PlayCollectAnimation()`:

- Монета увеличивается до 1.5x масштаба за 0.1 сек
- Затем уменьшается до 0 за 0.3 сек
- Одновременно с уменьшением улетает вверх на 100 единиц
- При завершении вызывает `Destroy(gameObject)`

**Задание 2: Тряска экрана при ошибке**

Напиши метод `ShakeOnError()` для поля ввода пароля:

- Поле трясётся горизонтально (DOShakeAnchorPos или через DOPunchPosition)
- Цвет рамки поля меняется на красный
- Через 0.5 секунды цвет возвращается к белому
- Не забудь про `OnDestroy`

**Задание 3: Полоса загрузки**

Создай `LoadingBarAnimator` с методом `AnimateLoading(float targetValue)`:

- `Image` с `Image.Type = Filled` заполняется от текущего значения до `targetValue`
- Длительность зависит от расстояния: `duration = Mathf.Abs(targetValue - currentFill) * 2f`
- При достижении 1.0f (100%) запускается анимация исчезновения всей панели

**Задание 4 (сложное): Рейтинговые звёзды**

Создай `StarRatingAnimator` с массивом из 5 звёзд (`Image[]`). Метод `ShowRating(int stars)` должен:

- Сначала все звёзды уходят вниз за экран
- Затем последовательно появляются снизу одна за другой с задержкой 0.2 сек
- Звёзды до `stars` окрашиваются в жёлтый, остальные — в серый
- Активные звёзды "подпрыгивают" (DOPunchScale) при появлении

---

### 🔍 Найди ошибки в коде

**Код 1:**



```csharp
public class BuggyAnimation : MonoBehaviour
{
    void Start()
    {
        for (int i = 0; i < 10; i++)
        {
            transform.DOMoveX(i * 2f, 0.5f); // Ошибка здесь
        }
    }
}
```

_Подсказка: что происходит когда запускаешь несколько твинов на одно свойство без управления?_

**Код 2:**



```csharp
public class AnotherBug : MonoBehaviour
{
    void Start()
    {
        Sequence seq = DOTween.Sequence();
        seq.Join(transform.DOMoveX(5f, 1f));  // Ошибка здесь
        seq.Join(transform.DOMoveY(3f, 1f));
        seq.Append(transform.DOScale(2f, 0.5f));
    }
    
    // OnDestroy отсутствует — это тоже ошибка!
}
```

_Подсказка: с чего должна начинаться Sequence?_

**Код 3:**



```csharp
public class TimingBug : MonoBehaviour
{
    [SerializeField] private CanvasGroup panel;
    
    public void HideAndDestroy()
    {
        panel.DOFade(0f, 1f);
        Destroy(gameObject); // Ошибка здесь
    }
}
```

_Подсказка: что происходит с твином когда объект уничтожается до завершения анимации?_

---

### ✅ Ответы на вопрос "Найди ошибки"

<details> <summary>Раскрой когда проверишь сам</summary>

**Код 1:** Запускаются 10 одновременных твинов на `transform.position.x`. Они конфликтуют между собой. Нужно либо использовать `Sequence` и `Append`, либо добавлять `SetDelay(i * 0.5f)` к каждому твину.

**Код 2:** `Sequence` не может начинаться с `Join`. Первый элемент всегда должен быть `Append` или `Insert`. Плюс отсутствует `OnDestroy` с `DOTween.Kill(this)`.

**Код 3:** `Destroy(gameObject)` вызывается немедленно, уничтожая `panel` до завершения анимации. Нужно вызывать `Destroy` в `OnComplete`:



```csharp
panel.DOFade(0f, 1f).OnComplete(() => Destroy(gameObject));
```

</details>

---

### 📚 Что изучить дальше

После освоения этого руководства, следующие темы расширят возможности:

- **DOPath** (DOTween Pro) — анимация движения по кривым Безье
- **DOTween визуальный редактор** (DOTween Pro) — настройка анимаций без кода
- **DOTween.To с шейдерами** — анимация параметров материалов
- **Интеграция с UniTask/async-await** — современный подход к асинхронным анимациям
- **DOTween + объектные пулы** — оптимизация для частых повторяющихся анимаций

---

_Документация DOTween: [dotween.demigiant.com/documentation](http://dotween.demigiant.com/documentation.php)_