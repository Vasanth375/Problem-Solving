from collections import defaultdict
import bisect

class NumberContainers:

    def __init__(self):
        self.ns = defaultdict(lambda: -1)
        self.value_to_indices = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        if self.ns[index] != -1:
            old_number = self.ns[index]
            self.value_to_indices[old_number].remove(index)
        self.ns[index] = number
        bisect.insort(self.value_to_indices[number], index)

    def find(self, number: int) -> int:
        if self.value_to_indices[number]:
            return self.value_to_indices[number][0]
        return -1
    