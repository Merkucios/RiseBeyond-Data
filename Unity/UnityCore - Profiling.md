# Profiling в Unity: найти и уничтожить проблемы производительности

---
# Содержание

- [Введение: три секунды, которые убивают игру](#%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5:%20%D1%82%D1%80%D0%B8%20%D1%81%D0%B5%D0%BA%D1%83%D0%BD%D0%B4%D1%8B,%20%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D1%8B%D0%B5%20%D1%83%D0%B1%D0%B8%D0%B2%D0%B0%D1%8E%D1%82%20%D0%B8%D0%B3%D1%80%D1%83)
- [Содержание](#%D0%A1%D0%BE%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D0%BD%D0%B8%D0%B5)
- [Как работает Unity под капотом](#%D0%9A%D0%B0%D0%BA%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D0%B5%D1%82%20Unity%20%D0%BF%D0%BE%D0%B4%20%D0%BA%D0%B0%D0%BF%D0%BE%D1%82%D0%BE%D0%BC)
	- [Игровой цикл и бюджет кадра](#%D0%98%D0%B3%D1%80%D0%BE%D0%B2%D0%BE%D0%B9%20%D1%86%D0%B8%D0%BA%D0%BB%20%D0%B8%20%D0%B1%D1%8E%D0%B4%D0%B6%D0%B5%D1%82%20%D0%BA%D0%B0%D0%B4%D1%80%D0%B0)
	- [Managed и Native память](#Managed%20%D0%B8%20Native%20%D0%BF%D0%B0%D0%BC%D1%8F%D1%82%D1%8C)
	- [CPU-bound vs GPU-bound: фундаментальная диагностика](#CPU-bound%20vs%20GPU-bound:%20%D1%84%D1%83%D0%BD%D0%B4%D0%B0%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%B4%D0%B8%D0%B0%D0%B3%D0%BD%D0%BE%D1%81%D1%82%D0%B8%D0%BA%D0%B0)
- [Инструменты профилирования](#%D0%98%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D1%80%D0%BE%D1%84%D0%B8%D0%BB%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F)
	- [Unity Profiler: анатомия главного инструмента](#Unity%20Profiler:%20%D0%B0%D0%BD%D0%B0%D1%82%D0%BE%D0%BC%D0%B8%D1%8F%20%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0)
	- [ProfilerRecorder: метрики без накладных расходов](#ProfilerRecorder:%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%B1%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%BA%D0%BB%D0%B0%D0%B4%D0%BD%D1%8B%D1%85%20%D1%80%D0%B0%D1%81%D1%85%D0%BE%D0%B4%D0%BE%D0%B2)
	- [Memory Profiler Package: глубокий анализ памяти](#Memory%20Profiler%20Package:%20%D0%B3%D0%BB%D1%83%D0%B1%D0%BE%D0%BA%D0%B8%D0%B9%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20%D0%BF%D0%B0%D0%BC%D1%8F%D1%82%D0%B8)
	- [Frame Debugger: рентген рендеринга](#Frame%20Debugger:%20%D1%80%D0%B5%D0%BD%D1%82%D0%B3%D0%B5%D0%BD%20%D1%80%D0%B5%D0%BD%D0%B4%D0%B5%D1%80%D0%B8%D0%BD%D0%B3%D0%B0)
	- [Сравнение инструментов](#%D0%A1%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2)
- [Garbage Collector: главный подозреваемый](#Garbage%20Collector:%20%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D1%8B%D0%B9%20%D0%BF%D0%BE%D0%B4%D0%BE%D0%B7%D1%80%D0%B5%D0%B2%D0%B0%D0%B5%D0%BC%D1%8B%D0%B9)
	- [Как GC решает когда работать](#%D0%9A%D0%B0%D0%BA%20GC%20%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D1%82%20%D0%BA%D0%BE%D0%B3%D0%B4%D0%B0%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D1%82%D1%8C)
	- [Что вызывает аллокации: полный каталог](#%D0%A7%D1%82%D0%BE%20%D0%B2%D1%8B%D0%B7%D1%8B%D0%B2%D0%B0%D0%B5%D1%82%20%D0%B0%D0%BB%D0%BB%D0%BE%D0%BA%D0%B0%D1%86%D0%B8%D0%B8:%20%D0%BF%D0%BE%D0%BB%D0%BD%D1%8B%D0%B9%20%D0%BA%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3)
- [Чеклист первого профилирования](#%D0%A7%D0%B5%D0%BA%D0%BB%D0%B8%D1%81%D1%82%20%D0%BF%D0%B5%D1%80%D0%B2%D0%BE%D0%B3%D0%BE%20%D0%BF%D1%80%D0%BE%D1%84%D0%B8%D0%BB%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F)
	- [ШАГ 1 — Подготовка (5 минут)](#%D0%A8%D0%90%D0%93%201%20%E2%80%94%20%D0%9F%D0%BE%D0%B4%D0%B3%D0%BE%D1%82%D0%BE%D0%B2%D0%BA%D0%B0%20(5%20%D0%BC%D0%B8%D0%BD%D1%83%D1%82))
	- [ШАГ 2 — Первичный снимок (10 минут)](#%D0%A8%D0%90%D0%93%202%20%E2%80%94%20%D0%9F%D0%B5%D1%80%D0%B2%D0%B8%D1%87%D0%BD%D1%8B%D0%B9%20%D1%81%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20(10%20%D0%BC%D0%B8%D0%BD%D1%83%D1%82))
	- [ШАГ 3 — CPU анализ (15 минут)](#%D0%A8%D0%90%D0%93%203%20%E2%80%94%20CPU%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20(15%20%D0%BC%D0%B8%D0%BD%D1%83%D1%82))
	- [ШАГ 4 — Memory анализ (10 минут)](#%D0%A8%D0%90%D0%93%204%20%E2%80%94%20Memory%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20(10%20%D0%BC%D0%B8%D0%BD%D1%83%D1%82))
	- [ШАГ 5 — Rendering анализ (10 минут)](#%D0%A8%D0%90%D0%93%205%20%E2%80%94%20Rendering%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20(10%20%D0%BC%D0%B8%D0%BD%D1%83%D1%82))
	- [ШАГ 6 — Синтез (5 минут)](#%D0%A8%D0%90%D0%93%206%20%E2%80%94%20%D0%A1%D0%B8%D0%BD%D1%82%D0%B5%D0%B7%20(5%20%D0%BC%D0%B8%D0%BD%D1%83%D1%82))
- [Практика: диагностика и лечение](#%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0:%20%D0%B4%D0%B8%D0%B0%D0%B3%D0%BD%D0%BE%D1%81%D1%82%D0%B8%D0%BA%D0%B0%20%D0%B8%20%D0%BB%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D0%B5)
	- [Проблема 1: String concatenation в Update](#%D0%9F%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0%201:%20String%20concatenation%20%D0%B2%20Update)
	- [Проблема 2: LINQ в горячем пути](#%D0%9F%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0%202:%20LINQ%20%D0%B2%20%D0%B3%D0%BE%D1%80%D1%8F%D1%87%D0%B5%D0%BC%20%D0%BF%D1%83%D1%82%D0%B8)
	- [Проблема 3: GetComponent в Update](#%D0%9F%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0%203:%20GetComponent%20%D0%B2%20Update)
	- [Проблема 4: Instantiate/Destroy вместо Object Pool](#%D0%9F%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0%204:%20Instantiate/Destroy%20%D0%B2%D0%BC%D0%B5%D1%81%D1%82%D0%BE%20Object%20Pool)
	- [Проблема 5: Физика и Layer Collision Matrix](#%D0%9F%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0%205:%20%D0%A4%D0%B8%D0%B7%D0%B8%D0%BA%D0%B0%20%D0%B8%20Layer%20Collision%20Matrix)
- [Паттерны оптимизации](#%D0%9F%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%D1%8B%20%D0%BE%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8)
	- [Span< T >: работа с данными без копирования](#Span%3CT%3E:%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%20%D1%81%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%BC%D0%B8%20%D0%B1%D0%B5%D0%B7%20%D0%BA%D0%BE%D0%BF%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F)
	- [Устранение boxing: правильные обобщения](#%D0%A3%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%20boxing:%20%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D0%BE%D0%B1%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D1%8F)
	- [Правильные корутины: избегаем аллокаций](#%D0%9F%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D0%BA%D0%BE%D1%80%D1%83%D1%82%D0%B8%D0%BD%D1%8B:%20%D0%B8%D0%B7%D0%B1%D0%B5%D0%B3%D0%B0%D0%B5%D0%BC%20%D0%B0%D0%BB%D0%BB%D0%BE%D0%BA%D0%B0%D1%86%D0%B8%D0%B9)
- [GPU: когда проблема не в коде](#GPU:%20%D0%BA%D0%BE%D0%B3%D0%B4%D0%B0%20%D0%BF%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0%20%D0%BD%D0%B5%20%D0%B2%20%D0%BA%D0%BE%D0%B4%D0%B5)
	- [Batching: объединение draw calls](#Batching:%20%D0%BE%D0%B1%D1%8A%D0%B5%D0%B4%D0%B8%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%20draw%20calls)
	- [Overdraw: лишняя работа Fragment Shader](#Overdraw:%20%D0%BB%D0%B8%D1%88%D0%BD%D1%8F%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%20Fragment%20Shader)
- [Мифы об оптимизации в Unity](#%D0%9C%D0%B8%D1%84%D1%8B%20%D0%BE%D0%B1%20%D0%BE%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8%20%D0%B2%20Unity)
	- [Миф 1: «Надо оптимизировать каждую строчку кода»](#%D0%9C%D0%B8%D1%84%201:%20%C2%AB%D0%9D%D0%B0%D0%B4%D0%BE%20%D0%BE%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%20%D0%BA%D0%B0%D0%B6%D0%B4%D1%83%D1%8E%20%D1%81%D1%82%D1%80%D0%BE%D1%87%D0%BA%D1%83%20%D0%BA%D0%BE%D0%B4%D0%B0%C2%BB)
	- [Миф 2: «Update() дорогой, надо использовать корутины»](#%D0%9C%D0%B8%D1%84%202:%20%C2%ABUpdate()%20%D0%B4%D0%BE%D1%80%D0%BE%D0%B3%D0%BE%D0%B9,%20%D0%BD%D0%B0%D0%B4%D0%BE%20%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%20%D0%BA%D0%BE%D1%80%D1%83%D1%82%D0%B8%D0%BD%D1%8B%C2%BB)
	- [Миф 3: «GameObject.Find дорогой, надо его избегать везде»](#%D0%9C%D0%B8%D1%84%203:%20%C2%ABGameObject.Find%20%D0%B4%D0%BE%D1%80%D0%BE%D0%B3%D0%BE%D0%B9,%20%D0%BD%D0%B0%D0%B4%D0%BE%20%D0%B5%D0%B3%D0%BE%20%D0%B8%D0%B7%D0%B1%D0%B5%D0%B3%D0%B0%D1%82%D1%8C%20%D0%B2%D0%B5%D0%B7%D0%B4%D0%B5%C2%BB)
	- [Миф 4: «Математика с float медленная, надо использовать int»](#%D0%9C%D0%B8%D1%84%204:%20%C2%AB%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0%20%D1%81%20float%20%D0%BC%D0%B5%D0%B4%D0%BB%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F,%20%D0%BD%D0%B0%D0%B4%D0%BE%20%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%20int%C2%BB)
	- [Миф 5: «Debug.Log не влияет на производительность в релизе»](#%D0%9C%D0%B8%D1%84%205:%20%C2%ABDebug.Log%20%D0%BD%D0%B5%20%D0%B2%D0%BB%D0%B8%D1%8F%D0%B5%D1%82%20%D0%BD%D0%B0%20%D0%BF%D1%80%D0%BE%D0%B8%D0%B7%D0%B2%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%B2%20%D1%80%D0%B5%D0%BB%D0%B8%D0%B7%D0%B5%C2%BB)
	- [Миф 6: «Camera.main дорогой — надо кэшировать»](#%D0%9C%D0%B8%D1%84%206:%20%C2%ABCamera.main%20%D0%B4%D0%BE%D1%80%D0%BE%D0%B3%D0%BE%D0%B9%20%E2%80%94%20%D0%BD%D0%B0%D0%B4%D0%BE%20%D0%BA%D1%8D%D1%88%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%C2%BB)
	- [Миф 7: «OnGUI надо полностью избегать»](#%D0%9C%D0%B8%D1%84%207:%20%C2%ABOnGUI%20%D0%BD%D0%B0%D0%B4%D0%BE%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D1%82%D1%8C%D1%8E%20%D0%B8%D0%B7%D0%B1%D0%B5%D0%B3%D0%B0%D1%82%D1%8C%C2%BB)
	- [Миф 8: «Больше скриптов = медленнее»](#%D0%9C%D0%B8%D1%84%208:%20%C2%AB%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%B5%20%D1%81%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B2%20=%20%D0%BC%D0%B5%D0%B4%D0%BB%D0%B5%D0%BD%D0%BD%D0%B5%D0%B5%C2%BB)
- [Таблица: Проблема → Причина → Решение](#%D0%A2%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0:%20%D0%9F%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0%20%E2%86%92%20%D0%9F%D1%80%D0%B8%D1%87%D0%B8%D0%BD%D0%B0%20%E2%86%92%20%D0%A0%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D0%B5)
- [Чеклист production-ready проекта](#%D0%A7%D0%B5%D0%BA%D0%BB%D0%B8%D1%81%D1%82%20production-ready%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
	- [Блок A: Профилирование и измерения](#%D0%91%D0%BB%D0%BE%D0%BA%20A:%20%D0%9F%D1%80%D0%BE%D1%84%D0%B8%D0%BB%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%B8%20%D0%B8%D0%B7%D0%BC%D0%B5%D1%80%D0%B5%D0%BD%D0%B8%D1%8F)
	- [Блок B: Memory Management](#%D0%91%D0%BB%D0%BE%D0%BA%20B:%20Memory%20Management)
	- [Блок C: CPU Performance](#%D0%91%D0%BB%D0%BE%D0%BA%20C:%20CPU%20Performance)
	- [Блок D: Rendering](#%D0%91%D0%BB%D0%BE%D0%BA%20D:%20Rendering)
	- [Блок E: Build настройки](#%D0%91%D0%BB%D0%BE%D0%BA%20E:%20Build%20%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B8)
	- [Блок F: Workflow и процесс](#%D0%91%D0%BB%D0%BE%D0%BA%20F:%20Workflow%20%D0%B8%20%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D1%81%D1%81)
- [Ресурсы](#%D0%A0%D0%B5%D1%81%D1%83%D1%80%D1%81%D1%8B)
	- [Официальная документация](#%D0%9E%D1%84%D0%B8%D1%86%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D1%8F)
	- [Книги](#%D0%9A%D0%BD%D0%B8%D0%B3%D0%B8)
	- [Видео и курсы](#%D0%92%D0%B8%D0%B4%D0%B5%D0%BE%20%D0%B8%20%D0%BA%D1%83%D1%80%D1%81%D1%8B)
	- [Инструменты](#%D0%98%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B)
	- [Статьи и блоги](#%D0%A1%D1%82%D0%B0%D1%82%D1%8C%D0%B8%20%D0%B8%20%D0%B1%D0%BB%D0%BE%D0%B3%D0%B8)
- [Заключение](#%D0%97%D0%B0%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B5)


## Введение: три секунды, которые убивают игру

Представьте сцену. Финальный босс. Игрок час прорывался сквозь уровень, здоровье на излёте, пальцы напряжены. Момент атаки — и игра замирает на полсекунды. Фриз. Потом всё продолжается как ни в чём не бывало, но магия уже разрушена. Игрок умирает не от босса — от дёргания анимации в критический момент. Закрывает игру. Оставляет отзыв: _«Лагает»_.

Это не гипотетический сценарий. Это происходит с каждой второй игрой, выходящей без серьёзного этапа профилирования. И самое болезненное: фриз длился 480 миллисекунд. Меньше полсекунды. Но именно в этот момент Garbage Collector решил убраться в куче памяти, накопившейся за час игры.

Причина? Строка кода, написанная три месяца назад:



```csharp
void Update()
{
    status. = "HP: " + currentHP + "/" + maxHP; // невинная строчка
}
```

Sixty frames per second. Sixty new string objects per second. За час — 216 000 объектов в памяти, ожидающих сборщика мусора. И он пришёл. Ровно в момент финального босса.

Эта статья — о том, как находить такие проблемы до того, как их найдут игроки. О инструментах, методологии, паттернах и мышлении, которое отличает разработчика, пишущего «работающий» код, от разработчика, пишущего код, который _остаётся рабочим_ при любых условиях.

Профилирование — это не финальный этап разработки. Это культура.

---

## Содержание

- [Как работает Unity под капотом](https://arena.ai/c/019e2600-c239-76dc-858a-23ea0adb456c#%D0%BA%D0%B0%D0%BA-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D0%B5%D1%82-unity-%D0%BF%D0%BE%D0%B4-%D0%BA%D0%B0%D0%BF%D0%BE%D1%82%D0%BE%D0%BC)
- [Инструменты профилирования](https://arena.ai/c/019e2600-c239-76dc-858a-23ea0adb456c#%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B-%D0%BF%D1%80%D0%BE%D1%84%D0%B8%D0%BB%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F)
- [Garbage Collector: главный подозреваемый](https://arena.ai/c/019e2600-c239-76dc-858a-23ea0adb456c#garbage-collector-%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D1%8B%D0%B9-%D0%BF%D0%BE%D0%B4%D0%BE%D0%B7%D1%80%D0%B5%D0%B2%D0%B0%D0%B5%D0%BC%D1%8B%D0%B9)
- [Чеклист первого профилирования](https://arena.ai/c/019e2600-c239-76dc-858a-23ea0adb456c#%D1%87%D0%B5%D0%BA%D0%BB%D0%B8%D1%81%D1%82-%D0%BF%D0%B5%D1%80%D0%B2%D0%BE%D0%B3%D0%BE-%D0%BF%D1%80%D0%BE%D1%84%D0%B8%D0%BB%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F)
- [Практика: диагностика и лечение](https://arena.ai/c/019e2600-c239-76dc-858a-23ea0adb456c#%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0-%D0%B4%D0%B8%D0%B0%D0%B3%D0%BD%D0%BE%D1%81%D1%82%D0%B8%D0%BA%D0%B0-%D0%B8-%D0%BB%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D0%B5)
- [Паттерны оптимизации](https://arena.ai/c/019e2600-c239-76dc-858a-23ea0adb456c#%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%D1%8B-%D0%BE%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8)
- [GPU: когда проблема не в коде](https://arena.ai/c/019e2600-c239-76dc-858a-23ea0adb456c#gpu-%D0%BA%D0%BE%D0%B3%D0%B4%D0%B0-%D0%BF%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0-%D0%BD%D0%B5-%D0%B2-%D0%BA%D0%BE%D0%B4%D0%B5)
- [Мифы об оптимизации в Unity](https://arena.ai/c/019e2600-c239-76dc-858a-23ea0adb456c#%D0%BC%D0%B8%D1%84%D1%8B-%D0%BE%D0%B1-%D0%BE%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8-%D0%B2-unity)
- [Таблица: Проблема → Причина → Решение](https://arena.ai/c/019e2600-c239-76dc-858a-23ea0adb456c#%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0-%D0%BF%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0--%D0%BF%D1%80%D0%B8%D1%87%D0%B8%D0%BD%D0%B0--%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D0%B5)
- [Чеклист production-ready проекта](https://arena.ai/c/019e2600-c239-76dc-858a-23ea0adb456c#%D1%87%D0%B5%D0%BA%D0%BB%D0%B8%D1%81%D1%82-production-ready-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
- [Ресурсы](https://arena.ai/c/019e2600-c239-76dc-858a-23ea0adb456c#%D1%80%D0%B5%D1%81%D1%83%D1%80%D1%81%D1%8B)

---

## Как работает Unity под капотом

Прежде чем искать проблемы, нужно понять архитектуру того, что профилируем. Без этого понимания оптимизация превращается в угадывание.

### Игровой цикл и бюджет кадра

Unity выполняет игровой цикл непрерывно. Каждая итерация — один кадр. При цели 60 FPS у нас есть ровно **16.6 миллисекунды** на весь кадр: физику, логику, рендеринг, звук, и всё остальное.



```csharp
Один кадр = 16.6ms при 60 FPS
           = 33.3ms при 30 FPS

Типичное распределение бюджета (мобайл):
┌─────────────────────────────────────────┐
│ CPU Main Thread                    ~8ms │
│   ├── Game Logic (Update)          ~3ms │
│   ├── Physics                      ~2ms │
│   ├── Animation                    ~1ms │
│   └── Rendering prep               ~2ms │
├─────────────────────────────────────────┤
│ GPU                               ~10ms │
│   ├── Opaque geometry              ~4ms │
│   ├── Shadows                      ~2ms │
│   ├── Transparent                  ~2ms │
│   └── Post Processing              ~2ms │
├─────────────────────────────────────────┤
│ Резерв / GC / прочее               ~2ms │
└─────────────────────────────────────────┘

Примечание: CPU и GPU работают частично параллельно,
поэтому сумма может превышать 16.6ms
```

Когда любой из блоков превышает свою часть бюджета — кадр не укладывается в 16.6ms. Для игрока это выглядит как падение FPS или, что хуже, как нерегулярный фриз.

### Managed и Native память

Unity использует два мира памяти, и их смешение — источник многих проблем:



```csharp
┌─────────────────────────────────────────────────────┐
│                   NATIVE MEMORY                     │
│  Управляется Unity C++ движком                      │
│  Текстуры, Mesh, Audio, Physics, Render             │
│  Освобождается немедленно при Destroy()             │
│  Профилируется: Memory Profiler (Native Objects)    │
├─────────────────────────────────────────────────────┤
│                   MANAGED MEMORY                    │
│  Управляется .NET/Mono runtime                      │
│  Ваш C# код, string, List<T>, массивы               │
│  Освобождается ТОЛЬКО через GC (непредсказуемо!)   │
│  Профилируется: Profiler Memory Module              │
└─────────────────────────────────────────────────────┘
```

Ключевое различие: native память освобождается когда вы вызываете `Destroy()`. Managed память освобождается когда **GC решит**, что пришло время. И это решение GC принимает самостоятельно, в самый неподходящий момент.

### CPU-bound vs GPU-bound: фундаментальная диагностика

Первый вопрос при любой проблеме производительности — кто виноват: процессор или видеокарта? От ответа зависит всё дальнейшее.



```csharp
ДИАГНОСТИКА ЗА 60 СЕКУНД:

Тест 1: Снизьте разрешение рендеринга в 2 раза
  Screen.SetResolution(Screen.width / 2, Screen.height / 2, true);
  
  FPS значительно вырос? → GPU-bound
  FPS почти не изменился? → CPU-bound

Тест 2: Отключите все игровые объекты сцены
  Засеките время через Profiler → Camera.Render time
  
  Camera.Render < 2ms? → чистая CPU проблема в логике
  Camera.Render > 5ms? → есть GPU проблема

Тест 3: Посмотрите на WaitForTargetFPS в Profiler
  Большой блок WaitForTargetFPS → вы не CPU-bound,
  кто-то другой замедляет кадр (GPU или vsync)
```

---

## Инструменты профилирования

### Unity Profiler: анатомия главного инструмента



```csharp
Открыть: Window → Analysis → Profiler  (Ctrl+7)
```

Profiler — это не одно окно, а набор модулей. Критически важно понимать каждый.



```csharp
╔══════════════════════════════════════════════════════════╗
║                    UNITY PROFILER                        ║
╠══════════════╦═══════════════════════════════════════════╣
║ CPU Module   ║ Время выполнения кода по функциям        ║
║              ║ ← НАЧИНАЙТЕ ЗДЕСЬ ВСЕГДА                 ║
╠══════════════╬═══════════════════════════════════════════╣
║ GPU Module   ║ Время выполнения на видеокарте            ║
║              ║ Требует подключения к устройству          ║
╠══════════════╬═══════════════════════════════════════════╣
║ Memory       ║ Аллокации, GC, размер heap                ║
║              ║ GC Allocated In Frame — главная метрика   ║
╠══════════════╬═══════════════════════════════════════════╣
║ Rendering    ║ Draw Calls, Batches, Triangles            ║
║              ║ SetPass Calls — дороже чем Draw Calls     ║
╠══════════════╬═══════════════════════════════════════════╣
║ Physics      ║ Время симуляции физики                    ║
║              ║ Число active contacts                     ║
╠══════════════╬═══════════════════════════════════════════╣
║ Audio        ║ DSP время, число источников               ║
╚══════════════╩═══════════════════════════════════════════╝
```

**Два режима просмотра CPU данных:**



```csharp
// HIERARCHY MODE — суммирует все вызовы одной функции
// Показывает: Total%, Self%, Calls, GC Alloc, Time ms
// Используйте для: "что суммарно занимает больше всего времени?"

// TIMELINE MODE — реальная последовательность вызовов
// Показывает: порядок выполнения, параллельность потоков
// Используйте для: "почему кадр длинный именно сейчас?"
```

**Deep Profile** — записывает каждый вызов метода, включая внутренние. Накладные расходы огромны (5-10x замедление), но точность максимальна. Используйте точечно для локализации проблемы.

**ProfilerMarker** — правильный способ маркировать собственный код:



```csharp
using Unity.Profiling;

public class EnemyAI : MonoBehaviour
{
    // Создаём маркер один раз — нет аллокаций при использовании
    private static readonly ProfilerMarker s_PathfindingMarker =
        new ProfilerMarker(ProfilerCategory.AI, "EnemyAI.UpdatePathfinding");

    private static readonly ProfilerMarker s_DecisionMarker =
        new ProfilerMarker(ProfilerCategory.AI, "EnemyAI.MakeDecision");

    void Update()
    {
        using (s_PathfindingMarker.Auto()) // виден в Profiler как отдельный блок
        {
            UpdatePathfinding();
        }

        using (s_DecisionMarker.Auto())
        {
            MakeDecision();
        }
    }
}
```

### ProfilerRecorder: метрики без накладных расходов



```csharp
// Получать данные Profiler'а в runtime — без аллокаций
using Unity.Profiling;

public class PerformanceMonitor : MonoBehaviour
{
    private ProfilerRecorder _mainThreadRecorder;
    private ProfilerRecorder _gcAllocRecorder;
    private ProfilerRecorder _drawCallRecorder;

    void OnEnable()
    {
        // Подписываемся на нужные счётчики
        _mainThreadRecorder = ProfilerRecorder.StartNew(
            ProfilerCategory.Internal, "Main Thread", 15); // 15 кадров истории

        _gcAllocRecorder = ProfilerRecorder.StartNew(
            ProfilerCategory.Memory, "GC Allocated In Frame", 1);

        _drawCallRecorder = ProfilerRecorder.StartNew(
            ProfilerCategory.Render, "Draw Calls Count", 1);
    }

    void OnDisable()
    {
        // ОБЯЗАТЕЛЬНО освобождать — иначе утечка native ресурсов
        _mainThreadRecorder.Dispose();
        _gcAllocRecorder.Dispose();
        _drawCallRecorder.Dispose();
    }

    void Update()
    {
        if (!_mainThreadRecorder.Valid) return;

        // Значения в наносекундах → конвертируем в ms
        double frameTimeMs = _mainThreadRecorder.LastValue * 1e-6;
        long gcBytesThisFrame = _gcAllocRecorder.LastValue;
        long drawCalls = _drawCallRecorder.LastValue;

        // Предупреждение при нарушении бюджетов
        if (frameTimeMs > 16.6)
            Debug.LogWarning($"[Perf] Кадр превысил бюджет: {frameTimeMs:F1}ms");

        if (gcBytesThisFrame > 0)
            Debug.LogWarning($"[Perf] GC аллокация: {gcBytesThisFrame / 1024f:F1} KB");
    }
}
```

### Memory Profiler Package: глубокий анализ памяти



```csharp
Установить: Package Manager → Memory Profiler (com.unity.memoryprofiler)
Открыть:    Window → Analysis → Memory Profiler
```

Memory Profiler делает полный снимок состояния памяти в конкретный момент. В отличие от Profiler-окна, он показывает **каждый объект** в managed heap с размером, количеством экземпляров и графом ссылок.



```csharp
Workflow поиска утечки памяти:

1. Загрузить уровень → нажать "Capture" → сохранить как Snapshot_A
2. Поиграть 10-15 минут (особенно: умирать и перезапускаться)
3. Снова нажать "Capture" → сохранить как Snapshot_B
4. Нажать "Diff" → сравнить снимки

Объекты в B, которых нет в A = потенциальные утечки

Частые виновники в Diff:
- EventHandler / Action — незакрытые подписки на события
- ure2D — дубликаты текстур, не освобождённые ресурсы
- MeshRenderer — объекты на сцене, не попавшие в Destroy
- String — накопление строк через конкатенацию
```

### Frame Debugger: рентген рендеринга



```csharp
Открыть: Window → Analysis → Frame Debugger
```

Frame Debugger записывает каждую GPU-команду одного кадра. Вы буквально «прокручиваете» кадр шаг за шагом, видя каждый draw call, каждый pass, каждое переключение состояния.



```csharp
Что искать в Frame Debugger:

✓ Секции "SRP Batch" — хорошо, объекты объединены
✗ Одиночные "Draw Mesh" для одинаковых объектов — батчинг сломан

Почему батчинг сломан? Frame Debugger покажет причину:
- "Разный материал" → проверьте sharedMaterial
- "Разный lightmap" → объекты на разных lightmap atlas
- "Нет instancing" → материал не поддерживает GPU Instancing

Считайте draw calls для конкретных систем:
- Тени (Shadow Pass): сколько?
- UI: сколько Canvas сборок?
- Particles: много ли отдельных систем?
```

### Сравнение инструментов



```csharp
╔═══════════════════╦══════════════╦════════════════════════════════╗
║ Инструмент        ║ Когда        ║ Что показывает                 ║
╠═══════════════════╬══════════════╬════════════════════════════════╣
║ Unity Profiler    ║ Ежедневно    ║ CPU/GPU время, GC аллокации    ║
║ Memory Profiler   ║ При утечках  ║ Каждый объект в heap           ║
║ Frame Debugger    ║ При GPU      ║ Последовательность draw calls  ║
║ Physics Debugger  ║ При физике   ║ Коллайдеры, контакты, слои     ║
║ RenderDoc         ║ GPU глубоко  ║ GPU state machine, шейдеры     ║
║ Xcode Instruments ║ iOS          ║ Metal GPU, нативная память      ║
║ Android Studio    ║ Android      ║ CPU profiler, memory           ║
╚═══════════════════╩══════════════╩════════════════════════════════╝
```

---

## Garbage Collector: главный подозреваемый

### Как GC решает когда работать

Unity (на большинстве платформ) использует **Boehm-Demers-Weiser** — консервативный mark-and-sweep коллектор. Его работа предельно проста в концепции и катастрофична в последствиях:



```csharp
Жизнь объекта в managed heap:

new MyClass()          → объект создан в heap
    ↓
используется           → GC Root держит ссылку (поле класса, стек, статика)
    ↓
ссылка потеряна        → объект недостижим, но ещё в памяти
    ↓
heap заполнен на ~75%  → GC решает "пора"
    ↓
Mark Phase             → обходит все корни, помечает живые объекты
    ↓
Sweep Phase            → неотмеченное = мусор, помечается как свободное
    ↓
НЕТ компакции          → Boehm НЕ перемещает объекты!
                          фрагментация нарастает со временем
    ↓
STOP-THE-WORLD         → весь managed код заморожен на время GC
```

**Ключевой факт**: Boehm GC **не компактирует** heap. Это означает, что после долгой работы в памяти образуются "дыры". Суммарно свободного места может быть достаточно, но непрерывного блока под крупный объект — нет. GC вынужден расширять heap.

**Incremental GC** (Unity 2019+) разбивает работу GC на маленькие кванты, размазывая паузу по нескольким кадрам:



```csharp
Включить: Edit → Project Settings → Player → Use Incremental GC

Классический GC:
Кадр 1: 2ms ██
Кадр 2: 2ms ██
Кадр 3: 47ms ██████████████████████████████████████████ ← SPIKE

Incremental GC:
Кадр 1: 4ms ████
Кадр 2: 4ms ████
Кадр 3: 4ms ████   ← размазанная нагрузка, нет spike
Кадр 4: 4ms ████

Incremental GC — не серебряная пуля:
✓ Убирает спайки
✗ Увеличивает общую нагрузку GC
✗ Не решает проблему избыточных аллокаций
```

### Что вызывает аллокации: полный каталог



```csharp
// ══════════════════════════════════════════════════
// ГРУППА 1: СТРОКИ
// ══════════════════════════════════════════════════

// ❌ Конкатенация — каждый + создаёт новый string объект
void Update()
{
    label. = "HP: " + hp + "/" + maxHp; // 3 аллокации за строку
}

// ❌ string.Format — внутренние промежуточные аллокации
string s = string.Format("Score: {0}", score);

// ❌ Интерполяция — в Unity/Mono не оптимизируется
string s = $"Player {name} has {hp} HP"; // аллокация

// ══════════════════════════════════════════════════
// ГРУППА 2: LINQ
// ══════════════════════════════════════════════════

// ❌ Каждый LINQ-метод создаёт объект-перечислитель
var active = enemies
    .Where(e => e.IsAlive)      // → IEnumerable аллокация
    .OrderBy(e => e.Distance)   // → OrderedEnumerable + List для сортировки
    .Take(5)                    // → ещё один перечислитель
    .ToList();                  // → финальный List<T>

// ══════════════════════════════════════════════════
// ГРУППА 3: BOXING
// ══════════════════════════════════════════════════

// ❌ Value type → object = boxing, всегда аллокация
object boxed = 42;
void Log(object value) { } // вызов с int, float, struct → boxing
interface IAction { void Do(); }
struct MyAction : IAction { } // вызов через интерфейс → boxing

// ❌ Enum как ключ Dictionary без кастомного comparer
Dictionary<MyEnum, string> dict = new Dictionary<MyEnum, string>();
dict[MyEnum.Value] = "x"; // boxing enum для GetHashCode

// ══════════════════════════════════════════════════
// ГРУППА 4: ЗАМЫКАНИЯ (CLOSURES)
// ══════════════════════════════════════════════════

// ❌ Захват локальной переменной → компилятор создаёт класс
void Update()
{
    float threshold = GetThreshold(); // локальная переменная

    // Компилятор генерирует примерно:
    // class DisplayClass_001 { public float threshold; }
    // var c = new DisplayClass_001 { threshold = threshold }; // АЛЛОКАЦИЯ
    items.ForEach(x => Process(x, threshold)); // лямбда + замыкание
}

// ══════════════════════════════════════════════════
// ГРУППА 5: КОЛЛЕКЦИИ
// ══════════════════════════════════════════════════

// ❌ foreach на Dictionary → аллокация Enumerator
foreach (var pair in myDictionary) { } // struct enumerator боксируется в Mono

// ❌ Новый List внутри Update
void Update()
{
    var temp = new List<Enemy>(); // КАЖДЫЙ КАДР — аллокация
}

// ❌ params массивы
void Log(params object[] args) { }
Log(x, y, z); // создаёт временный object[] каждый вызов

// ══════════════════════════════════════════════════
// ГРУППА 6: UNITY API
// ══════════════════════════════════════════════════

// ❌ GetComponent в Update
void Update()
{
    var rb = GetComponent<Rigidbody>(); // поиск каждый кадр
}

// ❌ FindObjectsOfType — O(n) по всем объектам + аллокация массива
Enemy[] enemies = FindObjectsOfType<Enemy>();

// ❌ Coroutine с new WaitForSeconds каждый раз
IEnumerator Bad()
{
    yield return new WaitForSeconds(1f); // аллокация каждый вызов
}

// ❌ Physics.OverlapSphere — возвращает новый Collider[] каждый вызов
Collider[] hits = Physics.OverlapSphere(pos, radius);

// ❌ Input.touches — создаёт новый массив каждый вызов
Touch[] touches = Input.touches;
```

---

## Чеклист первого профилирования

Вы открываете Profiler первый раз на новом проекте или новой сцене. Вот строгая последовательность действий, которая не даст потратить время впустую.

---

### ШАГ 1 — Подготовка (5 минут)



```csharp
□ Сделать Development Build (не профилировать в редакторе для финальных цифр)
  Build Settings → Development Build ✓
  Build Settings → Autoconnect Profiler ✓

□ Если нет времени на билд — хотя бы закрыть лишние окна редактора:
  Game View оставить, Inspector можно свернуть
  Это снижает Editor overhead

□ Открыть Profiler: Window → Analysis → Profiler
□ Выбрать Target: Playmode (или подключённое устройство)
□ Убедиться что запись не ведётся (кнопка Record не активна)
□ Выставить Frame Count: 300 кадров (правый нижний угол Profiler)
```

---

### ШАГ 2 — Первичный снимок (10 минут)



```csharp
□ Нажать Record
□ Запустить Play Mode
□ НИЧЕГО НЕ ДЕЛАТЬ 30 секунд — только наблюдать idle state
□ Затем симулировать активный геймплей:
  - Передвигаться
  - Стрелять / взаимодействовать
  - Открыть инвентарь / меню
  - Сделать то, что по ощущениям лагает
□ Остановить запись
□ СРАЗУ записать базовые метрики (до анализа):

  Среднее frame time: _______ ms
  Максимальное frame time: _______ ms
  Есть ли спайки? Да / Нет
  Паттерн спайков: регулярные / случайные / при действии: _______
```

---

### ШАГ 3 — CPU анализ (15 минут)



```csharp
□ Выбрать самый длинный кадр (кликнуть на пик в timeline)
□ CPU Module → Hierarchy view → сортировать по "Total ms"
□ Записать топ-5 по времени:
  1. _________________ | ___ms | ___% GC Alloc: ___
  2. _________________ | ___ms | ___% GC Alloc: ___
  3. _________________ | ___ms | ___% GC Alloc: ___
  4. _________________ | ___ms | ___% GC Alloc: ___
  5. _________________ | ___ms | ___% GC Alloc: ___

□ Проверить наличие (отметить найденное):
  □ GC.Collect — сборщик мусора работал в этом кадре
  □ GC.Alloc — аллокации в кадре (колонка GC Alloc > 0)
  □ FindObjectsOfType — поиск по всей сцене
  □ SendMessage / BroadcastMessage — медленный messaging
  □ Resources.Load во время геймплея — синхронная загрузка
  □ Physics.OverlapSphere (не NonAlloc версия)
  □ Camera.Render > 5ms — GPU проблема или много draw calls

□ Переключиться на Timeline view
□ Проверить: есть ли Worker Threads? Загружены ли они?
  Пустые Worker Threads = Job System не используется
  Main Thread ждёт чего-то = зависимость не параллелится
```

---

### ШАГ 4 — Memory анализ (10 минут)



```csharp
□ Memory Module → смотреть на график за всё время записи
□ Зафиксировать:
  GC Allocated In Frame (avg): _______ bytes
  GC Allocated In Frame (max): _______ bytes
  Managed Heap Used: _______ MB
  Managed Heap Reserved: _______ MB

□ Оценить паттерн Managed Heap:
  □ Монотонно растёт → потенциальная утечка памяти
  □ Пилообразный, периодически падает → нормальный GC цикл
  □ Стабильный → отличное состояние (цель!)

□ Если GC Alloc In Frame > 0 в steady state:
  □ Переключить CPU Module → Hierarchy
  □ Сортировать по "GC Alloc"
  □ Записать топ-источники аллокаций
  1. _________________ | _____ bytes | _____ calls/frame
  2. _________________ | _____ bytes | _____ calls/frame
  3. _________________ | _____ bytes | _____ calls/frame
```

---

### ШАГ 5 — Rendering анализ (10 минут)



```csharp
□ Rendering Module → зафиксировать:
  Draw Calls: _______  (цель мобайл: < 100, PC: < 1000)
  Batches: _______     (чем ближе к Draw Calls — тем хуже батчинг)
  SetPass Calls: ____  (смена шейдера — дороже чем Draw Call)
  Triangles: _______   (цель мобайл: < 300k)
  Vertices: _______

□ Открыть Frame Debugger (Window → Analysis → Frame Debugger)
□ Проверить:
  □ Есть ли "SRP Batch" блоки? (хорошо)
  □ Есть ли одиночные Draw Mesh для одинаковых объектов? (плохо)
  □ Сколько draw calls у UI?
  □ Сколько draw calls у теней?
  □ Есть ли объекты рендерящиеся несколько раз?

□ Scene View → Shading Mode → Overdraw
  □ Есть ли красные зоны (>4x overdraw)?
  □ Много ли прозрачных объектов в одном месте?
```

---

### ШАГ 6 — Синтез (5 минут)



```csharp
□ Определить главный тип проблемы:
  □ CPU-bound: логика занимает > 8ms
  □ GPU-bound: рендеринг занимает > 10ms
  □ Memory: GC Alloc > 0 в steady state, или heap растёт
  □ Несколько проблем одновременно

□ Выбрать ONE вещь для оптимизации (самую большую по impact)
  Правило: исправлять по одной проблеме, затем перемерять

□ Зафиксировать baseline (до оптимизации):
  FPS avg: _______
  Frame time avg: _______ ms
  GC Alloc/frame: _______ bytes
  Draw Calls: _______

Без baseline невозможно доказать что оптимизация помогла.
```

---

## Практика: диагностика и лечение

Разберём конкретные проблемы с диагностикой и исправлением.

### Проблема 1: String concatenation в Update

**Симптом в Profiler**: `GC.Alloc` 100-300 bytes каждый кадр, источник в строках вашего UI-кода.



```csharp
// ══════════════════════════════════════════════
// ❌ КАК ОБЫЧНО ПИШУТ
// ══════════════════════════════════════════════
void Update()
{
    // Три аллокации за строчку, 60 раз в секунду
    hp. = "HP: " + currentHP + "/" + maxHP;
    fps. = "FPS: " + Mathf.RoundToInt(1f / Time.deltaTime);
    name. = "Player: " + playerName + " [Lv." + level + "]";
}

// ══════════════════════════════════════════════
// ✅ КАК НУЖНО
// ══════════════════════════════════════════════
public class HUDController : MonoBehaviour
{
    [SerializeField] private  _hp;
    [SerializeField] private  _fps;

    // Один StringBuilder на класс — не создаётся каждый кадр
    private readonly StringBuilder _sb = new StringBuilder(128);

    // Кэш предыдущих значений — обновляем UI только при изменении
    private int _lastHP = -1;
    private int _lastMaxHP = -1;
    private float _fpsTimer;
    private const float FPS_INTERVAL = 0.5f; // обновление FPS дважды в секунду

    void Update()
    {
        // HP — обновляем только при реальном изменении
        if (currentHP != _lastHP || maxHP != _lastMaxHP)
        {
            _lastHP = currentHP;
            _lastMaxHP = maxHP;

            _sb.Clear();
            _sb.Append("HP: ");
            _sb.Append(currentHP);
            _sb.Append('/');
            _sb.Append(maxHP);
            _hp. = _sb.ToString();
            // ToString() аллоцирует — но только при реальном изменении HP
        }

        // FPS — обновляем редко, игроку не нужна точность до кадра
        _fpsTimer += Time.unscaledDeltaTime;
        if (_fpsTimer >= FPS_INTERVAL)
        {
            _fpsTimer = 0f;
            _sb.Clear();
            _sb.Append("FPS: ");
            _sb.Append(Mathf.RoundToInt(1f / Time.unscaledDeltaTime));
            _fps. = _sb.ToString();
        }
    }
}

/*
РЕЗУЛЬТАТ:
До:   ~200 bytes GC/frame × 60 FPS = 12 KB/сек → GC Spike каждые ~6 мин
После: 0 bytes GC/frame в steady state
       Редкая аллокация только при реальном изменении значений
*/
```

### Проблема 2: LINQ в горячем пути

**Симптом в Profiler**: `Enumerable.Where`, `Enumerable.OrderBy` в Hierarchy, 300-800 bytes GC Alloc каждый кадр из скрипта логики.



```csharp
// ══════════════════════════════════════════════
// ❌ LINQ в Update
// ══════════════════════════════════════════════
void Update()
{
    // 4 аллокации каждый кадр, 0.5-1ms CPU
    var targets = allEnemies
        .Where(e => e.IsAlive && e.IsVisible)
        .OrderBy(e => Vector3.Distance(pos, e.transform.position))
        .Take(3)
        .ToList();

    ProcessTargets(targets);
}

// ══════════════════════════════════════════════
// ✅ Ручная итерация без аллокаций
// ══════════════════════════════════════════════
public class TargetSelector : MonoBehaviour
{
    // Pre-allocated буфер результатов
    private readonly List<(Enemy enemy, float sqrDist)> _candidates
        = new List<(Enemy, float)>(16);

    // Кэшированный comparer — struct, без аллокации
    private static readonly EnemyDistanceComparer _comparer
        = new EnemyDistanceComparer();

    // Результат — переиспользуемый список
    private readonly List<Enemy> _selectedTargets = new List<Enemy>(3);

    // Интервал обновления: не каждый кадр
    private float _updateTimer;
    private const float UPDATE_INTERVAL = 0.1f; // 10 раз/сек достаточно

    void Update()
    {
        _updateTimer += Time.deltaTime;
        if (_updateTimer < UPDATE_INTERVAL) return;
        _updateTimer -= UPDATE_INTERVAL;

        SelectTargets();
    }

    private void SelectTargets()
    {
        Vector3 myPos = transform.position;
        _candidates.Clear();

        // Цикл без LINQ — нет аллокаций
        for (int i = 0; i < allEnemies.Count; i++)
        {
            Enemy e = allEnemies[i];
            if (!e.IsAlive || !e.IsVisible) continue;

            // sqrMagnitude вместо Distance — нет операции sqrt
            float sqrDist = (myPos - e.transform.position).sqrMagnitude;
            _candidates.Add((e, sqrDist));
        }

        // Sort in-place — модифицирует существующий список
        _candidates.Sort(_comparer);

        _selectedTargets.Clear();
        int count = Mathf.Min(3, _candidates.Count);
        for (int i = 0; i < count; i++)
            _selectedTargets.Add(_candidates[i].enemy);

        ProcessTargets(_selectedTargets);
    }

    // Struct comparer: нет boxing, нет heap аллокации
    private struct EnemyDistanceComparer
        : IComparer<(Enemy enemy, float sqrDist)>
    {
        public int Compare(
            (Enemy enemy, float sqrDist) x,
            (Enemy enemy, float sqrDist) y)
            => x.sqrDist.CompareTo(y.sqrDist);
    }
}

/*
РЕЗУЛЬТАТ:
До:   600 bytes GC/frame, 0.8ms CPU
После: 0 bytes GC/frame, 0.05ms CPU
       (плюс интервал снизил частоту с 60/сек до 10/сек)
*/
```

### Проблема 3: GetComponent в Update

**Симптом в Profiler** (Deep Profile): `Component.GetComponent` вызывается 60+ раз в секунду из одного и того же метода.



```csharp
// ══════════════════════════════════════════════
// ❌ GetComponent каждый кадр
// ══════════════════════════════════════════════
void Update()
{
    // GetComponent — поиск по массиву компонентов, каждый кадр
    GetComponent<Rigidbody>().AddForce(Vector3.up);
    GetComponent<Animator>().SetFloat("Speed", speed);
    GetComponent<AudioSource>().pitch = speedMultiplier;
}

// ══════════════════════════════════════════════
// ✅ Кэширование в Awake
// ══════════════════════════════════════════════
public class PlayerController : MonoBehaviour
{
    // Кэшированные ссылки — инициализируются один раз
    private Rigidbody _rigidbody;
    private Animator _animator;
    private AudioSource _audioSource;

    // Кэшированные Animator parameter hashes — строковый lookup только раз
    private static readonly int SpeedHash = Animator.StringToHash("Speed");
    private static readonly int JumpHash = Animator.StringToHash("Jump");
    private static readonly int GroundedHash = Animator.StringToHash("IsGrounded");

    void Awake()
    {
        // Awake — не Start! Start может быть вызван позже Awake других объектов
        _rigidbody = GetComponent<Rigidbody>();
        _animator = GetComponent<Animator>();
        _audioSource = GetComponent<AudioSource>();

        // Явные проверки с диагностикой
        if (_rigidbody == null)
            Debug.LogError($"[PlayerController] Rigidbody не найден на {name}", this);
    }

    void Update()
    {
        // Все обращения — через кэшированные ссылки
        _rigidbody.AddForce(Vector3.up * jumpForce);
        _animator.SetFloat(SpeedHash, currentSpeed);   // hash вместо string
        _audioSource.pitch = speedMultiplier;
    }
}

/*
РЕЗУЛЬТАТ:
До:   GetComponent ~0.03ms/call × 3 компонента × 60 FPS = 5.4ms/сек лишних
После: 0ms на поиск компонентов в Update
       Animator.SetFloat(hash) быстрее SetFloat(string) примерно в 2-3 раза
*/
```

### Проблема 4: Instantiate/Destroy вместо Object Pool

**Симптом в Profiler**: регулярные GC Spikes при интенсивном геймплее, `Object.Instantiate` в горячем пути, `GC.Collect` каждые несколько секунд.



```csharp
// ══════════════════════════════════════════════
// ❌ Instantiate/Destroy — фабрика мусора
// ══════════════════════════════════════════════
void Shoot()
{
    // Instantiate: аллокация GameObject + все компоненты
    GameObject bullet = Instantiate(bulletPrefab, firePoint.position, firePoint.rotation);
    bullet.GetComponent<Bullet>().Initialize(direction);

    // Destroy: помечает для GC, не освобождает сразу
    Destroy(bullet, 3f);
}

// ══════════════════════════════════════════════
// ✅ Generic Object Pool
// ══════════════════════════════════════════════
public class ObjectPool<T> where T : Component
{
    private readonly Stack<T> _available;
    private readonly Func<T> _factory;
    private readonly Action<T> _onGet;
    private readonly Action<T> _onReturn;
    private readonly int _maxSize;

    public int CountAll { get; private set; }
    public int CountAvailable => _available.Count;
    public int CountActive => CountAll - CountAvailable;

    public ObjectPool(
        Func<T> factory,
        Action<T> onGet = null,
        Action<T> onReturn = null,
        int prewarmCount = 10,
        int maxSize = 100)
    {
        _factory = factory ?? throw new ArgumentNullException(nameof(factory));
        _onGet = onGet;
        _onReturn = onReturn;
        _maxSize = maxSize;
        _available = new Stack<T>(prewarmCount);

        // Прогрев: создаём объекты заранее, не в hot path
        for (int i = 0; i < prewarmCount; i++)
        {
            T item = _factory();
            _onReturn?.Invoke(item); // деактивируем
            _available.Push(item);
            CountAll++;
        }
    }

    public T Get()
    {
        T item = _available.Count > 0
            ? _available.Pop()
            : CreateNew();

        _onGet?.Invoke(item);
        return item;
    }

    public void Return(T item)
    {
        if (item == null) return;

        _onReturn?.Invoke(item);

        if (_available.Count < _maxSize)
            _available.Push(item);
        else
            Object.Destroy(item.gameObject); // пул полон — уничтожаем лишнее
    }

    private T CreateNew()
    {
        T item = _factory();
        CountAll++;

        // Предупреждение: пул исчерпан, нужно увеличить prewarmCount
        Debug.LogWarning(
            $"[Pool<{typeof(T).Name}>] Создаём новый объект (всего: {CountAll}). " +
            "Рассмотрите увеличение prewarmCount.");
        return item;
    }

    public void Clear()
    {
        while (_available.Count > 0)
        {
            T item = _available.Pop();
            Object.Destroy(item.gameObject);
        }
        CountAll = 0;
    }
}

// ══════════════════════════════════════════════
// ИСПОЛЬЗОВАНИЕ
// ══════════════════════════════════════════════
public class WeaponController : MonoBehaviour
{
    [SerializeField] private GameObject _bulletPrefab;
    [SerializeField] private Transform _firePoint;

    private ObjectPool<Bullet> _bulletPool;

    void Awake()
    {
        Transform poolParent = new GameObject("BulletPool").transform;

        _bulletPool = new ObjectPool<Bullet>(
            factory: () =>
            {
                var go = Instantiate(_bulletPrefab, poolParent);
                return go.GetComponent<Bullet>();
            },
            onGet: b => b.gameObject.SetActive(true),
            onReturn: b =>
            {
                b.gameObject.SetActive(false);
                b.transform.SetParent(poolParent);
            },
            prewarmCount: 20,
            maxSize: 50
        );
    }

    public void Shoot()
    {
        // Нет Instantiate → нет аллокации → нет GC давления
        Bullet bullet = _bulletPool.Get();
        bullet.transform.SetPositionAndRotation(_firePoint.position, _firePoint.rotation);
        bullet.Initialize(transform.forward * 25f, _bulletPool);
    }
}

public class Bullet : MonoBehaviour
{
    private ObjectPool<Bullet> _pool;
    private Vector3 _velocity;
    private float _lifetime;

    // Кэшированный WaitForSeconds — одна аллокация на тип
    private static readonly WaitForSeconds _lifetimeWait = new WaitForSeconds(3f);

    public void Initialize(Vector3 velocity, ObjectPool<Bullet> pool)
    {
        _velocity = velocity;
        _pool = pool;
        StartCoroutine(AutoReturn());
    }

    void Update()
    {
        transform.position += _velocity * Time.deltaTime;
    }

    void OnTriggerEnter(Collider other)
    {
        ReturnToPool();
    }

    private IEnumerator AutoReturn()
    {
        yield return _lifetimeWait; // нет аллокации!
        ReturnToPool();
    }

    private void ReturnToPool()
    {
        StopAllCoroutines();
        _pool?.Return(this);
    }
}

/*
РЕЗУЛЬТАТ:
До:   GC Spike каждые 3-5 секунд при стрельбе, 5-20ms пауза
После: 0 bytes GC в steady state
       0 Instantiate calls в горячем пути
       Пулы работают с первого выстрела (прогрев в Awake)
*/
```

### Проблема 5: Физика и Layer Collision Matrix

**Симптом в Profiler**: `Physics.Processing` занимает > 2ms, растёт пропорционально количеству объектов.



```csharp
НАСТРОЙКА LAYER COLLISION MATRIX

Edit → Project Settings → Physics → Layer Collision Matrix

Создать слои:
Layer 8:  Player
Layer 9:  Enemy
Layer 10: PlayerBullet
Layer 11: EnemyBullet
Layer 12: Environment
Layer 13: Pickup

Матрица взаимодействий (✓ = взаимодействуют, ✗ = игнорируют):

              Player Enemy PBullet EBullet Environ Pickup
Player          ✗      ✓     ✗       ✓       ✓       ✓
Enemy           ✓      ✗     ✓       ✗       ✓       ✗
PlayerBullet    ✗      ✓     ✗       ✗       ✓       ✗
EnemyBullet     ✓      ✗     ✗       ✗       ✓       ✗
Environment     ✓      ✓     ✓       ✓       ✗       ✗
Pickup          ✓      ✗     ✗       ✗       ✗       ✗

Ключевые оптимизации:
- Пули игрока не взаимодействуют с пулями врага
- Враги не сталкиваются между собой (если не нужно)
- Подбираемые предметы игнорируют пули и врагов

Расчёт экономии:
При "все со всеми": N×(N-1)/2 пар проверяется
При оптимизированной матрице: только нужные пары

50 пуль + 20 врагов + 1 игрок = 71 объект
"Все со всеми": 71×70/2 = 2485 пар
Оптимизировано: ~300-400 реальных пар
Экономия: ~85% Physics Broad Phase работы
```



```csharp
// Верификация настройки через код
[ExecuteInEditMode]
public class PhysicsLayerValidator : MonoBehaviour
{
    [ConMenu("Validate Layer Matrix")]
    void Validate()
    {
        // Пары которые ДОЛЖНЫ взаимодействовать
        var required = new (string a, string b)[]
        {
            ("Player", "Enemy"),
            ("Player", "EnemyBullet"),
            ("Enemy", "PlayerBullet"),
            ("Player", "Environment"),
            ("Enemy", "Environment"),
        };

        // Пары которые НЕ должны
        var forbidden = new (string a, string b)[]
        {
            ("PlayerBullet", "EnemyBullet"),
            ("PlayerBullet", "PlayerBullet"),
            ("Enemy", "Enemy"),
        };

        bool allOk = true;

        foreach (var (a, b) in required)
        {
            int layerA = LayerMask.NameToLayer(a);
            int layerB = LayerMask.NameToLayer(b);

            if (layerA == -1 || layerB == -1)
            {
                Debug.LogError($"Слой не найден: {(layerA == -1 ? a : b)}");
                allOk = false;
                continue;
            }

            if (Physics.GetIgnoreLayerCollision(layerA, layerB))
            {
                Debug.LogError($"ОШИБКА: {a} ↔ {b} должны взаимодействовать!");
                allOk = false;
            }
        }

        foreach (var (a, b) in forbidden)
        {
            int layerA = LayerMask.NameToLayer(a);
            int layerB = LayerMask.NameToLayer(b);

            if (layerA == -1 || layerB == -1) continue;

            if (!Physics.GetIgnoreLayerCollision(layerA, layerB))
            {
                Debug.LogWarning($"ЛИШНЯЯ КОЛЛИЗИЯ: {a} ↔ {b} не нужны");
                allOk = false;
            }
        }

        if (allOk)
            Debug.Log("✓ Layer Collision Matrix настроена корректно!");
    }
}
```

---

## Паттерны оптимизации

### Span< T >: работа с данными без копирования



```csharp
// ══════════════════════════════════════════════
// Span<T> — работа со срезами без аллокаций
// ══════════════════════════════════════════════

// Parsing без промежуточных аллокаций
void ParseEnemyData(ReadOnlySpan<char> data)
{
    // Не создаём подстроки — работаем со срезами
    int separatorIndex = data.IndexOf(':');
    if (separatorIndex < 0) return;

    ReadOnlySpan<char> key = data.Slice(0, separatorIndex).Trim();
    ReadOnlySpan<char> value = data.Slice(separatorIndex + 1).Trim();

    // float.TryParse принимает ReadOnlySpan — нет аллокации string
    if (float.TryParse(value, out float result))
        ApplyValue(key, result);
}

// Работа с частью массива без копирования
void ProcessDamageZone(float[] allDamageValues, int startIndex, int count)
{
    // Span указывает на часть существующего массива — нет new float[]
    Span<float> zone = allDamageValues.AsSpan(startIndex, count);

    float total = 0f;
    for (int i = 0; i < zone.Length; i++)
        total += zone[i];

    ApplyZoneDamage(total / zone.Length);
}

// stackalloc — временный буфер на стеке, не в heap
void BuildAttackPattern(int patternSize)
{
    // Только для небольших буферов! Стек ограничен ~1MB
    Span<Vector2> pattern = patternSize <= 64
        ? stackalloc Vector2[patternSize]  // стек: нет GC
        : new Vector2[patternSize];        // heap: fallback для больших размеров

    // Заполняем паттерн
    for (int i = 0; i < patternSize; i++)
    {
        float angle = i * (360f / patternSize) * Mathf.Deg2Rad;
        pattern[i] = new Vector2(Mathf.Cos(angle), Mathf.Sin(angle));
    }

    ApplyPattern(pattern);
}
```

### Устранение boxing: правильные обобщения



```csharp
// ══════════════════════════════════════════════
// Boxing: когда struct становится object
// ══════════════════════════════════════════════

// ❌ Boxing через интерфейс без обобщений
public interface IDamageable
{
    void TakeDamage(int amount);
}

void DealDamage(IDamageable target, int damage)
{
    target.TakeDamage(damage); // если target — struct, boxing неизбежен
}

// ✅ Generic метод с constraint — компилятор генерирует специализированный код
void DealDamage<T>(ref T target, int damage) where T : struct, IDamageable
{
    target.TakeDamage(damage); // нет boxing!
}

// ══════════════════════════════════════════════
// Словари с value-type ключами
// ══════════════════════════════════════════════

// ❌ Enum ключ без custom comparer → boxing при каждом обращении
Dictionary<WeaponType, float> damages = new Dictionary<WeaponType, float>();
float d = damages[WeaponType.Sword]; // boxing WeaponType для GetHashCode

// ✅ Кастомный comparer без boxing
public struct EnumComparer<T> : IEqualityComparer<T>
    where T : unmanaged, Enum
{
    public bool Equals(T x, T y)
        => EqualityComparer<T>.Default.Equals(x, y);

    public int GetHashCode(T obj)
        => EqualityComparer<T>.Default.GetHashCode(obj);

    public static readonly EnumComparer<T> Instance = new EnumComparer<T>();
}

// Использование:
var damages = new Dictionary<WeaponType, float>(
    EnumComparer<WeaponType>.Instance);
```

### Правильные корутины: избегаем аллокаций



```csharp
public class CoroutineOptimizations : MonoBehaviour
{
    // ══════════════════════════════════════════════
    // Кэшированные YieldInstruction
    // ══════════════════════════════════════════════

    // ✅ Статические кэши — создаются один раз для всего типа
    private static readonly WaitForSeconds Wait1s = new WaitForSeconds(1f);
    private static readonly WaitForSeconds Wait05s = new WaitForSeconds(0.5f);
    private static readonly WaitForFixedUpdate WaitFixed = new WaitForFixedUpdate();
    private static readonly WaitForEndOfFrame WaitEOF = new WaitForEndOfFrame();

    // ❌ new каждый вызов — аллокация каждый раз
    IEnumerator BadCoroutine()
    {
        while (true)
        {
            yield return new WaitForSeconds(1f); // аллокация каждую итерацию
        }
    }

    // ✅ Кэшированный WaitForSeconds
    IEnumerator GoodCoroutine()
    {
        while (true)
        {
            yield return Wait1s; // нет аллокации
            DoSomething();
        }
    }

    // ═══════════════════════════════════════════════
    // Кастомный YieldInstruction для переменных задержек
    // ═══════════════════════════════════════════════

    // WaitForSeconds нельзя переиспользовать с разными значениями
    // Используйте WaitUntil с кэшированным predicate

    private float _waitUntilTime;

    // ❌ Не кэшируемо — разные задержки требуют new WaitForSeconds
    IEnumerator DelayedAction_Bad(float delay)
    {
        yield return new WaitForSeconds(delay); // аллокация каждый вызов
        DoAction();
    }

    // ✅ WaitUntil с кэшированным предикатом
    private Func<bool> _waitPredicate; // инициализируем в Awake

    void Awake()
    {
        // Замыкание создаётся один раз в Awake
        _waitPredicate = () => Time.time >= _waitUntilTime;
    }

    IEnumerator DelayedAction_Good(float delay)
    {
        _waitUntilTime = Time.time + delay;
        yield return new WaitUntil(_waitPredicate); // _waitPredicate кэширован!
        DoAction();
    }

    private void DoSomething() { }
    private void DoAction() { }
}
```

---

## GPU: когда проблема не в коде

### Batching: объединение draw calls

Unity может объединять несколько объектов в один draw call. Существует несколько механизмов с разными требованиями:



```csharp
╔══════════════════════╦═══════════════════╦══════════════════════════╗
║ Тип батчинга         ║ Требования        ║ Ограничения              ║
╠══════════════════════╬═══════════════════╬══════════════════════════╣
║ Static Batching      ║ Один материал     ║ Объекты не двигаются     ║
║                      ║ Static флаг       ║ Увеличивает размер билда ║
╠══════════════════════╬═══════════════════╬══════════════════════════╣
║ Dynamic Batching     ║ Один материал     ║ < 300 вершин на меш      ║
║                      ║ Нет skinning      ║ CPU overhead на батчинг  ║
╠══════════════════════╬═══════════════════╬══════════════════════════╣
║ GPU Instancing       ║ Один материал     ║ Шейдер с instancing      ║
║                      ║ Один меш          ║ Разные transform/цвет OK ║
╠══════════════════════╬═══════════════════╬══════════════════════════╣
║ SRP Batcher          ║ URP/HDRP          ║ Шейдер с CBUFFER         ║
║                      ║ Совместимый шейдер║ Снижает CPU overhead     ║
╚══════════════════════╩═══════════════════╩══════════════════════════╝
```

**Главный враг батчинга — `renderer.material`:**



```csharp
// ══════════════════════════════════════════════
// ❌ renderer.material создаёт копию материала
// ══════════════════════════════════════════════
void SetEnemyAlert(bool alert)
{
    // Это создаёт уникальный экземпляр материала для этого объекта
    // Теперь объект несовместим с батчингом и инстансингом!
    renderer.material.color = alert ? Color.red : Color.white;
}

// ══════════════════════════════════════════════
// ✅ MaterialPropertyBlock — не ломает батчинг
// ══════════════════════════════════════════════
public class EnemyVisuals : MonoBehaviour
{
    private MaterialPropertyBlock _propertyBlock;
    private Renderer _renderer;

    // Кэшируем ID property — строковый lookup только при старте
    private static readonly int ColorID = Shader.PropertyToID("_Color");
    private static readonly int EmissionID = Shader.PropertyToID("_EmissionColor");
    private static readonly Color AlertColor = new Color(1f, 0.2f, 0.2f);
    private static readonly Color NormalColor = Color.white;

    void Awake()
    {
        _renderer = GetComponent<Renderer>();
        _propertyBlock = new MaterialPropertyBlock(); // один раз
    }

    public void SetAlert(bool alert)
    {
        // GetPropertyBlock → SetColor → SetPropertyBlock
        // Не создаёт копию материала, совместимо с GPU Instancing
        _renderer.GetPropertyBlock(_propertyBlock);
        _propertyBlock.SetColor(ColorID, alert ? AlertColor : NormalColor);
        _renderer.SetPropertyBlock(_propertyBlock);
    }
}
```

**Диагностика батчинга через Frame Debugger:**



```csharp
Window → Analysis → Frame Debugger → Enable

Признаки работающего батчинга:
✓ "SRP Batch" с числом объектов внутри
✓ "Draw Mesh (Instanced)" — GPU Instancing работает
✓ Мало "Draw Mesh" одиночных вызовов для одинаковых объектов

Признаки сломанного батчинга:
✗ 100 врагов → 100 отдельных "Draw Mesh" записей
✗ Причина указана: "Different material", "Not batched: Too many vertices"
```

### Overdraw: лишняя работа Fragment Shader



```csharp
Scene View → Shading Mode → Overdraw

Цвета:
Синий  (1x) → пиксель закрашен один раз    → отлично
Зелёный (2x) → два слоя                     → нормально
Жёлтый  (3x) → три слоя                     → стоит проверить
Красный (4x+) → критическое overdraw        → проблема

Главные источники overdraw:
1. Particle Systems с прозрачными текстурами
   → Снизить Max Particles, использовать непрозрачные материалы где возможно
   → Sort Mode: By Distance (меньше перекрытий)

2. Прозрачный UI
   → Разделить Canvas: статичный + динамичный
   → Скрытые панели: SetActive(false), не alpha = 0

3. Skybox рендерится поверх геометрии
   → Camera → Clear Flags → Depth Only (если небо не видно)
   → Depth Prepass снижает overdraw для опака
```

---

## Мифы об оптимизации в Unity

Вокруг оптимизации сложилось множество устойчивых заблуждений. Некоторые из них были правдой в старых версиях Unity. Некоторые никогда не были правдой. Все они опасны, потому что заставляют тратить время не там.

---

### Миф 1: «Надо оптимизировать каждую строчку кода»

**Реальность**: Преждевременная оптимизация — корень всех зол (Кнут, 1974). Этот принцип не устарел.

Оптимизация без данных Profiler'а — угадывание. Разработчики систематически ошибаются в оценке того, что является bottleneck'ом. Исследования показывают: интуитивные предположения об узких местах правильны менее чем в 20% случаев.



```csharp
ПРАВИЛО: Measure → Identify → Optimize → Measure Again

Никогда не оптимизируйте:
- Код, который выполняется редко (инициализация, загрузка)
- Код вне горячего пути без данных профайлера
- Ради "красоты" или "правильности" без измеримого эффекта
```

---

### Миф 2: «Update() дорогой, надо использовать корутины»

**Реальность**: Unity вызывает `Update()` через reflection и SendMessage — это реальный overhead. Но корутины не быстрее, а иногда медленнее.



```csharp
// Реальные цифры (Unity 2022, 10 000 объектов):
// Update() пустой:           ~0.3ms
// Coroutine с yield return:  ~0.5ms (overhead на state machine)
// Update() со логикой:       зависит от логики, не от Update()

// Реальная оптимизация: уменьшить количество объектов с Update()
// Не: заменять Update() на корутины

// ✅ Действительно работающие подходы:
// 1. Централизованный Update через Manager
public class EnemyManager : MonoBehaviour
{
    private List<Enemy> _enemies = new List<Enemy>();

    void Update() // Один вызов Update вместо 100
    {
        for (int i = 0; i < _enemies.Count; i++)
            _enemies[i].ManualUpdate(); // прямой вызов, без reflection
    }
}

// 2. Интервальное обновление через Time
void Update()
{
    _timer += Time.deltaTime;
    if (_timer < _updateInterval) return; // большинство кадров — ранний выход
    _timer -= _updateInterval;
    DoExpensiveWork();
}
```

---

### Миф 3: «GameObject.Find дорогой, надо его избегать везде»

**Реальность**: `GameObject.Find` — O(n) поиск, действительно дорогой. Но это проблема только в горячем пути (Update). В Awake/Start это абсолютно нормально.



```csharp
// ✅ Нормально — вызывается один раз
void Awake()
{
    _player = GameObject.FindWithTag("Player");     // окей
    _gameManager = FindObjectOfType<GameManager>(); // окей
}

// ❌ Проблема — вызывается каждый кадр
void Update()
{
    var player = GameObject.FindWithTag("Player"); // каждый кадр!
}

// Настоящие альтернативы для архитектуры:
// 1. Dependency Injection (ServiceLocator, Zenject, VContainer)
// 2. ScriptableObject как shared reference
// 3. Статические ссылки (с осторожностью — проблемы с тестированием)
// 4. Events/Delegates для loose coupling
```

---

### Миф 4: «Математика с float медленная, надо использовать int»

**Реальность**: Современные CPU выполняют float и int операции с одинаковой скоростью (часто float быстрее благодаря SIMD). На мобайлах ситуация аналогична.



```csharp
Реальные узкие места в математике:
✗ Mathf.Sqrt()  → используйте sqrMagnitude где возможно
✗ Mathf.Sin/Cos в Update → кэшируйте результат если аргумент не меняется
✗ Vector3.Distance → используйте sqrMagnitude для сравнений

Не являются проблемой:
✓ float + float, float * float
✓ Vector3 + Vector3
✓ Quaternion * Vector3
```

---

### Миф 5: «Debug.Log не влияет на производительность в релизе»

**Реальность**: В Release Build вызовы `Debug.Log` убираются... только если вы используете `[Conditional]` атрибут или `#if DEBUG`. Сам по себе `Debug.Log` в release билде работает, просто не показывается в консоли.



```csharp
// ❌ Это работает и в Release — аллоцирует строку, отправляет в stack
void Update()
{
    Debug.Log("Enemy position: " + transform.position); // работает в release!
}

// ✅ Условная компиляция — вырезается полностью
[System.Diagnostics.Conditional("DEVELOPMENT_BUILD")]
[System.Diagnostics.Conditional("UNITY_EDITOR")]
static void DebugLog(string message)
{
    Debug.Log(message);
}

// ✅ Или через препроцессор
void Update()
{
#if UNITY_EDITOR || DEVELOPMENT_BUILD
    Debug.Log("Enemy position: " + transform.position);
#endif
}

// ✅ В Unity 2021+ можно использовать Logger
private static ILogger _logger = Debug.unityLogger;
// В Release: Debug.unityLogger.logEnabled = false; в одном месте
```

---

### Миф 6: «Camera.main дорогой — надо кэшировать»

**Реальность**: Это было правдой до Unity 2020. Начиная с Unity 2020.2, `Camera.main` кэшируется внутри и больше не выполняет поиск по тегам каждый вызов.



```csharp
// До Unity 2020.2 — кэширование было необходимо
private Camera _camera;
void Awake() { _camera = Camera.main; } // обязательно!

// Unity 2020.2+ — Camera.main кэшируется движком
void Update()
{
    Camera.main.transform.position; // быстро, нет FindWithTag()
}

// Тем не менее, кэширование в Awake не вредит и улучшает читаемость
// Это не миф о том что "кэшировать плохо" — 
// это уточнение что "НЕкэшировать больше не катастрофа"
```

---

### Миф 7: «OnGUI надо полностью избегать»

**Реальность**: `OnGUI` — дорогая система (CPU intensive, immediate mode), но для **debug tools** и **editor scripts** — это правильный инструмент. Проблема только если использовать `OnGUI` для игрового UI.



```csharp
// ❌ OnGUI для игрового UI — плохо
void OnGUI()
{
    GUI.Label(new Rect(10, 10, 200, 30), "Score: " + score); // каждый кадр
}

// ✅ OnGUI для debug overlay — нормально (только в development builds)
void OnGUI()
{
#if UNITY_EDITOR || DEVELOPMENT_BUILD
    GUILayout.Label($"FPS: {_currentFPS:F0}");
    GUILayout.Label($"GC Alloc: {_gcAllocLastFrame / 1024f:F1} KB");
    GUILayout.Label($"Draw Calls: {_drawCalls}");
#endif
}

// Для игрового UI: используйте Unity UI (uGUI) или UI Toolkit
```

---

### Миф 8: «Больше скриптов = медленнее»

**Реальность**: Количество MonoBehaviour скриптов влияет на время вызова Update() (overhead на каждый MonoBehaviour). Но разбиение одного большого скрипта на несколько маленьких — правильная архитектура, и реальный overhead минимален.



```csharp
Реальная проблема не в количестве скриптов, а в:
- Что эти скрипты делают в Update()
- Сколько аллокаций они производят
- Насколько дорогие операции выполняются

10 000 пустых MonoBehaviour ≈ 0.3ms (измеримо, но не катастрофа)
100 MonoBehaviour с FindObjectsOfType в Update = катастрофа
```

---

## Таблица: Проблема → Причина → Решение



```csharp
╔══════════════════════════╦═══════════════════════════════╦════════════════════════════════════╗
║ Проблема                 ║ Причина                       ║ Решение                            ║
╠══════════════════════════╬═══════════════════════════════╬════════════════════════════════════╣
║ GC Spike каждые          ║ Регулярные аллокации в        ║ Найти источник через Profiler      ║
║ несколько секунд         ║ Update() накапливают мусор    ║ Memory Module → GC Alloc column    ║
║                          ║ до порога срабатывания GC     ║ Устранить string concat, LINQ      ║
╠══════════════════════════╬═══════════════════════════════╬════════════════════════════════════╣
║ Растущий Managed Heap    ║ Утечка памяти: объекты        ║ Memory Profiler: Diff двух         ║
║ без снижения после GC    ║ держатся живыми через         ║ снимков. Искать незакрытые         ║
║                          ║ незакрытые события,           ║ EventHandler подписки,             ║
║                          ║ статические ссылки            ║ статические коллекции              ║
╠══════════════════════════╬═══════════════════════════════╬════════════════════════════════════╣
║ string concat в Update   ║ Каждый + создаёт новый        ║ StringBuilder (переиспользовать)   ║
║ GC Alloc 100-500 B/frame ║ string объект в heap          ║ Обновлять только при изменении     ║
║                          ║                               ║ значения, не каждый кадр           ║
╠══════════════════════════╬═══════════════════════════════╬════════════════════════════════════╣
║ LINQ в Update            ║ Каждый LINQ-метод создаёт     ║ Ручная итерация с for-loop         ║
║ GC Alloc 300-800 B/frame ║ IEnumerable объект в heap,    ║ Pre-allocated List + Clear()       ║
║                          ║ ToList() — финальная List<T>  ║ Struct IComparer вместо лямбды     ║
╠══════════════════════════╬═══════════════════════════════╬════════════════════════════════════╣
║ GetComponent в Update    ║ Поиск по массиву компонентов  ║ Кэшировать в Awake()               ║
║                          ║ каждый кадр — O(n) работа     ║ private Rigidbody _rb;             ║
║                          ║                               ║ void Awake() { _rb = GetComponent  ║
║                          ║                               ║ <Rigidbody>(); }                   ║
╠══════════════════════════╬═══════════════════════════════╬════════════════════════════════════╣
║ Instantiate/Destroy в    ║ Каждый Instantiate аллоцирует ║ Object Pool: создать заранее,      ║
║ горячем пути             ║ managed+native память.        ║ переиспользовать. Прогреть пул     ║
║                          ║ Destroy помечает для GC,      ║ в Awake до начала геймплея         ║
║                          ║ не освобождает сразу          ║                                    ║
╠══════════════════════════╬═══════════════════════════════╬════════════════════════════════════╣
║ FindObjectsOfType в      ║ O(n) поиск по всем объектам   ║ Центральный Manager: Registration  ║
║ Update                   ║ сцены каждый кадр             ║ pattern. Объекты регистрируются    ║
║                          ║ + аллокация нового массива    ║ в OnEnable, дерегистрируются       ║
║                          ║                               ║ в OnDisable                        ║
╠══════════════════════════╬═══════════════════════════════╬════════════════════════════════════╣
║ Physics.OverlapSphere    ║ Возвращает новый Collider[]   ║ Physics.OverlapSphereNonAlloc():   ║
║ создаёт массив           ║ каждый вызов — heap аллокация ║ записывает в существующий буфер.  ║
║                          ║                               ║ Объявить static readonly буфер     ║
╠══════════════════════════╬═══════════════════════════════╬════════════════════════════════════╣
║ foreach по Dictionary    ║ В Mono: Enumerator боксируется║ Итерировать по Keys/Values через   ║
║ аллоцирует               ║ как IEnumerator — heap alloc  ║ параллельные List<TKey> и          ║
║                          ║                               ║ List<TValue>. Или for по           ║
║                          ║                               ║ заранее построенному массиву       ║
╠══════════════════════════╬═══════════════════════════════╬════════════════════════════════════╣
║ Boxing value types       ║ Struct/int/enum → object      ║ Использовать generic constraints:  ║
║                          ║ требует heap аллокацию        ║ where T : struct                   ║
║                          ║ для «оборачивания»            ║ EqualityComparer<T>.Default        ║
║                          ║                               ║ для enum ключей в Dictionary       ║
╠══════════════════════════╬═══════════════════════════════╬════════════════════════════════════╣
║ new WaitForSeconds в     ║ Каждый new WaitForSeconds()   ║ Кэшировать статически:             ║
║ корутине каждый вызов    ║ аллоцирует объект в heap      ║ static readonly WaitForSeconds     ║
║                          ║                               ║ Wait1s = new WaitForSeconds(1f);   ║
╠══════════════════════════╬═══════════════════════════════╬════════════════════════════════════╣
║ renderer.material        ║ Создаёт уникальный экземпляр  ║ MaterialPropertyBlock:             ║
║ ломает батчинг           ║ материала для объекта.        ║ _renderer.GetPropertyBlock(_pb);   ║
║                          ║ Объект выходит из батчинга    ║ _pb.SetColor(id, color);           ║
║                          ║ и GPU Instancing              ║ _renderer.SetPropertyBlock(_pb);   ║
╠══════════════════════════╬═══════════════════════════════╬════════════════════════════════════╣
║ Много Draw Calls для     ║ Каждый объект — отдельный     ║ GPU Instancing: один материал +    ║
║ одинаковых объектов      ║ Draw Call без батчинга        ║ Enable GPU Instancing + шейдер     ║
║                          ║                               ║ с #pragma multi_compile_instancing ║
╠══════════════════════════╬═══════════════════════════════╬════════════════════════════════════╣
║ Высокий overdraw         ║ Пиксели закрашиваются         ║ Depth Prepass для опака.           ║
║ (красные зоны)           ║ несколько раз: particles,     ║ Ограничить particle overdraw.      ║
║                          ║ прозрачные объекты, плохой    ║ Скрытый UI: SetActive(false)       ║
║                          ║ порядок рендеринга            ║ а не alpha = 0                     ║
╠══════════════════════════╬═══════════════════════════════╬════════════════════════════════════╣
║ Лишние Physics           ║ Layer Collision Matrix не     ║ Edit → Project Settings →          ║
║ проверки коллизий        ║ настроена: все слои           ║ Physics → Layer Collision Matrix.  ║
║                          ║ взаимодействуют со всеми      ║ Отключить ненужные пары слоёв      ║
╠══════════════════════════╬═══════════════════════════════╬════════════════════════════════════╣
║ Фризы при загрузке       ║ Synchronous Resources.Load    ║ Async loading: LoadSceneAsync,     ║
║ ресурсов во время игры   ║ блокирует Main Thread         ║ Addressables с async API.          ║
║                          ║                               ║ Предзагружать в фоне               ║
╠══════════════════════════╬═══════════════════════════════╬════════════════════════════════════╣
║ Замыкания аллоцируют     ║ Лямбда с захватом переменной  ║ Кэшировать делегат как поле.       ║
║ класс в heap             ║ → компилятор создаёт класс    ║ Передавать данные через параметры, ║
║                          ║ DisplayClass в heap           ║ а не захватывать в замыкание       ║
╠══════════════════════════╬═══════════════════════════════╬════════════════════════════════════╣
║ Animator.SetFloat/Bool   ║ Строковый поиск parameter'а   ║ Кэшировать hash в static поле:     ║
║ с string параметром      ║ в Animator каждый вызов       ║ static readonly int SpeedHash =    ║
║                          ║                               ║ Animator.StringToHash("Speed");    ║
╠══════════════════════════╬═══════════════════════════════╬════════════════════════════════════╣
║ Shader.PropertyToID      ║ Строковый lookup в таблице    ║ Кэшировать int ID в static поле.   ║
║ вызывается в горячем     ║ шейдерных свойств каждый раз  ║ PropertyToID вызывать в Awake      ║
║ пути                     ║                               ║ или как static initializer         ║
╠══════════════════════════╬═══════════════════════════════╬════════════════════════════════════╣
║ Debug.Log в Release      ║ Debug.Log работает в release  ║ [Conditional("DEVELOPMENT_BUILD")] ║
║ аллоцирует строки        ║ если не обёрнут в conditional ║ атрибут на метод логирования.      ║
║                          ║ compilation                   ║ Или #if UNITY_EDITOR блоки         ║
╚══════════════════════════╩═══════════════════════════════╩════════════════════════════════════╝
```

---

## Чеклист production-ready проекта

Используйте этот чеклист перед каждым релизом и как ориентир в процессе разработки.

---

### Блок A: Профилирование и измерения



```csharp
□ A1. Profiler запускался на реальном устройстве (не только в редакторе)
      Разница между редактором и устройством может быть 3-10x

□ A2. Baseline зафиксирован: FPS, frame time, GC Alloc, Draw Calls
      Без baseline невозможно доказать что оптимизация помогла

□ A3. Профилирование проводилось в Development Build
      Редактор добавляет overhead и даёт неточные абсолютные цифры

□ A4. Протестированы минимальные целевые устройства
      Не только флагманы — старший телефон из списка поддерживаемых

□ A5. Профилирование проводилось в "тёплом" состоянии
      После 5-10 минут геймплея, не только при старте

□ A6. Установлены и задокументированы performance budgets
      Frame time: __ms | Draw Calls: __ | GC Alloc/frame: __ bytes
```

---

### Блок B: Memory Management



```csharp
□ B1. GC Allocated In Frame = 0 в steady state (установившийся геймплей)
      Проверить: Profiler → Memory Module → GC Allocated In Frame

□ B2. Нет string concatenation в Update/FixedUpdate/LateUpdate
      Поиск в коде: регулярное выражение: void Update.*\n.*".*"\s*\+

□ B3. Нет LINQ в горячем пути (методы Update, часто вызываемые функции)
      using System.Linq должен отсутствовать в файлах с Update-логикой

□ B4. GetComponent вызывается только в Awake/Start, не в Update
      Все ссылки на компоненты кэшированы в полях класса

□ B5. Object Pool реализован для: пули, эффекты, враги, UI-элементы
      Проверить: Instantiate в Update/FixedUpdate — признак отсутствия пула

□ B6. WaitForSeconds кэшированы как static readonly
      new WaitForSeconds внутри IEnumerator — признак проблемы

□ B7. Все EventHandler подписки закрываются в OnDisable/OnDestroy
      Memory Profiler Diff должен показывать 0 новых объектов после
      reload уровня

□ B8. Managed Heap стабилен: не растёт монотонно за час геймплея
      Memory Profiler: снимок начало сессии vs конец сессии

□ B9. Нет boxing value types через интерфейсы в горячем пути
      Enum как ключ Dictionary: использовать custom EqualityComparer

□ B10. Pre-allocated буферы для Physics.NonAlloc методов
       OverlapSphere → OverlapSphereNonAlloc
       RaycastAll → RaycastNonAlloc
```

---

### Блок C: CPU Performance



```csharp
□ C1. Нет FindObjectsOfType в Update
      Используется Manager/Registry pattern или кэширование

□ C2. Нет Resources.Load во время активного геймплея
      Все ресурсы предзагружены или используется Addressables

□ C3. Physics Layer Collision Matrix настроена
      Проверить: Edit → Project Settings → Physics
      Только нужные пары слоёв имеют коллизии

□ C4. Animator параметры вызываются через hash, не через string
      Animator.StringToHash кэшируется в static readonly поле

□ C5. Shader.PropertyToID кэшируется в static readonly поле
      Не вызывается с string параметром в Update

□ C6. Update-intensive системы используют интервальное обновление
      Не каждый враг делает pathfinding каждый кадр

□ C7. Job System или Burst используется для вычислительно дорогих систем
      (если проект требует высокой производительности симуляции)

□ C8. ProfilerMarker добавлен для ключевых систем
      Позволяет быстро находить проблемы при регрессии
```

---

### Блок D: Rendering



```csharp
□ D1. Draw Calls в пределах бюджета для целевой платформы
      Мобайл: < 100 | PC: < 1000 | Console: ситуационно

□ D2. GPU Instancing включён для повторяющихся объектов (враги, деревья)
      Материал: Enable GPU Instancing ✓
      Шейдер: #pragma multi_compile_instancing

□ D3. renderer.material не используется (только sharedMaterial + PropertyBlock)
      Поиск в коде: renderer.material = | renderer.material.

□ D4. Статичная геометрия помечена как Static для Static Batching
      Inspector → Static → Batching Static

□ D5. Overdraw проверен в Scene View → Shading Mode → Overdraw
      Нет красных зон в игровых сценах

□ D6. ure atlases используются для UI и 2D объектов
      Sprite Atlas в Package Manager → настроен для всех UI спрайтов

□ D7. Mip maps включены для всех 3D текстур (кроме UI)
      Import Settings → Generate Mip Maps ✓

□ D8. ure compression настроена для каждой платформы
      Android: ASTC | iOS: ASTC | PC: DXT5

□ D9. LOD (Level of Detail) настроен для крупных 3D объектов
      LOD Group компонент на сложных мешах

□ D10. Тени ограничены: Shadow Distance, Shadow Cascades
        Quality Settings → Shadows → Shadow Distance разумный

□ D11. Post Processing эффекты профилированы
        Каждый эффект: измерен вклад в GPU время
```

---

### Блок E: Build настройки



```csharp
□ E1. IL2CPP включён для финального билда
      Player Settings → Scripting Backend → IL2CPP
      (не Mono — IL2CPP быстрее в runtime)

□ E2. Code Stripping настроен
      Player Settings → Managed Stripping Level → Medium/High

□ E3. Development Build ВЫКЛЮЧЕН для финального релиза
      Build Settings → Development Build — снять галочку

□ E4. Incremental GC включён или осознанно выключен
      Player Settings → Use Incremental GC
      (включайте если видите GC Spikes > 5ms)

□ E5. Profiler не подключён к релизному билду
      Build Settings → Autoconnect Profiler — снять галочку

□ E6. Stack Trace отключён в релизе
      Player Settings → Stack Trace → None для всех типов логов

□ E7. Physics Fixed Timestep проверен
      Project Settings → Physics → Fixed Timestep
      0.02 (50Hz) — стандарт; 0.016 (60Hz) для точной физики
```

---

### Блок F: Workflow и процесс



```csharp
□ F1. Профилирование включено в Definition of Done
      Фича не готова если GC Alloc > 0 в steady state

□ F2. Performance regression тесты написаны для критических систем
      Unity Test Framework + Performance Testing Package

□ F3. Baseline сохранён в системе контроля версий
      performance_baseline.json рядом с кодом

□ F4. Профилирование на устройстве проводится еженедельно
      Не только перед релизом — проблемы накапливаются постепенно

□ F5. Memory Profiler снимок делается после каждого major feature
      Ранее обнаружить утечки легче чем после накопления

□ F6. Frame Debugger проверяется при изменениях в рендеринге
      Добавили новый материал/шейдер → проверить батчинг
```

---

## Ресурсы

### Официальная документация

|Ресурс|Описание|
|---|---|
|[Unity Profiler Manual](https://docs.unity3d.com/Manual/Profiler.html)|Официальная документация по всем модулям Profiler|
|[Memory Profiler Package](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest)|Документация Memory Profiler с примерами|
|[Frame Debugger](https://docs.unity3d.com/Manual/FrameDebugger.html)|Руководство по Frame Debugger|
|[Understanding Optimization in Unity](https://docs.unity3d.com/Manual/BestPracticeUnderstandingPerformanceInUnity.html)|Best Practices от Unity Technologies|
|[Profile Analyzer](https://docs.unity3d.com/Packages/com.unity.performance.profile-analyzer@latest)|Инструмент сравнения Profiler записей|

### Книги

|Книга|Автор|Почему стоит прочитать|
|---|---|---|
|**Unity Performance Optimization**|Dr. Davide Aversa|Системный подход к оптимизации Unity проектов|
|**Game Programming Patterns**|Robert Nystrom|Паттерны (включая Object Pool) с объяснением мотивации. [Бесплатно онлайн](https://gameprogrammingpatterns.com/)|
|**Pro .NET Memory Management**|Konrad Kokosa|Глубокое понимание GC в .NET/Mono|
|**Real-Time Rendering, 4th Ed.**|Akenine-Möller et al.|Фундаментальные основы GPU рендеринга|

### Видео и курсы

|Ресурс|Описание|
|---|---|
|[Unity Unite talks — Performance](https://www.youtube.com/c/Unity/search?query=performance)|Доклады с Unite конференций по оптимизации|
|[Catlike Coding](https://catlikecoding.com/unity/tutorials/)|Глубокие туториалы включая производительность|
|[Jason Weimann — Optimization](https://www.youtube.com/c/Unity3dCollege)|Практические видео по оптимизации Unity|

### Инструменты

|Инструмент|Платформа|Назначение|
|---|---|---|
|[RenderDoc](https://renderdoc.org/)|PC|Детальный GPU debugging|
|[Xcode Instruments](https://developer.apple.com/instruments/)|iOS/macOS|Нативный профайлер Apple платформ|
|[Android GPU Inspector](https://gpuinspector.dev/)|Android|GPU профилирование на Android|
|[PIX for Windows](https://devblogs.microsoft.com/pix/)|PC/Xbox|GPU профилирование Microsoft|
|[Heap Explorer](https://github.com/pschraut/UnityHeapExplorer)|Unity Editor|Расширенный анализ managed heap|

### Статьи и блоги

|Ресурс|Описание|
|---|---|
|[Unity Blog — Performance](https://blog.unity.com/topic/performance)|Официальный блог Unity с техническими статьями|
|[Gamasutra/Game Developer](https://www.gamedeveloper.com/)|Постмортемы и технические статьи от разработчиков|
|[Aras Pranckevičius Blog](https://aras-p.info/blog/)|Глубокие технические статьи от бывшего Unity инженера|
|[Aleksey Kutsenok Blog](https://blog.unity.com/author/aleksey-kutsenok)|Статьи о DOTS и ECS оптимизациях|

---

## Заключение

Вернёмся к той строчке кода из введения:



```csharp
void Update()
{
    status. = "HP: " + currentHP + "/" + maxHP;
}
```

Три символа — два `+` и один вызов. За час геймплея — 216 000 объектов в памяти. Один фриз перед финальным боссом. Один плохой отзыв.

Исправление заняло бы пять минут. Нахождение проблемы без Profiler'а — несколько часов. С Profiler'ом — две минуты: открыть Memory Module, отсортировать по GC Alloc, увидеть строку кода.

Profiling — это не дополнительная работа. Это способ работать эффективно. Это разница между «мне кажется, что тут всё быстро» и «я знаю, что здесь 0 байт аллокаций в steady state».

Инструменты есть. Методология есть. Теперь есть и знания.

Осталось открыть Profiler.
