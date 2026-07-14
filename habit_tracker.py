import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import json
import os

MENU = """
=== Дневник привычек ===
1. Добавить привычку
2. Отметить выполнение
3. Показать статистику
4. Выйти
"""

def load_habits():
    if os.path.exists("habits.json"):
        try:
            with open ("habits.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            print("Файл поврежден. Сохдайте новый!")
            return{}
    else:
        return{}

def save_habits(data):
    try:
        with open("habits.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except IOError:
        print("Ошибка при сохранении данных.")           
def main():
    data = load_habits()
    while True:
        print(MENU)
        vibor = input("выберите действие:")
        if vibor == "1":
            print("добавление привычки")
        elif vibor == "2":
            print("отметка выполнения")
        elif vibor == "3":
            print("Статистика")
        elif vibor == "4":
            save_habits(data)
            print("данные сохранены!")
            break
        else:
            print("Неверный ввод")
            
            
if __name__ == "__main__":
    main()