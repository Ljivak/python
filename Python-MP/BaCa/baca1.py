#Dmytro Malynyak
from past.builtins import raw_input # baca uses python 2.7 so this library can't be used


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def __str__(self):
        return 'name: {:10} surname: {:15}'.format(self.name, self.surname)
class Employee:
    def __init__(self, person, experience, salary):
        self.person = person
        self.experience = experience
        self.salary = salary
    def __str__(self):
        return '{} experience: {:2} salary: {:5}'.format(self.person, self.experience, self.salary)


def selection_sort(arr, key):
    n = len(arr)
    for i in range(n):

        min_idx = i

        for j in range(i + 1, n):
            if int(key(arr[j])) < int(key(arr[min_idx])):
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


def cocktail_sort(arr, key):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False

        for i in range(start, end):
            if str(key(arr[i])) > str(key(arr[i+1])):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if str(key(arr[i])) > str(key(arr[i+1])):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start = start + 1


def count_sort(input_array, key):
    n = len(input_array)
    M = 0
    for i in range(n):
        if M < int(key(input_array[i])):
            M = int(key(input_array[i]))
    count_array = [0] * (M + 1)

    for num in input_array:
        count_array[int(key(num))] += 1

    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]

    output_array = [None] * len(input_array)

    for i in range(len(input_array) - 1, -1, -1):
        value = int(key(input_array[i]))
        output_array[count_array[value] - 1] = input_array[i]
        count_array[value] -= 1

    for i in range(len(input_array)):
        input_array[i] = output_array[i]



def main():

    namelist = raw_input()
    surnamelist = raw_input()
    experiencelist = raw_input()
    salarylist = raw_input()
    names = namelist.split()
    surnames = surnamelist.split()
    experiences = experiencelist.split()
    salaries = salarylist.split()

    persons = []
    for i in range (len(names)):
        persons.append(Person(names[i], surnames[i]))


    employees= [Employee(person, experience, salary) for person, experience, salary in zip(persons,experiences, salaries)]
#    for i in range (len(names)):
#        print(employees[i])


    selection_sort(employees, key = lambda employee: employee.salary)
#    print("--------------------------")
#    for i in range(len(names)):
#        print(employees[i])

    count_sort(employees, key = lambda employee: employee.experience)
#    print("--------------------------")
#    for i in range (len(names)):
#        print(employees[i])

    cocktail_sort(employees, key = lambda employee: employee.person.name)
#    print("--------------------------")
#    for i in range(len(names)):
#       print(employees[i])

    cocktail_sort(employees, key = lambda employee: employee.person.surname)
#    print("--------------------------")
    for i in range(len(names)):
        print(employees[i])

if __name__ == "__main__":
    main()

'''
Adam Bromir Bruno Abelard Adam Bromir Bruno Abelard Adam Bromir Bruno Abelard Adam Bromir Bruno Abelard
Dachtera Dacka Dachtera Dacka Dachtera Dacka Dachtera Dacka Dachtera Dacka Dachtera Dacka Dachtera Dacka Dachtera Dacka
8 25 56 2 24 59 19 38 8 25 56 2 24 59 19 38
7080 4500 6360 3120 8040 10140 7740 8880 8640 3540 3180 3240 7500 7020 9840 7800
'''