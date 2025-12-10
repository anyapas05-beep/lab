# Імпортуємо декоратор secure_function з файлу decorator.py
from decorator import secure_function


# Використовуємо декоратор secure_function
# "1234" — це пароль, який потрібно ввести для доступу до функції
@secure_function("1234")
def secret_function():
    # Цей текст виведеться ТІЛЬКИ якщо пароль введено правильно
    print("✅ Доступ дозволено. Секретна функція виконана.")


# Викликаємо функцію
# Під час виклику програма попросить ввести пароль
secret_function()
