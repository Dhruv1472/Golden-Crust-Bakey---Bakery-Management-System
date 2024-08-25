import datetime as dt


class Food:
    def __init__(self, h):
        self.userA = "LJIET"
        self.passA = 1234
        self.Aproduct = ["cake", "brownie", "bread roll", "cookies"]
        self.Aquantity = [2, 5, 14, 10]
        self.Acost = [900, 200, 100, 200]
        self.Aworker = ["Dipak", "vaibhav"]
        self.Awsalary = [10000, 5000]
        self.name = []
        self.mobile = []
        self.password = []
        now = dt.datetime.now()
        self.d = now.strftime("%d/%m/%y")
        self.t = now.strftime("%H:%M:%S")

        self.G = h
        if self.G == 1:
            self.get()
        else:
            self.p()

    def get(self):
        user = input("ENTER USERNAME:")
        pass1 = int(input("ENTER PASSWORD:"))
        if user == self.userA and pass1 == self.passA:
            print("***** HELLO SIR ,You Logged in as Admin Successfully*****")
            self.get1()
        else:
            print("Enter valid user Name and Password")

    def get1(self):
        print()
        print(
            """ PLEASE CHOOSE
                       1.To Add Item in the shop
                       2.To see Items In The Shop
                       3.To Update cost of any item
                       4.To Add Worker in the shop
                       5.To See workers
                       6.Update salary of any Worker
                       7.FOR EXIT"""
        )

        E = int(input("Enter Your Choice:"))
        if E == 1:
            product = input("Enter Product Name:")
            cost = int(input("Enter The Cost:"))
            quan = int(input("Enter The Quantity:"))
            self.Aproduct.append(product)
            self.Acost.append(cost)
            self.Aquantity.append(quan)
            print("Item Added Succesfully")
            print()
            self.get1()
        elif E == 2:
            print("----------------------------------------------------------------")
            print("|   Serial No. |   Product Name   |   Quantity   |   Price   |")
            print("----------------------------------------------------------------")
            for i in range(len(self.Acost)):
                print(
                    f"| {i+1:<12} | {self.Aproduct[i]:<20} | {self.Aquantity[i]:<10} | {self.Acost[i]:<15} |"
                )
            print("----------------------------------------------------------------")
            self.get1()
        elif E == 3:
            i1 = int(input("Enter the S.no of Product:"))
            n_cost = int(input("Enter the new Cost"))
            self.Acost[i1 - 1] = n_cost
            print("Price Is Updated")
            self.get1()
        elif E == 4:
            item = input("Enter The Worker Name:")
            salary = int(input("Enter Employee Salary:"))
            self.Aworker.append(item)
            self.Awsalary.append(salary)
            print("New Worker Added Successfully")
            print()
            self.get1()
        elif E == 5:
            print("-------------------------------------------------------")
            print("|   Serial No. |   Worker Name    |   Salary   |")
            print("-------------------------------------------------------")
            for i in range(len(self.Aworker)):
                print(f"| {i+1:<12} | {self.Aworker[i]:<20} | {self.Awsalary[i]:<15} |")
            print("-------------------------------------------------------")
            self.get1()
        elif E == 6:
            i1 = int(input("Enter the S.no of Worker:"))
            n_salary = int(input("Enter The New Salary:"))
            self.Awsalary[i1 - 1] = n_salary
            print("Salary Is Updated")
            self.get1()
        else:
            print("SORRY... YOU HAVE ENTERED THE WRONG INPUT")

    def p(self):
        name = input("Enter Your Name:")
        phone = int(input("Enter The Your Mobile Number:"))
        self.name.append(name)
        self.mobile.append(phone)
        self.p1()

    def generate_bill(self):
        file_name = f"Bill-{self.name[0]}.txt"
        with open(file_name, "w") as writer:
            writer.write(
                "|--------------------------------------------------------------------------------|\n"
            )
            writer.write(
                "|                             GOLDEN CRUST BAKERY                              |\n"
            )
            writer.write(
                "|--------------------------------------------------------------------------------|\n"
            )
            writer.write(f"| BILL-ID:1{'':<40} Date: {self.d:<20} |\n")
            writer.write(f"| CUSTOMER-NAME: {self.name[0]:<72} |\n")
            writer.write(f"| PHONE NO: {self.mobile[0]:<72} |\n")
            writer.write("| ADDRESS: Ahmedabad{'':<67} |\n")
            writer.write(
                "|--------------------------------------------------------------------------------|\n"
            )
            writer.write(
                "|                 items                 |    quantity    |        price         |\n"
            )
            writer.write(
                "|--------------------------------------------------------------------------------|\n"
            )
            writer.write(
                f"| {self.Aproduct[self.u - 1]:<40} | {self.j:<14} | {self.Acost[self.u - 1] * self.j:<24} |\n"
            )
            writer.write(
                "|                                    |                |                        |\n"
            )
            writer.write(
                "|                                    |                |                        |\n"
            )
            writer.write(
                "|--------------------------------------------------------------------------------|\n"
            )
            writer.write(f"| {'Total':<49} | {self.Acost[self.u - 1] * self.j:<24} |\n")
            writer.write(
                "|--------------------------------------------------------------------------------|\n"
            )

    def p1(self):
        print("Press 1 to See The Menu")
        print("Press 2 to Order an Item")

        t = int(input("Enter Your Choice:"))
        if t == 1:
            print("----------------------------------------------------------------")
            print("|   Serial No. |   Product Name   |   Quantity   |   Price   |")
            print("----------------------------------------------------------------")
            for i in range(len(self.Acost)):
                print(
                    f"| {i+1:<12} | {self.Aproduct[i]:<20} | {self.Aquantity[i]:<10} | {self.Acost[i]:<15} |"
                )
            print("----------------------------------------------------------------")
            self.p1()
        elif t == 2:
            self.u = int(
                input("Enter The serial Number of the product You want to buy")
            )
            self.j = int(input("Enter The Qty."))
            if self.j <= self.Aquantity[self.u - 1]:
                print("You Have Succesfully ordered your Selected Item!!!!")
                self.Aquantity[self.u - 1] -= self.j
                self.generate_bill()
            else:
                print("This item is not available")
            self.p1()
        else:
            print("Enter Your Valid Choice")


print("|--------------------------------------------------------|")
print("|---------      Welcome To BAKERY        -------------|")
print("|--------------------------------------------------------|")

print(
    """ PLEASE CHOOSE
                       1.FOR ADMIN
                       2.FOR CUSTOMER
                       3.FOR EXIT"""
)
G = int(input("Enter Your Choice:"))

a = Food(G)
