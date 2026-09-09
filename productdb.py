import mysql.connector


class Dbconnection:
    def get_connection(self):
        try:
            self.connection=mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ansiya@123",
                database="shopdb")

            return self.connection
        except Exception as e:
            print(e)
class ProductManager(Dbconnection):
    def get(self,id=None):
        try:
            self.connect=super().get_connection()
            self.cursor=self.connection.cursor()
            query="select * from product"
            self.cursor.execute(query)
            record=self.cursor.fetchall()
            print(record)
        except Exception as e:
            print(e)

    def post(self,**kwargs):
        try:
            self.cursor=self.connection.cursor()
            query="""
                insert into product(name,category)
                values(%s,%s)
            """
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()
            print("Donor added Successfully...")
        except Exception as e:
            print(e)


    def get_object(self,id=None):
        try:
            self.connect=super().get_connection()
            self.cursor=self.connection.cursor()
            query="select * from product where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            records=self.cursor.fetchone()
            return records
        except Exception as e:
            print(e)

    def put(self,id=None,**kwargs):
        try:
            self.connection=super().get_connection()
            self.cursor=self.connection.cursor()
            records = self.get_object(id=id)
            placeholder=""
            for k in kwargs.keys():
                placeholder+=k+"=%s,"
            placeholder=placeholder.rstrip(",")
            query=f"update product set {placeholder} where id=%s"
            values=[v for v in kwargs.values()]
            values.append(id)
            self.cursor.execute(query,values)
            self.connection.commit()
            print("details updated")
        except Exception as e:
            print(e)



connection=Dbconnection()
products=ProductManager()
products.get()
#products.get_object(id=1)
#products.put(id=1,name="Maggie",category="Snack")
#products.post(name="Chips",category="Snacks")
#products.post(name="Maggie",category="Food")