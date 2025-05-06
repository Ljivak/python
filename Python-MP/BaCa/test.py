class HistogramNode:
    def __init__(self, key):
        self.key = key
        self.count = 1  # liczba węzłów w poddrzewie (na początku tylko ten węzeł)
        self.left = None
        self.right = None

class HistogramTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def localinsert(node, localkey):
            if node is None:
                return HistogramNode(localkey)
            if localkey < node.key:
                node.left = localinsert(node.left, localkey)
            elif localkey > node.key:
                node.right = localinsert(node.right, localkey)
            node.count += 1
            return node

        self.root = localinsert(self.root, key)


    def delete(self, key):
        """Usuwa element z drzewa. Złożoność: O(h)"""
        pass


    def search(self, key):

        def localsearch(node, localkey):
            if node is None:
                print("NO")
                return
            if node.key == localkey:
                print("YES")
                return
            if localkey < node.key:
                return localsearch(node.left, key)
            elif localkey > node.key:
                return localsearch(node.right, key)

        localsearch(self.root, key)


    def count_in_range(self, start, end):
        def localcount_in_range(node, localstart, localend):
            if node.key > localend:
                return localcount_in_range(node.left, localstart, localend)
            if node.key < localstart:
                return localcount_in_range(node.right, localstart, localend)

            return 1 + localcount_in_range(node.left, localstart, localend) + localcount_in_range(node.right, localstart, localend)

        localcount_in_range(self.root, start, end)



    def count_less_than(self, key):
        def localcount_less_than(node, localkey):
            if node.key > localkey:
                return localcount_less_than(node.left, localkey)


    def count_greater_than(self, key):
        """Liczy elementy większe od klucza. Złożoność: O(h)"""
        pass

    def find_kth_smallest(self, k):
        """Znajduje k-ty najmniejszy element w drzewie. Złożoność: O(h)"""
        pass

    def inorder(self):
        result = []
        def localinorder(node):
            if node is None:
                return
            localinorder(node.left)
            result.append(node.key)      # собираем ключ в список
            localinorder(node.right)
        localinorder(self.root)
        return result


def main():
    tree = HistogramTree()
    insertrroot = input()
    rootparts = insertrroot.split()
    tree.root = HistogramNode(int(rootparts[1]))
    while (request := input()) != "EXIT":
        parts = request.split()


        if parts[0] == "INSERT":
            tree.insert(int(parts[1]))
        if parts[0] == "INORDER":
            print("[ ", end='')
            tree.inorder()
            print("]", )
        if parts[0] == "DELETE":
            tree.delete(int(parts[1]))
        if parts[0] == "SEARCH":
            tree.search(int(parts[1]))
        if parts[0] == "FIND_KTH":
            tree.find_kth_smallest(int(parts[1]))
        if parts[0] == "COUNT_RANGE":
            tree.count_in_range(int(parts[1]), int(parts[2]))
        if parts[0] == "COUNT_LESS":
            tree.count_less_than(int(parts[1]))
        if parts[0] == "COUNT_GREATER":
            tree.count_greater_than(int(parts[1]))


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
'''