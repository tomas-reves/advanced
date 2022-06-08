def limit_args_decorator(args_count):
    def _limit_args_decorator(func):
        def wrapper(*args: int):
            if len(args) > args_count:
                return "No more than 2 arguments are accepted"
            return func(args)

        return wrapper

    return limit_args_decorator


def suma(*argss):
    return sum(*argss)


limit_args_decorator(4)(suma)(1, 2, 3)
