
class Operation:
    def __init__(self):
        pass

    @staticmethod
    def addition(*args):
        if len(args) < 2:
            raise ValueError("Calculation requires at least 2 numbers.")
        return sum(args)

    @staticmethod
    def subtraction(*args):
        sub = args[0]
        if len(args) < 2:
            raise ValueError("Calculation requires at least 2 numbers.")
        for arg in args[1:]:
            sub -= arg
        return sub

    @staticmethod
    def multiplication(*args):
        mul = 1
        if len(args) < 2:
            raise ValueError("Calculation requires at least 2 numbers.")
        elif len(args) == 0:
            return 1
        for arg in args:
            mul *= arg
        return mul

    @staticmethod
    def division(*args):
        div = args[0]
        if len(args) < 2:
            raise ValueError("Calculation requires at least 2 numbers.")
        elif 0 in args[1:]:
            raise ZeroDivisionError("Cannot Divide by Zero.")
        else:
            for arg in args[1:]:
                div /= arg
            return div
