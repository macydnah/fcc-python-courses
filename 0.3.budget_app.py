class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(transaction['amount'] for transaction in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.category}")
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ''
        for item in self.ledger:
            description = item['description'][:23]
            amount = f"{item['amount']:.2f}"
            items += f"{description:<23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    TOTAL_SPENT = sum(
        sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        for category in categories
    )

    rows = ["Percentage spent by category"]
    percentages = []

    # calculate percentages
    for category in categories:
        spent = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        percentage = int(spent / TOTAL_SPENT * 100) // 10 * 10
        percentages.append(percentage)

    # build graph
    for i in range(100, -1, -10):
        row = f"{i:>3}| "
        for percentage in percentages:
            row += "o  " if percentage >= i else "   "
        rows.append(row)

    # horizontal line below the graph
    rows.append("    -" + "-" * (len(categories) * 3))

    # category name vertically printed
    biggest_category_len = max(len(category.category) for category in categories)
    for char_idx in range(biggest_category_len):
        row = "     "
        for category in categories:
            row += (category.category[char_idx] if char_idx < len(category.category) else " ") + "  "
        rows.append(row)

    return "\n".join(rows)

if __name__ == "__main__":
    food = Category('Food')
    food.deposit(1000, 'deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')

    clothing = Category('Clothing')
    food.transfer(50, clothing)

    print(food)

    auto = Category('Auto')
    auto.deposit(1000, 'deposit')
    auto.withdraw(15.89, 'gas')
    auto.transfer(100, food)

    internet = Category('Internet')
    internet.deposit(1000, 'deposit')
    internet.withdraw(15.89, 'gas')
    internet.transfer(100, food)

    categories = [food, clothing, auto, internet]
    print(create_spend_chart(categories))
