def single_root_words(root_word, *other_words):
    # Пустой список для подходящих слов
    same_words = []

    # Перебираем слова в other_words
    for word in other_words:
        # Условие: если root_word содержится в word или word содержится в root_word
        if root_word in word or word in root_word:
            same_words.append(word)  # Добавляем слово в список same_words

    return same_words  # Возвращаем список подходящих слов


# Примеры вызова функции
result_1 = single_root_words("книга", "книги", "журнал", "газета", "письмо")
print("Подходящие слова:", result_1)

result_2 = single_root_words("дом", "подъезд", "квартира", "комната", "дом")
print("Подходящие слова:", result_2)
