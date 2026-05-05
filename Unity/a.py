import re
from pathlib import Path

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Удаляем все вхождения "text" и "csharp" (независимо от регистра)
    content = re.sub(r'text', '', content, flags=re.IGNORECASE)
    content = re.sub(r'csharp', '', content, flags=re.IGNORECASE)

    # 2. Удаляем ```text и ```csharp
    content = re.sub(r'```text', '', content, flags=re.IGNORECASE)
    content = re.sub(r'```csharp', '', content, flags=re.IGNORECASE)

    # 3. Заменяем только НЕЧЁТНЫЕ ``` на ```csharp
    count = 0
    def replace_odd(match):
        nonlocal count
        count += 1
        if count % 2 == 1:
            return '```csharp'
        return '```'

    content = re.sub(r'```', replace_odd, content)

    # Сохраняем файл
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Готово: {file_path.name}  ({count} вхождений ```)")


# ====================== ЗАПУСК ======================
directory = Path(".")   # текущая папка

print("🚀 Начинаю обработку всех .md файлов...\n")

for file_path in sorted(directory.glob("*.md")):
    print(f"Обрабатываю: {file_path.name}")
    process_file(file_path)

print("\n🎉 Обработка завершена!")