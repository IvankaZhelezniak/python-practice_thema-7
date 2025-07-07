# Є список в якому потрібно підрахувати кількість елементів, що в ньому зустрічаються. 
# Для цього досить зручно скористатися словником. Реалізація такої задачі може виглядати наступним чином.
from collections import Counter

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = {}
for mark in student_marks:
    if mark in mark_counts:      # Перевірка, чи є mark у словнику
        # Якщо mark вже є в словнику, збільшуємо його лічильник
        mark_counts[mark] += 1
    else:
        mark_counts[mark] = 1  # Якщо mark немає в словнику, додаємо його з лічильником 1

print(mark_counts)

# Але для цього є спеціальний клас Counter, який реалізований в модулі collections.

mark_counts = Counter(student_marks)
print(mark_counts)

# Використання методу most_common для отримання найбільш поширених елементів
# повертає список елементів та їх частоту, починаючи з тих які зустрічаються найчастіше.
print(mark_counts.most_common())
print(mark_counts.most_common(1))
print(mark_counts.most_common(2))


# Наприклад, якщо вам потрібно підрахувати кількість кожної літери у рядку, 
# просто передайте рядок безпосередньо до Counter. 
# Тоді ви можете легко отримати доступ до кількості кожної літери за допомогою ключів, як у звичайному словнику.

# Створення Counter з рядка
letter_count = Counter("banana")
print(letter_count)


# Виконати підрахунок слів в тексті теж стає досить простою задачею:
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_count = Counter(words)

# Виведення слова та його частоти
for word, count in word_count.items():
    print(f"{word}: {count}")
# Виведення найбільш поширених слів
print(word_count.most_common(3))  # Виведе три найбільш поширені слова