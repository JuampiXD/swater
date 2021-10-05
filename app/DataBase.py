import pymysql


class DataBase:
    def __init__(self, expedition):
        self.expedition = expedition
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='expedition_to_mars'
        )
        self.cursor = self.connection.cursor()
        print("Conexion establecida exitosamente")

    def Insert(self):
        sql = "insert into coordinates (length,latitude,size,potable) VALUES ('{}','{}','{}','{}')".format(
            self.expedition['length'],
            self.expedition['latitude'], self.expedition['size'], self.expedition['potable'])
        print(sql)
        self.cursor.execute(sql)
        self.connection.commit()
        print('Registro insertado exitosamente')
