from os import system
import random
import datetime


class CompareSorting:

    def __init__(self, amount):
        self.collection = []
        self.amount = amount
        self.path = "Data/Data.txt"
        self.encoding = "utf-8"

    def quicksort(self, left, right):
        start = datetime.datetime.now()
        i, j = left, right
        middle = int((left + right) / 2)
        pivot = self.collection[middle]
        while i <= j:
            while self.collection[i] < pivot:
                i += 1
            while self.collection[j] > pivot:
                j -= 1
            if i <= j:
                self.collection[i], self.collection[j] = self.collection[j], self.collection[i]
                i += 1
                j -= 1
        if left < j:
            self.quicksort(left, j)
        if right > i:
            self.quicksort(i, right)
        duration = datetime.datetime.now() - start
        return self.collection, duration

    def bubblesort(self):
        start = datetime.datetime.now()
        n = len(self.collection)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.collection[j] > self.collection[j+1]:
                    self.collection[j], self.collection[j +
                                                        1] = self.collection[j+1], self.collection[j]
        duration = datetime.datetime.now() - start
        return self.collection, duration

    def get_data_from_file(self):
        tab = []
        with open(self.path, 'r', encoding=self.encoding) as file:
            for line in file:
                if line.split():
                    line = [int(x) for x in line.split(",")]
                    tab.append(line)
        file.close()
        self.collection = tab[0]

    def generate_random_numbers(self):
        try:
            f = open(self.path, "w", encoding=self.encoding)
        except IOError:
            print("Error while opening the file! ")
            return
        for i in range(1, self.amount):
            random_num = random.randint(1, 1000)
            if i != self.amount-1:
                f.write(f"{random_num},")
            else:
                f.write(f"{random_num}")
        f.close()


def main():
    system("cls")
    print("==============SORTING==============\n")
    print("1) Bubble Sort")
    print("2) Quick Sort")
    print("3) Test the performance")
    print("4) Quit\n")
    try:
        choice = int(input("Chose option: "))
    except ValueError:
        print("Incorrect value given!")
        return

    if choice == 4:
        system("cls")
        print("Thanks for using!")
        return

    system("cls")
    try:
        amount = int(input("How many numbers you want to sort? "))
    except:
        print("Incorrect value given!")
        return

    compareSorting = CompareSorting(amount)
    compareSorting.generate_random_numbers()
    compareSorting.get_data_from_file()

    if choice == 1:
        collection, duration = compareSorting.bubblesort()
        print("Bubble Sort: ", collection)
        print("The algorithm ran over time: ", duration)
        system("pause")
        system("cls")
    elif choice == 2:
        collection, duration = compareSorting.quicksort(
            0, len(compareSorting.collection)-1)
        print("Quick Sort: ", collection)
        print("The algorithm ran over time: ", duration)
        system("pause")
        system("cls")
    elif choice == 3:
        n = (len(compareSorting.collection) - 1)
        collection, b_duration = compareSorting.bubblesort()
        collection, q_duration = compareSorting.quicksort(0, n)
        print(
            f"For {amount} numbers, 'bubblesort' executed in: { b_duration} while 'quicksort' in: { q_duration}")
    else:
        print("Wrong option!")


if __name__ == '__main__':
    main()
