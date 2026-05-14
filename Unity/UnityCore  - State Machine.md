## Содержание

- [1. Введение — что такое State Machine {#введение}](#1.%20%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%E2%80%94%20%D1%87%D1%82%D0%BE%20%D1%82%D0%B0%D0%BA%D0%BE%D0%B5%20State%20Machine%20%7B#%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%7D)
	- [Где применяется State Machine в играх?](#%D0%93%D0%B4%D0%B5%20%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D1%8F%D0%B5%D1%82%D1%81%D1%8F%20State%20Machine%20%D0%B2%20%D0%B8%D0%B3%D1%80%D0%B0%D1%85?)
	- [Основные понятия](#%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5%20%D0%BF%D0%BE%D0%BD%D1%8F%D1%82%D0%B8%D1%8F)
	- [Диаграмма состояний персонажа](#%D0%94%D0%B8%D0%B0%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B0%20%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D0%B9%20%D0%BF%D0%B5%D1%80%D1%81%D0%BE%D0%BD%D0%B0%D0%B6%D0%B0)
- [2. Проблема без State Machine — хаос if/else {#проблема}](#2.%20%D0%9F%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0%20%D0%B1%D0%B5%D0%B7%20State%20Machine%20%E2%80%94%20%D1%85%D0%B0%D0%BE%D1%81%20if/else%20%7B#%D0%BF%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0%7D)
	- [😱 Как выглядит код без State Machine](#%F0%9F%98%B1%20%D0%9A%D0%B0%D0%BA%20%D0%B2%D1%8B%D0%B3%D0%BB%D1%8F%D0%B4%D0%B8%D1%82%20%D0%BA%D0%BE%D0%B4%20%D0%B1%D0%B5%D0%B7%20State%20Machine)
	- [Что не так с этим кодом?](#%D0%A7%D1%82%D0%BE%20%D0%BD%D0%B5%20%D1%82%D0%B0%D0%BA%20%D1%81%20%D1%8D%D1%82%D0%B8%D0%BC%20%D0%BA%D0%BE%D0%B4%D0%BE%D0%BC?)
	- [Проблема множественных состояний](#%D0%9F%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0%20%D0%BC%D0%BD%D0%BE%D0%B6%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D1%85%20%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D0%B9)
- [3. Enum-based State Machine — простое решение {#enum-based}](#3.%20Enum-based%20State%20Machine%20%E2%80%94%20%D0%BF%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%B5%20%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D0%B5%20%7B#enum-based%7D)
	- [Определяем состояния](#%D0%9E%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D1%8F%D0%B5%D0%BC%20%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F)
	- [Реализация через enum](#%D0%A0%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20enum)
	- [✅ Что улучшилось с Enum-based подходом?](#%E2%9C%85%20%D0%A7%D1%82%D0%BE%20%D1%83%D0%BB%D1%83%D1%87%D1%88%D0%B8%D0%BB%D0%BE%D1%81%D1%8C%20%D1%81%20Enum-based%20%D0%BF%D0%BE%D0%B4%D1%85%D0%BE%D0%B4%D0%BE%D0%BC?)
	- [Недостатки Enum-based подхода](#%D0%9D%D0%B5%D0%B4%D0%BE%D1%81%D1%82%D0%B0%D1%82%D0%BA%D0%B8%20Enum-based%20%D0%BF%D0%BE%D0%B4%D1%85%D0%BE%D0%B4%D0%B0)
- [4. Class-based State Machine — профессиональный подход {#class-based}](#4.%20Class-based%20State%20Machine%20%E2%80%94%20%D0%BF%D1%80%D0%BE%D1%84%D0%B5%D1%81%D1%81%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%BF%D0%BE%D0%B4%D1%85%D0%BE%D0%B4%20%7B#class-based%7D)
	- [Архитектура системы](#%D0%90%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B)
	- [Шаг 1: Интерфейс IState](#%D0%A8%D0%B0%D0%B3%201:%20%D0%98%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%20IState)
	- [Шаг 2: Базовый класс State (опционально)](#%D0%A8%D0%B0%D0%B3%202:%20%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B9%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%20State%20(%D0%BE%D0%BF%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE))
	- [Шаг 3: Класс StateMachine](#%D0%A8%D0%B0%D0%B3%203:%20%D0%9A%D0%BB%D0%B0%D1%81%D1%81%20StateMachine)
	- [Шаг 4: Контроллер персонажа с StateMachine](#%D0%A8%D0%B0%D0%B3%204:%20%D0%9A%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D0%BB%D0%B5%D1%80%20%D0%BF%D0%B5%D1%80%D1%81%D0%BE%D0%BD%D0%B0%D0%B6%D0%B0%20%D1%81%20StateMachine)
- [5. Состояния персонажа — реализация конкретных состояний {#состояния-персонажа}](#5.%20%D0%A1%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F%20%D0%BF%D0%B5%D1%80%D1%81%D0%BE%D0%BD%D0%B0%D0%B6%D0%B0%20%E2%80%94%20%D1%80%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%BA%D0%BE%D0%BD%D0%BA%D1%80%D0%B5%D1%82%D0%BD%D1%8B%D1%85%20%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D0%B9%20%7B#%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F-%D0%BF%D0%B5%D1%80%D1%81%D0%BE%D0%BD%D0%B0%D0%B6%D0%B0%7D)
	- [IdleState — состояние покоя](#IdleState%20%E2%80%94%20%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D0%B5%20%D0%BF%D0%BE%D0%BA%D0%BE%D1%8F)
	- [RunState — состояние бега](#RunState%20%E2%80%94%20%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D0%B5%20%D0%B1%D0%B5%D0%B3%D0%B0)
	- [JumpState — состояние прыжка](#JumpState%20%E2%80%94%20%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D0%B5%20%D0%BF%D1%80%D1%8B%D0%B6%D0%BA%D0%B0)
	- [FallState — состояние падения](#FallState%20%E2%80%94%20%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D0%B5%20%D0%BF%D0%B0%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F)
	- [LandState — состояние приземления](#LandState%20%E2%80%94%20%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D0%B5%20%D0%BF%D1%80%D0%B8%D0%B7%D0%B5%D0%BC%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F)
	- [AttackState — состояние атаки](#AttackState%20%E2%80%94%20%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D0%B5%20%D0%B0%D1%82%D0%B0%D0%BA%D0%B8)
- [6. Переходы между состояниями — логика и условия {#переходы}](#6.%20%D0%9F%D0%B5%D1%80%D0%B5%D1%85%D0%BE%D0%B4%D1%8B%20%D0%BC%D0%B5%D0%B6%D0%B4%D1%83%20%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F%D0%BC%D0%B8%20%E2%80%94%20%D0%BB%D0%BE%D0%B3%D0%B8%D0%BA%D0%B0%20%D0%B8%20%D1%83%D1%81%D0%BB%D0%BE%D0%B2%D0%B8%D1%8F%20%7B#%D0%BF%D0%B5%D1%80%D0%B5%D1%85%D0%BE%D0%B4%D1%8B%7D)
	- [Типы переходов](#%D0%A2%D0%B8%D0%BF%D1%8B%20%D0%BF%D0%B5%D1%80%D0%B5%D1%85%D0%BE%D0%B4%D0%BE%D0%B2)
	- [Матрица переходов](#%D0%9C%D0%B0%D1%82%D1%80%D0%B8%D1%86%D0%B0%20%D0%BF%D0%B5%D1%80%D0%B5%D1%85%D0%BE%D0%B4%D0%BE%D0%B2)
	- [Сложные переходы с приоритетами](#%D0%A1%D0%BB%D0%BE%D0%B6%D0%BD%D1%8B%D0%B5%20%D0%BF%D0%B5%D1%80%D0%B5%D1%85%D0%BE%D0%B4%D1%8B%20%D1%81%20%D0%BF%D1%80%D0%B8%D0%BE%D1%80%D0%B8%D1%82%D0%B5%D1%82%D0%B0%D0%BC%D0%B8)
	- [Переходы с условиями и задержками](#%D0%9F%D0%B5%D1%80%D0%B5%D1%85%D0%BE%D0%B4%D1%8B%20%D1%81%20%D1%83%D1%81%D0%BB%D0%BE%D0%B2%D0%B8%D1%8F%D0%BC%D0%B8%20%D0%B8%20%D0%B7%D0%B0%D0%B4%D0%B5%D1%80%D0%B6%D0%BA%D0%B0%D0%BC%D0%B8)
	- [Система событий для переходов](#%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9%20%D0%B4%D0%BB%D1%8F%20%D0%BF%D0%B5%D1%80%D0%B5%D1%85%D0%BE%D0%B4%D0%BE%D0%B2)
- [7. Практическое задание — полноценный State Machine {#практика}](#7.%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%E2%80%94%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%86%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9%20State%20Machine%20%7B#%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0%7D)
	- [Полная структура проекта](#%D0%9F%D0%BE%D0%BB%D0%BD%D0%B0%D1%8F%20%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
	- [Финальная версия IState.cs](#%D0%A4%D0%B8%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%8F%20IState.cs)
	- [Финальная версия BaseState.cs](#%D0%A4%D0%B8%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%8F%20BaseState.cs)
	- [Финальная версия StateMachine.cs](#%D0%A4%D0%B8%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%8F%20StateMachine.cs)
	- [Финальная версия PlayerController.cs](#%D0%A4%D0%B8%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%8F%20PlayerController.cs)
	- [Отладчик StateMachineDebugger.cs](#%D0%9E%D1%82%D0%BB%D0%B0%D0%B4%D1%87%D0%B8%D0%BA%20StateMachineDebugger.cs)
	- [Инструкция по настройке в Unity](#%D0%98%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%86%D0%B8%D1%8F%20%D0%BF%D0%BE%20%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B5%20%D0%B2%20Unity)
- [8. Проверь себя {#проверь-себя}](#8.%20%D0%9F%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D1%8C%20%D1%81%D0%B5%D0%B1%D1%8F%20%7B#%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D1%8C-%D1%81%D0%B5%D0%B1%D1%8F%7D)
	- [📝 Теоретические вопросы](#%F0%9F%93%9D%20%D0%A2%D0%B5%D0%BE%D1%80%D0%B5%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%B2%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D1%8B)
	- [🔧 Практические задания](#%F0%9F%94%A7%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F)
	- [🧠 Вопросы для самопроверки](#%F0%9F%A7%A0%20%D0%92%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D1%8B%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%B0%D0%BC%D0%BE%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B8)
	- [✅ Чеклист — что должно работать в итоге](#%E2%9C%85%20%D0%A7%D0%B5%D0%BA%D0%BB%D0%B8%D1%81%D1%82%20%E2%80%94%20%D1%87%D1%82%D0%BE%20%D0%B4%D0%BE%D0%BB%D0%B6%D0%BD%D0%BE%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D1%82%D1%8C%20%D0%B2%20%D0%B8%D1%82%D0%BE%D0%B3%D0%B5)
- [Итоги](#%D0%98%D1%82%D0%BE%D0%B3%D0%B8)


---

## 1. Введение — что такое State Machine {#введение}

**State Machine (Конечный автомат)** — это паттерн проектирования, который позволяет объекту изменять своё поведение в зависимости от внутреннего состояния. Создаётся впечатление, будто объект изменил свой класс.

### Где применяется State Machine в играх?



```csharp
🎮 Персонаж:        Idle → Running → Jumping → Falling → Landing
🤖 ИИ врага:        Patrol → Chase → Attack → Death → Respawn  
🎯 Игровой процесс: Menu → Playing → Paused → GameOver
🚪 Двери:           Closed → Opening → Open → Closing
💬 Диалоги:         Hidden → FadeIn → Showing → FadeOut
🎵 Аудио:           Silent → FadeIn → Playing → FadeOut
```

### Основные понятия

|Термин|Описание|Пример|
|---|---|---|
|**State**|Состояние — конкретное поведение объекта|`Running`, `Jumping`, `Attacking`|
|**Transition**|Переход — смена одного состояния на другое|`Idle → Running` при нажатии WASD|
|**Trigger**|Триггер — событие, запускающее переход|Нажатие клавиши, столкновение|
|**Condition**|Условие — логическая проверка для перехода|`isGrounded && Input.Space`|

### Диаграмма состояний персонажа



```csharp
          [Start]
             │
             ▼
        ┌─────────┐   Input.Move   ┌─────────┐
        │  IDLE   │───────────────►│ RUNNING │
        │         │                │         │
        └─────────┘                └─────────┘
             ▲                           │
             │ Input.None                │ Input.Jump
             │                           │  && isGrounded
             │                           ▼
        ┌─────────┐                ┌─────────┐
        │ LANDING │                │ JUMPING │
        │         │                │         │
        └─────────┘                └─────────┘
             ▲                           │
             │ isGrounded                │ velocity.y < 0
             │                           ▼
             │                      ┌─────────┐
             └──────────────────────│ FALLING │
                                    │         │
                                    └─────────┘
```

---

## 2. Проблема без State Machine — хаос if/else {#проблема}

### 😱 Как выглядит код без State Machine



```csharp
public class PlayerControllerBad : MonoBehaviour
{
    [SerializeField] private float speed = 5f;
    [SerializeField] private float jumpForce = 10f;
    
    private Rigidbody2D rb;
    private bool isGrounded;
    private bool isJumping;
    private bool isAttacking;
    private bool isRunning;
    private float attackTimer;
    private float jumpTimer;

    private void Update()
    {
        // ❌ ХАОС НАЧАЛАСЬ — все состояния в одной куче
        
        if (isAttacking)
        {
            attackTimer -= Time.deltaTime;
            if (attackTimer <= 0)
            {
                isAttacking = false;
                Debug.Log("Attack finished");
            }
            // Во время атаки запрещено двигаться... или можно? 🤔
            return; // А может не return? Кто знает!
        }

        if (isJumping)
        {
            jumpTimer -= Time.deltaTime;
            if (jumpTimer <= 0 || isGrounded)
            {
                isJumping = false;
                Debug.Log("Jump finished");
            }
            
            // Можно ли атаковать в прыжке? А бегать в воздухе?
            if (Input.GetKeyDown(KeyCode.X) && !isAttacking)
            {
                isAttacking = true;
                attackTimer = 0.5f;
                // А что с прыжком? Отменяется? Продолжается?
            }
        }

        float input = Input.GetAxis("Horizontal");
        
        if (Mathf.Abs(input) > 0.1f)
        {
            if (!isJumping && !isAttacking) // А если и то и то?
            {
                isRunning = true;
                rb.velocity = new Vector2(input * speed, rb.velocity.y);
                Debug.Log("Running");
            }
            else if (isJumping && !isAttacking) // Можно бегать в прыжке?
            {
                rb.velocity = new Vector2(input * speed * 0.7f, rb.velocity.y);
            }
            // А если isAttacking = true? Вообще не двигаться?
        }
        else
        {
            isRunning = false;
            if (!isJumping && !isAttacking)
            {
                rb.velocity = new Vector2(0, rb.velocity.y);
                Debug.Log("Idle");
            }
        }

        if (Input.GetKeyDown(KeyCode.Space))
        {
            if (isGrounded && !isAttacking) // А что если уже прыгает?
            {
                if (isJumping) // Эта проверка бессмысленна!
                {
                    // Мы же уже проверили isGrounded...
                }
                
                isJumping = true;
                jumpTimer = 0.3f;
                rb.velocity = new Vector2(rb.velocity.x, jumpForce);
                Debug.Log("Jump started");
            }
        }

        if (Input.GetKeyDown(KeyCode.X))
        {
            if (!isAttacking && !isJumping) // А в воздухе нельзя атаковать?
            {
                isAttacking = true;
                attackTimer = 0.5f;
                Debug.Log("Attack started");
                rb.velocity = Vector2.zero; // Останавливаемся полностью?
            }
        }

        // А где проверка на падение? А на приземление?
        // А что если добавить состояние "Hurt" или "Dead"? 
        // Каждое новое состояние = новый уровень ада в этой функции!
    }
}
```

### Что не так с этим кодом?

|Проблема|Описание|
|---|---|
|**🤯 Когнитивная нагрузка**|Вся логика всех состояний в одном методе|
|**🐛 Баги из-за флагов**|`isJumping && !isGrounded` — противоречивые состояния|
|**🔄 Дублирование**|Одинаковые условия `!isAttacking && !isJumping`|
|**📈 Экспоненциальная сложность**|N состояний = N² проверок комбинаций|
|**🚫 Невозможность расширения**|Добавить новое состояние = переписать всё|
|**🧪 Нетестируемость**|Невозможно изолированно протестировать одно состояние|
|**📚 Нарушение SRP**|Один метод отвечает за ВСЕ состояния|

### Проблема множественных состояний



```csharp
// ❌ Что это значит?
if (isRunning && isJumping && !isAttacking && isGrounded)
{
    // Бежим, прыгаем, на земле, не атакуем... Как так?
    // Игрок сломал физику? 🤔
}

// ❌ А это?
bool canMove = !isAttacking && !isDead && !isStunned && !isDialogOpen;
// Добавляется новое состояние → меняется эта формула везде!
```

---

## 3. Enum-based State Machine — простое решение {#enum-based}

Первый шаг к спасению — заменить множество `bool` флагов одним `enum` состоянием.

### Определяем состояния



```csharp
public enum PlayerState
{
    Idle,
    Running, 
    Jumping,
    Falling,
    Landing,
    Attacking
}
```

### Реализация через enum



```csharp
using UnityEngine;

public class PlayerControllerEnum : MonoBehaviour
{
    [Header("Settings")]
    [SerializeField] private float speed = 5f;
    [SerializeField] private float jumpForce = 10f;
    [SerializeField] private float attackDuration = 0.5f;
    
    [Header("Debug")]
    [SerializeField] private PlayerState currentState = PlayerState.Idle;
    
    private Rigidbody2D rb;
    private bool isGrounded;
    private float stateTimer; // Универсальный таймер для временны́х состояний

    private void Awake()
    {
        rb = GetComponent<Rigidbody2D>();
    }

    private void Update()
    {
        // Единая точка обработки состояний
        HandleCurrentState();
        CheckTransitions();
    }

    private void HandleCurrentState()
    {
        switch (currentState)
        {
            case PlayerState.Idle:
                HandleIdleState();
                break;
            
            case PlayerState.Running:
                HandleRunningState();
                break;
            
            case PlayerState.Jumping:
                HandleJumpingState();
                break;
            
            case PlayerState.Falling:
                HandleFallingState();
                break;
            
            case PlayerState.Landing:
                HandleLandingState();
                break;
            
            case PlayerState.Attacking:
                HandleAttackingState();
                break;
        }
    }

    private void CheckTransitions()
    {
        switch (currentState)
        {
            case PlayerState.Idle:
                if (HasMoveInput())
                    ChangeState(PlayerState.Running);
                else if (Input.GetKeyDown(KeyCode.Space) && isGrounded)
                    ChangeState(PlayerState.Jumping);
                else if (Input.GetKeyDown(KeyCode.X))
                    ChangeState(PlayerState.Attacking);
                break;

            case PlayerState.Running:
                if (!HasMoveInput())
                    ChangeState(PlayerState.Idle);
                else if (Input.GetKeyDown(KeyCode.Space) && isGrounded)
                    ChangeState(PlayerState.Jumping);
                else if (Input.GetKeyDown(KeyCode.X))
                    ChangeState(PlayerState.Attacking);
                break;

            case PlayerState.Jumping:
                if (rb.velocity.y < -0.1f) // Начинаем падать
                    ChangeState(PlayerState.Falling);
                break;

            case PlayerState.Falling:
                if (isGrounded)
                    ChangeState(PlayerState.Landing);
                break;

            case PlayerState.Landing:
                if (stateTimer <= 0) // Короткая анимация приземления
                {
                    if (HasMoveInput())
                        ChangeState(PlayerState.Running);
                    else
                        ChangeState(PlayerState.Idle);
                }
                break;

            case PlayerState.Attacking:
                if (stateTimer <= 0)
                {
                    if (HasMoveInput())
                        ChangeState(PlayerState.Running);
                    else
                        ChangeState(PlayerState.Idle);
                }
                break;
        }
    }

    #region State Handlers

    private void HandleIdleState()
    {
        rb.velocity = new Vector2(0, rb.velocity.y);
    }

    private void HandleRunningState()
    {
        float input = Input.GetAxis("Horizontal");
        rb.velocity = new Vector2(input * speed, rb.velocity.y);
    }

    private void HandleJumpingState()
    {
        // В прыжке можно немного управлять горизонтальным движением
        float input = Input.GetAxis("Horizontal");
        rb.velocity = new Vector2(input * speed * 0.7f, rb.velocity.y);
    }

    private void HandleFallingState()
    {
        // Аналогично прыжку
        float input = Input.GetAxis("Horizontal");
        rb.velocity = new Vector2(input * speed * 0.7f, rb.velocity.y);
    }

    private void HandleLandingState()
    {
        // Во время приземления движение ограничено
        rb.velocity = new Vector2(rb.velocity.x * 0.5f, rb.velocity.y);
        stateTimer -= Time.deltaTime;
    }

    private void HandleAttackingState()
    {
        // Во время атаки стоим на месте
        rb.velocity = new Vector2(0, rb.velocity.y);
        stateTimer -= Time.deltaTime;
    }

    #endregion

    private void ChangeState(PlayerState newState)
    {
        if (currentState == newState) return;

        // Выход из старого состояния
        ExitState(currentState);
        
        // Смена состояния
        PlayerState previousState = currentState;
        currentState = newState;
        
        // Вход в новое состояние
        EnterState(newState);
        
        Debug.Log($"[State] {previousState} → {newState}");
    }

    private void EnterState(PlayerState state)
    {
        switch (state)
        {
            case PlayerState.Jumping:
                rb.velocity = new Vector2(rb.velocity.x, jumpForce);
                break;
            
            case PlayerState.Landing:
                stateTimer = 0.1f; // Короткая анимация приземления
                break;
            
            case PlayerState.Attacking:
                stateTimer = attackDuration;
                // Здесь можно запустить анимацию атаки
                break;
        }
    }

    private void ExitState(PlayerState state)
    {
        // Действия при выходе из состояния (если нужны)
        switch (state)
        {
            case PlayerState.Attacking:
                // Завершить анимацию атаки
                break;
        }
    }

    private bool HasMoveInput()
    {
        return Mathf.Abs(Input.GetAxis("Horizontal")) > 0.1f;
    }

 private void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.CompareTag("Ground"))
        {
            isGrounded = true;
        }
    }

    private void OnCollisionExit2D(Collision2D collision)
    {
        if (collision.gameObject.CompareTag("Ground"))
        {
            isGrounded = false;
        }
    }
}
```

### ✅ Что улучшилось с Enum-based подходом?

|До (Bool флаги)|После (Enum состояния)|
|---|---|
|`isRunning && isJumping`|**Невозможно** — состояние только одно|
|6+ булевых переменных|**1** enum переменная|
|Логика размазана по Update|**Структурированно** по методам|
|Сложно отладить|**Видно** текущее состояние в Inspector|
|Нет гарантии корректности|**Гарантированно** валидное состояние|

### Недостатки Enum-based подхода



```csharp
// ❌ Switch растёт с каждым новым состоянием
private void HandleCurrentState()
{
    switch (currentState) // 50+ case'ов в большой игре?
    {
        case PlayerState.Idle: /*...*/ break;
        case PlayerState.Running: /*...*/ break;
        case PlayerState.Jumping: /*...*/ break;
        case PlayerState.Attacking: /*...*/ break;
        case PlayerState.Hurt: /*...*/ break;
        case PlayerState.Dead: /*...*/ break;
        case PlayerState.Swimming: /*...*/ break;
        case PlayerState.Climbing: /*...*/ break;
        // ... ещё 40 состояний
    }
}

// ❌ Невозможно переиспользовать состояние в другом контексте
// Например, и Player, и Enemy имеют состояние "Attacking"
// Но нужно дублировать логику в разных классах

// ❌ Сложно тестировать отдельное состояние
// Чтобы протестировать атаку, нужно создать весь PlayerController
```

---

## 4. Class-based State Machine — профессиональный подход {#class-based}

Class-based подход решает проблемы enum-based: каждое состояние — отдельный класс, легко тестировать и переиспользовать.

### Архитектура системы



```csharp
┌─────────────────────────────────────────────────────────────┐
│                    STATEMACHINE                             │
│                                                             │
│  - currentState: IState                                     │
│  - states: Dictionary<Type, IState>                         │
│  + ChangeState<T>()                                         │
│  + Update() → currentState.Update()                         │
└─────────────────────┬───────────────────────────────────────┘
                      │ управляет
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                     ISTATE                                  │ ← Интерфейс
│                                                             │
│  + Enter(StateMachine sm)                                   │
│  + Update()                                                 │
│  + Exit()                                                   │
└─────────────────────┬───────────────────────────────────────┘
                      │ реализуют
          ┌───────────┼───────────┬───────────┐
          ▼           ▼           ▼           ▼
    ┌──────────┐ ┌─────────┐ ┌─────────┐ ┌──────────┐
    │IdleState │ │RunState │ │JumpState│ │AttackStat│
    │          │ │         │ │         │ │          │
    │Enter()   │ │Enter()  │ │Enter()  │ │Enter()   │
    │Update()  │ │Update() │ │Update() │ │Update()  │
    │Exit()    │ │Exit()   │ │Exit()   │ │Exit()    │
    └──────────┘ └─────────┘ └─────────┘ └──────────┘
```

### Шаг 1: Интерфейс IState



```csharp
/// <summary>
/// Интерфейс для всех состояний
/// </summary>
public interface IState
{
    /// <summary>
    /// Вызывается один раз при входе в состояние
    /// </summary>
    void Enter(StateMachine stateMachine);
    
    /// <summary>
    /// Вызывается каждый кадр, пока состояние активно
    /// </summary>
    void Update();
    
    /// <summary>
    /// Вызывается один раз при выходе из состояния
    /// </summary>
    void Exit();
}
```

### Шаг 2: Базовый класс State (опционально)



```csharp
using UnityEngine;

/// <summary>
/// Базовый класс для состояний с общими свойствами
/// </summary>
public abstract class BaseState : IState
{
    protected StateMachine stateMachine;
    protected float timeInState; // Сколько времени мы в этом состоянии

    public virtual void Enter(StateMachine stateMachine)
    {
        this.stateMachine = stateMachine;
        timeInState = 0f;
    }

    public virtual void Update()
    {
        timeInState += Time.deltaTime;
    }

    public virtual void Exit()
    {
        // Очистка при выходе (если нужна)
    }
}
```

### Шаг 3: Класс StateMachine



```csharp
using System;
using System.Collections.Generic;
using UnityEngine;

/// <summary>
/// Универсальный конечный автомат
/// </summary>
public class StateMachine
{
    // Текущее активное состояние
    private IState _currentState;
    
    // Кэш всех созданных состояний (Flyweight pattern)
    private readonly Dictionary<Type, IState> _states = new();

    // Для отладки
    public IState CurrentState => _currentState;
    public string CurrentStateName => _currentState?.GetType().Name ?? "None";

    /// <summary>
    /// Обновление текущего состояния
    /// </summary>
    public void Update()
    {
        _currentState?.Update();
    }

    /// <summary>
    /// Смена состояния на новое
    /// </summary>
    public void ChangeState<T>() where T : class, IState, new()
    {
        // Получаем или создаём состояние
        var newState = GetOrCreateState<T>();
        
        if (_currentState == newState)
        {
            Debug.LogWarning($"[StateMachine] Попытка сменить состояние на то же самое: {typeof(T).Name}");
            return;
        }

        // Выходим из текущего состояния
        _currentState?.Exit();
        
        // Сохраняем предыдущее для логирования
        var previousState = _currentState;
        
        // Меняем состояние
        _currentState = newState;
        
        // Входим в новое состояние
        _currentState.Enter(this);
        
        // Логируем переход
        string prevName = previousState?.GetType().Name ?? "None";
        string newName = _currentState.GetType().Name;
        Debug.Log($"[StateMachine] {prevName} → {newName}");
    }

    /// <summary>
    /// Получает существующее состояние или создаёт новое
    /// </summary>
    private T GetOrCreateState<T>() where T : class, IState, new()
    {
        var stateType = typeof(T);
        
        if (!_states.TryGetValue(stateType, out var state))
        {
            state = new T();
            _states[stateType] = state;
        }
        
        return state as T;
    }

    /// <summary>
    /// Проверяет, находимся ли мы в указанном состоянии
    /// </summary>
    public bool IsInState<T>() where T : class, IState
    {
        return _currentState is T;
    }

    /// <summary>
    /// Принудительная остановка автомата
    /// </summary>
    public void Stop()
    {
        _currentState?.Exit();
        _currentState = null;
    }
}
```

### Шаг 4: Контроллер персонажа с StateMachine



```csharp
using UnityEngine;

/// <summary>
/// Контроллер персонажа, использующий State Machine
/// </summary>
public class PlayerController : MonoBehaviour
{
    [Header("Movement")]
    [SerializeField] private float speed = 5f;
    [SerializeField] private float jumpForce = 10f;
    [SerializeField] private float airControlFactor = 0.7f;

    [Header("Combat")]
    [SerializeField] private float attackDuration = 0.5f;

    [Header("Debug")]
    [SerializeField] private bool showDebugGUI = true;

    // Компоненты
    public Rigidbody2D Rb { get; private set; }
    public bool IsGrounded { get; private set; }

    // Настройки (доступ для состояний)
    public float Speed => speed;
    public float JumpForce => jumpForce;
    public float AirControlFactor => airControlFactor;
    public float AttackDuration => attackDuration;

    // State Machine
    private StateMachine _stateMachine;

    // Инпут (можно заменить на Input System)
    public float MoveInput { get; private set; }
    public bool JumpPressed { get; private set; }
    public bool AttackPressed { get; private set; }

    private void Awake()
    {
        Rb = GetComponent<Rigidbody2D>();
        _stateMachine = new StateMachine();
    }

    private void Start()
    {
        // Стартуем с состояния Idle
        _stateMachine.ChangeState<IdleState>();
    }

    private void Update()
    {
        HandleInput();
        _stateMachine.Update();
    }

    private void HandleInput()
    {
        MoveInput = Input.GetAxis("Horizontal");
        JumpPressed = Input.GetKeyDown(KeyCode.Space);
        AttackPressed = Input.GetKeyDown(KeyCode.X);
    }

    public void ChangeState<T>() where T : class, IState, new()
    {
        _stateMachine.ChangeState<T>();
    }

    public bool IsInState<T>() where T : class, IState
    {
        return _stateMachine.IsInState<T>();
    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.CompareTag("Ground"))
        {
            IsGrounded = true;
        }
    }

    private void OnCollisionExit2D(Collision2D collision)
    {
        if (collision.gameObject.CompareTag("Ground"))
        {
            IsGrounded = false;
        }
    }

    // Отладочный GUI
    private void OnGUI()
    {
        if (!showDebugGUI) return;

        GUI.Label(new Rect(10, 10, 200, 20), $"State: {_stateMachine.CurrentStateName}");
        GUI.Label(new Rect(10, 30, 200, 20), $"Grounded: {IsGrounded}");
        GUI.Label(new Rect(10, 50, 200, 20), $"Velocity: {Rb.velocity}");
    }
}
```

---

## 5. Состояния персонажа — реализация конкретных состояний {#состояния-персонажа}

Теперь создадим конкретные состояния для нашего персонажа.

### IdleState — состояние покоя



```csharp
using UnityEngine;

/// <summary>
/// Состояние покоя — персонаж стоит на месте
/// </summary>
public class IdleState : BaseState
{
    private PlayerController player;

    public override void Enter(StateMachine stateMachine)
    {
        base.Enter(stateMachine);
        player = stateMachine.CurrentState as PlayerController ?? 
                 Object.FindObjectOfType<PlayerController>(); // Fallback
        
        Debug.Log("[IdleState] Entering Idle");
        
        // Останавливаем горизонтальное движение
        player.Rb.velocity = new Vector2(0, player.Rb.velocity.y);
    }

    public override void Update()
    {
        base.Update();
        
        // Проверяем условия для перехода в другие состояния
        CheckTransitions();
    }

    private void CheckTransitions()
    {
        // Переход в бег
        if (Mathf.Abs(player.MoveInput) > 0.1f)
        {
            player.ChangeState<RunState>();
            return;
        }

        // Переход в прыжок
        if (player.JumpPressed && player.IsGrounded)
        {
            player.ChangeState<JumpState>();
            return;
        }

        // Переход в атаку
        if (player.AttackPressed)
        {
            player.ChangeState<AttackState>();
            return;
        }

        // Переход в падение (если упали с платформы)
        if (!player.IsGrounded && player.Rb.velocity.y < -0.1f)
        {
            player.ChangeState<FallState>();
            return;
        }
    }

    public override void Exit()
    {
        Debug.Log("[IdleState] Exiting Idle");
    }
}
```

### RunState — состояние бега



```csharp
using UnityEngine;

/// <summary>
/// Состояние бега — персонаж движется горизонтально
/// </summary>
public class RunState : BaseState
{
    private PlayerController player;

    public override void Enter(StateMachine stateMachine)
    {
        base.Enter(stateMachine);
        player = Object.FindObjectOfType<PlayerController>();
        
        Debug.Log("[RunState] Entering Run");
    }

    public override void Update()
    {
        base.Update();
        
        // Движение
        HandleMovement();
        
        // Переходы
        CheckTransitions();
    }

    private void HandleMovement()
    {
        // Горизонтальное движение на земле
        float targetVelocityX = player.MoveInput * player.Speed;
        player.Rb.velocity = new Vector2(targetVelocityX, player.Rb.velocity.y);
    }

    private void CheckTransitions()
    {
        // Остановились — переходим в Idle
        if (Mathf.Abs(player.MoveInput) < 0.1f)
        {
            player.ChangeState<IdleState>();
            return;
        }

        // Нажали прыжок
        if (player.JumpPressed && player.IsGrounded)
        {
            player.ChangeState<JumpState>();
            return;
        }

         // Нажали атаку
        if (player.AttackPressed)
        {
            player.ChangeState<AttackState>();
            return;
        }

        // Упали с платформы
        if (!player.IsGrounded && player.Rb.velocity.y < -0.1f)
        {
            player.ChangeState<FallState>();
            return;
        }
    }

    public override void Exit()
    {
        Debug.Log("[RunState] Exiting Run");
    }
}
```

### JumpState — состояние прыжка



```csharp
using UnityEngine;

/// <summary>
/// Состояние прыжка — персонаж взлетает вверх
/// </summary>
public class JumpState : BaseState
{
    private PlayerController player;

    public override void Enter(StateMachine stateMachine)
    {
        base.Enter(stateMachine);
        player = Object.FindObjectOfType<PlayerController>();
        
        Debug.Log("[JumpState] Entering Jump");
        
        // Применяем силу прыжка
        player.Rb.velocity = new Vector2(player.Rb.velocity.x, player.JumpForce);
    }

    public override void Update()
    {
        base.Update();
        
        // Воздушное управление
        HandleAirMovement();
        
        // Переходы
        CheckTransitions();
    }

    private void HandleAirMovement()
    {
        // Ограниченное управление в воздухе
        if (Mathf.Abs(player.MoveInput) > 0.1f)
        {
            float airSpeed = player.Speed * player.AirControlFactor;
            float targetVelocityX = player.MoveInput * airSpeed;
            
            // Плавное изменение скорости в воздухе
            float currentX = player.Rb.velocity.x;
            float newX = Mathf.MoveTowards(currentX, targetVelocityX, airSpeed * Time.deltaTime);
            
            player.Rb.velocity = new Vector2(newX, player.Rb.velocity.y);
        }
    }

    private void CheckTransitions()
    {
        // Начинаем падать
        if (player.Rb.velocity.y < -0.1f)
        {
            player.ChangeState<FallState>();
            return;
        }

        // Атака в воздухе (если разрешена)
        if (player.AttackPressed)
        {
            player.ChangeState<AttackState>();
            return;
        }
    }

    public override void Exit()
    {
        Debug.Log("[JumpState] Exiting Jump");
    }
}
```

### FallState — состояние падения



```csharp
using UnityEngine;

/// <summary>
/// Состояние падения — персонаж падает вниз
/// </summary>
public class FallState : BaseState
{
    private PlayerController player;

    public override void Enter(StateMachine stateMachine)
    {
        base.Enter(stateMachine);
        player = Object.FindObjectOfType<PlayerController>();
        
        Debug.Log("[FallState] Entering Fall");
    }

    public override void Update()
    {
        base.Update();
        
        // Воздушное управление (как в прыжке)
        HandleAirMovement();
        
        // Переходы
        CheckTransitions();
    }

    private void HandleAirMovement()
    {
        // Аналогично JumpState — ограниченное управление
        if (Mathf.Abs(player.MoveInput) > 0.1f)
        {
            float airSpeed = player.Speed * player.AirControlFactor;
            float targetVelocityX = player.MoveInput * airSpeed;
            
            float currentX = player.Rb.velocity.x;
            float newX = Mathf.MoveTowards(currentX, targetVelocityX, airSpeed * Time.deltaTime);
            
            player.Rb.velocity = new Vector2(newX, player.Rb.velocity.y);
        }
    }

    private void CheckTransitions()
    {
        // Приземлились
        if (player.IsGrounded)
        {
            player.ChangeState<LandState>();
            return;
        }

        // Воздушная атака
        if (player.AttackPressed)
        {
            player.ChangeState<AttackState>();
            return;
        }
    }

    public override void Exit()
    {
        Debug.Log("[FallState] Exiting Fall");
    }
}
```

### LandState — состояние приземления



```csharp
using UnityEngine;

/// <summary>
/// Состояние приземления — короткая анимация после падения
/// </summary>
public class LandState : BaseState
{
    private PlayerController player;
    private const float LAND_DURATION = 0.1f; // Длительность приземления

    public override void Enter(StateMachine stateMachine)
    {
        base.Enter(stateMachine);
        player = Object.FindObjectOfType<PlayerController>();
        
        Debug.Log("[LandState] Entering Land");
        
        // Замедляем движение при приземлении
        player.Rb.velocity = new Vector2(player.Rb.velocity.x * 0.5f, player.Rb.velocity.y);
    }

    public override void Update()
    {
        base.Update();
        
        // Ограничиваем движение во время приземления
        HandleLandMovement();
        
        // Переходы
        CheckTransitions();
    }

    private void HandleLandMovement()
    {
        // Постепенно замедляемся
        Vector2 currentVelocity = player.Rb.velocity;
        float dampedX = currentVelocity.x * (1f - Time.deltaTime * 5f);
        player.Rb.velocity = new Vector2(dampedX, currentVelocity.y);
    }

    private void CheckTransitions()
    {
        // Приземление завершено
        if (timeInState >= LAND_DURATION)
        {
            // Определяем следующее состояние на основе ввода
            if (Mathf.Abs(player.MoveInput) > 0.1f)
            {
                player.ChangeState<RunState>();
            }
            else
            {
                player.ChangeState<IdleState>();
            }
            return;
        }

        // Прерываем приземление прыжком
        if (player.JumpPressed)
        {
            player.ChangeState<JumpState>();
            return;
        }

        // Прерываем атакой
        if (player.AttackPressed)
        {
            player.ChangeState<AttackState>();
            return;
        }
    }

    public override void Exit()
    {
        Debug.Log("[LandState] Exiting Land");
    }
}
```

### AttackState — состояние атаки



```csharp
using UnityEngine;

/// <summary>
/// Состояние атаки — персонаж выполняет атаку
/// </summary>
public class AttackState : BaseState
{
    private PlayerController player;
    private bool wasGroundedOnEnter;

    public override void Enter(StateMachine stateMachine)
    {
        base.Enter(stateMachine);
        player = Object.FindObjectOfType<PlayerController>();
        wasGroundedOnEnter = player.IsGrounded;
        
        Debug.Log("[AttackState] Entering Attack");
        
        // Останавливаем горизонтальное движение при атаке на земле
        if (wasGroundedOnEnter)
        {
            player.Rb.velocity = new Vector2(0, player.Rb.velocity.y);
        }
        
        // Здесь можно запустить анимацию атаки
        // animator.SetTrigger("Attack");
        
        // Здесь можно создать хитбокс атаки
        // CreateAttackHitbox();
    }

    public override void Update()
    {
        base.Update();
        
        // Ограниченное движение во время атаки
        HandleAttackMovement();
        
        // Переходы
        CheckTransitions();
    }

    private void HandleAttackMovement()
    {
        // На земле — не двигаемся
        if (wasGroundedOnEnter)
        {
            player.Rb.velocity = new Vector2(0, player.Rb.velocity.y);
        }
        else
        {
            // В воздухе — сохраняем инерцию, но не можем управлять
            // player.Rb.velocity остаётся как есть
        }
    }

    private void CheckTransitions()
    {
        // Атака завершена
        if (timeInState >= player.AttackDuration)
        {
            // Определяем следующее состояние
            if (!player.IsGrounded)
            {
                // Если в воздухе — падаем или прыгаем
                if (player.Rb.velocity.y > 0.1f)
                    player.ChangeState<JumpState>();
                else
                    player.ChangeState<FallState>();
            }
            else
            {
                // На земле — idle или бег
                if (Mathf.Abs(player.MoveInput) > 0.1f)
                    player.ChangeState<RunState>();
                else
                    player.ChangeState<IdleState>();
            }
            return;
        }

        // Примечание: во время атаки нельзя прерывать другими действиями
        // Это дизайнерское решение — можно изменить при необходимости
    }

    public override void Exit()
    {
        Debug.Log("[AttackState] Exiting Attack");
        
        // Здесь можно убрать хитбокс атаки
        // DestroyAttackHitbox();
    }
}
```

---

## 6. Переходы между состояниями — логика и условия {#переходы}

### Типы переходов



```csharp
// 1. Переходы по вводу (Input-driven)
if (Input.GetKeyDown(KeyCode.Space))
    stateMachine.ChangeState<JumpState>();

// 2. Переходы по времени (Time-driven)
if (timeInState >= attackDuration)
    stateMachine.ChangeState<IdleState>();

// 3. Переходы по физике (Physics-driven)
if (rb.velocity.y < 0 && !isGrounded)
    stateMachine.ChangeState<FallState>();

// 4. Переходы по событиям (Event-driven)
if (health <= 0)
    stateMachine.ChangeState<DeathState>();

// 5. Условные переходы (Condition-driven)
if (isGrounded && hasInput)
    stateMachine.ChangeState<RunState>();
else if (isGrounded && !hasInput)
    stateMachine.ChangeState<IdleState>();
```

### Матрица переходов

|Из ↓ \ В →|Idle|Run|Jump|Fall|Land|Attack|
|---|---|---|---|---|---|---|
|**Idle**|❌|✅¹|✅²|✅⁵|❌|✅⁴|
|**Run**|✅³|❌|✅²|✅⁵|❌|✅⁴|
|**Jump**|❌|❌|❌|✅⁶|❌|✅⁷|
|**Fall**|❌|❌|❌|❌|✅⁸|✅⁷|
|**Land**|✅⁹|✅⁹|✅²|❌|❌|✅⁴|
|**Attack**|✅¹⁰|✅¹⁰|✅¹⁰|✅¹⁰|❌|❌|

**Условия переходов:**

- ¹ `HasMoveInput()`
- ² `JumpPressed && IsGrounded`
- ³ `!HasMoveInput()`
- ⁴ `AttackPressed`
- ⁵ `!IsGrounded && velocity.y < 0`
- ⁶ `velocity.y < 0`
- ⁷ `AttackPressed` (воздушная атака)
- ⁸ `IsGrounded`
- ⁹ `timeInState >= landDuration`
- ¹⁰ `timeInState >= attackDuration`

### Сложные переходы с приоритетами



```csharp
/// <summary>
/// Универсальный метод проверки переходов с приоритетами
/// </summary>
private void CheckTransitionsWithPriority()
{
    // Приоритет 1: Критические состояния (смерть, урон)
    if (player.Health <= 0)
    {
        player.ChangeState<DeathState>();
        return;
    }

    if (player.TookDamage)
    {
        player.ChangeState<HurtState>();
        return;
    }

    // Приоритет 2: Физика (падение с платформы)
    if (!player.IsGrounded && player.Rb.velocity.y < -0.1f && 
        !player.IsInState<JumpState>() && !player.IsInState<FallState>())
    {
        player.ChangeState<FallState>();
        return;
    }

    // Приоритет 3: Пользовательский ввод
    CheckInputTransitions();
    
    // Приоритет 4: Автоматические переходы (таймеры)
    CheckTimerTransitions();
}

private void CheckInputTransitions()
{
    // Атака — высший приоритет среди пользовательских действий
    if (player.AttackPressed)
    {
        player.ChangeState<AttackState>();
        return;
    }

    // Прыжок — только на земле
    if (player.JumpPressed && player.IsGrounded)
    {
        player.ChangeState<JumpState>();
        return;
    }

    // Движение
    if (Mathf.Abs(player.MoveInput) > 0.1f)
    {
        if (player.IsInState<IdleState>())
            player.ChangeState<RunState>();
    }
    else
    {
        if (player.IsInState<RunState>())
            player.ChangeState<IdleState>();
    }
}
```

### Переходы с условиями и задержками



```csharp
/// <summary>
/// Состояние с условными переходами
/// </summary>
public class ConditionalState : BaseState
{
    private float transitionDelay = 0.2f; // Минимальное время в состоянии
    
    public override void Update()
    {
        base.Update();
        
        // Не позволяем немедленные переходы — требуем минимальное время
        if (timeInState < transitionDelay)
            return;
            
        CheckDelay
```

Продолжаю статью с того места, где она оборвалась:



```csharp
        // Не позволяем немедленные переходы — требуем минимальное время
        if (timeInState < transitionDelay)
            return;
            
        CheckTransitions();
    }

    private void CheckTransitions()
    {
        // Теперь можно проверять переходы
    }
}
```

### Система событий для переходов



```csharp
using System;
using UnityEngine;

/// <summary>
/// State Machine на основе событий — переходы через C# события
/// </summary>
public class EventDrivenStateMachine
{
    private IState _currentState;

    // Глобальные события
    public event Action<IState, IState> OnStateChanged;

    public void ChangeState<T>() where T : class, IState, new()
    {
        var newState = new T();
        var oldState = _currentState;

        _currentState?.Exit();
        _currentState = newState;
        _currentState.Enter(this as StateMachine);

        // Уведомляем подписчиков
        OnStateChanged?.Invoke(oldState, newState);
    }
}

// Пример использования событий
public class PlayerController : MonoBehaviour
{
    private StateMachine _stateMachine;

    private void Awake()
    {
        _stateMachine = new StateMachine();

        // Подписываемся на событие смены состояния
        // _stateMachine.OnStateChanged += HandleStateChanged;
    }

    private void HandleStateChanged(IState from, IState to)
    {
        Debug.Log($"[Event] Переход: {from?.GetType().Name} → {to?.GetType().Name}");

        // Обновляем UI, аналитику, достижения и т.д.
        UpdateUI(to);
        TrackAnalytics(from, to);
    }

    private void UpdateUI(IState newState)
    {
        // Пример: показываем иконку состояния
        if (newState is AttackState)
            Debug.Log("[UI] Показываем иконку атаки");
        else if (newState is JumpState)
            Debug.Log("[UI] Показываем иконку прыжка");
    }

    private void TrackAnalytics(IState from, IState to)
    {
        // Пример: трекинг переходов для аналитики
        Debug.Log($"[Analytics] {from?.GetType().Name} → {to?.GetType().Name}");
    }
}
```

---

## 7. Практическое задание — полноценный State Machine {#практика}

Теперь соберём всё вместе в единую, рабочую систему с отладкой.

### Полная структура проекта



```csharp
Assets/
├── Scripts/
│   ├── StateMachine/
│   │   ├── IState.cs
│   │   ├── BaseState.cs
│   │   └── StateMachine.cs
│   ├── Player/
│   │   ├── PlayerController.cs
│   │   └── States/
│   │       ├── IdleState.cs
│   │       ├── RunState.cs
│   │       ├── JumpState.cs
│   │       ├── FallState.cs
│   │       ├── LandState.cs
│   │       └── AttackState.cs
│   └── Debug/
│       └── StateMachineDebugger.cs
```

### Финальная версия IState.cs



```csharp
/// <summary>
/// Базовый интерфейс для всех состояний
/// </summary>
public interface IState
{
    void Enter(StateMachine stateMachine);
    void Update();
    void Exit();
}
```

### Финальная версия BaseState.cs



```csharp
using UnityEngine;

/// <summary>
/// Базовый класс с общей логикой для всех состояний
/// </summary>
public abstract class BaseState : IState
{
    protected StateMachine StateMachine;
    protected float TimeInState;

    public virtual void Enter(StateMachine stateMachine)
    {
        StateMachine = stateMachine;
        TimeInState = 0f;
        Debug.Log($"[{GetType().Name}] Enter");
    }

    public virtual void Update()
    {
        TimeInState += Time.deltaTime;
    }

    public virtual void Exit()
    {
        Debug.Log($"[{GetType().Name}] Exit (время в состоянии: {TimeInState:F2}s)");
    }
}
```

### Финальная версия StateMachine.cs



```csharp
using System;
using System.Collections.Generic;
using UnityEngine;

/// <summary>
/// Универсальный конечный автомат с историей переходов
/// </summary>
public class StateMachine
{
    private IState _currentState;
    private readonly Dictionary<Type, IState> _stateCache = new();

    // История последних переходов для отладки
    private readonly Queue<string> _transitionHistory = new();
    private const int MAX_HISTORY = 10;

    public IState CurrentState => _currentState;
    public string CurrentStateName => _currentState?.GetType().Name ?? "None";
    public IEnumerable<string> TransitionHistory => _transitionHistory;

    /// <summary>
    /// Обновляет текущее состояние
    /// </summary>
    public void Update()
    {
        _currentState?.Update();
    }

    /// <summary>
    /// Меняет состояние на указанный тип
    /// </summary>
    public void ChangeState<T>() where T : class, IState, new()
    {
        var newState = GetOrCreate<T>();

        if (_currentState == newState)
            return;

        string prevName = _currentState?.GetType().Name ?? "None";
        string newName = typeof(T).Name;

        _currentState?.Exit();
        _currentState = newState;
        _currentState.Enter(this);

        // Записываем в историю
        string record = $"{prevName} → {newName} [{Time.time:F1}s]";
        _transitionHistory.Enqueue(record);

        if (_transitionHistory.Count > MAX_HISTORY)
            _transitionHistory.Dequeue();

        Debug.Log($"[StateMachine] {record}");
    }

    /// <summary>
    /// Проверяет, находимся ли мы в указанном состоянии
    /// </summary>
    public bool IsInState<T>() where T : IState => _currentState is T;

    /// <summary>
    /// Сбрасывает автомат
    /// </summary>
    public void Reset()
    {
        _currentState?.Exit();
        _currentState = null;
        _stateCache.Clear();
        _transitionHistory.Clear();
    }

    private T GetOrCreate<T>() where T : class, IState, new()
    {
        if (!_stateCache.TryGetValue(typeof(T), out var state))
        {
            state = new T();
            _stateCache[typeof(T)] = state;
        }
        return (T)state;
    }
}
```

### Финальная версия PlayerController.cs



```csharp
using System.Collections;
using UnityEngine;

/// <summary>
/// Полноценный контроллер персонажа на основе State Machine
/// </summary>
[RequireComponent(typeof(Rigidbody2D))]
public class PlayerController : MonoBehaviour
{
    // ─── Настройки движения ───────────────────────────────────────────
    [Header("Movement Settings")]
    [SerializeField] private float moveSpeed = 6f;
    [SerializeField] private float jumpForce = 12f;
    [SerializeField] private float airControl = 0.65f;
    [SerializeField] private float groundCheckDistance = 0.1f;
    [SerializeField] private LayerMask groundLayer;

    // ─── Настройки боя ────────────────────────────────────────────────
    [Header("Combat Settings")]
    [SerializeField] private float attackDuration = 0.4f;

    // ─── Отладка ──────────────────────────────────────────────────────
    [Header("Debug")]
    [SerializeField] private bool showDebugGUI = true;
    [SerializeField] private bool showGroundRay = true;

    // ─── Публичные свойства для состояний ────────────────────────────
    public Rigidbody2D Rb           { get; private set; }
    public bool IsGrounded          { get; private set; }
    public float MoveInput          { get; private set; }
    public bool JumpPressed         { get; private set; }
    public bool AttackPressed       { get; private set; }

    public float MoveSpeed          => moveSpeed;
    public float JumpForce          => jumpForce;
    public float AirControl         => airControl;
    public float AttackDuration     => attackDuration;

    // ─── Приватные поля ───────────────────────────────────────────────
    private StateMachine _stateMachine;
    private Collider2D _collider;

    // ─── Unity Lifecycle ──────────────────────────────────────────────

    private void Awake()
    {
        Rb = GetComponent<Rigidbody2D>();
        _collider = GetComponent<Collider2D>();
        _stateMachine = new StateMachine();
    }

    private void Start()
    {
        // Входим в начальное состояние
        _stateMachine.ChangeState<IdleState>();
    }

    private void Update()
    {
        ReadInput();
        CheckGrounded();
        _stateMachine.Update();
    }

    // ─── Ввод ─────────────────────────────────────────────────────────

    private void ReadInput()
    {
        MoveInput    = Input.GetAxis("Horizontal");
        JumpPressed  = Input.GetKeyDown(KeyCode.Space);
        AttackPressed = Input.GetKeyDown(KeyCode.X);
    }

    // ─── Физика ───────────────────────────────────────────────────────

    /// <summary>
    /// Проверяет, стоит ли персонаж на земле через Raycast
    /// </summary>
    private void CheckGrounded()
    {
        Vector2 origin = new Vector2(
            _collider.bounds.center.x,
            _collider.bounds.min.y
        );

        IsGrounded = Physics2D.Raycast(
            origin,
            Vector2.down,
            groundCheckDistance,
            groundLayer
        );
    }

    // ─── Публичные методы для состояний ──────────────────────────────

    public void ChangeState<T>() where T : class, IState, new()
    {
        _stateMachine.ChangeState<T>();
    }

    public bool IsInState<T>() where T : class, IState
    {
        return _stateMachine.IsInState<T>();
    }

    // ─── Отладка ──────────────────────────────────────────────────────

    private void OnDrawGizmos()
    {
        if (!showGroundRay || _collider == null) return;

        Vector2 origin = new Vector2(
            _collider.bounds.center.x,
            _collider.bounds.min.y
        );

        Gizmos.color = IsGrounded ? Color.green : Color.red;
        Gizmos.DrawLine(origin, origin + Vector2.down * groundCheckDistance);
    }

    private void OnGUI()
    {
        if (!showDebugGUI) return;

        // Фон
        GUI.Box(new Rect(8, 8, 220, 150), "");

        GUIStyle style = new GUIStyle(GUI.skin.label) { fontSize = 13 };

        GUI.Label(new Rect(15, 15,  200, 25), $"State:     {_stateMachine.CurrentStateName}", style);
        GUI.Label(new Rect(15, 38,  200, 25), $"Grounded:  {IsGrounded}", style);
        GUI.Label(new Rect(15, 61,  200, 25), $"Velocity:  {Rb.velocity:F1}", style);
        GUI.Label(new Rect(15, 84,  200, 25), $"MoveInput: {MoveInput:F2}", style);

        // История переходов
        GUI.Label(new Rect(15, 110, 200, 20), "— Last transitions —", style);
        int y = 130;
        foreach (var entry in _stateMachine.TransitionHistory)
        {
            GUI.Label(new Rect(15, y, 300, 18), entry, style);
            y += 18;
        }
    }
}
```

### Отладчик StateMachineDebugger.cs



```csharp
using UnityEngine;

/// <summary>
/// Вспомогательный компонент для расширенной отладки State Machine
/// </summary>
public class StateMachineDebugger : MonoBehaviour
{
    [SerializeField] private PlayerController player;
    [SerializeField] private bool logEveryFrame = false;
    [SerializeField] private KeyCode resetKey = KeyCode.R;

    private string _lastStateName = "";

    private void Update()
    {
        if (player == null) return;

        // Логируем только при смене состояния
        string currentName = player.IsInState<IdleState>()   ? "Idle"   :
                             player.IsInState<RunState>()    ? "Run"    :
                             player.IsInState<JumpState>()   ? "Jump"   :
                             player.IsInState<FallState>()   ? "Fall"   :
                             player.IsInState<LandState>()   ? "Land"   :
                             player.IsInState<AttackState>() ? "Attack" :
                             "Unknown";

        if (currentName != _lastStateName)
        {
            Debug.Log($"[Debugger] Состояние изменилось: {_lastStateName} → {currentName} " +
                      $"| Velocity: {player.Rb.velocity:F1} " +
                      $"| Grounded: {player.IsGrounded}");
            _lastStateName = currentName;
        }

        // Принудительный сброс в Idle для тестирования
        if (Input.GetKeyDown(resetKey))
        {
            Debug.Log("[Debugger] Принудительный сброс в IdleState");
            player.ChangeState<IdleState>();
        }

        // Логирование каждый кадр (если включено)
        if (logEveryFrame)
        {
            Debug.Log($"[Frame {Time.frameCount}] State: {currentName} | " +
                      $"Vel: {player.Rb.velocity:F1} | " +
                      $"Input: {player.MoveInput:F2}");
        }
    }
}
```

### Инструкция по настройке в Unity



```csharp
1. Создайте GameObject "Player"
2. Добавьте компоненты:
   - Rigidbody2D (Gravity Scale: 3)
   - BoxCollider2D
   - PlayerController (наш скрипт)
3. Создайте GameObject "Ground":
   - BoxCollider2D
   - Layer: "Ground" (создайте новый слой)
4. В PlayerController укажите:
   - Ground Layer → Ground
   - Ground Check Distance → 0.05
5. Добавьте пустой GameObject "Debugger":
   - StateMachineDebugger
   - Перетащите Player в поле Player
6. Назначьте управление:
   - Горизонталь: A/D или стрелки
   - Прыжок: Space
   - Атака: X
```

---

## 8. Проверь себя {#проверь-себя}

### 📝 Теоретические вопросы

**1. Что такое State Machine и из каких ключевых элементов он состоит?**

<details> <summary>Ответ</summary>

State Machine (конечный автомат) — паттерн проектирования, при котором объект может находиться строго в одном из конечного множества состояний. Ключевые элементы: **State** (состояние — описывает поведение), **Transition** (переход — смена состояния), **Trigger** (триггер — событие, запускающее переход), **Condition** (условие — логическая проверка для перехода).

</details>

---

**2. Почему bool-флаги (`isRunning`, `isJumping`) — плохая практика?**

<details> <summary>Ответ</summary>

Потому что несколько флагов могут одновременно принимать противоречивые значения (`isRunning = true` и `isJumping = true` одновременно). Количество возможных комбинаций растёт экспоненциально: при 4 флагах это уже 16 комбинаций, большинство из которых невалидны. State Machine гарантирует, что объект находится **ровно в одном** состоянии.

</details>

---

**3. В чём разница между методами `Enter()`, `Update()` и `Exit()` в состоянии?**

<details> <summary>Ответ</summary>

- **`Enter()`** — вызывается **один раз** при входе в состояние. Здесь инициализируем: запускаем анимацию, применяем силу прыжка, сбрасываем таймеры.
- **`Update()`** — вызывается **каждый кадр** пока состояние активно. Здесь обрабатываем логику и проверяем условия перехода.
- **`Exit()`** — вызывается **один раз** при выходе. Здесь убираем за собой: останавливаем анимацию, удаляем хитбоксы.

</details>

---

**4. В чём преимущество Class-based State Machine перед Enum-based?**

<details> <summary>Ответ</summary>



</details>
|Критерий|Enum-based|Class-based|
|---|---|---|
|Изоляция логики|❌ В одном классе|✅ Каждое состояние отдельно|
|Переиспользование|❌ Нельзя|✅ Можно для разных объектов|
|Тестирование|❌ Сложно|✅ Легко тестировать состояние изолированно|
|Масштабирование|❌ Switch растёт|✅ Добавляем новый класс|
|Принцип SRP|❌ Нарушен|✅ Соблюдён|
---

### 🔧 Практические задания

**Задание 1 — Лёгкое:** Добавьте состояние `DashState`, в котором персонаж совершает быстрый рывок в направлении движения. Длительность рывка — 0.2 секунды, скорость во время рывка — 3× от обычной. Переход: из `IdleState` или `RunState` по нажатию `LeftShift`.

---

**Задание 2 — Среднее:** Реализуйте `HurtState` — состояние получения урона. Требования:

- Персонаж отлетает назад (knockback)
- Длительность: 0.5 секунды
- Во время урона нельзя двигаться и атаковать
- Переход в `HurtState` возможен из **любого** состояния (кроме `DeathState`)
- Добавьте публичный метод `TakeDamage()` в `PlayerController`

---

**Задание 3 — Сложное:** Реализуйте `CrouchState` — состояние приседания. Требования:

- Переход: зажать `LeftControl` на земле
- В приседании скорость движения снижена до 40%
- Из приседания нельзя прыгать
- Добавьте возможность атаковать из приседания (`CrouchAttackState`)
- При зажатом `LeftControl` в воздухе — ускоренное падение (fast fall)

---

**Задание 4 — Экспертное:** Реализуйте State Machine для **врага** с ИИ:



```csharp
Patrol → Chase → Attack → Stun → Death
```

- **Patrol**: движется между точками патруля
- **Chase**: преследует игрока, если тот в радиусе 5 единиц
- **Attack**: атакует, если игрок в радиусе 1.5 единицы
- **Stun**: временно оглушён после получения урона (1 секунда)
- **Death**: воспроизводит анимацию смерти, затем уничтожает объект

Переиспользуйте ту же систему `IState` / `StateMachine` / `BaseState`.

---

### 🧠 Вопросы для самопроверки

Ответьте на вопросы, не подглядывая в код:

1. Что произойдёт, если вызвать `ChangeState<IdleState>()`, когда мы уже в `IdleState`?
2. Зачем нужен `Dictionary<Type, IState>` в классе `StateMachine`?
3. Почему `Object.FindObjectOfType<PlayerController>()` — не лучший способ получить ссылку на игрока внутри состояния? Как это исправить?
4. Можно ли реализовать **вложенные** State Machine (Hierarchical State Machine)? Где это применяется?
5. Как изменить систему, чтобы один и тот же `JumpState` работал и для игрока, и для врага?

---

### ✅ Чеклист — что должно работать в итоге



```csharp
□ Персонаж стоит на месте в состоянии Idle
□ При нажатии A/D — переход в RunState
□ При отпускании A/D из Run — возврат в Idle
□ При нажатии Space на земле — JumpState
□ Во время прыжка (velocity.y < 0) — FallState
□ После приземления — LandState → Idle/Run
□ При нажатии X — AttackState из любого наземного состояния
□ После атаки — возврат в Idle/Run в зависимости от ввода
□ В консоли виден лог переходов: Idle → Run → Jump → Fall → Land → Idle
□ В GUI отображается текущее состояние
□ Одновременно не активны два состояния
□ Нет ошибок NullReferenceException
```

---

## Итоги

В этой статье мы прошли путь от хаотичных `if/else` до профессиональной архитектуры:

|Этап|Подход|Когда использовать|
|---|---|---|
|**❌ Bool-флаги**|`isRunning`, `isJumping`|Никогда в реальных проектах|
|**⚠️ Enum-based**|`switch(currentState)`|Прототипы, <5 состояний|
|**✅ Class-based**|`IState`, `StateMachine`|Все серьёзные проекты|

**Ключевые принципы State Machine:**

- Объект находится **строго в одном** состоянии в каждый момент времени
- Каждое состояние **изолировано** и отвечает только за себя
- Переходы **явно описаны** и легко отслеживаются
- Система **легко расширяется** без изменения существующего кода

> 💡 **Совет:** В крупных проектах рассмотрите готовые решения — **Animator Controller** в Unity (для анимаций) или пакет [**Unity.StateMachine**](https://github.com/UnityTechnologies/com.unity.statemachine). Но понимание основ, которые мы изучили, обязательно для любого разработчика игр.