class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        # 구현해보세요!

        # 1. 원소를 맨 끝에 추가합니다.
        self.items.append(value)

        cur_index = len(self.items) - 1

        while cur_index != 1:  # 1인 경우에는 root node 라 더 비교할게 없음. 올라갈 일이 없음
            parent_index = cur_index // 2  # 2. 부모 노드랑 비교해서 내가 더 크다면 위치를 바꾼다.
            if self.items[cur_index] > self.items[parent_index]:
                # 두개의 값을 변경
                self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index]
                cur_index = parent_index
            else:
                break
        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
# 1. 맨뒤에다가 원소르 넣는다
# 2. 부모와 비교해서 자기가 높으면 바꾼다
# 3. 2의 과정을 부모가 더 크거나 루트 노드에 달했을때까지 반복한다.

# 1. 맨 뒤에 넣는다
# 3  level 0
# 4  level 1

# 2. 반복을 끝냅니다.
# 4 level 0
#  3 level 1
# [None,4,3]

max_heap.insert(2)

# 부모가 자식보다 큰 max_heap 규칙을 지켜지기때문에
# 순서 변경은 일어나지않고 배열 맨마지막에 추가됨

#  4 level 0
#  3 2 level1
#  [None,4,3,2]

max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!
