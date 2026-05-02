class ElectricityBill:
    def __init__(self, units):
        self.units = units
        self.bill_amount = 0.0
    def calculate(self):
        if self.units <= 100:
            self.bill_amount = 0
        elif self.units <= 200:
            self.bill_amount = (self.units - 100) * 1.5
        elif self.units <= 300:
            self.bill_amount = (100 * 1.5) + (self.units - 200) * 2.5
        elif self.units <= 400:
            self.bill_amount = (100 * 1.5) + (100 * 2.5) + (self.units - 300) * 4.0
        else:
            self.bill_amount = (100 * 1.5) + (100 * 2.5) + (100 * 4.0) + (self.units - 400) * 5.0
        return self.bill_amount
units_consumed = float(input("Enter the total units consumed: "))
bill_obj = ElectricityBill(units_consumed)
total_bill = bill_obj.calculate()
print(f"Total Electricity Bill: Rs. {total_bill:.2f}")
