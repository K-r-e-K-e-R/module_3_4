def single_root_words(root_word, *other_words):
    # Пустой список для подходящих слов
    same_words = []
    # Привод корня к нижнему регистру
    lower_root_word = root_word.lower()

    # Перебираем слова в other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        lower_word = word.lower()
        # Условие: если корень присутствует в слове
        if lower_root_word in lower_word:
            same_words.append(word)  # Добавляем слово в список same_words


    return same_words  # Возвращаем список подходящих слов

# Примеры вызова функции
result_1 = single_root_words("свет", "Светильник", "проСВЕТ", "Осветленный", "Святотатсво")
print("Подходящие слова:", result_1)

result_2 = single_root_words("дом", "Домино", "ДОмоВОЙ", "ДомА", "дОмиКИ")
print("Подходящие слова:", result_2)
