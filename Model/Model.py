from decouple import config
import pymysql


class Model:
    def __init__(self):
        self.connection = pymysql.connect(
            host=config('MYSQL_HOST'),
            user=config('MYSQL_USER'),
            password=config('MYSQL_PASSWORD'),
            db=config('MYSQL_DB')
        )
        self.cursor = self.connection.cursor()
        print('coneccion estableciada correctamente')

    def close(self):
        self.connection.close()
    
    def get_usuarios(self):
        sql = "SELECT nombre FROM usuarios"
        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()
            return users
        except Exception as e:
            print(e)
            return False


    def login(self, nombre, password):
        sql = "SELECT * FROM usuarios WHERE nombre = '{}' AND password = '{}'".format(nombre, password)
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            if user:
                return user
            else:
                return False
        except Exception as e:
            print(e)
            return False
    def crear_usuario_by_dni(self, dni):
        sql = "INSERT INTO usuarios (dni) VALUES ('{}')".format(dni)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False
    
    def existe_dni(self, dni):
        sql = "SELECT * FROM usuarios WHERE dni = '{}'".format(dni)
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            if user:
                return user
            else:
                return False
        except Exception as e:
            print(e)
            return False
    

