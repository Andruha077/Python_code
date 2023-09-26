def swap_first_and_last_words(sentence):
    # Розбиваємо речення на слова
    words = sentence.split()

    # Перевіряємо, чи є в реченні хоча б два слова
    if len(words) >= 2:
        # Міняємо місцями перше та останнє слова
        words[0], words[-1] = words[-1], words[0]

        # Збираємо слова назад у речення
        swapped_sentence = ' '.join(words)

        # Виводимо отримане речення
        print("Речення з першим і останнім словами, зміненими місцями:")
        print(swapped_sentence)
    else:
        print("У реченні має бути хоча б два слова для обміну.")


# Зчитуємо введення користувача
sentence = input("Введіть речення: ")

# Викликаємо функцію для обміну першого та останнього слова
swap_first_and_last_words(sentence)
