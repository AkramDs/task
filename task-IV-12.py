def decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)#1,2,3)

        total_args = args
        print(total_args)
        
        total_kwargs = kwargs
        print(total_kwargs)

    return wrapper

@decorator
def test(a, b, c):
    print(f'{a} это хорошо. {b} это плохо. {c} это заебумба')

test(1,2,3)
