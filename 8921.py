def division(a,b):
    try:
        return int(a)/b
    except TypeError:
        print("Type Error")
    except ValueError:
        print("Value Error")
    finally:
        print("Finally")
        print("Done")
division("A",10)