from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

animals_on_treatment = ["Кілер", "Катран", "Крістіан", "Кербер", "Дарлінг"]
healed_animals = []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Показати список тварин на лікуванні", callback_data='show_animals')],
        [InlineKeyboardButton("Додати нову тварину", callback_data='add_animal')],
        [InlineKeyboardButton("Тварину вилікувано", callback_data='heal_animal')],
        [InlineKeyboardButton("Показати список вилікуваних тварин", callback_data='show_healed')],
        [InlineKeyboardButton("Видалити тварину за ім'ям", callback_data='delete_by_name')],
        [InlineKeyboardButton("Видалити тварину за номером", callback_data='delete_by_number')],
        [InlineKeyboardButton("Відсортувати список", callback_data='sort_animals')],
        [InlineKeyboardButton("Змінити ім'я тварини", callback_data='change_name')],
        [InlineKeyboardButton("Знайти номер тварини", callback_data='find_number')],
        [InlineKeyboardButton("Вийти", callback_data='exit')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Вітаю! Я бот для керування списком тварин на лікуванні.\n"
        "Оберіть дію за допомогою кнопок нижче.",
        reply_markup=reply_markup
    )

async def show_animals_on_treatment(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not animals_on_treatment:
        await update.callback_query.message.reply_text("Список тварин на лікуванні порожній.")
    else:
        response = "Список тварин на лікуванні:\n"
        for index, animal in enumerate(animals_on_treatment, start=1):
            response += f"{index}. {animal}\n"
        await update.callback_query.message.reply_text(response)

async def add_new_animal(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.callback_query.message.reply_text("Введіть ім'я нової тварини:")
    context.user_data['action'] = 'add_animal'

async def heal_animal(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not animals_on_treatment:
        await update.callback_query.message.reply_text("Список тварин на лікуванні порожній.")
    else:
        await show_animals_on_treatment(update, context)
        await update.callback_query.message.reply_text("Введіть номер тварини, яку вилікували:")
        context.user_data['action'] = 'heal_animal'

async def process_user_input(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    action = context.user_data.get('action')

    if action == 'add_animal':
        animal_name = update.message.text
        animals_on_treatment.append(animal_name)
        await update.message.reply_text(f"Тварина '{animal_name}' додана до списку на лікування.")
        context.user_data['action'] = None

    elif action == 'heal_animal':
        try:
            animal_index = int(update.message.text) - 1
            healed_animal = animals_on_treatment.pop(animal_index)
            healed_animals.append(healed_animal)
            await update.message.reply_text(f"Тварину '{healed_animal}' вилікувано.")
            context.user_data['action'] = None
        except (IndexError, ValueError):
            await update.message.reply_text("Неправильний номер тварини. Спробуйте ще раз.")
    
    elif action == 'delete_by_name':
        animal_name = update.message.text
        if animal_name in animals_on_treatment:
            animals_on_treatment.remove(animal_name)
            await update.message.reply_text(f"Тварину '{animal_name}' видалено зі списку на лікування.")
        else:
            await update.message.reply_text(f"Тварина '{animal_name}' не знайдена у списку на лікуванні.")
        context.user_data['action'] = None

    elif action == 'delete_by_number':
        try:
            animal_index = int(update.message.text) - 1
            deleted_animal = animals_on_treatment.pop(animal_index)
            await update.message.reply_text(f"Тварину '{deleted_animal}' видалено зі списку на лікування.")
        except (IndexError, ValueError):
            await update.message.reply_text("Неправильний номер тварини. Спробуйте ще раз.")
        context.user_data['action'] = None
    
    elif action == 'change_name':
        if 'change_name_index' not in context.user_data:
            try:
                animal_index = int(update.message.text) - 1
                if 0 <= animal_index < len(animals_on_treatment):
                    context.user_data['change_name_index'] = animal_index
                    await update.message.reply_text("Введіть нове ім'я для тварини:")
                else:
                    await update.message.reply_text("Неправильний номер тварини. Спробуйте ще раз.")
            except ValueError:
                await update.message.reply_text("Неправильний формат. Введіть число.")
        else:
            new_name = update.message.text
            animals_on_treatment[context.user_data['change_name_index']] = new_name
            await update.message.reply_text(f"Ім'я тварини змінено на '{new_name}'.")
            del context.user_data['change_name_index']
            context.user_data['action'] = None
    
    elif action == 'find_number':
        animal_name = update.message.text
        if animal_name in animals_on_treatment:
            animal_index = animals_on_treatment.index(animal_name) + 1
            await update.message.reply_text(f"Номер тварини '{animal_name}': {animal_index}.")
        else:
            await update.message.reply_text(f"Тварина '{animal_name}' не знайдена у списку на лікуванні.")
        context.user_data['action'] = None

async def show_healed_animals(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not healed_animals:
        await update.callback_query.message.reply_text("Список вилікуваних тварин порожній.")
    else:
        response = "Список вилікуваних тварин:\n"
        for index, animal in enumerate(healed_animals, start=1):
            response += f"{index}. {animal}\n"
        await update.callback_query.message.reply_text(response)

async def delete_animal_by_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.callback_query.message.reply_text("Введіть ім'я тварини для видалення:")
    context.user_data['action'] = 'delete_by_name'

async def delete_animal_by_number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not animals_on_treatment:
        await update.callback_query.message.reply_text("Список тварин на лікуванні порожній.")
    else:
        await show_animals_on_treatment(update, context)
        await update.callback_query.message.reply_text("Введіть номер тварини для видалення:")
        context.user_data['action'] = 'delete_by_number'

async def sort_animals_by_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    animals_on_treatment.sort()
    await update.callback_query.message.reply_text("Список тварин на лікуванні відсортовано за ім'ям.")

async def change_animal_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not animals_on_treatment:
        await update.callback_query.message.reply_text("Список тварин на лікуванні порожній.")
    else:
        await show_animals_on_treatment(update, context)
        await update.callback_query.message.reply_text("Введіть номер тварини, для якої бажаєте змінити ім'я:")
        context.user_data['action'] = 'change_name'

async def find_number_by_animal_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.callback_query.message.reply_text("Введіть ім'я тварини для пошуку номера:")
    context.user_data['action'] = 'find_number'

async def exit_bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.callback_query.message.reply_text("Бот завершив роботу. Дякуємо за використання!")
    await context.application.stop()

async def handle_button_click(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "show_animals":
        await show_animals_on_treatment(update, context)
    elif query.data == "add_animal":
        await add_new_animal(update, context)
    elif query.data == "heal_animal":
        await heal_animal(update, context)
    elif query.data == "show_healed":
        await show_healed_animals(update, context)
    elif query.data == "delete_by_name":
        await delete_animal_by_name(update, context)
    elif query.data == "delete_by_number":
        await delete_animal_by_number(update, context)
    elif query.data == "sort_animals":
        await sort_animals_by_name(update, context)
    elif query.data == "change_name":
        await change_animal_name(update, context)
    elif query.data == "find_number":
        await find_number_by_animal_name(update, context)
    elif query.data == "exit":
        await exit_bot(update, context)

def main():
    application = Application.builder().token("7355697413:AAFRnGA_cFAlmkIGJoK5VxzeORfKEuKBvjM").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_button_click))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_user_input))

    application.run_polling()

if __name__ == '__main__':
    main()