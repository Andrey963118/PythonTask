def my_func(*args):

    try:
        arg1 = int(input("Ввести числитель "))
        arg2 = int(input("Ввести знаменатель "))
        result = arg1 / arg2
    except ZeroDivisionError:
        return "На ноль делить нельзя"
    return result

print(f'result {my_func()}')
