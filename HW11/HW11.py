def call_times(file_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            call_counts = {}
            try:
                with open(file_name, 'r') as file:
                    for line in file:
                        name, count_text = line.strip().split(' was called ')
                        count = int(count_text.split()[0])
                        call_counts[name] = count
            except FileNotFoundError:
                pass

            result = func(*args, **kwargs)
            call_counts[func.__name__] = call_counts.get(func.__name__, 0) + 1
            with open(file_name, 'w') as file:
                for name, count in call_counts.items():
                    file.write(f'{name} was called {count} time{"s" if count != 1 else ""}.\n')

            return result
        return wrapper
    return decorator
@call_times('foo.txt')
def foo():
    pass
@call_times('foo.txt')
def boo():
    pass
@call_times('calls.txt')
def doo():
    pass

foo()
boo()
boo()
doo()
doo()
