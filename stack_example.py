# Створення стеку
def create_stack():
    return []

# Перевірка на порожнечу
def is_empty(stack):
    return len(stack) == 0

# Додавання елементу
def push(stack, item):
    stack.append(item)

# Вилучення елементу
def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        print("Стек порожній")

# Перегляд верхнього елемента
def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        print("Стек порожній")


# Приклад використання стеку
# створення стеку та додавання елементів
stack = create_stack()
push(stack, 'a')
push(stack, 'b')
push(stack, 'c')
print("Поточний стек:", stack)

# Перегляд верхнього елемента
print(peek(stack))  # Виведе 'c'

# Видалимо верхній елемент:
print(pop(stack))  # Виведе 'c'
