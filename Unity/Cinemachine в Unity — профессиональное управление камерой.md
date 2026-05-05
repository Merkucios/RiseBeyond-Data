
## Содержание

- [Содержание](#%D0%A1%D0%BE%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D0%BD%D0%B8%D0%B5)
- [Введение](#%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5)
- [Установка](#%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0)
	- [Шаг 1 — Открытие Package Manager](#%D0%A8%D0%B0%D0%B3%201%20%E2%80%94%20%D0%9E%D1%82%D0%BA%D1%80%D1%8B%D1%82%D0%B8%D0%B5%20Package%20Manager)
	- [Шаг 2 — Поиск пакета](#%D0%A8%D0%B0%D0%B3%202%20%E2%80%94%20%D0%9F%D0%BE%D0%B8%D1%81%D0%BA%20%D0%BF%D0%B0%D0%BA%D0%B5%D1%82%D0%B0)
	- [Шаг 3 — Установка](#%D0%A8%D0%B0%D0%B3%203%20%E2%80%94%20%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0)
	- [Проверка установки](#%D0%9F%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0%20%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B8)
- [CinemachineBrain](#CinemachineBrain)
	- [Как добавить](#%D0%9A%D0%B0%D0%BA%20%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C)
	- [Параметры CinemachineBrain](#%D0%9F%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B%20CinemachineBrain)
	- [Что делает CinemachineBrain](#%D0%A7%D1%82%D0%BE%20%D0%B4%D0%B5%D0%BB%D0%B0%D0%B5%D1%82%20CinemachineBrain)
- [Virtual Camera](#Virtual%20Camera)
	- [Создание Virtual Camera](#%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20Virtual%20Camera)
	- [Структура компонента](#%D0%A1%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D0%BA%D0%BE%D0%BC%D0%BF%D0%BE%D0%BD%D0%B5%D0%BD%D1%82%D0%B0)
	- [Priority — ключевой параметр](#Priority%20%E2%80%94%20%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%B2%D0%BE%D0%B9%20%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80)
- [Follow и LookAt](#Follow%20%D0%B8%20LookAt)
	- [Follow](#Follow)
	- [LookAt](#LookAt)
	- [Настройка через код](#%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20%D0%BA%D0%BE%D0%B4)
	- [Лучшая практика: отдельный Aim Target](#%D0%9B%D1%83%D1%87%D1%88%D0%B0%D1%8F%20%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0:%20%D0%BE%D1%82%D0%B4%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20Aim%20Target)
- [Body](#Body)
	- [Доступные алгоритмы Body](#%D0%94%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D1%8B%D0%B5%20%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D1%8B%20Body)
	- [Transposer — простое следование с офсетом](#Transposer%20%E2%80%94%20%D0%BF%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%B5%20%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%81%20%D0%BE%D1%84%D1%81%D0%B5%D1%82%D0%BE%D0%BC)
	- [Framing Transposer — умное следование](#Framing%20Transposer%20%E2%80%94%20%D1%83%D0%BC%D0%BD%D0%BE%D0%B5%20%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5)
- [Aim](#Aim)
	- [Доступные алгоритмы Aim](#%D0%94%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D1%8B%D0%B5%20%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D1%8B%20Aim)
	- [Composer — умное прицеливание](#Composer%20%E2%80%94%20%D1%83%D0%BC%D0%BD%D0%BE%D0%B5%20%D0%BF%D1%80%D0%B8%D1%86%D0%B5%D0%BB%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5)
	- [Hard Look At](#Hard%20Look%20At)
- [Damping](#Damping)
	- [Принцип работы](#%D0%9F%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B)
	- [Damping в Transposer](#Damping%20%D0%B2%20Transposer)
	- [Damping в Framing Transposer](#Damping%20%D0%B2%20Framing%20Transposer)
	- [Практические рекомендации по Damping](#%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8%20%D0%BF%D0%BE%20Damping)
	- [Управление Damping через код](#%D0%A3%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20Damping%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20%D0%BA%D0%BE%D0%B4)
- [Camera Shake](#Camera%20Shake)
	- [Noise Profiles](#Noise%20Profiles)
	- [Настройка через Inspector](#%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20Inspector)
	- [Полная система Camera Shake через код](#%D0%9F%D0%BE%D0%BB%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20Camera%20Shake%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20%D0%BA%D0%BE%D0%B4)
	- [Использование в других скриптах](#%D0%98%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%B2%20%D0%B4%D1%80%D1%83%D0%B3%D0%B8%D1%85%20%D1%81%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D0%B0%D1%85)
- [Multiple Virtual Cameras](#Multiple%20Virtual%20Cameras)
	- [Система приоритетов](#%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D0%BF%D1%80%D0%B8%D0%BE%D1%80%D0%B8%D1%82%D0%B5%D1%82%D0%BE%D0%B2)
	- [Создание нескольких камер](#%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%B5%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%B8%D1%85%20%D0%BA%D0%B0%D0%BC%D0%B5%D1%80)
	- [Настройка переходов (Blends)](#%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0%20%D0%BF%D0%B5%D1%80%D0%B5%D1%85%D0%BE%D0%B4%D0%BE%D0%B2%20(Blends))
- [Практическое задание](#%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5)
	- [Схема проекта](#%D0%A1%D1%85%D0%B5%D0%BC%D0%B0%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
	- [Шаг 1 — Создание структуры сцены](#%D0%A8%D0%B0%D0%B3%201%20%E2%80%94%20%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D1%8B%20%D1%81%D1%86%D0%B5%D0%BD%D1%8B)
	- [Шаг 2 — Настройка CM_Gameplay](#%D0%A8%D0%B0%D0%B3%202%20%E2%80%94%20%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0%20CM_Gameplay)
	- [Шаг 3 — Настройка CM_Boss](#%D0%A8%D0%B0%D0%B3%203%20%E2%80%94%20%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0%20CM_Boss)
	- [Шаг 4 — Скрипт триггера](#%D0%A8%D0%B0%D0%B3%204%20%E2%80%94%20%D0%A1%D0%BA%D1%80%D0%B8%D0%BF%D1%82%20%D1%82%D1%80%D0%B8%D0%B3%D0%B3%D0%B5%D1%80%D0%B0)
	- [Шаг 5 — Дополнительный скрипт: Camera Shake при появлении босса](#%D0%A8%D0%B0%D0%B3%205%20%E2%80%94%20%D0%94%D0%BE%D0%BF%D0%BE%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D1%81%D0%BA%D1%80%D0%B8%D0%BF%D1%82:%20Camera%20Shake%20%D0%BF%D1%80%D0%B8%20%D0%BF%D0%BE%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B8%20%D0%B1%D0%BE%D1%81%D1%81%D0%B0)
	- [Шаг 6 — Финальная проверка](#%D0%A8%D0%B0%D0%B3%206%20%E2%80%94%20%D0%A4%D0%B8%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0)
- [Проверь себя](#%D0%9F%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D1%8C%20%D1%81%D0%B5%D0%B1%D1%8F)
	- [Теоретические вопросы](#%D0%A2%D0%B5%D0%BE%D1%80%D0%B5%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%B2%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D1%8B)
	- [Практические задания](#%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F)
	- [Быстрый чеклист перед релизом](#%D0%91%D1%8B%D1%81%D1%82%D1%80%D1%8B%D0%B9%20%D1%87%D0%B5%D0%BA%D0%BB%D0%B8%D1%81%D1%82%20%D0%BF%D0%B5%D1%80%D0%B5%D0%B4%20%D1%80%D0%B5%D0%BB%D0%B8%D0%B7%D0%BE%D0%BC)

---

## Введение

Когда разработчики начинают работать с камерой в Unity вручную, они неизбежно сталкиваются с одними и теми же проблемами:

- Камера дёргается и двигается не плавно
- Переход между точками обзора выглядит резко и неприятно
- Код управления камерой разрастается и становится трудно поддерживаемым
- Тряска камеры, плавное следование, зоны «мёртвой» зоны — всё это приходится писать с нуля

Типичный «ручной» скрипт камеры выглядит примерно так:



```csharp
// ❌ Так делать НЕ рекомендуется — это быстро становится неуправляемым
public class ManualCamera : MonoBehaviour
{
    public Transform target;
    public float smoothSpeed = 0.125f;
    public Vector3 offset;

    void LateUpdate()
    {
        Vector3 desiredPosition = target.position + offset;
        Vector3 smoothedPosition = Vector3.Lerp(
            transform.position,
            desiredPosition,
            smoothSpeed
        );
        transform.position = smoothedPosition;
        transform.LookAt(target);
    }
}
```

Этот код не учитывает множество сценариев: что если нужно переключиться на другую камеру во время катсцены? Что если нужна тряска при взрыве? Что если камера должна обходить препятствия?

**Cinemachine** — это официальный пакет Unity, который решает все эти проблемы на профессиональном уровне. Его используют в AAA-играх, инди-проектах и кинематографических сценах. Cinemachine предоставляет:

|Возможность|Ручная камера|Cinemachine|
|---|---|---|
|Плавное следование|Нужно писать самому|✅ Встроено|
|Переключение камер|Сложный код|✅ По приоритету|
|Тряска камеры|Нужно писать самому|✅ Noise профили|
|Dead Zone / Soft Zone|Очень сложно|✅ Визуальный редактор|
|Blend между камерами|Очень сложно|✅ Анимированный переход|

---

## Установка

### Шаг 1 — Открытие Package Manager

Перейдите в меню **Window → Package Manager**.

### Шаг 2 — Поиск пакета

В выпадающем меню слева выберите **Unity Registry** и в строке поиска введите `Cinemachine`.

### Шаг 3 — Установка

Нажмите кнопку **Install**. После установки в меню Unity появится новый пункт **Cinemachine**.



```csharp
Unity Editor
├── Window
│   └── Package Manager
│       └── Unity Registry
│           └── Cinemachine → [Install]
└── GameObject
    └── Cinemachine  ← появится после установки
        ├── Virtual Camera
        ├── FreeLook Camera
        ├── Blend List Camera
        └── ...
```

> **Версии:** Статья написана для Cinemachine **2.x** (совместима с Unity 2020–2023). В Unity 6 используется Cinemachine 3.x с незначительными отличиями в именовании компонентов.

### Проверка установки

После установки создайте тестовую виртуальную камеру: **GameObject → Cinemachine → Virtual Camera**. Если объект создался — всё работает корректно.

---

## CinemachineBrain

**CinemachineBrain** — это «мозг» всей системы. Он располагается на объекте **Main Camera** и управляет тем, какая виртуальная камера активна в данный момент.

### Как добавить

При создании первой виртуальной камеры через меню **GameObject → Cinemachine → Virtual Camera** компонент `CinemachineBrain` добавляется на Main Camera **автоматически**. Но вы можете добавить его вручную:

1. Выберите объект **Main Camera** в иерархии
2. **Add Component → Cinemachine → CinemachineBrain**

### Параметры CinemachineBrain



```csharp
CinemachineBrain
├── Show Debug           — показывать отладочную информацию на экране
├── Show Camera Frustum      — показывать фрустум камеры в Scene View
├── Ignore Time Scale        — игнорировать Time.timeScale (для паузы)
├── World Up Override        — переопределить направление «вверх»
├── Update Method            — когда обновлять камеру
│   ├── Fixed Update         — синхронно с физикой
│   ├── Late Update          — после всех Update (рекомендуется)
│   └── Smart Update         — автоматический выбор
├── Blend Update Method      — метод обновления при переходе
├── Default Blend            — настройки перехода по умолчанию
│   ├── Style: Cut/Ease In Out/Linear/Custom
│   └── Time: 2              — время перехода в секундах
└── Custom Blends            — кастомные правила переходов
```

### Что делает CinemachineBrain

Brain постоянно смотрит на **все** Virtual Camera на сцене и выбирает ту, у которой **наибольший Priority**. Именно её позицию и ориентацию он передаёт реальной камере. При переключении между виртуальными камерами Brain выполняет плавный blend (переход) согласно настройкам.



```csharp
// Пример: получить текущую активную виртуальную камеру
using Cinemachine;
using UnityEngine;

public class CameraInfo : MonoBehaviour
{
    private CinemachineBrain brain;

    void Start()
    {
        // Brain всегда на Main Camera
        brain = Camera.main.GetComponent<CinemachineBrain>();
    }

    void Update()
    {
        if (brain.ActiveVirtualCamera != null)
        {
            Debug.Log($"Активная камера: {brain.ActiveVirtualCamera.Name}");
            Debug.Log($"Идёт переход: {brain.IsBlending}");
        }
    }
}
```

> **Важно:** Никогда не перемещайте Main Camera вручную через скрипт, если на ней есть CinemachineBrain — Brain перезаписывает позицию каждый кадр. Управляйте только виртуальными камерами.

---

## Virtual Camera

**CinemachineVirtualCamera** — это не настоящая камера. Это набор инструкций: «как должна вести себя камера в данный момент». Brain читает эти инструкции и применяет их к реальной камере.

### Создание Virtual Camera



```csharp
GameObject → Cinemachine → Virtual Camera
```

В иерархии появится объект `CM vcam1` с компонентом `CinemachineVirtualCamera`.

### Структура компонента



```csharp
CinemachineVirtualCamera
├── Solo              — принудительно активировать эту камеру (только в Editor)
├── Game Window Guides — показывать направляющие в Game View
├── Save During Play  — сохранять изменения сделанные во время Play Mode
│
├── Priority: 10      — приоритет (чем выше, тем важнее)
├── Follow: None      — цель для следования (Transform)
├── Look At: None     — цель для взгляда (Transform)
│
├── Lens              — параметры объектива
│   ├── Field of View: 60      — угол обзора
│   ├── Near Clip Plane: 0.1   — ближняя плоскость отсечения
│   └── Far Clip Plane: 5000   — дальняя плоскость отсечения
│
├── Transitions       — настройки перехода
│   ├── Blend Hint    — подсказка для типа перехода
│   └── Inherit Position — наследовать позицию при активации
│
├── Body              — КАК камера двигается (алгоритм позиции)
└── Aim               — КАК камера смотрит (алгоритм поворота)
```

### Priority — ключевой параметр



```csharp
using Cinemachine;
using UnityEngine;

public class PriorityExample : MonoBehaviour
{
    [SerializeField] private CinemachineVirtualCamera gameplayCamera;
    [SerializeField] private CinemachineVirtualCamera bossCamera;

    void Start()
    {
        // Gameplay камера активна по умолчанию
        gameplayCamera.Priority = 10;
        bossCamera.Priority = 0;
    }

    // При входе в зону босса — поднимаем приоритет камеры босса
    public void EnterBossZone()
    {
        bossCamera.Priority = 20; // Теперь boss камера активна
    }

    public void ExitBossZone()
    {
        bossCamera.Priority = 0; // Возвращаемся к gameplay камере
    }
}
```

---

## Follow и LookAt

Два главных параметра Virtual Camera, которые определяют, **за чем** следит камера.

### Follow

Параметр `Follow` задаёт **Transform**, за которым камера будет физически следовать. Позиция камеры будет вычисляться относительно этого объекта с учётом настроек **Body**.

### LookAt

Параметр `Look At` задаёт **Transform**, на который камера будет **смотреть**. Ориентация камеры будет вычисляться согласно настройкам **Aim**.

### Настройка через код



```csharp
using Cinemachine;
using UnityEngine;

public class CameraSetup : MonoBehaviour
{
    [Header("Камеры")]
    [SerializeField] private CinemachineVirtualCamera virtualCamera;

    [Header("Цели")]
    [SerializeField] private Transform playerTransform;
    [SerializeField] private Transform aimTargetTransform;

    void Start()
    {
        SetupCamera();
    }

    private void SetupCamera()
    {
        // Камера следует за игроком
        virtualCamera.Follow = playerTransform;

        // Камера смотрит на отдельную точку прицеливания
        // (например, точка между игроком и курсором мыши)
        virtualCamera.LookAt = aimTargetTransform;
    }

    // Динамически сменить цель (например, при посадке в транспорт)
    public void SwitchFollowTarget(Transform newTarget)
    {
        virtualCamera.Follow = newTarget;
        virtualCamera.LookAt = newTarget;
    }
}
```

### Лучшая практика: отдельный Aim Target

Вместо того чтобы смотреть прямо на игрока, профессиональный подход — создать пустой объект `AimTarget` и двигать его программно:



```csharp
using UnityEngine;

public class AimTargetController : MonoBehaviour
{
    [SerializeField] private Transform player;
    [SerializeField] private float lookAheadDistance = 3f;

    void LateUpdate()
    {
        // Точка прицеливания — немного впереди игрока
        // в направлении его движения
        Vector3 lookAheadPoint = player.position +
                                  player.forward * lookAheadDistance;
        transform.position = lookAheadPoint;
    }
}
```

---

## Body

Секция **Body** определяет **алгоритм позиционирования** камеры — то, как камера двигается в пространстве относительно цели Follow.

### Доступные алгоритмы Body



```csharp
Body
├── Do Nothing          — камера не двигается сама
├── 3rd Person Follow   — следование от третьего лица
├── Framing Transposer  — 2D/3D следование с учётом экранного пространства
├── Hard Lock to Target — жёсткая привязка к позиции цели
├── Orbital Transposer  — орбитальное движение вокруг цели
└── Transposer          — следование с фиксированным смещением
```

### Transposer — простое следование с офсетом

Самый простой алгоритм. Камера следует за целью с **фиксированным смещением** в мировых или локальных координатах.



```csharp
Body: Transposer
├── Binding Mode        — система координат смещения
│   ├── Lock To Target On Assign  — смещение фиксируется при назначении цели
│   ├── Lock To Target With World Up — смещение в мировых координатах
│   ├── Lock To Target No Roll    — без крена
│   ├── Simple Follow With World Up — простое следование
│   └── World Space               — смещение в мировом пространстве
├── Follow Offset       — смещение камеры от цели (X, Y, Z)
│   ├── X: 0  — смещение вправо/влево
│   ├── Y: 5  — смещение вверх (высота камеры)
│   └── Z: -10 — смещение назад (дистанция)
└── Damping             — плавность (подробнее в разделе Damping)
    ├── X: 1
    ├── Y: 1
    └── Z: 1
```

**Пример:** Для 2D-игры с видом сбоку идеально подходит Transposer с `Z = -10`, `X = 0`, `Y = 0`.

### Framing Transposer — умное следование

Более продвинутый алгоритм, который работает в **экранном пространстве**. Камера держит цель в определённой области экрана.



```csharp
Body: Framing Transposer
├── Lookahead Time      — время предсказания движения (0 = выкл)
│                         Камера «смотрит вперёд» по траектории цели
├── Lookahead Smoothing — сглаживание предсказания (0-30)
├── Lookahead Ignore Y  — игнорировать Y при предсказании
│
├── Camera Distance     — дистанция от цели по оси Z
├── Dead Zone Width     — ширина мёртвой зоны (0-1 от ширины экрана)
│   Пока цель в этой зоне — камера НЕ двигается
├── Dead Zone Height    — высота мёртвой зоны
├── Dead Zone Depth     — глубина мёртвой зоны (по оси Z)
│
├── Soft Zone Width     — мягкая зона (камера начинает двигаться)
│   Когда цель входит сюда — камера плавно возвращает её в центр
├── Soft Zone Height    — высота мягкой зоны
│
├── Bias X              — смещение центра по горизонтали (-0.5 до 0.5)
│   Полезно для следования в профиль (игрок смотрит вправо — сдвиг влево)
├── Bias Y              — смещение центра по вертикали
│
└── Center On Activate  — центрировать при активации камеры
```

**Визуальное объяснение зон:**



```csharp
┌─────────────────────────────────┐
│         Game View               │
│  ┌───────────────────────────┐  │
│  │       Soft Zone           │  │
│  │   ┌───────────────────┐   │  │
│  │   │    Dead Zone      │   │  │
│  │   │       [●]         │   │  │  ← Цель (игрок)
│  │   │   Камера стоит    │   │  │
│  │   └───────────────────┘   │  │
│  │   Камера плавно следует   │  │
│  └───────────────────────────┘  │
│   За Soft Zone — резкое следование│
└─────────────────────────────────┘
```

**Настройка Framing Transposer через код:**



```csharp
using Cinemachine;
using UnityEngine;

public class CameraFramingSetup : MonoBehaviour
{
    [SerializeField] private CinemachineVirtualCamera virtualCamera;

    void Start()
    {
        // Получаем компонент Framing Transposer
        var framingTransposer = virtualCamera
            .GetCinemachineComponent<CinemachineFramingTransposer>();

        if (framingTransposer != null)
        {
            // Настройка для 2D платформера
            framingTransposer.m_CameraDistance = 10f;

            // Мёртвая зона — 20% от ширины и высоты экрана
            framingTransposer.m_DeadZoneWidth = 0.2f;
            framingTransposer.m_DeadZoneHeight = 0.1f;

            // Мягкая зона — 80% от ширины экрана
            framingTransposer.m_SoftZoneWidth = 0.8f;
            framingTransposer.m_SoftZoneHeight = 0.8f;

            // Сдвиг — игрок чуть левее центра
            // (чтобы видеть больше пространства впереди)
            framingTransposer.m_BiasX = 0.15f;

            // Предсказание движения на 0.5 секунды вперёд
            framingTransposer.m_LookaheadTime = 0.5f;
            framingTransposer.m_LookaheadSmoothing = 10f;
        }
    }
}
```

---

## Aim

Секция **Aim** определяет **алгоритм ориентации** камеры — то, как камера поворачивается, чтобы смотреть на цель `LookAt`.

### Доступные алгоритмы Aim



```csharp
Aim
├── Do Nothing        — камера не вращается сама
├── Composer          — умное прицеливание с зонами
├── Group Composer    — прицеливание на группу объектов
├── Hard Look At      — жёсткое прицеливание точно в цель
├── POV               — управление мышью (Point of View)
└── Same As Follow Target — использовать поворот цели Follow
```

### Composer — умное прицеливание

Аналог Framing Transposer, но для **вращения** камеры. Работает с теми же концепциями Dead Zone и Soft Zone, но в угловом пространстве.



```csharp
Aim: Composer
├── Tracked Object Offset — смещение точки прицеливания от LookAt цели
│   Например (0, 1, 0) — смотреть на метр выше позиции игрока
│
├── Lookahead Time        — предсказание вращения
├── Lookahead Smoothing   — сглаживание предсказания поворота
├── Lookahead Ignore Y    — игнорировать вертикальное предсказание
│
├── Horizontal Damping    — плавность горизонтального поворота
├── Vertical Damping      — плавность вертикального поворота
│
├── Screen X (Bias X)     — горизонтальная позиция цели на экране (0-1)
│   0 = левый край, 0.5 = центр, 1 = правый край
├── Screen Y (Bias Y)     — вертикальная позиция цели на экране (0-1)
│
├── Dead Zone Width       — горизонтальная мёртвая зона (в градусах)
├── Dead Zone Height      — вертикальная мёртвая зона
│
├── Soft Zone Width       — мягкая горизонтальная зона
├── Soft Zone Height      — мягкая вертикальная зона
│
└── Center On Activate    — центрировать при активации
```

**Пример настройки Composer:**



```csharp
using Cinemachine;
using UnityEngine;

public class AimComposerSetup : MonoBehaviour
{
    [SerializeField] private CinemachineVirtualCamera virtualCamera;

    void ConfigureAimComposer()
    {
        var composer = virtualCamera
            .GetCinemachineComponent<CinemachineComposer>();

        if (composer == null)
        {
            Debug.LogWarning("Composer не найден! " +
                             "Убедитесь что в Aim выбран Composer");
            return;
        }

        // Смотреть немного выше головы персонажа
        composer.m_TrackedObjectOffset = new Vector3(0f, 1.8f, 0f);

        // Цель находится чуть левее центра экрана
        // (персонаж смотрит вправо — видим больше пространства)
        composer.m_ScreenX = 0.4f;
        composer.m_ScreenY = 0.5f;

        // Небольшая мёртвая зона — камера не реагирует на мелкие движения
        composer.m_DeadZoneWidth = 0.1f;
        composer.m_DeadZoneHeight = 0.1f;

        // Мягкая зона — плавное возвращение к цели
        composer.m_SoftZoneWidth = 0.6f;
        composer.m_SoftZoneHeight = 0.6f;

        // Плавный поворот камеры
        composer.m_HorizontalDamping = 0.5f;
        composer.m_VerticalDamping = 0.3f;
    }
}
```

### Hard Look At

Самый простой алгоритм — камера **всегда** точно смотрит на цель `LookAt` без каких-либо зон и плавности. Подходит для камер, которые должны жёстко следить за объектом.



```csharp
Aim: Hard Look At
└── (нет настраиваемых параметров)
    Камера мгновенно и точно смотрит на LookAt цель
```

---

## Damping

**Damping** (демпфирование) — один из важнейших параметров Cinemachine. Он определяет, насколько **плавно** камера реагирует на изменение позиции или поворота цели.

### Принцип работы



```csharp
Damping = 0  →  Камера мгновенно следует за целью (жёстко)
Damping = 1  →  Камера следует с небольшой задержкой (мягко)
Damping = 5  →  Камера очень медленно догоняет цель
Damping = 10 →  Очень ленивая камера, почти не реагирует
```

Физически Damping — это время в секундах, за которое камера проходит **половину** оставшегося расстояния до цели (exponential decay).

### Damping в Transposer



```csharp
Body: Transposer
└── Damping
    ├── X: 0.5  — горизонтальное следование (быстрее)
    ├── Y: 1.0  — вертикальное следование (медленнее — приятнее)
    └── Z: 0.5  — следование по глубине
```

### Damping в Framing Transposer



```csharp
Body: Framing Transposer
├── X Damping: 0.5
├── Y Damping: 1.0
└── Z Damping: 2.0   — изменение дистанции очень плавное
```

### Практические рекомендации по Damping

|Тип игры|X Damping|Y Damping|Описание|
|---|---|---|---|
|2D Платформер|0.3|0.8|Быстрое горизонтальное, плавное вертикальное|
|3D Экшн (TPS)|0.5|0.5|Сбалансированное|
|Хоррор|2.0|2.0|Очень ленивая, нагнетает атмосферу|
|Гоночная игра|0.1|0.1|Почти жёсткое следование|
|Стратегия|1.0|1.0|Плавное|

### Управление Damping через код



```csharp
using Cinemachine;
using UnityEngine;

public class DampingController : MonoBehaviour
{
    [SerializeField] private CinemachineVirtualCamera virtualCamera;

    // Изменяем damping динамически (например, при рывке персонажа)
    public void SetDampingForSprint(bool isSprinting)
    {
        var transposer = virtualCamera
            .GetCinemachineComponent<CinemachineTransposer>();

        if (transposer != null)
        {
            if (isSprinting)
            {
                // При беге — камера более «ленивая», создаёт ощущение скорости
                transposer.m_XDamping = 1.5f;
                transposer.m_YDamping = 2.0f;
                transposer.m_ZDamping = 1.5f;
            }
            else
            {
                // В покое — обычная плавность
                transposer.m_XDamping = 0.5f;
                transposer.m_YDamping = 0.8f;
                transposer.m_ZDamping = 0.5f;
            }
        }
    }
}
```

---

## Camera Shake

Тряска камеры — важный инструмент для передачи удара, взрыва, землетрясения. В Cinemachine она реализуется через компонент **CinemachineBasicMultiChannelPerlin**.

### Noise Profiles

Тряска основана на **Noise Profiles** — встроенных профилях шума. После установки Cinemachine они доступны в папке `Packages/Cinemachine/Presets/Noise/`:



```csharp
Встроенные профили:
├── 6D Shake        — полноценная 6-DOF тряска (позиция + вращение)
├── Handheld_tele_mild   — лёгкая "ручная камера"
├── Handheld_tele_strong — сильная "ручная камера"
├── shake-noise     — простая тряска
└── ...
```

### Настройка через Inspector

1. Выберите Virtual Camera
2. В секции **Noise** выберите `Basic Multi Channel Perlin`
3. Назначьте **Noise Profile** (например, `6D Shake`)
4. Установите **Amplitude Gain** и **Frequency Gain**



```csharp
Noise: Basic Multi Channel Perlin
├── Noise Profile    — профиль шума (ScriptableObject)
├── Amplitude Gain   — амплитуда (интенсивность) тряски
│   0 = нет тряски, 1 = нормальная, 3 = сильная
└── Frequency Gain   — частота тряски
    0.5 = медленная, 1 = нормальная, 2 = быстрая
```

### Полная система Camera Shake через код



```csharp
using System.Collections;
using Cinemachine;
using UnityEngine;

public class CameraShakeManager : MonoBehaviour
{
    // Синглтон для удобного доступа из любого скрипта
    public static CameraShakeManager Instance { get; private set; }

    [SerializeField] private CinemachineVirtualCamera virtualCamera;

    private CinemachineBasicMultiChannelPerlin _perlinNoise;

    // Корутина для затухания тряски
    private Coroutine _shakeCoroutine;

    void Awake()
    {
        // Настройка синглтона
        if (Instance == null)
        {
            Instance = this;
        }
        else
        {
            Destroy(gameObject);
            return;
        }

        // Получаем компонент шума
        _perlinNoise = virtualCamera
            .GetCinemachineComponent<CinemachineBasicMultiChannelPerlin>();

        // Изначально тряски нет
        StopShake();
    }

    /// <summary>
    /// Запустить тряску камеры
    /// </summary>
    /// <param name="amplitude">Интенсивность (0-3)</param>
    /// <param name="frequency">Частота (0.5-3)</param>
    /// <param name="duration">Длительность в секундах</param>
    public void ShakeCamera(float amplitude, float frequency, float duration)
    {
        if (_perlinNoise == null)
        {
            Debug.LogError("CinemachineBasicMultiChannelPerlin не найден!");
            return;
        }

        // Если уже идёт тряска — останавливаем
        if (_shakeCoroutine != null)
        {
            StopCoroutine(_shakeCoroutine);
        }

        _shakeCoroutine = StartCoroutine(
            ShakeCoroutine(amplitude, frequency, duration)
        );
    }

    /// <summary>
    /// Тряска с затуханием (fade out)
    /// </summary>
    private IEnumerator ShakeCoroutine(
        float amplitude,
        float frequency,
        float duration)
    {
        // Применяем тряску
        _perlinNoise.m_AmplitudeGain = amplitude;
        _perlinNoise.m_FrequencyGain = frequency;

        float elapsed = 0f;

        while (elapsed < duration)
        {
            elapsed += Time.deltaTime;

            // Плавное затухание тряски к концу
            float fadeProgress = elapsed / duration;
            float currentAmplitude = Mathf.Lerp(amplitude, 0f, fadeProgress);
            _perlinNoise.m_AmplitudeGain = currentAmplitude;

            yield return null;
        }

        // Полностью останавливаем тряску
        StopShake();
    }

    /// <summary>
    /// Мгновенно остановить тряску
    /// </summary>
    public void StopShake()
    {
        if (_perlinNoise != null)
        {
            _perlinNoise.m_AmplitudeGain = 0f;
            _perlinNoise.m_FrequencyGain = 1f;
        }
    }
}
```

### Использование в других скриптах



```csharp
using UnityEngine;

public class PlayerWeapon : MonoBehaviour
{
    [Header("Параметры тряски при выстреле")]
    [SerializeField] private float shakeAmplitude = 1.5f;
    [SerializeField] private float shakeFrequency = 2.0f;
    [SerializeField] private float shakeDuration = 0.2f;

    [Header("Параметры тряски при взрыве")]
    [SerializeField] private float explosionAmplitude = 3.0f;
    [SerializeField] private float explosionDuration = 0.5f;

    public void OnShoot()
    {
        // Лёгкая тряска при выстреле
        CameraShakeManager.Instance?.ShakeCamera(
            shakeAmplitude,
            shakeFrequency,
            shakeDuration
        );
    }

    public void OnExplosionNearby()
    {
        // Сильная тряска при близком взрыве
        CameraShakeManager.Instance?.ShakeCamera(
            explosionAmplitude,
            3.0f,
            explosionDuration
        );
    }
}
```

---

## Multiple Virtual Cameras

Сила Cinemachine в работе с **несколькими** виртуальными камерами. Вы можете иметь десятки камер, и Brain автоматически управляет переходами между ними.

### Система приоритетов



```csharp
Priority 0:   Камера неактивна (но существует)
Priority 10:  Стандартный gameplay (активна по умолчанию)
Priority 20:  Диалоговая сцена (перебивает gameplay)
Priority 30:  Катсцена (перебивает всё)
Priority 100: Экстренная камера (всегда на первом месте)
```

**Правило:** Brain всегда активирует камеру с **наибольшим** Priority. При равном Priority выигрывает та, что стоит выше в иерархии.

### Создание нескольких камер



```csharp
using Cinemachine;
using UnityEngine;

public class CameraManager : MonoBehaviour
{
    [Header("Виртуальные камеры")]
    [SerializeField] private CinemachineVirtualCamera gameplayCamera;
    [SerializeField] private CinemachineVirtualCamera dialogueCamera;
    [SerializeField] private CinemachineVirtualCamera deathCamera;
    [SerializeField] private CinemachineVirtualCamera bossCamera;

    // Константы приоритетов
    private const int PRIORITY_INACTIVE = 0;
    private const int PRIORITY_GAMEPLAY = 10;
    private const int PRIORITY_DIALOGUE = 20;
    private const int PRIORITY_BOSS = 25;
    private const int PRIORITY_DEATH = 30;

    void Start()
    {
        // Инициализация — только gameplay камера активна
        ResetAllPriorities();
        gameplayCamera.Priority = PRIORITY_GAMEPLAY;
    }

    private void ResetAllPriorities()
    {
        gameplayCamera.Priority = PRIORITY_INACTIVE;
        dialogueCamera.Priority = PRIORITY_INACTIVE;
        deathCamera.Priority = PRIORITY_INACTIVE;
        bossCamera.Priority = PRIORITY_INACTIVE;
    }

    public void ActivateGameplayCamera()
    {
        ResetAllPriorities();
        gameplayCamera.Priority = PRIORITY_GAMEPLAY;
        Debug.Log("📹 Gameplay камера активна");
    }

    public void ActivateDialogueCamera()
    {
        dialogueCamera.Priority = PRIORITY_DIALOGUE;
        Debug.Log("📹 Диалоговая камера активна");
    }

    public void DeactivateDialogueCamera()
    {
        dialogueCamera.Priority = PRIORITY_INACTIVE;
        Debug.Log("📹 Возврат к gameplay камере");
    }

    public void ActivateBossCamera()
    {
        bossCamera.Priority = PRIORITY_BOSS;
        Debug.Log("📹 Камера босса активна!");
    }

    public void DeactivateBossCamera()
    {
        bossCamera.Priority = PRIORITY_INACTIVE;
    }

    public void ActivateDeathCamera()
    {
        // Смерть перебивает всё
        deathCamera.Priority = PRIORITY_DEATH;
        Debug.Log("📹 Камера смерти...");
    }
}
```

### Настройка переходов (Blends)



```csharp
using Cinemachine;
using UnityEngine;

public class BlendSetup : MonoBehaviour
{
    [SerializeField] private CinemachineBrain brain;

    void Start()
    {
        ConfigureBlends();
    }

    private void ConfigureBlends()
    {
        // Настройка перехода по умолчанию
        brain.m_DefaultBlend = new CinemachineBlendDefinition(
            CinemachineBlendDefinition.Style.EaseInOut,
            1.5f  // 1.5 секунды
        );

        // Кастомные переходы для конкретных пар камер
        // (обычно настраивается через Inspector в Custom Blends)
    }

    // Пример: резкое переключение (Cut) без перехода
    public void CutToCamera(CinemachineVirtualCamera targetCamera)
    {
        // Временно меняем тип перехода на Cut
        var savedBlend = brain.m_DefaultBlend;

        brain.m_DefaultBlend = new CinemachineBlendDefinition(
            CinemachineBlendDefinition.Style.Cut,
            0f
        );

        // Активируем камеру
        targetCamera.Priority = 100;

        // Восстанавливаем плавный переход (через 1 кадр)
        StartCoroutine(RestoreBlendNextFrame(savedBlend));
    }

    private System.Collections.IEnumerator RestoreBlendNextFrame(
        CinemachineBlendDefinition blend)
    {
        yield return null;
        brain.m_DefaultBlend = blend;
    }
}
```

---

## Практическое задание

Давайте создадим полноценную систему из **двух виртуальных камер**:

1. **Gameplay камера** — следит за игроком во время обычного геймплея
2. **Boss камера** — автоматически активируется при входе игрока в зону босса

### Схема проекта



```csharp
Scene Hierarchy
├── Main Camera                     ← CinemachineBrain
│
├── CM_Gameplay (Virtual Camera)    ← Follow: Player, Priority: 10
├── CM_Boss (Virtual Camera)        ← LookAt: Boss, Priority: 0
│
├── Player                          ← PlayerController + Rigidbody
│
├── Boss                            ← BossEnemy
│
└── BossZoneTrigger                 ← Collider (IsTrigger: true)
    └── BossTriggerHandler.cs
```

### Шаг 1 — Создание структуры сцены



```csharp
1. Создайте сцену с объектами: Player, Boss
2. GameObject → Cinemachine → Virtual Camera → назовите "CM_Gameplay"
3. GameObject → Cinemachine → Virtual Camera → назовите "CM_Boss"
4. Создайте пустой объект "BossZoneTrigger"
   - Добавьте Box Collider → Is Trigger: true
   - Расставьте вокруг зоны босса
```

### Шаг 2 — Настройка CM_Gameplay



```csharp
CM_Gameplay настройки:
├── Priority: 10
├── Follow: Player
├── Look At: Player
├── Body: Framing Transposer
│   ├── Camera Distance: 10
│   ├── Dead Zone Width: 0.2
│   ├── Dead Zone Height: 0.1
│   ├── Soft Zone Width: 0.8
│   ├── Soft Zone Height: 0.8
│   ├── Lookahead Time: 0.3
│   └── Y Damping: 0.8
└── Aim: Composer
    ├── Screen X: 0.5
    ├── Screen Y: 0.4  (чуть выше центра)
    └── Tracked Object Offset: (0, 1, 0)
```

### Шаг 3 — Настройка CM_Boss



```csharp
CM_Boss настройки:
├── Priority: 0  (неактивна по умолчанию)
├── Follow: (none)       ← камера стоит на месте
├── Look At: Boss        ← всегда смотрит на босса
├── Body: Do Nothing     ← не двигается
└── Aim: Hard Look At    ← жёстко смотрит на босса
```

Или более кинематографичный вариант:



```csharp
CM_Boss (вариант 2):
├── Priority: 0
├── Follow: Boss         ← следует за боссом на расстоянии
├── Look At: Boss
├── Body: Transposer
│   ├── Follow Offset: (0, 3, -8)  — за и выше босса
│   └── Damping: (1, 1, 1)
└── Aim: Composer
    ├── Screen X: 0.5
    └── Tracked Object Offset: (0, 1, 0)
```

### Шаг 4 — Скрипт триггера



```csharp
using Cinemachine;
using UnityEngine;

/// <summary>
/// Переключает камеры при входе игрока в зону босса
/// </summary>
public class BossTriggerHandler : MonoBehaviour
{
    [Header("Виртуальные камеры")]
    [SerializeField] private CinemachineVirtualCamera gameplayCamera;
    [SerializeField] private CinemachineVirtualCamera bossCamera;

    [Header("Приоритеты")]
    [SerializeField] private int gameplayPriority = 10;
    [SerializeField] private int bossPriority = 20;

    [Header("Настройки")]
    [SerializeField] private string playerTag = "Player";

    [Header("Дополнительно")]
    [Tooltip("Камера остаётся на боссе даже после выхода из зоны")]
    [SerializeField] private bool stayOnBossAfterEnter = false;

    private bool _bossSequenceStarted = false;

    void Start()
    {
        ValidateSetup();

        // Начальное состояние
        gameplayCamera.Priority = gameplayPriority;
        bossCamera.Priority = 0;
    }

    private void ValidateSetup()
    {
        if (gameplayCamera == null)
            Debug.LogError($"[{name}] Gameplay камера не назначена!");

        if (bossCamera == null)
            Debug.LogError($"[{name}] Boss камера не назначена!");

        var collider = GetComponent<Collider>();
        if (collider == null || !collider.isTrigger)
            Debug.LogError($"[{name}] Нужен Collider с Is Trigger = true!");
    }

    private void OnTriggerEnter(Collider other)
    {
        if (!other.CompareTag(playerTag)) return;
        if (_bossSequenceStarted && stayOnBossAfterEnter) return;

        Debug.Log("🎬 Игрок вошёл в зону босса — переключение камеры!");

        SwitchToBossCamera();
        _bossSequenceStarted = true;
    }

    private void OnTriggerExit(Collider other)
    {
        if (!other.CompareTag(playerTag)) return;
        if (stayOnBossAfterEnter) return;

        Debug.Log("🎬 Игрок покинул зону босса — возврат к gameplay камере");

        SwitchToGameplayCamera();
        _bossSequenceStarted = false;
    }

    private void SwitchToBossCamera()
    {
        // Поднимаем приоритет Boss камеры выше Gameplay
        bossCamera.Priority = bossPriority;

        // Brain автоматически выполнит плавный переход
    }

    private void SwitchToGameplayCamera()
    {
        // Понижаем приоритет Boss камеры — Gameplay камера становится активной
        bossCamera.Priority = 0;
    }

    /// <summary>
    /// Принудительное переключение (вызывается из других скриптов)
    /// Например, при начале битвы с боссом
    /// </summary>
    public void ForceSwitchToBoss()
    {
        SwitchToBossCamera();
    }

    public void ForceSwitchToGameplay()
    {
        SwitchToGameplayCamera();
    }

#if UNITY_EDITOR
    // Отладочная визуализация зоны триггера
    private void OnDrawGizmos()
    {
        Gizmos.color = new Color(1f, 0f, 0f, 0.2f);
        var col = GetComponent<BoxCollider>();
        if (col != null)
        {
            Gizmos.matrix = transform.localToWorldMatrix;
            Gizmos.DrawCube(col.center, col.size);
            Gizmos.color = Color.red;
            Gizmos.DrawWireCube(col.center, col.size);
        }
    }
#endif
}
```

### Шаг 5 — Дополнительный скрипт: Camera Shake при появлении босса



```csharp
using System.Collections;
using Cinemachine;
using UnityEngine;

/// <summary>
/// Полная система управления камерами с тряской при появлении босса
/// </summary>
public class BossEncounterManager : MonoBehaviour
{
    [Header("Камеры")]
    [SerializeField] private CinemachineVirtualCamera gameplayCamera;
    [SerializeField] private CinemachineVirtualCamera bossCamera;

    [Header("Тряска при появлении босса")]
    [SerializeField] private float bossAppearShakeAmplitude = 3f;
    [SerializeField] private float bossAppearShakeDuration = 1f;

    [Header("Задержка перед переключением камеры")]
    [SerializeField] private float cameraTransitionDelay = 0.5f;

    private CinemachineBasicMultiChannelPerlin _bossNoise;

    void Awake()
    {
        // Получаем компонент шума Boss камеры
        _bossNoise = bossCamera
            .GetCinemachineComponent<CinemachineBasicMultiChannelPerlin>();
    }

    /// <summary>
    /// Вызвать при начале encounter с боссом
    /// </summary>
    public void StartBossEncounter()
    {
        StartCoroutine(BossEncounterSequence());
    }

    private IEnumerator BossEncounterSequence()
    {
        Debug.Log("⚔️ Начало встречи с боссом!");

        // 1. Небольшая задержка для атмосферы
        yield return new WaitForSeconds(cameraTransitionDelay);

        // 2. Переключаем камеру на босса
        bossCamera.Priority = 20;
        gameplayCamera.Priority = 10;

        // 3. Тряска камеры — босс появился!
        yield return StartCoroutine(ShakeBossCamera());

        // 4. После тряски — стабильный вид босса
        Debug.Log("👁️ Камера стабилизировалась на боссе");
    }

    private IEnumerator ShakeBossCamera()
    {
        if (_bossNoise == null)
        {
            Debug.LogWarning("Noise компонент не найден на Boss камере. " +
                             "Добавьте BasicMultiChannelPerlin в Noise секцию.");
            yield break;
        }

        float elapsed = 0f;
        float amplitude = bossAppearShakeAmplitude;

        // Начинаем тряску
        _bossNoise.m_AmplitudeGain = amplitude;
        _bossNoise.m_FrequencyGain = 2f;

        // Плавное затухание
        while (elapsed < bossAppearShakeDuration)
        {
            elapsed += Time.deltaTime;
            float t = elapsed / bossAppearShakeDuration;
            _bossNoise.m_AmplitudeGain = Mathf.Lerp(amplitude, 0f, t);
            yield return null;
        }

        // Останавливаем тряску
        _bossNoise.m_AmplitudeGain = 0f;
    }

    public void EndBossEncounter()
    {
        StartCoroutine(EndEncounterSequence());
    }

    private IEnumerator EndEncounterSequence()
    {
        Debug.Log("🏆 Босс побеждён! Возврат к gameplay камере");

        // Небольшая задержка для финальной сцены
        yield return new WaitForSeconds(2f);

        // Возвращаемся к gameplay камере
        bossCamera.Priority = 0;

        Debug.Log("📹 Gameplay камера активна");
    }
}
```

### Шаг 6 — Финальная проверка



```csharp
using Cinemachine;
using UnityEngine;

/// <summary>
/// Тестовый скрипт — проверяет корректность настройки в Editor
/// </summary>
public class CinemachineDebugger : MonoBehaviour
{
    [SerializeField] private CinemachineBrain brain;

    void Update()
    {
        if (brain == null) return;

        // Показываем текущее состояние в Game View
        if (brain.ActiveVirtualCamera != null)
        {
            var vcam = brain.ActiveVirtualCamera as CinemachineVirtualCamera;
            if (vcam != null)
            {
                Debug.Log($"Активная камера: [{vcam.name}] " +
                          $"Priority: {vcam.Priority} " +
                          $"Blend: {brain.IsBlending}");
            }
        }
    }

#if UNITY_EDITOR
    // Горячие клавиши для тестирования в Editor
    void OnGUI()
    {
        GUILayout.BeginArea(new Rect(10, 10, 300, 100));

        if (brain.ActiveVirtualCamera != null)
        {
            GUILayout.Label($"Камера: {brain.ActiveVirtualCamera.Name}");
            GUILayout.Label($"Переход: {(brain.IsBlending ? "Да" : "Нет")}");
        }

        GUILayout.EndArea();
    }
#endif
}
```

---

## Проверь себя

### Теоретические вопросы

**1.** Что такое CinemachineBrain и где он должен находиться?

> _Ожидаемый ответ:_ CinemachineBrain — главный компонент системы, который располагается на **Main Camera**. Он следит за всеми Virtual Camera на сцене, выбирает активную по приоритету и управляет переходами.

---

**2.** Чем отличается `Follow` от `LookAt`?

> _Ожидаемый ответ:_ `Follow` определяет цель, за которой камера **физически перемещается** (через настройки Body). `LookAt` определяет цель, на которую камера **поворачивается** (через настройки Aim).

---

**3.** У вас две камеры с Priority 10 и 15. Какая будет активна? Что произойдёт если изменить Priority первой камеры на 20?

> _Ожидаемый ответ:_ Активна будет камера с Priority **15**. При изменении первой камеры на 20 — Brain автоматически переключится на неё с плавным переходом (Blend).

---

**4.** В чём разница между Dead Zone и Soft Zone в Framing Transposer?

> _Ожидаемый ответ:_ **Dead Zone** — область, где камера **вообще не реагирует** на движение цели (цель в центре и немного двигается — камера стоит). **Soft Zone** — область вокруг Dead Zone, где камера **плавно** возвращает цель в Dead Zone. За пределами Soft Zone — камера двигается жёстко.

---

**5.** Что означает Damping = 0 и Damping = 5?

> _Ожидаемый ответ:_ **Damping = 0** — камера **мгновенно** следует за целью без задержки. **Damping = 5** — камера очень **медленно и плавно** догоняет цель, создавая эффект "ленивой" камеры.

---

### Практические задания

**Задание 1** ⭐

Создайте сцену с персонажем и настройте Virtual Camera c Framing Transposer так, чтобы:

- Персонаж находился на 30% от левого края экрана (для игр где персонаж смотрит вправо)
- Dead Zone занимала 15% ширины и 10% высоты
- Было предсказание движения на 0.4 секунды

---

**Задание 2** ⭐⭐

Добавьте систему Camera Shake:

- Лёгкая тряска (amplitude 0.5, duration 0.1) при прыжке персонажа
- Сильная тряска (amplitude 3.0, duration 0.6) при приземлении после большого падения
- Тряска должна плавно затухать (fade out)

---

**Задание 3** ⭐⭐⭐

Реализуйте систему из **трёх** виртуальных камер:

1. **Gameplay** — следит за игроком (Priority: 10)
2. **Boss Intro** — показывает босса 3 секунды при входе в зону (Priority: 20, затем сбрасывается)
3. **Boss Fight** — следит за игроком но с большим отдалением для вида всей арены (Priority: 15)

Переключение должно происходить автоматически через триггеры с плавными переходами.

---

**Задание 4** ⭐⭐⭐⭐

Создайте **динамическое изменение Damping** в зависимости от скорости персонажа:

- Скорость 0 (стоит) → Damping = 1.0 (плавное)
- Скорость максимальная (бежит) → Damping = 0.1 (почти жёсткое)
- Плавная интерполяция между значениями через `Mathf.Lerp`

---

### Быстрый чеклист перед релизом



```csharp
✅ Все виртуальные камеры имеют корректный Priority
✅ На Main Camera есть CinemachineBrain
✅ Default Blend настроен (рекомендуется EaseInOut, 1-2 секунды)
✅ Damping не равен 0 (иначе камера дёргается)
✅ Dead Zone не слишком большая (иначе цель выходит за экран)
✅ Lookahead не слишком большой (иначе камера "предугадывает" неправильно)
✅ Camera Shake сбрасывается в 0 после завершения
✅ Все триггеры имеют тег "Player" на игроке
✅ Нет скриптов, которые вручную двигают Main Camera
```

---

> **Итог:** Cinemachine — это мощный инструмент, который превращает работу с камерой из рутинного программирования в творческий процесс. Освоив базовые концепции Priority, Body и Aim, вы сможете создавать кинематографичные игровые моменты без единой строчки сложного кода. Виртуальные камеры декларативны — вы описываете _что_ должна делать камера, а Cinemachine сам разбирается _как_ это сделать.