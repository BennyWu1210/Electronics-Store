import database


class Product:
    def __init__(self, p_id, name, price, stock, p_type, year, brand):
        self.name = name
        self.productID = p_id
        self.price = price
        self.stock = stock
        self.brand = brand
        self.year = year
        self.productType = p_type

    def update(self, db, name=None, price=None, stock=None, p_type=None, year=None, brand=None):
        query = """ 
        UPDATE "Product" 
        SET
        """

        if name is not None:
            query += "product_name = \'" + name + "\', "

        if price is not None:
            query += "price = " + str(price) + ", "

        if stock is not None:
            query += "stock = " + str(stock) + ", "

        if p_type is not None:
            query += "product_type = \'" + p_type + "\', "

        if year is not None:
            query += "year = " + str(year) + ", "

        if brand is not None:
            query += "brand = \'" + brand + "\', "

        if query[-2] == ",":
            query = query[0: -2] + ""
            query += """ WHERE product_id = """ + str(self.productID) + ";"
            db.update(query)

        else:
            print("INVALID QUERY: Please pass in at least one argument")


def select_product(db, product_id=None, name=None, price=None, stock=None, p_type=None, year=None, brand=None):
    query = """ SELECT * FROM "Product" WHERE """
    if product_id is not None:
        query += "product_id = " + str(product_id) + ";"
    else:
        if name is not None:
            query += "product_name = \'" + name + "\' AND "

        if price is not None:
            query += "price = " + str(price) + " AND "

        if stock is not None:
            query += "stock = " + str(stock) + " AND "

        if p_type is not None:
            query += "product_type = \'" + p_type + "\' AND "

        if year is not None:
            query += "year = " + str(year) + " AND "

        if brand is not None:
            query += "brand = \'" + brand + "\' AND "

        if query[-4: -1] == "AND":
            query = query[0: -5] + ";"
        else:
            print("INVALID QUERY: Please pass in at least one argument")

    print("query: " + str(query))
    info = db.query(query)
    return info






















