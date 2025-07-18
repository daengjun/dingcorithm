from operator import index

class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))  # ["333",7] -> ["77",6]

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v

# linked_tuple = LinkedTuple()
# linked_tuple.add("333",7)
# linked_tuple.add("77",6)
#
# print(linked_tuple.items)
# print(linked_tuple.get("333"))

class LinkedDict:
    def __init__(self):
        # self.items = [None] * 8
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key,value)

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)

my_dict = LinkedDict()
my_dict.put("test", 3)
print(my_dict.get("test"))  # 3이 반환되어야 합니다!
