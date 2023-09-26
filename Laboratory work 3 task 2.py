def find_longest_repeating_characters(word):
    longest_count = 0  # Початкова найбільша кількість повторюваних символів
    current_count = 1  # Початкова кількість повторюваних символів у поточному ряді
    longest_char = ""  # Початковий символ з найбільшою кількістю повторень

    # Перебираємо символи в слові, починаючи з другого символу
    for i in range(1, len(word)):
        if word[i] == word[i - 1]:  # Порівнюємо поточний символ з попереднім
            current_count += 1
        else:
            current_count = 1  # Скидаємо лічильник, якщо символи не співпадають

        if current_count > longest_count:
            longest_count = current_count
            longest_char = word[i]

    if longest_count >= 2:
        print(f"Найбільша кількість однакових символів, розташованих підряд: '{longest_char}' ({longest_count} рази)")
    else:
        print("У слові немає двох і більше однакових символів підряд.")

# Зчитуємо введення користувача
word = input("Введіть слово: ")

# Викликаємо функцію для пошуку найбільшої кількості однакових символів
find_longest_repeating_characters(word)
