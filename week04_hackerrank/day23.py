import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self, root):
        # Write your code here
        if root is None:
            return
        my_queue = []
        lst = []
        # Store root into the queue
        my_queue.append(root)
        # Print and remove element inside the queue
        while len(my_queue) > 0:
            lst.append(my_queue[0].data)
            node = my_queue.pop(0)

            # Add the left node of removed element into a queue
            if node.left:
                my_queue.append(node.left)

            # Add the right node of removed element into a queue
            if node.right:
                my_queue.append(node.right)

        print(' '.join(map(str,lst)))

T=int(input())
myTree=Solution()
root=None
for i in range(6):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
