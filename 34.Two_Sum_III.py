# Design and implement a TwoSum class. It should support the following operations: add and find.
# add - Add the number to an internal data structure. find - Find if there exists any pair of numbers which sum is equal to the value.
# For example, add(1); add(3); add(5); find(4) -> true find(7) -> false

class TwoSum:

    def __init__(self) -> None:
        self.out_list = []

    def add(self, number: int) -> None:
        self.out_list.append(number)

    def find(self, value: int) -> bool:
        temp_dict = {}
        for i in self.out_list:
            if i not in temp_dict:
                temp_dict[value - i] = i
            else:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
twoSum = TwoSum()
twoSum.add(1)
twoSum.add(3)
twoSum.add(5)
print(twoSum.find(4))
print(twoSum.find(7))