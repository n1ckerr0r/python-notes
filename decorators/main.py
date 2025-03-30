# Простой декоратор
def decorator(func):
    def wrapper(*args, **kwargs):
        print('start')
        func(*args, **kwargs)
        print('end')
    return wrapper

@decorator
def my_func(a):
    print(a)

# Декоратор с параметрами
def repeat(n):
    def decorator1(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                print('start')
                func(*args, **kwargs)
                print('end')
        return wrapper
    return decorator1

@repeat(3)
def my_func1(a):
    print(a)

# Использование информации о функции
def decorator2(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        print(func.__doc__)
    return wrapper

@decorator2
def my_func2(a):
    print(a)

# Создание декоратора класса

def class_decorator(cls):
    cls.cls_name = cls.__name__
    return cls

@class_decorator
class Class:
    def __init__(self):
        print('class')
    cls_name = 'not class'

# Создание декоратора метода

def method_decorator(method):
    def wrapper(*args, **kwargs):
        method(*args, **kwargs)
        print(method.__name__)
    return wrapper

class Class1:
    @method_decorator
    def method(self):
        print('method name: ')

def main():
    my_func('func')
    my_func1('func1')
    my_func2('func2')
    cls = Class()
    print(cls.cls_name)
    cls1 = Class1()
    cls1.method()

if __name__ == '__main__':
    main()