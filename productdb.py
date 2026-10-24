import mysql.connector
class Dbconnection:
    def get_connection(self):
        try:
            self.connection=mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ansiya@123",
                database="shopdb"
            )
            return self.connection
        except Exception as e:
            return None
class ProductManager(Dbconnection):
    def get(self):
        try:
            self.connect=super().get_connection()
            self.cursor=self.connect.cursor()
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
            print("item added Successfully...")
        except Exception as e:
            print(e)


    def get_object(self,id=None):
        try:
            self.connect=super().get_connection()
            self.cursor=self.connect.cursor()
            query="select * from product where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            records=self.cursor.fetchone()
            return records
        except Exception as e:
            print(e)

    def retrive(self,id=None):
        try:
            records=self.get_object(id=id)
            print(records)
            if records==None:
                print("Items not found..")
        except Exception as e:
            print(e)

    def put(self,id=None,**kwargs):
        try:
            self.connection=super().get_connection()
            records = self.get_object(id=id)
            if records!=None:
                self.cursor=self.connect.cursor()
                placeholder=" "
                for k in kwargs.keys():
                    placeholder+=k+"=%s,"
                placeholder=placeholder.rstrip(",")
                query=f"update product set {placeholder} where id=%s"
                values=[v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connect.commit()
            print("Item details Updated")
        except Exception as e:
            print(e)

    def delete(self,id=None):
        try:
            self.connection=super().get_connection()
            records = self.get_object(id=id)
            print(records)
            if id==None:
                print("Items not found")
            else:
                query = "delete from product where id=%s"
                values = (id,)
                self.cursor.execute(query, values)
                records = self.cursor.fetchone()
                self.connect.commit()
                print("Items deleted successfully..")
        except Exception as e:
            print(e)





connection_instances=Dbconnection()
print(connection_instances.get_connection())
products_instance=ProductManager()
products_instance.get()
#products_instance.post(name="Shampoo",category="Hair Products")
#products_instance.put(id=2,name="Pepsi",category="Drinks")
#products_instance.retrive(4)
#products_instance.delete(2)