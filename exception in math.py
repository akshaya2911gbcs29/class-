class Exceptiondemo:
    def divide(self):
        try:
            a = int(input("Enter numerator: "))
            b = int(input("Enter denominator: "))
            result = a / b
            print("Result: ", result)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero")
        except ValueError:
            print("Error: Invalid input (only numbers allowed)")
    def access_list(self):
        try:
            lst = list(map(int, input("Enter list elements (space separated): ").split()))
            index = int(input("Enter index: "))
            print("Result: ", lst[index])
        except IndexError:
            print("Error: Index out of range")
        except ValueError:
            print("Error: Invalid input")
    def access_dict(self):
        try:
            d = {}
            n = int(input("Enter number of key-value pairs: "))
            for i in range(n):
                key = input("Enter key: ")
                value = input("Enter value: ")
                d[key] = value
            search_key = input("Enter key to search: ")
            print("Value: ", d[search_key])
        except KeyError:
            print("Error: Key not found in dictionary")
        except ValueError:
            print("Error: Invalid input for number of pairs")
obj = Exceptiondemo()
obj.divide()
obj.access_list()
obj.access_dict()
