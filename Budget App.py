import math

class Category:
    def __init__(self, budget):
        self.budget = budget
        self.ledger = list()

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return sum(i.get("amount") for i in self.ledger)

    def transfer(self, amount, budget):
        if self.check_funds(amount) == True:
            self.withdraw(amount, "Transfer to " + budget.budget)
            budget.deposit(amount, "Transfer from " + self.budget)
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        r = list()
        r.append("*" * int(math.floor(15 - len(self.budget)/2)) + self.budget[:30] + "*" * int(math.ceil(15 - len(self.budget)/2)) + "\n")
        for i in self.ledger:
            r.append(i.get("description")[:23] + (" " * (30 - len(i.get("description")[:23]) - len("{:.2f}".format(i.get("amount"))[:7]))) + "{:.2f}".format(i.get("amount"))[:7] + "\n")
        r.append("Total: " + str(self.get_balance()))
        return "".join(r)

def create_spend_chart(categories):
    p = list()
    for c in categories:
        p.append({"amount": sum(i.get("amount") for i in c.ledger if i.get("amount") < 0), "category": c.budget})
    for i in p:
        i["percentage"] = math.floor(i.get("amount")/sum(i.get("amount") for i in p) * 10) * 10
    
    chart = list()
    chart.append("Percentage spent by category\n")
    for ten in range(11):
        ten = 100 - 10 * ten
        chart.append((3 - len(str(ten))) * " " + str(ten) + "|")
        for i in p:
            o = "   "
            if i.get("percentage") >= ten:
                o = " o "
            chart.append(o)
        chart.append(" \n")
    chart.append("    -" + "---" * len(p))
    for long in range(len(max((i.budget for i in categories), key=len))):
        chart.append("\n    ")
        for i in p:
            try:
                chart.append(" " + list(i.get("category"))[long] + " ")
            except:
                chart.append("   ")
        chart.append(" ")
    return "".join(chart)