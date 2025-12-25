
class Swapper:
    def __init__(self):
        pass

    @staticmethod
    def show_index(tuple_):
        for index, value in enumerate(tuple_):
            print(f"{index}: {value}")

    @staticmethod
    def swap(tuple_, index_1, index_2):
        tuple_ = list(tuple_)
        tuple_[index_1], tuple_[index_2] = tuple_[index_2], tuple_[index_1]
        return tuple(tuple_)

if __name__ == "__main__":
    tuple_ = (4, 2, 3, 'a', 5)
    Swapper.show_index(tuple_)
    print(Swapper.swap(tuple_, 0, 3))
    
    