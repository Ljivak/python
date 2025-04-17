
class AdjecentHanoi:
    def __init__(self, number):
        self.number = number
        self.first = list(range(number, 0, -1))
        self.second = []
        self.third = []


    def makeLeft(self, tower_id: int):
        if tower_id == 0:
            return
        if tower_id == 1:
            if len(self.second) == 0:
                return
            self.first.append(self.second.pop())
        if tower_id == 2:
            if len(self.third) == 0:
                return
            self.second.append(self.third.pop())

    def makeRight(self, tower_id: int):
        if tower_id == 2:
            return
        if tower_id == 1:
            if len(self.second) == 0:
                return
            self.third.append(self.second.pop())
        if tower_id == 0:
            if len(self.first) == 0:
                return
            self.second.append(self.first.pop())

    def move(self, from_tower, to_tower):
        if ord(from_tower) == ord(to_tower) + 1:
            self.makeLeft(int(ord(from_tower)-65))
        elif ord(from_tower) == ord(to_tower) - 1:
            self.makeRight(int(ord(from_tower)-65))
        else :
            print('ERROR ERROR ERROR ERROR')
            return




    def rek(self, n, first, third, second):
        if n > 0:
            self.rek(n - 1, first, third, second)
            self.move(first, second)
            self.rek(n - 1, third, first, second)
            self.move(second, third)
            self.rek(n - 1, first, third, second)

    def solve(self):

        if self.number == 0:
            print('No solution')
            return
        else:
            self.rek(self.number, 'A', 'C', 'B')




    def displey(self):
        print(self.first)
        print(self.second)
        print(self.third)




def main():
    hanoi = AdjecentHanoi(10)
    hanoi.displey()
    print('\n', '--------------', '\n')
    hanoi.solve()
    hanoi.displey()

if __name__ == '__main__':
    main()
