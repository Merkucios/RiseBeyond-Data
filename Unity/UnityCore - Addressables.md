# Addressables: профессиональное управление ассетами Unity

# Содержание

- [Введение: когда игра весит 2GB {#введение}](#%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5:%20%D0%BA%D0%BE%D0%B3%D0%B4%D0%B0%20%D0%B8%D0%B3%D1%80%D0%B0%20%D0%B2%D0%B5%D1%81%D0%B8%D1%82%202GB%20%7B#%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%7D)
- [Почему не Resources и не AssetBundles {#почему-не-resources}](#%D0%9F%D0%BE%D1%87%D0%B5%D0%BC%D1%83%20%D0%BD%D0%B5%20Resources%20%D0%B8%20%D0%BD%D0%B5%20AssetBundles%20%7B#%D0%BF%D0%BE%D1%87%D0%B5%D0%BC%D1%83-%D0%BD%D0%B5-resources%7D)
	- [Проблемы папки Resources](#%D0%9F%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D1%8B%20%D0%BF%D0%B0%D0%BF%D0%BA%D0%B8%20Resources)
	- [Проблемы AssetBundles](#%D0%9F%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D1%8B%20AssetBundles)
	- [Что предлагают Addressables](#%D0%A7%D1%82%D0%BE%20%D0%BF%D1%80%D0%B5%D0%B4%D0%BB%D0%B0%D0%B3%D0%B0%D1%8E%D1%82%20Addressables)
- [Архитектура Addressables {#архитектура}](#%D0%90%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D0%B0%20Addressables%20%7B#%D0%B0%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D0%B0%7D)
	- [Диаграмма архитектуры](#%D0%94%D0%B8%D0%B0%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B0%20%D0%B0%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D1%8B)
	- [Пять ключевых понятий](#%D0%9F%D1%8F%D1%82%D1%8C%20%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%B2%D1%8B%D1%85%20%D0%BF%D0%BE%D0%BD%D1%8F%D1%82%D0%B8%D0%B9)
	- [Жизненный цикл ассета](#%D0%96%D0%B8%D0%B7%D0%BD%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9%20%D1%86%D0%B8%D0%BA%D0%BB%20%D0%B0%D1%81%D1%81%D0%B5%D1%82%D0%B0)
- [Настройка с нуля {#настройка}](#%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0%20%D1%81%20%D0%BD%D1%83%D0%BB%D1%8F%20%7B#%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0%7D)
	- [Установка](#%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0)
	- [Структура групп для production-проекта](#%D0%A1%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D0%B3%D1%80%D1%83%D0%BF%D0%BF%20%D0%B4%D0%BB%D1%8F%20production-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
	- [Стратегии упаковки: когда что выбирать](#%D0%A1%D1%82%D1%80%D0%B0%D1%82%D0%B5%D0%B3%D0%B8%D0%B8%20%D1%83%D0%BF%D0%B0%D0%BA%D0%BE%D0%B2%D0%BA%D0%B8:%20%D0%BA%D0%BE%D0%B3%D0%B4%D0%B0%20%D1%87%D1%82%D0%BE%20%D0%B2%D1%8B%D0%B1%D0%B8%D1%80%D0%B0%D1%82%D1%8C)
	- [Назначение адресов программно](#%D0%9D%D0%B0%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B0%D0%B4%D1%80%D0%B5%D1%81%D0%BE%D0%B2%20%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D0%BE)
- [Загрузка ассетов: API и паттерны {#загрузка}](#%D0%97%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B0%20%D0%B0%D1%81%D1%81%D0%B5%D1%82%D0%BE%D0%B2:%20API%20%D0%B8%20%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%D1%8B%20%7B#%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B0%7D)
	- [AsyncOperationHandle — центральный объект системы](#AsyncOperationHandle%20%E2%80%94%20%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B)
	- [LoadAssetAsync: базовая загрузка](#LoadAssetAsync:%20%D0%B1%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D1%8F%20%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B0)
	- [AssetReference: типизированные ссылки](#AssetReference:%20%D1%82%D0%B8%D0%BF%D0%B8%D0%B7%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8)
	- [InstantiateAsync: загрузка и создание экземпляра](#InstantiateAsync:%20%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B0%20%D0%B8%20%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%8D%D0%BA%D0%B7%D0%B5%D0%BC%D0%BF%D0%BB%D1%8F%D1%80%D0%B0)
	- [LoadSceneAsync: загрузка сцен](#LoadSceneAsync:%20%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B0%20%D1%81%D1%86%D0%B5%D0%BD)
	- [Паттерн надёжной загрузки с retry](#%D0%9F%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%20%D0%BD%D0%B0%D0%B4%D1%91%D0%B6%D0%BD%D0%BE%D0%B9%20%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8%20%D1%81%20retry)
- [Управление памятью {#память}](#%D0%A3%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BF%D0%B0%D0%BC%D1%8F%D1%82%D1%8C%D1%8E%20%7B#%D0%BF%D0%B0%D0%BC%D1%8F%D1%82%D1%8C%7D)
	- [Модель подсчёта ссылок](#%D0%9C%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C%20%D0%BF%D0%BE%D0%B4%D1%81%D1%87%D1%91%D1%82%D0%B0%20%D1%81%D1%81%D1%8B%D0%BB%D0%BE%D0%BA)
	- [Правила управления памятью](#%D0%9F%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0%20%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%BF%D0%B0%D0%BC%D1%8F%D1%82%D1%8C%D1%8E)
	- [Обёртка с автоматическим управлением](#%D0%9E%D0%B1%D1%91%D1%80%D1%82%D0%BA%D0%B0%20%D1%81%20%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%BC%20%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%D0%BC)
	- [Кэш ассетов с подсчётом ссылок](#%D0%9A%D1%8D%D1%88%20%D0%B0%D1%81%D1%81%D0%B5%D1%82%D0%BE%D0%B2%20%D1%81%20%D0%BF%D0%BE%D0%B4%D1%81%D1%87%D1%91%D1%82%D0%BE%D0%BC%20%D1%81%D1%81%D1%8B%D0%BB%D0%BE%D0%BA)
- [Labels: групповые операции {#labels}](#Labels:%20%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D0%BE%D0%B2%D1%8B%D0%B5%20%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8%20%7B#labels%7D)
	- [LoadAssetsAsync: загрузка по лейблу](#LoadAssetsAsync:%20%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B0%20%D0%BF%D0%BE%20%D0%BB%D0%B5%D0%B9%D0%B1%D0%BB%D1%83)
	- [Загрузка по нескольким лейблам](#%D0%97%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B0%20%D0%BF%D0%BE%20%D0%BD%D0%B5%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%B8%D0%BC%20%D0%BB%D0%B5%D0%B9%D0%B1%D0%BB%D0%B0%D0%BC)
	- [Проверка ассетов без загрузки](#%D0%9F%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0%20%D0%B0%D1%81%D1%81%D0%B5%D1%82%D0%BE%D0%B2%20%D0%B1%D0%B5%D0%B7%20%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8)
- [Remote-контент и CDN {#remote}](#Remote-%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82%20%D0%B8%20CDN%20%7B#remote%7D)
	- [Настройка профилей](#%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0%20%D0%BF%D1%80%D0%BE%D1%84%D0%B8%D0%BB%D0%B5%D0%B9)
	- [Жизненный цикл remote-контента](#%D0%96%D0%B8%D0%B7%D0%BD%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9%20%D1%86%D0%B8%D0%BA%D0%BB%20remote-%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82%D0%B0)
	- [Полный bootstrap с проверкой обновлений](#%D0%9F%D0%BE%D0%BB%D0%BD%D1%8B%D0%B9%20bootstrap%20%D1%81%20%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%BE%D0%B9%20%D0%BE%D0%B1%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B9)
	- [Локальный сервер для разработки](#%D0%9B%D0%BE%D0%BA%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D1%81%D0%B5%D1%80%D0%B2%D0%B5%D1%80%20%D0%B4%D0%BB%D1%8F%20%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8)
- [Практика: три уровня сложности {#практика}](#%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0:%20%D1%82%D1%80%D0%B8%20%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F%20%D1%81%D0%BB%D0%BE%D0%B6%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%7B#%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0%7D)
	- [Уровень 1: Загрузка спрайтов персонажей](#%D0%A3%D1%80%D0%BE%D0%B2%D0%B5%D0%BD%D1%8C%201:%20%D0%97%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B0%20%D1%81%D0%BF%D1%80%D0%B0%D0%B9%D1%82%D0%BE%D0%B2%20%D0%BF%D0%B5%D1%80%D1%81%D0%BE%D0%BD%D0%B0%D0%B6%D0%B5%D0%B9)
	- [Уровень 2: Система загрузки уровней](#%D0%A3%D1%80%D0%BE%D0%B2%D0%B5%D0%BD%D1%8C%202:%20%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8%20%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D0%B5%D0%B9)
	- [Уровень 3: Remote-контент с симуляцией CDN](#%D0%A3%D1%80%D0%BE%D0%B2%D0%B5%D0%BD%D1%8C%203:%20Remote-%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82%20%D1%81%20%D1%81%D0%B8%D0%BC%D1%83%D0%BB%D1%8F%D1%86%D0%B8%D0%B5%D0%B9%20CDN)
- [Ловушки Addressables: утечки памяти и как их найти {#ловушки}](#%D0%9B%D0%BE%D0%B2%D1%83%D1%88%D0%BA%D0%B8%20Addressables:%20%D1%83%D1%82%D0%B5%D1%87%D0%BA%D0%B8%20%D0%BF%D0%B0%D0%BC%D1%8F%D1%82%D0%B8%20%D0%B8%20%D0%BA%D0%B0%D0%BA%20%D0%B8%D1%85%20%D0%BD%D0%B0%D0%B9%D1%82%D0%B8%20%7B#%D0%BB%D0%BE%D0%B2%D1%83%D1%88%D0%BA%D0%B8%7D)
	- [Ловушка 1: Потеря handle — самая частая утечка](#%D0%9B%D0%BE%D0%B2%D1%83%D1%88%D0%BA%D0%B0%201:%20%D0%9F%D0%BE%D1%82%D0%B5%D1%80%D1%8F%20handle%20%E2%80%94%20%D1%81%D0%B0%D0%BC%D0%B0%D1%8F%20%D1%87%D0%B0%D1%81%D1%82%D0%B0%D1%8F%20%D1%83%D1%82%D0%B5%D1%87%D0%BA%D0%B0)
	- [Ловушка 2: Destroy вместо ReleaseInstance](#%D0%9B%D0%BE%D0%B2%D1%83%D1%88%D0%BA%D0%B0%202:%20Destroy%20%D0%B2%D0%BC%D0%B5%D1%81%D1%82%D0%BE%20ReleaseInstance)
	- [Ловушка 3: Release до завершения загрузки](#%D0%9B%D0%BE%D0%B2%D1%83%D1%88%D0%BA%D0%B0%203:%20Release%20%D0%B4%D0%BE%20%D0%B7%D0%B0%D0%B2%D0%B5%D1%80%D1%88%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8)
	- [Ловушка 4: Использование ассета после Release](#%D0%9B%D0%BE%D0%B2%D1%83%D1%88%D0%BA%D0%B0%204:%20%D0%98%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%B0%D1%81%D1%81%D0%B5%D1%82%D0%B0%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%20Release)
	- [Ловушка 5: Двойной Release](#%D0%9B%D0%BE%D0%B2%D1%83%D1%88%D0%BA%D0%B0%205:%20%D0%94%D0%B2%D0%BE%D0%B9%D0%BD%D0%BE%D0%B9%20Release)
	- [Ловушка 6: Утечка при LoadAssetsAsync с частичной ошибкой](#%D0%9B%D0%BE%D0%B2%D1%83%D1%88%D0%BA%D0%B0%206:%20%D0%A3%D1%82%D0%B5%D1%87%D0%BA%D0%B0%20%D0%BF%D1%80%D0%B8%20LoadAssetsAsync%20%D1%81%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D0%B9%20%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D0%BE%D0%B9)
	- [Диагностика утечек: Event Viewer](#%D0%94%D0%B8%D0%B0%D0%B3%D0%BD%D0%BE%D1%81%D1%82%D0%B8%D0%BA%D0%B0%20%D1%83%D1%82%D0%B5%D1%87%D0%B5%D0%BA:%20Event%20Viewer)
	- [Диагностика через Memory Profiler](#%D0%94%D0%B8%D0%B0%D0%B3%D0%BD%D0%BE%D1%81%D1%82%D0%B8%D0%BA%D0%B0%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20Memory%20Profiler)
	- [Автоматическая проверка утечек в тестах](#%D0%90%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0%20%D1%83%D1%82%D0%B5%D1%87%D0%B5%D0%BA%20%D0%B2%20%D1%82%D0%B5%D1%81%D1%82%D0%B0%D1%85)
	- [Итоговая таблица ловушек](#%D0%98%D1%82%D0%BE%D0%B3%D0%BE%D0%B2%D0%B0%D1%8F%20%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0%20%D0%BB%D0%BE%D0%B2%D1%83%D1%88%D0%B5%D0%BA)
- [Чеклист production-ready {#чеклист}](#%D0%A7%D0%B5%D0%BA%D0%BB%D0%B8%D1%81%D1%82%20production-ready%20%7B#%D1%87%D0%B5%D0%BA%D0%BB%D0%B8%D1%81%D1%82%7D)
	- [Архитектура и настройка](#%D0%90%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D0%B8%20%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0)
	- [Управление памятью](#%D0%A3%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BF%D0%B0%D0%BC%D1%8F%D1%82%D1%8C%D1%8E)
	- [Тестирование](#%D0%A2%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5)
	- [Remote-контент](#Remote-%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82)
	- [Производительность](#%D0%9F%D1%80%D0%BE%D0%B8%D0%B7%D0%B2%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C)
- [Ресурсы {#ресурсы}](#%D0%A0%D0%B5%D1%81%D1%83%D1%80%D1%81%D1%8B%20%7B#%D1%80%D0%B5%D1%81%D1%83%D1%80%D1%81%D1%8B%7D)
	- [Официальная документация](#%D0%9E%D1%84%D0%B8%D1%86%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D1%8F)
	- [Пакеты](#%D0%9F%D0%B0%D0%BA%D0%B5%D1%82%D1%8B)
	- [Инструменты диагностики](#%D0%98%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%B4%D0%B8%D0%B0%D0%B3%D0%BD%D0%BE%D1%81%D1%82%D0%B8%D0%BA%D0%B8)
	- [Дополнительное чтение](#%D0%94%D0%BE%D0%BF%D0%BE%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5%20%D1%87%D1%82%D0%B5%D0%BD%D0%B8%D0%B5)
- [Послесловие](#%D0%9F%D0%BE%D1%81%D0%BB%D0%B5%D1%81%D0%BB%D0%BE%D0%B2%D0%B8%D0%B5)




---

## Введение: когда игра весит 2GB {#введение}

Представьте типичный сценарий. Команда разрабатывает мобильную игру. Дедлайн, фичи добавляются быстрее, чем успевают убираться. Художники кладут текстуры в папку `Resources` — "так быстрее". Через полгода происходит следующее:

- Первый запуск приложения занимает **8 секунд** на среднем Android-устройстве
- Размер установленного приложения — **2.1 GB**
- В `Resources` лежит контент трёх уже удалённых персонажей, которые "были на попробовать"
- Обновить текстуру меча без нового релиза в магазин **невозможно**
- Каждый `Resources.Load` в коде — это строка вида `"Characters/Knight/Idle"`, и никто не знает, что произойдёт если переименовать папку

Это не гипотетическая история — это типичный технический долг проектов, которые начинались как прототипы и выросли в production. Unity Addressables — система, которая решает все перечисленные проблемы системно, а не патчами поверх патчей.

Эта статья написана для разработчика, который уже столкнулся с болью `Resources` или `AssetBundles` и хочет понять Addressables не поверхностно, а как инструмент production-уровня: с архитектурой, паттернами управления памятью, диагностикой утечек и рабочим чеклистом перед релизом.

---

## Почему не Resources и не AssetBundles {#почему-не-resources}

### Проблемы папки Resources

Папка `Resources` — первое, что узнаёт разработчик Unity о загрузке ассетов. Синтаксис подкупает простотой:



```csharp
// Выглядит невинно. Но за этим стоят серьёзные последствия.
var prefab = Resources.Load<GameObject>("Enemies/Dragon");
var icon   = Resources.Load<Sprite>("UI/Icons/Sword");
```

Под капотом происходит следующее: при старте приложения Unity строит индексный файл **всего** содержимого всех папок `Resources` в проекте. Этот процесс блокирует загрузку и не зависит от того, будут ли ассеты реально использованы. Чем больше ассетов — тем длиннее cold start.

**Что идёт не так при масштабировании:**



```csharp
Проблема 1: Bloated build
  ├── Всё содержимое Resources включается в билд без исключений
  ├── Тестовые ассеты, забытые после эксперимента — в продакшне
  └── Нет способа загружать ассеты по требованию

Проблема 2: Невозможность обновления
  ├── Ассет изменился → нужен новый билд → store review → дни ожидания
  └── Hot-fix текстуры или баланс-файла требует полного переиздания

Проблема 3: Строковые пути — источник невидимых ошибок
  ├── "Characters/Knight" — не типизировано, компилятор не проверяет
  ├── Переименовали папку → runtime exception при первом вызове
  └── Рефакторинг превращается в поиск по всей кодовой базе

Проблема 4: Грубое управление памятью
  ├── Resources.UnloadUnusedAssets() — дорого и неточно
  ├── Resources.UnloadAsset() — ручное и опасное
  └── Нет подсчёта ссылок: выгрузили ассет пока другой код его использует → баг
```

### Проблемы AssetBundles

AssetBundles решают часть проблем Resources: ассеты можно загружать с сервера, обновлять независимо от приложения, включать в билд только нужное. Но цена — сложность, которая растёт быстрее проекта:



```csharp
// Реальный код работы с AssetBundles.
// И это ещё упрощённая версия без retry-логики и версионирования.
IEnumerator LoadDragonPrefab()
{
    // 1. Вы сами строите URL и знаете имена бандлов
    var bundleReq = UnityWebRequestAssetBundle
        .GetAssetBundle("https://cdn.example.com/enemies_v7.bundle");
    yield return bundleReq.SendWebRequest();

    if (bundleReq.result != UnityWebRequest.Result.Success)
    {
        Debug.LogError(bundleReq.error);
        yield break;
    }

    var bundle = DownloadHandlerAssetBundle.GetContent(bundleReq);

    // 2. Вы сами знаете что enemies_bundle зависит от materials_bundle
    //    и обязаны загрузить его ПЕРВЫМ. Граф зависимостей — ваша голова.
    var materialBundleReq = UnityWebRequestAssetBundle
        .GetAssetBundle("https://cdn.example.com/materials_v3.bundle");
    yield return materialBundleReq.SendWebRequest();
    // ... обработка ошибок ещё раз ...

    // 3. Вы знаете точное имя ассета внутри бандла
    var assetReq = bundle.LoadAssetAsync<GameObject>("Dragon");
    yield return assetReq;

    Instantiate(assetReq.asset as GameObject);

    // 4. Вы не забыли выгрузить бандл? А зависимости?
    // А как понять что больше никто не использует materials_bundle?
    bundle.Unload(false);
}
```



```csharp
Проблемы AssetBundles:

Ручное управление зависимостями
  └── Dragon.prefab использует материал из materials.bundle?
      Загрузите materials.bundle первым. Вручную. Всегда.

Дублирование ассетов
  └── ure.png не в отдельном бандле?
      Она включена в КАЖДЫЙ бандл, который её использует.
      ×3 бандла = ×3 размер текстуры в памяти при загрузке всех трёх.

Ручное версионирование
  └── Кэш инвалидирован? Новая версия бандла? Пишите логику сами.

Нет удобного инструментария
  └── Анализ дублей — самописный скрипт.
      Просмотр содержимого бандла — сторонние утилиты.
      Профили окружений — самодельные конфиги.
```

### Что предлагают Addressables

Addressables — это **слой абстракции поверх AssetBundles** (именно они используются под капотом), который берёт лучшее из обоих предыдущих подходов и добавляет production-ready инфраструктуру:

|Функция|Resources|AssetBundles|Addressables|
|---|---|---|---|
|Удобный API|✅|❌|✅|
|Загрузка по требованию|❌|✅|✅|
|Remote-контент|❌|✅|✅|
|Автоматические зависимости|✅|❌|✅|
|Подсчёт ссылок|❌|❌|✅|
|Типизированные ссылки|❌|❌|✅|
|Обновление без переиздания|❌|✅|✅|
|Встроенный анализатор|❌|❌|✅|
|Профили окружений|❌|❌|✅|

---

## Архитектура Addressables {#архитектура}

Прежде чем писать код, необходимо понять концептуальную модель системы. Addressables — это не просто "загрузчик файлов", это полноценная система управления контентом с пятью ключевыми компонентами.

### Диаграмма архитектуры



```csharp
┌─────────────────────────────────────────────────────────────────┐
│                        СЛОЙ КОДА                                │
│                                                                 │
│   Addressables.LoadAssetAsync<T>(key)                           │
│   Addressables.LoadSceneAsync(key)                              │
│   Addressables.InstantiateAsync(key)                            │
└────────────────────────┬────────────────────────────────────────┘
                         │ key = Address / Label / AssetReference
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    RESOURCE MANAGER                             │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                      CATALOG                            │   │
│  │                                                         │   │
│  │  "Dragon"          → enemies.bundle @ CDN               │   │
│  │  "UI/Icons/Sword"  → ui.bundle @ Local                  │   │
│  │  "Scenes/Level_01" → level01.bundle @ CDN               │   │
│  │                                                         │   │
│  │  Catalog — JSON-файл, обновляемый независимо от         │   │
│  │  приложения. Ключ механизма hot-fix.                    │   │
│  └──────────────────────────┬──────────────────────────────┘   │
│                             │                                   │
│  ┌──────────────────────────▼──────────────────────────────┐   │
│  │              DEPENDENCY RESOLVER                        │   │
│  │                                                         │   │
│  │  enemies.bundle требует materials.bundle?               │   │
│  │  → Загружает materials.bundle автоматически             │   │
│  │  → Порядок загрузки определяется системой, не вами      │   │
│  └──────────────────────────┬──────────────────────────────┘   │
│                             │                                   │
│  ┌──────────────────────────▼──────────────────────────────┐   │
│  │               REFERENCE COUNTER                         │   │
│  │                                                         │   │
│  │  Dragon: refCount = 2  (два загрузчика держат ссылку)   │   │
│  │  Material: refCount = 1                                 │   │
│  │                                                         │   │
│  │  Release() → refCount--                                 │   │
│  │  refCount = 0 → выгрузка из памяти                      │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│    LOCAL    │  │   REMOTE    │  │   BUILT-IN  │
│  BUNDLES   │  │   BUNDLES   │  │   ASSETS    │
│             │  │             │  │             │
│ Streaming  │  │ CDN /       │  │ В самом     │
│ Assets/    │  │ localhost   │  │ приложении  │
│ AppData/   │  │ /s3/etc.    │  │             │
└─────────────┘  └─────────────┘  └─────────────┘
```

### Пять ключевых понятий

**Address** — строковый ключ, по которому система находит ассет. Это контракт между кодом и контентом: код запрашивает `"Dragon"`, система разбирается где физически лежит файл. Переезд ассета между папками не ломает загрузку — достаточно сохранить тот же адрес.



```csharp
Файловая система             Адрес в Addressables
─────────────────────────    ────────────────────
Assets/Prefabs/Enemies/      →  "Dragon"
  Dragon.prefab                 (можно переместить файл,
                                 адрес останется прежним)

Assets/UI/Icons/Sword.png    →  "UI/Icons/Sword"

Assets/Scenes/Level_01.unity →  "Scenes/Level_01"
```

**Label** — тег для группы ассетов. Один ассет может иметь несколько лейблов. Позволяет загружать наборы ассетов одним вызовом.



```csharp
Dragon.prefab    → labels: ["enemies", "boss", "chapter1"]
Goblin.prefab    → labels: ["enemies", "chapter1"]
Sword.prefab     → labels: ["weapons", "chapter1"]

// Загрузить всё с лейблом "chapter1" — один вызов:
Addressables.LoadAssetsAsync<Object>("chapter1", callback)
```

**Group** — единица упаковки ассетов в бандлы. Определяет стратегию упаковки (один большой бандл или каждый ассет отдельно) и источник загрузки (локально или с сервера).



```csharp
Group "UI_Elements"           Group "Characters"
Pack Together                 Pack Separately
────────────────────          ────────────────────────
MainMenu.prefab  ──┐          Warrior.prefab → warrior.bundle
PauseMenu.prefab   ├→ ui.bundle
HUD.prefab       ──┘          Mage.prefab    → mage.bundle

                              Archer.prefab  → archer.bundle
```

**Profile** — набор переменных для разных окружений. Переключение профиля меняет URL загрузки без изменения кода.



```csharp
Profile: Development          Profile: Production
───────────────────────       ───────────────────────────────
RemoteLoadPath:               RemoteLoadPath:
  http://localhost:9876         https://cdn.example.com/v2.1
```

**Catalog** — JSON-файл с маппингом адресов на физические файлы. Может обновляться независимо от приложения. Именно через обновление каталога работает механизм hot-fix без переиздания.

JSON

```csharp
{
  "m_Keys": ["Dragon", "enemies"],
  "m_Locations": [{
    "m_Keys": ["Dragon"],
    "m_InternalId": "https://cdn.example.com/enemies.bundle",
    "m_Dependencies": ["materials_bundle"]
  }]
}
```

### Жизненный цикл ассета



```csharp
1. Запрос                    2. Lookup в Catalog
   LoadAssetAsync("Dragon")  →  Dragon → enemies.bundle @ CDN
                                         + depends on: materials.bundle

2. Dependency Resolution     4. Загрузка
   materials.bundle нужен?   →  [Download] materials.bundle
   Есть в кэше? Нет          →  [Download] enemies.bundle
   Загрузить первым          →  [Extract] Dragon из enemies.bundle

3. Reference Counting        6. В памяти
   Dragon.refCount = 1       →  Dragon доступен как UnityEngine.Object

4. Release                   8. Выгрузка
   Addressables.Release()    →  Dragon.refCount = 0
                             →  Выгрузка из памяти
                             →  enemies.bundle.refCount--
                             →  materials.bundle.refCount--
```

---

## Настройка с нуля {#настройка}

### Установка



```csharp
Window → Package Manager → поиск "Addressables" → Install
После установки:
Window → Asset Management → Addressables → Groups
При первом открытии: Create Addressables Settings
```

Это создаст папку `Assets/AddressableAssetsData/` — держите её в системе контроля версий.

### Структура групп для production-проекта



```csharp
Addressables Groups
│
├── Default Local Group          ← Базовые ассеты, нужные при старте
│   Pack Together                   (стартовая UI, конфиги)
│   Build: Local / Load: Local
│
├── UI_Elements                  ← Всё UI в одном бандле
│   Pack Together                   Загружается одним HTTP-запросом
│   Build: Local / Load: Local
│
├── Characters                   ← Персонажи по требованию
│   Pack Separately                 Каждый персонаж = отдельный бандл
│   Build: Remote / Load: Remote    Загружаются только нужные
│
├── Levels                       ← Сцены и контент уровней
│   Pack Separately
│   Build: Remote / Load: Remote
│
└── Shared_Assets                ← Общие материалы и текстуры
    Pack Together                   Выносим чтобы избежать дублей
    Build: Remote / Load: Remote
```

### Стратегии упаковки: когда что выбирать

**Pack Together** — все ассеты группы в одном бандле:



```csharp
Когда использовать:
✓ Ассеты всегда загружаются вместе (UI одного экрана)
✓ Нужно минимизировать HTTP-запросы
✓ Ассеты редко обновляются по отдельности

Когда не использовать:
✗ Изменение одного ассета требует перезагрузки всего бандла
✗ Бандл вырастает до 50+ MB (медленная первая загрузка)
```

**Pack Separately** — каждый ассет в своём бандле:



```csharp
Когда использовать:
✓ Ассеты загружаются независимо (персонажи, уровни)
✓ Нужна гранулярность обновлений
✓ Ассеты большого размера

Когда не использовать:
✗ Много мелких ассетов — overhead на каждый HTTP-запрос
✗ Ассеты всегда нужны вместе — лишние запросы
```

### Назначение адресов программно



```csharp
#if UNITY_EDITOR
using UnityEditor.AddressableAssets;
using UnityEditor.AddressableAssets.Settings;
using UnityEditor;

public static class AddressablesSetup
{
    /// <summary>
    /// Делает ассет Addressable и назначает ему адрес и лейблы.
    /// Запускайте из редактор-скрипта при первоначальной настройке проекта.
    /// </summary>
    public static AddressableAssetEntry MakeAddressable(
        string assetPath,
        string address,
        string groupName,
        params string[] labels)
    {
        var settings = AddressableAssetSettingsDefaultObject.Settings;

        // Получаем или создаём группу
        var group = settings.FindGroup(groupName)
                    ?? settings.CreateGroup(
                        groupName,
                        setAsDefaultGroup: false,
                        readOnly: false,
                        postEvent: false,
                        null);

        var guid = AssetDatabase.AssetPathToGUID(assetPath);
        var entry = settings.CreateOrMoveEntry(guid, group, readOnly: false, postEvent: false);

        entry.address = address;

        foreach (var label in labels)
        {
            // Создаём лейбл если не существует, затем добавляем к ассету
            settings.AddLabel(label);
            entry.SetLabel(label, true, true, false);
        }

        settings.SetDirty(
            AddressableAssetSettings.ModificationEvent.EntryMoved,
            entry,
            postEvent: true);
        AssetDatabase.SaveAssets();

        return entry;
    }
}
#endif
```

---

## Загрузка ассетов: API и паттерны {#загрузка}

### AsyncOperationHandle — центральный объект системы

Все операции загрузки возвращают `AsyncOperationHandle<T>`. Это одновременно:

- Объект для ожидания результата
- Токен для управления временем жизни ассета
- Источник информации о прогрессе и ошибках

Никогда не теряйте handle — без него невозможно освободить ассет.

### LoadAssetAsync: базовая загрузка



```csharp
using UnityEngine;
using UnityEngine.AddressableAssets;
using UnityEngine.ResourceManagement.AsyncOperations;
using Cysharp.Threading.Tasks;

public class AssetLoader : MonoBehaviour
{
    // Поле для handle — НЕ локальная переменная
    private AsyncOperationHandle<GameObject> _prefabHandle;

    private async UniTaskVoid LoadDragon()
    {
        // Запуск загрузки — асинхронно, не блокирует поток
        _prefabHandle = Addressables.LoadAssetAsync<GameObject>("Dragon");

        // Ожидание с поддержкой отмены
        await _prefabHandle.ToUniTask(cancellationToken: destroyCancellationToken);

        if (_prefabHandle.Status == AsyncOperationStatus.Succeeded)
        {
            // Result доступен только после успешного завершения
            Instantiate(_prefabHandle.Result, Vector3.zero, Quaternion.identity);
        }
        else
        {
            Debug.LogError(
                $"Failed to load Dragon: {_prefabHandle.OperationException?.Message}"
            );
        }
    }

    private void OnDestroy()
    {
        // Обязательный Release — без него ассет остаётся в памяти
        if (_prefabHandle.IsValid())
            Addressables.Release(_prefabHandle);
    }
}
```

### AssetReference: типизированные ссылки

`AssetReference` — это предпочтительный способ указывать на Addressable-ассеты вместо строк. Назначается через Inspector, проверяется компилятором:



```csharp
public class EnemySpawner : MonoBehaviour
{
    // Назначается в Inspector — drag & drop из Project окна
    // Тип проверяется: AssetReferenceGameObject не даст назначить текстуру
    [SerializeField] private AssetReferenceGameObject _enemyPrefabRef;
    [SerializeField] private AssetReferenceure2D _iconRef;
    [SerializeField] private AssetReferenceT<AudioClip> _spawnSoundRef;

    private readonly List<AsyncOperationHandle> _handles = new();

    public async UniTask<GameObject> SpawnEnemy(Vector3 position)
    {
        var handle = _enemyPrefabRef.LoadAssetAsync<GameObject>();
        _handles.Add(handle);

        await handle.ToUniTask(cancellationToken: destroyCancellationToken);

        if (handle.Status != AsyncOperationStatus.Succeeded)
        {
            Debug.LogError($"Enemy prefab load failed: {handle.OperationException}");
            return null;
        }

        return Instantiate(handle.Result, position, Quaternion.identity);
    }

    private void OnDestroy()
    {
        foreach (var h in _handles)
            if (h.IsValid()) Addressables.Release(h);
    }
}
```

### InstantiateAsync: загрузка и создание экземпляра

`InstantiateAsync` — удобная комбинация загрузки и инстанцирования. Каждый созданный объект управляется отдельно и **должен** освобождаться через `ReleaseInstance`, не через `Destroy`:



```csharp
public class EnemyManager : MonoBehaviour
{
    [SerializeField] private string _enemyAddress = "Enemies/Dragon";

    // Храним созданные объекты для последующего освобождения
    private readonly HashSet<GameObject> _activeEnemies = new();

    public async UniTask<GameObject> SpawnEnemy(Vector3 position)
    {
        var handle = Addressables.InstantiateAsync(
            _enemyAddress,
            position,
            Quaternion.identity
        );

        await handle.ToUniTask(cancellationToken: destroyCancellationToken);

        if (handle.Status != AsyncOperationStatus.Succeeded)
            return null;

        var enemy = handle.Result;
        _activeEnemies.Add(enemy);
        return enemy;
    }

    public void DespawnEnemy(GameObject enemy)
    {
        if (!_activeEnemies.Remove(enemy)) return;

        // ReleaseInstance: уничтожает объект И уменьшает refCount ассета
        // Никогда не используйте Destroy() для объектов из InstantiateAsync
        Addressables.ReleaseInstance(enemy);
    }

    private void OnDestroy()
    {
        foreach (var enemy in _activeEnemies.ToArray())
            Addressables.ReleaseInstance(enemy);

        _activeEnemies.Clear();
    }
}
```

### LoadSceneAsync: загрузка сцен



```csharp
using UnityEngine.ResourceManagement.ResourceProviders;
using UnityEngine.SceneManagement;

public class SceneLoader : MonoBehaviour
{
    private AsyncOperationHandle<SceneInstance> _currentSceneHandle;
    private bool _sceneHandleValid = false;

    public async UniTask LoadLevel(
        string sceneAddress,
        IProgress<float> progress = null,
        CancellationToken cancellationToken = default)
    {
        var previousHandle = _currentSceneHandle;
        var previousValid = _sceneHandleValid;

        // activateOnLoad: false — загружаем сцену, но не переключаемся
        // пока не готовы (можно показать анимацию перехода)
        var handle = Addressables.LoadSceneAsync(
            sceneAddress,
            LoadSceneMode.Additive,
            activateOnLoad: false
        );

        _currentSceneHandle = handle;
        _sceneHandleValid = true;

        // Ожидание с прогрессом
        while (!handle.IsDone)
        {
            progress?.Report(handle.PercentComplete);
            await UniTask.Yield(cancellationToken: cancellationToken);
        }

        if (handle.Status != AsyncOperationStatus.Succeeded)
            throw new Exception($"Failed to load scene '{sceneAddress}'");

        // Активируем новую сцену
        await handle.Result.ActivateAsync().ToUniTask();

        // Выгружаем предыдущую сцену только после активации новой
        if (previousValid && previousHandle.IsValid())
            await Addressables.UnloadSceneAsync(previousHandle).Task;
    }

    private async void OnDestroy()
    {
        if (_sceneHandleValid && _currentSceneHandle.IsValid())
            await Addressables.UnloadSceneAsync(_currentSceneHandle).Task;
    }
}
```

### Паттерн надёжной загрузки с retry



```csharp
public static class AddressablesExtensions
{
    /// <summary>
    /// Загружает ассет с автоматическим повтором при сетевых ошибках.
    /// Подходит для remote-контента с нестабильным соединением.
    /// </summary>
    public static async UniTask<(T asset, AsyncOperationHandle<T> handle)> LoadWithRetry<T>(
        string address,
        int maxAttempts = 3,
        float delayBetweenAttempts = 2f,
        IProgress<float> progress = null,
        CancellationToken cancellationToken = default) where T : UnityEngine.Object
    {
        Exception lastException = null;

        for (int attempt = 1; attempt <= maxAttempts; attempt++)
        {
            cancellationToken.ThrowIfCancellationRequested();

            var handle = Addressables.LoadAssetAsync<T>(address);

            try
            {
                while (!handle.IsDone)
                {
                    progress?.Report(handle.PercentComplete);
                    await UniTask.Yield(cancellationToken: cancellationToken);
                }

                if (handle.Status == AsyncOperationStatus.Succeeded)
                {
                    progress?.Report(1f);
                    return (handle.Result, handle);
                }

                lastException = handle.OperationException;
                Addressables.Release(handle);

                Debug.LogWarning(
                    $"[Addressables] Attempt {attempt}/{maxAttempts} failed " +
                    $"for '{address}': {lastException?.Message}"
                );
            }
            catch (OperationCanceledException)
            {
                if (handle.IsValid()) Addressables.Release(handle);
                throw;
            }

            if (attempt < maxAttempts)
                await UniTask.Delay(
                    TimeSpan.FromSeconds(delayBetweenAttempts),
                    cancellationToken: cancellationToken
                );
        }

        throw new Exception(
            $"Failed to load '{address}' after {maxAttempts} attempts. " +
            $"Last error: {lastException?.Message}",
            lastException
        );
    }
}
```

---

## Управление памятью {#память}

### Модель подсчёта ссылок

Addressables используют reference counting. Это фундаментальный принцип, который отличает систему от `Resources`:



```csharp
Операция                         Dragon.refCount   В памяти
───────────────────────────────  ───────────────   ────────
LoadAssetAsync("Dragon")      →        1           ✅
LoadAssetAsync("Dragon")      →        2           ✅  (второй загрузчик)
Release(handle1)              →        1           ✅  (ещё используется)
Release(handle2)              →        0           ❌  (выгружен)

// Два разных LoadAssetAsync для одного адреса:
// второй НЕ делает сетевого запроса — берёт из кэша
// но ТРЕБУЕТ парного Release
```

### Правила управления памятью



```csharp
ПРАВИЛО 1: Каждый LoadAssetAsync требует парного Release
┌─────────────────────────────────────────────────────┐
│  var handle = Addressables.LoadAssetAsync<T>(addr)  │
│  // ... используем handle.Result ...                │
│  Addressables.Release(handle)  // ОБЯЗАТЕЛЬНО       │
└─────────────────────────────────────────────────────┘

ПРАВИЛО 2: Каждый InstantiateAsync требует ReleaseInstance, не Destroy
┌─────────────────────────────────────────────────────┐
│  var handle = Addressables.InstantiateAsync(addr)   │
│  // ... используем handle.Result (GameObject) ...  │
│  Addressables.ReleaseInstance(gameObject) // НЕ Destroy() │
└─────────────────────────────────────────────────────┘

ПРАВИЛО 3: Не используйте ассет после Release
┌─────────────────────────────────────────────────────┐
│  Addressables.Release(handle)                       │
│  var obj = handle.Result  // ← undefined behavior   │
│  image.sprite = sprite    // ← розовый квадрат      │
└─────────────────────────────────────────────────────┘

ПРАВИЛО 4: Проверяйте IsValid() перед Release
┌─────────────────────────────────────────────────────┐
│  if (handle.IsValid())                              │
│      Addressables.Release(handle)                  │
└─────────────────────────────────────────────────────┘
```

### Обёртка с автоматическим управлением



```csharp
/// <summary>
/// RAII-обёртка для AsyncOperationHandle.
/// Гарантирует Release через IDisposable / финализатор.
/// Используйте в using-блоках или как поле класса с Dispose в OnDestroy.
/// </summary>
public sealed class ManagedAsset<T> : IDisposable where T : UnityEngine.Object
{
    private AsyncOperationHandle<T> _handle;
    private bool _disposed;

    public T Value
    {
        get
        {
            ThrowIfDisposed();
            if (!_handle.IsDone)
                throw new InvalidOperationException("Asset is not loaded yet. Await LoadAsync first.");
            return _handle.Result;
        }
    }

    public bool IsLoaded => !_disposed && _handle.IsValid() && _handle.IsDone
                            && _handle.Status == AsyncOperationStatus.Succeeded;

    private ManagedAsset() { }

    public static async UniTask<ManagedAsset<T>> LoadAsync(
        string address,
        CancellationToken cancellationToken = default)
    {
        var wrapper = new ManagedAsset<T>();
        wrapper._handle = Addressables.LoadAssetAsync<T>(address);

        try
        {
            await wrapper._handle.ToUniTask(cancellationToken: cancellationToken);
        }
        catch (OperationCanceledException)
        {
            // При отмене — освобождаем если операция уже завершилась
            if (wrapper._handle.IsDone && wrapper._handle.IsValid())
                Addressables.Release(wrapper._handle);
            throw;
        }

        if (wrapper._handle.Status != AsyncOperationStatus.Succeeded)
        {
            var ex = wrapper._handle.OperationException;
            if (wrapper._handle.IsValid())
                Addressables.Release(wrapper._handle);
            throw new Exception($"Failed to load '{address}'", ex);
        }

        return wrapper;
    }

    private void ThrowIfDisposed()
    {
        if (_disposed)
            throw new ObjectDisposedException(nameof(ManagedAsset<T>));
    }

    public void Dispose()
    {
        if (_disposed) return;
        _disposed = true;

        if (_handle.IsValid())
            Addressables.Release(_handle);
    }
}

// Использование:
public class SpriteUser : MonoBehaviour
{
    private ManagedAsset<Sprite> _iconAsset;

    private async UniTaskVoid Start()
    {
        // Загружаем
        _iconAsset = await ManagedAsset<Sprite>.LoadAsync(
            "UI/PlayerIcon",
            destroyCancellationToken
        );

        GetComponent<Image>().sprite = _iconAsset.Value;
    }

    private void OnDestroy()
    {
        // Dispose автоматически вызывает Release
        _iconAsset?.Dispose();
    }
}
```

### Кэш ассетов с подсчётом ссылок



```csharp
/// <summary>
/// Централизованный кэш ассетов.
/// Ассет остаётся в памяти пока есть хотя бы один потребитель.
/// Потребители получают/освобождают доступ через Get/Release.
/// </summary>
public class AddressablesCache : MonoBehaviour
{
    public static AddressablesCache Instance { get; private set; }

    private class CacheEntry
    {
        public AsyncOperationHandle Handle;
        public int ConsumerCount;
        public bool IsLoaded => Handle.IsDone
                                && Handle.Status == AsyncOperationStatus.Succeeded;
    }

    private readonly Dictionary<string, CacheEntry> _cache = new();

    private void Awake()
    {
        if (Instance != null) { Destroy(gameObject); return; }
        Instance = this;
        DontDestroyOnLoad(gameObject);
    }

    /// <summary>
    /// Загружает ассет (или возвращает кэшированный).
    /// Вызовите Release(address) когда ассет больше не нужен.
    /// </summary>
    public async UniTask<T> Get<T>(string address, CancellationToken ct = default)
        where T : UnityEngine.Object
    {
        if (!_cache.TryGetValue(address, out var entry))
        {
            entry = new CacheEntry
            {
                Handle = Addressables.LoadAssetAsync<T>(address),
                ConsumerCount = 0
            };
            _cache[address] = entry;
        }

        entry.ConsumerCount++;

        if (!entry.Handle.IsDone)
            await entry.Handle.ToUniTask(cancellationToken: ct);

        if (entry.Handle.Status != AsyncOperationStatus.Succeeded)
        {
            entry.ConsumerCount--;
            if (entry.ConsumerCount <= 0)
            {
                if (entry.Handle.IsValid()) Addressables.Release(entry.Handle);
                _cache.Remove(address);
            }
            throw new Exception(
                $"Cache: failed to load '{address}': {entry.Handle.OperationException}"
            );
        }

        return (T)entry.Handle.Result;
    }

    /// <summary>
    /// Уменьшает счётчик потребителей. Ассет выгружается при нуле.
    /// </summary>
    public void Release(string address)
    {
        if (!_cache.TryGetValue(address, out var entry)) return;

        entry.ConsumerCount--;

        if (entry.ConsumerCount <= 0)
        {
            if (entry.Handle.IsValid())
                Addressables.Release(entry.Handle);
            _cache.Remove(address);

            Debug.Log($"[Cache] Evicted: '{address}'");
        }
    }

    private void OnDestroy()
    {
        foreach (var entry in _cache.Values)
            if (entry.Handle.IsValid())
                Addressables.Release(entry.Handle);

        _cache.Clear();
    }
}
```

---

## Labels: групповые операции {#labels}

### LoadAssetsAsync: загрузка по лейблу



```csharp
public class LevelPreloader : MonoBehaviour
{
    private AsyncOperationHandle<IList<UnityEngine.Object>> _levelAssetsHandle;
    private bool _handleValid = false;

    /// <summary>
    /// Загружает все ассеты с указанным лейблом.
    /// Callback вызывается для каждого загруженного ассета — можно
    /// показывать прогресс или немедленно использовать ассет.
    /// </summary>
    public async UniTask PreloadLevel(string levelLabel, CancellationToken ct = default)
    {
        // Callback для каждого загруженного ассета
        void OnAssetLoaded(UnityEngine.Object asset)
        {
            Debug.Log($"[Preloader] Loaded: {asset.name} ({asset.GetType().Name})");
        }

        _levelAssetsHandle = Addressables.LoadAssetsAsync<UnityEngine.Object>(
            levelLabel,
            OnAssetLoaded
        );
        _handleValid = true;

        await _levelAssetsHandle.ToUniTask(cancellationToken: ct);

        if (_levelAssetsHandle.Status != AsyncOperationStatus.Succeeded)
        {
            Debug.LogError($"[Preloader] Failed: {_levelAssetsHandle.OperationException}");
            return;
        }

        Debug.Log($"[Preloader] Level '{levelLabel}' ready: " +
                  $"{_levelAssetsHandle.Result.Count} assets");
    }

    private void OnDestroy()
    {
        if (_handleValid && _levelAssetsHandle.IsValid())
            Addressables.Release(_levelAssetsHandle);
    }
}
```

### Загрузка по нескольким лейблам



```csharp
public static class LabeledAssetLoader
{
    /// <summary>
    /// MergeMode.Intersection — ассеты со ВСЕМИ указанными лейблами (AND).
    /// MergeMode.Union — ассеты с ЛЮБЫМ из лейблов (OR).
    /// </summary>
    public static async UniTask<(IList<T> assets, AsyncOperationHandle<IList<T>> handle)>
        LoadByLabels<T>(
            IEnumerable<string> labels,
            Addressables.MergeMode mode = Addressables.MergeMode.Intersection,
            CancellationToken ct = default) where T : UnityEngine.Object
    {
        var handle = Addressables.LoadAssetsAsync<T>(
            new List<string>(labels),
            asset => { },
            mode
        );

        await handle.ToUniTask(cancellationToken: ct);

        if (handle.Status != AsyncOperationStatus.Succeeded)
        {
            if (handle.IsValid()) Addressables.Release(handle);
            throw new Exception($"LoadByLabels failed: {handle.OperationException}");
        }

        return (handle.Result, handle);
    }
}

// Примеры использования:
private async UniTaskVoid Examples()
{
    // Все боссы главы 1 — ассеты с лейблами "boss" И "chapter1" одновременно
    var (chapter1Bosses, bossHandle) = await LabeledAssetLoader
        .LoadByLabels<GameObject>(
            new[] { "boss", "chapter1" },
            Addressables.MergeMode.Intersection
        );

    // Все враги ИЛИ все боссы
    var (allThreats, threatsHandle) = await LabeledAssetLoader
        .LoadByLabels<GameObject>(
            new[] { "enemy", "boss" },
            Addressables.MergeMode.Union
        );

    // Не забываем освободить после использования
    Addressables.Release(bossHandle);
    Addressables.Release(threatsHandle);
}
```

### Проверка ассетов без загрузки



```csharp
public static class AssetLocator
{
    /// <summary>
    /// Проверяет существование ассета без его загрузки.
    /// Полезно для валидации конфигурации при старте.
    /// </summary>
    public static async UniTask<bool> Exists(string addressOrLabel)
    {
        var handle = Addressables.LoadResourceLocationsAsync(addressOrLabel);
        await handle.Task;

        bool exists = handle.Status == AsyncOperationStatus.Succeeded
                      && handle.Result.Count > 0;

        Addressables.Release(handle);
        return exists;
    }

    /// <summary>
    /// Возвращает все адреса ассетов с указанным лейблом.
    /// Не загружает сами ассеты.
    /// </summary>
    public static async UniTask<List<string>> GetAddressesByLabel(string label)
    {
        var handle = Addressables.LoadResourceLocationsAsync(label);
        await handle.Task;

        if (handle.Status != AsyncOperationStatus.Succeeded)
        {
            Addressables.Release(handle);
            return new List<string>();
        }

        var addresses = handle.Result
            .Select(loc => loc.PrimaryKey)
            .ToList();

        Addressables.Release(handle);
        return addresses;
    }
}
```

---

## Remote-контент и CDN {#remote}

### Настройка профилей



```csharp
Window → Asset Management → Addressables → Profiles

Profile "LocalServer" (разработка):
  RemoteBuildPath: ServerData/[BuildTarget]
  RemoteLoadPath:  http://localhost:9876/[BuildTarget]

Profile "Staging":
  RemoteBuildPath: ServerData/[BuildTarget]
  RemoteLoadPath:  https://staging.cdn.example.com/[BuildTarget]

Profile "Production":
  RemoteBuildPath: ServerData/[BuildTarget]
  RemoteLoadPath:  https://cdn.example.com/v{AppVersion}/[BuildTarget]
```

Для Remote-группы:



```csharp
Group Schema → Content Packing & Loading:
  Build Path: RemoteBuildPath    ← Remote, не Local
  Load Path:  RemoteLoadPath     ← Remote, не Local
  Update Restriction: Can Change Post Release
```

### Жизненный цикл remote-контента



```csharp
ПЕРВЫЙ ЗАПУСК:
App старт
  → Загрузить catalog.json с CDN
  → Сохранить в локальный кэш
  → При запросе "Dragon": lookup в каталоге
  → Dragon → dragons.bundle @ CDN
  → Скачать dragons.bundle → сохранить в кэш
  → Загрузить Dragon из кэша

СЛЕДУЮЩИЕ ЗАПУСКИ (контент не изменился):
App старт
  → Загрузить catalog.json с CDN
  → Хэш совпадает с кэшем → каталог актуален
  → Dragon уже в кэше → загрузка с диска (быстро)

ОБНОВЛЕНИЕ КОНТЕНТА (hot-fix):
CDN: загружен новый catalog.json + новый dragons.bundle
App старт
  → Загрузить catalog.json с CDN
  → Хэш изменился → каталог обновлён
  → GetDownloadSizeAsync → X MB новых данных
  → DownloadDependenciesAsync → скачать новый dragons.bundle
  → Dragon загружается в новой версии
  (без пересборки приложения!)
```

### Полный bootstrap с проверкой обновлений



```csharp
public class ContentBootstrap : MonoBehaviour
{
    [SerializeField] private BootstrapUI _ui;

    private const string REMOTE_LABEL = "remote_content";

    private async UniTaskVoid Start()
    {
        using var cts = new CancellationTokenSource();
        var token = cts.Token;

        try
        {
            await RunBootstrap(token);
        }
        catch (Exception ex)
        {
            Debug.LogError($"[Bootstrap] Fatal: {ex}");
            _ui.ShowError(ex.Message);
        }
    }

    private async UniTask RunBootstrap(CancellationToken token)
    {
        // ШАГ 1: Инициализация
        _ui.SetStatus("Initializing...", 0f);
        var initHandle = Addressables.InitializeAsync(autoReleaseHandle: false);
        await initHandle.ToUniTask(cancellationToken: token);

        if (initHandle.Status != AsyncOperationStatus.Succeeded)
            throw new Exception($"Init failed: {initHandle.OperationException?.Message}");
        Addressables.Release(initHandle);

        // ШАГ 2: Проверка обновлений каталога
        _ui.SetStatus("Checking for updates...", 0.15f);
        var catalogsToUpdate = await CheckCatalogUpdates(token);

        if (catalogsToUpdate.Count > 0)
        {
            // ШАГ 3: Размер загрузки
            _ui.SetStatus("Calculating download size...", 0.25f);
            long downloadSize = await GetDownloadSize(REMOTE_LABEL, token);

            if (downloadSize > 0)
            {
                float sizeMB = downloadSize / (1024f * 1024f);
                _ui.SetStatus($"Downloading updates ({sizeMB:F1} MB)...", 0.3f);

                // ШАГ 4: Скачивание
                await DownloadContent(REMOTE_LABEL, downloadSize, token);
            }
        }

        // ШАГ 5: Переход в игру
        _ui.SetStatus("Starting...", 0.95f);
        await UniTask.Delay(300, cancellationToken: token);

        await Addressables.LoadSceneAsync("Scenes/MainMenu")
            .ToUniTask(cancellationToken: token);
    }

    private async UniTask<List<string>> CheckCatalogUpdates(CancellationToken token)
    {
        try
        {
            var checkHandle = Addressables.CheckForCatalogUpdates(autoReleaseHandle: false);
            await checkHandle.ToUniTask(cancellationToken: token);

            if (checkHandle.Status != AsyncOperationStatus.Succeeded)
            {
                Addressables.Release(checkHandle);
                Debug.LogWarning("[Bootstrap] Could not check updates. Using cached catalog.");
                return new List<string>();
            }

            var outdated = new List<string>(checkHandle.Result);
            Addressables.Release(checkHandle);

            if (outdated.Count == 0)
                return outdated;

            // Применяем обновления каталога
            var updateHandle = Addressables.UpdateCatalogs(outdated, autoReleaseHandle: false);
            await updateHandle.ToUniTask(cancellationToken: token);
            Addressables.Release(updateHandle);

            Debug.Log($"[Bootstrap] Updated {outdated.Count} catalog(s)");
            return outdated;
        }
        catch (OperationCanceledException) { throw; }
        catch (Exception ex)
        {
            Debug.LogWarning($"[Bootstrap] Catalog check error: {ex.Message}");
            return new List<string>();
        }
    }

    private async UniTask<long> GetDownloadSize(string label, CancellationToken token)
    {
        var handle = Addressables.GetDownloadSizeAsync(label);
        await handle.ToUniTask(cancellationToken: token);
        var size = handle.Result;
        Addressables.Release(handle);
        return size;
    }

    private async UniTask DownloadContent(
        string label,
        long totalBytes,
        CancellationToken token)
    {
        var handle = Addressables.DownloadDependenciesAsync(label, autoReleaseHandle: false);

        while (!handle.IsDone)
        {
            token.ThrowIfCancellationRequested();
            float progress = handle.PercentComplete;
            float downloadedMB = (totalBytes * progress) / (1024f * 1024f);
            float totalMB = totalBytes / (1024f * 1024f);
            _ui.SetStatus($"Downloading... {downloadedMB:F1}/{totalMB:F1} MB",
                           0.3f + progress * 0.6f);
            await UniTask.Yield(cancellationToken: token);
        }

        if (handle.Status != AsyncOperationStatus.Succeeded)
        {
            Addressables.Release(handle);
            throw new Exception($"Download failed: {handle.OperationException}");
        }

        Addressables.Release(handle);
        Debug.Log("[Bootstrap] Download complete");
    }
}
```

### Локальный сервер для разработки



```csharp
#if UNITY_EDITOR
using System.IO;
using System.Net;
using System.;
using System.Threading;
using UnityEditor;
using UnityEngine;

/// <summary>
/// HTTP-сервер симулирующий CDN для тестирования remote-контента в Editor.
/// Tools → Addressables → Start Local Server
/// </summary>
[InitializeOnLoad]
public static class LocalCDNServer
{
    public const int PORT = 9876;
    private static HttpListener _listener;
    private static Thread _thread;
    private static string _root;
    public static bool IsRunning => _listener?.IsListening ?? false;

    static LocalCDNServer()
    {
        EditorApplication.quitting += Stop;
        AssemblyReloadEvents.beforeAssemblyReload += Stop;
    }

    [MenuItem("Tools/Addressables/▶ Start Local CDN Server")]
    public static void Start()
    {
        if (IsRunning) { Debug.Log($"Already running: http://localhost:{PORT}/"); return; }

        _root = Path.Combine(Directory.GetCurrentDirectory(), "ServerData");
        Directory.CreateDirectory(_root);

        _listener = new HttpListener();
        _listener.Prefixes.Add($"http://localhost:{PORT}/");

        try { _listener.Start(); }
        catch (HttpListenerException ex)
        {
            Debug.LogError($"Cannot start server on port {PORT}: {ex.Message}");
            return;
        }

        _thread = new Thread(Loop) { IsBackground = true, Name = "LocalCDN" };
        _thread.Start();

        Debug.Log($"[LocalCDN] Started: http://localhost:{PORT}/\nServing: {_root}");
    }

    [MenuItem("Tools/Addressables/■ Stop Local CDN Server")]
    public static void Stop()
    {
        if (!IsRunning) return;
        _listener.Stop();
        _thread?.Join(500);
        Debug.Log("[LocalCDN] Stopped");
    }

    private static void Loop()
    {
        while (_listener.IsListening)
        {
            HttpListenerCon ctx;
            try { ctx = _listener.GetCon(); }
            catch { break; }
            ThreadPool.QueueUserWorkItem(_ => Serve(ctx));
        }
    }

    private static void Serve(HttpListenerCon ctx)
    {
        var path = Uri.UnescapeDataString(ctx.Request.Url.LocalPath).TrimStart('/');
        var file = Path.GetFullPath(Path.Combine(_root, path));

        if (!file.StartsWith(Path.GetFullPath(_root)))
        {
            ctx.Response.StatusCode = 403;
        }
        else if (!File.Exists(file))
        {
            ctx.Response.StatusCode = 404;
            Debug.LogWarning($"[LocalCDN] 404: /{path}");
        }
        else
        {
            var bytes = File.ReadAllBytes(file);
            ctx.Response.StatusCode = 200;
            ctx.Response.ContentLength64 = bytes.Length;
            ctx.Response.Headers.Add("Access-Control-Allow-Origin", "*");
            ctx.Response.OutputStream.Write(bytes, 0, bytes.Length);
        }
        ctx.Response.OutputStream.Close();
    }
}
#endif
```

---

## Практика: три уровня сложности {#практика}

### Уровень 1: Загрузка спрайтов персонажей

**Задача:** Система выбора персонажа. Спрайты загружаются по требованию. При смене персонажа предыдущий спрайт корректно освобождается.

**Настройка Addressables:**



```csharp
Группа "Characters_Sprites" → Pack Separately
  warrior_idle.png → address: "Characters/Warrior" → label: "characters"
  mage_idle.png    → address: "Characters/Mage"    → label: "characters"
  archer_idle.png  → address: "Characters/Archer"  → label: "characters"
```

**Реализация загрузчика:**



```csharp
public sealed class CharacterSpriteLoader : IDisposable
{
    private AsyncOperationHandle<Sprite> _handle;
    private bool _hasHandle;
    private bool _disposed;
    private CancellationTokenSource _cts;

    public bool IsLoading { get; private set; }

    /// <summary>
    /// Загружает спрайт по адресу. Если идёт предыдущая загрузка — отменяет её.
    /// Предыдущий загруженный спрайт освобождается перед загрузкой нового.
    /// </summary>
    public async UniTask LoadAsync(
        string address,
        Action<Sprite> onSuccess,
        Action<string> onError = null,
        CancellationToken externalToken = default)
    {
        if (_disposed) { onError?.Invoke("Loader disposed"); return; }

        // Отменяем текущую загрузку
        _cts?.Cancel();
        _cts?.Dispose();
        _cts = CancellationTokenSource.CreateLinkedTokenSource(externalToken);

        // Освобождаем предыдущий ассет до начала новой загрузки
        ReleaseHandle();

        IsLoading = true;

        try
        {
            _handle = Addressables.LoadAssetAsync<Sprite>(address);
            _hasHandle = true;

            await _handle.ToUniTask(cancellationToken: _cts.Token);

            if (_handle.Status == AsyncOperationStatus.Succeeded)
            {
                if (!_cts.Token.IsCancellationRequested)
                    onSuccess?.Invoke(_handle.Result);
            }
            else
            {
                var err = _handle.OperationException?.Message ?? "Unknown error";
                onError?.Invoke(err);
                ReleaseHandle();
            }
        }
        catch (OperationCanceledException)
        {
            // Загрузка отменена при смене персонажа — нормально
            if (_hasHandle)
            {
                if (!_handle.IsDone)
                    // Нельзя Release незавершённую операцию — ждём и релизим там
                    _handle.Completed += h => Addressables.Release(h);
                else
                    ReleaseHandle();

                _hasHandle = false;
            }
        }
        finally
        {
            IsLoading = false;
        }
    }

    private void ReleaseHandle()
    {
        if (_hasHandle && _handle.IsValid())
            Addressables.Release(_handle);
        _hasHandle = false;
        _handle = default;
    }

    public void Dispose()
    {
        if (_disposed) return;
        _disposed = true;
        _cts?.Cancel();
        _cts?.Dispose();
        ReleaseHandle();
    }
}
```



```csharp
public class CharacterSelectUI : MonoBehaviour
{
    [SerializeField] private Image _portrait;
    [SerializeField] private Button _prev, _next;
    [SerializeField] private GameObject _spinner;
    [SerializeField] private CharacterData[] _characters;

    private int _index;
    private CharacterSpriteLoader _loader;

    private void Awake()
    {
        _loader = new CharacterSpriteLoader();
        _prev.onClick.AddListener(() => Navigate(-1));
        _next.onClick.AddListener(() => Navigate(1));
    }

    private void Start() => ShowCharacter(0);

    private void Navigate(int dir)
    {
        _index = (_index + dir + _characters.Length) % _characters.Length;
        ShowCharacter(_index);
    }

    private void ShowCharacter(int index)
    {
        _spinner.SetActive(true);
        _portrait.color = new Color(1, 1, 1, 0.5f);

        _loader.LoadAsync(
            _characters[index].spriteAddress,
            onSuccess: sprite =>
            {
                _portrait.sprite = sprite;
                _portrait.color = Color.white;
                _spinner.SetActive(false);
            },
            onError: err =>
            {
                Debug.LogError($"Sprite load failed: {err}");
                _spinner.SetActive(false);
            },
            externalToken: destroyCancellationToken
        ).Forget();
    }

    private void OnDestroy() => _loader?.Dispose();
}
```

**Критерии выполнения:**

- ✅ Спрайты в Addressable-группе с осмысленными адресами
- ✅ Асинхронная загрузка без блокировки главного потока
- ✅ При смене персонажа предыдущий handle освобождается
- ✅ Event Viewer не показывает незакрытых операций
- ✅ UI отображает состояние Loading / Loaded / Error

---

### Уровень 2: Система загрузки уровней

**Задача:** Менеджер уровней загружает сцену и все ассеты уровня по Label. Показывает суммарный прогресс. Корректно выгружает всё при выходе.

**Настройка:**



```csharp
Группа "Level_01" → Pack Together → Remote
  Level_01.unity     → address: "Scenes/Level_01"  → label: "level_01"
  Goblin.prefab      → address: "Level01/Goblin"    → label: "level_01"
  Tileset.png        → address: "Level01/Tileset"   → label: "level_01"
  BGMusic.mp3        → address: "Level01/BGMusic"   → label: "level_01"
```



```csharp
public class LevelManager : MonoBehaviour
{
    public static LevelManager Instance { get; private set; }

    private AsyncOperationHandle<IList<UnityEngine.Object>> _assetsHandle;
    private AsyncOperationHandle<SceneInstance> _sceneHandle;
    private bool _assetsValid, _sceneValid, _loaded;
    private CancellationTokenSource _cts;

    public bool IsLoaded => _loaded;

    private void Awake()
    {
        if (Instance != null) { Destroy(gameObject); return; }
        Instance = this;
        DontDestroyOnLoad(gameObject);
    }

    /// <summary>
    /// Двухэтапная загрузка: сначала ассеты по Label, затем сцена.
    /// assetsWeight определяет долю прогресса для каждого этапа.
    /// </summary>
    public async UniTask<bool> LoadLevelAsync(
        string label,
        string sceneAddress,
        IProgress<(float progress, string status)> progress = null,
        float assetsWeight = 0.6f,
        CancellationToken externalToken = default)
    {
        if (_loaded)
        {
            Debug.LogWarning("[LevelManager] Already loaded. Call Unload first.");
            return false;
        }

        _cts?.Cancel();
        _cts?.Dispose();
        _cts = CancellationTokenSource.CreateLinkedTokenSource(externalToken);
        var token = _cts.Token;

        try
        {
            // ЭТАП 1: Ассеты по Label
            _assetsHandle = Addressables.LoadAssetsAsync<UnityEngine.Object>(label, null);
            _assetsValid = true;

            while (!_assetsHandle.IsDone)
            {
                token.ThrowIfCancellationRequested();
                float p = _assetsHandle.PercentComplete * assetsWeight;
                progress?.Report((p, $"Loading assets ({Mathf.RoundToInt(p / assetsWeight * 100)}%)"));
                await UniTask.Yield(cancellationToken: token);
            }

            if (_assetsHandle.Status != AsyncOperationStatus.Succeeded)
                throw new Exception($"Assets load failed: {_assetsHandle.OperationException}");

            progress?.Report((assetsWeight, $"Assets ready: {_assetsHandle.Result.Count} items"));

            // ЭТАП 2: Сцена
            float sceneWeight = 1f - assetsWeight;
            _sceneHandle = Addressables.LoadSceneAsync(sceneAddress, LoadSceneMode.Additive, false);
            _sceneValid = true;

            while (!_sceneHandle.IsDone)
            {
                token.ThrowIfCancellationRequested();
                float p = assetsWeight + _sceneHandle.PercentComplete * sceneWeight;
                progress?.Report((p, $"Loading scene ({Mathf.RoundToInt(_sceneHandle.PercentComplete * 100)}%)"));
                await UniTask.Yield(cancellationToken: token);
            }

            if (_sceneHandle.Status != AsyncOperationStatus.Succeeded)
                throw new Exception($"Scene load failed: {_sceneHandle.OperationException}");

            // ЭТАП 3: Активация
            progress?.Report((0.97f, "Activating..."));
            await _sceneHandle.Result.ActivateAsync().ToUniTask();

            progress?.Report((1f, "Ready!"));
            _loaded = true;

            Debug.Log($"[LevelManager] Level loaded: '{label}' + '{sceneAddress}'");
            return true;
        }
        catch (OperationCanceledException)
        {
            Debug.Log("[LevelManager] Loading cancelled");
            await CleanupAsync();
            return false;
        }
        catch (Exception ex)
        {
            Debug.LogError($"[LevelManager] Load failed: {ex}");
            await CleanupAsync();
            return false;
        }
    }

    public async UniTask UnloadAsync()
    {
        if (!_loaded) return;
        await CleanupAsync();
        Debug.Log("[LevelManager] Level unloaded");
    }

    private async UniTask CleanupAsync()
    {
        // ПОРЯДОК КРИТИЧЕСКИ ВАЖЕН:
        // 1. Сначала выгружаем сцену (там объекты, использующие ассеты)
        // 2. Потом освобождаем ассеты
        if (_sceneValid && _sceneHandle.IsValid())
        {
            await Addressables.UnloadSceneAsync(_sceneHandle).Task;
            _sceneValid = false;
            _sceneHandle = default;
        }

        if (_assetsValid && _assetsHandle.IsValid())
        {
            Addressables.Release(_assetsHandle);
            _assetsValid = false;
            _assetsHandle = default;
        }

        _loaded = false;
    }

    public void CancelLoading() => _cts?.Cancel();

    private void OnDestroy()
    {
        _cts?.Cancel();
        _cts?.Dispose();

        if (_sceneValid && _sceneHandle.IsValid())
            Addressables.UnloadSceneAsync(_sceneHandle);

        if (_assetsValid && _assetsHandle.IsValid())
            Addressables.Release(_assetsHandle);
    }
}
```

**Критерии выполнения:**

- ✅ Сцена через `LoadSceneAsync`, ассеты через `LoadAssetsAsync`
- ✅ Суммарный прогресс обоих этапов
- ✅ Выгрузка в порядке: сцена → ассеты
- ✅ Повторный вход в уровень работает без накопления handle
- ✅ Кнопка отмены останавливает загрузку и освобождает частично загруженное

---

### Уровень 3: Remote-контент с симуляцией CDN

**Задача:** Полный цикл remote-контента. Запускаем локальный HTTP-сервер, строим remote-бандлы, при перезапуске приложения получаем обновлённый контент без пересборки.

**Workflow:**



```csharp
ПЕРВОНАЧАЛЬНАЯ НАСТРОЙКА:
1. Создать Remote-группу с Build Path = RemoteBuildPath, Load Path = RemoteLoadPath
2. Выбрать профиль "LocalServer" (RemoteLoadPath = http://localhost:9876/[BuildTarget])
3. Tools → Addressables → Build Remote Content
   → ServerData/StandaloneWindows64/ заполнится бандлами
4. Tools → Addressables → Start Local CDN Server
5. Запустить игру → контент загружается с localhost

ЦИКЛ ОБНОВЛЕНИЯ (без пересборки приложения):
1. Изменить любой ассет в Remote-группе
2. Tools → Addressables → Content Update Build
   → Создаётся только изменённый бандл + новый catalog.json
3. Перезапустить игру
   → Bootstrap: CheckForCatalogUpdates → обновление найдено
   → DownloadDependenciesAsync → скачивается только изменённый бандл
   → Ассет отображается в новой версии
```

**Editor-инструменты для workflow:**



```csharp
#if UNITY_EDITOR
using UnityEditor;
using UnityEditor.AddressableAssets;
using UnityEditor.AddressableAssets.Build;
using UnityEditor.AddressableAssets.Settings;

public static class RemoteContentBuildTools
{
    [MenuItem("Tools/Addressables/🔨 Build Remote Content (LocalServer)")]
    public static void BuildForLocalServer()
    {
        var settings = AddressableAssetSettingsDefaultObject.Settings;
        var profileId = settings.profileSettings.GetProfileId("LocalServer");

        if (string.IsNullOrEmpty(profileId))
        {
            Debug.LogError("Profile 'LocalServer' not found. Create it in Addressables Profiles.");
            return;
        }

        var prev = settings.activeProfileId;
        settings.activeProfileId = profileId;

        AddressableAssetSettings.BuildPlayerContent(out var result);
        settings.activeProfileId = prev;

        if (!string.IsNullOrEmpty(result.Error))
            Debug.LogError($"Build failed: {result.Error}");
        else
            Debug.Log($"Build done in {result.Duration:F1}s → ServerData/\n" +
                      "Start local server and run the game.");
    }

    [MenuItem("Tools/Addressables/📦 Content Update Build")]
    public static void BuildUpdate()
    {
        var settings = AddressableAssetSettingsDefaultObject.Settings;
        var statePath = ContentUpdateScript.GetContentStateDataPath(false);

        if (!System.IO.File.Exists(statePath))
        {
            Debug.LogError(
                $"Content state not found: {statePath}\n" +
                "Run a full build first and commit addressables_content_state.bin"
            );
            return;
        }

        var modified = ContentUpdateScript.GatherModifiedEntriesWithDependencies(
            settings, statePath
        );

        if (modified == null || modified.Count == 0)
        {
            Debug.Log("No modified entries. Nothing to update.");
            return;
        }

        foreach (var e in modified)
            Debug.Log($"Modified: {e.address}");

        ContentUpdateScript.CreateContentUpdateGroup(settings, modified, "ContentUpdate");
        ContentUpdateScript.BuildContentUpdate(settings, statePath);
        Debug.Log("Content Update built → upload ServerData/ to CDN");
    }
}
#endif
```

**Критерии выполнения:**

- ✅ Remote-группа с корректными Build/Load Path
- ✅ Локальный сервер раздаёт бандлы без ошибок 404
- ✅ Bootstrap проверяет и применяет обновления каталога
- ✅ Цикл "изменить ассет → Content Update Build → перезапустить → получить" работает
- ✅ `addressables_content_state.bin` сохранён в VCS

---

## Ловушки Addressables: утечки памяти и как их найти {#ловушки}

Этот раздел — самый практически важный. Утечки памяти в Addressables бесшумны: игра работает, но RAM медленно растёт, пока не падает по OOM на устройстве пользователя.

### Ловушка 1: Потеря handle — самая частая утечка



```csharp
// ❌ ПЛОХО: handle — локальная переменная, выходит из scope
private async void LoadAndInstantiate(string address)
{
    var handle = Addressables.LoadAssetAsync<GameObject>(address);
    await handle.Task;
    Instantiate(handle.Result);
    // handle уничтожен сборщиком мусора НА УРОВНЕ C#,
    // но ассет в памяти Unity остаётся навсегда.
    // refCount никогда не обнулится.
}

// ✅ ХОРОШО: handle хранится в поле или коллекции
private readonly List<AsyncOperationHandle> _handles = new();

private async void LoadAndInstantiate(string address)
{
    var handle = Addressables.LoadAssetAsync<GameObject>(address);
    _handles.Add(handle); // ← сохраняем
    await handle.Task;
    Instantiate(handle.Result);
}

private void OnDestroy()
{
    foreach (var h in _handles)
        if (h.IsValid()) Addressables.Release(h);
}
```

**Почему это происходит:** `AsyncOperationHandle` — это struct, не class. Сборщик мусора C# не управляет ассетами Unity. Потеря struct-handle не освобождает ассет — нужен явный `Release`.

### Ловушка 2: Destroy вместо ReleaseInstance



```csharp
// ❌ ПЛОХО: refCount не уменьшается, ассет в памяти
private void KillEnemy(GameObject enemy)
{
    Destroy(enemy); // Unity объект уничтожен, но Addressables не знает
    // Dragon.prefab: refCount = 1 → так и останется
}

// ✅ ХОРОШО: и объект уничтожается, и refCount уменьшается
private void KillEnemy(GameObject enemy)
{
    Addressables.ReleaseInstance(enemy);
    // Dragon.prefab: refCount = 0 → выгрузка из памяти
}
```

**Как обнаружить:** Создайте 10 врагов через `InstantiateAsync`, уничтожьте через `Destroy`. В Event Viewer будут 10 открытых операций на prefab.

### Ловушка 3: Release до завершения загрузки



```csharp
// ❌ ПЛОХО: краш или undefined behavior
private async void BadLoad(string address)
{
    var handle = Addressables.LoadAssetAsync<Sprite>(address);
    Addressables.Release(handle); // операция ещё идёт!
    var sprite = await handle.Task; // поведение неопределено
}

// ✅ ХОРОШО: всегда ждём завершения перед Release
// Или при отмене — используем Completed callback:
private void CancelLoad(AsyncOperationHandle handle)
{
    if (handle.IsDone)
    {
        Addressables.Release(handle);
    }
    else
    {
        // Ждём завершения, потом релизим
        handle.Completed += h => Addressables.Release(h);
    }
}
```

### Ловушка 4: Использование ассета после Release



```csharp
// ❌ ПЛОХО: "розовый квадрат" или нулевая ссылка
private AsyncOperationHandle<Sprite> _handle;

private void SomeMethod()
{
    Addressables.Release(_handle);
    // _handle.Result теперь недействителен
    _image.sprite = _handle.Result; // → розовый квадрат
    Debug.Log(_handle.Result.name); // → NullReferenceException
}

// ✅ ХОРОШО: не используйте Result после Release
// Паттерн: Clear UI → Release, не наоборот
private void UnloadSprite()
{
    _image.sprite = null; // сначала очищаем ссылку
    if (_handle.IsValid())
        Addressables.Release(_handle); // потом освобождаем
}
```

### Ловушка 5: Двойной Release



```csharp
// ❌ ПЛОХО: двойной Release — исключение и повреждение refCount
private void OnDisable()
{
    Addressables.Release(_handle); // первый Release
}

private void OnDestroy()
{
    Addressables.Release(_handle); // второй Release — ошибка!
}

// ✅ ХОРОШО: проверяйте IsValid() перед Release
// После Release handle становится невалидным
private void ReleaseOnce(ref AsyncOperationHandle handle)
{
    if (handle.IsValid())
    {
        Addressables.Release(handle);
        handle = default; // сбрасываем чтобы IsValid() вернул false
    }
}
```

### Ловушка 6: Утечка при LoadAssetsAsync с частичной ошибкой



```csharp
// ❌ ПЛОХО: handle не освобождается при ошибке загрузки
private async UniTask LoadGroupBad(string label)
{
    var handle = Addressables.LoadAssetsAsync<Object>(label, null);
    await handle.Task;

    if (handle.Status != AsyncOperationStatus.Succeeded)
    {
        Debug.LogError("Failed!"); // handle утекает
        return;
    }
    // ...
}

// ✅ ХОРОШО: Release при любом завершении
private async UniTask LoadGroupGood(string label)
{
    var handle = Addressables.LoadAssetsAsync<Object>(label, null);

    try
    {
        await handle.ToUniTask(cancellationToken: destroyCancellationToken);

        if (handle.Status != AsyncOperationStatus.Succeeded)
        {
            Debug.LogError($"Failed: {handle.OperationException}");
            return; // finally выполнит Release
        }

        // Используем handle.Result...
        _savedHandle = handle; // если хотим хранить — сохраняем ДО finally
        return;
    }
    finally
    {
        // ВНИМАНИЕ: если вы сохранили handle в _savedHandle,
        // НЕ освобождайте его здесь — только при ошибке
        if (handle.Status != AsyncOperationStatus.Succeeded && handle.IsValid())
            Addressables.Release(handle);
    }
}
```

### Диагностика утечек: Event Viewer



```csharp
Открыть: Window → Asset Management → Addressables → Event Viewer

Что искать:
┌────────────────────────────────────────────────────────────────┐
│  Event Viewer                                              [●] │
│                                                                │
│  Asset Name              RefCount  Load   Unload  Status      │
│  ─────────────────────────────────────────────────────────    │
│  Dragon.prefab              2        ●             LOADED      │
│  Goblin.prefab              1        ●             LOADED      │
│  warrior_idle.png           0               ●     UNLOADED     │
│  Sword.prefab               1        ●             LOADED      │
│                                                                │
│  ⚠ Dragon.prefab: RefCount=2 после уничтожения всех врагов   │
│    → Утечка: один Release пропущен                            │
└────────────────────────────────────────────────────────────────┘

Нормальная картина:
  Загрузили уровень → RefCount растёт
  Выгрузили уровень → RefCount падает до 0
  Загрузили следующий уровень → другие ассеты

Аномалии:
  RefCount не падает до 0 после выгрузки → утечка
  RefCount = -1 или странные значения → двойной Release
  Операции висят "In Progress" вечно → незавершённый handle
```

### Диагностика через Memory Profiler



```csharp
Workflow поиска утечки:

1. Установить Memory Profiler: Package Manager → Memory Profiler
2. Window → Analysis → Memory Profiler
3. Выполнить тестируемый сценарий:
   a. Снапшот ДО (нажать Take Snapshot)
   b. Загрузить уровень
   c. Выгрузить уровень
   d. Снапшот ПОСЛЕ
4. Compare Snapshots:
   - Раздел "ure2D" / "Mesh" / "AudioClip"
   - Объекты, которые есть в ПОСЛЕ но не в ДО → подозреваемые утечки
   - Проверьте что они действительно должны быть выгружены

Альтернатива — Unity Profiler → Memory:
  - Total Used Memory должна возвращаться к baseline после выгрузки
  - GfxDriver (текстуры) — следите за этим разделом
```

### Автоматическая проверка утечек в тестах



```csharp
// Tests/AddressablesLeakTests.cs
// Требует пакет Unity Test Framework

using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.AddressableAssets;
using UnityEngine.TestTools;

public class AddressablesLeakTests
{
    /// <summary>
    /// Тест проверяет что после Load+Release операция полностью закрыта.
    /// Запускайте в Test Runner перед каждым релизом.
    /// </summary>
    [UnityTest]
    public IEnumerator LoadAndRelease_NoLeaks()
    {
        // Запоминаем количество активных операций до теста
        var operationsBefore = Addressables.ResourceManager.OperationCacheCount;

        // Загружаем и сразу освобождаем
        var handle = Addressables.LoadAssetAsync<GameObject>("Dragon");
        yield return handle;

        Assert.AreEqual(
            AsyncOperationStatus.Succeeded,
            handle.Status,
            "Load should succeed"
        );

        Addressables.Release(handle);

        // Даём один кадр на обработку Release
        yield return null;

        var operationsAfter = Addressables.ResourceManager.OperationCacheCount;

        // Количество активных операций не должно расти
        Assert.LessOrEqual(
            operationsAfter,
            operationsBefore,
            $"Operation leak detected: before={operationsBefore}, after={operationsAfter}"
        );
    }

    [UnityTest]
    public IEnumerator InstantiateAndRelease_NoLeaks()
    {
        var operationsBefore = Addressables.ResourceManager.OperationCacheCount;

        var handle = Addressables.InstantiateAsync("Dragon");
        yield return handle;

        var instance = handle.Result;

        // Правильное освобождение
        Addressables.ReleaseInstance(instance);
        yield return null;

        Assert.LessOrEqual(
            Addressables.ResourceManager.OperationCacheCount,
            operationsBefore,
            "ReleaseInstance should not leave operations open"
        );
    }
}
```

### Итоговая таблица ловушек



```csharp
┌──────────────────────────────────────────────────────────────────────────┐
│                    ЛОВУШКИ ADDRESSABLES: БЫСТРЫЙ СПРАВОЧНИК              │
├────────────────────────┬─────────────────────────┬───────────────────────┤
│ Ловушка                │ Симптом                 │ Решение               │
├────────────────────────┼─────────────────────────┼───────────────────────┤
│ Потеря handle          │ RAM растёт, ассеты не   │ Храните handle в поле │
│                        │ выгружаются             │ или коллекции класса  │
├────────────────────────┼─────────────────────────┼───────────────────────┤
│ Destroy вместо         │ Prefab refCount не       │ ReleaseInstance()     │
│ ReleaseInstance        │ обнуляется              │ вместо Destroy()      │
├────────────────────────┼─────────────────────────┼───────────────────────┤
│ Release незавершённой  │ Краш / исключение       │ Ждите IsDone или      │
│ операции               │ при загрузке            │ используйте Completed │
├────────────────────────┼─────────────────────────┼───────────────────────┤
│ Использование после    │ Розовые квадраты /      │ Очищайте UI до        │
│ Release                │ NullReference           │ вызова Release        │
├────────────────────────┼─────────────────────────┼───────────────────────┤
│ Двойной Release        │ Исключение,             │ Проверяйте IsValid()  │
│                        │ повреждение refCount    │ перед Release         │
├────────────────────────┼─────────────────────────┼───────────────────────┤
│ Неправильный порядок   │ Missing references в    │ Сначала выгружайте    │
│ выгрузки сцены/ассетов │ сцене при unload        │ сцену, потом ассеты   │
├────────────────────────┼─────────────────────────┼───────────────────────┤
│ LoadAssetsAsync без    │ Утечка при ошибке       │ Release в catch/      │
│ Release при ошибке     │ загрузки группы         │ finally блоке         │
└────────────────────────┴─────────────────────────┴───────────────────────┘
```

---

## Чеклист production-ready {#чеклист}

Используйте этот чеклист перед каждым релизом. Каждый пункт — это конкретная проверка, не абстрактная рекомендация.

### Архитектура и настройка



```csharp
АРХИТЕКТУРА
□ Группы разбиты по паттернам загрузки, не по файловой структуре
  Проверка: ассеты всегда нужны вместе → Pack Together
            ассеты нужны независимо   → Pack Separately

□ Общие зависимости (shared ures, materials) вынесены
  в отдельную группу Shared_Assets
  Проверка: Analyze → Check Duplicate Bundle Dependencies → 0 дублей

□ Remote-группы имеют Update Restriction: "Can Change Post Release"
  Проверка: Group → Content Update Restriction в инспекторе

□ addressables_content_state.bin сохранён в VCS и
  протегирован для каждого публичного релиза
  Проверка: git log --all -- "*content_state*"

□ Настроены профили для всех окружений:
  Development, Staging, Production
  Проверка: Addressables Profiles → убедитесь что URL разные
```

### Управление памятью



```csharp
УПРАВЛЕНИЕ ПАМЯТЬЮ
□ Каждый LoadAssetAsync имеет парный Release
  Проверка: Event Viewer → после unload сцены все handles закрыты

□ Все объекты из InstantiateAsync освобождаются через ReleaseInstance
  Проверка: grep -r "Destroy(" --include="*.cs" | grep -v "//.*Destroy"
  (найдёт Destroy() вне комментариев — проверьте каждый случай)

□ Нет локальных handle-переменных без сохранения
  Проверка: code review — поиск паттерна:
  "var handle = Addressables." без "_handle = " или "_handles.Add"

□ OnDestroy/Dispose освобождает все handles
  Проверка: каждый класс с Addressables-загрузкой имеет OnDestroy

□ IsValid() проверяется перед Release
  Проверка: нет прямых Addressables.Release() без if (handle.IsValid())
```

### Тестирование



```csharp
ТЕСТИРОВАНИЕ
□ Addressables Analyze запущен и показывает 0 ошибок
  Window → Addressables → Analyze → Run All

□ Memory Profiler: нет роста памяти после load+unload цикла
  Методология: снапшот до → load → unload → снапшот после → compare

□ Test Runner: тесты на утечки проходят
  Проверка: Tests/AddressablesLeakTests → все зелёные

□ Протестированы edge cases:
  □ Быстрая смена персонажей (race condition в загрузке)
  □ Выход из уровня во время загрузки (cancellation)
  □ Загрузка при отсутствии сети (для remote-групп)
  □ Повторный вход в уровень без перезапуска игры

□ Протестировано на целевых устройствах (не только на PC)
  Особенно важно для мобильных: iOS/Android имеют другие
  бюджеты памяти и поведение GC
```

### Remote-контент



```csharp
REMOTE КОНТЕНТ
□ Build и Load пути в Remote-группах используют Profile-переменные,
  не хардкоженные URL
  Проверка: Group → Schema → Load Path не содержит прямых https://

□ Bootstrapper корректно обрабатывает недоступность CDN
  Проверка: отключите сеть → игра запускается с кэшированным контентом

□ GetDownloadSizeAsync возвращает 0 когда контент актуален
  (нет лишней загрузки при каждом запуске)

□ Workflow Content Update Build проверен end-to-end:
  Изменить ассет → Content Update Build →
  Перезапустить → получить обновление
  Проверка: выполните 2-3 итерации обновления до релиза

□ ServerData/ НЕ попадает в git (добавьте в .gitignore)
  ServerData/ — это build output, не source
```

### Производительность



```csharp
ПРОИЗВОДИТЕЛЬНОСТЬ
□ Время загрузки первого уровня измерено и приемлемо
  Benchmark: < 3 сек на целевом устройстве для мобильных

□ Нет синхронных операций на главном потоке
  Проверка: Profiler → нет пиков от Resources.Load

□ Bundle size разумный:
  □ Ни один бандл не превышает 50 MB (долгая загрузка при сбое)
  □ Shared_Assets бандл < 20 MB (загружается при каждом старте)

□ Asset Load Mode настроен правильно для каждой группы:
  Pack Together → "All Packed Assets" (загружаем всё, раз уж скачали бандл)
  Pack Separately → "Requested Asset and Dependencies"
```

---

## Ресурсы {#ресурсы}

### Официальная документация



```csharp
Документация Unity Addressables:
https://docs.unity3d.com/Packages/com.unity.addressables@latest

Best Practices (официальный гайд по памяти):
https://docs.unity3d.com/Packages/com.unity.addressables@latest/manual/MemoryManagement.html

Content Update Workflow:
https://docs.unity3d.com/Packages/com.unity.addressables@latest/manual/ContentUpdateWorkflow.html

Addressables GitHub (примеры и исходники):
https://github.com/Unity-Technologies/Addressables-Sample
```

### Пакеты



```csharp
UniTask (zero-allocation async для Unity):
https://github.com/Cysharp/UniTask
  → Заменяет async/await Task на UniTask — меньше аллокаций,
    лучшая интеграция с Unity lifecycle

Memory Profiler:
Package Manager → Memory Profiler
  → Детальный анализ памяти, сравнение снапшотов

Profile Analyzer:
Package Manager → Profile Analyzer
  → Сравнение Profiler-сессий до/после оптимизации
```

### Инструменты диагностики



```csharp
Встроенные в Addressables:
  Window → Asset Management → Addressables → Analyze
    → Check Duplicate Bundle Dependencies (самый важный)
    → Check Resources to Addressable Duplicate Dependencies
    → Build Bundle Layout

  Window → Asset Management → Addressables → Event Viewer
    → Мониторинг операций в реальном времени
    → RefCount для каждого ассета

  Window → Asset Management → Addressables → Profiles
    → Управление окружениями

Внешние:
  AssetBundle Browser (устарел, но полезен для инспекции):
  https://github.com/Unity-Technologies/AssetBundles-Browser
```

### Дополнительное чтение



```csharp
"Addressables: Asset management in Unity"
Официальный Unite Talk:
https://www.youtube.com/results?search_query=unity+addressables+unite

Memory in Unity (понимание того как Unity управляет памятью):
https://docs.unity3d.com/Manual/performance-memory-overview.html

AssetBundle fundamentals (что лежит под Addressables):
https://docs.unity3d.com/Manual/AssetBundlesIntro.html
```

---

## Послесловие

Addressables — это не серебряная пуля, которая автоматически решит проблемы плохо спроектированного контент-менеджмента. Это инструмент, который даёт правильные примитивы: подсчёт ссылок, типизированные ссылки, декларативные группы, профили окружений, обновляемый каталог.

Правильное использование требует дисциплины:

- Каждый `LoadAssetAsync` должен иметь парный `Release` — это не рекомендация, это требование корректности программы
- Группы проектируются под паттерны загрузки, не под удобство файловой структуры
- `addressables_content_state.bin` — это артефакт релиза, такой же важный как версия приложения
- Event Viewer запускается не "когда что-то сломается", а регулярно в процессе разработки

Если вы дочитали до этого места и реализовали хотя бы первые два уровня практики — вы уже умеете работать с Addressables лучше, чем большинство проектов на Resources.Load. Остальное — практика и итерации.

---

_В_