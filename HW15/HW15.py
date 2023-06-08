from typing import Any, List
class ReverseIterator:
    def __init__(self, data: List[Any]):
        self.data = data
        self.index = len(data) - 1
    def __iter__(self):
        return self
    def __next__(self) -> Any:
        if self.index >= 0:
            item = self.data[self.index]
            self.index -= 1
            return item
        else:
            raise StopIteration

it = ReverseIterator([1, 2, 3, 4, 5])

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))