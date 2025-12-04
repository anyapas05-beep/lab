from decorator import secure_function


@secure_function("1234")
def secret_function():
    print("✅ Доступ дозволено. Секретна функція виконана.")


secret_function()
