# MAX HEAP Implementation
# A max-heap is a complete binary tree in which the value in each internal node 
# is greater than or equal to the values in the children of that. Its very FAST.

# Main condition: Parent >= Childs (Each node is <= of its parent)
# Main structure: COMPLETE BINARY TREE (2-tree)
#      condition: Every node except the leaves has two childs, 
#               every level its completed except for posible leaf elements. 
#               Nodes that are leafs does not have right siblings. 
#               All nodes are added towards left (first fill the left side)
# Methods:
# Peek: get the max value (root)
# Push: add value to the end, float up to the right position
# Pop: removes the max, return the max, swap the max with the last node then remove.
#   Bubbledown the swapped value (root) to the right position, compare first left side
#   and needs to check all the tree for acomplish the main condition.

# Implements using list, for this approach we need to omit the firts position (0 index)
# to apply the following formulas to traverse trough the heap
# max value = heap[1]
# parent = index//2 
# left child = index * 2
# right child = (index * 2) + 1
class MaxHeap:
    def __init__(self, items=[]) -> None:
        
        self._heap = [0] 
        for item in items:
            self._heap.append(item)
            self._floatUp(len(self._heap) -1 )
    
    def __str__(self) -> str:
        if len(self._heap) > 1:
            return f"MAX HEAP: max{self._heap[1]} items{self._heap[1:]}"
        else:
            return f"MAX HEAP: empty"

    def push(self, item):
        self._heap.append(item)
        self._floatUp(len(self._heap) -1 )

    def peek(self):
        if len(self._heap) > 1:
            return self._heap[1]
        else:
            return None
    
    def _get_parent(self, position:int) -> int:
        return position // 2
    def _get_left_child(self, position: int) -> int:
        return position * 2
    def _get_right_child(self, position: int) -> int:
        return (position * 2) + 1

    def _swapp(self, child_position: int, parent_position:int) -> None:
        temp = self._heap[parent_position]
        self._heap[parent_position] = self._heap[child_position]
        self._heap[child_position] = temp
        # self._heap[parent_position], self._heap[child_position] = self._heap[child_position], self._heap[parent_position]
    
    def pop(self):
        if len(self._heap) > 2:
            last_index = len(self._heap) - 1
            # Swapp the max and the last
            self._swapp(last_index, 1)
            # Remove from heap
            item = self._heap.pop()
            # Reorder heap
            self._bubbleDown(1)
            return item
        elif len(self._heap) == 2:
            return self._heap.pop()
        else:
            return None

    def _floatUp(self, position) -> None:
        
        parent_index = self._get_parent(position)
        
        if position == 1 or parent_index == 0:
            return
        
        if self._heap[parent_index] >= self._heap[position]:
            return
        
        self._swapp(position, parent_index)
        self._floatUp(parent_index)

    def _bubbleDown(self, position:int)->None:
        
        left_child_index = self._get_left_child(position)
        if left_child_index <= len(self._heap)-1:
            if self._heap[position] < self._heap[left_child_index]:
                self._swapp(left_child_index, position)
                self._bubbleDown(left_child_index)
            else:
                return
        
        right_child_index = self._get_right_child(position)
        if right_child_index <= len(self._heap)-1:
            if self._heap[position] < self._heap[right_child_index]:
                self._swapp(right_child_index, position)
                self._bubbleDown(right_child_index)
            else:
                return
    
# TEST

mh = MaxHeap([95,3,21])
print(mh)
mh.push(10)
print(mh)
print(f"PEEK: {mh.peek()}")
print(f"POP: {mh.pop()}")
print(mh)





