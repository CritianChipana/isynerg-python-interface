from Model.Model import Model
# from View.View import View

class Controller:

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


# control = Controller()
# control.run()