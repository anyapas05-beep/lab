def secure_function(password):
    # ↑ функція-декоратор, приймає правильний пароль

    def decorator(func):
        # ↑ decorator отримує функцію, яку треба захистити

        def wrapper(*args, **kwargs):
            # ↑ wrapper — обгортка, яка виконується замість функції

            user_password = input("Введіть пароль: ")
            # ↑ запитуємо пароль у користувача

            if user_password == password:
                # ↑ перевіряємо, чи правильний пароль
                return func(*args, **kwargs)
                # ↑ виконуємо захищену функцію
            else:
                # ↑ якщо пароль неправильний
                print("❌ Невірний пароль. Доступ заборонено.")
                # ↑ виводимо повідомлення про відмову

        return wrapper
        # ↑ повертаємо обгортку

    return decorator
    # ↑ повертаємо декоратор
