import sys
sys.path.append('../queue_and_stack')
sys.path.append('../doubly_linked_list')
from dll_queue import Queue
from dll_stack import Stack
from doubly_linked_list import ListNode

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if (value < self.value):
            if (self.left is None):
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif (value >= self.value):
            if (self.right is None):
                self.right = BinarySearchTree(value)

            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            maximum = self.value
            return maximum
        else:
            return self.right.get_max()
        

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left is not None and self.right is not None:
            self.left.for_each(cb)
            self.right.for_each(cb)
        elif self.left is not None:
            self.left.for_each(cb)
        elif self.right is not None:
            self.right.for_each(cb)
        else:
            return


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(node.left)
        print(self.value)
        if self.right:
            self.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        while q.len() > 0:
            temp = q.dequeue()
            print(temp)
            if temp.left:
                q.enqueue(temp.left)
            if temp.right:
                q.enqueue(temp.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.len() > 0:
            temp = stack.pop()
            print(temp)
            if temp.left:
                stack.push(temp.left)
            if temp.right:
                stack.push(temp.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
