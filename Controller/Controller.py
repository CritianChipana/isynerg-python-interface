from Model.Model import Model
# from View.View import View
from datetime import datetime

class Controller:

    prodcuccion_teorica = 14400

    def __init__(selft):
        selft.model = Model()
        print('a')
        # self.view = View
    
    def get_usuarios(self):
        try:
            users = self.model.get_usuarios()
            return users
        except Exception as e:
            print(e)
            return False

    def login(self, nombre, password):
        try:
            user = self.model.login(nombre, password)
            return user
        except Exception as e:
            print(e)
            return False

    def crear_usuario_by_dni(self, dni):
        try:
            # verificar si existe dni
            existe_usuario = self.model.existe_dni(dni)
            if existe_usuario:
                return existe_usuario
            else:
                # crear usuario
                response = self.model.crear_usuario_by_dni(dni)

                if response:
                    return response
                else:
                    return False
        except Exception as e:
            print(e)
            return False

    def crear_actividad_user(self, user_id, maquina_id, data):
        try:
            response = self.model.crear_actividad_user(user_id, maquina_id ,data)
            if response:
                return response
            else:
                return False
        except Exception as e:
            print('###################################')
            print(e)
            print('###################################')
            return False

    def create_session(self, user_id):
        try:
            response = self.model.create_session(user_id)
            if response:
                return response
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def get_actividad_user_siete_ultimos_dias(self, maquina_id):
        lista_actividades = []
        lista_actividades_auxiliar = []
        try:
            actividades = self.model.get_actividad_user_siete_ultimos_dias(maquina_id)
            if actividades:
                for actividad in actividades:
                    lista_actividades.append(list(actividad))
                # print(lista_actividades)
                # print(lista_actividades[0][8])
                # print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                # print(datetime.strftime(lista_actividades[0][8], "%d-%m-%Y"))
                for i in range(len(lista_actividades)-1):
                    for j in range(len(lista_actividades)):
                        # print('* ',i, ' ',j, ' *')
                        if lista_actividades[i][8] != 0 and lista_actividades[j][8] != 0 and i < j:
                            if datetime.strftime(lista_actividades[i][8], "%d-%m-%Y") == datetime.strftime(lista_actividades[j][8], "%d-%m-%Y"):
                                lista_actividades[i][2] = lista_actividades[i][2] + lista_actividades[j][2]
                                lista_actividades[i][3] = lista_actividades[i][3] + lista_actividades[j][3]
                                lista_actividades[i][4] = lista_actividades[i][4] + lista_actividades[j][4]
                                lista_actividades[i][5] = lista_actividades[i][5] + lista_actividades[j][5]
                                lista_actividades[i][6] = lista_actividades[i][6] + lista_actividades[j][6]
                                lista_actividades[i][7] = lista_actividades[i][7] + lista_actividades[j][7]
                                # print(i, ' ',j)
                                # print('se elimina la actividad')
                                lista_actividades[j][8] =  0
                                # print('activiades despues de eliminar')
                # # LO QUE SE QUIERE RETORNAR
                # # ['0%', '20%', '40%', '20%', '80%', '20%', '120%']

                # print('limpiar arreglo')
                # print(lista_actividades)
                # print('limpiar arreglo')

                # # LIMPIAR EL ARREGLO DE ACTIVIDADES
                lista_final = []
                for actividad in lista_actividades:
                    # print('NOSE1')
                    # print(actividad)
                    if actividad[8] != 0:
                        lista_final.append(actividad)
                        # print('NOSE2')

                # print('????????????????????????????????')
                # print(lista_actividades)
                # print('????????????????????????????????')
                # print(lista_final)
                # # verde : 2
                # # amarillo : 3
                # # morado : 4
                # # rojo : 5
                # # producto_Real = 6
                # #piezas_malas = 7
                return lista_final
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def segundos_a_minutos(self, segundos):
            minutos = int(segundos/60)
            return minutos

    def dashboard_rendimiento(self, maquina_id):
        # # LO QUE SE QUIERE RETORNAR
        # # ['0%', '20%', '40%', '20%', '80%', '20%', '120%']

        print('rendimiento')
        lista_para_bashboard = []
        lista_actividades = self.get_actividad_user_siete_ultimos_dias(maquina_id)
        # print(lista_actividades)

        for i in range(len(lista_actividades)):
            lista_para_bashboard.append(round((lista_actividades[i][6]/self.prodcuccion_teorica)*100))

        for i in range( 7 - len(lista_para_bashboard)):
            lista_para_bashboard.append(0)
        # print('rendimiento')
        print(lista_para_bashboard)
        a = lista_para_bashboard[::-1]
        print(a)
        print('rendimiento')
        return a

    def dashboard_calidad(self, maquina_id):
        # # LO QUE SE QUIERE RETORNAR
        # # ['0%', '20%', '40%', '20%', '80%', '20%', '120%']

        print('calidad')
        lista_para_bashboard = []
        lista_actividades = self.get_actividad_user_siete_ultimos_dias(maquina_id)

        for i in range(len(lista_actividades)):
            lista_para_bashboard.append(round(((lista_actividades[i][6]/(lista_actividades[i][6] + lista_actividades[i][7]))*100)))

        for i in range( 7 - len(lista_para_bashboard)):
            lista_para_bashboard.append(0)

        lista_para_bashboard_reverse = lista_para_bashboard[::-1]
        return lista_para_bashboard_reverse

    def dashboard_capacidad_ociosa(self, maquina_id):
        # # LO QUE SE QUIERE RETORNAR
        # # ['0%', '20%', '40%', '20%', '80%', '20%', '120%']
        lista_para_bashboard = []
        lista_actividades = self.get_actividad_user_siete_ultimos_dias(maquina_id)

        for i in range(len(lista_actividades)):
            total = lista_actividades[i][2] + lista_actividades[i][3] + lista_actividades[i][4] + lista_actividades[i][5] + lista_actividades[i][6] + lista_actividades[i][7]
            lista_para_bashboard.append(round(((lista_actividades[i][6]/(lista_actividades[i][6] + lista_actividades[i][7]))*100)))

        for i in range( 7 - len(lista_para_bashboard)):
            lista_para_bashboard.append(0)

        lista_para_bashboard_reverse = lista_para_bashboard[::-1]
        return lista_para_bashboard_reverse

def dashboard_capacidad_disponibilidad(self, maquina_id):
        # # LO QUE SE QUIERE RETORNAR
        # # ['0%', '20%', '40%', '20%', '80%', '20%', '120%']

        print('calidad')
        lista_para_bashboard = []
        lista_actividades = self.get_actividad_user_siete_ultimos_dias(maquina_id)

        for i in range(len(lista_actividades)):
            lista_para_bashboard.append(round(((lista_actividades[i][6]/(lista_actividades[i][6] + lista_actividades[i][7]))*100)))

        for i in range( 7 - len(lista_para_bashboard)):
            lista_para_bashboard.append(0)

        lista_para_bashboard_reverse = lista_para_bashboard[::-1]
        return lista_para_bashboard_reverse

def dashboard_capacidad_oee(self, maquina_id):
        # # LO QUE SE QUIERE RETORNAR
        # # ['0%', '20%', '40%', '20%', '80%', '20%', '120%']

        print('calidad')
        lista_para_bashboard = []
        lista_actividades = self.get_actividad_user_siete_ultimos_dias(maquina_id)

        for i in range(len(lista_actividades)):
            lista_para_bashboard.append(round(((lista_actividades[i][6]/(lista_actividades[i][6] + lista_actividades[i][7]))*100)))

        for i in range( 7 - len(lista_para_bashboard)):
            lista_para_bashboard.append(0)

        lista_para_bashboard_reverse = lista_para_bashboard[::-1]
        return lista_para_bashboard_reverse

