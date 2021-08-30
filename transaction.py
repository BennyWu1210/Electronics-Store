import datetime


class Purchase:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.total = product.price * quantity


class Invoice:
    def __init__(self, user, invoice_time):
        self.transactions = []  # list of purchases
        self.total = 0

    def add_purchase(self, new_purchase):
        if type(new_purchase) != Purchase:
            print("Invalid argument[ERROR]: method takes in a purchase. Received different type")
        else:
            self.transactions.append(new_purchase)

