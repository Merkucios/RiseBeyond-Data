## Содержание

- [1. Введение — проблема Instantiate/Destroy и GC {#введение}](#1.%20%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%E2%80%94%20%D0%BF%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0%20Instantiate/Destroy%20%D0%B8%20GC%20%7B#%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%7D)
	- [Что происходит под капотом](#%D0%A7%D1%82%D0%BE%20%D0%BF%D1%80%D0%BE%D0%B8%D1%81%D1%85%D0%BE%D0%B4%D0%B8%D1%82%20%D0%BF%D0%BE%D0%B4%20%D0%BA%D0%B0%D0%BF%D0%BE%D1%82%D0%BE%D0%BC)
	- [Проблема Garbage Collector](#%D0%9F%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0%20Garbage%20Collector)
	- [Концептуальное сравнение производительности](#%D0%9A%D0%BE%D0%BD%D1%86%D0%B5%D0%BF%D1%82%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5%20%D1%81%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BF%D1%80%D0%BE%D0%B8%D0%B7%D0%B2%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8)
- [2. Концепция пула объектов {#концепция}](#2.%20%D0%9A%D0%BE%D0%BD%D1%86%D0%B5%D0%BF%D1%86%D0%B8%D1%8F%20%D0%BF%D1%83%D0%BB%D0%B0%20%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BE%D0%B2%20%7B#%D0%BA%D0%BE%D0%BD%D1%86%D0%B5%D0%BF%D1%86%D0%B8%D1%8F%7D)
	- [Принцип работы](#%D0%9F%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B)
	- [Жизненный цикл объекта в пуле](#%D0%96%D0%B8%D0%B7%D0%BD%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9%20%D1%86%D0%B8%D0%BA%D0%BB%20%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%B0%20%D0%B2%20%D0%BF%D1%83%D0%BB%D0%B5)
	- [Когда использовать Object Pool](#%D0%9A%D0%BE%D0%B3%D0%B4%D0%B0%20%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%20Object%20Pool)
- [3. Реализация простого пула на Stack< T > {#простой-пул}](#3.%20%D0%A0%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%BF%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%B3%D0%BE%20%D0%BF%D1%83%D0%BB%D0%B0%20%D0%BD%D0%B0%20Stack%3C%20T%20%3E%20%7B#%D0%BF%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%B9-%D0%BF%D1%83%D0%BB%7D)
	- [Почему Stack, а не List или Queue?](#%D0%9F%D0%BE%D1%87%D0%B5%D0%BC%D1%83%20Stack,%20%D0%B0%20%D0%BD%D0%B5%20List%20%D0%B8%D0%BB%D0%B8%20Queue?)
	- [Базовый пул GameObject](#%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B9%20%D0%BF%D1%83%D0%BB%20GameObject)
	- [Использование SimpleGameObjectPool](#%D0%98%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20SimpleGameObjectPool)
- [4. Unity встроенный ObjectPool< T > {#unity-pool}](#4.%20Unity%20%D0%B2%D1%81%D1%82%D1%80%D0%BE%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9%20ObjectPool%3C%20T%20%3E%20%7B#unity-pool%7D)
	- [Базовое API](#%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D0%BE%D0%B5%20API)
	- [Пример: пул для пуль с ObjectPool< T >](#%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80:%20%D0%BF%D1%83%D0%BB%20%D0%B4%D0%BB%D1%8F%20%D0%BF%D1%83%D0%BB%D1%8C%20%D1%81%20ObjectPool%3C%20T%20%3E)
	- [Параметр collectionCheck](#%D0%9F%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%20collectionCheck)
- [5. Интеграция с OnEnable/OnDisable {#onenable-ondisable}](#5.%20%D0%98%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F%20%D1%81%20OnEnable/OnDisable%20%7B#onenable-ondisable%7D)
	- [Почему это важно](#%D0%9F%D0%BE%D1%87%D0%B5%D0%BC%D1%83%20%D1%8D%D1%82%D0%BE%20%D0%B2%D0%B0%D0%B6%D0%BD%D0%BE)
	- [Правильная реализация компонента для пула](#%D0%9F%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%BA%D0%BE%D0%BC%D0%BF%D0%BE%D0%BD%D0%B5%D0%BD%D1%82%D0%B0%20%D0%B4%D0%BB%D1%8F%20%D0%BF%D1%83%D0%BB%D0%B0)
	- [Частые ошибки с OnEnable/OnDisable](#%D0%A7%D0%B0%D1%81%D1%82%D1%8B%D0%B5%20%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D0%B8%20%D1%81%20OnEnable/OnDisable)
- [6. Generic Pool для любых типов {#generic-pool}](#6.%20Generic%20Pool%20%D0%B4%D0%BB%D1%8F%20%D0%BB%D1%8E%D0%B1%D1%8B%D1%85%20%D1%82%D0%B8%D0%BF%D0%BE%D0%B2%20%7B#generic-pool%7D)
	- [Интерфейс для объектов, поддерживающих пул](#%D0%98%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%20%D0%B4%D0%BB%D1%8F%20%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BE%D0%B2,%20%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%B8%D0%B2%D0%B0%D1%8E%D1%89%D0%B8%D1%85%20%D0%BF%D1%83%D0%BB)
	- [Generic Pool Manager](#Generic%20Pool%20Manager)
	- [Использование Generic Pool Manager](#%D0%98%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20Generic%20Pool%20Manager)
- [7. Практическое задание: пул для пуль {#практика}](#7.%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5:%20%D0%BF%D1%83%D0%BB%20%D0%B4%D0%BB%D1%8F%20%D0%BF%D1%83%D0%BB%D1%8C%20%7B#%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0%7D)
	- [Структура проекта](#%D0%A1%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
	- [IDamageable интерфейс](#IDamageable%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81)
	- [Компонент пули — полная версия](#%D0%9A%D0%BE%D0%BC%D0%BF%D0%BE%D0%BD%D0%B5%D0%BD%D1%82%20%D0%BF%D1%83%D0%BB%D0%B8%20%E2%80%94%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%B0%D1%8F%20%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%8F)
	- [Пул пуль — специализированная версия](#%D0%9F%D1%83%D0%BB%20%D0%BF%D1%83%D0%BB%D1%8C%20%E2%80%94%20%D1%81%D0%BF%D0%B5%D1%86%D0%B8%D0%B0%D0%BB%D0%B8%D0%B7%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%B0%D1%8F%20%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%8F)
	- [Компонент стрельбы](#%D0%9A%D0%BE%D0%BC%D0%BF%D0%BE%D0%BD%D0%B5%D0%BD%D1%82%20%D1%81%D1%82%D1%80%D0%B5%D0%BB%D1%8C%D0%B1%D1%8B)
	- [Компонент автоматического возврата (без пули)](#%D0%9A%D0%BE%D0%BC%D0%BF%D0%BE%D0%BD%D0%B5%D0%BD%D1%82%20%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B3%D0%BE%20%D0%B2%D0%BE%D0%B7%D0%B2%D1%80%D0%B0%D1%82%D0%B0%20(%D0%B1%D0%B5%D0%B7%20%D0%BF%D1%83%D0%BB%D0%B8))
	- [Тестовая сцена — как всё соединить](#%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%B0%D1%8F%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%20%E2%80%94%20%D0%BA%D0%B0%D0%BA%20%D0%B2%D1%81%D1%91%20%D1%81%D0%BE%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%82%D1%8C)
	- [Настройка в Unity Editor](#%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0%20%D0%B2%20Unity%20Editor)
- [8. Проверь себя {#проверка}](#8.%20%D0%9F%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D1%8C%20%D1%81%D0%B5%D0%B1%D1%8F%20%7B#%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0%7D)
	- [Теоретические вопросы](#%D0%A2%D0%B5%D0%BE%D1%80%D0%B5%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%B2%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D1%8B)
	- [Практические задания](#%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F)
	- [Чеклист для самопроверки](#%D0%A7%D0%B5%D0%BA%D0%BB%D0%B8%D1%81%D1%82%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%B0%D0%BC%D0%BE%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B8)
- [Итоги](#%D0%98%D1%82%D0%BE%D0%B3%D0%B8)




---

## 1. Введение — проблема Instantiate/Destroy и GC {#введение}

Когда разработчики начинают делать первые игры в Unity, они привычно используют `Instantiate` для создания объектов и `Destroy` для их уничтожения. Это выглядит логично и понятно — создал пулю, она улетела, уничтожил. Но за этой простотой скрывается серьёзная проблема производительности.

### Что происходит под капотом



```csharp
// Так делают новички — и это работает, но плохо масштабируется
public class BadShooter : MonoBehaviour
{
    [SerializeField] private GameObject bulletPrefab;

    void Update()
    {
        if (Input.GetButtonDown("Fire1"))
        {
            // Каждый кадр нажатия — выделение памяти в heap!
            GameObject bullet = Instantiate(bulletPrefab, transform.position, transform.rotation);
        }
    }
}

public class BadBullet : MonoBehaviour
{
    void OnCollisionEnter(Collision collision)
    {
        // Освобождение памяти — провоцируем GC
        Destroy(gameObject);
    }
}
```

Каждый вызов `Instantiate` делает следующее:

- Выделяет память в **управляемой куче (managed heap)**
- Копирует данные префаба
- Инициализирует все компоненты
- Регистрирует объект в движке Unity

Каждый вызов `Destroy` помечает объект для удаления, после чего **Garbage Collector (GC)** должен освободить память.

### Проблема Garbage Collector

GC в Unity работает по принципу **stop-the-world**: когда он запускается, он **останавливает все потоки** для сборки мусора. Это проявляется как:



```csharp
Типичная картина в Profiler:
Frame 1:  2ms  ✅ нормально
Frame 2:  2ms  ✅ нормально  
Frame 3:  2ms  ✅ нормально
Frame 47: 47ms ❌ GC spike! (заметный фриз)
Frame 48: 2ms  ✅ нормально
```

При интенсивном создании объектов (частая стрельба, эффекты частиц, враги) эти спайки происходят **регулярно и ощутимо**.

### Концептуальное сравнение производительности

|Операция|Instantiate/Destroy|Object Pool|
|---|---|---|
|Создание объекта|~0.1–1ms|~0.001ms|
|Уничтожение|~0.05ms + GC|~0.001ms|
|Давление на GC|Высокое|Минимальное|
|Аллокации heap|Каждый раз|Только при инициализации|
|Риск фризов|Высокий|Отсутствует|

> **Важно**: Конкретные цифры зависят от платформы, сложности объекта и окружения. На мобильных устройствах разница может быть в 10–100 раз ощутимее, чем на ПК.

---

## 2. Концепция пула объектов {#концепция}

**Object Pool (пул объектов)** — это паттерн проектирования, при котором объекты не уничтожаются после использования, а **деактивируются и возвращаются в хранилище** для повторного использования.

### Принцип работы



```csharp
┌─────────────────────────────────────────────────────┐
│                    OBJECT POOL                       │
│                                                      │
│  [●][●][●]  ← Неактивные объекты (ждут в пуле)     │
│                                                      │
│  Запрос объекта:                                     │
│  Pool ──► Достать из стека ──► Активировать ──► Игра│
│                                                      │
│  Возврат объекта:                                    │
│  Игра ──► Деактивировать ──► Положить в стек ──► Pool│
└─────────────────────────────────────────────────────┘
```

### Жизненный цикл объекта в пуле



```csharp
Традиционный подход:
Создать → Использовать → Уничтожить → [GC] → Создать → ...

Пул объектов:
Создать (один раз) → Активировать → Использовать → Деактивировать → Активировать → ...
       ↑___________________________________________________|
```

### Когда использовать Object Pool

✅ **Подходит для:**

- Пули, снаряды, лазеры
- Эффекты частиц (взрывы, искры)
- Враги волнами
- UI-элементы в списках
- Звуковые источники (AudioSource)
- Декали (следы пуль, кровь)

❌ **Не нужен для:**

- Объектов, создаваемых один раз
- Объектов с уникальным состоянием, сложным для сброса
- Очень тяжёлых объектов, которых одновременно мало (< 5–10)

---

## 3. Реализация простого пула на Stack< T > {#простой-пул}

Начнём с создания пула вручную, чтобы понять внутренний механизм. Используем ```csharpStack<T>``` — он даёт O(1) для операций Push/Pop.

### Почему Stack, а не List или Queue?



```csharp
// Stack (LIFO) — оптимален для пула:
// - Pop() и Push() работают за O(1)
// - Последний возвращённый объект — первый выданный
// - Лучше кэшируется в памяти (последние объекты "горячие")

// Queue (FIFO) тоже работает, но Stack обычно предпочтительнее
// List — избыточен, O(n) для поиска
```

### Базовый пул GameObject



```csharp
using System.Collections.Generic;
using UnityEngine;

public class SimpleGameObjectPool : MonoBehaviour
{
    [Header("Настройки пула")]
    [SerializeField] private GameObject prefab;
    [SerializeField] private int initialSize = 20;
    [SerializeField] private bool expandable = true; // Расширять ли пул при нехватке

    private Stack<GameObject> _pool;
    private Transform _poolContainer; // Родитель для неактивных объектов

    private void Awake()
    {
        // Создаём контейнер для удобства в иерархии
        _poolContainer = new GameObject($"[Pool] {prefab.name}").transform;
        _poolContainer.SetParent(transform);

        _pool = new Stack<GameObject>(initialSize);
        
        // Прогрев пула — создаём объекты заранее
        Prewarm(initialSize);
    }

    private void Prewarm(int count)
    {
        for (int i = 0; i < count; i++)
        {
            var obj = CreateNewInstance();
            ReturnToPool(obj);
        }
    }

    private GameObject CreateNewInstance()
    {
        var obj = Instantiate(prefab, _poolContainer);
        obj.SetActive(false);
        return obj;
    }

    /// <summary>
    /// Получить объект из пула
    /// </summary>
    public GameObject Get(Vector3 position, Quaternion rotation)
    {
        GameObject obj;

        if (_pool.Count > 0)
        {
            obj = _pool.Pop();
        }
        else if (expandable)
        {
            // Пул пуст — создаём новый объект
            Debug.LogWarning($"[Pool] {prefab.name}: пул пуст, создаём новый объект. " +
                           $"Рассмотрите увеличение initialSize!");
            obj = CreateNewInstance();
        }
        else
        {
            Debug.LogError($"[Pool] {prefab.name}: пул пуст и не расширяется!");
            return null;
        }

        // Устанавливаем позицию и активируем
        obj.transform.SetPositionAndRotation(position, rotation);
        obj.transform.SetParent(null); // Отсоединяем от контейнера
        obj.SetActive(true);

        return obj;
    }

    /// <summary>
    /// Вернуть объект в пул
    /// </summary>
    public void ReturnToPool(GameObject obj)
    {
        if (obj == null)
        {
            Debug.LogWarning("[Pool] Попытка вернуть null объект!");
            return;
        }

        obj.SetActive(false);
        obj.transform.SetParent(_poolContainer);
        _pool.Push(obj);
    }

    /// <summary>
    /// Текущее количество доступных объектов
    /// </summary>
    public int AvailableCount => _pool.Count;

    private void OnDestroy()
    {
        _pool.Clear();
    }
}
```

### Использование SimpleGameObjectPool



```csharp
public class PoolUser : MonoBehaviour
{
    [SerializeField] private SimpleGameObjectPool bulletPool;

    void Update()
    {
        if (Input.GetButtonDown("Fire1"))
        {
            var bullet = bulletPool.Get(transform.position, transform.rotation);
            
            if (bullet != null)
            {
                // Настраиваем объект после получения из пула
                var rb = bullet.GetComponent<Rigidbody>();
                rb.linearVelocity = transform.forward * 20f;
            }
        }
    }
}
```

> **Проблема** этого подхода: каждый пул привязан к конкретному `MonoBehaviour` и конкретному `GameObject`. Нам нужен более гибкий подход.

---

## 4. Unity встроенный ObjectPool< T > {#unity-pool}
 
Начиная с **Unity 2021**, в пространстве имён `UnityEngine.Pool` появился встроенный `ObjectPool<T>`. Он поддерживает любые типы объектов и предоставляет callbacks для управления жизненным циклом.

### Базовое API



```csharp
using UnityEngine.Pool;

// Конструктор ObjectPool<T>:
var pool = new ObjectPool<T>(
    createFunc:       () => { /* создание */ },   // Обязательно
    actionOnGet:      obj => { /* при выдаче */ }, // Опционально
    actionOnRelease:  obj => { /* при возврате */},// Опционально
    actionOnDestroy:  obj => { /* при очистке */ },// Опционально
    collectionCheck: true,  // Проверка двойного возврата (только в Debug)
    defaultCapacity: 10,    // Начальная ёмкость
    maxSize:         100    // Максимальный размер пула
);

// Получить объект:
T item = pool.Get();

// Вернуть объект:
pool.Release(item);

// Информация:
int count = pool.CountAll;      // Всего объектов
int active = pool.CountActive;  // Активных
int inactive = pool.CountInactive; // В пуле
```

### Пример: пул для пуль с ObjectPool< T >



```csharp
using UnityEngine;
using UnityEngine.Pool;

public class BulletPoolManager : MonoBehaviour
{
    public static BulletPoolManager Instance { get; private set; }

    [Header("Префаб и настройки")]
    [SerializeField] private Bullet bulletPrefab;
    [SerializeField] private int defaultCapacity = 20;
    [SerializeField] private int maxPoolSize = 100;

    private ObjectPool<Bullet> _pool;

    private void Awake()
    {
        // Singleton для удобного доступа
        if (Instance != null && Instance != this)
        {
            Destroy(gameObject);
            return;
        }
        Instance = this;

        InitializePool();
    }

    private void InitializePool()
    {
        _pool = new ObjectPool<Bullet>(
            // 1. Создание нового объекта (вызывается когда пул пуст)
            createFunc: CreateBullet,
            
            // 2. Объект взят из пула
            actionOnGet: OnBulletGet,
            
            // 3. Объект возвращён в пул
            actionOnRelease: OnBulletRelease,
            
            // 4. Объект уничтожается (при переполнении пула)
            actionOnDestroy: OnBulletDestroy,
            
            // 5. Проверка двойного возврата (только в Editor/Development)
            collectionCheck: true,
            
            defaultCapacity: defaultCapacity,
            maxSize: maxPoolSize
        );
    }

    private Bullet CreateBullet()
    {
        var bullet = Instantiate(bulletPrefab);
        // Сообщаем пуле о её пуле (для самостоятельного возврата)
        bullet.SetPool(_pool);
        return bullet;
    }

    private void OnBulletGet(Bullet bullet)
    {
        bullet.gameObject.SetActive(true);
    }

    private void OnBulletRelease(Bullet bullet)
    {
        bullet.gameObject.SetActive(false);
    }

    private void OnBulletDestroy(Bullet bullet)
    {
        // Вызывается если пул переполнен (CountAll > maxSize)
        Destroy(bullet.gameObject);
    }

    /// <summary>
    /// Получить пулю из пула
    /// </summary>
    public Bullet GetBullet(Vector3 position, Quaternion rotation)
    {
        var bullet = _pool.Get();
        bullet.transform.SetPositionAndRotation(position, rotation);
        return bullet;
    }

    /// <summary>
    /// Вернуть пулю в пул
    /// </summary>
    public void ReleaseBullet(Bullet bullet)
    {
        _pool.Release(bullet);
    }

    // Отладочная информация
    private void OnGUI()
    {
        if (_pool == null) return;
        
        GUILayout.Label($"Пул пуль:");
        GUILayout.Label($"  Всего: {_pool.CountAll}");
        GUILayout.Label($"  Активных: {_pool.CountActive}");
        GUILayout.Label($"  В пуле: {_pool.CountInactive}");
    }
}
```

### Параметр collectionCheck



```csharp
// collectionCheck = true (рекомендуется при разработке):
// Если попытаться вернуть объект, который уже в пуле — 
// будет выброшено исключение:
// "InvalidOperationException: Trying to release an object 
//  that has already been released to the pool."

// Это помогает найти баги вида:
pool.Release(bullet); // первый раз — ок
pool.Release(bullet); // второй раз — ИСКЛЮЧЕНИЕ (и это правильно!)

// В Release-сборке отключите для производительности:
collectionCheck: Debug.isDebugBuild
```

---

## 5. Интеграция с OnEnable/OnDisable {#onenable-ondisable}

Ключевой момент при работе с пулами: нужно **переосмыслить жизненный цикл объекта**. Вместо `Start`/`OnDestroy` используем `OnEnable`/`OnDisable`.

### Почему это важно



```csharp
Традиционный жизненный цикл:
Instantiate → Awake → Start → [работа] → OnDestroy → Destroy

Жизненный цикл в пуле:
Instantiate → Awake → [в пуле]
                        ↓
              OnEnable → [работа] → OnDisable → [в пуле]
                              ↑________________________|
```

`Awake` вызывается **один раз** при создании. `OnEnable`/`OnDisable` вызываются **каждый раз** при активации/деактивации.

### Правильная реализация компонента для пула



```csharp
using UnityEngine;
using UnityEngine.Pool;

[RequireComponent(typeof(Rigidbody))]
public class Bullet : MonoBehaviour
{
    [Header("Настройки пули")]
    [SerializeField] private float speed = 20f;
    [SerializeField] private float lifetime = 3f;
    [SerializeField] private float damage = 10f;

    private Rigidbody _rb;
    private IObjectPool<Bullet> _pool;
    private float _spawnTime;

    // Кешируем компоненты в Awake — это выполняется ОДИН РАЗ
    private void Awake()
    {
        _rb = GetComponent<Rigidbody>();
    }

    /// <summary>
    /// Вызывается менеджером пула после создания
    /// </summary>
    public void SetPool(IObjectPool<Bullet> pool)
    {
        _pool = pool;
    }

    /// <summary>
    /// Настройка при выдаче из пула (аналог Start)
    /// Вызывается КАЖДЫЙ РАЗ при активации
    /// </summary>
    private void OnEnable()
    {
        // Сбрасываем состояние объекта!
        _rb.linearVelocity = Vector3.zero;
        _rb.angularVelocity = Vector3.zero;
        
        _spawnTime = Time.time;
        
        // Запускаем движение
        _rb.linearVelocity = transform.forward * speed;
    }

    /// <summary>
    /// Очистка при возврате в пул (аналог OnDestroy)
    /// Вызывается КАЖДЫЙ РАЗ при деактивации
    /// </summary>
    private void OnDisable()
    {
        // Останавливаем все корутины связанные с этим объектом
        StopAllCoroutines();
        
        // Сбрасываем физику
        _rb.linearVelocity = Vector3.zero;
        _rb.angularVelocity = Vector3.zero;
    }

    private void Update()
    {
        // Проверяем время жизни
        if (Time.time - _spawnTime >= lifetime)
        {
            ReturnToPool();
        }
    }

    private void OnCollisionEnter(Collision collision)
    {
        // Наносим урон
        if (collision.gameObject.TryGetComponent<IDamageable>(out var damageable))
        {
            damageable.TakeDamage(damage);
        }

        // Возвращаем в пул вместо Destroy!
        ReturnToPool();
    }

    public void ReturnToPool()
    {
        if (_pool != null)
        {
            _pool.Release(this);
        }
        else
        {
            // Fallback если пул не задан
            gameObject.SetActive(false);
        }
    }
}
```

### Частые ошибки с OnEnable/OnDisable



```csharp
public class CommonMistakes : MonoBehaviour
{
    private Coroutine _lifeCoroutine;

    // ❌ ПЛОХО: не сбрасываем состояние
    private void OnEnable_Wrong()
    {
        // Если объект уже имел velocity из прошлого использования
        // он продолжит двигаться в старом направлении!
        GetComponent<Rigidbody>().linearVelocity = transform.forward * 10f;
        // Старая velocity + новая = неправильное поведение
    }

    // ✅ ХОРОШО: всегда сбрасываем состояние
    private void OnEnable_Correct()
    {
        var rb = GetComponent<Rigidbody>();
        rb.linearVelocity = Vector3.zero;      // Сброс
        rb.angularVelocity = Vector3.zero;     // Сброс
        rb.linearVelocity = transform.forward * 10f; // Затем применяем
    }

    // ❌ ПЛОХО: не останавливаем корутины
    private void OnDisable_Wrong()
    {
        // Корутина продолжает работать даже после деактивации!
        // И при следующей активации запустится ещё одна
    }

    // ✅ ХОРОШО: останавливаем корутины
    private void OnDisable_Correct()
    {
        if (_lifeCoroutine != null)
        {
            StopCoroutine(_lifeCoroutine);
            _lifeCoroutine = null;
        }
    }

    // ❌ ПЛОХО: подписываемся на события в OnEnable без отписки в OnDisable
    private void OnEnable_EventLeak()
    {
        GameEvents.OnLevelComplete += HandleLevelComplete;
        // Если объект возвращён в пул, он всё ещё подписан!
    }

    // ✅ ХОРОШО: симметричная подписка/отписка
    private void OnEnable_EventCorrect()
    {
        GameEvents.OnLevelComplete += HandleLevelComplete;
    }

    private void OnDisable_EventCorrect()
    {
        GameEvents.OnLevelComplete -= HandleLevelComplete;
    }

    private void HandleLevelComplete() { }
}
```

---

## 6. Generic Pool для любых типов {#generic-pool}

Создадим универсальный менеджер пулов, который поддерживает любые типы компонентов и управляет несколькими пулами сразу.

### Интерфейс для объектов, поддерживающих пул



```csharp
/// <summary>
/// Интерфейс для объектов, которые умеют работать с пулом
/// </summary>
public interface IPoolable
{
    void OnGetFromPool();
    void OnReturnToPool();
}
```

### Generic Pool Manager



```csharp
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Pool;

/// <summary>
/// Универсальный менеджер пулов для MonoBehaviour компонентов
/// </summary>
public class PoolManager : MonoBehaviour
{
    public static PoolManager Instance { get; private set; }

    // Словарь: ключ = префаб, значение = его пул
    private Dictionary<GameObject, ObjectPool<GameObject>> _pools = new();
    
    [SerializeField] private bool collectionCheck = true;
    [SerializeField] private int defaultCapacity = 10;
    [SerializeField] private int maxSize = 1000;

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
    /// Получить объект из пула для данного префаба
    /// </summary>
    public GameObject Get(GameObject prefab, Vector3 position, Quaternion rotation)
    {
        var pool = GetOrCreatePool(prefab);
        var obj = pool.Get();
        obj.transform.SetPositionAndRotation(position, rotation);
        return obj;
    }

    /// <summary>
    /// Получить компонент T из пула для данного префаба
    /// </summary>
    public T Get<T>(GameObject prefab, Vector3 position, Quaternion rotation) 
        where T : Component
    {
        var obj = Get(prefab, position, rotation);
        return obj.GetComponent<T>();
    }

    /// <summary>
    /// Вернуть объект в пул
    /// </summary>
    public void Release(GameObject prefab, GameObject obj)
    {
        if (_pools.TryGetValue(prefab, out var pool))
        {
            pool.Release(obj);
        }
        else
        {
            Debug.LogWarning($"[PoolManager] Пул для {prefab.name} не найден! Уничтожаем объект.");
            Destroy(obj);
        }
    }

    private ObjectPool<GameObject> GetOrCreatePool(GameObject prefab)
    {
        if (!_pools.TryGetValue(prefab, out var pool))
        {
            // Создаём контейнер для этого пула
            var container = new GameObject($"[Pool] {prefab.name}").transform;
            container.SetParent(transform);

            pool = new ObjectPool<GameObject>(
                createFunc: () =>
                {
                    var instance = Instantiate(prefab, container);
                    
                    // Добавляем компонент-помощник для возврата в пул
                    var poolRef = instance.AddComponent<PoolReference>();
                    poolRef.Initialize(prefab, Instance);
                    
                    return instance;
                },
                actionOnGet: obj =>
                {
                    obj.SetActive(true);
                    // Уведомляем все IPoolable компоненты
                    foreach (var poolable in obj.GetComponents<IPoolable>())
                    {
                        poolable.OnGetFromPool();
                    }
                },
                actionOnRelease: obj =>
                {
                    // Уведомляем все IPoolable компоненты
                    foreach (var poolable in obj.GetComponents<IPoolable>())
                    {
                        poolable.OnReturnToPool();
                    }
                    obj.SetActive(false);
                    obj.transform.SetParent(container);
                },
                actionOnDestroy: obj => Destroy(obj),
                collectionCheck: collectionCheck,
                defaultCapacity: defaultCapacity,
                maxSize: maxSize
            );

            _pools[prefab] = pool;
        }

        return pool;
    }

    /// <summary>
    /// Прогрев конкретного пула
    /// </summary>
    public void Prewarm(GameObject prefab, int count)
    {
        var pool = GetOrCreatePool(prefab);
        var tempList = new List<GameObject>(count);
        
        // Берём и сразу возвращаем — пул заполнится
        for (int i = 0; i < count; i++)
        {
            tempList.Add(pool.Get());
        }
        
        foreach (var obj in tempList)
        {
            pool.Release(obj);
        }
    }

    private void OnDestroy()
    {
        foreach (var pool in _pools.Values)
        {
            pool.Dispose();
        }
        _pools.Clear();
    }
}

/// <summary>
/// Вспомогательный компонент, хранящий ссылку на префаб для возврата в пул
/// </summary>
public class PoolReference : MonoBehaviour
{
    private GameObject _prefab;
    private PoolManager _manager;

    public void Initialize(GameObject prefab, PoolManager manager)
    {
        _prefab = prefab;
        _manager = manager;
    }

    public void ReturnToPool()
    {
        _manager.Release(_prefab, gameObject);
    }
}
```

### Использование Generic Pool Manager



```csharp
public class GenericPoolUser : MonoBehaviour
{
    [SerializeField] private GameObject bulletPrefab;
    [SerializeField] private GameObject explosionPrefab;
    [SerializeField] private GameObject enemyPrefab;

    private void Start()
    {
        // Прогреваем пулы в начале уровня
        PoolManager.Instance.Prewarm(bulletPrefab, 50);
        PoolManager.Instance.Prewarm(explosionPrefab, 10);
        PoolManager.Instance.Prewarm(enemyPrefab, 20);
    }

    private void SpawnBullet()
    {
        // Получаем как GameObject
        var bullet = PoolManager.Instance.Get(bulletPrefab, transform.position, transform.rotation);
        
        // Или сразу получаем компонент
        var bulletComponent = PoolManager.Instance.Get<Bullet>(
            bulletPrefab, 
            transform.position, 
            transform.rotation
        );
    }

    private void SpawnExplosion(Vector3 position)
    {
        var explosion = PoolManager.Instance.Get(explosionPrefab, position, Quaternion.identity);
        // Объект сам вернётся в пул через свой PoolReference или таймер
    }
}
```

---

## 7. Практическое задание: пул для пуль {#практика}

Теперь соберём всё вместе и создадим полноценную систему стрельбы с пулом объектов.

### Структура проекта



```csharp
Assets/
├── Scripts/
│   ├── Pool/
│   │   ├── BulletPool.cs
│   │   └── PoolAutoReturn.cs
│   ├── Weapons/
│   │   ├── Shooter.cs
│   │   └── Bullet.cs
│   └── Interfaces/
│       └── IDamageable.cs
└── Prefabs/
    └── Bullet.prefab
```

### IDamageable интерфейс



```csharp
// IDamageable.cs
public interface IDamageable
{
    void TakeDamage(float damage);
}
```

### Компонент пули — полная версия



```csharp
// Bullet.cs
using System.Collections;
using UnityEngine;
using UnityEngine.Pool;

[RequireComponent(typeof(Rigidbody))]
[RequireComponent(typeof(Collider))]
public class Bullet : MonoBehaviour, IPoolable
{
    [Header("Характеристики")]
    [SerializeField] private float speed = 25f;
    [SerializeField] private float damage = 15f;
    [SerializeField] private float lifetime = 5f;

    [Header("Эффекты")]
    [SerializeField] private GameObject hitEffectPrefab;
    [SerializeField] private TrailRenderer trailRenderer;

    // Ссылка на пул (устанавливается снаружи)
    private IObjectPool<Bullet> _pool;
    
    // Компоненты (кэшируем в Awake)
    private Rigidbody _rb;
    private Collider _collider;
    
    // Таймер
    private Coroutine _lifetimeCoroutine;
    
    // Флаг возврата (предотвращает двойной возврат)
    private bool _isReturning;

    private void Awake()
    {
        _rb = GetComponent<Rigidbody>();
        _collider = GetComponent<Collider>();
    }

    // Вызывается извне после создания объекта
    public void SetPool(IObjectPool<Bullet> pool)
    {
        _pool = pool;
    }

    #region IPoolable Implementation

    public void OnGetFromPool()
    {
        // Сбрасываем флаг
        _isReturning = false;
        
        // Сбрасываем физику
        _rb.linearVelocity = Vector3.zero;
        _rb.angularVelocity = Vector3.zero;
        _rb.isKinematic = false;
        
        // Включаем коллайдер
        _collider.enabled = true;
        
        // Сбрасываем трейл
        if (trailRenderer != null)
        {
            trailRenderer.Clear();
            trailRenderer.enabled = true;
        }
        
        // Запускаем таймер жизни
        _lifetimeCoroutine = StartCoroutine(LifetimeRoutine());
        
        // Применяем скорость
        _rb.linearVelocity = transform.forward * speed;
    }

    public void OnReturnToPool()
    {
        // Останавливаем физику
        _rb.linearVelocity = Vector3.zero;
        _rb.angularVelocity = Vector3.zero;
        _rb.isKinematic = true;
        
        // Отключаем коллайдер (предотвращаем коллизии в пуле)
        _collider.enabled = false;
        
        // Отключаем трейл
        if (trailRenderer != null)
        {
            trailRenderer.enabled = false;
        }
        
        // Останавливаем корутину
        if (_lifetimeCoroutine != null)
        {
            StopCoroutine(_lifetimeCoroutine);
            _lifetimeCoroutine = null;
        }
    }

    #endregion

    private void OnCollisionEnter(Collision collision)
    {
        if (_isReturning) return; // Защита от двойного возврата

        // Наносим урон
        if (collision.gameObject.TryGetComponent<IDamageable>(out var damageable))
        {
            damageable.TakeDamage(damage);
        }

        // Спавн эффекта попадания
        if (hitEffectPrefab != null)
        {
            var hitNormal = collision.contacts[0].normal;
            var hitRotation = Quaternion.LookRotation(hitNormal);
            
            // Используем глобальный PoolManager для эффектов
            PoolManager.Instance.Get(hitEffectPrefab, collision.contacts[0].point, hitRotation);
        }

        ReturnToPool();
    }

    private IEnumerator LifetimeRoutine()
    {
        yield return new WaitForSeconds(lifetime);
        ReturnToPool();
    }

    public void ReturnToPool()
    {
        if (_isReturning) return;
        _isReturning = true;

        if (_pool != null)
        {
            _pool.Release(this);
        }
        else
        {
            gameObject.SetActive(false);
        }
    }

    // OnEnable/OnDisable как точки входа (вызываются при SetActive)
    private void OnEnable()
    {
        // OnGetFromPool вызывается из actionOnGet в пуле
        // Здесь можно добавить дополнительную логику если нужно
    }

    private void OnDisable()
    {
        // OnReturnToPool вызывается из actionOnRelease в пуле
    }
}
```

### Пул пуль — специализированная версия



```csharp
// BulletPool.cs
using UnityEngine;
using UnityEngine.Pool;

public class BulletPool : MonoBehaviour
{
    [Header("Настройки")]
    [SerializeField] private Bullet bulletPrefab;
    [SerializeField] private int defaultCapacity = 30;
    [SerializeField] private int maxSize = 200;

    private ObjectPool<Bullet> _pool;
    private Transform _container;

    public static BulletPool Instance { get; private set; }

    private void Awake()
    {
        if (Instance != null && Instance != this)
        {
            Destroy(gameObject);
            return;
        }
        Instance = this;

        _container = new GameObject("[BulletPool Container]").transform;
        _container.SetParent(transform);

        CreatePool();
    }

    private void CreatePool()
    {
        _pool = new ObjectPool<Bullet>(
            createFunc: () =>
            {
                var bullet = Instantiate(bulletPrefab, _container);
                bullet.SetPool(_pool);
                return bullet;
            },
            actionOnGet: bullet =>
            {
                bullet.gameObject.SetActive(true);
                bullet.OnGetFromPool();
            },
            actionOnRelease: bullet =>
            {
                bullet.OnReturnToPool();
                bullet.gameObject.SetActive(false);
                bullet.transform.SetParent(_container);
            },
            actionOnDestroy: bullet =>
            {
                Destroy(bullet.gameObject);
            },
            collectionCheck: Debug.isDebugBuild,
            defaultCapacity: defaultCapacity,
            maxSize: maxSize
        );

        // Прогрев
        PrewarmPool(defaultCapacity);
    }

    private void PrewarmPool(int count)
    {
        var temp = new Bullet[count];
        for (int i = 0; i < count; i++)
        {
            temp[i] = _pool.Get();
        }
        for (int i = 0; i < count; i++)
        {
            _pool.Release(temp[i]);
        }
    }

    public Bullet GetBullet(Vector3 position, Quaternion rotation)
    {
        var bullet = _pool.Get();
        bullet.transform.SetPositionAndRotation(position, rotation);
        bullet.transform.SetParent(null);
        return bullet;
    }

    public void ReleaseBullet(Bullet bullet)
    {
        _pool.Release(bullet);
    }

    // Статистика для дебага
    public (int total, int active, int inactive) GetStats() =>
        (_pool.CountAll, _pool.CountActive, _pool.CountInactive);
}
```

### Компонент стрельбы



```csharp
// Shooter.cs
using UnityEngine;

public class Shooter : MonoBehaviour
{
    [Header("Точка стрельбы")]
    [SerializeField] private Transform firePoint;
    
    [Header("Настройки стрельбы")]
    [SerializeField] private float fireRate = 10f; // Выстрелов в секунду
    [SerializeField] private int bulletsPerShot = 1;
    [SerializeField] private float spreadAngle = 0f; // Разброс в градусах

    [Header("Визуализация")]
    [SerializeField] private LineRenderer muzzleFlash;

    private float _nextFireTime;
    private float _fireInterval;

    private void Awake()
    {
        _fireInterval = 1f / fireRate;
    }

    private void Update()
    {
        HandleInput();
    }

    private void HandleInput()
    {
        // Автоматический огонь при удержании
        if (Input.GetButton("Fire1") && Time.time >= _nextFireTime)
        {
            Fire();
        }
    }

    public void Fire()
    {
        if (Time.time < _nextFireTime) return;
        if (BulletPool.Instance == null)
        {
            Debug.LogError("[Shooter] BulletPool.Instance не найден!");
            return;
        }

        _nextFireTime = Time.time + _fireInterval;

        for (int i = 0; i < bulletsPerShot; i++)
        {
            SpawnBullet();
        }

        // Мuzzle flash эффект
        if (muzzleFlash != null)
        {
            StartCoroutine(ShowMuzzleFlash());
        }
    }

    private void SpawnBullet()
    {
        Quaternion rotation = firePoint.rotation;

        // Применяем разброс
        if (spreadAngle > 0f)
        {
            var spread = new Vector3(
                Random.Range(-spreadAngle, spreadAngle),
                Random.Range(-spreadAngle, spreadAngle),
                0f
            );
            rotation = Quaternion.Euler(firePoint.eulerAngles + spread);
        }

        // Получаем пулю из пула
        var bullet = BulletPool.Instance.GetBullet(firePoint.position, rotation);

        if (bullet == null)
        {
            Debug.LogWarning("[Shooter] Не удалось получить пулю из пула!");
        }
    }

    private System.Collections.IEnumerator ShowMuzzleFlash()
    {
        muzzleFlash.enabled = true;
        yield return new WaitForSeconds(0.05f);
        muzzleFlash.enabled = false;
    }

    // Вызывается из UI или других систем
    public void SetFireRate(float newFireRate)
    {
        fireRate = Mathf.Max(0.1f, newFireRate);
        _fireInterval = 1f / fireRate;
    }
}
```

### Компонент автоматического возврата (без пули)



```csharp
// PoolAutoReturn.cs — универсальный компонент для любых пуловых объектов
using System.Collections;
using UnityEngine;

/// <summary>
/// Автоматически возвращает объект в пул через заданное время.
/// Прикрепите к объекту, который должен вернуться в пул через таймер.
/// </summary>
public class PoolAutoReturn : MonoBehaviour
{
    [SerializeField] private float returnDelay = 2f;
    
    private Coroutine _returnCoroutine;
    private PoolReference _poolReference;

    private void Awake()
    {
        _poolReference = GetComponent<PoolReference>();
    }

    private void OnEnable()
    {
        _returnCoroutine = StartCoroutine(ReturnAfterDelay());
    }

    private void OnDisable()
    {
        if (_returnCoroutine != null)
        {
            StopCoroutine(_returnCoroutine);
            _returnCoroutine = null;
        }
    }

    private IEnumerator ReturnAfterDelay()
    {
        yield return new WaitForSeconds(returnDelay);
        
        if (_poolReference != null)
        {
            _poolReference.ReturnToPool();
        }
        else
        {
            gameObject.SetActive(false);
        }
    }

    public void SetDelay(float delay)
    {
        returnDelay = delay;
    }
}
```

### Тестовая сцена — как всё соединить



```csharp
// GameSetup.cs — пример настройки сцены
using UnityEngine;

public class GameSetup : MonoBehaviour
{
    [Header("Ссылки на компоненты")]
    [SerializeField] private BulletPool bulletPool;
    [SerializeField] private Shooter playerShooter;
    
    [Header("Тест производительности")]
    [SerializeField] private bool showDebugInfo = true;

    private void OnGUI()
    {
        if (!showDebugInfo || BulletPool.Instance == null) return;

        var stats = BulletPool.Instance.GetStats();
        
        var style = new GUIStyle(GUI.skin.box)
        {
            fontSize = 16,
            alignment = Anchor.UpperLeft
        };

        var rect = new Rect(10, 10, 250, 100);
        GUI.Box(rect, "", style);
        
        GUI.Label(new Rect(20, 15, 240, 25), $"Пул пуль — всего: {stats.total}");
        GUI.Label(new Rect(20, 35, 240, 25), $"Активных: {stats.active}");
        GUI.Label(new Rect(20, 55, 240, 25), $"В пуле: {stats.inactive}");
        GUI.Label(new Rect(20, 75, 240, 25), $"FPS: {(int)(1f / Time.deltaTime)}");
    }
}
```

### Настройка в Unity Editor



```csharp
1. Создайте пустой GameObject "GameManager"
2. Добавьте BulletPool компонент
   - Bullet Prefab: ваш префаб пули
   - Default Capacity: 30
   - Max Size: 200

3. На пуле Bullet.prefab настройте:
   - Rigidbody: Mass=0.1, Drag=0, Use Gravity=false
   - Collider: Is Trigger=false
   - TrailRenderer (опционально)

4. Создайте игрока с Shooter компонентом
   - Fire Point: дочерний Transform (точка выхода пули)
   - Fire Rate: 10
   - Spread Angle: 2

5. Проверьте в Play Mode:
   - Нажмите Fire1 — пули должны стрелять
   - Смотрите на счётчики в OnGUI
   - Объекты в иерархии деактивируются, а не удаляются
```

---

## 8. Проверь себя {#проверка}

### Теоретические вопросы

**1.** Почему `Instantiate`/`Destroy` вызывают проблемы с производительностью?

<details> <summary>Ответ</summary>

Каждый `Instantiate` выделяет память в управляемой куче (managed heap), а каждый `Destroy` создаёт мусор для сборщика (GC). Когда GC запускается — он останавливает все потоки (stop-the-world), что проявляется как заметные фризы (спайки в профайлере). При интенсивном спавне/уничтожении объектов (пули, эффекты) это происходит регулярно.

</details>

---

**2.** Чем отличается `OnEnable` от `Start` и почему `OnEnable` предпочтительнее для пуловых объектов?

<details> <summary>Ответ</summary>

`Start` вызывается **один раз** — сразу после `Awake`, при первой активации объекта. `OnEnable` вызывается **каждый раз** при активации объекта (`SetActive(true)`). Для пуловых объектов `OnEnable` предпочтительнее, потому что объект переиспользуется: после возврата в пул и повторной выдачи нам нужно каждый раз сбрасывать и инициализировать его состояние. `Start` для этого не подойдёт — он не вызовется повторно.

</details>

---

**3.** Что такое `collectionCheck` в `ObjectPool<T>` и когда его стоит включать?

<details> <summary>Ответ</summary>

`collectionCheck = true` добавляет проверку: если попытаться вернуть объект в пул, который там уже есть (двойной возврат) — будет выброшено `InvalidOperationException`. Это помогает находить баги. Рекомендуется включать в **Debug-сборках** (`Debug.isDebugBuild`) и отключать в **Release** для производительности.

</details>

---

**4.** Что произойдёт, если не остановить корутину при возврате объекта в пул?

<details> <summary>Ответ</summary>

Корутина продолжит работу даже на деактивированном объекте (в Unity корутины на неактивных объектах приостанавливаются, но при повторной активации продолжают работу с того места). Хуже того — при следующей активации объекта запустится **ещё одна** корутина. В итоге будет несколько корутин, работающих одновременно, что приведёт к непредсказуемому поведению (например, пуля вернётся в пул раньше или позже, чем нужно).

</details>

---

**5.** Как работает `Stack<T>` в контексте пула и почему он лучше `List<T>`?

`Stack< T >` работает по принципу LIFO (Last In, First Out). Операции `Push` (добавить) и `Pop` (взять) выполняются за **O(1)**. Последний возвращённый объект — первый выданный, что означает что "горячие" объекты (недавно использованные) остаются в кэше процессора. `List< T >` для реализации пула потребовал бы `RemoveAt` — что даёт **O(n)** из-за сдвига элементов. `Queue< T >` тоже даёт O(1), но Stack предпочтительнее из-за лучшего поведения кэша.


---

### Практические задания

**Задание 1: Базовое** 🟢

Создайте простой пул для эффектов взрыва (Explosion). Взрыв должен:

- Активировать ParticleSystem при выдаче из пула
- Автоматически вернуться в пул через 2 секунды
- Остановить ParticleSystem при возврате

---

**Задание 2: Среднее** 🟡

Модифицируйте систему стрельбы: добавьте **несколько типов пуль** (обычная, бронебойная, взрывная). Каждый тип — отдельный пул. Реализуйте переключение типа пули в `Shooter`.



```csharp
// Подсказка: используйте Dictionary<BulletType, BulletPool>
public enum BulletType { Standard, ArmorPiercing, Explosive }
```

---

**Задание 3: Продвинутое** 🔴

Реализуйте **пул для AudioSource** — компонента воспроизведения звука. Требования:

- Пул AudioSource на GameObject
- Метод `Play(AudioClip clip, Vector3 position, float volume)`
- Автоматический возврат после окончания клипа
- Поддержка 3D-звука (позиционирование)



```csharp
// Подсказка:
public class PooledAudioSource : MonoBehaviour
{
    private AudioSource _source;
    // Ваша реализация...
}
```

---

**Задание 4: Исправь баг** 🔴

Найдите все ошибки в следующем коде:



```csharp
public class BuggyBullet : MonoBehaviour
{
    private Rigidbody _rb;
    private float _startTime;
    
    private void Start()
    {
        _rb = GetComponent<Rigidbody>();
        _startTime = Time.time;
    }
    
    private void OnEnable()
    {
        _rb.linearVelocity = transform.forward * 20f;
        StartCoroutine(LifetimeCheck());
    }
    
    private IEnumerator LifetimeCheck()
    {
        yield return new WaitForSeconds(3f);
        ReturnToPool();
    }
    
    private void OnCollisionEnter(Collision c)
    {
        ReturnToPool();
        ReturnToPool(); // на всякий случай
    }
    
    private void ReturnToPool()
    {
        _pool.Release(this);
    }
    
    private IObjectPool<BuggyBullet> _pool;
}
```

<details> <summary>Список ошибок</summary>

1. **`_rb` в `OnEnable`**: `_rb` кэшируется в `Start`, который вызывается один раз. Если объект переиспользуется и `Start` не вызывается снова — это нормально. Но если `OnEnable` вызовется до `Start` — будет `NullReferenceException`. Решение: кэшировать в `Awake`.
    
2. **`_startTime` в `Start`**: Время старта записывается один раз. При повторном использовании оно не сбрасывается. Нужно сбрасывать в `OnEnable`.
    
3. **Двойной вызов `ReturnToPool()`**: В `OnCollisionEnter` вызывается два раза — двойной возврат в пул, что приведёт к исключению (при `collectionCheck=true`) или повреждению состояния пула. Нужен флаг `_isReturning`.
    
4. **Корутина не останавливается в `OnDisable`**: Каждый `OnEnable` запускает новую корутину, старые не останавливаются. При 10 использованиях — 10 корутин! Решение: останавливать в `OnDisable`, хранить ссылку на `Coroutine`.
    
5. **Нет проверки `_isReturning`**: нет защиты от повторного возврата при одновременном коллизии и таймере.
    

</details>

---

### Чеклист для самопроверки

Перед тем как считать задание выполненным, убедитесь:

- [ ]  Объекты в пуле **деактивируются**, а не уничтожаются
- [ ]  В `OnEnable` происходит **полный сброс состояния** (velocity, флаги, таймеры)
- [ ]  В `OnDisable` **останавливаются корутины** и отписываются события
- [ ]  Есть **флаг защиты** от двойного возврата (`_isReturning`)
- [ ]  `Awake` используется для **кэширования компонентов**
- [ ]  `OnEnable` используется для **инициализации** (вместо `Start`)
- [ ]  Пул **прогревается** заранее, а не создаёт объекты в разгар игры
- [ ]  В профайлере **нет аллокаций** во время игрового процесса (только при прогреве)

---

## Итоги

В этой статье мы разобрали:

|Тема|Ключевой вывод|
|---|---|
|Проблема Instantiate/Destroy|Провоцирует GC, который вызывает фризы|
|Object Pool|Переиспользование объектов без аллокаций|
|Stack<T>|O(1) операции для простого пула|
|ObjectPool<T>|Встроенное решение Unity с callbacks|
|OnEnable/OnDisable|Правильные точки жизненного цикла|
|Generic Pool|Управление несколькими пулами через словарь|
|Bullet System|Полная интеграция всех концепций|

Object Pool — это один из важнейших паттернов в разработке игр. Его освоение позволяет создавать плавные, оптимизированные игры без неожиданных фризов. Применяйте его везде, где есть массовый спавн/деспавн объектов.

> 💡 **Следующий шаг**: Изучите `Span<T>` и `ArrayPool<T>` для оптимизации работы с массивами и временными данными без GC-аллокаций.