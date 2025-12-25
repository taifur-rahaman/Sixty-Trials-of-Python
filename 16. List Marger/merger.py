
class ListMerger:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    @staticmethod
    def _remove_duplicates(user_list):
        return list(set(user_list))

    def marge_lists(self):
        return self._mixed_sort(self._remove_duplicates((self.list_1 + self.list_2)))

    @staticmethod
    def _mixed_sort(user_list):
        int_part = sorted(i for i in user_list if isinstance(i, int))
        str_part = sorted(i for i in user_list if isinstance(i, str))
        return int_part + str_part

    
if __name__ == "__main__":
    list_1 = [1, 2, 'a', 'z', 5]
    list_2 = [4, 'A', 6, 7, 8]
    merger = ListMerger(list_1, list_2)
    print(merger.marge_lists())

