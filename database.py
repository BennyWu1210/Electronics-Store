import psycopg2 as pg


# The following code connects to the SQL Database


class Database:
    def __init__(self, host, db, user, password):
        self.link = pg.connect(host=host, database=db, user=user, password=password)
        self.cursor = self.link.cursor()
        print("opened connection")

    def __del__(self):
        self.link.close()
        print("closed connection")

    def query(self, command):
        try:
            self.cursor.execute(command)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def update(self, command):
        try:
            self.cursor.execute(command)
            self.link.commit()
        except Exception as e:
            print("ERROR: " + e)















