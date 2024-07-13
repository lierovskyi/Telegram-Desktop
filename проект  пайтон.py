animals_on_treatment = [    
    "Кілер",
    "Катран",
    "Крістіан",
    "Кербер",
    "Дарлінг",
    ]
healed_animals = []

def show_animals_on_treatment():
    if not animals_on_treatment:
        print("Список тварин на лікуванні порожній.")
    else:
        print("Список тварин на лікуванні:")
        for index, animal in enumerate(animals_on_treatment, start=1):
            print(f"{index}. {animal}")

def add_new_animal_to_treatment():
    animal_name = input("Введіть ім'я нової тварини: ")
    animals_on_treatment.append(animal_name)
    print(f"Тварина '{animal_name}' додана до списку на лікування.")

def heal_animal():
    if not animals_on_treatment:
        print("Список тварин на лікуванні порожній.")
        return
    
    show_animals_on_treatment()
    animal_index = int(input("Введіть номер тварини, яку вилікували: "))
    if 1 <= animal_index <= len(animals_on_treatment):
        healed_animal = animals_on_treatment.pop(animal_index - 1)
        healed_animals.append(healed_animal)
        print(f"Тварину '{healed_animal}' вилікувано.")
    else:
        print("Неправильний номер тварини.")

def show_healed_animals():
    if not healed_animals:
        print("Список вилікуваних тварин порожній.")
    else:
        print("Список вилікуваних тварин:")
        for index, animal in enumerate(healed_animals, start=1):
            print(f"{index}. {animal}")

def delete_animal_by_name():
    if not animals_on_treatment:
        print("Список тварин на лікуванні порожній.")
        return
    
    animal_name = input("Введіть ім'я тварини для видалення: ")
    if animal_name in animals_on_treatment:
        animals_on_treatment.remove(animal_name)
        print(f"Тварину '{animal_name}' видалено зі списку на лікування.")
    else:
        print(f"Тварина '{animal_name}' не знайдена у списку на лікування.")

def delete_animal_by_number():
    if not animals_on_treatment:
        print("Список тварин на лікуванні порожній.")
        return
    
    show_animals_on_treatment()
    animal_index = int(input("Введіть номер тварини для видалення: "))
    if 1 <= animal_index <= len(animals_on_treatment):
        deleted_animal = animals_on_treatment.pop(animal_index - 1)
        print(f"Тварину '{deleted_animal}' видалено зі списку на лікування.")
    else:
        print("Неправильний номер тварини.")

def sort_animals_by_name():
    animals_on_treatment.sort()
    print("Список тварин на лікуванні відсортовано за ім'ям.")

def change_animal_name():
    if not animals_on_treatment:
        print("Список тварин на лікуванні порожній.")
        return
    
    show_animals_on_treatment()
    animal_index = int(input("Введіть номер тварини для зміни імені: "))
    if 1 <= animal_index <= len(animals_on_treatment):
        new_name = input("Введіть нове ім'я для тварини: ")
        animals_on_treatment[animal_index - 1] = new_name
        print(f"Ім'я тварини змінено на '{new_name}'.")
    else:
        print("Неправильний номер тварини.")

def find_number_by_animal_name():
    animal_name = input("Введіть ім'я тварини для пошуку номера: ")
    if animal_name in animals_on_treatment:
        animal_index = animals_on_treatment.index(animal_name) + 1
        print(f"Номер тварини '{animal_name}': {animal_index}.")
    else:
        print(f"Тварина '{animal_name}' не знайдена у списку на лікування.")

# Основний код програми
while True:
    print("\nМеню команд:")
    print("1. Показати список тварин на лікуванні")
    print("2. Додати нову тварину до списку на лікування")
    print("3. Тварину вилікувано")
    print("4. Показати список вилікуваних тварин")
    print("5. Вийти з програми")
    print("6. Видалити помилково додану тварину за ім'ям")
    print("7. Видалити помилково додану тварину за номером")
    print("8. Відсортувати список тварин за ім'ям")
    print("9. Змінити ім'я тварини")
    print("10. Знайти номер тварини за ім'ям")

    choice = input("\nОберіть команду (1-10): ")

    if choice == '1':
        show_animals_on_treatment()
    elif choice == '2':
        add_new_animal_to_treatment()
    elif choice == '3':
        heal_animal()
    elif choice == '4':
        show_healed_animals()
    elif choice == '5':
        print("Програма завершена.")
        break
    elif choice == '6':
        delete_animal_by_name()
    elif choice == '7':
        delete_animal_by_number()
    elif choice == '8':
        sort_animals_by_name()
    elif choice == '9':
        change_animal_name()
    elif choice == '10':
        find_number_by_animal_name()
    else:
        print("Неправильний вибір команди. Введіть число від 1 до 10.")