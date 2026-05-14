# Unity Physics: Полное руководство от теории к практике

> **Стиль этой статьи** — технический наставник. Я не буду просто перечислять API. Я объясню _почему_ всё работает именно так, задам вопросы, которые заставят вас думать, и дам задачи, которые закрепят знание на уровне мышечной памяти.

---

## Содержание

- [Введение: зачем разработчику знать физику движка глубоко {#введение}](#%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5:%20%D0%B7%D0%B0%D1%87%D0%B5%D0%BC%20%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA%D1%83%20%D0%B7%D0%BD%D0%B0%D1%82%D1%8C%20%D1%84%D0%B8%D0%B7%D0%B8%D0%BA%D1%83%20%D0%B4%D0%B2%D0%B8%D0%B6%D0%BA%D0%B0%20%D0%B3%D0%BB%D1%83%D0%B1%D0%BE%D0%BA%D0%BE%20%7B#%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%7D)
	- [Что даёт глубокое понимание физики движка](#%D0%A7%D1%82%D0%BE%20%D0%B4%D0%B0%D1%91%D1%82%20%D0%B3%D0%BB%D1%83%D0%B1%D0%BE%D0%BA%D0%BE%D0%B5%20%D0%BF%D0%BE%D0%BD%D0%B8%D0%BC%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%84%D0%B8%D0%B7%D0%B8%D0%BA%D0%B8%20%D0%B4%D0%B2%D0%B8%D0%B6%D0%BA%D0%B0)
	- [Три уровня понимания](#%D0%A2%D1%80%D0%B8%20%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F%20%D0%BF%D0%BE%D0%BD%D0%B8%D0%BC%D0%B0%D0%BD%D0%B8%D1%8F)
- [1. Архитектура: PhysX и Box2D под капотом {#архитектура}](#1.%20%D0%90%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D0%B0:%20PhysX%20%D0%B8%20Box2D%20%D0%BF%D0%BE%D0%B4%20%D0%BA%D0%B0%D0%BF%D0%BE%D1%82%D0%BE%D0%BC%20%7B#%D0%B0%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D0%B0%7D)
	- [1.1 Два движка — два мира](#1.1%20%D0%94%D0%B2%D0%B0%20%D0%B4%D0%B2%D0%B8%D0%B6%D0%BA%D0%B0%20%E2%80%94%20%D0%B4%D0%B2%D0%B0%20%D0%BC%D0%B8%D1%80%D0%B0)
	- [1.2 PhysX Pipeline](#1.2%20PhysX%20Pipeline)
	- [1.3 Box2D Pipeline](#1.3%20Box2D%20Pipeline)
	- [1.4 Временная модель: накопитель времени](#1.4%20%D0%92%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C:%20%D0%BD%D0%B0%D0%BA%D0%BE%D0%BF%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%20%D0%B2%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%B8)
- [2. Rigidbody во всех деталях {#rigidbody}](#2.%20Rigidbody%20%D0%B2%D0%BE%20%D0%B2%D1%81%D0%B5%D1%85%20%D0%B4%D0%B5%D1%82%D0%B0%D0%BB%D1%8F%D1%85%20%7B#rigidbody%7D)
	- [2.1 Mass и ForceMode](#2.1%20Mass%20%D0%B8%20ForceMode)
	- [2.2 Drag: сопротивление среды](#2.2%20Drag:%20%D1%81%D0%BE%D0%BF%D1%80%D0%BE%D1%82%D0%B8%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%81%D1%80%D0%B5%D0%B4%D1%8B)
	- [2.3 Constraints: заморозка степеней свободы](#2.3%20Constraints:%20%D0%B7%D0%B0%D0%BC%D0%BE%D1%80%D0%BE%D0%B7%D0%BA%D0%B0%20%D1%81%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D0%B5%D0%B9%20%D1%81%D0%B2%D0%BE%D0%B1%D0%BE%D0%B4%D1%8B)
	- [2.4 Interpolation: плавность без рывков](#2.4%20Interpolation:%20%D0%BF%D0%BB%D0%B0%D0%B2%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%B1%D0%B5%D0%B7%20%D1%80%D1%8B%D0%B2%D0%BA%D0%BE%D0%B2)
	- [2.5 Collision Detection: спектр точности](#2.5%20Collision%20Detection:%20%D1%81%D0%BF%D0%B5%D0%BA%D1%82%D1%80%20%D1%82%D0%BE%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8)
	- [2.6 Rigidbody2D: особенности двумерного тела](#2.6%20Rigidbody2D:%20%D0%BE%D1%81%D0%BE%D0%B1%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D0%B4%D0%B2%D1%83%D0%BC%D0%B5%D1%80%D0%BD%D0%BE%D0%B3%D0%BE%20%D1%82%D0%B5%D0%BB%D0%B0)
- [3. Коллайдеры: геометрия столкновений {#коллайдеры}](#3.%20%D0%9A%D0%BE%D0%BB%D0%BB%D0%B0%D0%B9%D0%B4%D0%B5%D1%80%D1%8B:%20%D0%B3%D0%B5%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%8F%20%D1%81%D1%82%D0%BE%D0%BB%D0%BA%D0%BD%D0%BE%D0%B2%D0%B5%D0%BD%D0%B8%D0%B9%20%7B#%D0%BA%D0%BE%D0%BB%D0%BB%D0%B0%D0%B9%D0%B4%D0%B5%D1%80%D1%8B%7D)
	- [3.1 Иерархия стоимости (от быстрого к медленному)](#3.1%20%D0%98%D0%B5%D1%80%D0%B0%D1%80%D1%85%D0%B8%D1%8F%20%D1%81%D1%82%D0%BE%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D0%B8%20(%D0%BE%D1%82%20%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B3%D0%BE%20%D0%BA%20%D0%BC%D0%B5%D0%B4%D0%BB%D0%B5%D0%BD%D0%BD%D0%BE%D0%BC%D1%83))
	- [3.2 Compound Colliders: составная геометрия](#3.2%20Compound%20Colliders:%20%D1%81%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F%20%D0%B3%D0%B5%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%8F)
	- [3.3 Trigger vs Collider: фундаментальное различие](#3.3%20Trigger%20vs%20Collider:%20%D1%84%D1%83%D0%BD%D0%B4%D0%B0%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5%20%D1%80%D0%B0%D0%B7%D0%BB%D0%B8%D1%87%D0%B8%D0%B5)
- [4. Физические материалы {#физические-материалы}](#4.%20%D0%A4%D0%B8%D0%B7%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%BC%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D1%8B%20%7B#%D1%84%D0%B8%D0%B7%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5-%D0%BC%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D1%8B%7D)
- [5. Слои и Layer Collision Matrix {#слои}](#5.%20%D0%A1%D0%BB%D0%BE%D0%B8%20%D0%B8%20Layer%20Collision%20Matrix%20%7B#%D1%81%D0%BB%D0%BE%D0%B8%7D)
- [6. Физические запросы: Raycast и семья {#физические-запросы}](#6.%20%D0%A4%D0%B8%D0%B7%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D1%8B:%20Raycast%20%D0%B8%20%D1%81%D0%B5%D0%BC%D1%8C%D1%8F%20%7B#%D1%84%D0%B8%D0%B7%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5-%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D1%8B%7D)
	- [6.1 Семейство 3D запросов](#6.1%20%D0%A1%D0%B5%D0%BC%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%BE%203D%20%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D0%BE%D0%B2)
	- [6.2 Семейство 2D запросов](#6.2%20%D0%A1%D0%B5%D0%BC%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%BE%202D%20%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D0%BE%D0%B2)
- [7. FixedUpdate vs Update: почему это важно {#fixedupdate}](#7.%20FixedUpdate%20vs%20Update:%20%D0%BF%D0%BE%D1%87%D0%B5%D0%BC%D1%83%20%D1%8D%D1%82%D0%BE%20%D0%B2%D0%B0%D0%B6%D0%BD%D0%BE%20%7B#fixedupdate%7D)
	- [7.1 Детерминизм и стабильность](#7.1%20%D0%94%D0%B5%D1%82%D0%B5%D1%80%D0%BC%D0%B8%D0%BD%D0%B8%D0%B7%D0%BC%20%D0%B8%20%D1%81%D1%82%D0%B0%D0%B1%D0%B8%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C)
	- [7.2 Правила работы с Transform и Rigidbody](#7.2%20%D0%9F%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B%20%D1%81%20Transform%20%D0%B8%20Rigidbody)
- [8. Joints: суставы и ограничения {#joints}](#8.%20Joints:%20%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B2%D1%8B%20%D0%B8%20%D0%BE%D0%B3%D1%80%D0%B0%D0%BD%D0%B8%D1%87%D0%B5%D0%BD%D0%B8%D1%8F%20%7B#joints%7D)
	- [8.1 HingeJoint: вращение вокруг оси](#8.1%20HingeJoint:%20%D0%B2%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%D0%BE%D0%BA%D1%80%D1%83%D0%B3%20%D0%BE%D1%81%D0%B8)
	- [8.2 SpringJoint: пружинное соединение](#8.2%20SpringJoint:%20%D0%BF%D1%80%D1%83%D0%B6%D0%B8%D0%BD%D0%BD%D0%BE%D0%B5%20%D1%81%D0%BE%D0%B5%D0%B4%D0%B8%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5)
	- [8.3 ConfigurableJoint: полный контроль](#8.3%20ConfigurableJoint:%20%D0%BF%D0%BE%D0%BB%D0%BD%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C)
- [9. Оптимизация физической симуляции {#оптимизация}](#9.%20%D0%9E%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D1%84%D0%B8%D0%B7%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B9%20%D1%81%D0%B8%D0%BC%D1%83%D0%BB%D1%8F%D1%86%D0%B8%D0%B8%20%7B#%D0%BE%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%7D)
	- [9.1 Sleeping: экономия на неподвижных объектах](#9.1%20Sleeping:%20%D1%8D%D0%BA%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%8F%20%D0%BD%D0%B0%20%D0%BD%D0%B5%D0%BF%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%BD%D1%8B%D1%85%20%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%B0%D1%85)
	- [9.2 Physics Settings: ключевые параметры](#9.2%20Physics%20Settings:%20%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%B2%D1%8B%D0%B5%20%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B)
	- [9.3 Оптимизация коллайдеров](#9.3%20%D0%9E%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%BA%D0%BE%D0%BB%D0%BB%D0%B0%D0%B9%D0%B4%D0%B5%D1%80%D0%BE%D0%B2)
- [10. Подводные камни {#подводные-камни}](#10.%20%D0%9F%D0%BE%D0%B4%D0%B2%D0%BE%D0%B4%D0%BD%D1%8B%D0%B5%20%D0%BA%D0%B0%D0%BC%D0%BD%D0%B8%20%7B#%D0%BF%D0%BE%D0%B4%D0%B2%D0%BE%D0%B4%D0%BD%D1%8B%D0%B5-%D0%BA%D0%B0%D0%BC%D0%BD%D0%B8%7D)
	- [10.1 Tunneling: прохождение сквозь](#10.1%20Tunneling:%20%D0%BF%D1%80%D0%BE%D1%85%D0%BE%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%81%D0%BA%D0%B2%D0%BE%D0%B7%D1%8C)
	- [10.2 Jitter: дрожание объектов](#10.2%20Jitter:%20%D0%B4%D1%80%D0%BE%D0%B6%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BE%D0%B2)
	- [10.3 Масштаб сцены](#10.3%20%D0%9C%D0%B0%D1%81%D1%88%D1%82%D0%B0%D0%B1%20%D1%81%D1%86%D0%B5%D0%BD%D1%8B)
	- [10.4 Прочие ловушки](#10.4%20%D0%9F%D1%80%D0%BE%D1%87%D0%B8%D0%B5%20%D0%BB%D0%BE%D0%B2%D1%83%D1%88%D0%BA%D0%B8)
- [11. 2D vs 3D: полное сравнение {#сравнение}](#11.%202D%20vs%203D:%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D0%B5%20%D1%81%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%20%7B#%D1%81%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%7D)
	- [Ключевые отличия в коде](#%D0%9A%D0%BB%D1%8E%D1%87%D0%B5%D0%B2%D1%8B%D0%B5%20%D0%BE%D1%82%D0%BB%D0%B8%D1%87%D0%B8%D1%8F%20%D0%B2%20%D0%BA%D0%BE%D0%B4%D0%B5)
- [12. Практические задания {#практика}](#12.%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F%20%7B#%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0%7D)
	- [🟢 Задание 1 (Базовый): Физический персонаж](#%F0%9F%9F%A2%20%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%201%20(%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B9):%20%D0%A4%D0%B8%D0%B7%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BF%D0%B5%D1%80%D1%81%D0%BE%D0%BD%D0%B0%D0%B6)
		- [Условие](#%D0%A3%D1%81%D0%BB%D0%BE%D0%B2%D0%B8%D0%B5)
		- [Стартовый скелет](#%D0%A1%D1%82%D0%B0%D1%80%D1%82%D0%BE%D0%B2%D1%8B%D0%B9%20%D1%81%D0%BA%D0%B5%D0%BB%D0%B5%D1%82)
		- [Ожидаемое поведение](#%D0%9E%D0%B6%D0%B8%D0%B4%D0%B0%D0%B5%D0%BC%D0%BE%D0%B5%20%D0%BF%D0%BE%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5)
		- [Критерии оценки](#%D0%9A%D1%80%D0%B8%D1%82%D0%B5%D1%80%D0%B8%D0%B8%20%D0%BE%D1%86%D0%B5%D0%BD%D0%BA%D0%B8)
		- [Типичные ошибки](#%D0%A2%D0%B8%D0%BF%D0%B8%D1%87%D0%BD%D1%8B%D0%B5%20%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D0%B8)
	- [🟡 Задание 2 (Средний): Система стрельбы](#%F0%9F%9F%A1%20%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%202%20(%D0%A1%D1%80%D0%B5%D0%B4%D0%BD%D0%B8%D0%B9):%20%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D1%81%D1%82%D1%80%D0%B5%D0%BB%D1%8C%D0%B1%D1%8B)
		- [Условие](#%D0%A3%D1%81%D0%BB%D0%BE%D0%B2%D0%B8%D0%B5)
		- [Стартовый скелет](#%D0%A1%D1%82%D0%B0%D1%80%D1%82%D0%BE%D0%B2%D1%8B%D0%B9%20%D1%81%D0%BA%D0%B5%D0%BB%D0%B5%D1%82)
		- [Ожидаемое поведение](#%D0%9E%D0%B6%D0%B8%D0%B4%D0%B0%D0%B5%D0%BC%D0%BE%D0%B5%20%D0%BF%D0%BE%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5)
		- [Критерии оценки](#%D0%9A%D1%80%D0%B8%D1%82%D0%B5%D1%80%D0%B8%D0%B8%20%D0%BE%D1%86%D0%B5%D0%BD%D0%BA%D0%B8)
		- [Сравнительный анализ: Projectile vs Hitscan](#%D0%A1%D1%80%D0%B0%D0%B2%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7:%20Projectile%20vs%20Hitscan)
	- [🔴 Задание 3 (Продвинутый): Разрушаемый мост](#%F0%9F%94%B4%20%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%203%20(%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%BD%D1%83%D1%82%D1%8B%D0%B9):%20%D0%A0%D0%B0%D0%B7%D1%80%D1%83%D1%88%D0%B0%D0%B5%D0%BC%D1%8B%D0%B9%20%D0%BC%D0%BE%D1%81%D1%82)
		- [Условие](#%D0%A3%D1%81%D0%BB%D0%BE%D0%B2%D0%B8%D0%B5)
		- [Стартовый скелет](#%D0%A1%D1%82%D0%B0%D1%80%D1%82%D0%BE%D0%B2%D1%8B%D0%B9%20%D1%81%D0%BA%D0%B5%D0%BB%D0%B5%D1%82)
		- [Ожидаемое поведение](#%D0%9E%D0%B6%D0%B8%D0%B4%D0%B0%D0%B5%D0%BC%D0%BE%D0%B5%20%D0%BF%D0%BE%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5)
		- [Критерии оценки](#%D0%9A%D1%80%D0%B8%D1%82%D0%B5%D1%80%D0%B8%D0%B8%20%D0%BE%D1%86%D0%B5%D0%BD%D0%BA%D0%B8)
		- [Типичные ошибки в задании 3](#%D0%A2%D0%B8%D0%BF%D0%B8%D1%87%D0%BD%D1%8B%D0%B5%20%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D0%B8%20%D0%B2%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B8%203)
- [13. Чеклист компетенций {#чеклист}](#13.%20%D0%A7%D0%B5%D0%BA%D0%BB%D0%B8%D1%81%D1%82%20%D0%BA%D0%BE%D0%BC%D0%BF%D0%B5%D1%82%D0%B5%D0%BD%D1%86%D0%B8%D0%B9%20%7B#%D1%87%D0%B5%D0%BA%D0%BB%D0%B8%D1%81%D1%82%7D)
	- [Уровень 1: Основы (Junior)](#%D0%A3%D1%80%D0%BE%D0%B2%D0%B5%D0%BD%D1%8C%201:%20%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B%20(Junior))
	- [Уровень 2: Уверенный разработчик (Middle)](#%D0%A3%D1%80%D0%BE%D0%B2%D0%B5%D0%BD%D1%8C%202:%20%D0%A3%D0%B2%D0%B5%D1%80%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9%20%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA%20(Middle))
	- [Уровень 3: Эксперт (Senior)](#%D0%A3%D1%80%D0%BE%D0%B2%D0%B5%D0%BD%D1%8C%203:%20%D0%AD%D0%BA%D1%81%D0%BF%D0%B5%D1%80%D1%82%20(Senior))
	- [Чеклист перед релизом](#%D0%A7%D0%B5%D0%BA%D0%BB%D0%B8%D1%81%D1%82%20%D0%BF%D0%B5%D1%80%D0%B5%D0%B4%20%D1%80%D0%B5%D0%BB%D0%B8%D0%B7%D0%BE%D0%BC)


## Введение: зачем разработчику знать физику движка глубоко {#введение}

Представьте два сценария разработки.

**Сценарий А.** Персонаж начинает дрожать на ровной поверхности. Разработчик открывает Inspector и начинает наугад крутить параметры: `drag`, `mass`, `bounciness`. Через час случайного эксперимента дрожание уменьшилось, но не исчезло. Разработчик добавляет хак — принудительно обнуляет скорость если она меньше порога. Баг "исправлен".

**Сценарий Б.** Персонаж начинает дрожать. Разработчик видит: `bounciness > 0` на материале земли + `Contact Offset` слишком большой + `Solver Iterations` недостаточно для стека объектов. Три точечных изменения — баг устранён за пять минут, без хаков, с пониманием причины.

Разница между этими разработчиками — не опыт в годах. Разница в том, понимают ли они **что физический движок делает каждый кадр**.

### Что даёт глубокое понимание физики движка



```csharp
Поверхностное знание        Глубокое знание
─────────────────────       ─────────────────────────────────────
"Добавь Rigidbody"          "Понимаю mass, drag, constraints,
                             interpolation и их взаимодействие"

"Используй Raycast"         "Знаю Broad/Narrow Phase, выбираю
                             правильный тип запроса и NonAlloc"

"Физика в FixedUpdate"      "Понимаю fixed timestep, накопитель
                             времени и детерминизм симуляции"

"Оптимизируй коллайдеры"    "Знаю sleeping, culling, Layer Matrix
                             и стоимость каждого типа коллайдера"
```

### Три уровня понимания

Эта статья проведёт вас через три уровня:

- **Механика** — что делает каждый параметр и API
- **Архитектура** — как компоненты взаимодействуют внутри движка
- **Применение** — как проектировать системы, которые работают _с_ физикой, а не против неё

Мы начнём с самого фундаментального вопроса.

---

## 1. Архитектура: PhysX и Box2D под капотом {#архитектура}

### 1.1 Два движка — два мира

Unity использует два принципиально разных физических движка:

||3D Physics|2D Physics|
|---|---|---|
|**Движок**|NVIDIA PhysX|Box2D (Erin Catto)|
|**API**|`Physics.*`|`Physics2D.*`|
|**Компонент**|`Rigidbody`|`Rigidbody2D`|
|**Изоляция**|Полная — 3D и 2D не взаимодействуют||

Это не "3D версия" и "2D версия" одного движка. Это принципиально разные системы. Объект с `Rigidbody` и объект с `Rigidbody2D` **никогда не будут физически взаимодействовать**, даже если их коллайдеры визуально перекрываются.



```csharp
// Это работает визуально, но НЕ физически
var obj3d = new GameObject();
obj3d.AddComponent<Rigidbody>();      // 3D физика
obj3d.AddComponent<BoxCollider>();

var obj2d = new GameObject();
obj2d.AddComponent<Rigidbody2D>();    // 2D физика — другой мир
obj2d.AddComponent<BoxCollider2D>();

// Эти два объекта НИКОГДА не столкнутся
```

### 1.2 PhysX Pipeline

Каждый физический шаг PhysX проходит через строгий конвейер:



```csharp
┌──────────────────────────────────────────────────────────────────┐
│                    ОДИН ФИЗИЧЕСКИЙ ШАГ (0.02s)                    │
├─────────────┬──────────────┬───────────────┬──────────────────────┤
│ Broad Phase │ Narrow Phase │    Solver     │     Integration      │
│             │              │               │                      │
│ SAP алгоритм│ GJK + EPA   │ Constraint    │ Semi-implicit Euler  │
│ Найти пары  │ Точные точки │ solver        │ Обновить позиции     │
│ за O(n logn)│ контакта     │ 6 итераций    │ и скорости           │
└─────────────┴──────────────┴───────────────┴──────────────────────┘
```

**Broad Phase** — грубый фильтр. Алгоритм Sweep and Prune (SAP) сортирует объекты вдоль осей координат и находит пары с пересекающимися AABB. Из N²/2 возможных пар отбирает только кандидатов — за O(n log n).

**Narrow Phase** — точная проверка кандидатов. Алгоритм GJK (Gilbert-Johnson-Keerthi) определяет пересечение выпуклых тел. EPA (Expanding Polytope Algorithm) извлекает глубину проникновения и нормаль.

**Solver** — итеративный решатель ограничений методом PGS (Projected Gauss-Seidel). Применяет импульсы для разрешения столкновений и удовлетворения joint constraints. 6 итераций по умолчанию — компромисс между точностью и производительностью.

**Integration** — обновление состояния всех тел. Unity использует **semi-implicit Euler** (симплектический метод):



```csharp
// Явный Эйлер (нестабильный):
pos(t+dt) = pos(t) + vel(t) * dt

// Semi-implicit Euler (Unity, стабильный):
vel(t+dt) = vel(t) + acc(t) * dt   // Сначала скорость
pos(t+dt) = pos(t) + vel(t+dt) * dt // Затем позиция с НОВОЙ скоростью
```

Разница кажется небольшой, но semi-implicit метод лучше сохраняет энергию системы — объекты не "взрываются" со временем.

### 1.3 Box2D Pipeline

Box2D проще по архитектуре, но не менее эффективен:

**Dynamic Tree** вместо SAP для Broad Phase — самобалансирующееся дерево AABB, которое эффективнее при большом количестве движущихся объектов.

**Sequential Impulses** вместо PGS для решателя — итеративный метод, каждое ограничение решается последовательно. Проще в реализации, достаточно стабилен для игр.

**Warm Starting** — использование решений предыдущего кадра как начального приближения. Box2D "помнит" контакты между кадрами, что значительно ускоряет сходимость решателя.

### 1.4 Временная модель: накопитель времени

Понимание этой модели — ключ ко всем вопросам "почему в FixedUpdate":



```csharp
// Псевдокод Unity Game Loop (упрощённо)
void UnityGameLoop()
{
    float physicsAccumulator = 0f;

    while (gameIsRunning)
    {
        // Реальное время между кадрами — всегда разное
        float realFrameTime = MeasureTimeSinceLastFrame();
        // Time.deltaTime = realFrameTime

        // Накапливаем время
        physicsAccumulator += realFrameTime;

        // Защита от "спирали смерти":
        // если игра тормозит — не пытаемся бесконечно догонять
        physicsAccumulator = Mathf.Min(
            physicsAccumulator,
            Time.maximumDeltaTime  // По умолчанию 0.1333s
        );

        // Выполняем физику фиксированными шагами
        while (physicsAccumulator >= Time.fixedDeltaTime)
        {
            // Ваш код физики
            CallFixedUpdateOnAllMonoBehaviours();

            // Шаг физического движка
            Physics.Simulate(Time.fixedDeltaTime);

            // Коллбэки столкновений
            DispatchCollisionCallbacks();

            physicsAccumulator -= Time.fixedDeltaTime;
        }

        // Ваш неффизический код
        CallUpdateOnAllMonoBehaviours();
        CallLateUpdate();

        // Рендеринг
        Render();
    }
}
```

Из этой схемы следует несколько важных выводов:

1. `FixedUpdate` может вызываться **0, 1 или несколько раз** за один `Update`
2. При низком FPS физика делает **несколько шагов подряд** — поэтому нельзя читать `GetKeyDown` в `FixedUpdate` (нажатие может пропасть или задублироваться)
3. `Time.fixedDeltaTime` — **константа**, `Time.deltaTime` — переменная

> **🤔 Проверь себя #1**
> 
> Если `Time.fixedDeltaTime = 0.02s` и игра работает на 20 FPS (кадр = 0.05s), сколько раз вызовется `FixedUpdate` за один `Update`? А если FPS вырос до 120 (кадр = 0.0083s)?

<details> <summary>Ответ и объяснение</summary>

**При 20 FPS:** За кадр накапливается 0.05s. Делим: 0.05 / 0.02 = 2.5, значит `FixedUpdate` вызовется **2 раза** (0.05 остаток 0.01 переходит на следующий кадр).

**При 120 FPS:** За кадр накапливается 0.0083s. Это меньше 0.02s, значит `FixedUpdate` вызовется **0 раз**. Физика шагнёт только когда накопится ≥ 0.02s — примерно раз в 2-3 кадра рендеринга.

**Практический вывод:** `GetKeyDown` в `FixedUpdate` ненадёжен — при высоком FPS FixedUpdate вызывается реже Update и может пропустить нажатие. Всегда читайте ввод в `Update`, сохраняйте в поле, применяйте в `FixedUpdate`.

</details>

---

## 2. Rigidbody во всех деталях {#rigidbody}

`Rigidbody` — это контракт с физическим движком: "управляй этим объектом ты, а не я через `transform`". Каждый параметр влияет на то, как движок симулирует тело.

### 2.1 Mass и ForceMode

Mass — инертная масса. Определяет сопротивление ускорению по второму закону Ньютона: `F = ma`, следовательно `a = F/m`.

Единицы не привязаны к реальным килограммам — важны _соотношения_:



```csharp
// Эти две конфигурации физически эквивалентны:
// Конфигурация А: mass=1f, force=10f → a = 10 m/s²
// Конфигурация Б: mass=10f, force=100f → a = 10 m/s²

// Важны соотношения масс при СТОЛКНОВЕНИЯХ:
// Грузовик (mass=100) vs Мяч (mass=1) — мяч отлетает далеко, грузовик почти не останавливается
```

`ForceMode` определяет _как именно_ сила применяется:



```csharp
public class ForceModeGuide : MonoBehaviour
{
    private Rigidbody rb;

    void Start()
    {
        rb = GetComponent<Rigidbody>();
        rb.mass = 2f;
    }

    void ApplyForces()
    {
        // ────────────────────────────────────────────────────
        // ForceMode.Force
        // Непрерывная сила. Зависит от mass и fixedDeltaTime.
        // Δv = (F / mass) * fixedDeltaTime
        // При mass=2, F=10, dt=0.02: Δv = (10/2)*0.02 = 0.1 m/s за шаг
        // Используйте: двигатели, ветер, гравитация
        // ────────────────────────────────────────────────────
        rb.AddForce(Vector3.forward * 10f, ForceMode.Force);

        // ────────────────────────────────────────────────────
        // ForceMode.Acceleration
        // Непрерывная сила. НЕ зависит от mass.
        // Δv = F * fixedDeltaTime
        // Все объекты ускоряются одинаково — как реальная гравитация
        // Используйте: зоны изменённой гравитации, планетарное притяжение
        // ────────────────────────────────────────────────────
        rb.AddForce(Vector3.up * 9.81f, ForceMode.Acceleration);

        // ────────────────────────────────────────────────────
        // ForceMode.Impulse
        // Мгновенный импульс. Зависит от mass.
        // Δv = F / mass
        // При mass=2, F=10: Δv = 5 m/s мгновенно
        // Используйте: взрывы, прыжки, удары
        // ────────────────────────────────────────────────────
        rb.AddForce(Vector3.up * 10f, ForceMode.Impulse);

        // ────────────────────────────────────────────────────
        // ForceMode.VelocityChange
        // Мгновенный импульс. НЕ зависит от mass.
        // Δv = F (прямое изменение скорости)
        // Используйте: телепортация скорости, точный контроль движения
        // ────────────────────────────────────────────────────
        rb.AddForce(Vector3.forward * 5f, ForceMode.VelocityChange);
    }
}
```

### 2.2 Drag: сопротивление среды



```csharp
public class DragConfigurations : MonoBehaviour
{
    /*
    Формула линейного drag:
    velocity *= (1 - drag * fixedDeltaTime)

    При drag=1, fixedDeltaTime=0.02:
    velocity *= (1 - 1 * 0.02) = velocity * 0.98 (потеря 2% скорости за шаг)

    Скорость убывает экспоненциально — никогда не достигает нуля
    */

    void SetupDrag()
    {
        var rb = GetComponent<Rigidbody>();

        // Различные среды:
        rb.linearDamping  = 0f;    // Вакуум — движение без потерь
        rb.linearDamping  = 0.01f; // Снаряд в воздухе — минимальное сопротивление
        rb.linearDamping  = 1f;    // Обычный объект в воздухе
        rb.linearDamping  = 3f;    // Объект в воде
        rb.linearDamping  = 10f;   // Очень вязкая среда

        rb.angularDamping = 0.05f; // По умолчанию — небольшое затухание вращения
        rb.angularDamping = 0f;    // Вечное вращение (как в космосе)
        rb.angularDamping = 5f;    // Быстрое затухание вращения

        // Примечание: Unity 6+ использует linearDamping и angularDamping
        // Unity < 6 использует drag и angularDrag
    }
}
```

### 2.3 Constraints: заморозка степеней свободы

Твёрдое тело в 3D имеет 6 степеней свободы: 3 позиции (X, Y, Z) и 3 вращения. `RigidbodyConstraints` — это битовая маска для их заморозки:



```csharp
public class ConstraintsPatterns : MonoBehaviour
{
    void Start()
    {
        var rb = GetComponent<Rigidbody>();

        // Паттерн: 3D персонаж — движется, но не переворачивается
        rb.constraints = RigidbodyConstraints.FreezeRotation;

        // Паттерн: 2.5D платформер — движение только по X и Y
        rb.constraints = RigidbodyConstraints.FreezePositionZ |
                         RigidbodyConstraints.FreezeRotationX |
                         RigidbodyConstraints.FreezeRotationY;

        // Паттерн: Объект на рельсах — только движение по Z
        rb.constraints = RigidbodyConstraints.FreezePositionX |
                         RigidbodyConstraints.FreezePositionY |
                         RigidbodyConstraints.FreezeRotation;

        // Полная заморозка (аналог isKinematic, но constraints быстрее)
        rb.constraints = RigidbodyConstraints.FreezeAll;

        // Сброс
        rb.constraints = RigidbodyConstraints.None;
    }
}
```

### 2.4 Interpolation: плавность без рывков



```csharp
Проблема (без интерполяции):

Физика (50Hz):   [P0]────────[P1]────────[P2]────────[P3]
                 0ms         20ms        40ms        60ms

Рендер (75Hz):  [R0]──[R1]──[R2]──[R3]──[R4]──[R5]──[R6]
                0ms  13ms  26ms  40ms  53ms  66ms  80ms

R0,R1 → P0 (правильно)
R2 → P0 (устаревшие данные!)
R3 → P1 (рывок на экране)

Решение (Interpolate):
R2 показывает 30% пути от P0 к P1 — плавное движение
```



```csharp
public class InterpolationSetup : MonoBehaviour
{
    void Configure()
    {
        var rb = GetComponent<Rigidbody>();

        // Interpolate: позиция интерполируется между предыдущим и текущим
        // физическим шагом. Задержка 1 физический кадр (20ms при 50Hz)
        // ИСПОЛЬЗУЙТЕ для: игрока, объектов с камерой, важных визуальных объектов
        rb.interpolation = RigidbodyInterpolation.Interpolate;

        // Extrapolate: предсказывает СЛЕДУЮЩУЮ позицию на основе скорости
        // Нет задержки, но артефакты при резких изменениях (столкновения)
        // ИСПОЛЬЗУЙТЕ для: сетевых объектов, удалённых игроков
        rb.interpolation = RigidbodyInterpolation.Extrapolate;

        // None: позиция напрямую из последнего физического шага
        // ИСПОЛЬЗУЙТЕ для: статичных объектов, FPS совпадает с Physics Rate
        rb.interpolation = RigidbodyInterpolation.None;
    }
}
```

### 2.5 Collision Detection: спектр точности



```csharp
public class CollisionDetectionGuide : MonoBehaviour
{
    void SelectMode()
    {
        var rb = GetComponent<Rigidbody>();

        // Discrete ─── дешевле всех ──────────────────────────────────────
        // Проверяет только в дискретные моменты (каждый fixedDeltaTime)
        // Риск tunneling: v_max = коллайдер_размер / fixedDeltaTime
        // Для BoxCollider 1m и dt=0.02: v_max = 50 m/s (безопасно для большинства)
        rb.collisionDetectionMode = CollisionDetectionMode.Discrete;

        // Continuous ──────────────────────────────────────────────────────
        // CCD этот объект → статические коллайдеры
        // Swept volume: "размазывает" коллайдер вдоль траектории
        // В 2-4 раза дороже Discrete
        rb.collisionDetectionMode = CollisionDetectionMode.Continuous;

        // ContinuousDynamic ───────────────────────────────────────────────
        // CCD этот объект → все Rigidbody + статика
        // Самый надёжный, самый дорогой
        // ТОЛЬКО для критичных объектов (игрок, важные снаряды)
        rb.collisionDetectionMode = CollisionDetectionMode.ContinuousDynamic;

        // ContinuousSpeculative ── хороший баланс ─────────────────────────
        // Расширяет AABB на предполагаемое движение
        // Быстрее ContinuousDynamic, иногда даёт ghost collisions
        rb.collisionDetectionMode = CollisionDetectionMode.ContinuousSpeculative;
    }
}
```

### 2.6 Rigidbody2D: особенности двумерного тела



```csharp
public class Rigidbody2DGuide : MonoBehaviour
{
    void Configure()
    {
        var rb = GetComponent<Rigidbody2D>();

        // Body Type — ключевое отличие от 3D
        rb.bodyType = RigidbodyType2D.Dynamic;    // Полная физика
        rb.bodyType = RigidbodyType2D.Kinematic;  // Управляется кодом
        rb.bodyType = RigidbodyType2D.Static;     // Не движется

        // В 2D вращение — только Z-ось, в градусах
        rb.rotation = 45f;
        rb.angularVelocity = 90f; // Градусов в секунду

        // GravityScale — масштаб гравитации для этого объекта
        rb.gravityScale = 1f;   // Нормальная гравитация
        rb.gravityScale = 0f;   // Топдаун игра — гравитации нет
        rb.gravityScale = 2f;   // "Тяжёлый" объект
        rb.gravityScale = -1f;  // Антигравитация

        // Правильное движение кинематических тел
        rb.bodyType = RigidbodyType2D.Kinematic;
        // В FixedUpdate:
        rb.MovePosition(rb.position + Vector2.right * 5f * Time.fixedDeltaTime);
        rb.MoveRotation(rb.rotation + 90f * Time.fixedDeltaTime);
    }
}
```

> **🤔 Проверь себя #2**
> 
> У вас снаряд со скоростью 50 м/с и размером коллайдера 0.1 м. `fixedDeltaTime = 0.02s`. Какой режим Collision Detection нужен? Посчитайте критическую скорость.

<details> <summary>Ответ и объяснение</summary>

**Критическая скорость** = размер / fixedDeltaTime = 0.1 / 0.02 = **5 м/с**.

Скорость снаряда (50 м/с) в 10 раз превышает критическую — Discrete режим гарантированно даст tunneling.

Нужно: `ContinuousSpeculative` (баланс цены и надёжности) или `ContinuousDynamic` (максимальная надёжность для критически важного объекта). Также стоит установить `rb.maxLinearVelocity = 100f` как дополнительный предохранитель.

</details>

---

## 3. Коллайдеры: геометрия столкновений {#коллайдеры}

Коллайдер — это не визуальная модель. Это упрощённая геометрическая форма, которую физический движок использует для обнаружения столкновений. Правило первое: **коллайдер должен быть настолько прост, насколько это допустимо геймплеем**.

### 3.1 Иерархия стоимости (от быстрого к медленному)



```csharp
3D: Sphere < Capsule < Box < Convex Mesh << Concave Mesh
2D: Circle < Capsule < Box < Polygon     << Edge (complex)
```



```csharp
public class ColliderTypesGuide : MonoBehaviour
{
    void Setup3DColliders()
    {
        // SphereCollider ─────────────────────────────────────────────────
        // Проверка: dist(centers) < r1 + r2  — O(1), математически идеален
        // Применение: снаряды, персонажи (грубо), зоны обнаружения
        var sphere = gameObject.AddComponent<SphereCollider>();
        sphere.radius = 1f;
        sphere.center = Vector3.zero;

        // CapsuleCollider ─────────────────────────────────────────────────
        // Два полусфера + цилиндр. Идеален для персонажей:
        // - Устойчив на неровных поверхностях
        // - Не застревает в углах
        // - Хорошо скользит по препятствиям
        var capsule = gameObject.AddComponent<CapsuleCollider>();
        capsule.radius = 0.5f;
        capsule.height = 2f;
        capsule.direction = 1; // 0=X, 1=Y (вертикаль), 2=Z

        // BoxCollider ─────────────────────────────────────────────────────
        // OBB (Oriented Bounding Box). Точен для прямоугольных объектов.
        // Применение: ящики, стены, платформы, транспорт
        var box = gameObject.AddComponent<BoxCollider>();
        box.size   = new Vector3(1f, 1f, 1f);
        box.center = Vector3.zero;

        // MeshCollider ─────────────────────────────────────────────────────
        // Точный, но ДОРОГОЙ. Concave (вогнутый) — только для статики!
        // Convex: работает с Rigidbody, макс. 255 полигонов, только выпуклые
        var mesh = gameObject.AddComponent<MeshCollider>();
        mesh.sharedMesh = GetComponent<MeshFilter>().sharedMesh;
        mesh.convex     = true;  // Обязательно для динамических объектов!
    }

    void Setup2DColliders()
    {
        // CircleCollider2D — аналог Sphere
        var circle = gameObject.AddComponent<CircleCollider2D>();
        circle.radius = 0.5f;

        // BoxCollider2D
        var box2d = gameObject.AddComponent<BoxCollider2D>();
        box2d.size       = new Vector2(1f, 1f);
        box2d.edgeRadius = 0.02f; // Скруглённые углы → меньше jitter!

        // EdgeCollider2D — линия без заполнения
        // Идеал для: поверхностей уровня, платформ, рельефа
        var edge = gameObject.AddComponent<EdgeCollider2D>();
        edge.points = new Vector2[]
        {
            new Vector2(-5f, 0f),
            new Vector2(-2f, 1f),
            new Vector2(2f,  1f),
            new Vector2(5f,  0f)
        };

        // PolygonCollider2D — замкнутый полигон
        var polygon = gameObject.AddComponent<PolygonCollider2D>();
        polygon.SetPath(0, new Vector2[]
        {
            new Vector2(-1f, 0f),
            new Vector2(0f,  1f),
            new Vector2(1f,  0f)
        });
    }
}
```

### 3.2 Compound Colliders: составная геометрия

Один из самых мощных паттернов: несколько простых коллайдеров на дочерних объектах образуют одно физическое тело через родительский `Rigidbody`:



```csharp
/*
Иерархия:
Car (Rigidbody) ← единое физическое тело
├── Body_Collider    (BoxCollider)     — корпус
├── Roof_Collider    (BoxCollider)     — крыша
└── Wheel_FL_Collider (SphereCollider) — колесо
└── Wheel_FR_Collider (SphereCollider)
└── Wheel_RL_Collider (SphereCollider)
└── Wheel_RR_Collider (SphereCollider)
*/

public class CompoundColliderBuilder : MonoBehaviour
{
    [ConMenu("Build Car Compound Collider")]
    void BuildCarColliders()
    {
        // Корпус — вытянутый ящик
        var body = CreateChildCollider("Body");
        var bodyBox = body.AddComponent<BoxCollider>();
        bodyBox.size   = new Vector3(2f, 0.5f, 4f);
        body.transform.localPosition = new Vector3(0f, 0.5f, 0f);

        // Крыша — меньший ящик
        var roof = CreateChildCollider("Roof");
        var roofBox = roof.AddComponent<BoxCollider>();
        roofBox.size   = new Vector3(1.5f, 0.4f, 2f);
        roof.transform.localPosition = new Vector3(0f, 1.1f, 0.3f);

        // Колёса — сферы
        AddWheel("Wheel_FL", new Vector3(-1f, 0f,  1.5f));
        AddWheel("Wheel_FR", new Vector3( 1f, 0f,  1.5f));
        AddWheel("Wheel_RL", new Vector3(-1f, 0f, -1.5f));
        AddWheel("Wheel_RR", new Vector3( 1f, 0f, -1.5f));
    }

    GameObject CreateChildCollider(string childName)
    {
        var child = new GameObject(childName + "_Collider");
        child.transform.SetParent(transform);
        child.transform.localPosition = Vector3.zero;
        child.transform.localRotation = Quaternion.identity;
        child.transform.localScale    = Vector3.one;
        return child;
    }

    void AddWheel(string wheelName, Vector3 localPos)
    {
        var wheel = CreateChildCollider(wheelName);
        var col = wheel.AddComponent<SphereCollider>();
        col.radius = 0.35f;
        wheel.transform.localPosition = localPos;
    }
}
```

### 3.3 Trigger vs Collider: фундаментальное различие



```csharp
/*
Collider (isTrigger = false): создаёт физическое препятствие
Trigger  (isTrigger = true):  только обнаруживает присутствие

Таблица вызова событий:
────────────────────────────────────────────────────────────────────
Объект A              Объект B              Событие
────────────────────────────────────────────────────────────────────
Static Collider     + Static Collider     = НЕТ (оба статичны)
Static Collider     + Rigidbody Collider = OnCollision*
Static Trigger      + Rigidbody Collider = OnTrigger*
Rigidbody Trigger   + Rigidbody Collider = OnTrigger*
Rigidbody Trigger   + Kinematic Rb       = OnTrigger*
Kinematic           + Kinematic           = НЕТ (без isTrigger)
────────────────────────────────────────────────────────────────────
Правило: хотя бы один объект должен иметь Rigidbody!
*/

public class TriggerColliderExamples : MonoBehaviour
{
    // ═══════════════════════════════════════════════
    // СОБЫТИЯ КОЛЛАЙДЕРА (физический контакт)
    // ═══════════════════════════════════════════════

    void OnCollisionEnter(Collision collision)
    {
        // Вызывается ОДИН РАЗ при первом касании
        float impactSpeed = collision.relativeVelocity.magnitude;

        // RichиRich информация о контакте:
        foreach (ContactPoint contact in collision.contacts)
        {
            Debug.DrawRay(contact.point, contact.normal, Color.red, 1f);
        }

        // Звук удара на основе силы
        if (impactSpeed > 3f)
            PlayImpactSound(impactSpeed);
    }

    void OnCollisionStay(Collision collision)
    {
        // Каждый FixedUpdate пока в контакте
        // ОСТОРОЖНО: дорогой если используется неправильно
    }

    void OnCollisionExit(Collision collision)
    {
        // ОДИН РАЗ при разрыве контакта
    }

    // ═══════════════════════════════════════════════
    // СОБЫТИЯ ТРИГГЕРА (зонального обнаружения)
    // ═══════════════════════════════════════════════

    void OnTriggerEnter(Collider other)
    {
        // Паттерн: зона сбора предмета
        if (other.TryGetComponent<Item>(out var item))
            item.Collect();
    }

    void OnTriggerStay(Collider other)
    {
        // Паттерн: зона урона — каждый FixedUpdate наносит урон
        if (other.TryGetComponent<Health>(out var health))
            health.TakeDamage(10f * Time.fixedDeltaTime); // Урон в секунду
    }

    void OnTriggerExit(Collider other)
    {
        // Паттерн: выход из зоны эффекта
        Debug.Log($"{other.name} покинул зону");
    }

    // 2D версии (те же правила, другие сигнатуры)
    void OnTriggerEnter2D(Collider2D other) { }
    void OnTriggerStay2D(Collider2D other) { }
    void OnTriggerExit2D(Collider2D other) { }
    void OnCollisionEnter2D(Collision2D collision) { }
    void OnCollisionStay2D(Collision2D collision) { }
    void OnCollisionExit2D(Collision2D collision) { }

    void PlayImpactSound(float speed) { }
}
```

> **🤔 Проверь себя #3**
> 
> Вы создали зону-триггер для сбора монет. Монеты — статичные объекты без Rigidbody. Персонаж имеет Rigidbody. Почему `OnTriggerEnter` не вызывается, хотя персонаж входит в триггер?

<details> <summary>Ответ и объяснение</summary>

Проблема: монеты (Static Trigger) + персонаж (Rigidbody Collider) → `OnTriggerEnter` **должен** вызываться. Это правильная конфигурация.

Но если монеты — Static Trigger + персонаж — Static Collider (без Rigidbody!) — событие не вызовется.

Проверьте: на каком объекте висит `MonoBehaviour` с `OnTriggerEnter`? Он должен быть **на объекте с коллайдером или триггером**, участвующем в паре. Событие вызывается на **обоих** объектах пары, у которых есть соответствующий метод.

</details>

---

## 4. Физические материалы {#физические-материалы}

`PhysicsMaterial` определяет поверхностные свойства при контакте. Это простой, но часто неправильно используемый инструмент.



```csharp
public class PhysicsMaterialComplete : MonoBehaviour
{
    void Start()
    {
        var mat = new PhysicsMaterial("CustomMaterial");

        // ─── ТРЕНИЕ ──────────────────────────────────────────────────────
        // Закон Кулона: F_friction = μ * F_normal
        // staticFriction >= dynamicFriction (всегда!)

        mat.staticFriction  = 0.6f; // Трение покоя  (начать скользить)
        mat.dynamicFriction = 0.4f; // Трение скольжения (уже скользим)

        // ─── УПРУГОСТЬ ───────────────────────────────────────────────────
        // 0 = пластилин (нет отскока), 1 = идеальный мяч
        // > 1 = физически некорректно, объект набирает энергию!
        mat.bounciness = 0.0f;

        // ─── КОМБИНИРОВАНИЕ ──────────────────────────────────────────────
        // При контакте двух объектов с разными материалами
        // движок должен выбрать одно значение:

        mat.frictionCombine = PhysicsMaterialCombine.Average;  // (A+B)/2
        mat.frictionCombine = PhysicsMaterialCombine.Minimum;  // min(A,B) — хоть одна скользкая = скользко
        mat.frictionCombine = PhysicsMaterialCombine.Maximum;  // max(A,B) — хоть одна шершавая = шершаво
        mat.frictionCombine = PhysicsMaterialCombine.Multiply; // A*B

        mat.bounceCombine   = PhysicsMaterialCombine.Maximum;  // Хорошо для мячей

        GetComponent<Collider>().material = mat;
    }

    // ─── ГОТОВЫЕ РЕЦЕПТЫ ─────────────────────────────────────────────────

    static PhysicsMaterial CreateIce()
    {
        return new PhysicsMaterial("Ice")
        {
            staticFriction  = 0.02f,
            dynamicFriction = 0.01f,
            bounciness      = 0f,
            frictionCombine = PhysicsMaterialCombine.Minimum, // Скользко если хоть одна сторона — лёд
            bounceCombine   = PhysicsMaterialCombine.Average
        };
    }

    static PhysicsMaterial CreateRubber()
    {
        return new PhysicsMaterial("Rubber")
        {
            staticFriction  = 1.0f,
            dynamicFriction = 0.8f,
            bounciness      = 0.8f,
            frictionCombine = PhysicsMaterialCombine.Maximum,
            bounceCombine   = PhysicsMaterialCombine.Maximum  // Отскок если хоть один — резина
        };
    }

    static PhysicsMaterial CreatePlayerMaterial()
    {
        // Нулевое трение для персонажей — не застревает на стенах
        return new PhysicsMaterial("Player")
        {
            staticFriction  = 0f,
            dynamicFriction = 0f,
            bounciness      = 0f,
            frictionCombine = PhysicsMaterialCombine.Minimum,
            bounceCombine   = PhysicsMaterialCombine.Minimum
        };
    }

    // ─── ВАЖНО: material vs sharedMaterial ───────────────────────────────
    void MaterialVsShared()
    {
        var col = GetComponent<Collider>();

        // .material — создаёт КОПИЮ материала для этого объекта
        // Изменения не влияют на другие объекты, но создают новый объект в памяти
        col.material.staticFriction = 0.1f;

        // .sharedMaterial — общий материал (asset)
        // Изменения влияют на ВСЕ объекты с этим материалом!
        // Экономит память, но опасно изменять в рантайме
        col.sharedMaterial = CreateIce();
    }
}
```

---

## 5. Слои и Layer Collision Matrix {#слои}

Слои — это система категоризации объектов для контроля взаимодействий в физике, рендеринге и запросах.



```csharp
public class LayerSystemComplete : MonoBehaviour
{
    // ─── КОНСТАНТЫ СЛОЁВ ─────────────────────────────────────────────────
    // Определяйте через константы, не через числа в коде
    public static class Layers
    {
        // Встроенные (0-7 зарезервированы Unity)
        public const int Default       = 0;
        public const int IgnoreRaycast = 2;
        public const int UI            = 5;

        // Пользовательские (8-31)
        public const int Player      = 8;
        public const int Enemy       = 9;
        public const int Projectile  = 10;
        public const int Environment = 11;
        public const int Trigger     = 12;
        public const int Water       = 13;

        // Маски для использования в Raycast и OverlapSphere
        public static readonly int PlayerMask      = 1 << Player;
        public static readonly int EnemyMask       = 1 << Enemy;
        public static readonly int EnvironmentMask = 1 << Environment;

        // Составные маски
        public static readonly int CharactersMask  = (1 << Player) | (1 << Enemy);
        public static readonly int PhysicalMask    = ~((1 << Trigger) | (1 << UI));
        public static readonly int AllExceptPlayer = ~(1 << Player);
    }

    // ─── LAYER COLLISION MATRIX ───────────────────────────────────────────
    // Настраивается в Edit > Project Settings > Physics
    // Но можно управлять программно:

    [ConMenu("Setup Game Collision Matrix")]
    void SetupCollisionMatrix()
    {
        int player     = LayerMask.NameToLayer("Player");
        int enemy      = LayerMask.NameToLayer("Enemy");
        int projectile = LayerMask.NameToLayer("Projectile");
        int trigger    = LayerMask.NameToLayer("Trigger");
        int env        = LayerMask.NameToLayer("Environment");

        // Снаряды не сталкиваются со снарядами
        Physics.IgnoreLayerCollision(projectile, projectile, true);

        // Игроки проходят друг сквозь друга (кооп)
        Physics.IgnoreLayerCollision(player, player, true);

        // Триггерные зоны не блокируют физику
        Physics.IgnoreLayerCollision(trigger, env,    true);
        Physics.IgnoreLayerCollision(trigger, player, true);
        Physics.IgnoreLayerCollision(trigger, enemy,  true);

        // Враги не блокируют друг друга (свободно ходят сквозь)
        Physics.IgnoreLayerCollision(enemy, enemy, true);

        // Включить столкновение (по умолчанию всё включено)
        Physics.IgnoreLayerCollision(player, enemy, false);
    }

    // Игнорирование конкретных объектов
    void IgnoreSpecificObjects()
    {
        var myCol    = GetComponent<Collider>();
        var otherCol = FindObjectOfType<EnemyShield>().GetComponent<Collider>();

        // Только эти два объекта
        Physics.IgnoreCollision(myCol, otherCol, true);
    }
}
```

> **🤔 Проверь себя #4**
> 
> Как выбрать все объекты КРОМЕ UI и Trigger слоёв с помощью битовой маски? Запишите выражение.

<details> <summary>Ответ и объяснение</summary>



```csharp
// Инвертируем маску из нежелательных слоёв:
LayerMask mask = ~((1 << LayerMask.NameToLayer("UI")) | 
                   (1 << LayerMask.NameToLayer("Trigger")));

// Или через константы:
LayerMask mask = ~((1 << Layers.UI) | (1 << Layers.Trigger));

// Оператор ~ инвертирует все биты:
// Если UI=5, Trigger=12:
// (1<<5) | (1<<12) = ...000001000000100000 (биты 5 и 12 установлены)
// ~(...) = ...111110111111011111 (все биты кроме 5 и 12)
```

</details>

---

## 6. Физические запросы: Raycast и семья {#физические-запросы}

Физические запросы — это способ получить информацию о пространстве без создания физических объектов. Ключевое правило производительности: **используйте NonAlloc-версии в игровом цикле**.

### 6.1 Семейство 3D запросов



```csharp
public class PhysicsQueriesComplete : MonoBehaviour
{
    // ─── ПРЕДВАРИТЕЛЬНО ВЫДЕЛЕННЫЕ БУФЕРЫ ────────────────────────────────
    // Создаём один раз — используем всегда
    private readonly RaycastHit[] hitBuffer     = new RaycastHit[20];
    private readonly Collider[]   overlapBuffer = new Collider[50];

    [Header("Query Settings")]
    [SerializeField] private float   rayLength  = 50f;
    [SerializeField] private LayerMask hitMask;

    void FixedUpdate()
    {
        BasicRaycastExample();
        ShapeCastExamples();
        OverlapExamples();
    }

    // ═══════════════════════════════════════════════
    // RAYCAST — луч
    // ═══════════════════════════════════════════════
    void BasicRaycastExample()
    {
        // Одиночный Raycast — первое попадание
        if (Physics.Raycast(transform.position, Vector3.forward,
                            out RaycastHit hit, rayLength, hitMask))
        {
            // Полная информация о попадании:
            Debug.Log($"Объект:    {hit.collider.name}");
            Debug.Log($"Дистанция: {hit.distance}");
            Debug.Log($"Точка:     {hit.point}");     // Мировые координаты
            Debug.Log($"Нормаль:   {hit.normal}");    // Нормаль поверхности
            Debug.Log($"UV:        {hit.ureCoord}"); // Для декалей
            Debug.Log($"Rigidbody: {hit.rigidbody}"); // null если нет
        }

        // NonAlloc — все попадания БЕЗ аллокации heap
        int count = Physics.RaycastNonAlloc(
            transform.position,
            Vector3.forward,
            hitBuffer,      // Предвыделенный буфер
            rayLength,
            hitMask
        );

        // Сортировка по расстоянию (порядок не гарантирован)
        System.Array.Sort(hitBuffer, 0, count,
            Comparer<RaycastHit>.Create((a, b) =>
                a.distance.CompareTo(b.distance)));

        for (int i = 0; i < count; i++)
        {
            ProcessHit(hitBuffer[i]);
        }
    }

    // ═══════════════════════════════════════════════
    // SHAPE CASTS — "толстые" лучи
    // ═══════════════════════════════════════════════
    void ShapeCastExamples()
    {
        // SphereCast: сфера движется вдоль луча
        // Незаменим для: проверки пути персонажа с учётом размера
        if (Physics.SphereCast(transform.position, 0.5f,
                               Vector3.forward, out RaycastHit sphereHit, rayLength, hitMask))
        {
            Debug.Log($"SphereCast: {sphereHit.collider.name}");
        }

        // CapsuleCast: идеален для проверки движения капсульного персонажа
        var cap = GetComponent<CapsuleCollider>();
        Vector3 top    = transform.position + Vector3.up * (cap.height / 2 - cap.radius);
        Vector3 bottom = transform.position - Vector3.up * (cap.height / 2 - cap.radius);

        if (Physics.CapsuleCast(top, bottom, cap.radius,
                                Vector3.forward, out RaycastHit capsuleHit, rayLength, hitMask))
        {
            Debug.Log($"CapsuleCast: препятствие на {capsuleHit.distance}м");
        }

        // BoxCast: для прямоугольных объектов
        if (Physics.BoxCast(transform.position, new Vector3(0.5f, 0.5f, 0.5f),
                            Vector3.forward, out RaycastHit boxHit,
                            transform.rotation, rayLength, hitMask))
        {
            Debug.Log($"BoxCast: {boxHit.collider.name}");
        }
    }

    // ═══════════════════════════════════════════════
    // OVERLAP — все объекты в зоне
    // ═══════════════════════════════════════════════
    void OverlapExamples()
    {
        // OverlapSphere — все коллайдеры в радиусе
        // Паттерн: взрыв, обнаружение врагов, зоны эффекта
        int count = Physics.OverlapSphereNonAlloc(
            transform.position, 5f, overlapBuffer, hitMask);

        for (int i = 0; i < count; i++)
        {
            float dist      = Vector3.Distance(transform.position,
                                               overlapBuffer[i].transform.position);
            float falloff   = 1f - Mathf.Clamp01(dist / 5f);
            float damage    = 100f * falloff * falloff; // Квадратичное затухание

            if (overlapBuffer[i].TryGetComponent<Health>(out var health))
                health.TakeDamage(damage);
        }

        // OverlapBox
        Physics.OverlapBoxNonAlloc(transform.position, new Vector3(2f, 1f, 3f),
                                   overlapBuffer, transform.rotation, hitMask);

        // OverlapCapsule
        Physics.OverlapCapsuleNonAlloc(transform.position,
                                       transform.position + Vector3.up * 2f,
                                       0.5f, overlapBuffer, hitMask);
    }

    void ProcessHit(RaycastHit hit) { }
}
```

### 6.2 Семейство 2D запросов



```csharp
public class Physics2DQueriesComplete : MonoBehaviour
{
    private readonly RaycastHit2D[] hitBuffer2D     = new RaycastHit2D[10];
    private readonly Collider2D[]   overlapBuffer2D = new Collider2D[20];

    [SerializeField] private LayerMask groundMask;

    void Update()
    {
        // Raycast2D — основное отличие: возвращает RaycastHit2D (не out параметр)
        RaycastHit2D hit = Physics2D.Raycast(
            transform.position, Vector2.down, 5f, groundMask);

        // Проверка: в 2D смотрим на .collider, не на bool
        if (hit.collider != null)
        {
            Debug.Log($"2D Raycast: {hit.collider.name}");
            Debug.Log($"Дистанция: {hit.distance}");
            Debug.Log($"Fraction:  {hit.fraction}"); // [0,1] доля от maxDistance
        }

        // NonAlloc для всех попаданий
        int count = Physics2D.RaycastNonAlloc(
            transform.position, Vector2.down, hitBuffer2D, 5f, groundMask);

        // CircleCast — аналог SphereCast
        RaycastHit2D circleHit = Physics2D.CircleCast(
            transform.position, 0.5f, Vector2.right, 5f, groundMask);

        // BoxCast2D
        RaycastHit2D boxHit2D = Physics2D.BoxCast(
            transform.position,
            new Vector2(1f, 1f),
            0f,              // Угол поворота бокса
            Vector2.down,
            5f, groundMask);

        // CapsuleCast2D
        RaycastHit2D capsuleHit2D = Physics2D.CapsuleCast(
            transform.position,
            new Vector2(1f, 2f),
            CapsuleDirection2D.Vertical,
            0f,
            Vector2.down, 5f, groundMask);

        // OverlapCircle — аналог OverlapSphere
        int overlapCount = Physics2D.OverlapCircleNonAlloc(
            transform.position, 3f, overlapBuffer2D, groundMask);

        // OverlapPoint — точечная проверка
        Collider2D atPoint = Physics2D.OverlapPoint(transform.position, groundMask);

        // Linеcast — от точки A до точки B
        RaycastHit2D lineHit = Physics2D.Linecast(
            transform.position,
            transform.position + Vector3.right * 5f,
            groundMask);
    }

    // Практичный IsGrounded для 2D платформера
    public bool IsGrounded2D()
    {
        var col    = GetComponent<CapsuleCollider2D>();
        Vector2 origin = (Vector2)transform.position +
                         Vector2.down * (col.size.y / 2 - 0.05f);

        // CircleCast лучше Raycast — не застревает в щелях
        RaycastHit2D hit = Physics2D.CircleCast(
            origin, col.size.x * 0.4f, Vector2.down, 0.15f, groundMask);

        return hit.collider != null;
    }
}
```

> **🤔 Проверь себя #5**
> 
> Чем отличается `Physics.RaycastAll` от `Physics.RaycastNonAlloc`? Когда критично использовать NonAlloc?

<details> <summary>Ответ и объяснение</summary>

`RaycastAll` создаёт новый массив `RaycastHit[]` при каждом вызове — это **аллокация в heap**. Garbage Collector должен периодически собирать этот мусор, что вызывает паузы (GC spikes).

`RaycastNonAlloc` записывает результаты в **предварительно выделенный буфер** — нет аллокации, нет мусора.

**Критично использовать NonAlloc:**

- В `Update` / `FixedUpdate` — вызывается каждый кадр
- В системах с множеством объектов (враги, частицы)
- В мобильных играх — GC паузы заметнее

**Можно использовать RaycastAll:**

- В инициализации (`Start`, `Awake`)
- В редко вызываемом коде (смена уровня, UI действия)
- В `#if UNITY_EDITOR` коде

</details>

---

## 7. FixedUpdate vs Update: почему это важно {#fixedupdate}

Это не просто "соглашение" — это математическое требование к стабильности численной симуляции.

### 7.1 Детерминизм и стабильность



```csharp
public class UpdateFixedUpdateExplained : MonoBehaviour
{
    private Rigidbody rb;
    private Vector3   moveInput;
    private bool      jumpPressed;

    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    // ─────────────────────────────────────────────────────────────────────
    // UPDATE: Только чтение и неффизическая логика
    // ─────────────────────────────────────────────────────────────────────
    void Update()
    {
        // ✓ ПРАВИЛЬНО в Update: чтение ввода
        float h = Input.GetAxisRaw("Horizontal");
        float v = Input.GetAxisRaw("Vertical");
        moveInput = new Vector3(h, 0f, v).normalized;

        // ✓ GetKeyDown работает ТОЛЬКО в Update!
        // В FixedUpdate пропускает нажатия при высоком FPS
        if (Input.GetKeyDown(KeyCode.Space))
            jumpPressed = true; // Флаг — применим в FixedUpdate

        // ✓ ПРАВИЛЬНО в Update: всё неффизическое
        // UI, AudioSource, Camera position (без физики), анимации
    }

    // ─────────────────────────────────────────────────────────────────────
    // FIXEDUPDATE: ВСЯ физика
    // ─────────────────────────────────────────────────────────────────────
    void FixedUpdate()
    {
        // ✓ ПРАВИЛЬНО: AddForce в FixedUpdate
        // Time.fixedDeltaTime — константа (обычно 0.02s)
        // Независимо от FPS физика получает одинаковые импульсы
        rb.AddForce(moveInput * 10f, ForceMode.Force);

        // ✓ ПРАВИЛЬНО: прыжок через флаг
        if (jumpPressed)
        {
            rb.AddForce(Vector3.up * 5f, ForceMode.VelocityChange);
            jumpPressed = false;
        }

        // ✗ НЕПРАВИЛЬНО в FixedUpdate:
        // Input.GetKeyDown → пропускает при высоком FPS
        // Time.deltaTime → используйте Time.fixedDeltaTime
        // Transform.position (напрямую) → конфликт с физикой
    }

    void LateUpdate()
    {
        // ✓ ПРАВИЛЬНО в LateUpdate: зависит от результатов Update
        // Камера следит за игроком (после того как он подвинулся)
        // UI обновляется после всей логики
    }
}
```

### 7.2 Правила работы с Transform и Rigidbody



```csharp
public class TransformRigidbodyRules : MonoBehaviour
{
    private Rigidbody rb;

    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    void FixedUpdate()
    {
        // ─── ТЕЛЕПОРТАЦИЯ (мгновенное перемещение) ───────────────────────

        // ✗ ПЛОХО: физика не знает о перемещении
        // transform.position = new Vector3(0, 5, 0);

        // ✓ ХОРОШО: PhysX обновит своё внутреннее состояние
        rb.position = new Vector3(0, 5, 0);
        rb.rotation = Quaternion.identity;
        rb.linearVelocity   = Vector3.zero; // Обнуляем скорость!
        rb.angularVelocity  = Vector3.zero;

        // ─── ПЛАВНОЕ КИНЕМАТИЧЕСКОЕ ДВИЖЕНИЕ ─────────────────────────────

        // Для isKinematic = true используйте MovePosition/MoveRotation
        // PhysX корректно обрабатывает столкновения при движении
        rb.MovePosition(rb.position + Vector3.forward * 5f * Time.fixedDeltaTime);
        rb.MoveRotation(Quaternion.Euler(0f, 90f * Time.fixedDeltaTime, 0f) * rb.rotation);

        // ─── ОГРАНИЧЕНИЕ СКОРОСТИ ─────────────────────────────────────────
        // Антипаттерн: нет максимальной скорости → бесконечное ускорение
        float maxSpeed = 10f;
        if (rb.linearVelocity.magnitude > maxSpeed)
        {
            rb.linearVelocity = rb.linearVelocity.normalized * maxSpeed;
        }

        // Или через rb.maxLinearVelocity:
        rb.maxLinearVelocity = maxSpeed;
    }
}
```

---

## 8. Joints: суставы и ограничения {#joints}

Joints реализуют физические ограничения между двумя Rigidbody. Внутри они работают как дополнительные ограничения в solver PhysX — применяют корректирующие импульсы каждый шаг.

### 8.1 HingeJoint: вращение вокруг оси



```csharp
public class HingeJointComplete : MonoBehaviour
{
    [Header("Hinge Settings")]
    [SerializeField] private Rigidbody connectedBody;
    [SerializeField] private float springForce    = 100f;
    [SerializeField] private float springDamper   = 10f;
    [SerializeField] private float motorSpeed     = 90f;
    [SerializeField] private float motorForce     = 200f;
    [SerializeField] private float angleLimitMin  = -90f;
    [SerializeField] private float angleLimitMax  =  90f;

    HingeJoint hinge;

    void Start()
    {
        hinge = gameObject.AddComponent<HingeJoint>();

        // ─── БАЗОВЫЕ ПАРАМЕТРЫ ────────────────────────────────────────────
        hinge.connectedBody = connectedBody; // null = мировое пространство

        // Ось вращения в локальном пространстве этого объекта
        hinge.axis = Vector3.up;

        // Точка крепления в локальном пространстве
        hinge.anchor = new Vector3(-0.5f, 0f, 0f); // Петля у края

        // ─── ПРУЖИНА ─────────────────────────────────────────────────────
        // Возвращает к целевому углу
        hinge.useSpring = true;
        var spring = hinge.spring;
        spring.spring         = springForce;   // Жёсткость
        spring.damper         = springDamper;  // Демпфирование колебаний
        spring.targetPosition = 0f;            // Нейтральный угол (закрыто)
        hinge.spring = spring;

        // ─── ЛИМИТЫ ──────────────────────────────────────────────────────
        hinge.useLimits = true;
        var limits = hinge.limits;
        limits.min              = angleLimitMin; // Минимальный угол
        limits.max              = angleLimitMax; // Максимальный угол
        limits.bounciness       = 0.1f;          // Отскок у лимита
        limits.bounceMinVelocity = 0.5f;         // Мин. скорость для отскока
        limits.contactDistance  = 5f;            // Мягкая зона перед лимитом
        hinge.limits = limits;

        // ─── МОТОР ───────────────────────────────────────────────────────
        // Принудительное вращение (двигатель)
        hinge.useMotor = true;
        var motor = hinge.motor;
        motor.targetVelocity = motorSpeed; // Целевая угловая скорость (°/s)
        motor.force          = motorForce; // Максимальная сила мотора
        motor.freeSpin       = false;      // Тормозить при достижении цели
        hinge.motor = motor;
    }

    // Чтение текущего состояния
    void Update()
    {
        Debug.Log($"Угол: {hinge.angle}°");
        Debug.Log($"Угловая скорость: {hinge.velocity}°/s");
    }
}

// ─── ПРАКТИЧЕСКИЙ ПРИМЕР: Физическая дверь ───────────────────────────────────
public class PhysicsDoor : MonoBehaviour
{
    private HingeJoint hinge;
    private Rigidbody  rb;

    void Start()
    {
        rb   = GetComponent<Rigidbody>();
        rb.mass = 30f;

        hinge       = gameObject.AddComponent<HingeJoint>();
        hinge.axis  = Vector3.up;
        hinge.anchor = new Vector3(-0.5f, 0f, 0f);

        hinge.useLimits = true;
        var lim = hinge.limits;
        lim.min = 0f;
        lim.max = 100f;
        lim.bounciness = 0.05f;
        hinge.limits = lim;

        hinge.useSpring = true;
        var spring = hinge.spring;
        spring.spring  = 50f;
        spring.damper  = 8f;
        spring.targetPosition = 0f;
        hinge.spring = spring;
    }

    public void Push(Vector3 forceDir, float force)
    {
        rb.AddForce(forceDir * force, ForceMode.Impulse);
    }

    public bool IsOpen()    => Mathf.Abs(hinge.angle) > 25f;
    public float OpenAngle() => hinge.angle;
}
```

### 8.2 SpringJoint: пружинное соединение



```csharp
public class SpringJointComplete : MonoBehaviour
{
    void SetupSpring()
    {
        var spring = gameObject.AddComponent<SpringJoint>();

        // Подвешен к фиксированной точке (null = мировые координаты)
        spring.connectedBody = null;
        spring.autoConfigureConnectedAnchor = false;
        spring.connectedAnchor = new Vector3(0f, 10f, 0f); // Точка крепления

        // ─── ПАРАМЕТРЫ ПРУЖИНЫ ────────────────────────────────────────────
        // Закон Гука: F = -k * x (k = spring, x = отклонение от natural length)
        spring.spring = 100f;  // Жёсткость: выше = жёстче

        // Критическое затухание: damper = 2 * sqrt(spring * mass)
        // При критическом затухании — плавный возврат без колебаний
        var rb = GetComponent<Rigidbody>();
        spring.damper = 2f * Mathf.Sqrt(spring.spring * rb.mass);

        // Диапазон, где пружина не действует (мёртвая зона)
        spring.minDistance = 0f;  // Минимальная длина
        spring.maxDistance = 2f;  // Максимальная длина (за ней пружина тянет)

        // Настройки anchor
        spring.anchor          = Vector3.zero; // Точка на этом объекте
        spring.connectedAnchor = Vector3.zero; // Точка на подключённом объекте
    }
}

// ─── GRAPPLING HOOK (Крюк-кошка) ─────────────────────────────────────────────
public class GrapplingHook : MonoBehaviour
{
    [SerializeField] private float maxDistance   = 25f;
    [SerializeField] private float springForce   = 4.5f;
    [SerializeField] private float damperForce   = 7f;
    [SerializeField] private float massScale     = 4.5f;

    private SpringJoint joint;
    private Rigidbody   rb;
    private LineRenderer lineRenderer;

    void Start()
    {
        rb           = GetComponent<Rigidbody>();
        lineRenderer = GetComponent<LineRenderer>();
    }

    public void Grapple(Vector3 targetPoint)
    {
        joint = gameObject.AddComponent<SpringJoint>();
        joint.autoConfigureConnectedAnchor = false;
        joint.connectedAnchor = targetPoint;

        float distance = Vector3.Distance(transform.position, targetPoint);

        // Пружина начинает тянуть когда дистанция > maxDistance
        joint.maxDistance = distance * 0.8f;
        joint.minDistance = distance * 0.2f;

        joint.spring    = springForce;
        joint.damper    = damperForce;
        joint.massScale = massScale;

        lineRenderer.enabled = true;
    }

    public void Release()
    {
        Destroy(joint);
        lineRenderer.enabled = false;
    }

    void LateUpdate()
    {
        if (joint == null) return;
        lineRenderer.SetPosition(0, transform.position);
        lineRenderer.SetPosition(1, joint.connectedAnchor);
    }
}
```

### 8.3 ConfigurableJoint: полный контроль



```csharp
public class ConfigurableJointComplete : MonoBehaviour
{
    void SetupConfigurable()
    {
        var joint = gameObject.AddComponent<ConfigurableJoint>();

        // ─── 6 СТЕПЕНЕЙ СВОБОДЫ ──────────────────────────────────────────
        // Каждая ось: Locked / Limited / Free

        // Пример: маятник на вертикальном стержне
        joint.xMotion = ConfigurableJointMotion.Locked;   // Нет сдвига по X
        joint.yMotion = ConfigurableJointMotion.Locked;   // Нет сдвига по Y
        joint.zMotion = ConfigurableJointMotion.Locked;   // Нет сдвига по Z

        joint.angularXMotion = ConfigurableJointMotion.Free;   // Качается по X
        joint.angularYMotion = ConfigurableJointMotion.Locked; // Нет вращения Y
        joint.angularZMotion = ConfigurableJointMotion.Free;   // Качается по Z

        // ─── ЛИМИТЫ ──────────────────────────────────────────────────────
        var angLimit = new SoftJointLimit();
        angLimit.limit         = 45f;
        angLimit.bounciness    = 0f;
        angLimit.contactDistance = 5f;

        joint.lowAngularXLimit  = angLimit;
        joint.highAngularXLimit = angLimit;
        joint.angularZLimit     = angLimit;

        // ─── DRIVE (принудительное движение) ─────────────────────────────
        var drive = new JointDrive();
        drive.positionSpring = 500f;   // Сила пружины позиции
        drive.positionDamper = 50f;    // Демпфирование
        drive.maximumForce   = 1000f;  // Лимит силы

        joint.xDrive = drive;
        joint.yDrive = drive;
        joint.zDrive = drive;

        var angDrive = new JointDrive();
        angDrive.positionSpring = 100f;
        angDrive.positionDamper = 10f;
        angDrive.maximumForce   = 500f;

        joint.angularXDrive  = angDrive;
        joint.angularYZDrive = angDrive;

        // Целевые позиция и поворот для Drive
        joint.targetPosition = Vector3.zero;
        joint.targetRotation = Quaternion.identity;
    }
}
```

---

## 9. Оптимизация физической симуляции {#оптимизация}

> Профилируйте перед оптимизацией. `Window > Analysis > Physics Profiler` — ваш главный инструмент.

### 9.1 Sleeping: экономия на неподвижных объектах



```csharp
public class SleepingOptimizationGuide : MonoBehaviour
{
    /*
    Sleeping — механизм PhysX/Box2D: когда кинетическая энергия тела
    падает ниже порога, движок перестаёт его симулировать.

    Условие сна: 0.5 * mass * v² + 0.5 * I * ω² < sleepThreshold

    Объект просыпается при:
    - Получении силы/импульса
    - Столкновении с движущимся объектом
    - Явном вызове rb.WakeUp()
    */

    private Rigidbody rb;

    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    void SleepingAPI()
    {
        // Проверить состояние
        bool isSleeping = rb.IsSleeping();

        // Принудительный сон (экономия ресурсов для далёких объектов)
        rb.Sleep();

        // Принудительное пробуждение
        rb.WakeUp();

        // Глобальный порог сна (Edit > Project Settings > Physics)
        Physics.sleepThreshold = 0.005f; // По умолчанию

        // Антипаттерн: объект никогда не спит
        // rb.AddForce(Vector3.zero); // Даже нулевая сила будит объект!
        // rb.WakeUp();               // Каждый кадр — никакого сна
    }

    // Distance Culling: отключаем физику для далёких объектов
    [SerializeField] private float cullingDistance = 50f;
    private Transform              playerTransform;

    void FixedUpdate()
    {
        if (playerTransform == null) return;

        float sqrDist = (transform.position - playerTransform.position).sqrMagnitude;
        float sqrCull = cullingDistance * cullingDistance;

        if (sqrDist > sqrCull)
        {
            if (!rb.IsSleeping()) rb.Sleep();
        }
        else
        {
            // Пробуждаем только если нужна физика
            if (rb.IsSleeping() && HasPhysicsActivity())
                rb.WakeUp();
        }
    }

    bool HasPhysicsActivity() => rb.linearVelocity.sqrMagnitude > 0.01f;
}
```

### 9.2 Physics Settings: ключевые параметры



```csharp
public class PhysicsSettingsGuide : MonoBehaviour
{
    void ApplySettings()
    {
        // ─── ВРЕМЕННОЙ ШАГ ────────────────────────────────────────────────
        // По умолчанию 0.02 (50 Hz)
        // Меньше = точнее, дороже. Больше = дешевле, нестабильнее.
        // Мобильные: 0.033 (30 Hz)
        // VR: 1/90 ≈ 0.011 (90 Hz) — обязательно!
        Time.fixedDeltaTime = 0.02f;

        // Защита от спирали смерти
        Time.maximumDeltaTime = 0.1333f; // Макс 8 физических шагов за кадр

        // ─── ГРАВИТАЦИЯ ───────────────────────────────────────────────────
        Physics.gravity = new Vector3(0f, -9.81f, 0f); // Земля
        // Physics.gravity = new Vector3(0f, -1.62f, 0f); // Луна
        // Physics.gravity = new Vector3(0f, -3.72f, 0f); // Марс

        // ─── SOLVER ITERATIONS ────────────────────────────────────────────
        // Больше = стабильнее стеки объектов, тяжелее
        Physics.defaultSolverIterations         = 6;  // По умолчанию
        Physics.defaultSolverVelocityIterations = 1;  // По умолчанию

        // Для конкретного Rigidbody (например нестабильный стек):
        var rb = GetComponent<Rigidbody>();
        rb.solverIterations         = 12;
        rb.solverVelocityIterations = 4;

        // ─── BOUNCE THRESHOLD ─────────────────────────────────────────────
        // Объекты со скоростью ниже этого порога не отскакивают
        // Увеличьте чтобы убрать микро-дрожания в стеках
        Physics.bounceThreshold = 2f; // По умолчанию 2

        // ─── CONTACT OFFSET ───────────────────────────────────────────────
        // Расстояние, на котором PhysX начинает создавать контакты
        // Слишком мало = нестабильность. Слишком много = объекты "плавают"
        Physics.defaultContactOffset = 0.01f;

        // ─── QUERY SETTINGS ───────────────────────────────────────────────
        // Включать ли триггеры в результаты Raycast
        Physics.queriesHitTriggers = true;

        // Хит с обратной стороны меша
        Physics.queriesHitBackfaces = false;

        // ─── SLEEP THRESHOLD ──────────────────────────────────────────────
        Physics.sleepThreshold = 0.005f;
    }
}
```

### 9.3 Оптимизация коллайдеров



```csharp
public class ColliderOptimizationRules : MonoBehaviour
{
    // ─── ПРАВИЛО 1: Используйте примитивы вместо MeshCollider ─────────────
    // Sphere проверка: расстояние < r1+r2 (1 операция)
    // MeshCollider concave: O(n) против O(m) треугольников

    // ─── ПРАВИЛО 2: Статические коллайдеры без Rigidbody ─────────────────
    // PhysX кэширует статическую геометрию в ускоряющих структурах
    // Движение статического коллайдера = перестройка кэша (ДОРОГО!)

    [ConMenu("Fix: Add Kinematic Rigidbody to Moving Collider")]
    void FixMovingColliderWithoutRigidbody()
    {
        // ЕСЛИ объект движется и имеет Collider — добавьте Rigidbody
        if (GetComponent<Collider>() != null && GetComponent<Rigidbody>() == null)
        {
            var rb = gameObject.AddComponent<Rigidbody>();
            rb.isKinematic = true; // Движется кодом, но PhysX знает об этом
            rb.interpolation = RigidbodyInterpolation.Interpolate;
        }
    }

    // ─── ПРАВИЛО 3: NonAlloc везде в игровом цикле ────────────────────────
    private readonly RaycastHit[] buffer = new RaycastHit[16];

    void Update()
    {
        // ✗ ПЛОХО: аллокация каждый кадр
        // RaycastHit[] hits = Physics.RaycastAll(...)

        // ✓ ХОРОШО: нет аллокации
        int count = Physics.RaycastNonAlloc(transform.position,
                                            Vector3.forward, buffer, 10f);
        for (int i = 0; i < count; i++)
        {
            // Обработка buffer[i]
        }
    }

    // ─── ПРАВИЛО 4: CompositeCollider2D для тайловых карт ────────────────
    // Тайловая карта из 1000 тайлов = 1000 коллайдеров (катастрофа)
    // TilemapCollider2D + CompositeCollider2D = 1 оптимизированный коллайдер

    // ─── ПРАВИЛО 5: Layer Collision Matrix ───────────────────────────────
    // Каждая активная пара слоёв добавляет работу в Broad Phase
    // Отключайте ненужные пары в Edit > Project Settings > Physics
}
```

---

## 10. Подводные камни {#подводные-камни}

### 10.1 Tunneling: прохождение сквозь



```csharp
public class TunnelingGuide : MonoBehaviour
{
    /*
    ПРИЧИНА:
    Discrete симуляция проверяет только фиксированные моменты.
    Если за 0.02s объект переместился дальше толщины коллайдера — пролетает насквозь.

    Критическая скорость = размер_коллайдера / fixedDeltaTime
    Стена 0.1m, dt=0.02s: v_critical = 5 m/s

    Снаряд 50 m/s >> 5 m/s → гарантированный tunneling!
    */

    void SolveTunneling()
    {
        var rb = GetComponent<Rigidbody>();

        // ─── РЕШЕНИЕ 1: ContinuousSpeculative ────────────────────────────
        rb.collisionDetectionMode = CollisionDetectionMode.ContinuousSpeculative;

        // ─── РЕШЕНИЕ 2: Ограничение скорости ─────────────────────────────
        rb.maxLinearVelocity = 20f;

        // ─── РЕШЕНИЕ 3: Более толстые коллайдеры ─────────────────────────
        // Дизайнерское решение: стены min 0.2m толщиной

        // ─── РЕШЕНИЕ 4: Ручной SphereCast для снарядов ───────────────────
    }
}

// Ручное анти-tunneling для снарядов
public class AntiTunnelingProjectile : MonoBehaviour
{
    private Rigidbody rb;
    private Vector3   previousPosition;

    [SerializeField] private float      radius  = 0.1f;
    [SerializeField] private LayerMask  hitMask;

    void Start()
    {
        rb               = GetComponent<Rigidbody>();
        previousPosition = transform.position;
    }

    void FixedUpdate()
    {
        Vector3 currentPos = rb.position;
        Vector3 delta      = currentPos - previousPosition;
        float   distance   = delta.magnitude;

        if (distance > 0.001f)
        {
            // Проверяем весь путь за этот шаг
            if (Physics.SphereCast(previousPosition, radius,
                                   delta.normalized, out RaycastHit hit,
                                   distance, hitMask))
            {
                // Столкновение, которое Discrete пропустил!
                HandleHit(hit);

                // Возвращаем в точку контакта
                rb.position        = hit.point + hit.normal * radius;
                rb.linearVelocity  = Vector3.Reflect(rb.linearVelocity, hit.normal) * 0.3f;
            }
        }

        previousPosition = rb.position;
    }

    void HandleHit(RaycastHit hit) { }
}
```

### 10.2 Jitter: дрожание объектов



```csharp
public class JitterGuide : MonoBehaviour
{
    /*
    ПРИЧИНЫ jitter:
    1. bounciness > 0 на материале → микро-отскоки
    2. Несоответствие масс (тяжёлый на лёгком)
    3. Слишком большой Contact Offset
    4. Недостаточно Solver Iterations для стека
    5. Penetration слишком глубокое → solver "перестреливает"
    */

    void FixJitter()
    {
        var rb = GetComponent<Rigidbody>();

        // ─── FIX 1: Bounce Threshold ──────────────────────────────────────
        Physics.bounceThreshold = 2f; // Не отскакивать при скорости < 2 m/s

        // ─── FIX 2: Solver Iterations ────────────────────────────────────
        rb.solverIterations         = 10; // Лучше сходится, меньше ошибок
        rb.solverVelocityIterations = 4;

        // ─── FIX 3: Physics Material ──────────────────────────────────────
        var mat = new PhysicsMaterial("AntiJitter");
        mat.bounciness   = 0f;
        mat.bounceCombine = PhysicsMaterialCombine.Minimum;
        GetComponent<Collider>().material = mat;

        // ─── FIX 4: Angular Drag для стеков ──────────────────────────────
        rb.angularDamping = 0.5f; // Гасим компенсационное вращение

        // ─── FIX 5: Sleep Threshold ───────────────────────────────────────
        Physics.sleepThreshold = 0.01f; // Выше → быстрее засыпают
    }

    // Сглаживание камеры как альтернатива борьбы с jitter
    public class SmoothCamera : MonoBehaviour
    {
        [SerializeField] private Transform target;
        [SerializeField] private float     smoothTime = 0.1f;
        private Vector3                    velocity;

        void LateUpdate()
        {
            // SmoothDamp скрывает физический jitter от игрока
            transform.position = Vector3.SmoothDamp(
                transform.position, target.position,
                ref velocity, smoothTime);
        }
    }
}
```

### 10.3 Масштаб сцены



```csharp
public class ScaleProblemsGuide : MonoBehaviour
{
    /*
    PhysX СПРОЕКТИРОВАН для масштаба 1 unit = 1 метр.

    МАЛЕНЬКИЙ МАСШТАБ (1 unit = 1 cm):
    - Гравитация 9.81 unit/s² = 9.81 cm/s² → почти невесомость
    - Contact Offset 0.01 unit = 1% от размера объекта → объекты "плавают"
    - Sleep Threshold слишком большой

    БОЛЬШОЙ МАСШТАБ (1 unit = 100 m):
    - Float precision: объект на позиции (100000, 0, 100000) дрожит!
    - Числа с плавающей точкой float теряют точность при |x| > ~1000 units
    */

    void FixSmallScale()
    {
        float scale = 100f; // 1 unit = 1cm → масштаб 100

        // Масштабируем физические константы
        Physics.gravity               = new Vector3(0f, -9.81f * scale, 0f);
        Physics.defaultContactOffset  = 0.01f;   // Не меняем — он в мировых единицах
        Physics.sleepThreshold        = 0.005f * scale * scale; // Энергия = v²*m
        Physics.bounceThreshold       = 2f * scale;
    }

    // Floating Origin для больших миров
    public class FloatingOrigin : MonoBehaviour
    {
        [SerializeField] private Transform player;
        [SerializeField] private float     threshold = 500f;

        void Update()
        {
            if (player.position.magnitude <= threshold) return;

            Vector3 offset = player.position;

            // Сдвигаем все корневые объекты
            foreach (var obj in FindObjectsByType<Transform>(FindObjectsSortMode.None))
            {
                if (obj.parent == null && obj != transform)
                    obj.position -= offset;
            }

            Debug.Log($"Floating Origin: перецентрирование на {offset}");
        }
    }
}
```

### 10.4 Прочие ловушки



```csharp
public class OtherCommonPitfalls : MonoBehaviour
{
    // ─── ЛОВУШКА 1: CharacterController vs Rigidbody ─────────────────────
    // Никогда не ставьте оба на одном объекте!
    // CharacterController при Move() игнорирует Rigidbody
    // Используйте одно из двух

    // ─── ЛОВУШКА 2: Отрицательный scale ──────────────────────────────────
    // transform.localScale = new Vector3(-1, 1, 1) → ломает коллайдеры!
    // Для зеркала используйте поворот на 180° или другой меш

    // ─── ЛОВУШКА 3: Instantiate и физика ─────────────────────────────────
    void SpawnProjectile()
    {
        var obj = Instantiate(projectilePrefab, firePoint.position, firePoint.rotation);
        var rb  = obj.GetComponent<Rigidbody>();

        // Безопасно в FixedUpdate — применится в текущем шаге
        rb.linearVelocity = transform.forward * 50f;
    }

    // ─── ЛОВУШКА 4: OnCollision вызывается на обоих объектах ─────────────
    // При столкновении A и B: OnCollisionEnter вызывается И на A, И на B
    // Не применяйте урон дважды!

    void OnCollisionEnter(Collision collision)
    {
        // Проверяйте роль объекта чтобы не задублировать логику
        if (!CompareTag("Projectile")) return; // Только снаряд наносит урон
        if (collision.gameObject.TryGetComponent<Health>(out var h))
            h.TakeDamage(10f);
    }

    // ─── ЛОВУШКА 5: Physics Material через .material создаёт копию ───────
    void DontCreateMaterialEachFrame()
    {
        var col = GetComponent<Collider>();

        // ✗ ПЛОХО: создаёт новый объект каждый вызов!
        // col.material.friction = 0.5f;

        // ✓ ХОРОШО: измените через sharedMaterial или сохраните ссылку
        // col.sharedMaterial.staticFriction = 0.5f;
    }

    [SerializeField] private GameObject projectilePrefab;
    [SerializeField] private Transform  firePoint;
}
```

> **🤔 Проверь себя #6**
> 
> Ваш персонаж иногда "проваливается" сквозь пол при высокой скорости. Назовите три причины и решение для каждой.

<details> <summary>Ответ и объяснение</summary>

**Причина 1: Discrete collision detection**

- Решение: `rb.collisionDetectionMode = CollisionDetectionMode.ContinuousSpeculative`

**Причина 2: Пол слишком тонкий**

- Решение: Увеличить толщину пола до минимум 0.2м. Коллайдер должен быть толще `скорость × fixedDeltaTime`

**Причина 3: Скорость превышает критическую**

- Критическая скорость = размер_коллайдера / fixedDeltaTime
- Решение: `rb.maxLinearVelocity = разумный_предел` + увеличить Contact Offset: `Physics.defaultContactOffset = 0.02f`

**Бонус — Причина 4: Отрицательный scale у пола**

- Отрицательный localScale ломает нормали коллайдера
- Решение: никогда не используйте отрицательный scale, используйте поворот 180°

</details>

---

## 11. 2D vs 3D: полное сравнение {#сравнение}

|Характеристика|3D Physics (PhysX)|2D Physics (Box2D)|
|---|---|---|
|**Движок**|NVIDIA PhysX|Erin Catto's Box2D|
|**API**|`Physics.*`|`Physics2D.*`|
|**Rigidbody**|`Rigidbody`|`Rigidbody2D`|
|**Пространство**|X, Y, Z|X, Y|
|**Вращение**|Quaternion (3 оси)|float (только Z, градусы)|
|**Гравитация**|`Physics.gravity` (Vector3)|`Physics2D.gravity` (Vector2)|
|**Broad Phase**|SAP (Sweep and Prune)|Dynamic Tree|
|**Narrow Phase**|GJK + EPA|SAT + Clipping|
|**Solver**|PGS (Projected Gauss-Seidel)|Sequential Impulses|
|**Body Types**|`isKinematic` bool|`Dynamic / Kinematic / Static`|
|**Гравитация на объект**|Через `rb.useGravity`|`rb.gravityScale` (множитель)|
|**Raycast возврат**|`bool` + `out RaycastHit`|`RaycastHit2D` (проверяй `.collider`)|
|**OverlapSphere аналог**|`Physics.OverlapSphere`|`Physics2D.OverlapCircle`|
|**SphereCast аналог**|`Physics.SphereCast`|`Physics2D.CircleCast`|
|**CapsuleCast**|`Physics.CapsuleCast`|`Physics2D.CapsuleCast`|
|**Специфичный запрос**|`Physics.BoxCast`|`Physics2D.Linecast`, `OverlapPoint`|
|**Коллайдеры**|Sphere, Capsule, Box, Mesh, Terrain|Circle, Capsule, Box, Polygon, Edge|
|**Compound colliders**|Дочерние GameObject + Rigidbody на родителе|Аналогично|
|**Composite**|Нет прямого аналога|`CompositeCollider2D` (для тайлмапов)|
|**Joints 3D**|Hinge, Spring, Fixed, Configurable, Character|—|
|**Joints 2D**|—|Hinge, Distance, Spring, Slider, Wheel, Relative, Target|
|**HingeJoint**|`HingeJoint`|`HingeJoint2D`|
|**SpringJoint**|`SpringJoint` (spring + damper)|`SpringJoint2D` (frequency + dampingRatio)|
|**SliderJoint**|Через `ConfigurableJoint`|`SliderJoint2D`|
|**WheelJoint**|`WheelCollider` (специализированный)|`WheelJoint2D`|
|**Solver Iterations**|`Physics.defaultSolverIterations`|`Physics2D.velocityIterations` + `positionIterations`|
|**Sleep Mode**|`Physics.sleepThreshold`|`Physics2D.sleepMode` (enum)|
|**Collision Events**|`OnCollisionEnter/Stay/Exit`|`OnCollisionEnter2D/Stay2D/Exit2D`|
|**Trigger Events**|`OnTriggerEnter/Stay/Exit`|`OnTriggerEnter2D/Stay2D/Exit2D`|
|**Изоляция**|**3D и 2D физика полностью изолированы. Rigidbody и Rigidbody2D не взаимодействуют!**||
|**Лучше для**|Шутеры, гонки, симуляторы, 3D платформеры|Платформеры, top-down, puzzle, мобильные игры|
|**Производительность**|Тяжелее при сложной геометрии|Легче для простых 2D сцен|

### Ключевые отличия в коде



```csharp
// ─── ИНИЦИАЛИЗАЦИЯ ────────────────────────────────────────────────────────────

// 3D
var rb3D = GetComponent<Rigidbody>();
rb3D.mass          = 1f;
rb3D.linearDamping = 0f;
rb3D.constraints   = RigidbodyConstraints.FreezeRotation;
rb3D.useGravity    = true;

// 2D
var rb2D = GetComponent<Rigidbody2D>();
rb2D.mass         = 1f;
rb2D.linearDamping = 0f;
rb2D.constraints  = RigidbodyConstraints2D.FreezeRotation;
rb2D.gravityScale = 1f; // Вместо useGravity

// ─── СИЛЫ ─────────────────────────────────────────────────────────────────────

// 3D — то же API
rb3D.AddForce(new Vector3(10f, 0f, 0f), ForceMode.Force);
rb3D.AddTorque(new Vector3(0f, 90f, 0f), ForceMode.Force);

// 2D — Vector2, те же ForceMode
rb2D.AddForce(new Vector2(10f, 0f), ForceMode2D.Force);
rb2D.AddTorque(90f, ForceMode2D.Force); // Только скалярное значение!

// ─── RAYCAST ──────────────────────────────────────────────────────────────────

// 3D: bool return + out parameter
if (Physics.Raycast(origin3D, Vector3.forward, out RaycastHit hit3D, 10f, mask))
{
    Debug.Log(hit3D.collider.name);
}

// 2D: возвращает RaycastHit2D, проверяем .collider
RaycastHit2D hit2D = Physics2D.Raycast(origin2D, Vector2.right, 10f, mask);
if (hit2D.collider != null)
{
    Debug.Log(hit2D.collider.name);
    Debug.Log(hit2D.fraction); // Дополнительное поле, нет в 3D
}

// ─── SPRINGS ──────────────────────────────────────────────────────────────────

// 3D SpringJoint: spring (жёсткость) + damper (затухание)
var spring3D = gameObject.AddComponent<SpringJoint>();
spring3D.spring = 100f;
spring3D.damper = 10f;

// 2D SpringJoint2D: frequency (частота) + dampingRatio (коэффициент затухания)
// Более интуитивная параметризация!
var spring2D = gameObject.AddComponent<SpringJoint2D>();
spring2D.frequency    = 2f;   // Гц — 2 колебания в секунду
spring2D.dampingRatio = 0.5f; // 0 = нет затухания, 1 = критическое
```

---

## 12. Практические задания {#практика}

---

### 🟢 Задание 1 (Базовый): Физический персонаж

#### Условие

Создайте управляемого персонажа с использованием `Rigidbody`. Требования:

- Движение через `AddForce` (WASD)
- Прыжок через `ForceMode.VelocityChange` (Space, только на земле)
- `GroundCheck` через `OverlapSphereNonAlloc`
- Определение края платформы — персонаж тормозит у края
- Корректная настройка `Interpolation`, `Constraints`, `CollisionDetection`
- Отладочная визуализация в `OnDrawGizmosSelected`

#### Стартовый скелет



```csharp
using UnityEngine;

[RequireComponent(typeof(Rigidbody))]
[RequireComponent(typeof(CapsuleCollider))]
public class PhysicsCharacter : MonoBehaviour
{
    // ─── ИНСПЕКТОР ────────────────────────────────────────────────────────

    [Header("Movement")]
    [SerializeField] private float moveForce    = 15f;
    [SerializeField] private float maxSpeed     = 6f;
    [SerializeField] private float jumpForce    = 6f;
    [SerializeField] private float brakingForce = 20f; // Торможение при отпускании

    [Header("Ground Check")]
    [SerializeField] private float      groundCheckRadius = 0.28f;
    [SerializeField] private float      groundCheckOffset = 0.05f; // Смещение вниз
    [SerializeField] private LayerMask  groundMask;

    [Header("Edge Detection")]
    [SerializeField] private float edgeLookAhead  = 0.6f;  // Дистанция взгляда вперёд
    [SerializeField] private float edgeRayDown    = 1.5f;  // Как далеко смотреть вниз
    [SerializeField] private bool  stopAtEdges    = true;

    // ─── ПРИВАТНЫЕ ПОЛЯ ───────────────────────────────────────────────────

    private Rigidbody       rb;
    private CapsuleCollider col;

    // Состояние (читается в Update, применяется в FixedUpdate)
    private Vector3 moveInput;
    private bool    jumpPressed;
    private bool    isGrounded;
    private bool    isNearEdge;

    // NonAlloc буферы (выделяются один раз)
    private readonly Collider[]   groundBuffer = new Collider[4];
    private readonly RaycastHit[] edgeBuffer   = new RaycastHit[2];

    // ─── ИНИЦИАЛИЗАЦИЯ ────────────────────────────────────────────────────

    void Awake()
    {
        rb  = GetComponent<Rigidbody>();
        col = GetComponent<CapsuleCollider>();
        SetupRigidbody();
    }

    void SetupRigidbody()
    {
        // TODO: Настройте Rigidbody
        // Подсказка: mass, linearDamping, angularDamping,
        //            constraints (не переворачиваться!),
        //            interpolation (для гладкого движения),
        //            collisionDetectionMode

        throw new System.NotImplementedException("Реализуйте SetupRigidbody");
    }

    // ─── ИГРОВОЙ ЦИКЛ ─────────────────────────────────────────────────────

    void Update()
    {
        ReadInput();
    }

    void FixedUpdate()
    {
        isGrounded = CheckGrounded();
        isNearEdge = stopAtEdges && CheckNearEdge();

        ApplyMovement();

        if (jumpPressed && isGrounded)
        {
            ApplyJump();
            jumpPressed = false;
        }
    }

    // ─── ВВОД ─────────────────────────────────────────────────────────────

    void ReadInput()
    {
        // TODO: Читайте ввод и сохраняйте в поля
        // Подсказка:
        // - Input.GetAxisRaw для движения (избегайте GetAxis — там сглаживание Unity)
        // - Input.GetKeyDown для прыжка (только в Update!)
        // - moveInput должен быть в мировом пространстве или локальном?

        throw new System.NotImplementedException("Реализуйте ReadInput");
    }

    // ─── ПРОВЕРКА ЗЕМЛИ ───────────────────────────────────────────────────

    bool CheckGrounded()
    {
        // TODO: Используйте OverlapSphereNonAlloc
        // Подсказка:
        // - Центр сферы: нижняя точка капсулы + небольшое смещение вниз
        // - Нижняя точка: transform.position - Vector3.up * (col.height/2 - col.radius)
        // - Используйте groundBuffer для NonAlloc
        // - Проверяйте только groundMask

        throw new System.NotImplementedException("Реализуйте CheckGrounded");
    }

    // ─── ОБНАРУЖЕНИЕ КРАЯ ─────────────────────────────────────────────────

    bool CheckNearEdge()
    {
        // TODO: Проверьте есть ли земля впереди персонажа
        // Подсказка:
        // - Найдите точку впереди персонажа: transform.position + transform.forward * edgeLookAhead
        // - Из этой точки кастуйте луч вниз на edgeRayDown
        // - Если земли нет — мы у края
        // - Учтите: только если персонаж движется вперёд (moveInput.magnitude > 0.1f)
        // - Используйте Physics.RaycastNonAlloc с edgeBuffer

        throw new System.NotImplementedException("Реализуйте CheckNearEdge");
    }

    // ─── ДВИЖЕНИЕ ─────────────────────────────────────────────────────────

    void ApplyMovement()
    {
        // TODO: Реализуйте физическое движение
        // Подсказка:
        // 1. Если isNearEdge и движемся к краю — тормозить, не ускорять
        // 2. Вычислить желаемую скорость: moveInput * maxSpeed
        // 3. Ограничить текущую горизонтальную скорость: rb.linearVelocity.x/z
        // 4. Если нет ввода — применить тормозящую силу (brakingForce)
        // 5. ForceMode.VelocityChange удобен для точного контроля скорости

        throw new System.NotImplementedException("Реализуйте ApplyMovement");
    }

    // ─── ПРЫЖОК ───────────────────────────────────────────────────────────

    void ApplyJump()
    {
        // TODO: Реализуйте прыжок
        // Подсказка:
        // - Сбросьте вертикальную скорость перед прыжком (для консистентности)
        // - rb.linearVelocity = new Vector3(rb.linearVelocity.x, 0f, rb.linearVelocity.z)
        // - Используйте ForceMode.VelocityChange (не зависит от массы)

        throw new System.NotImplementedException("Реализуйте ApplyJump");
    }

    // ─── ОТЛАДКА ──────────────────────────────────────────────────────────

    void OnDrawGizmosSelected()
    {
        if (col == null) col = GetComponent<CapsuleCollider>();

        // TODO: Визуализируйте:
        // 1. Зону GroundCheck (сфера) — зелёная если земля, красная если нет
        // 2. Луч EdgeCheck — синяя линия впереди и вниз
        // 3. Текущий moveInput вектор — жёлтая стрелка
    }
}
```

#### Ожидаемое поведение

1. Персонаж плавно ускоряется от WASD, тормозит при отпускании
2. Прыжок стабилен и одинаков независимо от FPS
3. На краю платформы персонаж замедляется и останавливается
4. Нет переворотов, нет дрожания при стоянии на месте
5. В Scene View видны Gizmos: зона GroundCheck, луч EdgeDetection

#### Критерии оценки



```csharp
✓ Отлично (90-100%):
  - Всё выше + Physics Material нулевого трения для персонажа
  - Coyote Time (250ms после края всё ещё можно прыгнуть)
  - Jump Buffer (нажатие Space за 150ms до земли засчитывается)
  - Разные значения gravity scale при подъёме и падении

✓ Хорошо (70-89%):
  - Базовый функционал работает без багов

✓ Удовлетворительно (50-69%):
  - Движение работает, мелкие баги (иногда прыжок на краю, редкое дрожание)

✗ Неудовлетворительно (<50%):
  - Physics в Update, нет GroundCheck, персонаж переворачивается
```

#### Типичные ошибки



```csharp
// ❌ ОШИБКА 1: Физика в Update
void Update()
{
    rb.AddForce(Vector3.forward * 10f); // Нестабильно!
}

// ✓ ИСПРАВЛЕНИЕ:
void FixedUpdate()
{
    rb.AddForce(Vector3.forward * 10f, ForceMode.Force);
}

// ❌ ОШИБКА 2: GetKeyDown в FixedUpdate
void FixedUpdate()
{
    if (Input.GetKeyDown(KeyCode.Space)) // Пропускает при высоком FPS!
        Jump();
}

// ✓ ИСПРАВЛЕНИЕ: флаг из Update
void Update()   { if (Input.GetKeyDown(KeyCode.Space)) jumpPressed = true; }
void FixedUpdate() { if (jumpPressed) { Jump(); jumpPressed = false; } }

// ❌ ОШИБКА 3: Неправильная позиция GroundCheck
bool CheckGrounded()
{
    // Проверяем центр объекта — сфера торчит из земли!
    return Physics.OverlapSphere(transform.position, 0.3f, groundMask).Length > 0;
}

// ✓ ИСПРАВЛЕНИЕ: проверяем нижнюю точку
bool CheckGrounded()
{
    Vector3 bottom = transform.position - Vector3.up * (col.height / 2f - col.radius + groundCheckOffset);
    int count = Physics.OverlapSphereNonAlloc(bottom, groundCheckRadius, groundBuffer, groundMask);
    return count > 0;
}

// ❌ ОШИБКА 4: Нет ограничения скорости
void ApplyMovement()
{
    rb.AddForce(moveInput * moveForce, ForceMode.Force);
    // Скорость растёт до бесконечности!
}

// ✓ ИСПРАВЛЕНИЕ:
void ApplyMovement()
{
    Vector3 currentHorizVel = new Vector3(rb.linearVelocity.x, 0f, rb.linearVelocity.z);
    if (currentHorizVel.magnitude < maxSpeed)
        rb.AddForce(moveInput * moveForce, ForceMode.Force);
}
```

---

### 🟡 Задание 2 (Средний): Система стрельбы

#### Условие

Реализуйте два подхода к стрельбе и сравните их:

**Подход A — Projectile:** физическая пуля с `Rigidbody`, летит по траектории, при столкновении наносит урон через `OnCollisionEnter`.

**Подход B — Hitscan:** мгновенный `Raycast`, попадание и урон в одном кадре, трассер через `LineRenderer`.

Система должна включать:

- Пул пуль (Object Pool) для Projectile
- `NonAlloc` Raycast для Hitscan
- Компонент `Health` с событием смерти
- Визуализацию траекторий и хитмарок
- Сравнительную статистику производительности

#### Стартовый скелет



```csharp
using UnityEngine;
using System.Collections;
using System.Collections.Generic;

// ─────────────────────────────────────────────────────────────────────────────
// КОМПОНЕНТ ЗДОРОВЬЯ
// ─────────────────────────────────────────────────────────────────────────────
public class Health : MonoBehaviour
{
    [SerializeField] private float maxHealth = 100f;

    private float currentHealth;

    public event System.Action<float, float> OnHealthChanged; // current, max
    public event System.Action               OnDeath;

    public float Current => currentHealth;
    public float Max     => maxHealth;
    public bool  IsDead  => currentHealth <= 0f;

    void Awake()
    {
        currentHealth = maxHealth;
    }

    public void TakeDamage(float damage)
    {
        if (IsDead) return;

        // TODO: Реализуйте получение урона
        // 1. Уменьшить currentHealth (но не ниже 0)
        // 2. Вызвать OnHealthChanged
        // 3. Если currentHealth <= 0 — вызвать Die()

        throw new System.NotImplementedException("Реализуйте TakeDamage");
    }

    void Die()
    {
        // TODO: Реализуйте смерть
        // 1. Вызвать OnDeath
        // 2. Можно: Destroy с задержкой, отключить коллайдер, сыграть анимацию

        throw new System.NotImplementedException("Реализуйте Die");
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// ФИЗИЧЕСКАЯ ПУЛЯ
// ─────────────────────────────────────────────────────────────────────────────
[RequireComponent(typeof(Rigidbody))]
[RequireComponent(typeof(SphereCollider))]
public class Projectile : MonoBehaviour
{
    [Header("Settings")]
    [SerializeField] private float  damage    = 25f;
    [SerializeField] private float  lifetime  = 5f;
    [SerializeField] private bool   useGravity = false; // Баллистика?

    [Header("Effects")]
    [SerializeField] private GameObject hitEffectPrefab;
    [SerializeField] private TrailRenderer trail;

    private Rigidbody  rb;
    private float      timer;
    private ObjectPool<Projectile> ownerPool; // Ссылка на пул для возврата

    void Awake()
    {
        rb = GetComponent<Rigidbody>();

        // TODO: Настройте Rigidbody для пули
        // Подсказка:
        // - ContinuousDynamic collision detection (высокая скорость!)
        // - useGravity = this.useGravity
        // - Небольшая масса (0.01f)
        // - maxLinearVelocity для защиты от tunneling

        throw new System.NotImplementedException("Настройте Rigidbody в Awake");
    }

    // Вызывается при взятии из пула
    public void Launch(Vector3 position, Vector3 direction, float speed,
                       ObjectPool<Projectile> pool)
    {
        ownerPool = pool;
        timer     = 0f;

        transform.position = position;
        transform.rotation = Quaternion.LookRotation(direction);

        // TODO: Применить скорость
        // Подсказка: rb.linearVelocity = direction * speed

        if (trail != null) trail.Clear();

        throw new System.NotImplementedException("Реализуйте Launch");
    }

    void Update()
    {
        // TODO: Логика времени жизни
        // После lifetime секунд — вернуть в пул

        throw new System.NotImplementedException("Реализуйте Update");
    }

    void OnCollisionEnter(Collision collision)
    {
        // TODO: Обработка попадания
        // 1. Проверить, есть ли Health у цели
        // 2. Нанести урон
        // 3. Создать эффект попадания в collision.contacts[0].point
        // 4. Вернуть в пул

        throw new System.NotImplementedException("Реализуйте OnCollisionEnter");
    }

    void ReturnToPool()
    {
        // TODO: Вернуть в пул или уничтожить если пула нет
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// ПРОСТОЙ OBJECT POOL
// ─────────────────────────────────────────────────────────────────────────────
public class ObjectPool<T> where T : Component
{
    private readonly Queue<T>    pool;
    private readonly T           prefab;
    private readonly Transform   parent;

    public int ActiveCount   { get; private set; }
    public int InactiveCount => pool.Count;

    public ObjectPool(T prefab, int initialSize, Transform parent = null)
    {
        this.prefab = prefab;
        this.parent = parent;
        pool        = new Queue<T>(initialSize);

        // TODO: Создать initialSize экземпляров
        // Подсказка: Instantiate, SetActive(false), Enqueue

        throw new System.NotImplementedException("Реализуйте конструктор ObjectPool");
    }

    public T Get()
    {
        // TODO: Взять из очереди или создать новый если пустой
        // SetActive(true), ActiveCount++

        throw new System.NotImplementedException("Реализуйте Get");
    }

    public void Return(T item)
    {
        // TODO: Вернуть в очередь
        // SetActive(false), ActiveCount--

        throw new System.NotImplementedException("Реализуйте Return");
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// СИСТЕМА ОРУЖИЯ
// ─────────────────────────────────────────────────────────────────────────────
public class WeaponSystem : MonoBehaviour
{
    [Header("Shared")]
    [SerializeField] private Transform     firePoint;
    [SerializeField] private Camera        playerCamera;
    [SerializeField] private GameObject    hitEffectPrefab;
    [SerializeField] private AudioSource   audioSource;

    [Header("Projectile")]
    [SerializeField] private Projectile projectilePrefab;
    [SerializeField] private float      projectileSpeed  = 30f;
    [SerializeField] private int        poolInitialSize  = 20;
    [SerializeField] private AudioClip  projectileSound;

    [Header("Hitscan")]
    [SerializeField] private float     hitscanRange   = 100f;
    [SerializeField] private float     hitscanDamage  = 40f;
    [SerializeField] private LayerMask hitscanMask;
    [SerializeField] private AudioClip hitscanSound;

    [Header("Hitscan Visual")]
    [SerializeField] private LineRenderer   tracerRenderer;
    [SerializeField] private float          tracerDuration = 0.05f;

    // ─── СОСТОЯНИЕ ────────────────────────────────────────────────────────

    private ObjectPool<Projectile> bulletPool;
    private readonly RaycastHit[]  hitBuffer = new RaycastHit[5];

    // Статистика для сравнения
    private int   projectileShotCount;
    private int   hitscanShotCount;
    private float projectileTotalTime;
    private float hitscanTotalTime;

    // ─── ИНИЦИАЛИЗАЦИЯ ────────────────────────────────────────────────────

    void Start()
    {
        bulletPool = new ObjectPool<Projectile>(
            projectilePrefab, poolInitialSize, transform);

        if (tracerRenderer != null)
            tracerRenderer.enabled = false;
    }

    // ─── ВВОД ─────────────────────────────────────────────────────────────

    void Update()
    {
        if (Input.GetMouseButtonDown(0)) ShootProjectile();
        if (Input.GetMouseButtonDown(1)) ShootHitscan();
    }

    // ─── СТРЕЛЬБА: PROJECTILE ─────────────────────────────────────────────

    void ShootProjectile()
    {
        float startTime = Time.realtimeSinceStartup;

        // TODO: Реализуйте стрельбу физической пулей
        // 1. Вычислить направление (из камеры через центр экрана)
        //    Подсказка: Ray ray = playerCamera.ViewportPointToRay(new Vector3(0.5f, 0.5f, 0))
        // 2. Получить пулю: bulletPool.Get()
        // 3. Вызвать bullet.Launch(...)
        // 4. Сыграть звук
        // 5. Обновить статистику

        projectileShotCount++;
        projectileTotalTime += Time.realtimeSinceStartup - startTime;

        throw new System.NotImplementedException("Реализуйте ShootProjectile");
    }

    // ─── СТРЕЛЬБА: HITSCAN ────────────────────────────────────────────────

    void ShootHitscan()
    {
        float startTime = Time.realtimeSinceStartup;

        // TODO: Реализуйте мгновенную стрельбу
        // 1. Raycast из центра камеры
        //    Используйте NonAlloc: Physics.RaycastNonAlloc(..., hitBuffer, ...)
        // 2. При попадании:
        //    a. TakeDamage на Health если есть
        //    b. Создать hitEffectPrefab в точке попадания
        //    c. Повернуть эффект по нормали: Quaternion.LookRotation(hit.normal)
        // 3. Показать трассер через StartCoroutine(ShowTracer(...))
        // 4. Сыграть звук
        // 5. Обновить статистику

        hitscanShotCount++;
        hitscanTotalTime += Time.realtimeSinceStartup - startTime;

        throw new System.NotImplementedException("Реализуйте ShootHitscan");
    }

    // ─── ТРАССЕР ──────────────────────────────────────────────────────────

    IEnumerator ShowTracer(Vector3 startPos, Vector3 endPos)
    {
        // TODO: Показать LineRenderer на tracerDuration секунд
        // 1. tracerRenderer.enabled = true
        // 2. Установить позиции: SetPosition(0, startPos), SetPosition(1, endPos)
        // 3. yield return new WaitForSeconds(tracerDuration)
        // 4. tracerRenderer.enabled = false

        throw new System.NotImplementedException("Реализуйте ShowTracer");
    }

    // ─── СТАТИСТИКА ───────────────────────────────────────────────────────

    [ConMenu("Print Comparison Stats")]
    void PrintStats()
    {
        Debug.Log("═══ СРАВНЕНИЕ ПОДХОДОВ ═══");

        if (projectileShotCount > 0)
        {
            float avgMs = (projectileTotalTime / projectileShotCount) * 1000f;
            Debug.Log($"Projectile: {projectileShotCount} выстрелов, " +
                      $"среднее время вызова: {avgMs:F4} мс, " +
                      $"активных пуль: {bulletPool.ActiveCount}");
        }

        if (hitscanShotCount > 0)
        {
            float avgMs = (hitscanTotalTime / hitscanShotCount) * 1000f;
            Debug.Log($"Hitscan:    {hitscanShotCount} выстрелов, " +
                      $"среднее время вызова: {avgMs:F4} мс");
        }

        // TODO: Добавьте сравнение и вывод выводов
    }
}
```

#### Ожидаемое поведение

1. ЛКМ — физическая пуля летит и падает (гравитация), бьёт в точке контакта
2. ПКМ — мгновенное попадание, виден трассер
3. При попадании в врага — урон, смерть после 0HP
4. Пул работает: старые пули переиспользуются, не создаются заново
5. Статистика показывает разницу в скорости выполнения

#### Критерии оценки



```csharp
✓ Отлично (90-100%):
  - Оба подхода работают корректно
  - Пул без утечек памяти
  - Hitscan учитывает несколько попаданий (RaycastAll через укрытия)
  - Разброс (spread/bloom) для обоих типов
  - Правильная статистика с интерпретацией

✓ Хорошо (70-89%):
  - Оба подхода работают, пул функционирует

✓ Удовлетворительно (50-69%):
  - Один подход работает корректно

✗ Неудовлетворительно (<50%):
  - Нет пула, Raycast без NonAlloc, нет урона
```

#### Сравнительный анализ: Projectile vs Hitscan



```csharp
Характеристика     │ Projectile              │ Hitscan
───────────────────┼─────────────────────────┼──────────────────────────
Точность           │ Зависит от физики        │ 100% точный в момент
Задержка           │ Время полёта            │ Мгновенно
Баллистика         │ ✓ Реальная траектория    │ ✗ Только прямая линия
Производительность │ Каждая пуля = Rigidbody  │ Один Raycast за выстрел
Сеть               │ Сложно синхронизировать │ Легко (точка + направление)
Применение         │ RPG, медленные снаряды  │ Снайперки, пистолеты, дробь
```

---

### 🔴 Задание 3 (Продвинутый): Разрушаемый мост

#### Условие

Создайте мост из блоков на `HingeJoint`, который:

- Состоит из N деревянных блоков, соединённых `HingeJoint`
- Реагирует на вес персонажа — прогибается
- При достаточной нагрузке блоки "ломаются" (joint отключается)
- Сломанные блоки падают с физикой
- Мост правильно инициализируется через код (без ручной расстановки)
- Поддерживает восстановление (Reset)

#### Стартовый скелет



```csharp
using UnityEngine;
using System.Collections.Generic;

// ─────────────────────────────────────────────────────────────────────────────
// БЛОК МОСТА
// ─────────────────────────────────────────────────────────────────────────────
[RequireComponent(typeof(Rigidbody))]
[RequireComponent(typeof(BoxCollider))]
public class BridgePlank : MonoBehaviour
{
    [Header("Break Settings")]
    [SerializeField] private float maxJointForce  = 500f;   // При каком усилии ломается
    [SerializeField] private float breakCooldown  = 0.5f;   // Задержка перед проломом

    [Header("Visual Feedback")]
    [SerializeField] private Renderer plankRenderer;
    [SerializeField] private Color    intactColor  = new Color(0.6f, 0.3f, 0.1f);
    [SerializeField] private Color    stressedColor = Color.red;
    [SerializeField] private Color    brokenColor  = Color.black;

    // ─── СОСТОЯНИЕ ────────────────────────────────────────────────────────

    private HingeJoint hingeLeft;
    private HingeJoint hingeRight;
    private Rigidbody  rb;
    private bool       isBroken;
    private float      stressLevel; // [0, 1]

    // Сохранённые данные для Reset
    private Vector3    initialPosition;
    private Quaternion initialRotation;
    private bool       wasKinematic;

    // ─── СОБЫТИЯ ──────────────────────────────────────────────────────────

    public event System.Action<BridgePlank> OnPlaneBroken;

    // ─── ИНИЦИАЛИЗАЦИЯ ────────────────────────────────────────────────────

    void Awake()
    {
        rb = GetComponent<Rigidbody>();
        plankRenderer = GetComponent<Renderer>();

        initialPosition = transform.position;
        initialRotation = transform.rotation;
    }

    // Вызывается мостом при создании
    public void Initialize(float mass, float jointSpring, float jointDamper,
                           float maxBreakForce)
    {
        // TODO: Настройте Rigidbody планки
        // - Масса (передаётся как параметр)
        // - Drag, angular drag для стабильности
        // - Interpolation для визуальной гладкости
        // - Constraints (какое вращение разрешено для планки моста?)

        this.maxJointForce = maxBreakForce;

        if (plankRenderer != null)
            plankRenderer.material.color = intactColor;

        throw new System.NotImplementedException("Реализуйте Initialize");
    }

    // ─── JOINTS ───────────────────────────────────────────────────────────

    public HingeJoint AddHingeLeft(Rigidbody connectedBody)
    {
        // TODO: Создайте HingeJoint для левого соединения
        // Подсказка:
        // - Добавьте HingeJoint компонент
        // - connectedBody = передан параметром (или null = мировая точка)
        // - Ось вращения: Vector3.forward (мост качается вверх-вниз)
        // - Якорь: левый край планки (-0.5f по X)
        // - Добавьте spring для возврата в горизонталь
        // - Сохраните ссылку в hingeLeft

        throw new System.NotImplementedException("Реализуйте AddHingeLeft");
    }

    public HingeJoint AddHingeRight(Rigidbody connectedBody)
    {
        // TODO: Аналогично для правой стороны
        // Якорь: правый край (+0.5f по X)

        throw new System.NotImplementedException("Реализуйте AddHingeRight");
    }

    // ─── ОБНОВЛЕНИЕ ───────────────────────────────────────────────────────

    void FixedUpdate()
    {
        if (isBroken) return;

        CheckJointStress();
        UpdateVisuals();
    }

    void CheckJointStress()
    {
        // TODO: Проверить нагрузку на joints
        // Подсказка:
        // - currentForce = hingeLeft?.currentForce.magnitude + hingeRight?.currentForce.magnitude
        // - stressLevel = currentForce / maxJointForce (Clamp01)
        // - Если stressLevel >= 1f — вызвать Break()

        throw new System.NotImplementedException("Реализуйте CheckJointStress");
    }

    void UpdateVisuals()
    {
        // TODO: Изменить цвет планки на основе stressLevel
        // Color.Lerp(intactColor, stressedColor, stressLevel)
        // При isBroken — brokenColor

        throw new System.NotImplementedException("Реализуйте UpdateVisuals");
    }

    // ─── РАЗРУШЕНИЕ ───────────────────────────────────────────────────────

    public void Break()
    {
        if (isBroken) return;
        isBroken = true;

        // TODO: Сломайте планку
        // 1. Destroy(hingeLeft) — отсоединить от левого соседа
        // 2. Destroy(hingeRight) — отсоединить от правого соседа
        // 3. Сделать кинематику = false (если была) — планка падает!
        // 4. Добавить взрывной импульс для эффектности
        //    rb.AddExplosionForce(500f, transform.position, 2f)
        // 5. Изменить цвет на brokenColor
        // 6. Вызвать OnPlaneBroken?

        throw new System.NotImplementedException("Реализуйте Break");
    }

    // ─── СБРОС ────────────────────────────────────────────────────────────

    public void ResetPlank()
    {
        // TODO: Восстановить планку в исходное состояние
        // 1. Восстановить позицию и вращение
        // 2. Сбросить скорость (velocity, angularVelocity)
        // 3. isBroken = false
        // 4. stressLevel = 0f
        // 5. Восстановить цвет
        // Joints пересоздаются мостом!

        throw new System.NotImplementedException("Реализуйте ResetPlank");
    }

    public bool IsBroken => isBroken;

    void OnDrawGizmosSelected()
    {
        if (isBroken) return;

        // Visualize stress as color
        Gizmos.color = Color.Lerp(Color.green, Color.red, stressLevel);
        Gizmos.DrawWireCube(transform.position, transform.localScale * 1.1f);
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// СТРОИТЕЛЬ МОСТА
// ─────────────────────────────────────────────────────────────────────────────
public class DestructibleBridge : MonoBehaviour
{
    [Header("Bridge Structure")]
    [SerializeField] private BridgePlank plankPrefab;
    [SerializeField] private int         plankCount   = 10;
    [SerializeField] private float       plankWidth   = 1f;
    [SerializeField] private float       plankHeight  = 0.2f;
    [SerializeField] private float       plankDepth   = 2f;
    [SerializeField] private float       gapBetween   = 0.05f;

    [Header("Physics")]
    [SerializeField] private float       plankMass       = 5f;
    [SerializeField] private float       jointSpring     = 200f;
    [SerializeField] private float       jointDamper     = 20f;
    [SerializeField] private float       breakForce      = 800f;

    [Header("Anchors")]
    [SerializeField] private Transform   leftAnchor;   // Левая опора моста
    [SerializeField] private Transform   rightAnchor;  // Правая опора моста

    // ─── СОСТОЯНИЕ ────────────────────────────────────────────────────────

    private List<BridgePlank> planks = new List<BridgePlank>();
    private int               brokenCount;

    // ─── ИНИЦИАЛИЗАЦИЯ ────────────────────────────────────────────────────

    void Start()
    {
        BuildBridge();
    }

    [ConMenu("Build Bridge")]
    public void BuildBridge()
    {
        ClearBridge();

        // TODO: Постройте мост из планок
        // Алгоритм:
        // 1. Вычислить общую длину: plankCount * (plankWidth + gapBetween)
        // 2. Стартовая позиция: leftAnchor.position или transform.position - halfLength
        // 3. Для каждой планки:
        //    a. Instantiate plankPrefab
        //    b. Позиционировать: x = startX + i * (plankWidth + gapBetween)
        //    c. Установить localScale для размера
        //    d. plank.Initialize(plankMass, jointSpring, jointDamper, breakForce)
        //    e. Добавить в список
        // 4. Соединить планки HingeJoint:
        //    - Планка 0: hingeLeft → leftAnchor Rigidbody (или null)
        //    - Планка i: hingeLeft → planks[i-1].Rigidbody
        //    - Планка i: hingeRight → planks[i+1].Rigidbody (если есть)
        //    - Последняя планка: hingeRight → rightAnchor Rigidbody (или null)
        // 5. Подписаться на plank.OnPlaneBroken

        throw new System.NotImplementedException("Реализуйте BuildBridge");
    }

    void ClearBridge()
    {
        // TODO: Уничтожить все планки и очистить список

        foreach (var plank in planks)
        {
            if (plank != null)
                Destroy(plank.gameObject);
        }

        planks.Clear();
        brokenCount = 0;
    }

    // ─── ОБРАБОТКА СОБЫТИЙ ────────────────────────────────────────────────

    void OnPlankBroken(BridgePlank plank)
    {
        // TODO: Реагировать на слом планки
        // 1. brokenCount++
        // 2. Эффекты (звук, частицы)
        // 3. Если все сломаны — событие "мост разрушен"

        brokenCount++;
        Debug.Log($"Планка сломана! Сломано {brokenCount}/{plankCount}");
    }

    // ─── СБРОС ────────────────────────────────────────────────────────────

    [ConMenu("Reset Bridge")]
    public void ResetBridge()
    {
        // TODO: Восстановить мост
        // Вариант А: ResetPlank() на каждой + пересоздать joints
        // Вариант Б: ClearBridge() + BuildBridge() (проще, но медленнее)

        throw new System.NotImplementedException("Реализуйте ResetBridge");
    }

    // ─── ОТЛАДКА ──────────────────────────────────────────────────────────

    void OnDrawGizmos()
    {
        if (planks == null || planks.Count == 0) return;

        // TODO: Нарисуйте соединения между планками
        Gizmos.color = Color.cyan;
        for (int i = 0; i < planks.Count - 1; i++)
        {
            if (planks[i] == null || planks[i + 1] == null) continue;
            if (planks[i].IsBroken || planks[i + 1].IsBroken)
            {
                Gizmos.color = Color.red;
            }
            else
            {
                Gizmos.color = Color.cyan;
            }
            Gizmos.DrawLine(planks[i].transform.position,
                            planks[i + 1].transform.position);
        }
    }
}
```

#### Ожидаемое поведение

1. Мост строится из N планок при старте сцены
2. При заходе персонажа — мост прогибается
3. Цвет планок меняется от зелёного к красному при нагрузке
4. При критической нагрузке планка "ломается" и падает
5. Цепная реакция: соседние планки теряют опору и тоже могут сломаться
6. `ResetBridge()` полностью восстанавливает мост
7. В Scene View видны соединения Gizmos

#### Критерии оценки


```csharp
✓ Отлично (90-100%):
  - Всё выше + процедурное создание якорей (без ручного размещения)
  - Звуки: скрип при нагрузке (pitch от stress), треск при разрушении
  - LOD: дальние планки имеют Discrete collision detection
  - Сохранение/загрузка состояния моста через ScriptableObject
  - UI: полоска "здоровья моста" сверху экрана

✓ Хорошо (70-89%):
  - Мост строится, реагирует на вес, ломается, сбрасывается

✓ Удовлетворительно (50-69%):
  - Мост строится и ломается, но без цветовой индикации или Reset

✗ Неудовлетворительно (<50%):
  - Мост нестабилен, joints не работают, нет разрушения
```

#### Типичные ошибки в задании 3


```csharp
// ❌ ОШИБКА 1: Неправильное направление оси HingeJoint
// Мост должен качаться вверх-вниз (вокруг оси Z если мост по X)
hinge.axis = Vector3.up; // Это вращение в плоскости — мост крутится!

// ✓ ИСПРАВЛЕНИЕ:
hinge.axis = Vector3.forward; // Вращение вокруг Z — правильный прогиб

// ❌ ОШИБКА 2: anchor в мировых координатах вместо локальных
hinge.anchor = planks[i - 1].transform.position; // МИРОВЫЕ! Неверно

// ✓ ИСПРАВЛЕНИЕ:
hinge.anchor = new Vector3(-0.5f, 0f, 0f); // ЛОКАЛЬНЫЕ! Левый край планки

// ❌ ОШИБКА 3: Слишком маленький breakForce → мост рассыпается сразу
hinge.breakForce = 10f; // Рассыпается от собственного веса!

// ✓ ИСПРАВЛЕНИЕ: Рассчитайте исходя из масс
float weight = plankMass * Physics.gravity.magnitude; // Вес одной планки
hinge.breakForce = weight * 5f; // Выдерживает 5 собственных масс

// ❌ ОШИБКА 4: Нет sleep prevention при нагрузке
// Планки засыпают и не реагируют на персонажа!
// ✓ ИСПРАВЛЕНИЕ: Physics Material без bounce + достаточный drag
// ИЛИ: wake up планки при обнаружении коллизии с персонажем

// ❌ ОШИБКА 5: Joints создаются на уже спящих телах
// После Instantiate дайте физике один кадр:
// ✓ ИСПРАВЛЕНИЕ: BuildBridge через корутину
IEnumerator BuildBridgeCoroutine()
{
    CreateAllPlanks();
    yield return new WaitForFixedUpdate(); // Физика инициализирует тела
    ConnectWithJoints();                   // Теперь joints стабильны
}
```

---

## 13. Чеклист компетенций {#чеклист}

Используйте этот чеклист для самооценки. Будьте честны — это ваш инструмент, а не тест для галочки.

### Уровень 1: Основы (Junior)



```csharp
□ Понимаю разницу между PhysX (3D) и Box2D (2D)
□ Знаю, что 3D и 2D физика полностью изолированы
□ Могу объяснить, почему физику нужно делать в FixedUpdate
□ Знаю все параметры Rigidbody: mass, drag, constraints, interpolation
□ Понимаю ForceMode: Force, Acceleration, Impulse, VelocityChange
□ Умею настраивать GroundCheck через OverlapSphereNonAlloc
□ Знаю разницу между Trigger и Collider
□ Понимаю таблицу: когда вызываются OnTrigger* и OnCollision*
□ Умею читать ввод в Update, применять физику в FixedUpdate
□ Могу объяснить Interpolation: None, Interpolate, Extrapolate
```

### Уровень 2: Уверенный разработчик (Middle)



```csharp
□ Понимаю pipeline PhysX: Broad Phase → Narrow Phase → Solver → Integration
□ Знаю алгоритмы SAP, GJK, EPA на концептуальном уровне
□ Могу выбрать правильный Collision Detection Mode для объекта
□ Знаю стоимость коллайдеров: Sphere < Capsule < Box < Mesh
□ Умею создавать Compound Colliders через иерархию объектов
□ Использую NonAlloc версии всех физических запросов
□ Понимаю Layer Collision Matrix и умею настраивать через код
□ Могу настроить HingeJoint, SpringJoint с правильными параметрами
□ Знаю Physics Settings: sleepThreshold, bounceThreshold, solverIterations
□ Реализую Object Pool для физических объектов
□ Понимаю масштаб сцены и его влияние на физику
□ Умею диагностировать tunneling и jitter
```

### Уровень 3: Эксперт (Senior)



```csharp
□ Могу объяснить semi-implicit Euler integration и его преимущества
□ Знаю Warm Starting в Box2D и зачем он нужен
□ Умею настраивать ConfigurableJoint с Drive для сложных механизмов
□ Реализую Floating Origin для больших открытых миров
□ Профилирую физику через Physics Profiler и устраняю узкие места
□ Понимаю критическую скорость tunneling: v = size / fixedDeltaTime
□ Реализую ручной анти-tunneling через SphereCast для критичных объектов
□ Знаю влияние solverIterations на стабильность стеков и joints
□ Умею выбирать fixedDeltaTime для платформы (PC / Mobile / VR)
□ Проектирую физические системы с учётом sleeping и culling
□ Понимаю CCD: swept volume vs speculative contact
□ Реализую детерминированные физические системы для мультиплеера
```

