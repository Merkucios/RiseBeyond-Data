# UniTask: async/await который работает в Unity

# Содержание

- [Введение](#%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5)
	- [Coroutine-спагетти](#Coroutine-%D1%81%D0%BF%D0%B0%D0%B3%D0%B5%D1%82%D1%82%D0%B8)
	- [Чистый UniTask-код](#%D0%A7%D0%B8%D1%81%D1%82%D1%8B%D0%B9%20UniTask-%D0%BA%D0%BE%D0%B4)
- [Почему Coroutine и Task не справляются](#%D0%9F%D0%BE%D1%87%D0%B5%D0%BC%D1%83%20Coroutine%20%D0%B8%20Task%20%D0%BD%D0%B5%20%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D1%8F%D1%8E%D1%82%D1%81%D1%8F)
	- [Проблемы Coroutine](#%D0%9F%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D1%8B%20Coroutine)
	- [Проблемы System.Threading.Tasks.Task](#%D0%9F%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D1%8B%20System.Threading.Tasks.Task)
- [Что такое UniTask](#%D0%A7%D1%82%D0%BE%20%D1%82%D0%B0%D0%BA%D0%BE%D0%B5%20UniTask)
- [Архитектура](#%D0%90%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D0%B0)
	- [Структура вместо класса](#%D0%A1%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D0%B2%D0%BC%D0%B5%D1%81%D1%82%D0%BE%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B0)
	- [Zero Allocation через пул](#Zero%20Allocation%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20%D0%BF%D1%83%D0%BB)
	- [Интеграция с PlayerLoop](#%D0%98%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F%20%D1%81%20PlayerLoop)
- [Базовый синтаксис](#%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B9%20%D1%81%D0%B8%D0%BD%D1%82%D0%B0%D0%BA%D1%81%D0%B8%D1%81)
	- [Типы возвращаемых значений](#%D0%A2%D0%B8%D0%BF%D1%8B%20%D0%B2%D0%BE%D0%B7%D0%B2%D1%80%D0%B0%D1%89%D0%B0%D0%B5%D0%BC%D1%8B%D1%85%20%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B9)
	- [UniTask.Delay — ожидание с учётом времени Unity](#UniTask.Delay%20%E2%80%94%20%D0%BE%D0%B6%D0%B8%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%81%20%D1%83%D1%87%D1%91%D1%82%D0%BE%D0%BC%20%D0%B2%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%B8%20Unity)
	- [UniTask.Yield — синхронизация с PlayerLoop](#UniTask.Yield%20%E2%80%94%20%D1%81%D0%B8%D0%BD%D1%85%D1%80%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D1%81%20PlayerLoop)
- [CancellationToken](#CancellationToken)
	- [Создание и базовое использование](#%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%B8%20%D0%B1%D0%B0%D0%B7%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5)
	- [GetCancellationTokenOnDestroy — автоматическая отмена](#GetCancellationTokenOnDestroy%20%E2%80%94%20%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D1%82%D0%BC%D0%B5%D0%BD%D0%B0)
	- [Объединение токенов](#%D0%9E%D0%B1%D1%8A%D0%B5%D0%B4%D0%B8%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%82%D0%BE%D0%BA%D0%B5%D0%BD%D0%BE%D0%B2)
	- [Правило передачи токена](#%D0%9F%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%BE%20%D0%BF%D0%B5%D1%80%D0%B5%D0%B4%D0%B0%D1%87%D0%B8%20%D1%82%D0%BE%D0%BA%D0%B5%D0%BD%D0%B0)
- [Параллелизм](#%D0%9F%D0%B0%D1%80%D0%B0%D0%BB%D0%BB%D0%B5%D0%BB%D0%B8%D0%B7%D0%BC)
	- [UniTask.WhenAll — ждём все](#UniTask.WhenAll%20%E2%80%94%20%D0%B6%D0%B4%D1%91%D0%BC%20%D0%B2%D1%81%D0%B5)
	- [UniTask.WhenAny — побеждает первый](#UniTask.WhenAny%20%E2%80%94%20%D0%BF%D0%BE%D0%B1%D0%B5%D0%B6%D0%B4%D0%B0%D0%B5%D1%82%20%D0%BF%D0%B5%D1%80%D0%B2%D1%8B%D0%B9)
- [UniTaskCompletionSource](#UniTaskCompletionSource)
- [Загрузка сцен и ассетов](#%D0%97%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B0%20%D1%81%D1%86%D0%B5%D0%BD%20%D0%B8%20%D0%B0%D1%81%D1%81%D0%B5%D1%82%D0%BE%D0%B2)
	- [Загрузка сцены с прогрессом и переходом](#%D0%97%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B0%20%D1%81%D1%86%D0%B5%D0%BD%D1%8B%20%D1%81%20%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%BE%D0%BC%20%D0%B8%20%D0%BF%D0%B5%D1%80%D0%B5%D1%85%D0%BE%D0%B4%D0%BE%D0%BC)
	- [Параллельная загрузка ассетов](#%D0%9F%D0%B0%D1%80%D0%B0%D0%BB%D0%BB%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B0%20%D0%B0%D1%81%D1%81%D0%B5%D1%82%D0%BE%D0%B2)
	- [UnityWebRequest + UniTask](#UnityWebRequest%20+%20UniTask)
- [Сравнительная таблица](#%D0%A1%D1%80%D0%B0%D0%B2%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0)
- [Практика](#%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0)
	- [Задача 1 (Базовый): переписать корутину на UniTask](#%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0%201%20(%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B9):%20%D0%BF%D0%B5%D1%80%D0%B5%D0%BF%D0%B8%D1%81%D0%B0%D1%82%D1%8C%20%D0%BA%D0%BE%D1%80%D1%83%D1%82%D0%B8%D0%BD%D1%83%20%D0%BD%D0%B0%20UniTask)
	- [Задача 2 (Средний): экран загрузки с параллельными операциями](#%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0%202%20(%D0%A1%D1%80%D0%B5%D0%B4%D0%BD%D0%B8%D0%B9):%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%20%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8%20%D1%81%20%D0%BF%D0%B0%D1%80%D0%B0%D0%BB%D0%BB%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%BC%D0%B8%20%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F%D0%BC%D0%B8)
	- [Задача 3 (Продвинутый): последовательность финального босса](#%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0%203%20(%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%BD%D1%83%D1%82%D1%8B%D0%B9):%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%84%D0%B8%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%B1%D0%BE%D1%81%D1%81%D0%B0)
- [Частые ошибки](#%D0%A7%D0%B0%D1%81%D1%82%D1%8B%D0%B5%20%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D0%B8)
	- [Ошибка 1: `CancellationToken` не передан — отмена не работает](#%D0%9E%D1%88%D0%B8%D0%B1%D0%BA%D0%B0%201:%C2%A0%60CancellationToken%60%C2%A0%D0%BD%D0%B5%20%D0%BF%D0%B5%D1%80%D0%B5%D0%B4%D0%B0%D0%BD%20%E2%80%94%20%D0%BE%D1%82%D0%BC%D0%B5%D0%BD%D0%B0%20%D0%BD%D0%B5%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D0%B5%D1%82)
	- [Ошибка 2: `UniTaskVoid` вместо `UniTask` для awaitable метода](#%D0%9E%D1%88%D0%B8%D0%B1%D0%BA%D0%B0%202:%C2%A0%60UniTaskVoid%60%C2%A0%D0%B2%D0%BC%D0%B5%D1%81%D1%82%D0%BE%C2%A0%60UniTask%60%C2%A0%D0%B4%D0%BB%D1%8F%20awaitable%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D0%B0)
	- [Ошибка 3: забыть `Dispose` для `CancellationTokenSource`](#%D0%9E%D1%88%D0%B8%D0%B1%D0%BA%D0%B0%203:%20%D0%B7%D0%B0%D0%B1%D1%8B%D1%82%D1%8C%C2%A0%60Dispose%60%C2%A0%D0%B4%D0%BB%D1%8F%C2%A0%60CancellationTokenSource%60)
	- [Ошибка 4: обращение к Unity API после уничтожения объекта](#%D0%9E%D1%88%D0%B8%D0%B1%D0%BA%D0%B0%204:%20%D0%BE%D0%B1%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BA%20Unity%20API%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%20%D1%83%D0%BD%D0%B8%D1%87%D1%82%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%B0)
	- [Ошибка 5: не связать `CancellationTokenSource` с `GetCancellationTokenOnDestroy`](#%D0%9E%D1%88%D0%B8%D0%B1%D0%BA%D0%B0%205:%20%D0%BD%D0%B5%20%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D1%82%D1%8C%C2%A0%60CancellationTokenSource%60%C2%A0%D1%81%C2%A0%60GetCancellationTokenOnDestroy%60)
	- [Ошибка 6: последовательный вместо параллельного WhenAll](#%D0%9E%D1%88%D0%B8%D0%B1%D0%BA%D0%B0%206:%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%B2%D0%BC%D0%B5%D1%81%D1%82%D0%BE%20%D0%BF%D0%B0%D1%80%D0%B0%D0%BB%D0%BB%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D0%B3%D0%BE%20WhenAll)
	- [Ошибка 7: `OperationCanceledException` не обработан в `UniTaskVoid`](#%D0%9E%D1%88%D0%B8%D0%B1%D0%BA%D0%B0%207:%C2%A0%60OperationCanceledException%60%C2%A0%D0%BD%D0%B5%20%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D0%BD%20%D0%B2%C2%A0%60UniTaskVoid%60)
	- [Ошибка 8: утечка подписки на событие в `UniTaskCompletionSource`](#%D0%9E%D1%88%D0%B8%D0%B1%D0%BA%D0%B0%208:%20%D1%83%D1%82%D0%B5%D1%87%D0%BA%D0%B0%20%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%BA%D0%B8%20%D0%BD%D0%B0%20%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B5%20%D0%B2%C2%A0%60UniTaskCompletionSource%60)
	- [Ошибка 9: `allowSceneActivation` не выставлен в `false`](#%D0%9E%D1%88%D0%B8%D0%B1%D0%BA%D0%B0%209:%C2%A0%60allowSceneActivation%60%C2%A0%D0%BD%D0%B5%20%D0%B2%D1%8B%D1%81%D1%82%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%20%D0%B2%C2%A0%60false%60)
	- [Ошибка 10: `Task.Delay` вместо `UniTask.Delay` в Unity-коде](#%D0%9E%D1%88%D0%B8%D0%B1%D0%BA%D0%B0%2010:%C2%A0%60Task.Delay%60%C2%A0%D0%B2%D0%BC%D0%B5%D1%81%D1%82%D0%BE%C2%A0%60UniTask.Delay%60%C2%A0%D0%B2%20Unity-%D0%BA%D0%BE%D0%B4%D0%B5)
- [Чеклист](#%D0%A7%D0%B5%D0%BA%D0%BB%D0%B8%D1%81%D1%82)
	- [Перед написанием async метода](#%D0%9F%D0%B5%D1%80%D0%B5%D0%B4%20%D0%BD%D0%B0%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5%D0%BC%20async%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D0%B0)
	- [Управление CancellationToken](#%D0%A3%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20CancellationToken)
	- [Параллелизм](#%D0%9F%D0%B0%D1%80%D0%B0%D0%BB%D0%BB%D0%B5%D0%BB%D0%B8%D0%B7%D0%BC)
	- [Загрузка ресурсов](#%D0%97%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B0%20%D1%80%D0%B5%D1%81%D1%83%D1%80%D1%81%D0%BE%D0%B2)
	- [Исключения и безопасность](#%D0%98%D1%81%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B8%20%D0%B1%D0%B5%D0%B7%D0%BE%D0%BF%D0%B0%D1%81%D0%BD%D0%BE%D1%81%D1%82%D1%8C)
	- [Производительность](#%D0%9F%D1%80%D0%BE%D0%B8%D0%B7%D0%B2%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C)
	- [Отладка](#%D0%9E%D1%82%D0%BB%D0%B0%D0%B4%D0%BA%D0%B0)
- [Ресурсы](#%D0%A0%D0%B5%D1%81%D1%83%D1%80%D1%81%D1%8B)
	- [Официальные источники](#%D0%9E%D1%84%D0%B8%D1%86%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D0%B8%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8)
	- [Документация и статьи](#%D0%94%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B8%20%D1%81%D1%82%D0%B0%D1%82%D1%8C%D0%B8)
	- [Смежные библиотеки](#%D0%A1%D0%BC%D0%B5%D0%B6%D0%BD%D1%8B%D0%B5%20%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B8)
	- [Инструменты отладки](#%D0%98%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BE%D1%82%D0%BB%D0%B0%D0%B4%D0%BA%D0%B8)


---

## Введение

Посмотрите на два куска кода. Оба делают одно и то же: показывают UI-панель с анимацией, ждут, скрывают.

### Coroutine-спагетти



```csharp
// ❌ Coroutine-версия — 60 строк боли
public class UIPanel_Coroutine : MonoBehaviour
{
    [SerializeField] private CanvasGroup _canvasGroup;
    [SerializeField] private RectTransform _rect;

    private Coroutine _active;
    private bool _result;          // костыль: "возвращаемое значение"
    private bool _wasDestroyed;    // костыль: проверка уничтожения

    public void Show(System.Action<bool> onComplete)
    {
        if (_active != null) StopCoroutine(_active);
        _active = StartCoroutine(ShowSequence(onComplete));
    }

    private IEnumerator ShowSequence(System.Action<bool> onComplete)
    {
        // появление — нельзя запустить параллельно без ещё одной корутины
        yield return StartCoroutine(Fade(0f, 1f, 0.3f));
        yield return StartCoroutine(Slide(-200f, 0f, 0.3f));

        // ждём ввода — нет нормального способа вернуть значение
        _result = false;
        yield return StartCoroutine(WaitForInput());

        // скрытие — "параллельно" через костыль
        Coroutine c1 = StartCoroutine(Fade(1f, 0f, 0.3f));
        Coroutine c2 = StartCoroutine(Slide(0f, -200f, 0.3f));
        yield return c1;
        yield return c2;    // НЕ параллельно — c2 уже закончилась к этому моменту

        // ОПАСНО: объект мог быть уничтожен, пока мы ждали
        if (!_wasDestroyed)
            onComplete?.Invoke(_result);
    }

    private IEnumerator Fade(float from, float to, float duration)
    {
        float t = 0f;
        while (t < duration)
        {
            t += Time.deltaTime;
            _canvasGroup.alpha = Mathf.Lerp(from, to, t / duration);
            yield return null;
        }
        _canvasGroup.alpha = to;
    }

    private IEnumerator Slide(float fromX, float toX, float duration)
    {
        float t = 0f;
        var pos = _rect.anchoredPosition;
        while (t < duration)
        {
            t += Time.deltaTime;
            pos.x = Mathf.Lerp(fromX, toX, t / duration);
            _rect.anchoredPosition = pos;
            yield return null;
        }
        pos.x = toX;
        _rect.anchoredPosition = pos;
    }

    private IEnumerator WaitForInput()
    {
        // нет нормального способа вернуть значение из корутины
        while (!Input.GetKeyDown(KeyCode.Return) && !Input.GetKeyDown(KeyCode.Escape))
            yield return null;
        _result = Input.GetKeyDown(KeyCode.Return);
    }

    private void OnDestroy() => _wasDestroyed = true;
}
```

### Чистый UniTask-код



```csharp
// ✅ UniTask-версия — читается как синхронный код
public class UIPanel_UniTask : MonoBehaviour
{
    [SerializeField] private CanvasGroup _canvasGroup;
    [SerializeField] private RectTransform _rect;

    // возвращает реальный bool, поддерживает await, отменяется при Destroy
    public async UniTask<bool> ShowAsync(CancellationToken ct = default)
    {
        // появление — последовательно
        await FadeAsync(0f, 1f, 0.3f, ct);
        await SlideAsync(-200f, 0f, 0.3f, ct);

        // ждём ввода — возвращает настоящее значение
        bool confirmed = await WaitForInputAsync(ct);

        // скрытие — по-настоящему параллельно
        await UniTask.WhenAll(
            FadeAsync(1f, 0f, 0.3f, ct),
            SlideAsync(0f, -200f, 0.3f, ct)
        );

        return confirmed;
        // объект уничтожен? ct сработает — OperationCanceledException,
        // код ниже не выполнится, утечек нет
    }

    private async UniTask FadeAsync(float from, float to, float dur, CancellationToken ct)
    {
        float t = 0f;
        _canvasGroup.alpha = from;
        while (t < dur)
        {
            await UniTask.Yield(PlayerLoopTiming.Update, ct);
            t += Time.deltaTime;
            _canvasGroup.alpha = Mathf.Lerp(from, to, Mathf.Clamp01(t / dur));
        }
        _canvasGroup.alpha = to;
    }

    private async UniTask SlideAsync(float fromX, float toX, float dur, CancellationToken ct)
    {
        float t = 0f;
        var pos = _rect.anchoredPosition;
        pos.x = fromX;
        _rect.anchoredPosition = pos;
        while (t < dur)
        {
            await UniTask.Yield(PlayerLoopTiming.Update, ct);
            t += Time.deltaTime;
            pos.x = Mathf.Lerp(fromX, toX, Mathf.Clamp01(t / dur));
            _rect.anchoredPosition = pos;
        }
        pos.x = toX;
        _rect.anchoredPosition = pos;
    }

    private async UniTask<bool> WaitForInputAsync(CancellationToken ct)
    {
        await UniTask.WaitUntil(
            () => Input.GetKeyDown(KeyCode.Return) || Input.GetKeyDown(KeyCode.Escape),
            cancellationToken: ct
        );
        return Input.GetKeyDown(KeyCode.Return);
    }
}

// Вызов — никаких callback-ов, никаких костылей
public class GameController : MonoBehaviour
{
    [SerializeField] private UIPanel_UniTask _panel;

    private async UniTaskVoid OnButtonClicked()
    {
        var ct = this.GetCancellationTokenOnDestroy();
        try
        {
            bool confirmed = await _panel.ShowAsync(ct);
            Debug.Log(confirmed ? "Подтверждено" : "Отменено");
        }
        catch (OperationCanceledException)
        {
            Debug.Log("Панель закрыта досрочно");
        }
    }
}
```

Разница очевидна. UniTask-код читается сверху вниз, как синхронный. Возвращает настоящие значения. Отменяется автоматически. Не требует костылей.

---

## Почему Coroutine и Task не справляются

### Проблемы Coroutine

Корутины появились в Unity задолго до того, как C# получил `async/await`. Это итераторы (`IEnumerator`) с иллюзией асинхронности. Каждый `yield return` — это точка, в которой Unity приостанавливает выполнение и продолжает его на следующем кадре.

**Проблема 1: нет возвращаемых значений.**



```csharp
// Как вернуть результат из корутины? Только через поле — это антипаттерн
private string _loadedData; // состояние размазано по классу

private IEnumerator LoadData()
{
    yield return new WaitForSeconds(1f);
    _loadedData = "result";   // пишем в поле вместо return
}

private IEnumerator UseData()
{
    yield return StartCoroutine(LoadData());
    Debug.Log(_loadedData);   // читаем из поля — неявная зависимость
}
```

**Проблема 2: исключения поглощаются.**



```csharp
private IEnumerator BrokenCoroutine()
{
    yield return null;
    throw new Exception("Ошибка!");
    // Unity выведет в консоль, но перехватить снаружи НЕВОЗМОЖНО
}

private void Start()
{
    try
    {
        StartCoroutine(BrokenCoroutine()); // try/catch здесь бесполезен
    }
    catch (Exception e)
    {
        Debug.Log(e); // никогда не выполнится
    }
}
```

**Проблема 3: привязка к MonoBehaviour.**



```csharp
// Чистый C# класс — корутины недоступны
public class PlayerRepository
{
    public IEnumerator LoadPlayer() // ошибка компиляции — нет StartCoroutine
    {
        yield return new WaitForSeconds(1f);
    }
}
```

**Проблема 4: параллелизм через костыли.**



```csharp
// "Параллельный" запуск двух корутин
private IEnumerator FakeParallel()
{
    Coroutine a = StartCoroutine(OperationA());
    Coroutine b = StartCoroutine(OperationB());
    yield return a; // ждём A
    yield return b; // B уже могла завершиться — это не настоящий WhenAll
}
```

**Проблема 5: аллокации на каждый кадр.**



```csharp
// Каждый вызов создаёт новый объект в куче — нагрузка на GC
yield return new WaitForSeconds(1f);      // аллокация
yield return new WaitForEndOfFrame();     // аллокация
yield return new WaitUntil(() => ready); // аллокация + closure
```

### Проблемы System.Threading.Tasks.Task

`Task` из .NET решает часть проблем корутин, но создаёт новые — специфичные для Unity.

**Проблема 1: выполнение не в главном потоке.**



```csharp
private async Task UpdatePosition()
{
    await Task.Delay(1000);
    // После await можем оказаться в потоке из ThreadPool
    transform.position = Vector3.zero; // UnityException: не главный поток!
}
```

**Проблема 2: аллокации при каждом создании.**



```csharp
// Task — ссылочный тип, каждый new Task() — объект в куче
// В игровом цикле это неприемлемо
private async Task UpdateEveryFrame()
{
    while (true)
    {
        await Task.Yield(); // аллокация каждый кадр → GC spikes
        DoWork();
    }
}
```

**Проблема 3: игнорирование `Time.timeScale`.**



```csharp
private async Task IgnoresPause()
{
    Time.timeScale = 0f;          // пауза игры
    await Task.Delay(1000);       // продолжает идти в реальном времени
    // UniTask.Delay с DelayType.DeltaTime остановится вместе с игрой
}
```

**Проблема 4: нет интеграции с PlayerLoop.**

`Task.Delay` использует системный таймер, не синхронизированный с Unity. Продолжения после `await Task.Delay` могут выполняться между фазами Update, LateUpdate, FixedUpdate — непредсказуемо.

---

## Что такое UniTask

**UniTask** — библиотека с открытым кодом, созданная Yoshifumi Kawai. Это полноценная реализация `async/await`, разработанная специально для Unity.

**Ключевые принципы:**

- **Zero allocation** — структура вместо класса, пул объектов для асинхронных операций
- **Главный поток по умолчанию** — продолжения всегда в главном потоке Unity
- **Интеграция с PlayerLoop** — выполнение в нужной фазе игрового цикла
- **Полная поддержка `CancellationToken`** — включая `GetCancellationTokenOnDestroy`

**Установка:**



```csharp
// Package Manager → Add package from git URL:
https://github.com/Cysharp/UniTask.git?path=src/UniTask/Assets/Plugins/UniTask
```

---

## Архитектура

### Структура вместо класса

Центральная идея UniTask — `UniTask` является `struct`, а не `class`. Стандартный `Task<T>` — объект в куче. `UniTask<T>` — значимый тип.



```csharp
// System.Task — ссылочный тип
Task<int> task = SomeMethod();   // объект в куче, нагрузка на GC

// UniTask — значимый тип
UniTask<int> uniTask = SomeMethod(); // в стеке или встроен в другую структуру
```

Внутреннее устройство:



```csharp
// Упрощённое представление
public readonly struct UniTask
{
    // null если задача уже завершена синхронно — нет аллокации вообще
    private readonly IUniTaskSource source;
    // Версия токена — защита от повторного await одной задачи
    private readonly short token;
}
```

Если задача завершается синхронно (результат уже готов) — аллокации нет совсем. Если асинхронно — используется пул переиспользуемых объектов.

### Zero Allocation через пул



```csharp
// Внутри UniTask — переиспользование вместо создания
internal class DelayPromise : IUniTaskSource, IPlayerLoopItem
{
    // Статический пул — один на всё приложение
    private static TaskPool<DelayPromise> pool;

    public static IUniTaskSource Create(int delayMs, CancellationToken ct)
    {
        // Берём из пула — без аллокации
        if (!pool.TryPop(out var result))
            result = new DelayPromise(); // создаём только если пул пуст

        result.Initialize(delayMs, ct);
        return result;
    }

    private void Return()
    {
        Reset();
        pool.TryPush(this); // возвращаем в пул после завершения
    }
}
```

### Интеграция с PlayerLoop

Unity управляет порядком выполнения подсистем через `PlayerLoopSystem`. UniTask встраивается напрямую в этот механизм:



```csharp
[RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.BeforeSceneLoad)]
static void Init()
{
    var playerLoop = PlayerLoop.GetCurrentPlayerLoop();

    // UniTask регистрирует runners в каждой фазе:
    // Initialization, EarlyUpdate, FixedUpdate,
    // PreUpdate, Update, PreLateUpdate, PostLateUpdate
    PlayerLoopHelper.Initialize(ref playerLoop);

    PlayerLoop.SetPlayerLoop(playerLoop);
}
```

Это означает: `await UniTask.Yield(PlayerLoopTiming.FixedUpdate)` — продолжение выполнится **строго** в фазе FixedUpdate, не раньше и не позже.



```csharp
Кадр N:
├── EarlyUpdate
│   └── [UniTask: EarlyUpdate runners]
├── FixedUpdate
│   └── [UniTask: FixedUpdate runners] ← await Yield(FixedUpdate) продолжится здесь
├── Update
│   └── [UniTask: Update runners]      ← await Yield() / Delay() по умолчанию здесь
├── LateUpdate
└── PostLateUpdate
    └── [UniTask: PostLateUpdate runners]
```

---

## Базовый синтаксис

### Типы возвращаемых значений



```csharp
public class SyntaxExamples : MonoBehaviour
{
    // Нет значения, можно await-ить — основной тип
    private async UniTask DoWorkAsync()
    {
        await UniTask.Delay(500);
    }

    // Есть значение
    private async UniTask<int> ComputeAsync()
    {
        await UniTask.Delay(100);
        return 42;
    }

    // Fire-and-forget: нельзя await-ить, исключения идут в глобальный обработчик
    // Используйте ТОЛЬКО когда намеренно не ждёте результата
    private async UniTaskVoid FireAndForgetAsync()
    {
        await UniTask.Delay(100);
        Debug.Log("Готово");
    }

    private async UniTaskVoid Start()
    {
        await DoWorkAsync();                    // ждём завершения

        int value = await ComputeAsync();       // получаем результат
        Debug.Log(value);                       // 42

        FireAndForgetAsync().Forget();          // запускаем и забываем
        DoWorkAsync().Forget(ex =>             // с обработчиком ошибок
            Debug.LogException(ex));
    }
}
```

### UniTask.Delay — ожидание с учётом времени Unity



```csharp
private async UniTask DelayExamples(CancellationToken ct)
{
    // Игровое время — останавливается при timeScale = 0
    await UniTask.Delay(1000, cancellationToken: ct);
    await UniTask.Delay(TimeSpan.FromSeconds(2.5f), cancellationToken: ct);

    // Явный DelayType
    await UniTask.Delay(1000, DelayType.DeltaTime,        ct); // по умолчанию
    await UniTask.Delay(1000, DelayType.UnscaledDeltaTime, ct); // игнорирует timeScale
    await UniTask.Delay(1000, DelayType.Realtime,          ct); // системные часы

    // Ожидание по условию
    bool isReady = false;
    await UniTask.WaitUntil(() => isReady, cancellationToken: ct);
    await UniTask.WaitWhile(() => !isReady, cancellationToken: ct);
}
```

### UniTask.Yield — синхронизация с PlayerLoop



```csharp
private async UniTask YieldExamples(CancellationToken ct)
{
    // Следующий Update (аналог yield return null)
    await UniTask.Yield(ct);
    await UniTask.Yield(PlayerLoopTiming.Update, ct);   // то же самое явно

    // Другие фазы
    await UniTask.Yield(PlayerLoopTiming.FixedUpdate, ct);
    await UniTask.Yield(PlayerLoopTiming.LastUpdate, ct);    // конец Update
    await UniTask.Yield(PlayerLoopTiming.PostLateUpdate, ct);

    // Следующий кадр (семантически более явно чем Yield)
    await UniTask.NextFrame(ct);

    // Конец кадра — для ReadPixels, ure2D операций
    await UniTask.WaitForEndOfFrame(this, ct);
}
```

---

## CancellationToken

`CancellationToken` — стандартный механизм .NET для отмены операций. UniTask интегрирует его с жизненным циклом объектов Unity.

### Создание и базовое использование



```csharp
public class CancellationExamples : MonoBehaviour
{
    private CancellationTokenSource _cts;

    private void Start()
    {
        _cts = new CancellationTokenSource();
        RunAsync(_cts.Token).Forget();
    }

    private async UniTask RunAsync(CancellationToken ct)
    {
        try
        {
            for (int i = 0; i < 10; i++)
            {
                await UniTask.Delay(1000, cancellationToken: ct);
                Debug.Log($"Шаг {i}");
            }
        }
        catch (OperationCanceledException)
        {
            Debug.Log("Отменено — штатная ситуация, не ошибка");
        }
    }

    public void Cancel() => _cts?.Cancel();

    private void OnDestroy()
    {
        _cts?.Cancel();
        _cts?.Dispose(); // обязательно!
    }
}
```

### GetCancellationTokenOnDestroy — автоматическая отмена

Самый важный паттерн в UniTask для Unity:



```csharp
public class AutoCancelExample : MonoBehaviour
{
    private async UniTaskVoid Start()
    {
        // Токен отменяется автоматически при Destroy(gameObject)
        // Не нужен OnDestroy, не нужен ручной CTS
        var ct = this.GetCancellationTokenOnDestroy();

        await LongOperationAsync(ct);
        // Если объект уничтожен во время ожидания —
        // OperationCanceledException, код ниже не выполнится
        Debug.Log("Завершено");
    }

    private async UniTask LongOperationAsync(CancellationToken ct)
    {
        await UniTask.Delay(5000, cancellationToken: ct);
    }
}
```

### Объединение токенов



```csharp
public class LinkedTokenExample : MonoBehaviour
{
    private CancellationTokenSource _manualCts;

    private async UniTaskVoid Start()
    {
        var destroyCt = this.GetCancellationTokenOnDestroy();
        _manualCts = new CancellationTokenSource();

        // Операция отменяется при ЛЮБОМ из условий:
        // уничтожение объекта ИЛИ ручная отмена ИЛИ таймаут
        using var timeoutCts = new CancellationTokenSource(TimeSpan.FromSeconds(30));
        using var linkedCts = CancellationTokenSource.CreateLinkedTokenSource(
            destroyCt,
            _manualCts.Token,
            timeoutCts.Token
        );

        try
        {
            await DoWorkAsync(linkedCts.Token);
        }
        catch (OperationCanceledException)
        {
            Debug.Log("Отменено по одной из причин");
        }
    }

    public void CancelManually() => _manualCts?.Cancel();

    private void OnDestroy()
    {
        _manualCts?.Dispose();
    }

    private async UniTask DoWorkAsync(CancellationToken ct)
    {
        await UniTask.Delay(10000, cancellationToken: ct);
    }
}
```

### Правило передачи токена



```csharp
Правило: токен всегда приходит снаружи, создаётся у "владельца" операции.

Владелец операции (MonoBehaviour/сервис верхнего уровня)
    ↓ создаёт CTS или берёт GetCancellationTokenOnDestroy
    ↓ передаёт token в каждый вызов
        ↓ метод A получает ct, передаёт дальше
            ↓ метод B получает ct, передаёт дальше
                ↓ UniTask.Delay(..., ct) — конечный потребитель
```



```csharp
// ✅ Правило соблюдено — ct проходит через всю цепочку
public class ServiceLayer
{
    public async UniTask<Data> LoadAsync(CancellationToken ct)   // получает снаружи
    {
        var raw = await FetchAsync(ct);                          // передаёт дальше
        return await ParseAsync(raw, ct);                        // передаёт дальше
    }

    private async UniTask<string> FetchAsync(CancellationToken ct)
    {
        await UniTask.Delay(500, cancellationToken: ct);         // использует
        return "raw data";
    }

    private async UniTask<Data> ParseAsync(string raw, CancellationToken ct)
    {
        await UniTask.Yield(ct);                                 // использует
        return new Data();
    }
}
```

---

## Параллелизм

### UniTask.WhenAll — ждём все



```csharp
public class WhenAllExamples : MonoBehaviour
{
    private async UniTask LoadGameDataAsync(CancellationToken ct)
    {
        // Последовательно: 500 + 800 + 300 = 1600мс
        var player   = await LoadPlayerAsync(ct);
        var world    = await LoadWorldAsync(ct);
        var settings = await LoadSettingsAsync(ct);

        // Параллельно: max(500, 800, 300) = 800мс — в 2 раза быстрее!
        var (player2, world2, settings2) = await UniTask.WhenAll(
            LoadPlayerAsync(ct),
            LoadWorldAsync(ct),
            LoadSettingsAsync(ct)
        );
    }

    // WhenAll с коллекцией
    private async UniTask LoadAssetsAsync(string[] paths, CancellationToken ct)
    {
        var tasks  = paths.Select(p => LoadAssetAsync(p, ct));
        var assets = await UniTask.WhenAll(tasks);
        // assets — массив результатов в том же порядке что paths
    }

    private async UniTask<string> LoadPlayerAsync(CancellationToken ct)
    { await UniTask.Delay(500, cancellationToken: ct); return "player"; }

    private async UniTask<string> LoadWorldAsync(CancellationToken ct)
    { await UniTask.Delay(800, cancellationToken: ct); return "world"; }

    private async UniTask<string> LoadSettingsAsync(CancellationToken ct)
    { await UniTask.Delay(300, cancellationToken: ct); return "settings"; }

    private async UniTask<string> LoadAssetAsync(string path, CancellationToken ct)
    { await UniTask.Delay(200, cancellationToken: ct); return path; }
}
```

### UniTask.WhenAny — побеждает первый



```csharp
public class WhenAnyExamples : MonoBehaviour
{
    private async UniTask DemonstrateWhenAny(CancellationToken ct)
    {
        // Индекс первой завершившейся задачи
        int winner = await UniTask.WhenAny(
            UniTask.Delay(1000, cancellationToken: ct),
            UniTask.Delay(500,  cancellationToken: ct),   // победит эта
            UniTask.Delay(2000, cancellationToken: ct)
        );
        Debug.Log($"Победила задача {winner}"); // "1"

        // С результатами — возвращает (winnerIndex, result)
        var (index, data) = await UniTask.WhenAny(
            LoadFromCacheAsync(ct),     // быстро, часто побеждает
            LoadFromNetworkAsync(ct)    // медленно, запасной вариант
        );
        Debug.Log($"Источник {index}: {data}");
    }

    // Паттерн: гонка с таймаутом
    private async UniTask<string> LoadWithTimeoutAsync(CancellationToken ct)
    {
        int winner = await UniTask.WhenAny(
            LoadFromNetworkAsync(ct),
            UniTask.Delay(5000, cancellationToken: ct)
        );

        if (winner == 1) throw new TimeoutException("Загрузка превысила 5 секунд");
        return "loaded data";
    }

    // Паттерн: ожидание любого пользовательского ввода
    private async UniTask WaitForAnyInput(CancellationToken ct)
    {
        await UniTask.WhenAny(
            UniTask.WaitUntil(() => Input.GetKeyDown(KeyCode.Space),    ct),
            UniTask.WaitUntil(() => Input.GetMouseButtonDown(0),        ct),
            UniTask.Delay(TimeSpan.FromSeconds(10), cancellationToken:  ct)
        );
        Debug.Log("Получен ввод или истёк таймаут");
    }

    private async UniTask<string> LoadFromCacheAsync(CancellationToken ct)
    { await UniTask.Delay(100, cancellationToken: ct); return "cache"; }

    private async UniTask<string> LoadFromNetworkAsync(CancellationToken ct)
    { await UniTask.Delay(800, cancellationToken: ct); return "network"; }
}
```

---

## UniTaskCompletionSource

`UniTaskCompletionSource` — мост между событийной моделью и async/await. Позволяет создать `UniTask`, завершение которой вы контролируете вручную.



```csharp
// Классический случай: UI диалог — ждём решения пользователя
public class ConfirmDialog : MonoBehaviour
{
    private UniTaskCompletionSource<bool> _tcs;

    // Возвращает true (OK) или false (Cancel)
    public UniTask<bool> ShowAsync(string message)
    {
        gameObject.SetActive(true);
        // TODO: установить текст сообщения

        _tcs = new UniTaskCompletionSource<bool>();
        return _tcs.Task;
        // метод завершается СРАЗУ, возвращая ещё не готовую задачу
        // ждущий код заблокируется здесь до TrySetResult
    }

    // Вызывается кнопкой "OK" в инспекторе
    public void OnOkClicked()
    {
        gameObject.SetActive(false);
        _tcs?.TrySetResult(true);
    }

    // Вызывается кнопкой "Cancel" в инспекторе
    public void OnCancelClicked()
    {
        gameObject.SetActive(false);
        _tcs?.TrySetResult(false);
    }
}

// Использование — линейный читаемый код
public class GameFlow : MonoBehaviour
{
    [SerializeField] private ConfirmDialog _dialog;

    private async UniTaskVoid OnQuitPressed()
    {
        bool confirmed = await _dialog.ShowAsync("Выйти из игры?");
        if (confirmed) Application.Quit();
    }
}
```



```csharp
// Другой случай: оборачиваем событие в async
public static class Evenensions
{
    // Ждём следующего вызова UnityEvent
    public static UniTask WaitForEvent(UnityEngine.Events.UnityEvent unityEvent,
                                       CancellationToken ct = default)
    {
        var tcs = new UniTaskCompletionSource();

        // Одноразовый обработчик
        void Handler()
        {
            unityEvent.RemoveListener(Handler);
            tcs.TrySetResult();
        }

        unityEvent.AddListener(Handler);

        // При отмене — отписываемся и бросаем отмену
        ct.Register(() =>
        {
            unityEvent.RemoveListener(Handler);
            tcs.TrySetCanceled();
        });

        return tcs.Task;
    }
}
```

---

## Загрузка сцен и ассетов

### Загрузка сцены с прогрессом и переходом



```csharp
using Cysharp.Threading.Tasks;
using UnityEngine;
using UnityEngine.SceneManagement;

public class SceneLoader : MonoBehaviour
{
    [SerializeField] private CanvasGroup _fadeOverlay;

    public async UniTask LoadSceneAsync(
        string sceneName,
        IProgress<float> progress = null,
        CancellationToken ct = default)
    {
        // Затемнение
        await FadeAsync(_fadeOverlay, 0f, 1f, 0.4f, ct);

        // Начинаем загрузку, но не активируем сразу
        var op = SceneManager.LoadSceneAsync(sceneName);
        op.allowSceneActivation = false;

        // Ждём загрузки до 90% (Unity останавливается здесь)
        while (op.progress < 0.9f)
        {
            ct.ThrowIfCancellationRequested();
            progress?.Report(op.progress / 0.9f);
            await UniTask.Yield(ct);
        }

        progress?.Report(1f);

        // Активируем — Unity перейдёт на новую сцену
        op.allowSceneActivation = true;
        await op.ToUniTask(cancellationToken: ct);

        // Появление
        await FadeAsync(_fadeOverlay, 1f, 0f, 0.4f, ct);
    }

    // Аддитивная загрузка — не выгружает текущую сцену
    public async UniTask<Scene> LoadAdditiveAsync(string sceneName, CancellationToken ct)
    {
        await SceneManager.LoadSceneAsync(sceneName, LoadSceneMode.Additive)
                          .ToUniTask(cancellationToken: ct);
        return SceneManager.GetSceneByName(sceneName);
    }

    private async UniTask FadeAsync(CanvasGroup cg, float from, float to,
                                    float dur, CancellationToken ct)
    {
        float t = 0f;
        cg.alpha = from;
        while (t < dur)
        {
            await UniTask.Yield(PlayerLoopTiming.Update, ct);
            t += Time.deltaTime;
            cg.alpha = Mathf.Lerp(from, to, Mathf.Clamp01(t / dur));
        }
        cg.alpha = to;
    }
}
```

### Параллельная загрузка ассетов



```csharp
using Cysharp.Threading.Tasks;
using System.Linq;
using UnityEngine;

public class AssetLoader : MonoBehaviour
{
    // Загрузка нескольких ассетов параллельно с суммарным прогрессом
    public async UniTask<Object[]> LoadAssetsAsync(
        string[] paths,
        IProgress<float> totalProgress = null,
        CancellationToken ct = default)
    {
        if (paths.Length == 0) return System.Array.Empty<Object>();

        // Прогресс каждого ассета
        float[] progresses = new float[paths.Length];

        void UpdateTotal()
        {
            float sum = 0f;
            foreach (var p in progresses) sum += p;
            totalProgress?.Report(sum / progresses.Length);
        }

        // Задача загрузки одного ассета
        async UniTask<Object> LoadOne(string path, int index)
        {
            var op = Resources.LoadAsync(path);
            while (!op.isDone)
            {
                ct.ThrowIfCancellationRequested();
                progresses[index] = op.progress;
                UpdateTotal();
                await UniTask.Yield(ct);
            }
            progresses[index] = 1f;
            UpdateTotal();

            if (op.asset == null)
                throw new System.Exception($"Ассет не найден: '{path}'");
            return op.asset;
        }

        // Все параллельно
        var tasks = paths.Select((path, i) => LoadOne(path, i));
        return await UniTask.WhenAll(tasks);
    }
}
```

### UnityWebRequest + UniTask



```csharp
using Cysharp.Threading.Tasks;
using UnityEngine;
using UnityEngine.Networking;

public class ApiClient
{
    public async UniTask<string> GetAsync(string url, CancellationToken ct = default)
    {
        using var req = UnityWebRequest.Get(url);
        await req.SendWebRequest().WithCancellation(ct);

        if (req.result != UnityWebRequest.Result.Success)
            throw new System.Exception($"HTTP {req.responseCode}: {req.error}");

        return req.downloadHandler.;
    }

    public async UniTask<ure2D> GetureAsync(
        string url,
        IProgress<float> progress = null,
        CancellationToken ct = default)
    {
        using var req = UnityWebRequesture.Geture(url);
        await req.SendWebRequest().ToUniTask(progress: progress, cancellationToken: ct);

        if (req.result != UnityWebRequest.Result.Success)
            throw new System.Exception($"Ошибка загрузки текстуры: {req.error}");

        return DownloadHandlerure.GetContent(req);
    }
}
```

---

## Сравнительная таблица

|Критерий|Coroutine|Task (.NET)|UniTask|
|---|---|---|---|
|**Тип**|`IEnumerator` (итератор)|`class` (ссылочный тип)|`struct` (значимый тип)|
|**Аллокации**|На каждый `new Wait*`|На каждый `new Task`|Zero (горячий путь)|
|**Возвращаемое значение**|❌ Нет, только поля|✅ `Task<T>`|✅ `UniTask<T>`|
|**Обработка исключений**|❌ Невозможна снаружи|✅ `try/catch`|✅ `try/catch`|
|**CancellationToken**|❌ Ручной флаг|✅ Стандартный|✅ + `GetCancellationTokenOnDestroy`|
|**Поток выполнения**|Главный поток|ThreadPool (риск)|Главный поток (по умолчанию)|
|**`Time.timeScale`**|✅ `WaitForSeconds` учитывает|❌ Игнорирует|✅ `DelayType.DeltaTime`|
|**Интеграция PlayerLoop**|✅ Встроена|❌ Нет|✅ Любая фаза|
|**Параллелизм**|🔶 Костыли|✅ `WhenAll/WhenAny`|✅ `WhenAll/WhenAny`|
|**Без MonoBehaviour**|❌ Невозможно|✅ Да|✅ Да|
|**Производительность**|Средняя|Хуже (GC)|Лучшая|
|**Читаемость кода**|❌ Низкая|✅ Высокая|✅ Высокая|
|**Отмена при Destroy**|🔶 Автоматически, грубо|❌ Ручная|✅ `GetCancellationTokenOnDestroy`|
|**Отладка**|Unity Profiler|VS Debugger|UniTask Tracker + Profiler|
|**Зависимость**|Встроена|.NET Runtime|Пакет UniTask|
|**Кривая обучения**|Низкая|Средняя|Средняя|

---

## Практика

### Задача 1 (Базовый): переписать корутину на UniTask

**Задание:** переписать следующую корутину на UniTask. При уничтожении объекта анимация должна корректно завершаться.



```csharp
// Дано — переписать
public class NotificationBanner : MonoBehaviour
{
    [SerializeField] private CanvasGroup _group;
    [SerializeField] private float _showDuration = 3f;

    public void Show()
    {
        StartCoroutine(ShowCoroutine());
    }

    private IEnumerator ShowCoroutine()
    {
        // fade in
        float t = 0f;
        while (t < 0.3f)
        { t += Time.deltaTime; _group.alpha = t / 0.3f; yield return null; }
        _group.alpha = 1f;

        yield return new WaitForSeconds(_showDuration);

        // fade out
        t = 0f;
        while (t < 0.3f)
        { t += Time.deltaTime; _group.alpha = 1f - t / 0.3f; yield return null; }
        _group.alpha = 0f;

        gameObject.SetActive(false); // опасно если объект уничтожен
    }
}
```

**Решение:**



```csharp
public class NotificationBanner_Solution : MonoBehaviour
{
    [SerializeField] private CanvasGroup _group;
    [SerializeField] private float _showDuration = 3f;

    private CancellationTokenSource _cts;

    public void Show()
    {
        _cts?.Cancel();
        _cts?.Dispose();

        // Связываем с уничтожением объекта
        _cts = CancellationTokenSource.CreateLinkedTokenSource(
            this.GetCancellationTokenOnDestroy()
        );

        ShowAsync(_cts.Token).Forget(ex =>
        {
            if (ex is not OperationCanceledException)
                Debug.LogException(ex);
        });
    }

    private async UniTask ShowAsync(CancellationToken ct)
    {
        try
        {
            await FadeAsync(0f, 1f, 0.3f, ct);
            await UniTask.Delay(TimeSpan.FromSeconds(_showDuration),
                                DelayType.DeltaTime, cancellationToken: ct);
            await FadeAsync(1f, 0f, 0.3f, ct);

            // Безопасно — если объект уничтожен, ct сработает раньше
            gameObject.SetActive(false);
        }
        catch (OperationCanceledException)
        {
            // Сбрасываем состояние если объект жив
            if (this != null) _group.alpha = 0f;
        }
    }

    private async UniTask FadeAsync(float from, float to, float dur, CancellationToken ct)
    {
        float t = 0f;
        _group.alpha = from;
        while (t < dur)
        {
            await UniTask.Yield(PlayerLoopTiming.Update, ct); // ct в каждом Yield!
            t += Time.deltaTime;
            _group.alpha = Mathf.Lerp(from, to, Mathf.Clamp01(t / dur));
        }
        _group.alpha = to;
    }

    private void OnDestroy()
    {
        _cts?.Cancel();
        _cts?.Dispose();
    }
}
```

---

### Задача 2 (Средний): экран загрузки с параллельными операциями

**Задание:** реализовать систему загрузки уровня. Сцена и ассеты загружаются параллельно. Прогресс-бар отображает суммарный прогресс. Кнопка "Отмена" работает.



```csharp
// Дано — интерфейс и стартовая точка
public interface ILoadingView
{
    void SetProgress(float value);        // 0..1
    void SetStatus(string );
    void SetCancelVisible(bool visible);
}

public class LevelLoadingSystem : MonoBehaviour
{
    [SerializeField] private LoadingView _view; // реализует ILoadingView

    private CancellationTokenSource _cts;

    public void StartLoading(string sceneName, string[] assetPaths)
    {
        // TODO: реализовать
    }

    public void Cancel() => _cts?.Cancel();

    private void OnDestroy() { _cts?.Cancel(); _cts?.Dispose(); }
}
```

**Решение:**



```csharp
public class LevelLoadingSystem_Solution : MonoBehaviour
{
    [SerializeField] private LoadingView _view;

    private CancellationTokenSource _cts;
    private bool _isLoading;

    public void StartLoading(string sceneName, string[] assetPaths)
    {
        if (_isLoading) return;

        _cts?.Dispose();
        _cts = CancellationTokenSource.CreateLinkedTokenSource(
            this.GetCancellationTokenOnDestroy()
        );

        LoadAsync(sceneName, assetPaths, _cts.Token).Forget();
    }

    public void Cancel() => _cts?.Cancel();

    private async UniTaskVoid LoadAsync(string scene, string[] assets, CancellationToken ct)
    {
        _isLoading = true;
        _view.SetCancelVisible(true);
        _view.SetProgress(0f);
        _view.SetStatus("Загрузка...");

        try
        {
            // Прогресс каждой части — 50% сцена, 50% ассеты
            float sceneP = 0f, assetsP = 0f;
            void Update() => _view.SetProgress(sceneP * 0.5f + assetsP * 0.5f);

            var sceneOp = SceneManager.LoadSceneAsync(scene);
            sceneOp.allowSceneActivation = false;

            // Параллельно: сцена + ассеты
            await UniTask.WhenAll(
                TrackSceneAsync(sceneOp, p => { sceneP  = p; Update(); }, ct),
                LoadAssetsAsync(assets,  p => { assetsP = p; Update(); }, ct)
            );

            _view.SetStatus("Активация сцены...");
            sceneOp.allowSceneActivation = true;
            await sceneOp.ToUniTask(cancellationToken: ct);

            _view.SetProgress(1f);
            _view.SetStatus("Готово!");
            await UniTask.Delay(300, cancellationToken: ct);
        }
        catch (OperationCanceledException)
        {
            _view.SetStatus("Загрузка отменена");
            await UniTask.Delay(1000); // без ct — даём увидеть сообщение
            SceneManager.LoadScene("MainMenu");
        }
        catch (Exception ex)
        {
            Debug.LogException(ex);
            _view.SetStatus($"Ошибка: {ex.Message}");
            await UniTask.Delay(2000);
        }
        finally
        {
            _isLoading = false;
            _view.SetCancelVisible(false);
        }
    }

    private async UniTask TrackSceneAsync(AsyncOperation op,
                                          Action<float> onProgress,
                                          CancellationToken ct)
    {
        while (op.progress < 0.9f)
        {
            ct.ThrowIfCancellationRequested();
            onProgress(op.progress / 0.9f);
            await UniTask.Yield(ct);
        }
        onProgress(1f);
    }

    private async UniTask LoadAssetsAsync(string[] paths,
                                          Action<float> onProgress,
                                          CancellationToken ct)
    {
        if (paths.Length == 0) { onProgress(1f); return; }

        float[] progresses = new float[paths.Length];
        void UpdateTotal()
        {
            float s = 0; foreach (var p in progresses) s += p;
            onProgress(s / progresses.Length);
        }

        async UniTask LoadOne(string path, int index)
        {
            var op = Resources.LoadAsync(path);
            while (!op.isDone)
            {
                ct.ThrowIfCancellationRequested();
                progresses[index] = op.progress;
                UpdateTotal();
                await UniTask.Yield(ct);
            }
            progresses[index] = 1f;
            UpdateTotal();
            if (op.asset == null) throw new Exception($"Не найден: {path}");
        }

        await UniTask.WhenAll(paths.Select((p, i) => LoadOne(p, i)));
    }

    private void OnDestroy() { _cts?.Cancel(); _cts?.Dispose(); }
}
```

---

### Задача 3 (Продвинутый): последовательность финального босса

**Задание:** реализовать трёхфазную боевую последовательность. Фаза 1: ждём гибели всех миньонов (WhenAll + события). Катсцена: параллельные эффекты. Фаза 2: цикл атак. Всё отменяется при гибели игрока.



```csharp
// Интерфейсы — даны
public interface IMinion  { bool IsDead { get; } event Action OnDeath; }
public interface IBoss    { void SetPhase(int p); void Attack(string name); }
public interface IPlayer  { bool IsDead { get; } event Action OnDeath; }
```

**Решение:**



```csharp
public class BossSequence_Solution : MonoBehaviour
{
    [SerializeField] private MinionController[] _minions;
    [SerializeField] private BossController     _boss;
    [SerializeField] private PlayerController   _player;

    private CancellationTokenSource _cts;

    private void Start()
    {
        var destroyCt = this.GetCancellationTokenOnDestroy();
        _cts = CancellationTokenSource.CreateLinkedTokenSource(destroyCt);

        // Смерть игрока отменяет всю последовательность
        _player.OnDeath += () => _cts?.Cancel();

        RunSequenceAsync(_cts.Token).Forget(ex =>
        {
            if (ex is not OperationCanceledException) Debug.LogException(ex);
            else Debug.Log("[Босс] Последовательность прервана");
        });
    }

    // ── Главная последовательность ────────────────────────────────────────
    private async UniTask RunSequenceAsync(CancellationToken ct)
    {
        Debug.Log("[Босс] Фаза 1: ждём миньонов");
        await WaitForAllMinionsAsync(ct);

        Debug.Log("[Босс] Катсцена");
        await PlayCutsceneAsync(ct);

        Debug.Log("[Босс] Фаза 2: атаки");
        await RunAttackLoopAsync(ct);
    }

    // ── Фаза 1 ───────────────────────────────────────────────────────────
    private UniTask WaitForAllMinionsAsync(CancellationToken ct) =>
        UniTask.WhenAll(_minions.Select(m => WaitForOneMinionAsync(m, ct)));

    private UniTask WaitForOneMinionAsync(IMinion minion, CancellationToken ct)
    {
        if (minion.IsDead) return UniTask.CompletedTask;

        var tcs = new UniTaskCompletionSource();

        void OnDeath()
        {
            minion.OnDeath -= OnDeath;   // отписываемся сразу
            tcs.TrySetResult();
        }

        minion.OnDeath += OnDeath;

        ct.Register(() =>
        {
            minion.OnDeath -= OnDeath;   // отписываемся при отмене
            tcs.TrySetCanceled();
        });

        return tcs.Task;
    }

    // ── Катсцена ─────────────────────────────────────────────────────────
    private async UniTask PlayCutsceneAsync(CancellationToken ct)
    {
        // Параллельные эффекты появления
        await UniTask.WhenAll(
            AnimateCameraFocusAsync(ct),      // камера на босса
            PlayBossAppearAnimAsync(ct),      // анимация bosса
            FadeMusicAsync(ct)               // смена музыки
        );

        // Диалог — последовательно после эффектов
        Debug.Log("[Катсцена] Финальный диалог...");
        await UniTask.Delay(TimeSpan.FromSeconds(3f), cancellationToken: ct);

        Debug.Log("[Катсцена] Завершена");
    }

    private async UniTask AnimateCameraFocusAsync(CancellationToken ct)
    {
        Debug.Log("[Катсцена] Камера → босс");
        await UniTask.Delay(TimeSpan.FromSeconds(2f), cancellationToken: ct);
    }

    private async UniTask PlayBossAppearAnimAsync(CancellationToken ct)
    {
        Debug.Log("[Катсцена] Анимация появления");
        _boss.Attack("Appear");
        await UniTask.Delay(TimeSpan.FromSeconds(2.5f), cancellationToken: ct);
    }

    private async UniTask FadeMusicAsync(CancellationToken ct)
    {
        Debug.Log("[Катсцена] Переход музыки");
        await UniTask.Delay(TimeSpan.FromSeconds(1.5f), cancellationToken: ct);
    }

    // ── Фаза 2 ───────────────────────────────────────────────────────────
    private async UniTask RunAttackLoopAsync(CancellationToken ct)
    {
        _boss.SetPhase(2);
        int count = 0;

        // Делегаты паттернов — легко расширять
        UniTask[] patterns(CancellationToken t) => new[]
        {
            AttackPattern1Async(t),
            AttackPattern2Async(t),
            AttackPattern3Async(t),
        };

        while (!ct.IsCancellationRequested)
        {
            await patterns(ct)[count % 3];
            count++;

            // Интервал сокращается каждые 5 атак
            float interval = Mathf.Max(0.4f, 1.2f - count * 0.08f);
            await UniTask.Delay(TimeSpan.FromSeconds(interval), cancellationToken: ct);
        }
    }

    private async UniTask AttackPattern1Async(CancellationToken ct)
    {
        Debug.Log("[Атака 1] Быстрый удар");
        _boss.Attack("Attack1");
        await UniTask.Delay(TimeSpan.FromSeconds(0.8f), cancellationToken: ct);
    }

    private async UniTask AttackPattern2Async(CancellationToken ct)
    {
        Debug.Log("[Атака 2] Замах + мощный удар");
        _boss.Attack("ChargeUp");
        await UniTask.Delay(TimeSpan.FromSeconds(1.2f), cancellationToken: ct);
        _boss.Attack("HeavyAttack");
        await UniTask.Delay(TimeSpan.FromSeconds(0.8f), cancellationToken: ct);
    }

    private async UniTask AttackPattern3Async(CancellationToken ct)
    {
        Debug.Log("[Атака 3] Серия ударов");
        for (int i = 0; i < 3; i++)
        {
            ct.ThrowIfCancellationRequested();
            _boss.Attack($"Combo{i + 1}");
            await UniTask.Delay(TimeSpan.FromSeconds(0.35f), cancellationToken: ct);
        }
    }

    private void OnDestroy()
    {
        if (_player != null) _player.OnDeath -= () => _cts?.Cancel();
        _cts?.Cancel();
        _cts?.Dispose();
    }
}
```

---

## Частые ошибки

### Ошибка 1: `CancellationToken` не передан — отмена не работает



```csharp
// ❌ Токен создан, но в Delay не передан
private async UniTask RunAsync(CancellationToken ct)
{
    await UniTask.Delay(5000); // объект уничтожен — код продолжит работу!
    transform.position = Vector3.zero; // MissingReferenceException
}

// ✅ Токен передаётся в каждый Delay и Yield
private async UniTask RunAsync(CancellationToken ct)
{
    await UniTask.Delay(5000, cancellationToken: ct); // остановится при отмене
    if (this != null) transform.position = Vector3.zero;
}
```

---

### Ошибка 2: `UniTaskVoid` вместо `UniTask` для awaitable метода



```csharp
// ❌ UniTaskVoid нельзя await-ить — следующий код выполнится сразу
private async UniTaskVoid LoadDataAsync() { await UniTask.Delay(1000); }

private async UniTask Start()
{
    await LoadDataAsync(); // ошибка компиляции или неожиданное поведение
}

// ✅ UniTask для методов, которые нужно await-ить
private async UniTask LoadDataAsync() { await UniTask.Delay(1000); }

private async UniTask Start()
{
    await LoadDataAsync(); // ждём завершения
}

// UniTaskVoid — только для fire-and-forget с обработкой ошибок внутри
private async UniTaskVoid FireAndForgetSafely()
{
    try { await LoadDataAsync(); }
    catch (OperationCanceledException) { }
    catch (Exception ex) { Debug.LogException(ex); }
}
```

---

### Ошибка 3: забыть `Dispose` для `CancellationTokenSource`



```csharp
// ❌ Cancel без Dispose — утечка памяти
public void StopOperation()
{
    _cts?.Cancel(); // останавливает операцию
                    // но ресурсы CTS НЕ освобождены!
}

// ✅ Cancel + Dispose в правильном порядке
public void StopOperation()
{
    _cts?.Cancel();
    _cts?.Dispose();
    _cts = null;
}

// ✅ Или using для автоматического Dispose
using var cts = new CancellationTokenSource();
await RunAsync(cts.Token);
// cts.Dispose() вызовется автоматически
```

---

### Ошибка 4: обращение к Unity API после уничтожения объекта



```csharp
// ❌ Объект может быть уничтожен во время await
private async UniTask ShowResultAsync(CancellationToken ct)
{
    await UniTask.Delay(2000, cancellationToken: ct);
    // Если ct не сработал по какой-то причине:
    _label. = "Готово!"; // MissingReferenceException если объект уничтожен
}

// ✅ Проверка через this != null (работает благодаря operator== в Unity)
private async UniTask ShowResultAsync(CancellationToken ct)
{
    await UniTask.Delay(2000, cancellationToken: ct);
    if (this == null) return; // объект уничтожен — выходим
    _label. = "Готово!";
}

// ✅ Лучше: GetCancellationTokenOnDestroy гарантирует отмену при уничтожении
private async UniTask ShowResultAsync()
{
    var ct = this.GetCancellationTokenOnDestroy();
    await UniTask.Delay(2000, cancellationToken: ct);
    _label. = "Готово!"; // сюда не дойдём если объект уничтожен
}
```

---

### Ошибка 5: не связать `CancellationTokenSource` с `GetCancellationTokenOnDestroy`



```csharp
// ❌ Ручной CTS без связи с Destroy — утечка при уничтожении объекта
private void Start()
{
    _cts = new CancellationTokenSource();
    RunAsync(_cts.Token).Forget(); // продолжит работать даже после Destroy!
}

// ✅ Связываем через CreateLinkedTokenSource
private void Start()
{
    var destroyCt = this.GetCancellationTokenOnDestroy();
    _cts = CancellationTokenSource.CreateLinkedTokenSource(destroyCt);
    RunAsync(_cts.Token).Forget();
    // теперь: отменяется при Cancel() ИЛИ при Destroy
}
```

---

### Ошибка 6: последовательный вместо параллельного WhenAll



```csharp
// ❌ Это последовательно, не параллельно!
// Задачи создаются только когда предыдущая await завершилась
var a = await LoadAAsync(ct);  // ждём A
var b = await LoadBAsync(ct);  // только потом B — 1600мс суммарно

// ❌ Это тоже последовательно — WhenAll получает уже завершённые задачи
var taskA = await LoadAAsync(ct); // ждём A сразу
var taskB = await LoadBAsync(ct); // ждём B сразу
await UniTask.WhenAll(taskA, taskB); // обе уже готовы

// ✅ Сначала создаём задачи (запускаем), потом ждём все вместе — параллельно
var taskA = LoadAAsync(ct);     // ЗАПУСКАЕМ без await
var taskB = LoadBAsync(ct);     // ЗАПУСКАЕМ без await
var (a, b) = await UniTask.WhenAll(taskA, taskB); // ждём обе — 800мс
```

---

### Ошибка 7: `OperationCanceledException` не обработан в `UniTaskVoid`



```csharp
// ❌ Необработанное исключение идёт в глобальный обработчик — шумно
private async UniTaskVoid RunAsync(CancellationToken ct)
{
    await UniTask.Delay(5000, cancellationToken: ct);
    // При отмене: необработанный OperationCanceledException в консоль
}

// ✅ Обрабатываем отмену явно
private async UniTaskVoid RunAsync(CancellationToken ct)
{
    try
    {
        await UniTask.Delay(5000, cancellationToken: ct);
    }
    catch (OperationCanceledException) { /* штатно, молчим */ }
    catch (Exception ex) { Debug.LogException(ex); }
}

// ✅ Или через Forget с обработчиком
SomeMethodAsync(ct).Forget(ex =>
{
    if (ex is not OperationCanceledException) Debug.LogException(ex);
});
```

---

### Ошибка 8: утечка подписки на событие в `UniTaskCompletionSource`



```csharp
// ❌ При отмене токена обработчик не отписывается — утечка памяти
private UniTask WaitForDeathAsync(IMinion minion, CancellationToken ct)
{
    var tcs = new UniTaskCompletionSource();
    minion.OnDeath += () => tcs.TrySetResult(); // никогда не отпишется!
    ct.Register(() => tcs.TrySetCanceled());    // только отмена TCS
    return tcs.Task;
}

// ✅ Явная отписка в обоих сценариях
private UniTask WaitForDeathAsync(IMinion minion, CancellationToken ct)
{
    var tcs = new UniTaskCompletionSource();

    void Handler()
    {
        minion.OnDeath -= Handler; // отписка при срабатывании
        tcs.TrySetResult();
    }

    minion.OnDeath += Handler;

    ct.Register(() =>
    {
        minion.OnDeath -= Handler; // отписка при отмене
        tcs.TrySetCanceled();
    });

    return tcs.Task;
}
```

---

### Ошибка 9: `allowSceneActivation` не выставлен в `false`



```csharp
// ❌ Сцена активируется сразу — ассеты ещё не загружены
var sceneOp = SceneManager.LoadSceneAsync("Level1");
// allowSceneActivation по умолчанию = true!
await LoadAssetsAsync(ct); // уже поздно — сцена активировалась
sceneOp.allowSceneActivation = true; // бессмысленно

// ✅ Отключаем сразу после создания
var sceneOp = SceneManager.LoadSceneAsync("Level1");
sceneOp.allowSceneActivation = false; // немедленно!
await UniTask.WhenAll(TrackSceneAsync(sceneOp, ct), LoadAssetsAsync(ct));
sceneOp.allowSceneActivation = true; // теперь всё готово
```

---

### Ошибка 10: `Task.Delay` вместо `UniTask.Delay` в Unity-коде



```csharp
// ❌ Task.Delay — системный таймер, не Unity
private async UniTask Update()
{
    await Task.Delay(1000); // игнорирует timeScale, может выполниться не в главном потоке
    transform.Rotate(Vector3.up, 45f); // риск UnityException
}

// ✅ UniTask.Delay — интегрирован с Unity
private async UniTask Update()
{
    await UniTask.Delay(1000, DelayType.DeltaTime, cancellationToken: ct);
    transform.Rotate(Vector3.up, 45f); // всегда в главном потоке
}
```

---

## Чеклист

### Перед написанием async метода



```csharp
□ Определён правильный возвращаемый тип?
  □ UniTask       — если нужно await-ить снаружи
  □ UniTask<T>    — если нужно await-ить и получить значение
  □ UniTaskVoid   — ТОЛЬКО fire-and-forget, нельзя await-ить

□ Метод принимает CancellationToken?
  □ Да, последним параметром с default значением
  □ Токен передаётся во ВСЕ внутренние вызовы UniTask.Delay/Yield/etc
```

### Управление CancellationToken



```csharp
□ Источник токена определён правильно?
  □ this.GetCancellationTokenOnDestroy()  — для MonoBehaviour без ручного CTS
  □ new CancellationTokenSource()         — для ручного управления
  □ CreateLinkedTokenSource(a, b, c)      — для объединения условий отмены

□ CancellationTokenSource корректно освобождается?
  □ _cts?.Cancel() вызван перед Dispose
  □ _cts?.Dispose() вызван в OnDestroy или finally
  □ Используется using var для временных CTS

□ Отмена обрабатывается корректно?
  □ try/catch(OperationCanceledException) на верхнем уровне
  □ Состояние UI/объектов сбрасывается в catch
  □ throw или return — не проглатываем молча в середине цепочки
```

### Параллелизм



```csharp
□ Используется WhenAll правильно?
  □ Задачи СОЗДАНЫ (запущены) до await UniTask.WhenAll
  □ Не await-им каждую задачу отдельно перед WhenAll

□ Прогресс агрегирован?
  □ Каждая параллельная задача обновляет свою долю прогресса
  □ Суммарный прогресс = взвешенная сумма долей
```

### Загрузка ресурсов



```csharp
□ Сцена загружается правильно?
  □ allowSceneActivation = false сразу после LoadSceneAsync
  □ Активация только после завершения всех зависимых операций
  □ ToUniTask() используется вместо ручного цикла где возможно

□ Ассеты проверяются после загрузки?
  □ op.asset != null — иначе бросаем исключение с понятным сообщением
  □ Ресурсы освобождаются при ошибке (Addressables.Release)
```

### Исключения и безопасность



```csharp
□ Код после await безопасен при уничтожении объекта?
  □ GetCancellationTokenOnDestroy гарантирует отмену
  □ Или явная проверка: if (this == null) return;

□ UniTaskVoid методы обёрнуты в try/catch?
  □ OperationCanceledException обработан отдельно
  □ Остальные исключения — Debug.LogException

□ Forget() используется с обработчиком ошибок?
  □ .Forget(ex => { if (ex is not OperationCanceledException) Debug.LogException(ex); })

□ UniTaskCompletionSource не создаёт утечки?
  □ Обработчик событий отписывается при TrySetResult
  □ Обработчик событий отписывается при отмене через ct.Register
```

### Производительность



```csharp
□ Нет лишних аллокаций?
  □ UniTask используется вместо Task в Unity-коде
  □ WaitForSeconds не создаётся в цикле (используйте UniTask.Delay)

□ Правильная фаза PlayerLoop?
  □ Физическая логика → PlayerLoopTiming.FixedUpdate
  □ Работа с рендером → PlayerLoopTiming.PostLateUpdate
  □ Общая логика → PlayerLoopTiming.Update (по умолчанию)
```

### Отладка



```csharp
□ UniTask Tracker настроен?
  □ Window → UniTask Tracker открыт во время тестирования
  □ EnableTracking = true в Development Build
  □ Нет "зависших" Pending задач после завершения операции

□ Глобальный обработчик настроен?
  □ UniTaskScheduler.UnobservedTaskException подписан
  □ OperationCanceledException в нём фильтруется
```

---

## Ресурсы

### Официальные источники



```csharp
GitHub репозиторий (исходный код, документация, changelog):
https://github.com/Cysharp/UniTask

NuGet / OpenUPM пакет:
https://openupm.com/packages/com.cysharp.unitask/

Автор — Yoshifumi Kawai (neuecc):
https://twitter.com/neuecc
```

### Документация и статьи



```csharp
README с полным API:
https://github.com/Cysharp/UniTask#readme

Оригинальная статья автора (анонс UniTask v2):
https://neue.cc/2020/10/28.html

Microsoft: паттерны async/await в .NET (основа для понимания):
https://learn.microsoft.com/en-us/dotnet//asynchronous-programming/

ValueTask vs Task — когда что использовать:
https://devblogs.microsoft.com/dotnet/understanding-the-whys-whats-and-whens-of-valuetask/
```

### Смежные библиотеки



```csharp
R3 — Reactive Extensions для Unity (интегрируется с UniTask):
https://github.com/Cysharp/R3

VContainer — DI контейнер с поддержкой IAsyncStartable:
https://github.com/hadashiA/VContainer

MessagePipe — pub/sub система с UniTask-интеграцией:
https://github.com/Cysharp/MessagePipe
```

### Инструменты отладки



```csharp
UniTask Tracker: Window → UniTask Tracker
  — список активных задач в реальном времени
  — статус (Pending/Succeeded/Faulted/Canceled)
  — время выполнения и стек вызовов

Unity Profiler: Window → Analysis → Profiler
  — ProfilerMarker для измерения async-секций
  — CPU Usage: поиск GC Alloc в async методах
```

---

_UniTask превращает асинхронный код Unity из набора корутинных костылей в чистый, линейный, тестируемый C#. Один паттерн — `async UniTask`, `CancellationToken`, `WhenAll` — покрывает 90% сценариев. Остальное приходит с практикой_