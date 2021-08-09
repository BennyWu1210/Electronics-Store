

class Product:
    def __init__(self, p_id, name, price, stock, p_type, year, brand):
        self.name = name
        self.productID = p_id
        self.price = price
        self.stock = stock
        self.brand = brand
        self.year = year
        self.productType = p_type

    def update(self, name=None, price=None, stock=None, p_type=None, year=None, brand=None):
        query = """ 
        UPDATE TABLE "Products" 
        SET
        """


        if name is not None:
            query += "name = " + name + ", "

        if price is not None:
            query += "price = " + str(price) + ", "

        if stock is not None:
            query += "stock = " + str(stock) + ", "

        if p_type is not None:
            query += "p_type = " + p_type + ", "

        if year is not None:
            query += "year = " + str(year) + ", "

        if brand is not None:
            query += "brand = \'" + brand + "\', "

        if query[-2] == ",":
            query = query[0: -2] + ""
            query += """ WHERE product_id = """ + str(self.productID) + ";"
        else:
            print("INVALID QUERY: Please pass in at least one argument")

        print(query)


apple = Product(1, 2, 3, 4, 5, 6, 7)
apple.update("1", 2, 3, "4", 5, "6")










