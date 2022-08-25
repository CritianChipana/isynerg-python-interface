from Model.Model import Model
# from View.View import View
from datetime import datetime

class Controller:

    produccion_teorica = 14400
    minutos_totales_por_dia = 1440

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
        try:
            actividades = self.model.get_actividad_user_siete_ultimos_dias(maquina_id)
            if actividades:
                for actividad in actividades:
                    lista_actividades.append(list(actividad))
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
                                lista_actividades[j][8] =  0

                # # LIMPIAR EL ARREGLO DE ACTIVIDADES
                lista_final = []
                for actividad in lista_actividades:
                    # print('NOSE1')
                    # print(actividad)
                    if actividad[8] != 0:
                        lista_final.append(actividad)
                        # print('NOSE2')

                #PASAR DE SEGUNDOS A MINUTOS
                for i in range(len(lista_final)):
                    lista_final[i][2] = self.segundos_a_minutos(lista_final[i][2])
                    lista_final[i][3] = self.segundos_a_minutos(lista_final[i][3])
                    lista_final[i][4] = self.segundos_a_minutos(lista_final[i][4])
                    lista_final[i][5] = self.segundos_a_minutos(lista_final[i][5])

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
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print(lista_actividades)
        # print(len(lista_actividades))
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

        if lista_actividades:
            for i in range(len(lista_actividades)):
                lista_para_bashboard.append(round((lista_actividades[i][6]/self.produccion_teorica)*100))

        if lista_actividades:
            for i in range( 7 - len(lista_para_bashboard)):
                lista_para_bashboard.append(0)
        else: 
            for i in range(7):
                lista_para_bashboard.append(0)
        # print('rendimiento')
        print(lista_para_bashboard)
        lista_para_bashboard_inverso = lista_para_bashboard[::-1]
        return lista_para_bashboard_inverso

    def dashboard_calidad(self, maquina_id):
        # # LO QUE SE QUIERE RETORNAR
        # # ['0%', '20%', '40%', '20%', '80%', '20%', '120%']

        print('calidad')
        lista_para_bashboard = []
        lista_actividades = self.get_actividad_user_siete_ultimos_dias(maquina_id)

        if lista_actividades:
            for i in range(len(lista_actividades)):
                if (lista_actividades[i][6] == 0 and lista_actividades[i][7]==0):
                    lista_para_bashboard.append(0)
                else:
                    lista_para_bashboard.append(round(((lista_actividades[i][6]/(lista_actividades[i][6] + lista_actividades[i][7]))*100)))

        if lista_actividades:

            for i in range( 7 - len(lista_para_bashboard)):
                lista_para_bashboard.append(0)

        else: 
            for i in range(7):
                lista_para_bashboard.append(0)

        lista_para_bashboard_reverse = lista_para_bashboard[::-1]
        return lista_para_bashboard_reverse

    def dashboard_capacidad_ociosa(self, maquina_id):
        # # LO QUE SE QUIERE RETORNAR
        # # ['0%', '20%', '40%', '20%', '80%', '20%', '120%']
        lista_para_bashboard = []
        lista_actividades = self.get_actividad_user_siete_ultimos_dias(maquina_id)

        for i in range(len(lista_actividades)):
            total_colores = lista_actividades[i][2] + lista_actividades[i][3] + lista_actividades[i][4] + lista_actividades[i][5]
            total = lista_actividades[i][2] + lista_actividades[i][3] + lista_actividades[i][4] + lista_actividades[i][5] + lista_actividades[i][6] + lista_actividades[i][7]

            if total==0:
                lista_para_bashboard.append(0)
            else :
                lista_para_bashboard.append(round(((1440 - total_colores)/(total))*100))

        for i in range( 7 - len(lista_para_bashboard)):
            lista_para_bashboard.append(0)

        lista_para_bashboard_reverse = lista_para_bashboard[::-1]
        return lista_para_bashboard_reverse

    def dashboard_capacidad_disponibilidad(self, maquina_id):
        # # LO QUE SE QUIERE RETORNAR
        # # ['0%', '20%', '40%', '20%', '80%', '20%', '120%']

        print('disponibilidad')
        lista_para_bashboard = []
        lista_actividades = self.get_actividad_user_siete_ultimos_dias(maquina_id)
        print('lista de actividad controller')
        print(lista_actividades)
        print('lista de actividad controller')

        if lista_actividades:

            for i in range(len(lista_actividades)):
                total_colores = lista_actividades[i][2] + lista_actividades[i][3] + lista_actividades[i][4] + lista_actividades[i][5]
                total = lista_actividades[i][2] + lista_actividades[i][3] + lista_actividades[i][4] + lista_actividades[i][5] + lista_actividades[i][6] + lista_actividades[i][7]

                if (total - (1440 - total_colores)) == 0:
                    lista_para_bashboard.append(0)
                else:
                    lista_para_bashboard.append(round(((lista_actividades[i][2])/(total - (1440 - total_colores)))*100))
                print(7777777777777777777777)
                print((lista_actividades[i][2]))
                print((total - (1440 - total_colores)))
                print(7777777777777777777777)

        print('aaaaaaaaaaaaaaaaaaaaaaaa')
        print(lista_para_bashboard)

        if lista_actividades:
            for i in range( 7 - len(lista_para_bashboard)):
                lista_para_bashboard.append(0)
        else:
            for i in range(7):
                lista_para_bashboard.append(0)

        lista_para_bashboard_reverse = lista_para_bashboard[::-1]
        return lista_para_bashboard_reverse

    def dashboard_capacidad_oee(self, maquina_id):
        # # LO QUE SE QUIERE RETORNAR
        # # ['0%', '20%', '40%', '20%', '80%', '20%', '120%']
        disponibilidad = self.dashboard_capacidad_disponibilidad(maquina_id)
        rendimiento = self.dashboard_rendimiento(maquina_id)
        calidad = self.dashboard_calidad(maquina_id)
        print('ttttttttttttttttt')
        print(disponibilidad)
        print(rendimiento)
        print(calidad)
        print('ttttttttttttttttt')

        print('oee')
        lista_para_bashboard = []

        for i in range(len(rendimiento)):
            lista_para_bashboard.append(round((disponibilidad[i]*rendimiento[i]*calidad[i]*100)))
            print('ttttttttttttttttt')
            print(disponibilidad[i])
            print(rendimiento[i])
            print(calidad[i])


        return lista_para_bashboard

    def dashboard_pie(self, maquina_id):
        # # verde : 2
        # # amarillo : 3
        # # morado : 4
        # # rojo : 5
        # # producto_Real = 6
        # #piezas_malas = 7
        print('pie')
        lista_para_bashboard = []
        lista_actividades = self.get_actividad_user_siete_ultimos_dias(maquina_id)

        total_verde = 0
        total_amarillo = 0
        total_morado = 0
        total_rojo = 0
        total_colores = 0

        if lista_actividades:
            for i in range(len(lista_actividades)):
                total_verde += lista_actividades[i][2]
                total_amarillo += lista_actividades[i][3]
                total_morado += lista_actividades[i][4]
                total_rojo += lista_actividades[i][5]
                total_colores += lista_actividades[i][2] + lista_actividades[i][3] + lista_actividades[i][4] + lista_actividades[i][5]

        # verde, azul, rojo, amarillo, morado
        lista_para_bashboard.append(total_verde)
        lista_para_bashboard.append((1440 - total_colores))
        lista_para_bashboard.append(total_rojo)
        lista_para_bashboard.append(total_amarillo)
        lista_para_bashboard.append(total_morado)

        for i in range( 5 - len(lista_para_bashboard)):
            lista_para_bashboard.append(0)

        # lista_para_bashboard_reverse = lista_para_bashboard[::-1]
        return lista_para_bashboard
    
    def get_maquina_id(self):
        try:
            response = self.model.get_maquina_id()
            if response:
                return response
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def get_actividades_usuario_por_fecha(self):
        try:
            actividades_user_hoy = self.model.get_actividades_usuario_por_fecha()

            total_verde = 0
            total_amarillo = 0
            total_morado = 0
            total_rojo = 0
            total_colores = 0

            if actividades_user_hoy:

                for i in range(len(actividades_user_hoy)):
                    # total_verde += actividades_user_hoy[i][2]
                    # total_amarillo += actividades_user_hoy[i][3]
                    # total_morado += actividades_user_hoy[i][4]
                    # total_rojo += actividades_user_hoy[i][5]
                    total_colores += actividades_user_hoy[i][2] + actividades_user_hoy[i][3] + actividades_user_hoy[i][4] + actividades_user_hoy[i][5]

                return total_colores
            else:
                return False
        except Exception as e:
            print(e)
            return False

