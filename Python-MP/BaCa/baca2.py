# coding=utf-8
class HistogramNode:
    def __init__(self, key):
        self.key = key
        self.count = 1  # liczba węzłów w poddrzewie (na początku tylko ten węzeł)
        self.left = None
        self.right = None


class HistogramTree:
    def __init__(self):
        self.root = None

    #++++++++
    def insert(self, key):

        if self.search(key) is True:
            print "Element already exists"
            return
        else:
            print "Added:", key



        def localinsert(node, localkey):
            if node is None:
                return HistogramNode(localkey)
            if localkey < node.key:
                node.left = localinsert(node.left, localkey)
            elif localkey > node.key:
                node.right = localinsert(node.right, localkey)
            node.count += 1
            return node

        if self.root is None:
            self.root = HistogramNode(key)
            self.root.count = 1
        else:
            self.root = localinsert(self.root, key)

    def delete(self, key):

        if self.root is None:
            print "Element does not exist"
            return

        if self.search(key) is False:
            print "Element does not exist"
            return
        else:
            print "Deleted:", key

        parent = None
        node_to_delete = self.root

        while node_to_delete and node_to_delete.key != key:
            node_to_delete.count -= 1
            parent = node_to_delete
            if key < node_to_delete.key:
                node_to_delete = node_to_delete.left
            else:
                node_to_delete = node_to_delete.right

        if node_to_delete is None:
            return             # it will break counting

        if node_to_delete.left is None:
            node_to_replace = node_to_delete.right

        elif node_to_delete.right is None:
            node_to_replace = node_to_delete.left

        else:
            node_to_replace = node_to_delete.right
            node_to_replace_parent = node_to_delete
            while node_to_replace.left is not None:
                node_to_replace.count -= 1
                node_to_replace_parent = node_to_replace
                node_to_replace = node_to_replace.left
            node_to_delete.key = node_to_replace.key
            node_to_replace.count -= 1


            if node_to_replace_parent.left is node_to_replace:
                # node_to_replace.count -= 1
                node_to_replace_parent.left = node_to_replace.right
            else:
                node_to_replace_parent.right = node_to_replace.right
                # node_to_replace_parent.count -= 1

            if node_to_delete.left:
                left_count = node_to_delete.left.count
            else:
                left_count = 0
            if node_to_delete.right:
                right_count = node_to_delete.right.count
            else:
                right_count = 0
            node_to_delete.count = 1 + left_count + right_count

            return

        if parent is None:
            self.root = node_to_replace
        elif parent.left is node_to_delete:
            parent.left = node_to_replace
        else:
            parent.right = node_to_replace


    #+++++++
    def search(self, key):


        def localsearch(node, localkey):
            if node is None:
                # print("NO")
                return False
            if node.key == localkey:
                # print("YES")
                return True
            if localkey < node.key:
                return localsearch(node.left, key)
            elif localkey > node.key:
                return localsearch(node.right, key)

        if self.root is None:
            return False

        if localsearch(self.root, key) is True:
            return True
        return False

    #+++++++
    def count_in_range(self, start, end):
        if self.root is None:
            return 0
        else:
            # print ("root: ", self.root.count)
            # print (">end: ", self.count_greater_than(end))
            # print ("<start: ", self.count_less_than(start))
            # print ("all: ", self.root.count - self.count_greater_than(end) - self.count_less_than(start))
            return self.root.count - self.count_greater_than(end) - self.count_less_than(start)

    #++++++
    def count_less_than(self, key):
        if self.root is None:
            return 0

        node = self.root
        result = 0
        while node:
            if node.key < key:
                if node.left is not None:
                    node_left_count = node.left.count
                else:
                    node_left_count = 0
                result += node_left_count + 1
                node = node.right
            else:
                node = node.left

        return result

    #+++++++
    def count_greater_than(self, key):
        if self.root is None:
            return 0

        node = self.root
        result = 0
        while node:
            if node.key > key:
                if node.right is not None:
                    node_right_count = node.right.count
                else:
                    node_right_count = 0
                result += node_right_count + 1
                node = node.left
            else:
                node = node.right

        return result


    def find_kth_smallest(self, k):

        if self.root is None:
            print "Invalid index"
            return

        if k < 1 or k > self.root.count:
            print "Invalid index"
            return

        def local_find(node, localk):
            if node is None:
                return None

            if node.left:
                left_count = node.left.count
            else:
                left_count = 0

            if localk == node.count - (node.count - left_count - 1):
                return node.key

            if localk == left_count:
                node = node.left
                while node.right:
                    node = node.right
                return node.key

            elif localk < left_count:
                return local_find(node.left, localk)
            else:
                return local_find(node.right, localk - left_count - 1)

        print local_find(self.root, k)
        return local_find(self.root, k)



    def inorder_traversal(self):

        if self.root is None:
            return []


        stack = []
        node = self.root
        result = []

        while len(stack) > 0 or node is not None:
            while node is not None:
                stack.append(node)
                node = node.left

            node = stack.pop()
            result.append(node.key)
            node = node.right

        return result


def main():
    tree = HistogramTree()

    while True:
        request = raw_input()
        request = request.strip()
        if request == "EXIT":
            break
        parts = request.split()

        if parts[0].strip() == "INSERT":
            tree.insert(int(parts[1].strip()))

        elif parts[0].strip() == "INORDER":
            print "[",
            # tree.inorder()
            print ", ".join(str(x) for x in tree.inorder_traversal()),
            print "]"
        elif parts[0].strip() == "DELETE":
            tree.delete(int(parts[1].strip()))
        elif parts[0].strip() == "SEARCH":
            if tree.search(int(parts[1].strip())) is not False:
                print "YES"
            else:
                print "NO"
        elif parts[0].strip() == "FIND_KTH":
            tree.find_kth_smallest(int(parts[1].strip()))
        elif parts[0].strip() == "COUNT_RANGE":
            print "Elements in range [" + parts[1].strip() + ", " + parts[2].strip() + "]:",
            print tree.count_in_range(int(parts[1].strip()), int(parts[2].strip()))
        elif parts[0].strip() == "COUNT_LESS":
            print "Elements less than " + parts[1].strip() + ":",   #спереди и сзади убирает пробелы
            print tree.count_less_than(int(parts[1].strip()))
        elif parts[0].strip() == "COUNT_GREATER":
            print "Elements greater than " + parts[1].strip() + ":",
            print tree.count_greater_than(int(parts[1].strip()))



if __name__ == "__main__":
    main()

'''
INSERT 50
INSERT 30
INSERT 70
INSERT 20
INSERT 40
INSERT 60
INSERT 80
INORDER
COUNT_RANGE 30 60
COUNT_LESS 50
COUNT_GREATER 50
FIND_KTH 3
DELETE 30
INORDER
SEARCH 30
SEARCH 40
COUNT_LESS 50
FIND_KTH 3
EXIT
'''
