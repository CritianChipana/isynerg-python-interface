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
        sql2 = "SELECT * FROM usuarios WHERE dni = '{}'".format(dni)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            self.cursor.execute(sql2)
            user = self.cursor.fetchone()
            return user
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
    
    def crear_actividad_user(self, user_id, maquina_id, data):
        sql = "INSERT INTO actividades_usuario (usuario_id, verde, 	amarillo, morado, 	rojo, produccion_real, piezas_malas) VALUES ({}, {}, {}, {}, {}, {}, {})".format(user_id, data['verde'], data['amarillo'], data['morado'], data['rojo'], data['produccion_real'], data['piezas_malas'])

        sql2 = "INSERT INTO actividades_maquina (maquina_id, azul) VALUES ({}, {})".format(maquina_id, data['azul'])
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            self.cursor.execute(sql2)
            self.connection.commit()
            return True
        except Exception as e:

            print(e)
            return False

    def create_session(self, user_id):
        print('$$$$$$$$ se crea session $$$$$$$$$$')
        sql = "INSERT INTO session (usuario_id) VALUES ({})".format(user_id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    # SELECT * FROM actividades_usuario WHERE maquina_id = 1 AND created_at > (CURDATE() - INTERVAL 6 DAY) ORDER BY `created_at` ASC

    def get_actividad_user_siete_ultimos_dias(self, maquina_id):
        sql = "SELECT * FROM actividades_usuario WHERE maquina_id = {} AND created_at > (CURDATE() - INTERVAL 6 DAY) ORDER BY `created_at` ASC".format(maquina_id)
        try:
            self.cursor.execute(sql)
            actividad = self.cursor.fetchall()
            print('mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')
            print(actividad)
            print('mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')
            return actividad
        except Exception as e:
            print(e)
            return False