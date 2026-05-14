# ScriptableObjects: от данных к архитектуре

### Полное руководство для Unity-разработчика

---

> _«Мой проект работает, но я боюсь его трогать»_ — каждый разработчик, написавший достаточно кода.

---

# Содержание

- [1. Введение: анатомия спагетти-проекта](#1.%20%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5:%20%D0%B0%D0%BD%D0%B0%D1%82%D0%BE%D0%BC%D0%B8%D1%8F%20%D1%81%D0%BF%D0%B0%D0%B3%D0%B5%D1%82%D1%82%D0%B8-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
	- [Как это начинается](#%D0%9A%D0%B0%D0%BA%20%D1%8D%D1%82%D0%BE%20%D0%BD%D0%B0%D1%87%D0%B8%D0%BD%D0%B0%D0%B5%D1%82%D1%81%D1%8F)
	- [Что происходит с таким кодом](#%D0%A7%D1%82%D0%BE%20%D0%BF%D1%80%D0%BE%D0%B8%D1%81%D1%85%D0%BE%D0%B4%D0%B8%D1%82%20%D1%81%20%D1%82%D0%B0%D0%BA%D0%B8%D0%BC%20%D0%BA%D0%BE%D0%B4%D0%BE%D0%BC)
	- [Что предлагает эта статья](#%D0%A7%D1%82%D0%BE%20%D0%BF%D1%80%D0%B5%D0%B4%D0%BB%D0%B0%D0%B3%D0%B0%D0%B5%D1%82%20%D1%8D%D1%82%D0%B0%20%D1%81%D1%82%D0%B0%D1%82%D1%8C%D1%8F)
- [2. Что такое ScriptableObject](#2.%20%D0%A7%D1%82%D0%BE%20%D1%82%D0%B0%D0%BA%D0%BE%D0%B5%20ScriptableObject)
	- [Иерархия типов Unity](#%D0%98%D0%B5%D1%80%D0%B0%D1%80%D1%85%D0%B8%D1%8F%20%D1%82%D0%B8%D0%BF%D0%BE%D0%B2%20Unity)
	- [Ключевые отличия от MonoBehaviour](#%D0%9A%D0%BB%D1%8E%D1%87%D0%B5%D0%B2%D1%8B%D0%B5%20%D0%BE%D1%82%D0%BB%D0%B8%D1%87%D0%B8%D1%8F%20%D0%BE%D1%82%20MonoBehaviour)
	- [Почему «одна копия данных» — это важно](#%D0%9F%D0%BE%D1%87%D0%B5%D0%BC%D1%83%20%C2%AB%D0%BE%D0%B4%D0%BD%D0%B0%20%D0%BA%D0%BE%D0%BF%D0%B8%D1%8F%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85%C2%BB%20%E2%80%94%20%D1%8D%D1%82%D0%BE%20%D0%B2%D0%B0%D0%B6%D0%BD%D0%BE)
- [3. Жизненный цикл ScriptableObject](#3.%20%D0%96%D0%B8%D0%B7%D0%BD%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9%20%D1%86%D0%B8%D0%BA%D0%BB%20ScriptableObject)
	- [Полная схема жизненного цикла](#%D0%9F%D0%BE%D0%BB%D0%BD%D0%B0%D1%8F%20%D1%81%D1%85%D0%B5%D0%BC%D0%B0%20%D0%B6%D0%B8%D0%B7%D0%BD%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE%20%D1%86%D0%B8%D0%BA%D0%BB%D0%B0)
	- [OnEnable — правильное место для инициализации](#OnEnable%20%E2%80%94%20%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5%20%D0%BC%D0%B5%D1%81%D1%82%D0%BE%20%D0%B4%D0%BB%D1%8F%20%D0%B8%D0%BD%D0%B8%D1%86%D0%B8%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8)
	- [OnDisable — обязательная очистка](#OnDisable%20%E2%80%94%20%D0%BE%D0%B1%D1%8F%D0%B7%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%BE%D1%87%D0%B8%D1%81%D1%82%D0%BA%D0%B0)
	- [OnValidate — валидация и живые вычисления](#OnValidate%20%E2%80%94%20%D0%B2%D0%B0%D0%BB%D0%B8%D0%B4%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B8%20%D0%B6%D0%B8%D0%B2%D1%8B%D0%B5%20%D0%B2%D1%8B%D1%87%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F)
- [4. Создание и организация](#4.%20%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%B8%20%D0%BE%D1%80%D0%B3%D0%B0%D0%BD%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F)
	- [Создание через код (для инструментов и тестов)](#%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20%D0%BA%D0%BE%D0%B4%20(%D0%B4%D0%BB%D1%8F%20%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2%20%D0%B8%20%D1%82%D0%B5%D1%81%D1%82%D0%BE%D0%B2))
	- [Рекомендуемая структура папок](#%D0%A0%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D1%83%D0%B5%D0%BC%D0%B0%D1%8F%20%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D0%BF%D0%B0%D0%BF%D0%BE%D0%BA)
- [5. Архитектурные паттерны](#5.%20%D0%90%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D0%BD%D1%8B%D0%B5%20%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%D1%8B)
	- [5.1 Data Container](#5.1%20Data%20Container)
	- [5.2 Event System на ScriptableObjects](#5.2%20Event%20System%20%D0%BD%D0%B0%20ScriptableObjects)
	- [5.3 Runtime Variables — глобальное состояние без Singleton](#5.3%20Runtime%20Variables%20%E2%80%94%20%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5%20%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D0%B5%20%D0%B1%D0%B5%D0%B7%20Singleton)
	- [5.4 State Machine на ScriptableObjects](#5.4%20State%20Machine%20%D0%BD%D0%B0%20ScriptableObjects)
- [6. SO как замена Singleton](#6.%20SO%20%D0%BA%D0%B0%D0%BA%20%D0%B7%D0%B0%D0%BC%D0%B5%D0%BD%D0%B0%20Singleton)
	- [Почему Singleton — проблема](#%D0%9F%D0%BE%D1%87%D0%B5%D0%BC%D1%83%20Singleton%20%E2%80%94%20%D0%BF%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0)
	- [Замена через SO Runtime Variables](#%D0%97%D0%B0%D0%BC%D0%B5%D0%BD%D0%B0%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20SO%20Runtime%20Variables)
	- [Сравнение подходов к глобальному состоянию](#%D0%A1%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BF%D0%BE%D0%B4%D1%85%D0%BE%D0%B4%D0%BE%D0%B2%20%D0%BA%20%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%BC%D1%83%20%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8E)
- [7. Вложенные SO и базы данных](#7.%20%D0%92%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5%20SO%20%D0%B8%20%D0%B1%D0%B0%D0%B7%D1%8B%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)
	- [Ссылки между SO](#%D0%A1%D1%81%D1%8B%D0%BB%D0%BA%D0%B8%20%D0%BC%D0%B5%D0%B6%D0%B4%D1%83%20SO)
	- [Защита от циклических ссылок](#%D0%97%D0%B0%D1%89%D0%B8%D1%82%D0%B0%20%D0%BE%D1%82%20%D1%86%D0%B8%D0%BA%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D1%85%20%D1%81%D1%81%D1%8B%D0%BB%D0%BE%D0%BA)
- [8. SO vs JSON vs PlayerPrefs](#8.%20SO%20vs%20JSON%20vs%20PlayerPrefs)
	- [Полная сравнительная таблица](#%D0%9F%D0%BE%D0%BB%D0%BD%D0%B0%D1%8F%20%D1%81%D1%80%D0%B0%D0%B2%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0)
	- [Дерево принятия решений](#%D0%94%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%20%D0%BF%D1%80%D0%B8%D0%BD%D1%8F%D1%82%D0%B8%D1%8F%20%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D0%B9)
	- [Когда что использовать — конкретные примеры](#%D0%9A%D0%BE%D0%B3%D0%B4%D0%B0%20%D1%87%D1%82%D0%BE%20%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%20%E2%80%94%20%D0%BA%D0%BE%D0%BD%D0%BA%D1%80%D0%B5%D1%82%D0%BD%D1%8B%D0%B5%20%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B)
- [9. Ограничения и подводные камни](#9.%20%D0%9E%D0%B3%D1%80%D0%B0%D0%BD%D0%B8%D1%87%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B8%20%D0%BF%D0%BE%D0%B4%D0%B2%D0%BE%D0%B4%D0%BD%D1%8B%D0%B5%20%D0%BA%D0%B0%D0%BC%D0%BD%D0%B8)
	- [SO не для сохранения состояния](#SO%20%D0%BD%D0%B5%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%BE%D1%85%D1%80%D0%B0%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F%20%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F)
	- [Паттерн защитной копии](#%D0%9F%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%20%D0%B7%D0%B0%D1%89%D0%B8%D1%82%D0%BD%D0%BE%D0%B9%20%D0%BA%D0%BE%D0%BF%D0%B8%D0%B8)
	- [SO и сборка проекта](#SO%20%D0%B8%20%D1%81%D0%B1%D0%BE%D1%80%D0%BA%D0%B0%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
- [10. Антипаттерны: как НЕ надо использовать SO](#10.%20%D0%90%D0%BD%D1%82%D0%B8%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%D1%8B:%20%D0%BA%D0%B0%D0%BA%20%D0%9D%D0%95%20%D0%BD%D0%B0%D0%B4%D0%BE%20%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%20SO)
	- [❌ Антипаттерн 1: Мутирующий SO (Mutable ScriptableObject)](#%E2%9D%8C%20%D0%90%D0%BD%D1%82%D0%B8%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%201:%20%D0%9C%D1%83%D1%82%D0%B8%D1%80%D1%83%D1%8E%D1%89%D0%B8%D0%B9%20SO%20(Mutable%20ScriptableObject))
	- [❌ Антипаттерн 2: Ghost Callbacks (Забытая отписка)](#%E2%9D%8C%20%D0%90%D0%BD%D1%82%D0%B8%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%202:%20Ghost%20Callbacks%20(%D0%97%D0%B0%D0%B1%D1%8B%D1%82%D0%B0%D1%8F%20%D0%BE%D1%82%D0%BF%D0%B8%D1%81%D0%BA%D0%B0))
	- [❌ Антипаттерн 3: SO как Singleton «через чёрный ход»](#%E2%9D%8C%20%D0%90%D0%BD%D1%82%D0%B8%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%203:%20SO%20%D0%BA%D0%B0%D0%BA%20Singleton%20%C2%AB%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20%D1%87%D1%91%D1%80%D0%BD%D1%8B%D0%B9%20%D1%85%D0%BE%D0%B4%C2%BB)
	- [❌ Антипаттерн 4: Рантайм-данные в SO при нескольких экземплярах](#%E2%9D%8C%20%D0%90%D0%BD%D1%82%D0%B8%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%204:%20%D0%A0%D0%B0%D0%BD%D1%82%D0%B0%D0%B9%D0%BC-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D0%B2%20SO%20%D0%BF%D1%80%D0%B8%20%D0%BD%D0%B5%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%B8%D1%85%20%D1%8D%D0%BA%D0%B7%D0%B5%D0%BC%D0%BF%D0%BB%D1%8F%D1%80%D0%B0%D1%85)
	- [❌ Антипаттерн 5: Тяжёлые операции в OnValidate](#%E2%9D%8C%20%D0%90%D0%BD%D1%82%D0%B8%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%205:%20%D0%A2%D1%8F%D0%B6%D1%91%D0%BB%D1%8B%D0%B5%20%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8%20%D0%B2%20OnValidate)
	- [❌ Антипаттерн 6: Destroy(gameObject) перед Raise()](#%E2%9D%8C%20%D0%90%D0%BD%D1%82%D0%B8%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%206:%20Destroy(gameObject)%20%D0%BF%D0%B5%D1%80%D0%B5%D0%B4%20Raise())
	- [❌ Антипаттерн 7: FindObjectOfType внутри SO](#%E2%9D%8C%20%D0%90%D0%BD%D1%82%D0%B8%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%207:%20FindObjectOfType%20%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B8%20SO)
	- [❌ Антипаттерн 8: Один SO делает всё](#%E2%9D%8C%20%D0%90%D0%BD%D1%82%D0%B8%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%208:%20%D0%9E%D0%B4%D0%B8%D0%BD%20SO%20%D0%B4%D0%B5%D0%BB%D0%B0%D0%B5%D1%82%20%D0%B2%D1%81%D1%91)
- [11. Тестирование SO в изоляции](#11.%20%D0%A2%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20SO%20%D0%B2%20%D0%B8%D0%B7%D0%BE%D0%BB%D1%8F%D1%86%D0%B8%D0%B8)
- [12. Практические задания](#12.%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F)
	- [Задание 1 (Базовый): Система характеристик персонажа](#%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%201%20(%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B9):%20%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D1%85%D0%B0%D1%80%D0%B0%D0%BA%D1%82%D0%B5%D1%80%D0%B8%D1%81%D1%82%D0%B8%D0%BA%20%D0%BF%D0%B5%D1%80%D1%81%D0%BE%D0%BD%D0%B0%D0%B6%D0%B0)
	- [Задание 2 (Средний): Event System на ScriptableObjects](#%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%202%20(%D0%A1%D1%80%D0%B5%D0%B4%D0%BD%D0%B8%D0%B9):%20Event%20System%20%D0%BD%D0%B0%20ScriptableObjects)
	- [Задание 3 (Продвинутый): State Machine на ScriptableObjects](#%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%203%20(%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%BD%D1%83%D1%82%D1%8B%D0%B9):%20State%20Machine%20%D0%BD%D0%B0%20ScriptableObjects)
- [13. Чеклист знаний](#13.%20%D0%A7%D0%B5%D0%BA%D0%BB%D0%B8%D1%81%D1%82%20%D0%B7%D0%BD%D0%B0%D0%BD%D0%B8%D0%B9)
	- [Теория](#%D0%A2%D0%B5%D0%BE%D1%80%D0%B8%D1%8F)
	- [Практика](#%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0)
	- [Антипаттерны (что точно не делаю)](#%D0%90%D0%BD%D1%82%D0%B8%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%D1%8B%20(%D1%87%D1%82%D0%BE%20%D1%82%D0%BE%D1%87%D0%BD%D0%BE%20%D0%BD%D0%B5%20%D0%B4%D0%B5%D0%BB%D0%B0%D1%8E))
	- [Когда что использовать](#%D0%9A%D0%BE%D0%B3%D0%B4%D0%B0%20%D1%87%D1%82%D0%BE%20%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C)
- [Итог](#%D0%98%D1%82%D0%BE%D0%B3)




---

<a name="введение"></a>

## 1. Введение: анатомия спагетти-проекта

### Как это начинается

Любой Unity-проект начинается одинаково: чисто, логично, с хорошими намерениями. Первый месяц — два скрипта, всё понятно. Второй месяц — десять скриптов, ещё терпимо. Через полгода вы открываете файл `GameManager.cs` и видите 800 строк, которые управляют всем: врагами, UI, звуком, сохранениями и «пока не трогай, работает».

Вот типичная картина такого проекта:



```csharp
// GameManager.cs — реальный пример из реального проекта
// (имена изменены, боль — нет)

public class GameManager : MonoBehaviour
{
    public static GameManager Instance; // Singleton — первый звоночек
    
    public int score;           // public поле — любой может изменить
    public bool isGameOver;     // глобальное состояние без контроля
    public float playerHealth;  // UI, враги, ловушки — все пишут сюда
    
    public UIManager uiManager;         // прямая ссылка
    public AudioManager audioManager;   // прямая ссылка
    public EnemySpawner enemySpawner;   // прямая ссылка
    public PlayerController player;     // прямая ссылка
    
    private void Update()
    {
        // 200 строк обновления всего и вся
        uiManager.UpdateScore(score);       // каждый кадр!
        audioManager.UpdateMusic(isGameOver);
        
        if (playerHealth <= 0 && !isGameOver)
        {
            isGameOver = true;
            uiManager.ShowGameOver();
            audioManager.PlayDefeatMusic();
            enemySpawner.StopSpawning();
            // ... ещё 20 строк
        }
    }
    
    public void AddScore(int points)
    {
        score += points;
        // Три места в коде делают то же самое по-разному
    }
}
```

### Что происходит с таким кодом

Проходит ещё несколько недель, и вы сталкиваетесь с конкретными болями:

**Боль 1: Невозможно тестировать сцены изолированно.** Открываете сцену `Level_03` — NullReferenceException, потому что `GameManager` должен быть загружен из `MainMenu`. Добавляете `DontDestroyOnLoad`. Теперь при повторном запуске сцены в редакторе появляются дубликаты.

**Боль 2: Дизайнер не может редактировать баланс.** Характеристики гоблина зашиты в код: `float damage = 25f`. Чтобы изменить урон — нужно найти нужный prefab среди пятидесяти, открыть компонент, изменить значение, не сломав ничего вокруг. Дизайнер звонит программисту по три раза в день.

**Боль 3: Добавление новой системы ломает существующую.** Нужно добавить систему достижений? `EnemyController.Die()` уже вызывает UI и звук — добавляете третью строку. Потом четвёртую. Потом `Die()` занимает 40 строк и знает о половине систем игры.

**Боль 4: Порядок инициализации — русская рулетка.** `AudioManager` требует `GameManager`, `GameManager` требует `PlayerController`, `PlayerController` требует `AudioManager`. В зависимости от порядка объектов в Hierarchy — иногда работает, иногда нет.



```csharp
Визуальная карта зависимостей типичного «спагетти»-проекта:

PlayerController ◄──────────────────► GameManager
       │                                    │
       │                                    │
       ▼                                    ▼
 AudioManager ◄────────────────────► UIManager
       │                │                  │
       │                │                  │
       ▼                ▼                  ▼
 EnemySpawner ◄─── EnemyController ──► ScoreSystem
       │                │
       └────────────────┘
       
Каждая стрелка — прямая зависимость.
Изменение любого класса потенциально ломает все связанные.
Добавление нового класса — добавление новых стрелок.
```

### Что предлагает эта статья

ScriptableObject — это не серебряная пуля и не замена всему. Это инструмент, который при правильном применении:

- **Разрывает прямые зависимости** между системами
- **Выносит конфигурацию** из кода в ассеты, доступные дизайнерам
- **Делает код тестируемым** без запуска всей игры
- **Заменяет Singleton** в большинстве случаев применения

К концу статьи та же архитектура будет выглядеть так:



```csharp
После рефакторинга на ScriptableObjects:

PlayerController ──Raise()──► [PlayerDiedEvent SO]
                                       │
                         ┌─────────────┼─────────────┐
                         ▼             ▼             ▼
                      UISystem    AudioSystem   AchievementSystem
                      
EnemyController ──Raise()──► [EnemyDiedEvent SO]
                                       │
                         ┌─────────────┼─────────────┐
                         ▼             ▼             ▼
                      ScoreSystem  AudioSystem   SpawnSystem

Каждая система знает только о SO-событии.
Не знает, кто ещё на него подписан.
Добавление новой системы = подписка на существующее событие.
Существующий код не меняется.
```

---

<a name="что-такое-scriptableobject"></a>

## 2. Что такое ScriptableObject

### Иерархия типов Unity

Чтобы понять ScriptableObject, нужно увидеть его место в иерархии типов Unity:



```csharp
UnityEngine.Object  (управляется нативным движком C++)
├── Component
│   └── Behaviour
│       └── MonoBehaviour   ← требует GameObject, живёт в сцене
├── GameObject
├── ure, Mesh, AudioClip...
└── ScriptableObject         ← не требует GameObject, существует независимо
```

Оба типа — `MonoBehaviour` и `ScriptableObject` — управляются Unity, а не стандартным сборщиком мусора .NET. Это значит:

- Нельзя создать через `new ScriptableObject()` — только через `CreateInstance<T>()`
- Не уничтожаются автоматически — только через `Destroy()`
- Имеют стабильный GUID для разрешения ссылок между ассетами
- Сериализуются встроенной системой Unity

### Ключевые отличия от MonoBehaviour

|Характеристика|MonoBehaviour|ScriptableObject|
|---|---|---|
|Требует GameObject|**Да**, обязательно|**Нет**|
|Живёт в сцене|**Да**|**Нет** — как `.asset` файл|
|Update / Start / Awake|**Есть**|**Нет**|
|Количество копий данных|По одной на каждый GO|**Один ассет — одна копия**|
|Сохраняется в проекте|Только через сцену/prefab|Как независимый `.asset`|
|Создание|`AddComponent` / prefab|`CreateInstance` / `[CreateAssetMenu]`|
|Основное применение|Логика + данные на объекте|Данные, события, конфигурация|
|Редактируется дизайнером|Только через prefab/сцену|**Напрямую в Project Window**|

### Почему «одна копия данных» — это важно

Представьте сцену с 500 врагами типа «Гоблин». Если характеристики хранятся в `MonoBehaviour`:



```csharp
// ❌ 500 врагов = 500 копий всех полей в памяти
public class GoblinController : MonoBehaviour
{
    public float maxHealth  = 100f;  // × 500
    public float damage     = 25f;   // × 500
    public float moveSpeed  = 3f;    // × 500
    public string enemyName = "Goblin"; // × 500
    // ... ещё 20 полей × 500
}
```

Если характеристики в ScriptableObject:



```csharp
// ✅ 500 врагов = 500 ссылок на ОДИН объект данных
public class GoblinController : MonoBehaviour
{
    [SerializeField] private EnemyDataSO _data; // ссылка — 8 байт
    private float _currentHealth; // только то, что изменяется — уникально
}

[CreateAssetMenu(menuName = "Enemies/Goblin Data")]
public class EnemyDataSO : ScriptableObject
{
    public float MaxHealth  = 100f;  // одна копия на весь проект
    public float Damage     = 25f;   
    public float MoveSpeed  = 3f;    
    public string EnemyName = "Goblin";
}
```

Экономия памяти — лишь один из эффектов. Важнее другое: **изменение одного ассета мгновенно отражается на всех 500 врагах**. В редакторе — без перекомпиляции. Это делает итерацию баланса принципиально другим процессом.

---

<a name="жизненный-цикл"></a>

## 3. Жизненный цикл ScriptableObject

ScriptableObject не имеет `Start`, `Update`, `Awake` — но имеет свои callback-методы. Понимание их порядка критично.

### Полная схема жизненного цикла



```csharp
┌─────────────────────────────────────────────────────────────────┐
│                  Жизненный цикл ScriptableObject                 │
│                                                                  │
│  Запуск редактора / Enter Play Mode / Reload Scripts            │
│                          │                                       │
│                          ▼                                       │
│              ┌─── Загрузка ассета ───┐                          │
│              │                       │                           │
│              ▼                       ▼                           │
│         Из .asset файла     CreateInstance<T>()                 │
│              │                       │                           │
│              └──────────┬────────────┘                           │
│                         │                                        │
│                         ▼                                        │
│                    OnEnable() ◄────────────────────┐            │
│                         │                           │            │
│                         ▼                           │            │
│              ┌─── Объект активен ───┐               │            │
│              │                     │               │            │
│              ▼                     ▼               │            │
│     Изменение в Inspector    Domain Reload         │            │
│              │                     │               │            │
│              ▼                     ▼               │            │
│         OnValidate()          OnDisable() ─────────┘            │
│         (Editor only)                                            │
│                                                                  │
│              При явном Destroy():                                │
│              OnDisable() → объект уничтожен                     │
└─────────────────────────────────────────────────────────────────┘
```

### OnEnable — правильное место для инициализации

`OnEnable` вызывается:

- При загрузке ассета в память
- После `CreateInstance<T>()`
- После **каждой** перезагрузки домена скриптов в редакторе



```csharp
[CreateAssetMenu(fileName = "EnemyDatabase", menuName = "Data/Enemy Database")]
public class EnemyDatabaseSO : ScriptableObject
{
    [SerializeField] private List<EnemyDataSO> _enemies;
    
    // Кэш для быстрого поиска — не сериализуется
    private Dictionary<string, EnemyDataSO> _lookup;
    
    private void OnEnable()
    {
        // ✅ OnEnable — единственное правильное место для инициализации кэшей
        // Вызывается после каждого Domain Reload — кэш всегда актуален
        RebuildLookup();
        
        // ✅ Сброс C# событий — критично при Domain Reload
        // После перезагрузки домена delegate-цепочки могут содержать
        // ссылки на уничтоженные объекты
        _onDataChanged = null;
    }
    
    private event Action _onDataChanged;
    
    private void RebuildLookup()
    {
        _lookup = new Dictionary<string, EnemyDataSO>();
        if (_enemies == null) return;
        
        foreach (var enemy in _enemies)
        {
            if (enemy == null) continue;
            _lookup[enemy.name] = enemy;
        }
    }
    
    public EnemyDataSO GetByName(string enemyName)
        => _lookup.TryGetValue(enemyName, out var data) ? data : null;
}
```

### OnDisable — обязательная очистка



```csharp
public class EventChannelSO : ScriptableObject
{
    private event Action _onRaised;
    
    private void OnEnable()
    {
        _onRaised = null; // сброс при каждой загрузке
    }
    
    private void OnDisable()
    {
        // Финальная очистка при выгрузке
        // Важно: в билде SO выгружаются при Unload
        _onRaised = null;
    }
    
    public void Subscribe(Action action)     => _onRaised += action;
    public void Unsubscribe(Action action)   => _onRaised -= action;
    public void Raise()                      => _onRaised?.Invoke();
}
```

### OnValidate — валидация и живые вычисления

`OnValidate` вызывается **только в редакторе** при любом изменении поля в Inspector. Это делает его мощным инструментом немедленной обратной связи.



```csharp
[CreateAssetMenu(fileName = "WeaponData", menuName = "Items/Weapon")]
public class WeaponDataSO : ScriptableObject
{
    [Header("Base Stats")]
    [SerializeField] private float _baseDamage  = 10f;
    [SerializeField] private float _attackRate  = 1.5f;  // атак/сек
    [SerializeField] private float _critChance  = 0.15f; // 0..1
    [SerializeField] private float _critMult    = 2.0f;
    
    [Header("Computed — read only")]
    [SerializeField, HideInInspector] private float _dps;
    [SerializeField, HideInInspector] private float _effectiveDps;
    
    public float BaseDamage  => _baseDamage;
    public float AttackRate  => _attackRate;
    public float DPS         => _dps;
    public float EffectiveDPS => _effectiveDps;
    
    private void OnValidate()
    {
        // Зажимаем некорректные значения
        _baseDamage = Mathf.Max(0f, _baseDamage);
        _attackRate = Mathf.Max(0.1f, _attackRate); // защита от /0
        _critChance = Mathf.Clamp01(_critChance);
        _critMult   = Mathf.Max(1f, _critMult);
        
        // Пересчитываем производные значения — мгновенно в Inspector
        _dps = _baseDamage * _attackRate;
        float avgDamage = _baseDamage * (1f - _critChance) 
                        + _baseDamage * _critMult * _critChance;
        _effectiveDps = avgDamage * _attackRate;
        
        // Предупреждения — дизайнер видит проблему сразу
        if (_effectiveDps > 500f)
            Debug.LogWarning($"[{name}] Очень высокий DPS: {_effectiveDps:F1}. " +
                             "Проверьте баланс.", this);
    }
}
```

> **Правило**: `OnValidate` — только для лёгких операций. Никакого `Instantiate`, `FindObjectOfType`, обращений к базам данных. Он вызывается при каждом изменении любого поля — тяжёлые операции сделают редактор неотзывчивым.

---

<a name="создание-и-организация"></a>

## 4. Создание и организация

### [CreateAssetMenu]



```csharp
[CreateAssetMenu(
    fileName = "NewEnemyData",      // имя файла по умолчанию
    menuName = "Game/Enemies/Data", // Assets > Create > Game > Enemies > Data
    order = 0                       // порядок в меню (меньше = выше)
)]
public class EnemyDataSO : ScriptableObject { }
```

### Создание через код (для инструментов и тестов)



```csharp
// В памяти (для тестов, не сохраняется)
var instance = ScriptableObject.CreateInstance<EnemyDataSO>();

// Сохранение на диск (только в Editor)
#if UNITY_EDITOR
using UnityEditor;

public static class SOToolkit
{
    // Создать один ассет
    public static T CreateAsset<T>(string path) where T : ScriptableObject
    {
        var asset = ScriptableObject.CreateInstance<T>();
        EnsureDirectoryExists(path);
        AssetDatabase.CreateAsset(asset, path);
        AssetDatabase.SaveAssets();
        return asset;
    }
    
    // Генерация набора ассетов (например, для процедурного заполнения)
    [MenuItem("Tools/Generate Enemy Configs")]
    public static void GenerateEnemyConfigs()
    {
        var configs = new[]
        {
            ("Goblin",  100f, 25f, 3f),
            ("Orc",     250f, 50f, 2f),
            ("Dragon", 1000f, 150f, 4f),
        };
        
        foreach (var (name, hp, dmg, speed) in configs)
        {
            var so = CreateAsset<EnemyDataSO>($"Assets/Data/Enemies/{name}Data.asset");
            so.Initialize(name, hp, dmg, speed);
            EditorUtility.SetDirty(so);
        }
        
        AssetDatabase.SaveAssets();
        Debug.Log($"Создано {configs.Length} конфигураций");
    }
    
    private static void EnsureDirectoryExists(string assetPath)
    {
        var dir = System.IO.Path.GetDirectoryName(assetPath);
        if (!System.IO.Directory.Exists(dir))
            System.IO.Directory.CreateDirectory(dir);
    }
}
#endif
```

### Рекомендуемая структура папок



```csharp
Assets/
├── Data/                          ← все SO-ассеты
│   ├── Characters/
│   │   ├── Player/
│   │   │   └── PlayerStats.asset
│   │   └── Enemies/
│   │       ├── GoblinData.asset
│   │       ├── OrcData.asset
│   │       └── DragonData.asset
│   ├── Events/                    ← SO-события (Задание 2)
│   │   ├── OnPlayerDied.asset
│   │   ├── OnEnemyDied.asset
│   │   └── OnLevelCompleted.asset
│   ├── Variables/                 ← Runtime Variables
│   │   ├── PlayerScore.asset
│   │   └── PlayerHealth.asset
│   └── Config/
│       ├── GameConfig.asset
│       └── BalanceConfig.asset
│
└── Scripts/
    └── ScriptableObjects/         ← только определения классов
        ├── Data/
        │   └── EnemyDataSO.cs
        ├── Events/
        │   ├── GameEventSO.cs
        │   └── GameEventSOGeneric.cs
        └── Variables/
            └── RuntimeVariableSO.cs
```

> **Правило разделения**: папка `Data/` — ассеты (работа дизайнера), папка `Scripts/ScriptableObjects/` — определения классов (работа программиста). Дизайнер создаёт ассеты, не трогая код.

---

<a name="архитектурные-паттерны"></a>

## 5. Архитектурные паттерны

### 5.1 Data Container

Самый простой и частый паттерн. SO хранит конфигурацию, компонент хранит состояние.

**Принцип разделения**: конфигурация (что неизменно) — в SO, состояние (что меняется в рантайме) — в компоненте.



```csharp
// SO: только конфигурация, только чтение
[CreateAssetMenu(menuName = "Characters/Stats")]
public class CharacterStatsSO : ScriptableObject
{
    [SerializeField] private float _maxHealth  = 100f;
    [SerializeField] private float _moveSpeed  = 5f;
    [SerializeField] private float _damage     = 25f;
    [SerializeField] private float _defense    = 10f;
    
    // Публичный API — только get
    public float MaxHealth  => _maxHealth;
    public float MoveSpeed  => _moveSpeed;
    public float Damage     => _damage;
    
    // Логика на основе конфигурации — уместна в SO
    public float CalculateReceivedDamage(float incoming)
        => Mathf.Max(0f, incoming - _defense);
}

// Компонент: состояние + логика, конфигурация из SO
public class Character : MonoBehaviour
{
    [SerializeField] private CharacterStatsSO _stats;
    
    // Рантайм-состояние — уникально для каждого экземпляра
    private float _currentHealth;
    private float _attackTimer;
    
    // C# события — лёгкая альтернатива UnityEvent для межсистемной коммуникации
    public event Action<float> OnHealthChanged; // float: percent 0..1
    public event Action        OnDied;
    
    private void Start()
    {
        // Инициализируем из конфигурации
        _currentHealth = _stats.MaxHealth;
    }
    
    public void TakeDamage(float incoming)
    {
        if (_currentHealth <= 0f) return; // уже мёртв
        
        float actual = _stats.CalculateReceivedDamage(incoming);
        _currentHealth = Mathf.Max(0f, _currentHealth - actual);
        
        OnHealthChanged?.Invoke(_currentHealth / _stats.MaxHealth);
        
        if (_currentHealth <= 0f)
            OnDied?.Invoke();
    }
}
```

### 5.2 Event System на ScriptableObjects

Паттерн, описанный Ryan Hipple на Unite Austin 2017. Событие — это ассет. Publisher не знает о Subscribers.



```csharp
┌─────────────────────────────────────────────────────────────────┐
│                    Архитектура Event System                      │
│                                                                  │
│  ┌──────────────┐   Raise()   ┌──────────────────┐             │
│  │ EnemyController│───────────►│ EnemyDiedEventSO │             │
│  │  (Publisher) │             │    (.asset)      │             │
│  └──────────────┘             └────────┬─────────┘             │
│                                        │                        │
│                           Notify all subscribers               │
│                                        │                        │
│                    ┌───────────────────┼───────────────┐       │
│                    │                   │               │       │
│                    ▼                   ▼               ▼       │
│             ┌──────────┐       ┌──────────┐   ┌──────────┐   │
│             │ScoreSystem│       │AudioSystem│   │Achievements│  │
│             │(Subscriber│       │(Subscriber│   │(Subscriber│  │
│             └──────────┘       └──────────┘   └──────────┘   │
│                                                                  │
│  ✅ EnemyController ничего не знает о подписчиках               │
│  ✅ Добавление новой системы = подписка на ассет                │
│  ✅ Удаление системы = отписка, остальной код не меняется       │
└─────────────────────────────────────────────────────────────────┘
```



```csharp
// Безпараметрическое событие
[CreateAssetMenu(menuName = "Events/Game Event")]
public class GameEventSO : ScriptableObject
{
    private event Action _onRaised;
    private readonly List<GameEventListenerMB> _listeners = new();
    
    private void OnEnable()
    {
        // Сброс при Domain Reload — предотвращает Ghost Callbacks
        _onRaised = null;
    }
    
    public void Raise()
    {
        // Обратный порядок: listener может отписаться во время вызова
        for (int i = _listeners.Count - 1; i >= 0; i--)
            _listeners[i].OnEventRaised();
        
        _onRaised?.Invoke();
    }
    
    public void Subscribe(Action cb)   => _onRaised += cb;
    public void Unsubscribe(Action cb) => _onRaised -= cb;
    
    public void RegisterListener(GameEventListenerMB l)
    {
        if (!_listeners.Contains(l)) _listeners.Add(l);
    }
    public void UnregisterListener(GameEventListenerMB l)
        => _listeners.Remove(l);
    
    // Тестирование события прямо из Inspector
    [ConMenu("Test: Raise Event")]
    private void EditorRaise() => Raise();
}

// Generic-база для типизированных событий
public abstract class GameEventSO<T> : ScriptableObject
{
    private event Action<T> _onRaised;
    
    private void OnEnable() => _onRaised = null;
    
    public void Raise(T value)      => _onRaised?.Invoke(value);
    public void Subscribe(Action<T> cb)   => _onRaised += cb;
    public void Unsubscribe(Action<T> cb) => _onRaised -= cb;
}

// Конкретные типизированные события
[CreateAssetMenu(menuName = "Events/Int Event")]
public class IntEventSO : GameEventSO<int> { }

[CreateAssetMenu(menuName = "Events/Float Event")]
public class FloatEventSO : GameEventSO<float> { }

// Событие с пользовательскими данными
[Serializable]
public struct EnemyDiedData
{
    public Vector3 Position;
    public int     ScoreValue;
    public string  EnemyType;
}

[CreateAssetMenu(menuName = "Events/Enemy Died")]
public class EnemyDiedEventSO : GameEventSO<EnemyDiedData> { }
```



```csharp
// Компонент-мост для подписки через Inspector (без написания кода)
public class GameEventListenerMB : MonoBehaviour
{
    [SerializeField] private GameEventSO _event;
    [SerializeField] private UnityEvent  _response;
    
    private void OnEnable()  => _event.RegisterListener(this);
    private void OnDisable() => _event.UnregisterListener(this);
    
    public void OnEventRaised()
    {
        try { _response?.Invoke(); }
        catch (Exception e)
        {
            Debug.LogError($"[{name}] Ошибка в обработчике события: {e.Message}", this);
        }
    }
}

// Пример Publisher — враг
public class EnemyController : MonoBehaviour
{
    [SerializeField] private float          _maxHealth = 100f;
    [SerializeField] private int            _scoreValue = 100;
    [SerializeField] private string         _enemyType = "Basic";
    
    // Только публикует — не знает о подписчиках
    [SerializeField] private EnemyDiedEventSO _onEnemyDied;
    
    private float _currentHealth;
    private bool  _isDead;
    
    private void Start() => _currentHealth = _maxHealth;
    
    public void TakeDamage(float damage)
    {
        if (_isDead) return;
        _currentHealth -= damage;
        if (_currentHealth <= 0f) Die();
    }
    
    private void Die()
    {
        _isDead = true; // защита от двойного вызова
        
        var data = new EnemyDiedData
        {
            Position   = transform.position,
            ScoreValue = _scoreValue,
            EnemyType  = _enemyType
        };
        
        _onEnemyDied?.Raise(data); // сначала событие
        Destroy(gameObject);        // потом уничтожение
    }
}

// Пример Subscriber — система счёта
public class ScoreSystem : MonoBehaviour
{
    [SerializeField] private EnemyDiedEventSO _onEnemyDied;
    [SerializeField] private IntEventSO       _onScoreChanged;
    [SerializeField] private TMP_         _score;
    
    private int _score;
    
    // Симметричные OnEnable / OnDisable — золотое правило
    private void OnEnable()  => _onEnemyDied.Subscribe(HandleEnemyDied);
    private void OnDisable() => _onEnemyDied.Unsubscribe(HandleEnemyDied);
    
    private void HandleEnemyDied(EnemyDiedData data)
    {
        _score += data.ScoreValue;
        _score. = $"Score: {_score}";
        _onScoreChanged?.Raise(_score);
    }
}
```

### 5.3 Runtime Variables — глобальное состояние без Singleton



```csharp
// Переменная — это ассет с подписками
public abstract class RuntimeVariableSO<T> : ScriptableObject
{
    [SerializeField] private T    _initialValue;
    [SerializeField] private bool _resetOnPlay = true;
    
    private T _runtimeValue;
    private event Action<T> _onChanged;
    
    private void OnEnable()
    {
        if (_resetOnPlay)
            _runtimeValue = _initialValue;
    }
    
    public T Value
    {
        get => _runtimeValue;
        set
        {
            _runtimeValue = value;
            _onChanged?.Invoke(value);
        }
    }
    
    public void Subscribe(Action<T> cb)   => _onChanged += cb;
    public void Unsubscribe(Action<T> cb) => _onChanged -= cb;
}

[CreateAssetMenu(menuName = "Variables/Int")]
public class IntVariableSO : RuntimeVariableSO<int>
{
    public void Add(int v)      => Value += v;
    public void Subtract(int v) => Value -= v;
}

[CreateAssetMenu(menuName = "Variables/Float")]
public class FloatVariableSO : RuntimeVariableSO<float> { }

[CreateAssetMenu(menuName = "Variables/Bool")]
public class BoolVariableSO : RuntimeVariableSO<bool>
{
    public void Toggle() => Value = !Value;
}
```

### 5.4 State Machine на ScriptableObjects

Каждое состояние — отдельный SO-ассет. Переходы настраиваются в Inspector.



```csharp
┌─────────────────────────────────────────────────────────────────┐
│               SO-based State Machine: Архитектура               │
│                                                                  │
│  PlayerStateMachineMB (MonoBehaviour)                           │
│  ├─ _currentState: PlayerStateSO                                │
│  ├─ _con: StateCon  ← данные для состояний              │
│  └─ Update():                                                   │
│       con.UpdateInput()                                     │
│       _currentState.Execute(con, dt)                        │
│       next = _currentState.GetTransition(con)              │
│       if (next != null) TransitionTo(next)                     │
│                                                                  │
│  PlayerStateSO (abstract ScriptableObject)                      │
│  ├─ Enter(con)    ← один раз при входе                      │
│  ├─ Execute(con, dt) ← каждый кадр                         │
│  ├─ Exit(con)     ← один раз при выходе                    │
│  └─ GetTransition(con) → PlayerStateSO?                    │
│                                                                  │
│  Project Window:                                                 │
│  ├─ IdleState.asset    → _runState: RunState.asset             │
│  │                     → _attackState: AttackState.asset       │
│  ├─ RunState.asset     → _idleState: IdleState.asset           │
│  │                     → _attackState: AttackState.asset       │
│  └─ AttackState.asset  → _idleState: IdleState.asset           │
│                                                                  │
│  ⚠️ ВАЖНО: рантайм-данные хранятся в StateCon,             │
│     НЕ в SO (SO — синглтоны, данные разделяются!)              │
└─────────────────────────────────────────────────────────────────┘
```



```csharp
// StateCon — контейнер рантайм-данных
public class StateCon
{
    public Transform   Transform    { get; }
    public Animator    Animator     { get; }
    public Rigidbody2D Rigidbody    { get; }
    
    // Рантайм-данные — изменяются состояниями
    public Vector2 MoveInput      { get; set; }
    public bool    AttackPressed   { get; set; }
    public float   StateTimer      { get; set; }
    public bool    AttackDone      { get; set; }
    
    public StateCon(Transform t, Animator a, Rigidbody2D rb)
    {
        Transform = t; Animator = a; Rigidbody = rb;
    }
    
    public void UpdateInput()
    {
        MoveInput     = new Vector2(Input.GetAxisRaw("Horizontal"), 0f);
        AttackPressed = Input.GetButtonDown("Fire1");
    }
}

// Абстрактное состояние
public abstract class PlayerStateSO : ScriptableObject
{
    [SerializeField] protected string _animationName;
    
    public virtual void Enter(StateCon ctx)
    {
        ctx.StateTimer = 0f;
        if (!string.IsNullOrEmpty(_animationName))
            ctx.Animator?.Play(_animationName);
    }
    
    public abstract void Execute(StateCon ctx, float dt);
    public virtual  void Exit(StateCon ctx) { }
    
    // null = остаться в текущем состоянии
    public abstract PlayerStateSO GetTransition(StateCon ctx);
}

// Конкретное состояние
[CreateAssetMenu(menuName = "StateMachine/Idle")]
public class IdleStateSO : PlayerStateSO
{
    [SerializeField] private PlayerStateSO _runState;
    [SerializeField] private PlayerStateSO _attackState;
    
    public override void Enter(StateCon ctx)
    {
        base.Enter(ctx);
        ctx.Rigidbody.velocity = Vector2.zero;
    }
    
    public override void Execute(StateCon ctx, float dt)
    {
        // Плавное торможение
        var vel = ctx.Rigidbody.velocity;
        vel.x = Mathf.Lerp(vel.x, 0f, dt * 10f);
        ctx.Rigidbody.velocity = vel;
    }
    
    public override PlayerStateSO GetTransition(StateCon ctx)
    {
        if (ctx.AttackPressed)            return _attackState;
        if (ctx.MoveInput.x != 0f)        return _runState;
        return null;
    }
}

// Контроллер State Machine
public class PlayerStateMachineMB : MonoBehaviour
{
    [SerializeField] private PlayerStateSO _initialState;
    [SerializeField] private bool          _debugLog;
    
    private PlayerStateSO _currentState;
    private StateCon  _con;
    
    private void Awake()
    {
        _con = new StateCon(
            transform,
            GetComponent<Animator>(),
            GetComponent<Rigidbody2D>()
        );
    }
    
    private void Start() => TransitionTo(_initialState);
    
    private void Update()
    {
        if (_currentState == null) return;
        _con.UpdateInput();
        _currentState.Execute(_con, Time.deltaTime);
        
        var next = _currentState.GetTransition(_con);
        if (next != null) TransitionTo(next);
    }
    
    private void TransitionTo(PlayerStateSO next)
    {
        _currentState?.Exit(_con);
        _currentState = next;
        _currentState?.Enter(_con);
        
        if (_debugLog)
            Debug.Log($"[{name}] → {next?.name ?? "null"}");
    }
    
    // Внешний форс-переход (для стана, кат-сцен и т.д.)
    public void ForceState(PlayerStateSO state) => TransitionTo(state);
}
```

---

<a name="so-как-замена-singleton"></a>

## 6. SO как замена Singleton

### Почему Singleton — проблема



```csharp
// ❌ Классический Unity Singleton
public class AudioManager : MonoBehaviour
{
    public static AudioManager Instance { get; private set; }
    
    private void Awake()
    {
        if (Instance != null) { Destroy(gameObject); return; }
        Instance = this;
        DontDestroyOnLoad(gameObject);
    }
    
    public void PlaySound(string name) { /* ... */ }
}

// Использование — скрытая зависимость
AudioManager.Instance.PlaySound("explosion"); 
// Кто вызывает? Откуда? Inspector не покажет.
// Тест невозможен без Instance.
// Порядок инициализации не гарантирован.
```

### Замена через SO Runtime Variables



```csharp
// ✅ Глобальное состояние через SO — без Singleton
// Assets/Data/Variables/PlayerScore.asset (IntVariableSO)
// Assets/Data/Variables/PlayerHealth.asset (FloatVariableSO)

// Writer — не знает о Readers
public class ScoreTracker : MonoBehaviour
{
    [SerializeField] private IntVariableSO _playerScore;
    
    public void AddPoints(int points) => _playerScore.Add(points);
}

// Reader — не знает о Writers
public class ScoreDisplay : MonoBehaviour
{
    [SerializeField] private IntVariableSO _playerScore;
    [SerializeField] private TMP_      _;
    
    private void OnEnable()  => _playerScore.Subscribe(Update);
    private void OnDisable() => _playerScore.Unsubscribe(Update);
    private void Start()     => Update(_playerScore.Value);
    
    private void Update(int score) => _. = score.ToString();
}
```

### Сравнение подходов к глобальному состоянию



```csharp
┌──────────────────────────────────────────────────────────────────┐
│              Сравнение подходов к глобальному состоянию          │
├──────────────────┬──────────────────┬───────────────────────────┤
│   Критерий       │    Singleton     │   SO Runtime Variable      │
├──────────────────┼──────────────────┼───────────────────────────┤
│ Зависимость      │ Скрытая (static) │ Явная ([SerializeField])   │
│ Видимость в      │ Нет              │ Да — ссылка в Inspector    │
│ Inspector        │                  │                            │
│ Тестируемость    │ Сложно           │ Легко (CreateInstance)     │
│ Замена в тесте   │ Невозможно       │ Простой Instantiate        │
│ Инициализация    │ Зависит от Awake │ При загрузке ассета        │
│ Сброс при Play   │ Нужен ручной код │ Автоматически (_resetOnPlay│
│ Подписки         │ event (static)   │ event + Inspector          │
│ Множество сцен   │ DontDestroy...   │ Не привязан к сцене        │
└──────────────────┴──────────────────┴───────────────────────────┘
```

---

<a name="вложенные-so"></a>

## 7. Вложенные SO и базы данных

### Ссылки между SO

ScriptableObject может содержать поля типа другого SO. Unity сериализует ссылки по GUID — переименование файлов внутри Project Window не ломает связи.



```csharp
// База данных как SO — центральная точка доступа
[CreateAssetMenu(menuName = "Data/Item Database")]
public class ItemDatabaseSO : ScriptableObject
{
    [SerializeField] private List<ItemDataSO> _allItems;
    
    // Словарь для O(1) поиска — несериализуем, пересоздаётся в OnEnable
    private Dictionary<string, ItemDataSO> _byId;
    
    private void OnEnable()
    {
        _byId = new Dictionary<string, ItemDataSO>();
        foreach (var item in _allItems)
        {
            if (item == null) continue;
            if (_byId.ContainsKey(item.ItemId))
            {
                Debug.LogError($"Дублирующийся ID: {item.ItemId}", item);
                continue;
            }
            _byId[item.ItemId] = item;
        }
    }
    
    public ItemDataSO GetById(string id)
        => _byId.TryGetValue(id, out var item) ? item : null;
    
    public IReadOnlyList<ItemDataSO> GetAll() => _allItems;
    
    public IEnumerable<ItemDataSO> GetByType(ItemType type)
        => _allItems.Where(i => i != null && i.Type == type);
}

// Предмет ссылается на другие SO
[CreateAssetMenu(menuName = "Items/Equipment")]
public class EquipmentSO : ItemDataSO
{
    [SerializeField] private CharacterStatsSO _statBonus;  // SO → SO
    [SerializeField] private List<ItemDataSO> _craftingIngredients; // список SO
    
    public CharacterStatsSO StatBonus => _statBonus;
    
    public bool CanCraft(IEnumerable<ItemDataSO> inventory)
        => _craftingIngredients.All(ingredient => inventory.Contains(ingredient));
}
```

### Защита от циклических ссылок



```csharp
// ❌ Потенциальный цикл: A.next = B, B.next = A
[CreateAssetMenu(menuName = "Dialogue/Node")]
public class DialogueNodeSO : ScriptableObject
{
    public string ;
    public List<DialogueNodeSO> Choices; // может создать цикл!
}

// ✅ Решение: ссылки по ID через базу данных
[CreateAssetMenu(menuName = "Dialogue/Node")]
public class DialogueNodeSO : ScriptableObject
{
    public string NodeId;
    public string ;
    public List<string> ChoiceNodeIds; // ID, а не прямые ссылки
    
    public List<DialogueNodeSO> GetChoices(DialogueDatabaseSO db)
        => ChoiceNodeIds.Select(id => db.GetById(id))
                        .Where(n => n != null)
                        .ToList();
}
```

---

<a name="сравнение-подходов"></a>

## 8. SO vs JSON vs PlayerPrefs

### Полная сравнительная таблица

|Критерий|ScriptableObject|JSON файл|PlayerPrefs|
|---|---|---|---|
|**Что хранит**|Конфигурацию, архитектурный клей|Данные любого типа|Простые значения (int/float/string)|
|**Редактирование**|Inspector Unity|Любой текстовый редактор|Только из кода|
|**Типобезопасность**|Полная (строгая C#)|Нет (строки → парсинг)|Частичная|
|**Производительность**|Высокая (в памяти)|Средняя (IO + десериализация)|Средняя (реестр/файл)|
|**Git / версионирование**|YAML diff|Хороший текстовый diff|Нет (реестр/бинарный)|
|**Работа дизайнера**|Напрямую в Inspector|Через текстовый редактор|Не применимо|
|**Шифрование данных**|Нет (открытый ассет)|Возможно|Нет|
|**Runtime изменения**|Опасно (изменяет ассет)|Безопасно|Безопасно|
|**Сохранение между сессиями**|Нет (только конфигурация)|Да|Да|
|**Зависимость от Unity**|Полная|Нет|Полная|
|**Удалённая загрузка**|Нет|Да (HTTP + JSON)|Нет|
|**Размер данных**|Небольшой|Любой|Небольшой|
|**Тестирование**|Легко (CreateInstance)|Легко (строки)|Средне (статический API)|

### Дерево принятия решений



```csharp
Нужно сохранить данные?
           │
           ▼
 Данные меняются в рантайме?
           │
     ┌─────┴──────┐
    НЕТ           ДА
     │             │
     ▼             ▼
 Это конфигурация  Нужно сохранять между сессиями?
 (баланс, настройки│
  уровней)?        │
     │        ┌────┴─────┐
     ▼        НЕТ        ДА
ScriptableObject  │         │
                  ▼         ▼
            RuntimeState  Что именно?
            (в памяти,         │
             не сохраняем) ┌───┼──────────────┐
                           │   │              │
                      Простые  Прогресс   Конфигурация
                      настройки игры      с сервера /
                      пользователя        моды
                           │   │              │
                           ▼   ▼              ▼
                      PlayerPrefs JSON     JSON / 
                                  файл    Addressables
```

### Когда что использовать — конкретные примеры



```csharp
// ✅ ScriptableObject: конфигурация, не меняющаяся в рантайме
[CreateAssetMenu(menuName = "Config/Enemy")]
public class EnemyConfigSO : ScriptableObject
{
    public float MaxHealth = 100f;    // баланс → SO
    public float Damage    = 25f;     // баланс → SO
    public Sprite Sprite;             // визуал → SO
    public AudioClip DeathSound;      // аудио → SO
}

// ✅ JSON: сохранение прогресса игрока
[Serializable]
public class PlayerSaveData
{
    public int   Level       = 1;
    public int   TotalScore  = 0;
    public float TotalTime   = 0f;
    public List<string> UnlockedLevels = new();
}

public static class SaveSystem
{
    private static string Path => 
        System.IO.Path.Combine(Application.persistentDataPath, "save.json");
    
    public static void Save(PlayerSaveData data)
        => System.IO.File.WriteAll(Path, JsonUtility.ToJson(data, true));
    
    public static PlayerSaveData Load()
    {
        if (!System.IO.File.Exists(Path)) return new PlayerSaveData();
        return JsonUtility.FromJson<PlayerSaveData>(System.IO.File.ReadAll(Path));
    }
}

// ✅ PlayerPrefs: только пользовательские настройки
public static class UserSettings
{
    public static float MusicVolume
    {
        get => PlayerPrefs.GetFloat("music_vol", 1f);
        set { PlayerPrefs.SetFloat("music_vol", value); PlayerPrefs.Save(); }
    }
    
    public static bool IsFirstLaunch
    {
        get => PlayerPrefs.GetInt("first_launch", 1) == 1;
        set { PlayerPrefs.SetInt("first_launch", value ? 1 : 0); PlayerPrefs.Save(); }
    }
}

// ✅ Гибрид — реальный сценарий
public class GameBootstrap : MonoBehaviour
{
    [SerializeField] private EnemyConfigSO  _enemyConfig;  // SO: конфигурация
    [SerializeField] private IntVariableSO  _currentScore; // SO: рантайм-переменная
    
    private PlayerSaveData _saveData; // JSON: прогресс
    
    private void Start()
    {
        // Конфигурация уже в памяти (SO)
        float enemyHp = _enemyConfig.MaxHealth;
        
        // Загружаем прогресс (JSON)
        _saveData = SaveSystem.Load();
        
        // Применяем настройки (PlayerPrefs)
        AudioListener.volume = UserSettings.MusicVolume;
        
        // Инициализируем рантайм-переменные (SO Variables)
        _currentScore.Value = 0;
    }
    
    private void OnApplicationQuit()
    {
        // Сохраняем прогресс (JSON)
        _saveData.TotalScore += _currentScore.Value;
        SaveSystem.Save(_saveData);
    }
}
```

---

<a name="ограничения"></a>

## 9. Ограничения и подводные камни

### SO не для сохранения состояния

Это самое критичное и частое непонимание. Поведение SO при изменении данных различается в редакторе и в билде:



```csharp
[CreateAssetMenu(menuName = "Test/Mutable")]
public class MutableSO : ScriptableObject
{
    public int Score = 0;
}

public class BrokenScoreTracker : MonoBehaviour
{
    [SerializeField] private MutableSO _so;
    
    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            _so.Score++;
            // В РЕДАКТОРЕ: изменяет .asset файл на диске!
            //              Значение сохраняется после Play Mode.
            //              Это баг, который невозможно воспроизвести в билде.
            //
            // В БИЛДЕ:     изменяет только в памяти.
            //              Сбрасывается при перезапуске.
            //
            // Итог: поведение различается — худший вид бага.
        }
    }
}
```

**Решение: паттерн разделения конфигурации и состояния**



```csharp
// Конфигурация — неизменна, в SO
[CreateAssetMenu(menuName = "Characters/Base Stats")]
public class BaseStatsSO : ScriptableObject
{
    public float MaxHealth = 100f;
    public float MaxMana   = 50f;
    // Только чтение — никогда не изменяем в рантайме
}

// Состояние — изменяемо, в обычном C# классе
[Serializable]
public class CharacterRuntimeState
{
    public float CurrentHealth;
    public float CurrentMana;
    public int   Level;
    public int   Experience;
    
    public static CharacterRuntimeState FromConfig(BaseStatsSO cfg) => new()
    {
        CurrentHealth = cfg.MaxHealth,
        CurrentMana   = cfg.MaxMana,
        Level         = 1,
        Experience    = 0
    };
}

// Компонент: хранит оба
public class CharacterComponent : MonoBehaviour
{
    [SerializeField] private BaseStatsSO _config;     // конфигурация
    private CharacterRuntimeState        _state;      // состояние
    
    private void Awake() => _state = CharacterRuntimeState.FromConfig(_config);
    
    public void TakeDamage(float dmg)
    {
        _state.CurrentHealth -= dmg; // изменяем состояние, не конфиг
    }
}
```

### Паттерн защитной копии

Когда нужно модифицировать SO-данные в рантайме (например, предметы с динамическими характеристиками):



```csharp
public class ItemInstance : MonoBehaviour
{
    [SerializeField] private ItemDataSO _template; // оригинальный SO
    
    private ItemDataSO _runtimeCopy; // рабочая копия
    
    private void Awake()
    {
        // Instantiate SO — создаёт копию в памяти, не на диске
        _runtimeCopy = Instantiate(_template);
        _runtimeCopy.name = $"{_template.name}_Runtime";
    }
    
    public void ApplyEnchantment(float damageBonus)
    {
        // Изменяем копию — оригинал не затронут
        _runtimeCopy.Damage += damageBonus;
    }
    
    private void OnDestroy()
    {
        // Обязательно уничтожить — без этого утечка памяти
        if (_runtimeCopy != null)
            Destroy(_runtimeCopy);
    }
}
```

### SO и сборка проекта

SO включается в билд только при соблюдении одного из условий:



```csharp
Условия включения SO в билд:

1. ✅ Прямая ссылка из компонента в активной сцене
   [SerializeField] private EnemyDataSO _data; // ← включит SO в билд
   
2. ✅ Расположение в папке Resources/
   Resources.Load<EnemyDataSO>("Enemies/GoblinData")
   ⚠️ Resources — устаревший подход, всё в памяти сразу
   
3. ✅ Включение в Addressable Assets (рекомендуется для больших проектов)
   Addressables.LoadAssetAsync<EnemyDataSO>("GoblinData")
   
4. ❌ Динамически созданные через CreateInstance — не попадут
   var so = ScriptableObject.CreateInstance<EnemyDataSO>(); // только в памяти
   
5. ❌ Ссылки только из кода через строки — ненадёжно
   // AssetDatabase.LoadAssetAtPath работает только в Editor
```

---

<a name="антипаттерны"></a>

## 10. Антипаттерны: как НЕ надо использовать SO

Этот раздел — концентрат ошибок из реальных проектов. Каждый антипаттерн сопровождается объяснением **почему это плохо** и **как исправить**.

---

### ❌ Антипаттерн 1: Мутирующий SO (Mutable ScriptableObject)

**Что делают:**



```csharp
[CreateAssetMenu(menuName = "Player/Stats")]
public class PlayerStatsSO : ScriptableObject
{
    public int   Score     = 0;
    public float Health    = 100f;
    public int   Level     = 1;
    // Код повсюду пишет в эти поля напрямую
}

// В PlayerController:
_stats.Score += 100;  // ← изменяет ассет!

// В EnemyController:
_stats.Health -= damage; // ← изменяет ассет!
```

**Почему плохо:**

- В редакторе — изменяет `.asset` файл на диске. После выхода из Play Mode данные **не сбрасываются**. Следующий запуск начинается с изменёнными значениями.
- В билде — изменяется только в памяти, сбрасывается при рестарте.
- Поведение в редакторе и в билде **различается** — самый сложный для отладки вид бага.
- Несколько персонажей, использующих один SO, делят данные.

**Как исправить:**



```csharp
// ✅ SO — только конфигурация
[CreateAssetMenu(menuName = "Player/Stats Config")]
public class PlayerStatsConfigSO : ScriptableObject
{
    // Только начальные значения, только чтение
    public float InitialHealth = 100f;
    public int   InitialLevel  = 1;
    // Нет Score — это рантайм-данные
}

// ✅ Рантайм-состояние — в компоненте или отдельном C# классе
public class PlayerController : MonoBehaviour
{
    [SerializeField] private PlayerStatsConfigSO _config;
    
    // Рантайм — изменяется freely
    private float _currentHealth;
    private int   _currentScore;
    private int   _currentLevel;
    
    private void Awake()
    {
        _currentHealth = _config.InitialHealth;
        _currentLevel  = _config.InitialLevel;
        _currentScore  = 0;
    }
}
```

---

### ❌ Антипаттерн 2: Ghost Callbacks (Забытая отписка)

**Что делают:**



```csharp
public class UIPanel : MonoBehaviour
{
    [SerializeField] private GameEventSO _onPlayerDied;
    
    private void Start() // ← Start вместо OnEnable
    {
        _onPlayerDied.Subscribe(ShowGameOverScreen);
        // OnDisable не отписывает — подписка навсегда
    }
    
    private void ShowGameOverScreen()
    {
        // Этот метод будет вызван даже если UIPanel уже уничтожена
        gameObject.SetActive(true); // NullReferenceException или хуже
    }
}
```

**Почему плохо:**

- Уничтоженный объект продолжает получать события — `NullReferenceException`
- В лучшем случае: Unity поймает вызов к уничтоженному компоненту
- В худшем: метод выполнится частично, вызвав неочевидные баги
- Утечка памяти: объект не собирается GC, пока на него есть ссылка из delegate

**Как исправить:**



```csharp
// ✅ Золотое правило: OnEnable/OnDisable всегда в паре
public class UIPanel : MonoBehaviour
{
    [SerializeField] private GameEventSO _onPlayerDied;
    
    // Подписка при активации компонента
    private void OnEnable()  => _onPlayerDied.Subscribe(ShowGameOverScreen);
    
    // Отписка при деактивации — ВСЕГДА
    private void OnDisable() => _onPlayerDied.Unsubscribe(ShowGameOverScreen);
    
    private void ShowGameOverScreen() { /* ... */ }
}
```

**Почему OnEnable/OnDisable, а не Awake/OnDestroy?**



```csharp
Awake/OnDestroy:                  OnEnable/OnDisable:
┌──────────────────────┐          ┌──────────────────────────┐
│ GO создан → Subscribe│          │ GO активен → Subscribe   │
│ ...                  │          │ GO.SetActive(false)       │
│ GO.SetActive(false)  │          │   → OnDisable: Unsubscribe│
│   ← всё ещё слушает! │          │ GO.SetActive(true)        │
│ GO.SetActive(true)   │          │   → OnEnable: Subscribe   │
│   ← дубликат?        │          │ GO уничтожен → OnDisable  │
│ GO уничтожен         │          │   → Unsubscribe ✅        │
│   → OnDestroy: Unsub │          └──────────────────────────┘
│   ← но если объект   │
│     уже потерян?     │
└──────────────────────┘

OnEnable/OnDisable корректно обрабатывают SetActive(true/false)
```

---

### ❌ Антипаттерн 3: SO как Singleton «через чёрный ход»

**Что делают:**



```csharp
[CreateAssetMenu(menuName = "Managers/Audio Manager SO")]
public class AudioManagerSO : ScriptableObject
{
    [SerializeField] private AudioSource _audioSource; // ← НЕЛЬЗЯ!
    
    public void PlaySound(AudioClip clip)
    {
        _audioSource.PlayOneShot(clip); // NullReference в билде
    }
}
```

**Почему плохо:**

- `AudioSource` — компонент Unity, привязан к сцене. SO не привязан к сцене.
- В редакторе может работать (если сцена открыта). В билде — `NullReferenceException`.
- `AudioSource` не сериализуется в SO (это компонент, не ассет).
- SO пытается быть Singleton-менеджером — это не его задача.

**Как исправить:**



```csharp
// ✅ SO — только данные и события. Компонент — только логика.
[CreateAssetMenu(menuName = "Events/Play Sound")]
public class PlaySoundEventSO : GameEventSO<AudioClip> { }

// SO публикует событие
[CreateAssetMenu(menuName = "Items/Potion")]
public class PotionSO : ScriptableObject
{
    [SerializeField] private AudioClip         _useSound;
    [SerializeField] private PlaySoundEventSO  _playSoundEvent; // SO → SO
    
    public void OnUsed()
    {
        _playSoundEvent?.Raise(_useSound); // поднимаем событие
        // Кто воспроизведёт — не наша забота
    }
}

// Компонент-слушатель со всеми нужными компонентами Unity
public class AudioSystem : MonoBehaviour
{
    [SerializeField] private PlaySoundEventSO _playSoundEvent;
    [SerializeField] private AudioSource      _audioSource; // компонент в сцене
    
    private void OnEnable()  => _playSoundEvent.Subscribe(PlayClip);
    private void OnDisable() => _playSoundEvent.Unsubscribe(PlayClip);
    
    private void PlayClip(AudioClip clip) => _audioSource.PlayOneShot(clip);
}
```

---

### ❌ Антипаттерн 4: Рантайм-данные в SO при нескольких экземплярах

**Что делают:**



```csharp
[CreateAssetMenu(menuName = "States/Attack")]
public class AttackStateSO : PlayerStateSO
{
    // ❌ Приватные поля в SO — разделяются между ВСЕМИ,
    // кто использует этот ассет!
    private bool  _damageDealt;
    private float _timer;
    
    public override void Execute(StateCon ctx, float dt)
    {
        _timer += dt;
        if (!_damageDealt && _timer > 0.3f)
        {
            _damageDealt = true;
            // ...
        }
    }
}
```

**Почему плохо:**

- `AttackState.asset` — один объект в памяти
- Если два персонажа используют один SO, они делят `_timer` и `_damageDealt`
- Атака первого персонажа влияет на анимацию второго

**Как исправить:**



```csharp
// ✅ Рантайм-данные — в StateCon (у каждого персонажа свой)
public class StateCon
{
    // Рантайм-данные состояний
    public float StateTimer        { get; set; }
    public bool  AttackDamageDealt { get; set; }
    public bool  AttackDone        { get; set; }
    // Каждый персонаж имеет свой экземпляр StateCon
}

// SO использует данные из con — не хранит своих
public class AttackStateSO : PlayerStateSO
{
    [SerializeField] private float _damageMoment = 0.3f;
    [SerializeField] private float _duration     = 0.6f;
    
    public override void Enter(StateCon ctx)
    {
        base.Enter(ctx);
        ctx.AttackDamageDealt = false; // сброс в con, не в SO
        ctx.AttackDone        = false;
    }
    
    public override void Execute(StateCon ctx, float dt)
    {
        ctx.StateTimer += dt;
        
        if (!ctx.AttackDamageDealt && ctx.StateTimer >= _damageMoment)
        {
            ctx.AttackDamageDealt = true;
            PerformAttack(ctx);
        }
        
        if (ctx.StateTimer >= _duration)
            ctx.AttackDone = true;
    }
}
```

---

### ❌ Антипаттерн 5: Тяжёлые операции в OnValidate

**Что делают:**



```csharp
private void OnValidate()
{
    // ❌ OnValidate вызывается при КАЖДОМ изменении ЛЮБОГО поля
    var allEnemies = Resources.FindObjectsOfTypeAll<EnemyDataSO>(); // дорого!
    
    foreach (var enemy in allEnemies)
        RecalculateDependencies(enemy); // ещё дороже!
    
    var copy = Instantiate(this); // НИКОГДА не делайте это здесь
    AssetDatabase.Refresh();      // зависает редактор
}
```

**Почему плохо:**

- `OnValidate` вызывается синхронно при каждом изменении поля
- При быстром вводе — вызывается десятки раз в секунду
- Дорогие операции делают Inspector неотзывчивым

**Как исправить:**



```csharp
// ✅ OnValidate — только лёгкие операции
private void OnValidate()
{
    // ✅ Зажимание значений — O(1)
    _maxHealth  = Mathf.Max(1f, _maxHealth);
    _attackRate = Mathf.Max(0.1f, _attackRate);
    
    // ✅ Простые вычисления — O(1)
    _dps = _damage * _attackRate;
    
    // ✅ Предупреждения — дёшево
    if (_dps > 1000f)
        Debug.LogWarning($"Высокий DPS: {_dps}", this);
    
    // ❌ НЕ делайте в OnValidate:
    // Resources.FindObjectsOfTypeAll<T>()
    // Instantiate / Destroy
    // AssetDatabase.* операции
    // IO операции
    // Сложные алгоритмы O(n²) и выше
}
```

---

### ❌ Антипаттерн 6: Destroy(gameObject) перед Raise()

**Что делают:**



```csharp
private void Die()
{
    Destroy(gameObject); // ← сначала уничтожаем
    _onEnemyDied?.Raise(data); // ← потом событие — но объект уже мёртв!
}
```

**Почему плохо:**

- После `Destroy` компоненты объекта становятся невалидными
- Если обработчик события обращается к компонентам умершего объекта — NullReference
- Эффекты (частицы, звуки в позиции объекта) не могут получить `transform.position`

**Как исправить:**



```csharp
// ✅ Порядок: событие → уничтожение
private void Die()
{
    _isDead = true; // блокируем повторный вызов
    
    var data = new EnemyDiedData
    {
        Position   = transform.position, // получаем ДО уничтожения
        ScoreValue = _scoreValue,
        EnemyType  = _enemyType
    };
    
    _onEnemyDied?.Raise(data); // обработчики получают валидные данные
    
    Destroy(gameObject); // только теперь
}
```

---

### ❌ Антипаттерн 7: FindObjectOfType внутри SO

**Что делают:**



```csharp
[CreateAssetMenu(menuName = "Skills/Fireball")]
public class FireballSkillSO : ScriptableObject
{
    public void Use()
    {
        // ❌ SO ищет объекты в сцене — грубое нарушение архитектуры
        var player = FindObjectOfType<PlayerController>(); 
        var camera = FindObjectOfType<Camera>();
        // ...
    }
}
```

**Почему плохо:**

- SO не должен знать о сцене — он живёт независимо от неё
- `FindObjectOfType` — дорогая операция
- Жёсткая связь: SO зависит от конкретного MonoBehaviour
- Невозможно протестировать SO без загруженной сцены

**Как исправить:**



```csharp
// ✅ Вариант 1: передавать зависимости через параметры
[CreateAssetMenu(menuName = "Skills/Fireball")]
public class FireballSkillSO : ScriptableObject
{
    [SerializeField] private GameEventSO<Vector3> _onFireballLaunched;
    
    // Все данные получает снаружи — не ищет сам
    public void Use(Vector3 origin, Vector3 direction)
    {
        _onFireballLaunched?.Raise(origin);
        // Логика движения снаряда — в отдельном MonoBehaviour
    }
}

// ✅ Вариант 2: через StateCon (для State Machine)
public class FireAttackStateSO : PlayerStateSO
{
    public override void Execute(StateCon ctx, float dt)
    {
        // Всё нужное уже в con
        var position  = ctx.Transform.position;
        var direction = ctx.FacingDirection;
        // ...
    }
}
```

---

### ❌ Антипаттерн 8: Один SO делает всё

**Что делают:**



```csharp
[CreateAssetMenu(menuName = "God Object SO")]
public class GameManagerSO : ScriptableObject
{
    // Данные врагов
    public float EnemyHealth;
    public float EnemyDamage;
    
    // Данные игрока
    public float PlayerHealth;
    public float PlayerSpeed;
    
    // Конфигурация UI
    public Color HealthBarColor;
    public float UIAnimationSpeed;
    
    // Аудио
    public AudioClip BackgroundMusic;
    public float MusicVolume;
    
    // Физика
    public float Gravity;
    public float JumpForce;
    
    // ... ещё 50 полей
    
    // Методы для всего
    public void HandleEnemyDeath() { /* ... */ }
    public void UpdateUI()         { /* ... */ }
    public void PlayMusic()        { /* ... */ }
}
```

**Почему плохо:**

- God Object в новой обёртке — все проблемы Singleton, только в SO
- Невозможно переиспользовать части конфигурации
- Изменение одного поля затрагивает всех потребителей
- Дизайнеры не могут работать независимо

**Как исправить:**



```csharp
// ✅ Один SO — одна ответственность
[CreateAssetMenu(menuName = "Config/Enemy")]
public class EnemyConfigSO : ScriptableObject
{
    public float Health; public float Damage;
}

[CreateAssetMenu(menuName = "Config/Player")]
public class PlayerConfigSO : ScriptableObject
{
    public float Health; public float Speed;
}

[CreateAssetMenu(menuName = "Config/UI")]
public class UIConfigSO : ScriptableObject
{
    public Color HealthBarColor; public float AnimSpeed;
}

[CreateAssetMenu(menuName = "Config/Audio")]
public class AudioConfigSO : ScriptableObject
{
    public AudioClip Music; public float Volume;
}

// Если нужна агрегация — через составной SO
[CreateAssetMenu(menuName = "Config/Level")]
public class LevelConfigSO : ScriptableObject
{
    public EnemyConfigSO EnemyConfig;  // ссылки на специализированные SO
    public PlayerConfigSO PlayerConfig;
    public UIConfigSO     UIConfig;
}
```

---

<a name="тестирование"></a>

## 11. Тестирование SO в изоляции

Тестируемость — одно из главных достоинств SO. `ScriptableObject.CreateInstance<T>()` позволяет создавать экземпляры без запуска сцены.



```csharp
// Tests/Editor/CharacterStatsSOTests.cs
using NUnit.Framework;
using UnityEngine;

[TestFixture]
public class CharacterStatsSOTests
{
    private CharacterStatsSO _stats;
    
    [SetUp]
    public void SetUp()
    {
        // Создаём SO без сцены, без Editor, без prefab
        _stats = ScriptableObject.CreateInstance<CharacterStatsSO>();
    }
    
    [TearDown]
    public void TearDown()
    {
        Object.DestroyImmediate(_stats); // очистка после теста
    }
    
    [Test]
    public void CalculateReceivedDamage_IncomingLessThanDefense_ReturnsZero()
    {
        // Arrange
        _stats.SetValues(maxHealth: 100f, defense: 20f);
        
        // Act
        float result = _stats.CalculateReceivedDamage(10f); // 10 < 20
        
        // Assert
        Assert.AreEqual(0f, result, 0.001f);
    }
    
    [Test]
    [TestCase(50f, 10f, 40f)]   // стандартный случай
    [TestCase(10f, 0f,  10f)]   // нет защиты
    [TestCase(0f,  10f, 0f)]    // нет урона
    public void CalculateReceivedDamage_VariousCases(
        float incoming, float defense, float expected)
    {
        _stats.SetValues(defense: defense);
        float result = _stats.CalculateReceivedDamage(incoming);
        Assert.AreEqual(expected, result, 0.001f);
    }
}

// Tests/Editor/GameEventSOTests.cs
[TestFixture]
public class GameEventSOTests
{
    private GameEventSO _event;
    private int         _callCount;
    
    [SetUp]
    public void SetUp()
    {
        _event     = ScriptableObject.CreateInstance<GameEventSO>();
        _callCount = 0;
    }
    
    [TearDown]
    public void TearDown() => Object.DestroyImmediate(_event);
    
    [Test]
    public void Raise_WithSubscriber_CallsExactlyOnce()
    {
        _event.Subscribe(() => _callCount++);
        _event.Raise();
        Assert.AreEqual(1, _callCount);
    }
    
    [Test]
    public void Raise_AfterUnsubscribe_DoesNotCall()
    {
        Action cb = () => _callCount++;
        _event.Subscribe(cb);
        _event.Unsubscribe(cb);
        _event.Raise();
        Assert.AreEqual(0, _callCount);
    }
    
    [Test]
    public void Raise_ListenerUnsubscribesDuringRaise_NoCrash()
    {
        // Опасный сценарий: listener отписывается во время вызова
        Action selfUnsub = null;
        selfUnsub = () =>
        {
            _callCount++;
            _event.Unsubscribe(selfUnsub); // отписка во время Raise
        };
        
        _event.Subscribe(selfUnsub);
        
        // Не должно выбросить исключение
        Assert.DoesNotThrow(() => _event.Raise());
        Assert.AreEqual(1, _callCount);
    }
}
```

---

<a name="практические-задания"></a>

## 12. Практические задания

---

### Задание 1 (Базовый): Система характеристик персонажа

**Цель**: создать SO-контейнер данных, подключить к MonoBehaviour, UI обновляется по событию — без polling в Update.

**Стартовый код для рефакторинга:**



```csharp
// CharacterLegacy.cs — что нужно переделать
public class CharacterLegacy : MonoBehaviour
{
    // ❌ Данные и логика перемешаны, нет переиспользования
    public float maxHealth  = 100f;
    public float moveSpeed  = 5f;
    public float damage     = 25f;
    public float defense    = 10f;
    public float attackRate = 1.5f;
    
    private float _currentHealth;
    
    private void Start() => _currentHealth = maxHealth;
    
    public float CalculateDamageReceived(float incoming)
        => Mathf.Max(0f, incoming - defense);
    
    public void TakeDamage(float incoming)
    {
        _currentHealth -= CalculateDamageReceived(incoming);
        Debug.Log($"HP: {_currentHealth}/{maxHealth}");
    }
    
    public float GetHealthPercent() => _currentHealth / maxHealth;
    public bool  IsAlive()          => _currentHealth > 0f;
}

// HealthBarLegacy.cs — polling, плохо
public class HealthBarLegacy : MonoBehaviour
{
    [SerializeField] private CharacterLegacy _character;
    [SerializeField] private Image           _fillImage;
    
    private void Update() // ❌ каждый кадр
        => _fillImage.fillAmount = _character.GetHealthPercent();
}
```

**Что нужно создать:**



```csharp
// TODO: CharacterStatsSO.cs
[CreateAssetMenu(fileName = "NewCharacterStats", menuName = "RPG/Character Stats")]
public class CharacterStatsSO : ScriptableObject
{
    [Header("Vital Stats")]
    [SerializeField] private float _maxHealth  = 100f;
    [SerializeField] private float _defense    = 10f;
    
    [Header("Movement")]
    [SerializeField] private float _moveSpeed  = 5f;
    
    [Header("Combat")]
    [SerializeField] private float _damage     = 25f;
    [SerializeField] private float _attackRate = 1.5f;
    
    // TODO 1: Публичные свойства (только get)
    
    // TODO 2: CalculateReceivedDamage(float incoming) → float
    
    // TODO 3: OnValidate — зажать значения, пересчитать DPS в поле только для Inspector
}

// TODO: Character.cs
public class Character : MonoBehaviour
{
    [SerializeField] private CharacterStatsSO _stats;
    
    // TODO: события OnHealthChanged (float percent), OnDied
    // TODO: TakeDamage, Heal, CanAttack, IsAlive
    // Конфигурация из _stats, состояние в приватных полях
}

// TODO: HealthBar.cs
public class HealthBar : MonoBehaviour
{
    [SerializeField] private Character _character;
    [SerializeField] private Image     _fillImage;
    
    // TODO: подписка в OnEnable, отписка в OnDisable
    // Без Update — обновление только по событию
}
```

**Критерии выполнения:**



```csharp
✅ Обязательные:
   [ ] CharacterStatsSO создаётся через меню Assets > Create
   [ ] Изменение значения в Inspector пересчитывает DPS в реальном времени
   [ ] Character.cs не содержит числовых литералов характеристик
   [ ] HealthBar обновляется только по событию (нет Update в HealthBar)
   [ ] 3 разных SO: PlayerStats, GoblinStats, OrcStats — разные префабы

✅ Продвинутые:
   [ ] OnValidate предотвращает значения < 0 и AttackRate < 0.1
   [ ] TakeDamage не вызывает OnDied дважды (guard clause _isDead)
   [ ] Удаление Character из сцены не вызывает ошибок в HealthBar
```

---

### Задание 2 (Средний): Event System на ScriptableObjects

**Цель**: развязать все системы через SO-события. Враг умирает → счёт, звук, достижения — без прямых ссылок.

**Стартовый код для рефакторинга:**



```csharp
// EnemyControllerLegacy.cs — прямые зависимости
public class EnemyControllerLegacy : MonoBehaviour
{
    // ❌ Враг знает об UI, звуке и достижениях
    [SerializeField] private ScoreUILegacy      _scoreUI;
    [SerializeField] private AudioManagerLegacy _audioManager;
    [SerializeField] private AchievementSystem  _achievements;
    
    private void Die()
    {
        _scoreUI?.AddScore(100);
        _audioManager?.PlayEnemyDeathSound();
        _achievements?.NotifyEnemyKilled();
        Destroy(gameObject);
    }
}
```

**Что нужно создать:**



```csharp
// TODO 1: GameEventSO.cs — безпараметрическое событие
// TODO 2: GameEventSO<T>.cs — Generic-база
// TODO 3: EnemyDiedEventSO.cs + struct EnemyDiedData { Position, ScoreValue, EnemyType }
// TODO 4: GameEventListenerMB.cs — мост между SO и UnityEvent в Inspector

// TODO 5: EnemyController.cs (рефакторинг)
// - Только SerializeField EnemyDiedEventSO _onEnemyDied
// - Никаких ссылок на ScoreUI, AudioManager, AchievementSystem
// - Raise сначала, Destroy потом

// TODO 6: ScoreSystem.cs, AudioSystem.cs, AchievementSystem.cs
// - Каждый подписывается на события в OnEnable
// - Каждый отписывается в OnDisable
// - Никто не знает друг о друге
```

**Финальная архитектурная схема (заполните):**



```csharp
EnemyController ──Raise()──► [            .asset]
                                         │
                      ┌──────────────────┼──────────────────┐
                      │                  │                  │
                      ▼                  ▼                  ▼
               [           ]      [           ]      [           ]
               
Вопросы для самопроверки:
1. Нужно ли изменять EnemyController при добавлении новой системы?
2. Что произойдёт при удалении AudioSystem из сцены?
3. Как протестировать событие без запуска игры?
```

**Критерии выполнения:**



```csharp
✅ Обязательные:
   [ ] EnemyController не имеет ссылок на ScoreSystem, AudioSystem, Achievements
   [ ] Добавление новой системы не изменяет EnemyController
   [ ] [ConMenu("Test Raise")] работает без Play Mode
   [ ] Отписка в OnDisable у всех подписчиков

✅ Продвинутые:
   [ ] Удаление AudioSystem из сцены не ломает остальное
   [ ] EnemyDiedData передаёт Position — звук воспроизводится в точке смерти
   [ ] _isDead защищает от двойного Die()
```

---

### Задание 3 (Продвинутый): State Machine на ScriptableObjects

**Цель**: переписать монолитный switch-based Update в архитектуру, где каждое состояние — SO-ассет. Добавить новое состояние Roll без изменения существующего кода.

**Стартовый код для рефакторинга:**



```csharp
// PlayerControllerLegacy.cs — монолитная State Machine
public class PlayerControllerLegacy : MonoBehaviour
{
    private enum PlayerState { Idle, Run, Attack }
    private PlayerState _state = PlayerState.Idle;
    
    [SerializeField] private float _moveSpeed = 5f;
    [SerializeField] private float _attackCooldown = 0.8f;
    private float _attackTimer;
    
    private void Update()
    {
        // ❌ Всё в одном методе — добавление состояния требует изменения этого файла
        switch (_state)
        {
            case PlayerState.Idle:
                if (Input.GetAxisRaw("Horizontal") != 0) _state = PlayerState.Run;
                if (Input.GetButtonDown("Fire1"))         _state = PlayerState.Attack;
                break;
            case PlayerState.Run:
                transform.Translate(Vector3.right * Input.GetAxisRaw("Horizontal") 
                                    * _moveSpeed * Time.deltaTime);
                if (Input.GetAxisRaw("Horizontal") == 0) _state = PlayerState.Idle;
                if (Input.GetButtonDown("Fire1"))         _state = PlayerState.Attack;
                break;
            case PlayerState.Attack:
                _attackTimer += Time.deltaTime;
                if (_attackTimer >= _attackCooldown)
                {
                    _attackTimer = 0f;
                    _state = PlayerState.Idle;
                }
                break;
        }
    }
}
```

**Что нужно создать:**



```csharp
// TODO 1: StateCon.cs — рантайм-данные для состояний
public class StateCon
{
    public Transform   Transform  { get; }
    public Animator    Animator   { get; }
    public Rigidbody2D Rigidbody  { get; }
    
    // Рантайм (изменяется)
    public Vector2 MoveInput     { get; set; }
    public bool    AttackPressed  { get; set; }
    public float   StateTimer     { get; set; }
    public bool    AttackDone     { get; set; }
    
    // TODO: конструктор, UpdateInput(), UpdateGroundCheck()
}

// TODO 2: PlayerStateSO.cs — абстрактный базовый класс
public abstract class PlayerStateSO : ScriptableObject
{
    [SerializeField] protected string _animationName;
    
    public virtual  void Enter(StateCon ctx) { ctx.StateTimer = 0f; /* play anim */ }
    public abstract void Execute(StateCon ctx, float dt);
    public virtual  void Exit(StateCon ctx) { }
    public abstract PlayerStateSO GetTransition(StateCon ctx); // null = остаться
}

// TODO 3: IdleStateSO.cs, RunStateSO.cs, AttackStateSO.cs
// Каждый — [CreateAssetMenu], реализует Enter/Execute/Exit/GetTransition
// Переходы настраиваются в Inspector через SerializeField PlayerStateSO _nextState

// TODO 4: PlayerStateMachineMB.cs
// Update(): UpdateInput → Execute → GetTransition → TransitionTo (если не null)
// НЕТ switch/if по типам состояний

// TODO 5 (САМОСТОЯТЕЛЬНО): RollStateSO.cs
// Без изменения существующих файлов!
// Условие входа: LeftShift в RunState
// Длительность: 0.4 сек, скорость 2x, неуязвимость
```

**Критерии выполнения:**



```csharp
✅ Обязательные:
   [ ] PlayerStateMachineMB.Update() не содержит switch/if по типам состояний
   [ ] Каждое состояние — отдельный .asset файл, переходы в Inspector
   [ ] StateCon: рантайм-данные не в SO (SO — синглтоны!)
   [ ] Анимации переключаются корректно без застревания

✅ Расширяемость (Open/Closed Principle):
   [ ] RollStateSO создан без изменения IdleStateSO, AttackStateSO, PlayerStateMachineMB
   [ ] Для добавления состояния нужно: создать файл + создать ассет + назначить в Inspector
```

---

<a name="чеклист"></a>

## 13. Чеклист знаний

Используйте этот список для самооценки. Каждый пункт соответствует концепции из статьи.

### Теория



```csharp
Основы:
[ ] Могу объяснить разницу между MonoBehaviour и ScriptableObject
    (привязка к GO, жизненный цикл, количество копий в памяти)

[ ] Знаю, когда вызывается OnEnable, OnDisable, OnValidate
    и что делать в каждом из них

[ ] Понимаю, почему нельзя писать new ScriptableObject()
    и как правильно создавать экземпляры

[ ] Знаю разницу между ассетом SO и экземпляром в памяти

Архитектура:
[ ] Могу объяснить паттерн Data Container и когда его применять

[ ] Могу объяснить SO Event System:
    кто такой Publisher, кто Subscriber, что такое канал событий

[ ] Понимаю, зачем очищать C# events в OnEnable SO
    (Domain Reload, Ghost Callbacks)

[ ] Знаю разницу между SO Runtime Variable и Singleton

[ ] Понимаю, почему рантайм-данные State Machine хранятся в StateCon,
    а не в SO-состоянии

Ограничения:
[ ] Знаю, что изменение SO в Play Mode в редакторе изменяет ассет на диске

[ ] Знаю, при каких условиях SO попадает в билд

[ ] Понимаю разницу поведения SO в редакторе и в билде
```

### Практика



```csharp
Data Container:
[ ] Создаю SO с [CreateAssetMenu], правильно именую меню
[ ] Реализую OnValidate с зажиманием значений
[ ] Разделяю конфигурацию (SO) и состояние (компонент)
[ ] Не мутирую SO в рантайме

Event System:
[ ] Реализую GameEventSO с поддержкой C# Subscribe и Inspector Listeners
[ ] Пишу симметричные OnEnable/OnDisable для подписок — всегда
[ ] Не забываю сброс C# events в OnEnable SO
[ ] Тестирую события через [ConMenu] без Play Mode

State Machine:
[ ] Создаю абстрактный PlayerStateSO с Enter/Execute/Exit/GetTransition
[ ] Передаю рантайм-данные через StateCon, не через поля SO
[ ] Контроллер SM не содержит switch/if по типам состояний
[ ] Добавляю новое состояние без изменения существующих файлов
```

### Антипаттерны (что точно не делаю)



```csharp
[ ] НЕ мутирую SO в рантайме без создания защитной копии
[ ] НЕ подписываюсь без отписки (нет Subscribe без Unsubscribe)
[ ] НЕ храню ссылки на SceneObject (AudioSource, Camera) в SO
[ ] НЕ вызываю FindObjectOfType внутри SO
[ ] НЕ делаю тяжёлые операции в OnValidate
[ ] НЕ уничтожаю объект до вызова события (Destroy перед Raise)
[ ] НЕ храню рантайм-данные в SO, используемом несколькими экземплярами
[ ] НЕ создаю God Object SO — один SO, одна ответственность
```

### Когда что использовать



```csharp
[ ] SO: конфигурация, баланс, ассеты на которые ссылается дизайнер,
        архитектурный клей (события, переменные)

[ ] JSON: прогресс игры, пользовательский контент, данные с сервера,
          всё что нужно сохранить между сессиями

[ ] PlayerPrefs: только пользовательские настройки
                 (громкость, графика, первый запуск)
```

---

## Итог

ScriptableObject — это не просто «удобное место для данных». Это философия проектирования, которая ставит **явность зависимостей** над неявными связями, **ассеты** над жёстко зашитыми значениями, **слабую связность** над удобством быстрого доступа через `Instance`.

Путь от спагетти-проекта к SO-архитектуре не происходит за один день. Начните с малого:

1. **Неделя 1**: вынесите характеристики одного типа врага в `EnemyDataSO`. Оцените, насколько проще стало работать дизайнеру.
    
2. **Неделя 2**: замените одну связь через прямую ссылку на SO-событие. Убедитесь, что система достижений подписалась без изменения кода врага.
    
3. **Неделя 3**: замените один Singleton на `RuntimeVariableSO`. Напишите первый тест для SO без запуска сцены.
    

Через месяц такой практики вы обнаружите, что перестали бояться изменять код — потому что системы больше не переплетены в клубок, где дёргая за одну нить, вытягиваешь всё остальное.

---

_Статья основана на докладах Ryan Hipple «Game Architecture with ScriptableObjects» (Unite Austin 2017) и Richard Fine «Overthrowing the MonoBehaviour Tyranny» (Unite Europe 2016) с расширением практическими паттернами и антипаттернами из production-проекто_