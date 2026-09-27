def my_decorator(function):

    def wrapper(records):
        print("Function started")

        result = function(records)

        print("Function completed")

        return result

    return wrapper