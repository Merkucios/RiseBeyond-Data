# Unity Serialization: Полное руководство для разработчика


## Содержание

- [Введение](#%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5)
- [1. Что такое сериализация в Unity и зачем она нужна](#1.%20%D0%A7%D1%82%D0%BE%20%D1%82%D0%B0%D0%BA%D0%BE%D0%B5%20%D1%81%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B2%20Unity%20%D0%B8%20%D0%B7%D0%B0%D1%87%D0%B5%D0%BC%20%D0%BE%D0%BD%D0%B0%20%D0%BD%D1%83%D0%B6%D0%BD%D0%B0)
	- [Фундаментальная проблема](#%D0%A4%D1%83%D0%BD%D0%B4%D0%B0%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%BF%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0)
	- [Где Unity использует сериализацию](#%D0%93%D0%B4%D0%B5%20Unity%20%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D1%83%D0%B5%D1%82%20%D1%81%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8E)
	- [Формат хранения](#%D0%A4%D0%BE%D1%80%D0%BC%D0%B0%D1%82%20%D1%85%D1%80%D0%B0%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F)
- [2. Как Unity сериализует данные: поля, типы, правила](#2.%20%D0%9A%D0%B0%D0%BA%20Unity%20%D1%81%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D0%B8%D0%B7%D1%83%D0%B5%D1%82%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5:%20%D0%BF%D0%BE%D0%BB%D1%8F,%20%D1%82%D0%B8%D0%BF%D1%8B,%20%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0)
	- [Базовые правила сериализации](#%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B5%20%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0%20%D1%81%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8)
	- [Сериализуемые типы](#%D0%A1%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D0%B8%D0%B7%D1%83%D0%B5%D0%BC%D1%8B%D0%B5%20%D1%82%D0%B8%D0%BF%D1%8B)
	- [Глубина сериализации](#%D0%93%D0%BB%D1%83%D0%B1%D0%B8%D0%BD%D0%B0%20%D1%81%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8)
	- [Поведение при десериализации: важный нюанс](#%D0%9F%D0%BE%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BF%D1%80%D0%B8%20%D0%B4%D0%B5%D1%81%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8:%20%D0%B2%D0%B0%D0%B6%D0%BD%D1%8B%D0%B9%20%D0%BD%D1%8E%D0%B0%D0%BD%D1%81)
- [3. Атрибуты: [SerializeField], [NonSerialized], [System.Serializable]](#3.%20%D0%90%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%82%D1%8B:%20%5BSerializeField%5D,%20%5BNonSerialized%5D,%20%5BSystem.Serializable%5D)
	- [Дополнительные полезные атрибуты](#%D0%94%D0%BE%D0%BF%D0%BE%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D0%BF%D0%BE%D0%BB%D0%B5%D0%B7%D0%BD%D1%8B%D0%B5%20%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%82%D1%8B)
- [4. ScriptableObject vs MonoBehaviour сериализация](#4.%20ScriptableObject%20vs%20MonoBehaviour%20%D1%81%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F)
	- [Принципиальные различия](#%D0%9F%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D1%80%D0%B0%D0%B7%D0%BB%D0%B8%D1%87%D0%B8%D1%8F)
	- [Когда что использовать](#%D0%9A%D0%BE%D0%B3%D0%B4%D0%B0%20%D1%87%D1%82%D0%BE%20%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C)
	- [Паттерн "Database" на ScriptableObject](#%D0%9F%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%20%22Database%22%20%D0%BD%D0%B0%20ScriptableObject)
	- [Особенность сериализации ScriptableObject в Editor vs Runtime](#%D0%9E%D1%81%D0%BE%D0%B1%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%81%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8%20ScriptableObject%20%D0%B2%20Editor%20vs%20Runtime)
	- [ScriptableObject как ивент-система](#ScriptableObject%20%D0%BA%D0%B0%D0%BA%20%D0%B8%D0%B2%D0%B5%D0%BD%D1%82-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0)
- [5. Кастомная сериализация: ISerializationCallbackReceiver](#5.%20%D0%9A%D0%B0%D1%81%D1%82%D0%BE%D0%BC%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F:%20ISerializationCallbackReceiver)
	- [Зачем нужен интерфейс](#%D0%97%D0%B0%D1%87%D0%B5%D0%BC%20%D0%BD%D1%83%D0%B6%D0%B5%D0%BD%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81)
	- [Сериализация Dictionary](#%D0%A1%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20Dictionary)
	- [Сериализация с преобразованием типов](#%D0%A1%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D1%81%20%D0%BF%D1%80%D0%B5%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%D0%BC%20%D1%82%D0%B8%D0%BF%D0%BE%D0%B2)
	- [Сериализация интерфейсов](#%D0%A1%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%D0%BE%D0%B2)
	- [Важные предостережения](#%D0%92%D0%B0%D0%B6%D0%BD%D1%8B%D0%B5%20%D0%BF%D1%80%D0%B5%D0%B4%D0%BE%D1%81%D1%82%D0%B5%D1%80%D0%B5%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F)
- [6. JSON и бинарная сериализация вне Unity](#6.%20JSON%20%D0%B8%20%D0%B1%D0%B8%D0%BD%D0%B0%D1%80%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B2%D0%BD%D0%B5%20Unity)
	- [JsonUtility](#JsonUtility)
	- [Newtonsoft Json.NET](#Newtonsoft%20Json.NET)
	- [Бинарная сериализация](#%D0%91%D0%B8%D0%BD%D0%B0%D1%80%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F)
	- [Сравнение подходов](#%D0%A1%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BF%D0%BE%D0%B4%D1%85%D0%BE%D0%B4%D0%BE%D0%B2)
- [7. Подводные камни: циклические ссылки, полиморфизм, null-значения](#7.%20%D0%9F%D0%BE%D0%B4%D0%B2%D0%BE%D0%B4%D0%BD%D1%8B%D0%B5%20%D0%BA%D0%B0%D0%BC%D0%BD%D0%B8:%20%D1%86%D0%B8%D0%BA%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8,%20%D0%BF%D0%BE%D0%BB%D0%B8%D0%BC%D0%BE%D1%80%D1%84%D0%B8%D0%B7%D0%BC,%20null-%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D1%8F)
	- [Циклические ссылки](#%D0%A6%D0%B8%D0%BA%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8)
	- [Полиморфизм и потеря типовой информации](#%D0%9F%D0%BE%D0%BB%D0%B8%D0%BC%D0%BE%D1%80%D1%84%D0%B8%D0%B7%D0%BC%20%D0%B8%20%D0%BF%D0%BE%D1%82%D0%B5%D1%80%D1%8F%20%D1%82%D0%B8%D0%BF%D0%BE%D0%B2%D0%BE%D0%B9%20%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%B8)
	- [Поведение null-значений](#%D0%9F%D0%BE%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20null-%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B9)
	- [Проблемы с переименованием полей](#%D0%9F%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D1%8B%20%D1%81%20%D0%BF%D0%B5%D1%80%D0%B5%D0%B8%D0%BC%D0%B5%D0%BD%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%D0%BC%20%D0%BF%D0%BE%D0%BB%D0%B5%D0%B9)
	- [Ловушка с конструкторами](#%D0%9B%D0%BE%D0%B2%D1%83%D1%88%D0%BA%D0%B0%20%D1%81%20%D0%BA%D0%BE%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D0%BE%D1%80%D0%B0%D0%BC%D0%B8)
- [8. Практические советы и best practices](#8.%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D1%81%D0%BE%D0%B2%D0%B5%D1%82%D1%8B%20%D0%B8%20best%20practices)
	- [1. Всегда используйте [SerializeField] вместо public для полей, которые нужны только в Inspector](#1.%20%D0%92%D1%81%D0%B5%D0%B3%D0%B4%D0%B0%20%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D1%83%D0%B9%D1%82%D0%B5%20%5BSerializeField%5D%20%D0%B2%D0%BC%D0%B5%D1%81%D1%82%D0%BE%20public%20%D0%B4%D0%BB%D1%8F%20%D0%BF%D0%BE%D0%BB%D0%B5%D0%B9,%20%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D1%8B%D0%B5%20%D0%BD%D1%83%D0%B6%D0%BD%D1%8B%20%D1%82%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE%20%D0%B2%20Inspector)
	- [2. Группируйте связанные данные в [Serializable] классы](#2.%20%D0%93%D1%80%D1%83%D0%BF%D0%BF%D0%B8%D1%80%D1%83%D0%B9%D1%82%D0%B5%20%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D0%B2%20%5BSerializable%5D%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D1%8B)
	- [3. Чётко разделяйте данные конфигурации и runtime-состояние](#3.%20%D0%A7%D1%91%D1%82%D0%BA%D0%BE%20%D1%80%D0%B0%D0%B7%D0%B4%D0%B5%D0%BB%D1%8F%D0%B9%D1%82%D0%B5%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D0%BA%D0%BE%D0%BD%D1%84%D0%B8%D0%B3%D1%83%D1%80%D0%B0%D1%86%D0%B8%D0%B8%20%D0%B8%20runtime-%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D0%B5)
	- [4. Используйте [FormerlySerializedAs] при рефакторинге](#4.%20%D0%98%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D1%83%D0%B9%D1%82%D0%B5%20%5BFormerlySerializedAs%5D%20%D0%BF%D1%80%D0%B8%20%D1%80%D0%B5%D1%84%D0%B0%D0%BA%D1%82%D0%BE%D1%80%D0%B8%D0%BD%D0%B3%D0%B5)
	- [5. Будьте осторожны с данными в PlayMode](#5.%20%D0%91%D1%83%D0%B4%D1%8C%D1%82%D0%B5%20%D0%BE%D1%81%D1%82%D0%BE%D1%80%D0%BE%D0%B6%D0%BD%D1%8B%20%D1%81%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%BC%D0%B8%20%D0%B2%20PlayMode)
	- [6. Паттерн инициализации для сложных структур данных](#6.%20%D0%9F%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%20%D0%B8%D0%BD%D0%B8%D1%86%D0%B8%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%BB%D0%BE%D0%B6%D0%BD%D1%8B%D1%85%20%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)
	- [7. Версионирование сериализованных данных](#7.%20%D0%92%D0%B5%D1%80%D1%81%D0%B8%D0%BE%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%81%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D0%B8%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D1%85%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)
	- [8. Editor-специфичная сериализация](#8.%20Editor-%D1%81%D0%BF%D0%B5%D1%86%D0%B8%D1%84%D0%B8%D1%87%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F)
	- [9. Тестирование сериализации](#9.%20%D0%A2%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%81%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8)
	- [10. Профилирование и оптимизация](#10.%20%D0%9F%D1%80%D0%BE%D1%84%D0%B8%D0%BB%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%B8%20%D0%BE%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F)
- [Заключение](#%D0%97%D0%B0%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B5)

## Введение

Сериализация — один из тех механизмов Unity, который разработчики используют постоянно, часто не осознавая этого. Каждый раз, когда вы видите поле в Inspector, сохраняете сцену или создаёте префаб, за кулисами работает система сериализации. Непонимание её принципов приводит к трудноотлаживаемым багам: данные не сохраняются, ссылки теряются, поведение в Editor отличается от Runtime. Эта статья разбирает механизм изнутри.

---

## 1. Что такое сериализация в Unity и зачем она нужна

### Фундаментальная проблема

Программа существует в оперативной памяти. Объекты — это адреса, указатели, графы ссылок. Когда вы закрываете Unity, вся эта структура исчезает. Сериализация — процесс преобразования объектов из памяти в линейный поток байт (или текст), который можно сохранить на диск и впоследствии восстановить.

Десериализация — обратный процесс: из потока данных воссоздаётся объектный граф в памяти.

### Где Unity использует сериализацию

Unity применяет сериализацию значительно шире, чем просто "сохранение файлов":

**Хранение данных проекта:**
- `.unity` файлы сцен
- `.prefab` файлы префабов
- `.asset` файлы ScriptableObject
- Мета-файлы и настройки проекта

**Работа Inspector:**
Когда вы изменяете значение в Inspector, Unity немедленно сериализует компонент и сохраняет изменение. Это объясняет, почему изменения в Inspector переживают перекомпиляцию скриптов — данные сериализуются до перекомпиляции и десериализуются после.

**Hot Reload скриптов:**
```csharp
Изменили скрипт → Unity сериализует все MonoBehaviour
→ Перекомпилирует сборку → Создаёт новые экземпляры
→ Десериализует сохранённые данные обратно
```

**Prefab система:**
Префаб хранит сериализованное состояние объекта. Instance на сцене хранит только *переопределения* (overrides) относительно базового префаба.

**Undo/Redo система:**
Каждое действие в Editor сериализует состояние объектов в стек истории.

**Передача данных между процессами:**
Unity Editor и Play Mode могут обмениваться сериализованными данными.

### Формат хранения

Unity использует собственный текстовый формат YAML для сцен и префабов (при включённом "Force " в настройках):

```csharp
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_Script: {fileID: 11500000, guid: abc123..., type: 3}
  m_Name: ''
  playerName: John
  health: 100
  position:
    x: 1
    y: 0
    z: 0
```

Понимание того, что данные хранятся именно так, объясняет многие ограничения системы — например, почему интерфейсы не сериализуются (YAML не знает, объект какого конкретного класса создавать при десериализации).

---

## 2. Как Unity сериализует данные: поля, типы, правила

### Базовые правила сериализации

Unity сериализует поле, если выполняются **все** следующие условия:

1. Поле `public`, **или** помечено атрибутом `[SerializeField]`
2. Поле **не** помечено атрибутом `[NonSerialized]`
3. Поле **не** `static`
4. Поле **не** `const`
5. Поле **не** `readonly` (только для полей, не для свойств)
6. Тип поля является сериализуемым

```csharp
public class PlayerStats : MonoBehaviour
{
    // ✅ Сериализуется: public поле сериализуемого типа
    public int health = 100;
    
    // ✅ Сериализуется: private + [SerializeField]
    [SerializeField] private float speed = 5f;
    
    // ❌ Не сериализуется: private без атрибута
    private string secretKey = "abc";
    
    // ❌ Не сериализуется: static поля — принадлежат классу, не экземпляру
    public static int instanceCount = 0;
    
    // ❌ Не сериализуется: const — значение встроено в IL-код компилятором
    public const int MAX_HEALTH = 200;
    
    // ❌ Не сериализуется: readonly — нет публичного сеттера для десериализатора
    public readonly int id = 42;
    
    // ❌ Не сериализуется: свойства (только поля!)
    public int Level { get; set; }
    
    // ❌ Не сериализуется: [NonSerialized] явно исключает поле
    [NonSerialized] public int runtimeCache;
}
```

### Сериализуемые типы

**Примитивные типы C#:**
```csharp
bool, byte, sbyte, char, decimal, double, float,
int, uint, long, ulong, short, ushort, string
```

**Встроенные типы Unity:**
```csharp
Vector2, Vector3, Vector4
Quaternion
Color, Color32
Rect, Bounds
AnimationCurve
Gradient
LayerMask
Matrix4x4
```

**Объекты Unity (UnityEngine.Object):**
```csharp
// Любые наследники UnityEngine.Object сериализуются как ссылки
public GameObject prefabReference;
public AudioClip sound;
public Material material;
public ure2D icon;
public MyScriptableObject config;
```

Важный нюанс: эти объекты сериализуются **по ссылке** (через GUID и fileID), а не по значению. Unity хранит идентификатор ассета, а не его содержимое.

**Массивы и списки:**
```csharp
public int[] scores;           // ✅ Массив сериализуемого типа
public List<string> names;     // ✅ List<T> поддерживается
public List<Vector3> waypoints; // ✅ List встроенных типов

// ❌ Не поддерживаются:
public Dictionary<string, int> stats;  // Словари
public int[,] grid;                    // Многомерные массивы
public List<List<int>> matrix;         // Вложенные списки
```

**Вложенные сериализуемые классы:**
```csharp
[System.Serializable]
public class WeaponStats
{
    public string weaponName;
    public int damage;
    public float fireRate;
}

public class Player : MonoBehaviour
{
    // ✅ Вложенный сериализуемый класс
    public WeaponStats primaryWeapon;
    public List<WeaponStats> inventory;
}
```

### Глубина сериализации

Unity имеет **жёсткое ограничение глубины сериализации — 7 уровней**. Это сделано для защиты от бесконечной рекурсии при циклических ссылках (которые Unity не умеет корректно обрабатывать для обычных классов).

```csharp
[System.Serializable]
public class Node
{
    public string value;
    public Node child; // Рекурсивная структура!
}
```

При глубине больше 7 Unity просто прекращает сериализацию и выводит предупреждение. Это не исключение — просто данные обрежутся. Именно поэтому деревья и графы на обычных классах нельзя сериализовать напрямую.

### Поведение при десериализации: важный нюанс

Понимание порядка инициализации критично:

```csharp
public class Enemy : MonoBehaviour
{
    public int health = 100; // Значение по умолчанию
    
    private void Awake()
    {
        // К моменту вызова Awake десериализация уже завершена.
        // Если в Inspector выставлено health = 50,
        // то здесь мы увидим 50, а не 100.
        Debug.Log(health); 
    }
}
```

Порядок инициализации MonoBehaviour:
1. Выделение памяти под объект
2. **Десериализация** — данные из файла сцены/префаба записываются в поля
3. `Awake()` → `OnEnable()` → `Start()`

Это значит, что значения "по умолчанию" в объявлении полей (`= 100`) работают только как значения по умолчанию **в Inspector**, когда компонент добавляется впервые. После первого сохранения сцены значение берётся из сериализованных данных.

---

## 3. Атрибуты: [SerializeField], [NonSerialized], [System.Serializable]

### [SerializeField]

Самый важный атрибут. Заставляет Unity сериализовать `private` или `protected` поле.

```csharp
public class PlayerController : MonoBehaviour
{
    [SerializeField] private float moveSpeed = 5f;
    [SerializeField] private Transform groundCheck;
    [SerializeField] private LayerMask groundLayer;
}
```

**Почему использовать `[SerializeField]` вместо `public`?**

Это вопрос инкапсуляции. `public` поле нарушает принцип сокрытия данных — любой код может изменить его напрямую. `[SerializeField]` с `private` полем даёт доступ к полю только через Inspector и методы класса:

```csharp
// ❌ Плохо: полное нарушение инкапсуляции
public class BadExample : MonoBehaviour
{
    public float health; // Любой класс может написать health = -999
}

// ✅ Хорошо: Inspector видит поле, внешний код — нет
public class GoodExample : MonoBehaviour
{
    [SerializeField] private float health = 100f;
    
    public float Health => health; // Только чтение снаружи
    
    public void TakeDamage(float damage)
    {
        health = Mathf.Max(0, health - damage); // Контролируемое изменение
    }
}
```

Ещё один тонкий момент: если вы хотите иметь свойство с публичным геттером и контролировать сериализацию через backing field:

```csharp
public class Character : MonoBehaviour
{
    [SerializeField] private int _level = 1;
    
    public int Level
    {
        get => _level;
        private set => _level = Mathf.Clamp(value, 1, 100);
    }
    
    public void LevelUp() => Level++;
}
```

### [NonSerialized]

Явно исключает `public` поле из сериализации:

```csharp
public class GameManager : MonoBehaviour
{
    // Сериализуется — отображается в Inspector
    public int score = 0;
    
    // НЕ сериализуется — runtime-only данные
    [NonSerialized] public bool isGameOver = false;
    [NonSerialized] public List<Enemy> activeEnemies = new List<Enemy>();
    [NonSerialized] public event Action OnScoreChanged;
}
```

**Когда использовать `[NonSerialized]`:**
- Runtime-кэши, вычисляемые значения
- Ссылки на объекты, которые существуют только во время игры
- Делегаты и события
- Данные, которые должны сбрасываться при каждом запуске

Важное отличие от `[HideInInspector]`:

```csharp
// [HideInInspector]: поле СКРЫТО в Inspector, но ВСЁ ЕЩЁ сериализуется
[HideInInspector] public int hiddenButSerialized = 42;

// [NonSerialized]: поле НЕ отображается И НЕ сериализуется
[NonSerialized] public int notSerializedAtAll = 42;
```

`[HideInInspector]` полезен, когда вам нужно хранить данные между сессиями редактора, но не показывать их пользователю.

### [System.Serializable]

Помечает пользовательский класс или структуру как сериализуемую. Без этого атрибута Unity не будет пытаться сериализовать экземпляры класса.

```csharp
// Без атрибута — Unity проигнорирует этот класс при сериализации
public class NotSerializable
{
    public int value; // Не появится в Inspector
}

// С атрибутом — Unity сериализует как встроенный объект
[System.Serializable]
public class ItemData
{
    public string itemName;
    public int quantity;
    public float weight;
    [SerializeField] private bool isEquipped;
}

public class Inventory : MonoBehaviour
{
    public ItemData equippedItem;        // Развернётся в Inspector
    public List<ItemData> items;         // Список с полным UI
}
```

**Важное понимание: встроенная сериализация vs ссылочная**

Классы помеченные `[System.Serializable]` сериализуются **по значению** (inline), как структуры. Это означает:

```csharp
[System.Serializable]
public class Stats
{
    public int strength;
    public int agility;
}

public class Fighter : MonoBehaviour
{
    public Stats baseStats;
    public Stats currentStats;
}
```

В сериализованных данных будет храниться **две копии** Stats. Если `baseStats` и `currentStats` указывают на один объект в коде — после десериализации они станут **разными объектами** с одинаковыми значениями. Это критически важно понимать!

```csharp
// Runtime: эта операция НЕ работает корректно после десериализации
public void ResetStats()
{
    currentStats = baseStats; // Создаёт копию значений, не ссылку!
    // currentStats и baseStats теперь независимы
}
```

### Дополнительные полезные атрибуты

```csharp
public class UIConfig : MonoBehaviour
{
    // Ограничение диапазона значений в Inspector
    [Range(0f, 1f)]
    [SerializeField] private float opacity = 1f;
    
    // Многострочный текст в Inspector
    [Area(3, 10)]
    public string description;
    
    // Заголовок секции в Inspector
    [Header("Combat Settings")]
    public int attackDamage;
    
    // Подсказка при наведении
    [Tooltip("Скорость в единицах в секунду")]
    public float moveSpeed;
    
    // Пространство между полями в Inspector
    [Space(10)]
    public bool isActive;
}
```

---

## 4. ScriptableObject vs MonoBehaviour сериализация

### Принципиальные различия

`MonoBehaviour` и `ScriptableObject` оба наследуются от `UnityEngine.Object` и используют одну систему сериализации. Разница не в том, **как** они сериализуются, а в том, **где** хранятся данные и каков их жизненный цикл.

| Аспект | MonoBehaviour | ScriptableObject |
|--------|--------------|-----------------|
| Хранение | В файле сцены/префаба | В отдельном `.asset` файле |
| Привязка | К GameObject | Независим |
| Количество копий | Одна на каждый GameObject | Один файл, множество ссылок |
| Создание | `AddComponent<T>()` | `ScriptableObject.CreateInstance<T>()` |
| Жизненный цикл | Вместе со сценой | Независим от сцены |

### Когда что использовать

**MonoBehaviour** — для данных, специфичных для конкретного экземпляра:
```csharp
public class Enemy : MonoBehaviour
{
    // Эти данные уникальны для ЭТОГО врага
    public float currentHealth;
    public Vector3 spawnPosition;
    public int killCount;
}
```

**ScriptableObject** — для данных-конфигураций, разделяемых между объектами:
```csharp
[CreateAssetMenu(fileName = "EnemyConfig", menuName = "Game/Enemy Config")]
public class EnemyConfig : ScriptableObject
{
    // Эти данные одинаковы для ВСЕХ врагов одного типа
    public float maxHealth;
    public float moveSpeed;
    public int experienceReward;
    public GameObject deathEffect;
}

public class Enemy : MonoBehaviour
{
    // Ссылка на конфигурацию — не копия данных, а ссылка на единый asset
    [SerializeField] private EnemyConfig config;
    
    private float currentHealth;
    
    private void Start()
    {
        currentHealth = config.maxHealth; // Берём из конфигурации
    }
}
```

### Паттерн "Database" на ScriptableObject

ScriptableObject отлично подходит для хранения коллекций данных:

```csharp
[System.Serializable]
public class ItemDefinition
{
    public int id;
    public string itemName;
    public Sprite icon;
    public ItemType type;
    public int baseDamage;
}

[CreateAssetMenu(fileName = "ItemDatabase", menuName = "Game/Item Database")]
public class ItemDatabase : ScriptableObject
{
    [SerializeField] private List<ItemDefinition> items;
    
    // Построим словарь при загрузке — но не сериализуем его
    [NonSerialized] private Dictionary<int, ItemDefinition> _lookupCache;
    
    private void OnEnable()
    {
        // OnEnable вызывается после десериализации
        BuildCache();
    }
    
    private void BuildCache()
    {
        _lookupCache = items.ToDictionary(item => item.id);
    }
    
    public ItemDefinition GetItem(int id)
    {
        if (_lookupCache == null) BuildCache();
        return _lookupCache.TryGetValue(id, out var item) ? item : null;
    }
}
```

### Особенность сериализации ScriptableObject в Editor vs Runtime

В Editor сериализованные данные ScriptableObject хранятся в `.asset` файле и живут всё время работы редактора. Изменения в PlayMode сохраняются в файл (это отличает ScriptableObject от MonoBehaviour — у MonoBehaviour изменения в PlayMode теряются при выходе).

Это поведение удобно для дизайнеров, но опасно для программистов:

```csharp
[CreateAssetMenu]
public class PlayerConfig : ScriptableObject
{
    public int startingGold = 100;
    
    // ⚠️ ОПАСНО: эта операция изменит asset на диске в Editor!
    public void SpendGold(int amount)
    {
        startingGold -= amount;
    }
}
```

Для Runtime-состояния лучше хранить данные отдельно:

```csharp
[CreateAssetMenu]
public class PlayerConfig : ScriptableObject
{
    // Конфигурационные данные (не изменяются)
    public int startingGold = 100;
    
    // Runtime-состояние (не сериализуется)
    [NonSerialized] public int currentGold;
    
    private void OnEnable()
    {
        // Инициализируем runtime-состояние из конфигурации
        currentGold = startingGold;
    }
}
```

### ScriptableObject как ивент-система

Продвинутый паттерн — использование ScriptableObject как канала событий:

```csharp
[CreateAssetMenu(menuName = "Events/Game Event")]
public class GameEvent : ScriptableObject
{
    [NonSerialized] private List<GameEventListener> _listeners = new();
    
    public void Raise()
    {
        for (int i = _listeners.Count - 1; i >= 0; i--)
            _listeners[i].OnEventRaised();
    }
    
    public void Register(GameEventListener listener) => _listeners.Add(listener);
    public void Unregister(GameEventListener listener) => _listeners.Remove(listener);
}
```

---

## 5. Кастомная сериализация: ISerializationCallbackReceiver

### Зачем нужен интерфейс

Стандартная система сериализации Unity не умеет сериализовать Dictionary, интерфейсы, многомерные массивы и другие сложные структуры. `ISerializationCallbackReceiver` позволяет конвертировать эти данные в сериализуемый формат и обратно.

```csharp
public interface ISerializationCallbackReceiver
{
    void OnBeforeSerialize();   // Вызывается ПЕРЕД сериализацией
    void OnAfterDeserialize();  // Вызывается ПОСЛЕ десериализации
}
```

### Сериализация Dictionary

Самый распространённый use-case:

```csharp
[System.Serializable]
public class SerializableDictionary<TKey, TValue> : 
    Dictionary<TKey, TValue>, ISerializationCallbackReceiver
{
    [SerializeField] private List<TKey> _keys = new List<TKey>();
    [SerializeField] private List<TValue> _values = new List<TValue>();
    
    // Unity вызывает этот метод перед записью в файл
    public void OnBeforeSerialize()
    {
        _keys.Clear();
        _values.Clear();
        
        foreach (var pair in this)
        {
            _keys.Add(pair.Key);
            _values.Add(pair.Value);
        }
    }
    
    // Unity вызывает этот метод после чтения из файла
    public void OnAfterDeserialize()
    {
        Clear();
        
        if (_keys.Count != _values.Count)
        {
            Debug.LogError($"Deserialization error: keys ({_keys.Count}) " +
                          $"and values ({_values.Count}) count mismatch");
            return;
        }
        
        for (int i = 0; i < _keys.Count; i++)
            Add(_keys[i], _values[i]);
    }
}

// Использование:
public class QuestManager : MonoBehaviour
{
    [SerializeField] 
    private SerializableDictionary<string, bool> questCompletion = new();
}
```

### Сериализация с преобразованием типов

Более сложный пример — хранение данных в одном формате, работа в другом:

```csharp
public class ColorPalette : MonoBehaviour, ISerializationCallbackReceiver
{
    // Рабочий формат: HEX-строки для удобства в Inspector
    [SerializeField] private List<string> hexColors = new List<string>();
    
    // Runtime формат: Color для работы в коде
    [NonSerialized] public List<Color> colors = new List<Color>();
    
    public void OnBeforeSerialize()
    {
        hexColors.Clear();
        foreach (var color in colors)
        {
            hexColors.Add(ColorUtility.ToHtmlStringRGBA(color));
        }
    }
    
    public void OnAfterDeserialize()
    {
        colors.Clear();
        foreach (var hex in hexColors)
        {
            if (ColorUtility.TryParseHtmlString("#" + hex, out Color color))
                colors.Add(color);
            else
                Debug.LogWarning($"Invalid hex color: {hex}");
        }
    }
}
```

### Сериализация интерфейсов

Одна из самых болезненных проблем — Unity не может сериализовать поля интерфейсного типа. Решение через `ISerializationCallbackReceiver`:

```csharp
public interface IDamageable
{
    void TakeDamage(float amount);
}

[System.Serializable]
public class SerializableInterface<T> where T : class
{
    [SerializeField] private UnityEngine.Object _serializedObject;
    [NonSerialized] private T _cachedInterface;
    
    public T Value
    {
        get
        {
            if (_cachedInterface == null && _serializedObject != null)
                _cachedInterface = _serializedObject as T;
            return _cachedInterface;
        }
        set
        {
            _cachedInterface = value;
            _serializedObject = value as UnityEngine.Object;
        }
    }
}

public class Turret : MonoBehaviour
{
    // Теперь можно назначить любой компонент, реализующий IDamageable
    [SerializeField] 
    private SerializableInterface<IDamageable> target;
    
    private void Update()
    {
        target.Value?.TakeDamage(10f * Time.deltaTime);
    }
}
```

### Важные предостережения

`OnAfterDeserialize` вызывается **не в основном потоке Unity**. Это означает, что вы не можете использовать большинство Unity API внутри него:

```csharp
public void OnAfterDeserialize()
{
    // ❌ НЕЛЬЗЯ — Unity API недоступно в этом потоке
    var obj = Instantiate(prefab);
    Debug.Log("test"); // Даже это может вызвать проблемы
    
    // ✅ МОЖНО — только работа с данными C#
    _lookup = new Dictionary<string, int>();
    for (int i = 0; i < _keys.Count; i++)
        _lookup[_keys[i]] = _values[i];
}

public void OnBeforeSerialize()
{
    // ✅ Этот метод вызывается в основном потоке
    // Здесь Unity API доступно
}
```

---

## 6. JSON и бинарная сериализация вне Unity

### JsonUtility

`JsonUtility` — встроенный инструмент Unity для JSON-сериализации. Он использует **ту же систему сериализации**, что и Inspector, поэтому правила сериализации аналогичны.

```csharp
[System.Serializable]
public class SaveData
{
    public string playerName;
    public int level;
    public float health;
    public List<string> unlockedAchievements;
    public Vector3 lastPosition;
}

public class SaveSystem : MonoBehaviour
{
    private const string SAVE_FILE = "save.json";
    
    public void Save(SaveData data)
    {
        string json = JsonUtility.ToJson(data, prettyPrint: true);
        string path = Path.Combine(Application.persistentDataPath, SAVE_FILE);
        File.WriteAll(path, json);
    }
    
    public SaveData Load()
    {
        string path = Path.Combine(Application.persistentDataPath, SAVE_FILE);
        
        if (!File.Exists(path))
            return new SaveData();
            
        string json = File.ReadAll(path);
        return JsonUtility.FromJson<SaveData>(json);
    }
    
    // Десериализация в существующий объект (без аллокации)
    public void LoadInto(SaveData existingData)
    {
        string path = Path.Combine(Application.persistentDataPath, SAVE_FILE);
        string json = File.ReadAll(path);
        JsonUtility.FromJsonOverwrite(json, existingData); // Перезаписывает поля
    }
}
```

**Ограничения JsonUtility:**

```csharp
// ❌ Dictionary не поддерживается
public Dictionary<string, int> stats; // Будет проигнорирован

// ❌ Полиморфизм не поддерживается
[System.Serializable]
public class Animal { public string name; }
[System.Serializable]  
public class Dog : Animal { public string breed; }

Animal animal = new Dog { name = "Rex", breed = "Husky" };
string json = JsonUtility.ToJson(animal);
// В JSON попадут только поля Animal, информация о Dog потеряется

// ❌ Свойства не сериализуются
public int Level { get; set; } // В JSON не попадёт

// ✅ Работает только с [System.Serializable] классами
// ✅ Работает с UnityEngine типами (Vector3, Color, etc.)
```

### Newtonsoft Json.NET

Для сложных случаев лучше использовать Newtonsoft Json.NET (доступен через Package Manager как "Newtonsoft Json" или входит в состав ряда пакетов):

```csharp
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

[System.Serializable]
public class GameState
{
    public string PlayerName { get; set; }
    public Dictionary<string, int> Resources { get; set; }
    public List<QuestData> ActiveQuests { get; set; }
}

public class AdvancedSaveSystem
{
    private static readonly JsonSerializerSettings Settings = new JsonSerializerSettings
    {
        Formatting = Formatting.Indented,
        NullValueHandling = NullValueHandling.Ignore,
        // Для полиморфизма — включаем запись типа в JSON
        TypeNameHandling = TypeNameHandling.Auto,
        ReferenceLoopHandling = ReferenceLoopHandling.Ignore
    };
    
    public void Save<T>(T data, string fileName)
    {
        string json = JsonConvert.SerializeObject(data, Settings);
        File.WriteAll(GetPath(fileName), json);
    }
    
    public T Load<T>(string fileName) where T : new()
    {
        string path = GetPath(fileName);
        if (!File.Exists(path)) return new T();
        
        string json = File.ReadAll(path);
        return JsonConvert.DeserializeObject<T>(json, Settings);
    }
    
    private string GetPath(string fileName) =>
        Path.Combine(Application.persistentDataPath, fileName + ".json");
}
```

**Полиморфизм с Newtonsoft:**

```csharp
[JsonObject]
public abstract class Ability
{
    public string Name { get; set; }
    public abstract void Execute();
}

[JsonObject]
public class FireballAbility : Ability
{
    public float Damage { get; set; }
    public override void Execute() => Debug.Log($"Fireball! {Damage} damage");
}

[JsonObject]
public class HealAbility : Ability
{
    public float HealAmount { get; set; }
    public override void Execute() => Debug.Log($"Heal! {HealAmount} HP");
}

// С TypeNameHandling.Auto JSON будет содержать информацию о типе:
// {
//   "$type": "FireballAbility, Assembly-",
//   "Damage": 50.0,
//   "Name": "Fireball"
// }

var settings = new JsonSerializerSettings
{
    TypeNameHandling = TypeNameHandling.Auto
};

List<Ability> abilities = new List<Ability>
{
    new FireballAbility { Name = "Fireball", Damage = 50f },
    new HealAbility { Name = "Heal", HealAmount = 30f }
};

string json = JsonConvert.SerializeObject(abilities, settings);
var restored = JsonConvert.DeserializeObject<List<Ability>>(json, settings);
// restored[0] будет FireballAbility, restored[1] — HealAbility ✅
```

### Бинарная сериализация

Для производительности или защиты данных можно использовать бинарные форматы:

**BinaryFormatter (устаревший, небезопасный):**
```csharp
// ⚠️ BinaryFormatter признан небезопасным (уязвимость к десериализационным атакам)
// и устарел в .NET 5+. Не используйте в новых проектах.
```

**System..Json (.NET 6+):**
```csharp
using System..Json;

public class ModernSaveSystem
{
    private static readonly JsonSerializerOptions Options = new JsonSerializerOptions
    {
        WriteIndented = true,
        IncludeFields = true, // Включить поля (не только свойства)
        PropertyNamingPolicy = JsonNamingPolicy.CamelCase
    };
    
    public async Task SaveAsync<T>(T data, string path)
    {
        using var stream = File.Create(path);
        await JsonSerializer.SerializeAsync(stream, data, Options);
    }
    
    public async Task<T> LoadAsync<T>(string path)
    {
        using var stream = File.OpenRead(path);
        return await JsonSerializer.DeserializeAsync<T>(stream, Options);
    }
}
```

**MessagePack для высокой производительности:**
```csharp
// MessagePack-: быстрая бинарная сериализация
[MessagePackObject]
public class PlayerSave
{
    [Key(0)] public string Name { get; set; }
    [Key(1)] public int Level { get; set; }
    [Key(2)] public float[] Position { get; set; } // Vector3 как массив
}

// Сериализация
byte[] bytes = MessagePackSerializer.Serialize(player);
// Десериализация
var restored = MessagePackSerializer.Deserialize<PlayerSave>(bytes);
```

### Сравнение подходов

| Метод | Читаемость | Скорость | Возможности | Безопасность |
|-------|-----------|---------|------------|-------------|
| JsonUtility | ✅ | ✅✅ | ⚠️ Ограниченные | ✅ |
| Newtonsoft | ✅ | ✅ | ✅✅ Полные | ✅ |
| System..Json | ✅ | ✅✅ | ✅ | ✅ |
| MessagePack | ❌ | ✅✅✅ | ✅ | ✅ |

---

## 7. Подводные камни: циклические ссылки, полиморфизм, null-значения

### Циклические ссылки

Одна из самых коварных проблем. Unity сериализатор не отслеживает посещённые объекты при обходе графа, что приводит к бесконечной рекурсии:

```csharp
[System.Serializable]
public class TreeNode
{
    public string value;
    public TreeNode left;   // Может создать цикл
    public TreeNode right;
    public TreeNode parent; // Прямой цикл: node.parent.left == node
}
```

При попытке сериализовать дерево с заполненными `parent` ссылками Unity либо упадёт в бесконечный цикл, либо достигнет лимита глубины (7) и тихо обрежет данные.

**Решения:**

```csharp
// Вариант 1: Хранить только индексы, не ссылки
[System.Serializable]
public class SerializableTreeNode
{
    public string value;
    public int leftIndex = -1;   // Индекс в массиве узлов
    public int rightIndex = -1;
    public int parentIndex = -1; // -1 = нет родителя
}

public class Tree : MonoBehaviour, ISerializationCallbackReceiver
{
    [SerializeField] private List<SerializableTreeNode> _serializedNodes = new();
    [NonSerialized] private TreeNode _root; // Runtime-представление
    
    public void OnBeforeSerialize()
    {
        _serializedNodes.Clear();
        FlattenTree(_root, _serializedNodes);
    }
    
    public void OnAfterDeserialize()
    {
        _root = BuildTree(_serializedNodes);
    }
    
    private void FlattenTree(TreeNode node, List<SerializableTreeNode> result)
    {
        // Обход дерева с присвоением индексов
        // ...
    }
}
```

```csharp
// Вариант 2: Использовать ScriptableObject для узлов
// (ссылки между SO сериализуются корректно через GUID)
[CreateAssetMenu]
public class DialogueNode : ScriptableObject
{
    public string ;
    public List<DialogueNode> choices; // Ссылки через GUID — безопасны
}
```

### Полиморфизм и потеря типовой информации

Unity сериализатор не поддерживает полиморфизм для обычных классов:

```csharp
[System.Serializable]
public class Shape { public Color color; }

[System.Serializable]
public class Circle : Shape { public float radius; }

[System.Serializable]
public class Rectangle : Shape { public float width, height; }

public class Canvas : MonoBehaviour
{
    // ⚠️ ПРОБЛЕМА: Будет сериализован только как Shape,
    // поля Circle/Rectangle потеряются!
    public List<Shape> shapes = new List<Shape>();
}
```

При добавлении `new Circle { color = Color.red, radius = 5f }` в список, после десериализации вы получите объект типа `Shape` с `color`, но без `radius`. Тип теряется.

**Решения:**

```csharp
// Вариант 1: ScriptableObject (ссылки сохраняют тип)
public abstract class Shape : ScriptableObject
{
    public Color color;
    public abstract void Draw();
}

[CreateAssetMenu]
public class Circle : Shape
{
    public float radius;
    public override void Draw() { /* ... */ }
}

public class Canvas : MonoBehaviour
{
    // ✅ Работает: ссылки на SO сохраняют конкретный тип
    public List<Shape> shapes;
}
```

```csharp
// Вариант 2: Discriminated Union через enum
[System.Serializable]
public class ShapeData
{
    public ShapeType type;
    public Color color;
    
    // Все возможные поля
    public float radius;    // Для Circle
    public float width;     // Для Rectangle  
    public float height;    // Для Rectangle
    
    // Фабричный метод
    public Shape CreateShape() => type switch
    {
        ShapeType.Circle => new Circle { color = color, radius = radius },
        ShapeType.Rectangle => new Rectangle { color = color, width = width, height = height },
        _ => throw new ArgumentOutOfRangeException()
    };
}
```

```csharp
// Вариант 3: Кастомная сериализация через JSON
public class Canvas : MonoBehaviour, ISerializationCallbackReceiver
{
    [SerializeField] private List<string> _shapeTypes = new();
    [SerializeField] private List<string> _shapeJsons = new();
    
    [NonSerialized] public List<Shape> shapes = new();
    
    public void OnBeforeSerialize()
    {
        _shapeTypes.Clear();
        _shapeJsons.Clear();
        
        foreach (var shape in shapes)
        {
            _shapeTypes.Add(shape.GetType().AssemblyQualifiedName);
            _shapeJsons.Add(JsonConvert.SerializeObject(shape));
        }
    }
    
    public void OnAfterDeserialize()
    {
        shapes.Clear();
        for (int i = 0; i < _shapeTypes.Count; i++)
        {
            var type = Type.GetType(_shapeTypes[i]);
            if (type != null)
                shapes.Add((Shape)JsonConvert.DeserializeObject(_shapeJsons[i], type));
        }
    }
}
```

### Поведение null-значений

Unity сериализатор обращается с null специфично:

```csharp
[System.Serializable]
public class Config
{
    public string serverUrl;     // null → "" после десериализации
    public int[] scores;         // null → [] (пустой массив)
    public List<string> tags;    // null → [] (пустой список)
}

public class GameSettings : MonoBehaviour
{
    public Config config; // null → новый Config() с дефолтными значениями!
}
```

Unity **не сохраняет null** для `[System.Serializable]` классов. При десериализации всегда создаётся новый экземпляр с дефолтными значениями. Это ломает паттерны типа "null как отсутствие значения":

```csharp
// ❌ Этот код не работает как ожидается:
public class Player : MonoBehaviour
{
    public WeaponData equippedWeapon; // Хотим null = "нет оружия"
    
    public bool HasWeapon() => equippedWeapon != null; 
    // После десериализации equippedWeapon никогда не null!
    // Unity создаст WeaponData() с пустыми значениями
}

// ✅ Решение: явный флаг
[System.Serializable]
public class WeaponData
{
    public bool isValid; // false = "нет оружия"
    public string weaponName;
    public int damage;
}
```

Исключение: ссылки на `UnityEngine.Object` (MonoBehaviour, ScriptableObject, GameObject и т.д.) правильно сериализуют null как отсутствие ссылки.

```csharp
public class Turret : MonoBehaviour
{
    public Transform target; // ✅ null корректно сериализуется и десериализуется
}
```

### Проблемы с переименованием полей

Сериализация в Unity основана на **именах полей**. Если вы переименуете поле, все сохранённые данные для него потеряются:

```csharp
// Было:
public int playerHp = 100; // Сохранено в файл сцены как "playerHp"

// Стало:
public int health = 100; // Unity не найдёт "health" в файле, установит 100
// ПОТЕРЯ ДАННЫХ: все кастомные значения в Inspector исчезнут!
```

**Решение: атрибут [FormerlySerializedAs]:**

```csharp
using UnityEngine.Serialization;

public class Player : MonoBehaviour
{
    // Переименовали поле, но старые данные всё ещё загрузятся
    [FormerlySerializedAs("playerHp")]
    [FormerlySerializedAs("hp")] // Можно указать несколько старых имён
    public int health = 100;
}
```

Это критически важно при рефакторинге проектов с большим количеством сцен и префабов.

### Ловушка с конструкторами

```csharp
[System.Serializable]
public class AudioSettings
{
    public float masterVolume = 1f;
    public float musicVolume = 0.8f;
    
    // ⚠️ Конструктор НЕ вызывается при десериализации!
    public AudioSettings()
    {
        Debug.Log("Constructor called"); // Не будет вызван из Inspector
        masterVolume = 0.5f; // Это не сработает при десериализации
    }
}
```

Unity создаёт объекты через `FormatterServices.GetUninitializedObject` или аналогичный механизм, минуя конструктор. Для инициализации после десериализации используйте `ISerializationCallbackReceiver.OnAfterDeserialize` или `Awake`/`OnEnable` для MonoBehaviour.

---

## 8. Практические советы и best practices

### 1. Всегда используйте [SerializeField] вместо public для полей, которые нужны только в Inspector

```csharp
// ❌
public class Enemy : MonoBehaviour
{
    public float health;       // Нарушает инкапсуляцию
    public float damage;
    public float moveSpeed;
}

// ✅
public class Enemy : MonoBehaviour
{
    [SerializeField] private float health;
    [SerializeField] private float damage;
    [SerializeField] private float moveSpeed;
    
    // Публичный интерфейс — только то, что нужно снаружи
    public float Health => health;
    public void TakeDamage(float amount) => health -= amount;
}
```

### 2. Группируйте связанные данные в [Serializable] классы

```csharp
// ❌ Плоская структура — неудобна в Inspector и коде
public class Character : MonoBehaviour
{
    public int baseStrength, baseAgility, baseIntelligence;
    public int currentStrength, currentAgility, currentIntelligence;
    public float baseAttackSpeed, currentAttackSpeed;
    public float baseCritChance, currentCritChance;
}

// ✅ Сгруппированная структура
[System.Serializable]
public class AttributeSet
{
    public int strength;
    public int agility;
    public int intelligence;
    
    public AttributeSet GetModified(AttributeSet modifier)
    {
        return new AttributeSet
        {
            strength = strength + modifier.strength,
            agility = agility + modifier.agility,
            intelligence = intelligence + modifier.intelligence
        };
    }
}

public class Character : MonoBehaviour
{
    [Header("Base Attributes")]
    [SerializeField] private AttributeSet baseAttributes;
    
    [Header("Current Attributes (Runtime)")]
    [NonSerialized] public AttributeSet currentAttributes;
    
    private void Start()
    {
        currentAttributes = baseAttributes;
    }
}
```

### 3. Чётко разделяйте данные конфигурации и runtime-состояние

```csharp
// Конфигурация — ScriptableObject, не изменяется во время игры
[CreateAssetMenu]
public class EnemyConfig : ScriptableObject
{
    public float maxHealth = 100f;
    public float damage = 10f;
    public float speed = 3f;
    public GameObject deathEffectPrefab;
}

// Runtime-состояние — MonoBehaviour
public class Enemy : MonoBehaviour
{
    [SerializeField] private EnemyConfig config; // Ссылка на конфиг
    
    // Runtime данные — не сериализуем (не нужно сохранять в префаб)
    [NonSerialized] private float currentHealth;
    [NonSerialized] private bool isDead;
    [NonSerialized] private Rigidbody rb;
    
    private void Awake()
    {
        rb = GetComponent<Rigidbody>();
        currentHealth = config.maxHealth;
    }
}
```

### 4. Используйте [FormerlySerializedAs] при рефакторинге

```csharp
// Правило: ВСЕГДА добавляйте [FormerlySerializedAs] при переименовании
// сериализованного поля, если проект имеет сохранённые сцены/префабы

using UnityEngine.Serialization;

public class Weapon : MonoBehaviour
{
    [FormerlySerializedAs("dmg")]
    [FormerlySerializedAs("attackDamage")]
    [SerializeField] private float damage = 10f; // Итоговое имя
}
```

### 5. Будьте осторожны с данными в PlayMode

```csharp
// В Editor в PlayMode изменения ScriptableObject СОХРАНЯЮТСЯ В ФАЙЛ
// В Build — нет (SO в Resources/Addressables читаются как readonly)

[CreateAssetMenu]
public class GameConfig : ScriptableObject
{
    public int startingLives = 3;
}

// ❌ В Editor это изменит asset на диске!
public class GameManager : MonoBehaviour
{
    [SerializeField] private GameConfig config;
    
    public void OnPlayerDied()
    {
        config.startingLives--; // Изменяет файл в Editor!
    }
}

// ✅ Хранить runtime-данные отдельно
public class GameManager : MonoBehaviour
{
    [SerializeField] private GameConfig config;
    
    [NonSerialized] private int currentLives;
    
    private void Start()
    {
        currentLives = config.startingLives; // Копируем значение
    }
    
    public void OnPlayerDied()
    {
        currentLives--; // Изменяем только runtime-переменную
    }
}
```

### 6. Паттерн инициализации для сложных структур данных

```csharp
public class LevelManager : MonoBehaviour
{
    [SerializeField] private List<LevelConfig> levels;
    
    // Словарь для быстрого доступа — не сериализуем
    private Dictionary<string, LevelConfig> _levelLookup;
    
    private void Awake()
    {
        // Строим кэш после десериализации
        InitializeLookup();
    }
    
    private void InitializeLookup()
    {
        _levelLookup = levels
            .Where(l => l != null && !string.IsNullOrEmpty(l.levelId))
            .ToDictionary(l => l.levelId, l => l);
    }
    
    #if UNITY_EDITOR
    // Валидация данных в Editor
    private void OnValidate()
    {
        // OnValidate вызывается при изменении данных в Inspector
        var ids = new HashSet<string>();
        foreach (var level in levels)
        {
            if (level == null) continue;
            if (!ids.Add(level.levelId))
                Debug.LogWarning($"Duplicate level ID: {level.levelId}", this);
        }
    }
    #endif
}
```

### 7. Версионирование сериализованных данных

При обновлении формата сохранений нужна стратегия миграции:

```csharp
[System.Serializable]
public class SaveData : ISerializationCallbackReceiver
{
    public int version = 2; // Текущая версия формата
    
    // Актуальные поля (версия 2)
    public string playerName;
    public int level;
    public List<string> skills;
    
    // Устаревшие поля (версия 1) — оставляем для миграции
    [FormerlySerializedAs("playerLevel")]
    [SerializeField] private int _oldLevel; // Было: playerLevel
    
    public void OnBeforeSerialize() { }
    
    public void OnAfterDeserialize()
    {
        // Миграция данных
        if (version < 2)
        {
            // Мигрируем данные из версии 1
            level = _oldLevel;
            skills = new List<string>(); // Новое поле, инициализируем дефолтом
            version = 2;
        }
    }
}
```

### 8. Editor-специфичная сериализация

Иногда нужно хранить данные только в Editor, не включая их в билд:

```csharp
public class LevelDesignHelper : MonoBehaviour
{
    // Данные только для редактора
    #if UNITY_EDITOR
    [SerializeField] private bool showDebugGizmos = true;
    [SerializeField] private Color gizmoColor = Color.yellow;
    #endif
    
    private void OnDrawGizmos()
    {
        #if UNITY_EDITOR
        if (!showDebugGizmos) return;
        Gizmos.color = gizmoColor;
        Gizmos.DrawWireSphere(transform.position, 1f);
        #endif
    }
}
```

### 9. Тестирование сериализации

Пишите тесты для проверки корректности сериализации:

```csharp
using NUnit.Framework;
using UnityEngine;

[TestFixture]
public class SerializationTests
{
    [Test]
    public void JsonUtility_PreservesPlayerData()
    {
        var original = new PlayerSaveData
        {
            playerName = "TestPlayer",
            level = 42,
            health = 85.5f,
            position = new Vector3(1, 2, 3)
        };
        
        string json = JsonUtility.ToJson(original);
        var restored = JsonUtility.FromJson<PlayerSaveData>(json);
        
        Assert.AreEqual(original.playerName, restored.playerName);
        Assert.AreEqual(original.level, restored.level);
        Assert.AreEqual(original.health, restored.health, 0.001f);
        Assert.AreEqual(original.position, restored.position);
    }
    
    [Test]
    public void SerializableDictionary_RoundTrip()
    {
        var dict = new SerializableDictionary<string, int>();
        dict["gold"] = 100;
        dict["wood"] = 50;
        
        // Симулируем сериализацию-десериализацию
        ((ISerializationCallbackReceiver)dict).OnBeforeSerialize();
        var dict2 = new SerializableDictionary<string, int>();
        // Копируем внутренние сериализованные данные...
        ((ISerializationCallbackReceiver)dict2).OnAfterDeserialize();
        
        Assert.AreEqual(dict["gold"], dict2["gold"]);
    }
}
```

### 10. Профилирование и оптимизация

Сериализация имеет стоимость. В критичных местах:

```csharp
public class OptimizedDataManager : MonoBehaviour
{
    // ❌ Дорого: частая сериализация больших структур
    private void Update()
    {
        // НЕ делайте это каждый кадр!
        string json = JsonUtility.ToJson(largeDataObject);
        File.WriteAll(path, json);
    }
    
    // ✅ Лучше: инкрементальное сохранение
    private Queue<SaveOperation> _pendingSaves = new Queue<SaveOperation>();
    
    private IEnumerator ProcessSaveQueue()
    {
        while (true)
        {
            if (_pendingSaves.Count > 0)
            {
                var op = _pendingSaves.Dequeue();
                op.Execute();
                yield return null; // Одна операция за кадр
            }
            else
            {
                yield return new WaitForSeconds(0.1f);
            }
        }
    }
    
    // ✅ Ещё лучше: асинхронное сохранение
    private async Task SaveAsync(object data, string path)
    {
        string json = await Task.Run(() => JsonUtility.ToJson(data));
        await File.WriteAllAsync(path, json);
    }
}
```

---

## Заключение

Система сериализации Unity — это одновременно мощный инструмент и источник неочевидных проблем. Ключевые принципы для запоминания:

**Понимайте ограничения:**
- Только поля (не свойства)
- Нет полиморфизма для plain классов
- Нет Dictionary, многомерных массивов
- Глубина — максимум 7 уровней
- Null для `[Serializable]` классов восстанавливается как new instance

**Проектируйте с учётом сериализации:**
- Разделяйте конфиг (ScriptableObject) и состояние (MonoBehaviour)
- Явно помечайте runtime-данные как `[NonSerialized]`
- Используйте `[FormerlySerializedAs]` при рефакторинге
- Версионируйте формат сохранений с самого начала

**Выбирайте правильный инструмент:**
- Встроенная сериализация → Inspector, префабы, сцены
- `JsonUtility` → простые save/load, без полиморфизма
- Newtonsoft → сложные структуры, полиморфизм, Dictionary
- `ISerializationCallbackReceiver` → конвертация несериализуемых структур

Понимание сериализации на глубоком уровне — это то, что отличает разработчика, который "делает так, чтобы работало" от разработчика, который понимает, **почему** это работает именно так, и может проектировать системы, которые не сломаются при рефакторинге, не потеряют данные при обновлении и будут корректно работать как в Editor, так и в Production.

# Практическое задание: Unity Serialization Mini-Project

## Цель задания

Закрепить теоретические знания о системе сериализации Unity через построение реальной игровой системы. По завершении всех заданий у вас будет рабочий инвентарь с предметами, система сохранения/загрузки состояния игрока и сериализуемый словарь характеристик — три компонента, встречающихся в большинстве реальных проектов.

**Что вы построите:** Систему управления персонажем RPG с инвентарём, сохранением прогресса и словарём характеристик.

**Предварительные требования:**
- Unity 2021.3 LTS или новее
- Базовое знание C# и Unity Inspector
- Прочитана теоретическая статья по Unity Serialization

**Структура проекта:**
```csharp
Assets/
├── Scripts/
│   ├── Task1/
│   │   ├── ItemData.cs
│   │   ├── Inventory.cs
│   │   └── InventoryUI.cs
│   ├── Task2/
│   │   ├── PlayerState.cs
│   │   ├── SaveSystem.cs
│   │   └── PlayerController.cs
│   └── Task3/
│       ├── SerializableDictionary.cs
│       ├── CharacterStats.cs
│       └── StatsDebugger.cs
├── Scenes/
│   ├── Task1_Inventory.unity
│   ├── Task2_SaveLoad.unity
│   └── Task3_Stats.unity
└── SaveData/          ← создастся автоматически
```

---

## Задание 1 — Базовый уровень: Инвентарь предметов

### Условие

Создайте систему инвентаря для RPG-персонажа. Каждый предмет должен иметь несколько характеристик, отображаться в Inspector в читаемом виде и поддерживать вложенные сериализуемые структуры. Никакого UI на экране не нужно — только корректное отображение данных в Inspector и вывод в консоль.

**Требования:**
1. Создать сериализуемый класс `ItemData` с полями: название, тип предмета (enum), урон/защита, вес, стоимость, флаг "экипирован"
2. Создать сериализуемый класс `ItemRequirements` — вложенная структура с требованиями к уровню и характеристикам персонажа
3. Класс `Inventory` (MonoBehaviour) должен содержать список предметов и слот для экипированного оружия
4. Метод `PrintInventory()` должен выводить все предметы в консоль в читаемом формате
5. Поля, которые не нужно редактировать через Inspector, должны быть скрыты

### Стартовый код-скелет

**`Scripts/Task1/ItemData.cs`**
```csharp
using UnityEngine;

namespace Task1
{
    // TODO 1.1: Добавьте атрибут, делающий этот класс сериализуемым для Unity Inspector.
    // Без него класс будет проигнорирован системой сериализации.
    public class ItemData
    {
        // TODO 1.2: Объявите поле itemName типа string.
        // Подсказка: должно быть видно в Inspector, но защищено от внешнего изменения кода.
        
        // TODO 1.3: Объявите поле itemType типа ItemType (enum ниже).
        
        // TODO 1.4: Объявите поле damage типа int с атрибутом Range от 0 до 500.
        
        // TODO 1.5: Объявите поле defense типа int с атрибутом Range от 0 до 300.
        
        // TODO 1.6: Объявите поле weight типа float.
        
        // TODO 1.7: Объявите поле goldCost типа int.
        
        // TODO 1.8: Объявите поле isEquipped типа bool.
        
        // TODO 1.9: Объявите поле requirements типа ItemRequirements (класс ниже).
        // Это вложенный сериализуемый объект — проверьте, что он отобразится в Inspector.
        
        // TODO 1.10: Добавьте публичное read-only свойство ItemName,
        // возвращающее itemName. Свойства НЕ сериализуются — убедитесь,
        // что данные берутся из сериализованного поля.
        public string ItemName => /* ваш код */ null;
        
        // TODO 1.11: Переопределите ToString() для красивого вывода в консоль.
        // Формат: "[ТИП] Название — DMG:X DEF:X W:X.Xkg COST:Xg [EQUIPPED]"
        // [EQUIPPED] добавлять только если isEquipped == true
        public override string ToString()
        {
            // Ваш код
            return "";
        }
    }
    
    // TODO 1.12: Объявите enum ItemType со значениями:
    // None, Weapon, Armor, Helmet, Boots, Accessory, Consumable
    public enum ItemType
    {
        // Ваш код
    }
    
    // TODO 1.13: Создайте сериализуемый класс ItemRequirements со следующими полями:
    // - requiredLevel (int, Range 1-100)
    // - requiredStrength (int, Range 0-100)  
    // - requiredAgility (int, Range 0-100)
    // - description (string, с атрибутом Area для многострочного ввода)
    public class ItemRequirements
    {
        // Ваш код
    }
}
```

**`Scripts/Task1/Inventory.cs`**
```csharp
using UnityEngine;
using System.Collections.Generic;

namespace Task1
{
    public class Inventory : MonoBehaviour
    {
        // TODO 1.14: Добавьте Header атрибут "=== Inventory Settings ===" над следующими полями.
        
        // TODO 1.15: Объявите приватное сериализуемое поле maxCapacity типа int
        // со значением по умолчанию 20 и Range от 1 до 100.
        
        // TODO 1.16: Объявите приватное сериализуемое поле ownerName типа string
        // со значением "Hero" и Tooltip "Имя владельца инвентаря".
        
        // TODO 1.17: Добавьте Header атрибут "=== Items ===" над следующими полями.
        
        // TODO 1.18: Объявите приватный сериализуемый List<ItemData> items.
        
        // TODO 1.19: Объявите приватное сериализуемое поле equippedWeapon типа ItemData.
        // Это "слот" для экипированного оружия — отдельно от основного списка.
        
        // TODO 1.20: Объявите публичное НЕсериализуемое поле lastAccessTime типа System.DateTime.
        // Это runtime-данные, их не нужно хранить между сессиями.
        // Подсказка: какой атрибут запрещает сериализацию public поля?
        
        // TODO 1.21: Объявите приватное поле _totalWeight типа float.
        // Оно вычисляется в runtime — не должно сериализоваться.
        
        private void Awake()
        {
            // TODO 1.22: Инициализируйте lastAccessTime текущим временем.
            // TODO 1.23: Вызовите RecalculateTotalWeight().
        }
        
        private void Start()
        {
            // TODO 1.24: Вызовите PrintInventory().
        }
        
        // TODO 1.25: Реализуйте метод AddItem(ItemData item).
        // Условия добавления:
        // - item не равен null
        // - текущее количество предметов меньше maxCapacity
        // При успехе: добавить в список, пересчитать вес, вывести лог.
        // При неудаче: вывести предупреждение с причиной.
        public bool AddItem(ItemData item)
        {
            // Ваш код
            return false;
        }
        
        // TODO 1.26: Реализуйте метод RemoveItem(string itemName).
        // Найти первый предмет с именем itemName, удалить его из списка,
        // пересчитать вес. Вернуть true если удалён, false если не найден.
        public bool RemoveItem(string itemName)
        {
            // Ваш код
            return false;
        }
        
        // TODO 1.27: Реализуйте метод EquipWeapon(string weaponName).
        // Найти оружие в списке по имени, проверить что его тип == Weapon,
        // если ранее было другое оружие — вернуть его в список,
        // установить новое оружие в equippedWeapon, выставить isEquipped = true.
        public bool EquipWeapon(string weaponName)
        {
            // Ваш код
            return false;
        }
        
        // TODO 1.28: Реализуйте приватный метод RecalculateTotalWeight().
        // Суммировать weight всех предметов в items + equippedWeapon (если не null).
        private void RecalculateTotalWeight()
        {
            // Ваш код
        }
        
        // TODO 1.29: Реализуйте метод PrintInventory().
        // Формат вывода:
        // ===== Инвентарь: [ownerName] =====
        // Вместимость: X/Y | Общий вес: X.Xkg
        // Экипировано: [название оружия или "ничего"]
        // --- Предметы ---
        // 1. [ToString() предмета]
        // 2. [ToString() предмета]
        // ...
        // =================================
        public void PrintInventory()
        {
            // Ваш код
        }
        
        // TODO 1.30: Добавьте метод OnValidate() — он вызывается в Editor
        // при изменении любого поля в Inspector.
        // Внутри: проверить что maxCapacity > 0, если нет — исправить до 1
        // и вывести предупреждение в консоль.
        #if UNITY_EDITOR
        private void OnValidate()
        {
            // Ваш код
        }
        #endif
    }
}
```

**`Scripts/Task1/InventoryTester.cs`** *(создайте самостоятельно)*
```csharp
using UnityEngine;

namespace Task1
{
    // TODO: Создайте MonoBehaviour для тестирования инвентаря.
    // В методе Start():
    // 1. Получить компонент Inventory через GetComponent
    // 2. Создать 3-4 предмета ItemData с разными параметрами
    //    (нельзя создавать через new в Editor — используйте заполнение в Inspector
    //     ИЛИ создавайте через ScriptableObject паттерн)
    // 3. Попытаться добавить предметы через AddItem()
    // 4. Экипировать одно из оружий через EquipWeapon()  
    // 5. Удалить один предмет через RemoveItem()
    // 6. Вызвать PrintInventory() и проверить вывод в консоли
}
```

### Ожидаемый результат

**В Inspector** вы должны увидеть:

```csharp
▼ Inventory (Script)
  === Inventory Settings ===
  Max Capacity    [ 20        ]
  Owner Name      [ Hero      ]
  === Items ===
  ▼ Items         (размер: 3)
    ▼ Element 0
        Item Name    [ Iron Sword  ]
        Item Type    [ Weapon      ]
        Damage       [====85====  ]  ← слайдер Range
        Defense      [==0======   ]
        Weight       [ 3.5        ]
        Gold Cost    [ 150        ]
        Is Equipped  [✓]
        ▼ Requirements
            Required Level    [=10=]
            Required Strength [=15=]
            Required Agility  [=5= ]
            Description [ Базовый меч для начинающих... ]
    ▼ Element 1
        ...
```

**В консоли** при запуске:
```csharp
===== Инвентарь: Hero =====
Вместимость: 3/20 | Общий вес: 8.5kg
Экипировано: Iron Sword
--- Предметы ---
1. [Armor] Iron Shield — DMG:0 DEF:45 W:5.0kg COST:200g
2. [Consumable] Health Potion — DMG:0 DEF:0 W:0.3kg COST:50g
=================================
```
*(Iron Sword не в списке — он в слоте equippedWeapon)*

---

## Задание 2 — Средний уровень: Сохранение состояния игрока

### Условие

Реализуйте полную систему сохранения и загрузки состояния игрока через `JsonUtility`. Система должна корректно работать с перезапуском игры: данные сохраняются в JSON-файл на диск и загружаются при старте. Отдельно реализуйте систему версионирования сохранений для обработки устаревших данных.

**Требования:**
1. Класс `PlayerState` — сериализуемый контейнер данных игрока (не MonoBehaviour)
2. Поддержка версионирования: если формат файла устарел — выполнить миграцию
3. Класс `SaveSystem` — статический менеджер с методами Save/Load/Delete
4. Класс `PlayerController` (MonoBehaviour) — использует SaveSystem, демонстрирует сохранение/загрузку
5. Обработка всех edge cases: файл не существует, файл повреждён, устаревшая версия

### Стартовый код-скелет

**`Scripts/Task2/PlayerState.cs`**
```csharp
using UnityEngine;
using System.Collections.Generic;

namespace Task2
{
    // TODO 2.1: Добавьте необходимый атрибут для сериализации JsonUtility.
    // JsonUtility использует ТУ ЖЕ систему, что и Inspector —
    // какой атрибут нужен классу, чтобы быть сериализуемым?
    public class PlayerState
    {
        // --- Мета-информация сохранения ---
        
        // TODO 2.2: Объявите константу CURRENT_VERSION типа int = 2.
        // Это текущая версия формата сохранения.
        
        // TODO 2.3: Объявите публичное поле version типа int.
        // Значение по умолчанию = CURRENT_VERSION.
        // Используется для определения необходимости миграции.
        
        // TODO 2.4: Объявите публичное поле saveTimestamp типа string.
        // Будет хранить время сохранения в формате ISO 8601.
        // Почему string, а не DateTime? Подсказка: JsonUtility и DateTime...
        
        // --- Данные персонажа (версия 1+) ---
        
        // TODO 2.5: Объявите поля:
        // playerName (string), currentLevel (int), currentExperience (int),
        // experienceToNextLevel (int), totalPlayTimeSeconds (float)
        
        // --- Характеристики (версия 1+) ---
        
        // TODO 2.6: Объявите поля:
        // maxHealth (float = 100f), currentHealth (float),
        // maxMana (float = 50f), currentMana (float),
        // strength (int = 10), agility (int = 10), intelligence (int = 10)
        
        // --- Позиция в мире (версия 1+) ---
        
        // TODO 2.7: Объявите поля:
        // position (Vector3), rotation (Quaternion), currentSceneName (string)
        // Почему Vector3 и Quaternion сериализуются JsonUtility без проблем?
        
        // --- Инвентарь (версия 1+) ---
        
        // TODO 2.8: Объявите поля:
        // gold (int), equippedWeaponName (string)
        // collectedItemIds — List<int> для хранения ID собранных предметов
        
        // --- Флаги прогресса (версия 2+, добавлено позже) ---
        
        // TODO 2.9: Объявите поля:
        // completedQuestIds — List<string>
        // unlockedAbilityIds — List<string>  
        // isDlcUnlocked (bool)
        // (эти поля появились в версии 2 формата)
        
        // --- Устаревшие поля (версия 1, удалены в версии 2) ---
        
        // TODO 2.10: Объявите приватное поле _legacyScore типа int.
        // В версии 1 было поле "score", в версии 2 его убрали.
        // Используйте атрибут [FormerlySerializedAs("score")] чтобы
        // данные версии 1 корректно загрузились в это поле для миграции.
        
        // --- Конструктор по умолчанию ---
        
        // TODO 2.11: Создайте статический фабричный метод CreateNew(string playerName).
        // Он должен создавать новое сохранение с дефолтными значениями:
        // version = CURRENT_VERSION, все листы инициализированы,
        // saveTimestamp = DateTime.UtcNow.ToString("O"),
        // experienceToNextLevel = 100, currentHealth = maxHealth, и т.д.
        public static PlayerState CreateNew(string playerName)
        {
            // Ваш код
            return null;
        }
        
        // TODO 2.12: Реализуйте метод Migrate().
        // Этот метод обновляет данные старых версий до текущего формата.
        // Логика:
        // if (version < 2):
        //   completedQuestIds = new List<string>()
        //   unlockedAbilityIds = new List<string>()
        //   isDlcUnlocked = false
        //   // _legacyScore мигрировать не нужно — просто отбрасываем
        //   version = 2
        // Обновить version до CURRENT_VERSION в конце.
        public void Migrate()
        {
            // Ваш код
        }
        
        // TODO 2.13: Реализуйте метод IsValid().
        // Проверяет базовую корректность данных:
        // - playerName не null и не пустой
        // - currentHealth >= 0
        // - currentLevel >= 1
        // - version > 0
        // Возвращает true если все проверки прошли.
        public bool IsValid()
        {
            // Ваш код
            return false;
        }
        
        public override string ToString()
        {
            // TODO 2.14: Реализуйте ToString() для вывода ключевой информации.
            // Формат: "PlayerState v{version}: {playerName} | Lvl:{level} | HP:{hp}/{maxHp}"
            return "";
        }
    }
}
```

**`Scripts/Task2/SaveSystem.cs`**
```csharp
using UnityEngine;
using System;
using System.IO;

namespace Task2
{
    public static class SaveSystem
    {
        // TODO 2.15: Объявите приватную константу SAVE_FILE_NAME = "player_save.json".
        
        // TODO 2.16: Объявите приватную константу BACKUP_FILE_NAME = "player_save.backup.json".
        
        // TODO 2.17: Объявите публичное статическое свойство SaveFilePath,
        // возвращающее полный путь: Path.Combine(Application.persistentDataPath, SAVE_FILE_NAME).
        // Почему Application.persistentDataPath, а не Application.dataPath?
        public static string SaveFilePath => /* ваш код */ "";
        
        // TODO 2.18: Реализуйте метод Save(PlayerState state).
        // Алгоритм:
        // 1. Проверить state на null, вывести ошибку и вернуться если null
        // 2. Обновить saveTimestamp до текущего времени
        // 3. Если файл сохранения уже существует — скопировать его как backup
        //    (это защита от повреждения при сбое во время записи)
        // 4. Сериализовать state в JSON через JsonUtility.ToJson(state, prettyPrint: true)
        // 5. Записать JSON в файл через File.WriteAll
        // 6. Вывести лог: "Game saved: {путь}" с временной меткой
        // 7. Обернуть всё в try-catch, при ошибке — вывести Debug.LogError
        public static void Save(PlayerState state)
        {
            // Ваш код
        }
        
        // TODO 2.19: Реализуйте метод Load().
        // Возвращает PlayerState или null при неудаче.
        // Алгоритм:
        // 1. Проверить существование файла. Если нет — вернуть null.
        // 2. Прочитать содержимое файла через File.ReadAll
        // 3. Десериализовать через JsonUtility.FromJson<PlayerState>
        // 4. Если результат null или !IsValid() — попробовать загрузить backup
        // 5. Если version != CURRENT_VERSION — вызвать Migrate()
        // 6. Вернуть загруженное состояние
        // 7. При любом Exception — вывести ошибку, попробовать backup, вернуть null
        public static PlayerState Load()
        {
            // Ваш код
            return null;
        }
        
        // TODO 2.20: Реализуйте приватный метод TryLoadBackup().
        // Аналогичен Load(), но читает из BACKUP_FILE_NAME.
        // Возвращает PlayerState или null.
        private static PlayerState TryLoadBackup()
        {
            // Ваш код
            return null;
        }
        
        // TODO 2.21: Реализуйте метод Delete().
        // Удаляет основной файл и backup если они существуют.
        // Выводит лог об удалении.
        public static void Delete()
        {
            // Ваш код
        }
        
        // TODO 2.22: Реализуйте метод SaveExists() — возвращает bool.
        public static bool SaveExists()
        {
            // Ваш код
            return false;
        }
        
        // TODO 2.23: Реализуйте метод GetSaveInfo().
        // Возвращает строку с информацией о сохранении (без полной загрузки):
        // "Save found: {имя файла} | Size: {размер в КБ} | Modified: {дата изменения}"
        // Если файл не существует: "No save file found"
        public static string GetSaveInfo()
        {
            // Ваш код
            return "";
        }
    }
}
```

**`Scripts/Task2/PlayerController.cs`**
```csharp
using UnityEngine;

namespace Task2
{
    public class PlayerController : MonoBehaviour
    {
        [SerializeField] private string defaultPlayerName = "Hero";
        
        // TODO 2.24: Объявите приватное поле _state типа PlayerState.
        // НЕ сериализуйте его — это runtime данные, загружаемые из файла.
        
        // TODO 2.25: Объявите публичное свойство только для чтения State => _state.
        
        private void Start()
        {
            // TODO 2.26: Реализуйте логику инициализации:
            // 1. Вывести GetSaveInfo() в лог
            // 2. Попытаться загрузить сохранение через SaveSystem.Load()
            // 3. Если загрузка вернула null — создать новое через PlayerState.CreateNew()
            // 4. Применить загруженные данные: 
            //    - переместить transform на state.position
            //    - установить transform.rotation = state.rotation
            // 5. Вывести в лог что загружено/создано
        }
        
        private void Update()
        {
            // TODO 2.27: Обработайте нажатия клавиш для тестирования:
            // F5  → вызвать QuickSave()
            // F9  → вызвать QuickLoad()  
            // Del → вызвать DeleteSave()
            // F1  → вывести _state.ToString() в Debug.Log
            // Стрелки → перемещать объект (обновлять _state.position каждый кадр)
        }
        
        // TODO 2.28: Реализуйте метод QuickSave().
        // Перед сохранением обновить в _state:
        // - position и rotation из transform
        // - currentSceneName из UnityEngine.SceneManagement.SceneManager.GetActiveScene().name
        // - totalPlayTimeSeconds += Time.timeSinceLevelLoad (примерный подсчёт)
        // Затем вызвать SaveSystem.Save(_state).
        private void QuickSave()
        {
            // Ваш код
        }
        
        // TODO 2.29: Реализуйте метод QuickLoad().
        // Загрузить состояние через SaveSystem.Load().
        // Если загружено успешно — применить к объекту.
        // Если нет — вывести предупреждение "No save data found".
        private void QuickLoad()
        {
            // Ваш код
        }
        
        // TODO 2.30: Реализуйте метод DeleteSave().
        // Вызвать SaveSystem.Delete().
        // После удаления создать новое дефолтное состояние через CreateNew.
        private void DeleteSave()
        {
            // Ваш код
        }
        
        // TODO 2.31: Добавьте вызов QuickSave() в OnApplicationPause(bool) и OnApplicationQuit().
        // Это обеспечит автосохранение при сворачивании приложения и выходе.
        
        // TODO 2.32: Реализуйте OnGUI() для отображения подсказок:
        // Отобразить текст в левом верхнем углу экрана:
        // "F5: Save | F9: Load | Del: Delete | F1: Print State"
        // "Player: {name} | Level: {level} | HP: {hp}/{maxHp}"
        // "Position: {position}"
        private void OnGUI()
        {
            // Ваш код
        }
    }
}
```

### Ожидаемый результат

**JSON-файл** (найдёте по пути `Application.persistentDataPath/player_save.json`):

```csharpjson
{
    "version": 2,
    "saveTimestamp": "2024-01-15T14:32:07.1234567Z",
    "playerName": "Hero",
    "currentLevel": 1,
    "currentExperience": 0,
    "experienceToNextLevel": 100,
    "totalPlayTimeSeconds": 47.3,
    "maxHealth": 100.0,
    "currentHealth": 100.0,
    "maxMana": 50.0,
    "currentMana": 50.0,
    "strength": 10,
    "agility": 10,
    "intelligence": 10,
    "position": {"x": 2.5, "y": 0.0, "z": -1.3},
    "rotation": {"x": 0.0, "y": 0.0, "z": 0.0, "w": 1.0},
    "currentSceneName": "Task2_SaveLoad",
    "gold": 0,
    "equippedWeaponName": "",
    "collectedItemIds": [],
    "completedQuestIds": [],
    "unlockedAbilityIds": [],
    "isDlcUnlocked": false
}
```

**Консоль при работе:**
```csharp
[SaveSystem] No save file found.
[PlayerController] Created new save for: Hero
[SaveSystem] Game saved: /Users/.../player_save.json (2024-01-15 14:32:07)
[SaveSystem] Backup created: player_save.backup.json
PlayerState v2: Hero | Lvl:1 | HP:100/100
```

**Дополнительно:** Напишите тест миграции — вручную создайте JSON файл версии 1 (без полей `completedQuestIds`, `isDlcUnlocked`, с полем `"score": 9999`) и убедитесь, что система загружает и мигрирует его корректно:

```csharpjson
{
    "version": 1,
    "playerName": "OldHero",
    "currentLevel": 5,
    "score": 9999,
    "currentHealth": 80.0,
    "maxHealth": 100.0
}
```

---

## Задание 3 — Продвинутый уровень: Сериализуемый словарь характеристик

### Условие

Реализуйте обобщённый сериализуемый словарь `SerializableDictionary<TKey, TValue>` с полной поддержкой Inspector и корректной обработкой всех edge-cases. На его основе постройте систему характеристик персонажа `CharacterStats`, которая поддерживает модификаторы (бафы/дебафы) и выводит данные в Inspector. Это задание требует глубокого понимания `ISerializationCallbackReceiver`.

**Требования:**
1. `SerializableDictionary<TKey, TValue>` — обобщённый класс с `ISerializationCallbackReceiver`
2. Обработка дубликатов ключей при десериализации (не крашиться, а восстанавливаться)
3. Обработка null-ключей
4. Система характеристик `CharacterStats` использует словарь для хранения базовых значений и модификаторов
5. `StatsDebugger` — MonoBehaviour для тестирования и визуализации в Inspector
6. Реализовать метод `GetFinalValue(StatType stat)` — базовое значение + сумма модификаторов

### Стартовый код-скелет

**`Scripts/Task3/SerializableDictionary.cs`**
```csharp
using UnityEngine;
using System;
using System.Collections.Generic;

namespace Task3
{
    // TODO 3.1: Добавьте атрибут [System.Serializable] к классу.
    // Почему без него словарь не появится в Inspector даже с ISerializationCallbackReceiver?
    
    // TODO 3.2: Объявите класс SerializableDictionary<TKey, TValue>,
    // наследующий Dictionary<TKey, TValue> и реализующий ISerializationCallbackReceiver.
    // Ограничение: TKey должен быть ненулевым (where TKey : notnull).
    public class SerializableDictionary // TODO: добавьте generics и наследование
    {
        // TODO 3.3: Объявите приватный сериализуемый List<TKey> _keys.
        // Атрибут: [SerializeField] — обязателен для private поля.
        
        // TODO 3.4: Объявите приватный сериализуемый List<TValue> _values.
        
        // TODO 3.5: Объявите приватное поле _duplicateKeysFound типа bool.
        // Используется для предупреждения в Editor. НЕ сериализуем.
        
        // TODO 3.6: Реализуйте OnBeforeSerialize().
        // Алгоритм:
        // 1. Очистить _keys и _values
        // 2. Пройти по всем парам в словаре (this)
        // 3. Добавить каждый ключ в _keys, каждое значение в _values
        // ВАЖНО: порядок _keys[i] должен строго соответствовать _values[i]
        public void OnBeforeSerialize()
        {
            // Ваш код
        }
        
        // TODO 3.7: Реализуйте OnAfterDeserialize().
        // Алгоритм:
        // 1. Очистить словарь (Clear())
        // 2. Проверить что _keys.Count == _values.Count.
        //    Если нет — вывести ошибку и выйти (не крашить игру!)
        // 3. Пройти по всем индексам:
        //    a. Получить ключ _keys[i]
        //    b. Проверить ключ на null (для reference types)
        //       Если null — пропустить с предупреждением
        //    c. Проверить дубликат через ContainsKey()
        //       Если дубликат — установить _duplicateKeysFound = true, пропустить
        //    d. Добавить пару в словарь
        // ВАЖНО: этот метод вызывается НЕ в основном потоке!
        // Нельзя использовать Debug.Log и большинство Unity API.
        // Используйте только чистый C#.
        public void OnAfterDeserialize()
        {
            // Ваш код
        }
        
        // TODO 3.8: Реализуйте метод GetOrDefault(TKey key, TValue defaultValue = default).
        // Безопасный доступ: вернуть значение или defaultValue если ключ не найден.
        public TValue GetOrDefault(TKey key, TValue defaultValue = default)
        {
            // Ваш код
            return defaultValue;
        }
        
        // TODO 3.9: Реализуйте метод TryAdd(TKey key, TValue value).
        // Добавить пару только если ключ не существует.
        // Вернуть true если добавлено, false если ключ уже есть.
        public bool TryAdd(TKey key, TValue value)
        {
            // Ваш код
            return false;
        }
        
        // TODO 3.10: Реализуйте свойство HasDuplicateWarning => _duplicateKeysFound.
        // Позволяет внешнему коду узнать, были ли проблемы при десериализации.
    }
}
```

**`Scripts/Task3/CharacterStats.cs`**
```csharp
using UnityEngine;
using System.Collections.Generic;

namespace Task3
{
    // Типы характеристик персонажа
    // TODO 3.11: Объявите enum StatType со значениями:
    // MaxHealth, HealthRegen, MaxMana, ManaRegen,
    // Strength, Agility, Intelligence,
    // AttackSpeed, MoveSpeed, CriticalChance, CriticalDamage,
    // Armor, MagicResistance
    public enum StatType { }
    
    // TODO 3.12: Объявите [System.Serializable] класс StatModifier:
    // - source (string) — источник модификатора ("Sword +2", "Poison Debuff", etc.)
    // - value (float) — величина модификации (может быть отрицательной)
    // - isPercentage (bool) — процентный или абсолютный модификатор
    // - expirationTime (float) — время истечения (0 = бессрочный)
    // Добавьте метод IsExpired() — возвращает true если expirationTime > 0 и время вышло
    // Подсказка: используйте Time.time для проверки, но помните о потоке в OnAfterDeserialize!
    
    // TODO 3.13: Объявите [System.Serializable] класс StatModifierList,
    // оборачивающий List<StatModifier>. Это нужно для создания словаря вида:
    // Dictionary<StatType, List<StatModifier>> — вложенные списки не сериализуются,
    // но Dictionary<StatType, StatModifierList> — сериализуется через наш словарь!
    // Добавьте:
    // - неявный оператор преобразования из List<StatModifier>
    // - индексатор this[int i]
    // - свойство Count
    // - метод Add(StatModifier modifier)
    // - метод RemoveExpired() — удалить все истёкшие модификаторы
    
    // TODO 3.14: Объявите конкретные типы словарей (не generic) через наследование.
    // Это необходимо — Unity не может отобразить generic класс в Inspector напрямую.
    // [System.Serializable]
    // public class StatValueDictionary : SerializableDictionary<StatType, float> { }
    //
    // [System.Serializable]  
    // public class StatModifierDictionary : SerializableDictionary<StatType, StatModifierList> { }
    
    // TODO 3.15: Добавьте необходимый атрибут сериализации к классу CharacterStats.
    public class CharacterStats : MonoBehaviour
    {
        // TODO 3.16: Объявите [Header("Base Stats")] и приватное сериализуемое
        // поле _baseStats типа StatValueDictionary.
        // В Inspector вы сможете задать базовые значения для каждой характеристики.
        
        // TODO 3.17: Объявите [Header("Active Modifiers")] и приватное сериализуемое
        // поле _modifiers типа StatModifierDictionary.
        // Здесь будут храниться активные бафы/дебафы.
        
        // TODO 3.18: Объявите приватный НЕсериализуемый кэш _cachedFinalStats
        // типа Dictionary<StatType, float>.
        // Это вычисляемые значения — не нужно их сохранять.
        
        // TODO 3.19: Объявите приватный bool _cacheDirty = true.
        // Флаг инвалидации кэша — когда true, финальные значения нужно пересчитать.
        
        private void Awake()
        {
            // TODO 3.20: Инициализируйте _cachedFinalStats как новый Dictionary.
            // Вызовите InitializeDefaultStats() для заполнения базовых значений
            // если _baseStats пустой (первый запуск).
        }
        
        // TODO 3.21: Реализуйте метод InitializeDefaultStats().
        // Заполните _baseStats дефолтными значениями если они не заданы в Inspector:
        // MaxHealth=100, HealthRegen=1, MaxMana=50, ManaRegen=0.5,
        // Strength=10, Agility=10, Intelligence=10,
        // AttackSpeed=1.0, MoveSpeed=5.0, CriticalChance=0.05, CriticalDamage=1.5,
        // Armor=0, MagicResistance=0
        // Используйте TryAdd() чтобы не перезаписывать настроенные в Inspector значения!
        private void InitializeDefaultStats()
        {
            // Ваш код
        }
        
        // TODO 3.22: Реализуйте метод GetBaseValue(StatType stat).
        // Вернуть базовое значение из _baseStats или 0 если не найдено.
        public float GetBaseValue(StatType stat)
        {
            // Ваш код
            return 0f;
        }
        
        // TODO 3.23: Реализуйте метод GetFinalValue(StatType stat).
        // Это ключевой метод! Алгоритм:
        // 1. Если _cacheDirty — вызвать RecalculateCache()
        // 2. Вернуть значение из _cachedFinalStats[stat] или базовое если нет в кэше
        public float GetFinalValue(StatType stat)
        {
            // Ваш код
            return 0f;
        }
        
        // TODO 3.24: Реализуйте приватный метод RecalculateCache().
        // Алгоритм для каждого StatType:
        // 1. Взять базовое значение
        // 2. Найти все модификаторы для этого типа (из _modifiers)
        // 3. Удалить истёкшие модификаторы (RemoveExpired())
        // 4. Сначала применить абсолютные модификаторы (isPercentage == false): value += mod.value
        // 5. Затем применить процентные модификаторы: value *= (1 + mod.value)
        // 6. Сохранить результат в _cachedFinalStats
        // 7. Установить _cacheDirty = false
        private void RecalculateCache()
        {
            // Ваш код
        }
        
        // TODO 3.25: Реализуйте метод AddModifier(StatType stat, StatModifier modifier).
        // 1. Получить или создать StatModifierList для данного типа в _modifiers
        // 2. Добавить модификатор
        // 3. Инвалидировать кэш (_cacheDirty = true)
        public void AddModifier(StatType stat, StatModifier modifier)
        {
            // Ваш код
        }
        
        // TODO 3.26: Реализуйте метод RemoveModifiersBySource(string source).
        // Удалить все модификаторы от указанного источника во всех характеристиках.
        // Инвалидировать кэш.
        public void RemoveModifiersBySource(string source)
        {
            // Ваш код
        }
        
        // TODO 3.27: Реализуйте метод SetBaseValue(StatType stat, float value).
        // Установить новое базовое значение, инвалидировать кэш.
        public void SetBaseValue(StatType stat, float value)
        {
            // Ваш код
        }
        
        // TODO 3.28: Реализуйте метод PrintAllStats().
        // Для каждого значения StatType вывести в консоль:
        // "[StatType]: Base={базовое} Final={финальное} (модификаторов: N)"
        public void PrintAllStats()
        {
            // Ваш код
        }
    }
}
```

**`Scripts/Task3/StatsDebugger.cs`**
```csharp
using UnityEngine;

namespace Task3
{
    // TODO 3.29: Создайте MonoBehaviour StatsDebugger.
    // Поля (все сериализуемые):
    // - _stats (CharacterStats) — ссылка на компонент
    // - _testModifierSource (string = "Test Buff")
    // - _testModifierValue (float = 10f)
    // - _testModifierStat (StatType = StatType.Strength)
    // - _testIsPercentage (bool = false)
    // - _testDuration (float = 0f, 0 = бессрочный)
    
    public class StatsDebugger : MonoBehaviour
    {
        // TODO 3.30: В Start() вызвать _stats.PrintAllStats() и проверить
        // что словарь в Inspector совпадает с выводом в консоли.
        
        private void Update()
        {
            // TODO 3.31: Обработайте нажатия клавиш:
            // Q → AddModifier с настроенными параметрами, вывести новое финальное значение
            // W → RemoveModifiersBySource(_testModifierSource), вывести финальное значение
            // E → PrintAllStats()
            // R → SetBaseValue(_testModifierStat, Random.Range(1f, 100f)), PrintAllStats()
            
            // TODO 3.32: Каждые 5 секунд автоматически вызывать PrintAllStats()
            // чтобы видеть как истекают временные модификаторы.
            // Подсказка: используйте Time.time % 5 < Time.deltaTime
        }
        
        // TODO 3.33: Реализуйте OnGUI() с отображением:
        // - Всех финальных значений характеристик
        // - Количества активных модификаторов для каждой характеристики
        // - Подсказки по клавишам
        private void OnGUI()
        {
            // Ваш код
        }
    }
}
```

### Ожидаемый результат

**В Inspector** компонент CharacterStats:
```csharp
▼ Character Stats (Script)
  ▼ Base Stats
    ▼ Keys          (размер: 13)
      Element 0     MaxHealth
      Element 1     HealthRegen
      ...
    ▼ Values        (размер: 13)
      Element 0     100
      Element 1     1
      ...
  ▼ Active Modifiers
    ▼ Keys          (размер: 0)
    ▼ Values        (размер: 0)
```

**В консоли** при PrintAllStats():
```csharp
[MaxHealth]:         Base=100   Final=100.0  (модификаторов: 0)
[HealthRegen]:       Base=1     Final=1.0    (модификаторов: 0)
[Strength]:          Base=10    Final=10.0   (модификаторов: 0)
...

// После добавления модификатора (Q):
[Strength]:          Base=10    Final=20.0   (модификаторов: 1)

// После добавления процентного модификатора +50%:
[Strength]:          Base=10    Final=30.0   (модификаторов: 2)
// Расчёт: (10 + 10) * (1 + 0.5) = 30 ✅
```

**Тест на дубликаты** (ручной): добавьте в Inspector одинаковые ключи в секцию Keys словаря — система должна загрузиться без ошибок, дубликат проигнорирован, в `HasDuplicateWarning` стоит true.

---

## Критерии проверки

### Задание 1 — Базовый уровень ✓

```csharp
□ ItemData помечен [System.Serializable] и отображается в Inspector
□ Все поля ItemData видны в Inspector с корректными виджетами (слайдеры для Range)
□ ItemRequirements отображается как вложенная структура в Inspector
□ [Area] работает для многострочного поля description
□ Приватные поля с [SerializeField] видны в Inspector
□ Публичные поля с [NonSerialized] не видны в Inspector  
□ Static и const поля отсутствуют в Inspector
□ Свойство ItemName возвращает данные из сериализованного поля, не из property
□ Метод PrintInventory() выводит корректно форматированный текст
□ OnValidate() срабатывает при изменении maxCapacity в Inspector
□ equippedWeapon корректно перемещается из списка в слот через EquipWeapon()
□ RecalculateTotalWeight() учитывает equippedWeapon
□ lastAccessTime имеет [NonSerialized] и инициализируется в Awake, не в объявлении
```

### Задание 2 — Средний уровень ✓

```csharp
□ JsonUtility.ToJson() генерирует валидный JSON со всеми полями
□ Vector3 и Quaternion корректно сериализуются/десериализуются
□ DateTime хранится как string (JsonUtility не поддерживает DateTime напрямую)
□ [FormerlySerializedAs("score")] корректно мигрирует _legacyScore из старых файлов
□ Migrate() вызывается автоматически при несовпадении версий
□ IsValid() возвращает false для повреждённых данных
□ Backup создаётся перед каждым сохранением (файл присутствует на диске)
□ При повреждении основного файла система загружает backup
□ Автосохранение срабатывает в OnApplicationQuit
□ F5/F9 работают корректно: данные сохраняются и восстанавливаются
□ После Delete нового CreateNew создаётся с дефолтными значениями
□ JSON-файл версии 1 (без поля completedQuestIds) загружается и мигрирует без ошибок
□ SaveFilePath указывает на persistentDataPath, не на dataPath
```

### Задание 3 — Продвинутый уровень ✓

```csharp
□ SerializableDictionary отображается в Inspector (ключи и значения видны)
□ Изменения в Inspector сохраняются после перекомпиляции скриптов
□ OnBeforeSerialize синхронизирует данные из Dictionary в _keys/_values
□ OnAfterDeserialize восстанавливает Dictionary из _keys/_values
□ Дубликат ключа в Inspector не вызывает Exception — тихо игнорируется
□ Null ключ в Inspector не вызывает NullReferenceException
□ Несовпадение _keys.Count != _values.Count обрабатывается с ошибкой, не крашем
□ _duplicateKeysFound устанавливается в true при дубликатах
□ GetFinalValue учитывает как абсолютные, так и процентные модификаторы
□ Порядок применения: сначала абсолютные, потом процентные
□ Истёкшие модификаторы удаляются при пересчёте, не вызывают ошибок
□ _cacheDirty инвалидируется при добавлении/удалении модификаторов и изменении базы
□ StatModifierList используется для обхода ограничения вложенных списков
□ PrintAllStats() совпадает с данными видными в Inspector
□ RemoveModifiersBySource удаляет модификаторы из ВСЕХ характеристик
```

---

## Частые ошибки новичков

### Ошибка 1: Забытый [System.Serializable]

```csharp
// ❌ Класс без атрибута — Inspector покажет пустое поле или вообще ничего
public class ItemData
{
    public string name;
}

// ✅ С атрибутом — Inspector разворачивает поля
[System.Serializable]
public class ItemData
{
    public string name;
}
```

**Симптом:** Поле типа `ItemData` в Inspector отображается как `None` или пустой блок, все вложенные поля отсутствуют. Нет ошибок в консоли — Unity просто молча игнорирует несериализуемый тип.

---

### Ошибка 2: Сериализация свойств вместо полей

```csharp
// ❌ Свойства НЕ сериализуются — в Inspector не появится
[SerializeField] public int Health { get; set; }

// ✅ Только поля сериализуются
[SerializeField] private int health;
public int Health => health;
```

**Симптом:** Свойство с `[SerializeField]` не вызывает ошибок компиляции, но не появляется в Inspector и не сохраняется. Значение всегда равно дефолтному.

---

### Ошибка 3: Ожидание null от [System.Serializable] объектов

```csharp
// ❌ Так не работает — после десериализации это никогда не null
public class Enemy : MonoBehaviour
{
    public WeaponConfig weapon; // [Serializable] class
    
    public bool HasWeapon()
    {
        return weapon != null; // ВСЕГДА true после десериализации!
    }
}

// ✅ Используйте явный флаг
[System.Serializable]
public class WeaponConfig
{
    public bool isAssigned;
    public string weaponName;
}

public bool HasWeapon() => weapon.isAssigned;
```

**Симптом:** Проверка `if (equippedWeapon == null)` всегда ложная, даже если в Inspector поле выглядит пустым. Unity создаёт `new WeaponConfig()` с дефолтными значениями вместо null.

---

### Ошибка 4: Использование Unity API в OnAfterDeserialize

```csharp
// ❌ КРАШ или непредсказуемое поведение — вызов Unity API из неосновного потока
public void OnAfterDeserialize()
{
    Debug.Log("Loaded!"); // Может вызвать ошибку
    var go = Instantiate(prefab); // КРАШ
    StartCoroutine(Init()); // КРАШ
    
    // Даже это опасно:
    _lookup = items.ToDictionary(i => i.id); // ✅ Это безопасно — чистый C#
}

// ✅ Только операции с данными C# без Unity API
public void OnAfterDeserialize()
{
    _lookup = new Dictionary<int, ItemData>();
    for (int i = 0; i < _keys.Count; i++)
    {
        if (!_lookup.ContainsKey(_keys[i]))
            _lookup[_keys[i]] = _values[i];
    }
    // Логирование — только через флаг, вывести в Awake/Start
    _hasDeserializationWarnings = _keys.Count != _values.Count;
}

private void Awake()
{
    if (_hasDeserializationWarnings)
        Debug.LogWarning("Dictionary had issues during deserialization!", this);
}
```

**Симптом:** `InvalidOperationException: set_isPlaying can only be called from the main thread`, `ArgumentException` или полный краш Unity при открытии сцены.

---

### Ошибка 5: Потеря данных при переименовании поля

```csharp
// Версия 1 скрипта — было поле:
public int playerHp = 100;

// Версия 2 — переименовали:
public int health = 100;
// РЕЗУЛЬТАТ: все кастомные значения из Inspector сброшены в 100!
// Unity ищет поле "health" в файле сцены, не находит, берёт default.

// ✅ Правильный рефакторинг:
using UnityEngine.Serialization;

[FormerlySerializedAs("playerHp")]
public int health = 100;
// Теперь Unity найдёт "playerHp" в старых данных и загрузит в "health"
```

**Симптом:** После переименования поля все значения в Inspector на префабах и сценах сброшены. Никаких ошибок нет — данные тихо теряются.

---

### Ошибка 6: Изменение данных ScriptableObject в PlayMode

```csharp
// ❌ В Editor это изменит ФАЙЛ НА ДИСКЕ
public class EnemyConfig : ScriptableObject
{
    public int health = 100;
}

public class Enemy : MonoBehaviour
{
    [SerializeField] private EnemyConfig config;
    
    private void Start()
    {
        config.health = 80; // В Editor: изменяет asset файл!
        // После выхода из PlayMode — health останется 80 в файле
    }
}

// ✅ Работать с копией значений
public class Enemy : MonoBehaviour
{
    [SerializeField] private EnemyConfig config;
    [NonSerialized] private int _currentHealth; // Runtime-копия
    
    private void Start()
    {
        _currentHealth = config.health; // Копируем, не изменяем
    }
}
```

**Симптом:** Значения в ScriptableObject меняются "сами по себе" после тестирования. Дизайнеры жалуются, что данные "слетают" после запуска игры.

---

### Ошибка 7: Неправильный порядок инициализации

```csharp
// ❌ Конструктор вызывается ДО десериализации
[System.Serializable]
public class AudioManager : MonoBehaviour
{
    public float volume = 0.8f;
    
    // Конструктор MonoBehaviour НЕ вызывается стандартным образом Unity
    // Данные из Inspector ещё не загружены в момент "конструкции" объекта
}

// ❌ Неправильная инициализация зависимых данных
public class GameManager : MonoBehaviour
{
    [SerializeField] private List<LevelData> levels;
    
    // ❌ ОШИБКА: levels ещё null в объявлении!
    // Эта строка выполняется ДО десериализации в некоторых контекстах
    private Dictionary<int, LevelData> _levelLookup = 
        levels.ToDictionary(l => l.id); // NullReferenceException!
    
    // ✅ ПРАВИЛЬНО: инициализировать в Awake — после десериализации
    private Dictionary<int, LevelData> _levelLookup;
    
    private void Awake()
    {
        // К этому моменту levels уже десериализован
        _levelLookup = levels.ToDictionary(l => l.id);
    }
}
```

**Симптом:** `NullReferenceException` при старте сцены в строках, которые "выглядят нормально". Проблема в том, что инициализация поля выполняется раньше, чем Unity десериализует данные.

---

### Ошибка 8: Отсутствие обработки ошибок в SaveSystem

```csharp
// ❌ Хрупкий код — любая проблема крашит игру
public static PlayerState Load()
{
    string json = File.ReadAll(SaveFilePath); // FileNotFoundException если нет файла
    return JsonUtility.FromJson<PlayerState>(json); // NullReferenceException если JSON кривой
}

// ✅ Устойчивый код
public static PlayerState Load()
{
    if (!File.Exists(SaveFilePath))
    {
        Debug.Log("[SaveSystem] No save file found.");
        return null;
    }
    
    try
    {
        string json = File.ReadAll(SaveFilePath);
        
        if (string.IsNullOrWhiteSpace(json))
        {
            Debug.LogWarning("[SaveSystem] Save file is empty.");
            return TryLoadBackup();
        }
        
        var state = JsonUtility.FromJson<PlayerState>(json);
        
        if (state == null || !state.IsValid())
        {
            Debug.LogWarning("[SaveSystem] Save file is corrupted, trying backup.");
            return TryLoadBackup();
        }
        
        if (state.version != PlayerState.CURRENT_VERSION)
            state.Migrate();
            
        return state;
    }
    catch (Exception e)
    {
        Debug.LogError($"[SaveSystem] Failed to load save: {e.Message}");
        return TryLoadBackup();
    }
}
```

**Симптом:** Игра вылетает при запуске если файл сохранения повреждён или отсутствует. На мобильных устройствах — частый сценарий при нехватке памяти во время записи.

---

## Итоговая проверка проекта

После выполнения всех заданий пройдите финальный чеклист:

```csharp
ЗАДАНИЕ 1:
□ Создан GameObject с компонентами Inventory + InventoryTester
□ В Inspector настроены минимум 4 предмета разных типов
□ При запуске консоль показывает корректный вывод инвентаря
□ Смена maxCapacity в Inspector на 0 показывает предупреждение

ЗАДАНИЕ 2:
□ Нажатие F5 создаёт JSON файл в папке persistentDataPath
□ Перезапуск сцены загружает сохранённую позицию объекта
□ Ручное удаление полей из JSON не крашит игру
□ Файл версии 1 мигрирует до версии 2 без потери основных данных

ЗАДАНИЕ 3:
□ CharacterStats отображает все 13 характеристик в Inspector
□ Добавление модификатора (Q) немедленно меняет финальное значение
□ Временный модификатор (duration > 0) исчезает через указанное время
□ Ручное добавление дубликата ключа в Inspector не крашит Unity
□ После перекомпиляции скриптов данные в словаре сохраняются
```