def bad_fun(n):
    try:
        return n / 0
    except:
        print("¡..........Lo hice otra vez!")
        raise

bad_fun(0)
