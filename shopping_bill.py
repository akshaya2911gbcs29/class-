class ShoppingCart:
    def __init__(self):
        self.items = []
        self.subtotals = []
    def get_input(self, n):
        self.items = []
        for i in range(n):
            name = input("Enter item name: ")
            qua = int(input("Enter quantity: "))
            p = int(input("Enter price: "))
            self.items.append((name, qua, p))
        return self.items
    def calculate_subtotal(self):
        self.subtotals = []
        for item in self.items:
            sub = item[1] * item[2]
            self.subtotals.append(sub)
        return self.subtotals
    def calculate_total(self):
        t = sum(self.subtotals)
        print("Total:", t)
        if t > 3000:
            d = t * 0.10
            t = t - d
            print("After Discount:", t)
        else:
            print("After Discount:", t)
        g = t * 0.05
        t = g + t
        print("GST:", g)
        print("After GST Applied:", t)
n = int(input("Enter no of items: "))
cart = ShoppingCart()
r = cart.get_input(n)
print("Items:", r)
s = cart.calculate_subtotal()
print("Subtotal:", s)
cart.calculate_total()
