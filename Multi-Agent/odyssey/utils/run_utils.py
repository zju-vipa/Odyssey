import functools
import time

def retry(retry_count=3):
    def decorator_retry(func):
        @functools.wraps(func)
        def wrapper_retry(*args, **kwargs):
            last_exception = None
            for _ in range(retry_count):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    time.sleep(1)  
            raise last_exception
        return wrapper_retry
    return decorator_retry


if __name__ == '__main__':
    @retry(retry_count=3)
    def test_func():
        import random
        if random.randint(0, 1):
            print("Function succeeded")
            return "Success"
        else:
            print("Function failed")
            raise ValueError("Random error occurred")

    try:
        result = test_func()
        print("Result:", result)
    except Exception as error:
        print("An error occurred:", error)
