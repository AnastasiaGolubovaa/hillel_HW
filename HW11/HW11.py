def call_times(file_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Read the existing call counts from the file
            try:
                with open(file_name, 'r') as file:
                    lines = file.readlines()
                    call_counts = {}
                    for line in lines:
                        name, count = line.strip().split(' was called ')
                        call_counts[name] = int(count)
            except FileNotFoundError:
                call_counts = {}

            # Call the decorated function
            result = func(*args, **kwargs)

            # Update the call count
            func_name = func.__name__
            call_counts[func_name] = call_counts.get(func_name, 0) + 1

            # Write the updated call counts to the file
            with open(file_name, 'w') as file:
                for name, count in call_counts.items():
                    file.write(f'{name} was called {count} times.\n')

            return result

        return wrapper

    return decorator
