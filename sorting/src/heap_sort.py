'''
Created on 2011-09-15

@author: Alec
'''
from collections import namedtuple

HeapNode = namedtuple("HeapNode", "value children")

class Heap(object):
    
    def __init__(self, items):
#        self.current_parent = root = HeapNode(items[0], [])
        self.items = [items[0]]
        for item in items[1:]:
            self.add(item)

            
    def add(self, item):
        pos = len(self.items)
        self.items.append(item)
        up = (pos-1)//2
        while item > self.items[up]:
            self.swap(pos, up)
            pos = up
            if pos is 0:
                break
            up =  (pos-1)//2
            
            
    def trickle_down(self, pos):
        """This is like what happens in add, except we need to make sure to
        pick the greater value to swap with."""
        item = self.items[pos]
        down_1 = (pos * 2) + 1
        down_2 = down_1 + 1
        if (down_2) >= len(self.items):
            return
        if (down_2 + 1) >= len(self.items):
            new_pos = down_1
        else:
            new_pos = down_1 if self.items[down_1] > self.items[down_2] else down_2
        greater = self.items[new_pos]
        if item < greater:
#            print("Moving {0} from {1} to {2}".format(item, pos, new_pos))
            self.swap(pos, new_pos)
#            print(self.items)
            self.trickle_down(new_pos)
            
            
    def swap(self, one, two):
        self.items[one], self.items[two] = self.items[two], self.items[one]
#        

def heap_sort(items):
    heap = Heap(list(items))
    sorted_items = []
    while heap.items:
        heap.swap(0, -1)
        sorted_items.insert(0, heap.items.pop())
        if heap.items:
            heap.trickle_down(0)
    return sorted_items
    
    
if __name__ == "__main__":
    from timeit import Timer
    t = Timer('heap_sort("eqionvnmvjkclwjklcpwaxctwa")', 
              "from __main__ import heap_sort")
    my_time = t.timeit(number=10000)
    t_2 = Timer('sorted(list("eqionvnmvjkclwjklcpwaxctwa"))')
    py_time = t_2.timeit(number=10000)
    print("My sort takes {0} times as long.".format(my_time / py_time))