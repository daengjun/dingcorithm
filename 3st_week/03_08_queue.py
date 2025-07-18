class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# head  tail
# [4] -> [3]

# head          tail
# [4] -> [3] -> [2]

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # 현재 tail의 next에 새 노드를 연결하고
            self.tail = new_node  # tail을 새 노드로 갱신

        # [4] -> [2] -> [3]
        # dequeue!
        # [4] -> [2] -> [3]

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty!"  # 만약 비어있다면 에러!

        delete_head = self.head  # 제거할 node 를 변수에 잡습니다.
        self.head = self.head.next  # 그리고 head 를 현재 head 의 다음 걸로 잡으면 됩니다.

        return delete_head.data  # 그리고 제거할 node 반환

    def peek(self):
        if self.is_empty():
            return "Queue is empty!"

        return self.head.data

    def is_empty(self):
        return self.head is None


queue = Queue()
queue.enqueue(4)
print(queue.peek())
queue.enqueue(2)
print(queue.peek())
queue.enqueue(3)
print(queue.peek())

queue.dequeue()
print(queue.peek())

queue.dequeue()
print(queue.peek())

queue.dequeue()
print(queue.peek())