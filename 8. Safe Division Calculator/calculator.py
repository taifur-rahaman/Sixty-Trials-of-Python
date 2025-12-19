
class Operation:
    def __init__(self):
        pass

    @staticmethod
    def add(*args):
        if len(args) < 2:
            raise ValueError("Calculation requires at least 2 numbers.")
        return sum(args)

    @staticmethod
    def sub(*args):
        sub = args[0]
        if len(args) < 2:
            raise ValueError("Calculation requires at least 2 numbers.")
        for arg in args:
            sub -= arg
        return sub

    @staticmethod
    def mul(*args):
        mul = 1
        if len(args) < 2:
            raise ValueError("Calculation requires at least 2 numbers.")
        elif len(args) == 0:
            return 1
        for arg in args:
            mul *= arg
        return mul

    @staticmethod
    def div(*args):
        div = args[0]
        if len(args) < 2:
            raise ValueError("Calculation requires at least 2 numbers.")
        elif 0 in args[1:]:
            raise ZeroDivisionError("Cannot Divide by Zero.")
        else:
            for arg in args[1:]:
                div /= arg
            return div

# NOTE: Test Code
if __name__ == "__main__":
    operation = Operation()
    print(operation.add(1, 2, 3, 4, 5))
    print(operation.sub(10, 2, 3))
    print(operation.mul(1, 2, 3, 4, 5))
    print(operation.div(6, 2))