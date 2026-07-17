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
5. Удалить привычку
6. Очистить данные
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
        
def add_habit(data):
    title = input("введите название привычки:")
    if title in data:
        print("такая привычка уже добавлена")
    else:
        data[title] = [0] * 7
        save_habits(data)
        
def mark_habit(data):
    if not data:
        print("нет привычек")
        return
    
    habits = list(data.keys())
    print("\nСписок пирвычек:")
    for i, habit in enumerate(habits, start=1):
        print(f"{i}. {habit}")
        
    number = input("введите номер привычки: ")
    if not number.isdigit():
        print("Ошибка: нужно ввести число.")
        return
    number = int(number)
    if number <1 or number > len(habits):
        print("неверный номер привычки")
        return
    name = habits[number - 1]
    data[name][0] = 1
    print(f"привычка '{name}' отмечена")
    
def show_stats(data):
    if not data:
        print("нет привычек")
        return
    
    for habit, days in data.items():
        suma = sum(days)
        percent = round((suma/7) * 100)
        print(f"{habit}: {suma}/7 ({percent}%)")
        
        
def delete_habit(data):
    if not data:
        print("нет привычек для удаления")
        return
    habits = list(data.keys())
    print("\nсписок привычек")
    for i,habit in enumerate(habits, start=1):
        print(f"{i}. {habit}")
    number = input("введите номер привычки для удаления: ")
    if not number.isdigit():
        print("Ошибка: нужно ввести число")
        return
    number = int(number)
    if number < 1 or number > len(habits):
        print("неверный номер привычки")
        return
    name = habits[number - 1]
    del data [name]
    save_habits(data)
    print(f"привычка '{name}' удалена!")
    
def reset_all(data):
    if not data:
        print("нет привычек для удаления")
        return
    chistka = input("удалить все привычки? (да/нет)")
    if chistka == "да":
        data.clear()
        print("все данные успешно сброшены!")
        save_habits(data)
        return
    elif chistka == "нет":
        print("отмена")
        return
    else:
        print("неверный ввод")
        return

def main():
    data = load_habits()
    while True:
        print(MENU)
        vibor = input("выберите действие:")
        if vibor == "1":
            add_habit(data)
        elif vibor == "2":
            mark_habit(data)
        elif vibor == "3":
            show_stats(data)
        elif vibor == "4":
            save_habits(data)
            print("данные сохранены!")
            break
        elif vibor == 5:
            delete_habit(data)
        elif vibor == 6:
            reset_all(data)
        else:
            print("Неверный ввод")
            
            
if __name__ == "__main__":
    main()