class Node:
    def __init__(self, value=-1):
        self.left = None
        self.mid = None
        self.right = None
        self.value = value

    def preorder(self):
        print(self.value, " ", end="")
        if self.left is not None:
            self.left.preorder()
        if self.mid is not None:
            self.mid.preorder()
        if self.right is not None:
            self.right.preorder()

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.value, " ", end="")
        if self.mid is not None:
            self.mid.inorder()
        if self.right is not None:
            self.right.inorder()

    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.mid is not None:
            self.mid.postorder()
        if self.right is not None:
            self.right.postorder()
        print(self.value, " ", end="")

'''
class Tree:
    def __init__(self, root:Node):
        self.right = root.right
        self.mid = root.mid
        self.left = root.left
        self.value = root.value
        self.root = root
'''

def insert(parent, place, node):
    if place == "left":
       # print(parent.value, "left", node.value)
        parent.left = node
    elif place == "mid":
        parent.mid = node
      #  print("mid")
    elif place == "right":
        parent.right = node
       # print("right")



def main():
    # Creating nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)
    node11 = Node(11)
    node12 = Node(12)
    node13 = Node(13)
    node14 = Node(14)
    node15 = Node(15)

    #tree = Tree(node1)

    insert(node1, "left", node2)
    insert(node1, "mid", node3)
    insert(node1, "right", node4)
    insert(node2, "left", node5)
    insert(node2, "right", node6)
    insert(node4, "right", node8)
    insert(node5, "mid", node9)
    insert(node5, "right", node10)
    insert(node3, "right", node7)
    insert(node7, "left", node11)
    insert(node4, "right", node8)
    insert(node8, "left", node12)
    insert(node8, "mid", node13)
    insert(node8, "right", node14)
    insert(node12, "right", node15)

    print("preorder:", end=" ")
    node1.preorder()
    print("\n""inorder:", end=" ")
    node1.inorder()
    print("\n""postorder:", end=" ")
    node1.postorder()
    print()



if __name__ == "__main__":
    main()

