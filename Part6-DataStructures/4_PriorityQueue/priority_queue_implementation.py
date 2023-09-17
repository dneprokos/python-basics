import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def __str__(self):
        return str(self.elements)


if __name__ == "__main__":
    p_queue = PriorityQueue()
    print(p_queue)
    print(p_queue.is_empty())

    # item, priority
    p_queue.put("eat", 2)
    p_queue.put("code", 1)
    p_queue.put("sleep", 3)
    p_queue.put("test", 1)

    print(p_queue)

    print(p_queue.get())
    print(p_queue.get())

    print(p_queue)
