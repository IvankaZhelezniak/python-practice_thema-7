import decimal
from decimal import Decimal, getcontext, ROUND_DOWN

# Показуємо, як Decimal може бути використаний для точних арифметичних операцій
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
print(Decimal("0.1") + Decimal("0.2"))

# Точність обчислень з Decimal контролюється через контекст. Можна налаштувати загальну точність для всіх обчислень Decimal.
# Встановлюємо точність для Decimal
getcontext().prec = 4

# Тепер будь-які обчислення з Decimal будуть мати точність до чотирьох знаків після коми.
getcontext().prec = 6
print(Decimal("1") / Decimal("7"))

getcontext().prec = 8
print(Decimal("1") / Decimal("7"))


# Виведення буде саме 6 значущих цифр.
# Зміна точності Decimal
getcontext().prec = 6
print(Decimal("233") / Decimal("7"))




# Наприклад, якщо ви хочете округлити число до двох знаків після коми, 
# ви використовуєте Decimal об'єкт з двома нулями після коми як шаблон.

# Вихідне число Decimal
number = Decimal('3.14159')

# Встановлення точності до двох знаків після коми
rounded_number = number.quantize(Decimal('0.00'), rounding=ROUND_DOWN)

print(rounded_number)

# У цьому прикладі число 3.14159 округляється до 3.14 з використанням методу quantize, 
# де як шаблон для точності використовується Decimal('0.00'), а режим округлення встановлено як rounding=ROUND_DOWN.



# За замовчуванням округлення описується константою ROUND_HALF_EVEN
number = Decimal("1.45")

# Округлення за замовчуванням до одного десяткового знаку
print("Округлення за замовчуванням ROUND_HALF_EVEN:", number.quantize(Decimal("0.0")))

# Округлення вверх при нічиї (ROUND_HALF_UP)
print("Округлення вгору ROUND_HALF_UP:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_HALF_UP))

# Округлення вниз (ROUND_FLOOR)
print("Округлення вниз ROUND_FLOOR:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_FLOOR))

# Округлення вверх (ROUND_CEILING)
print("Округлення вгору ROUND_CEILING:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_CEILING))

# Округлення до трьох десяткових знаків за замовчуванням
print("Округлення до трьох десяткових знаків:", Decimal("3.14159").quantize(Decimal("0.000")))
