# У цьому прикладі, якщо ми звертаємось до ключа, 
# який ще не існує, defaultdict автоматично створює для нього новий список і це не призводить до помилок в коді.

from collections import defaultdict

# Створення defaultdict з list як фабрикою за замовчуванням
d = defaultdict(list)

# Додавання елементів до списку для кожного ключа
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)



# Наступний приклад де defaultdict використовує int як функцію за замовчуванням, 
# що означає, що кожен новий ключ має ініційоване значення 0.

d1 = defaultdict(int)

# Збільшення значення для кожного ключа
d1['a'] += 1
d1['b'] += 1
d1['a'] += 1

print(d1)



# Наприклад, у вас є список слів і ви хочете розбити його на декілька списків, залежно від першої літери слова.
words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = {}

for word in words:     # цикл по кожному слову
    # Отримання першої літери слова
    char = word[0]
    if char not in grouped_words:  # перевірка чи є ключ в словнику (ключем є перша літера слова)
        # Якщо ключа немає, створюємо новий список для цього ключа (перша літера)
        grouped_words[char] = []
    grouped_words[char].append(word)   # Додаємо слово до списку, що відповідає його першій літері

# print(grouped_words)

# Таким чином ми можемо отримати всі слова із words, 
# що починаються на якусь літеру. Подібні завдання зустрічаються досить часто. 
# Нам тут завжди доводиться перевіряти, чи створили ми для ключа char в словнику grouped_words пустий список:
#  if char not in grouped_words:
    # grouped_words[char] = []

# Щоб не перевіряти, чи є список на цю літеру в словнику grouped_words, 
# ми можемо скористатися defaultdict із collections та задати значенням за замовчуванням порожній список:

grouped_words1 = defaultdict(list)

for word in words:
    char = word[0]
    grouped_words1[char].append(word)

print(dict(grouped_words1))