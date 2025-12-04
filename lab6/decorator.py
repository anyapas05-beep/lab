def secure_function(password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user_password = input("Введіть пароль: ")
            if user_password == password:
                return func(*args, **kwargs)
            else:
                print("❌ Невірний пароль. Доступ заборонено.")
        return wrapper
    return decorator
