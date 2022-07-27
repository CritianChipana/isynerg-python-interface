from tkinter import *
from tkinter.ttk import Combobox
from turtle import color

from Controller.Controller import Controller
from Model.Model import Model

class View(object):

    contador_numeros_dni = 0
    arreglo_usuarios = []
    user = ()

    def __init__(self):
        self.controller = Controller()
        self.model = Model()
        self.interface()

    def interface(self):
        self.raiz = Tk()
        # raiz.attributes('-fullscreen', True)
        # self.raiz.geometry(str(self.raiz.winfo_screenwidth()) +'x' +  str(self.raiz.winfo_screenheight()) )
        # raiz.config(width="1200", height="800")
        self.raiz.geometry("1200x800")
        self.raiz.config(bg="blue")
        self.raiz.columnconfigure(1, weight=1)
        self.raiz.rowconfigure(1, weight=1)

        self.frame_padre = Frame(self.raiz, padx=10, pady=10, bg="yellow")
        self.frame_padre.grid(row=1, column=1, sticky="nsew")

        self.frame_padre.rowconfigure(1, weight=1)
        self.frame_padre.columnconfigure(1, weight=1)
        # self.frame_padre.rowconfigure(1, weight=1)
        self.frame_padre.columnconfigure(2, weight=1)

        frame_login = Frame( self.frame_padre,bg="green")
        frame_login.grid(row=1, column=1, sticky="nsew")

        frame_session = Frame(frame_login, padx=20, pady=20, bg="red")
        frame_session.grid(row=2, column=1, rowspan=2, sticky="nsew")

        # btn_start = Button(frame_login, text="Start", padx=100, pady=55, fg="white", bg="green", font=("Arial", 20), command=self.hola)
        self.btn_start = Button(frame_login, text="Start", state=DISABLED, padx=100, pady=55, fg="white", bg="green", font=("Arial", 20))
        self.btn_start.grid(row=1, column=1, padx=100, pady=100)

        #input NOMBRE
        label_operador = Label(frame_session, text="Nombre", font=("Arial", 13))
        label_operador.grid(row=2, column=1, padx=1)
        self.combo_operario = Combobox(frame_session, width=20, font=("Arial", 13), values=self.get_usuarios())
        self.combo_operario.bind("<<ComboboxSelected>>", self.selection_changed)
        self.combo_operario.grid(row=2, column=2, padx=1)

        # #INPUT CONTRASEÑA
        self.label_dni = Label(frame_session, text="Contraseña", font=("Arial", 13))
        self.label_dni.grid(row=3, column=1)
        self.input_dni = Entry(frame_session, show="*", width=20, font=("Arial", 13))
        self.input_dni.grid(row=3, column=2)
        # #INPUT PASSWORD INCORRECTO
        self.label_password_icorecto = Label(frame_session, text="", fg='red', font=("Arial", 13))
        self.label_password_icorecto.grid(row=4, column=2)

        # FRAME CALCULADORA
        frame_calculadora = Frame(frame_login, padx=20, pady=20, bg="pink")
        frame_calculadora.grid(row=4, column=1, sticky="nsew")

        btn_uno = Button(frame_calculadora, text="7", command=lambda:self.escribir_numeros(7), padx=23, pady=1, font=("Arial", 12))
        btn_uno.grid(row=4, column=1, padx=5, pady=5)
        btn_dos = Button(frame_calculadora, text="8", command=lambda:self.escribir_numeros(8),padx=23, pady=1, font=("Arial", 12))
        btn_dos.grid(row=4, column=2, padx=5, pady=5)
        btn_tres = Button(frame_calculadora, text="9", command=lambda:self.escribir_numeros(9), padx=23, pady=1, font=("Arial", 12))
        btn_tres.grid(row=4, column=3, padx=5, pady=5)
        btn_cuatro = Button(frame_calculadora, text="4", command=lambda:self.escribir_numeros(4), padx=23, pady=1, font=("Arial", 12))
        btn_cuatro.grid(row=5, column=1, padx=5, pady=5)
        btn_cinco = Button(frame_calculadora, text="5", command=lambda:self.escribir_numeros(5), padx=23, pady=1, font=("Arial", 12))
        btn_cinco.grid(row=5, column=2, padx=5, pady=5)
        btn_seis = Button(frame_calculadora, text="6", command=lambda:self.escribir_numeros(6), padx=23, pady=1, font=("Arial", 12))
        btn_seis.grid(row=5, column=3, padx=5, pady=5)
        btn_siete = Button(frame_calculadora, text="1", command=lambda:self.escribir_numeros(1), padx=23, pady=1, font=("Arial", 12))
        btn_siete.grid(row=6, column=1, padx=5, pady=5)
        btn_ocho = Button(frame_calculadora, text="2", command=lambda:self.escribir_numeros(2), padx=23, pady=1, font=("Arial", 12))
        btn_ocho.grid(row=6, column=2, padx=5, pady=5)
        btn_nueve = Button(frame_calculadora, text="3", command=lambda:self.escribir_numeros(3), padx=23, pady=1, font=("Arial", 12))
        btn_nueve.grid(row=6, column=3, padx=5, pady=5)
        btn_cero = Button(frame_calculadora, text="0", command=lambda:self.escribir_numeros(0), padx=23, pady=1, font=("Arial", 12))
        btn_cero.grid(row=7, column=1, padx=5, pady=5)
        btn_punto = Button(frame_calculadora, text="←", command=lambda:self.borrar_numero(), padx=20, pady=1, font=("Arial", 12, "bold"))
        btn_punto.grid(row=7, column=2, padx=5, pady=5)
        btn_igual = Button(frame_calculadora, text="✓", command=lambda:self.login(), padx=20, pady=1, font=("Arial", 12, "bold"), fg="white", bg="#097eeb")
        btn_igual.grid(row=7, column=3, padx=5, pady=5)

        self.interface_contador()


        self.frame_padre.mainloop()

    def interface_contador(self):
        # SEGUNDA COLUMNA
        # frame contador
        frame_contador = Frame( self.frame_padre, padx=0, pady=0, bg="pink")
        frame_contador.grid(row=1, column=2)
        # frame_contador.grid(row=1, column=2, sticky=W+E+N+S)

        frame_cronometro = Frame(frame_contador, padx=0, pady=0, bg="black")
        frame_cronometro.grid(row=1, column=1, rowspan=5, padx=10, pady=10)

        label_contador = Label(frame_cronometro, text="00:00:15", font=("Arial", 100),fg="white", bg="#00b248")
        label_contador.grid(row=1, column=1, rowspan=5, padx=50, pady=250)

        #BTN_COLORES:
        btn_azul = Button(frame_contador, text="", command=lambda:self.hide_label_error(), padx=30, pady=10, fg="white", bg="#00b248", font=("Arial", 20))
        btn_azul.grid(row=1, column=2, padx=10, pady=10)

        btn_verde = Button(frame_contador, text="", command=lambda:self.hide_label_error(), padx=30, pady=10, fg="white", bg="#0052b2", font=("Arial", 20))
        btn_verde.grid(row=2, column=2, padx=10, pady=10)

        btn_rojo = Button(frame_contador, text="", command=lambda:self.hide_label_error(), padx=30, pady=10, fg="white", bg="#ff0905", font=("Arial", 20))
        btn_rojo.grid(row=3, column=2, padx=10, pady=10)

        btn_naranja = Button(frame_contador, text="", command=lambda:self.hide_label_error(), padx=30, pady=10, fg="white", bg="#ffca0a", font=("Arial", 20))
        btn_naranja.grid(row=4, column=2, padx=10, pady=10)

        btn_morado = Button(frame_contador, text="", command=lambda:self.hide_label_error(), padx=30, pady=10, fg="white", bg="#7b00cb", font=("Arial", 20))
        btn_morado.grid(row=5, column=2, padx=10, pady=10)

    def escribir_numeros(self, numero):
        self.contador_numeros_dni = self.contador_numeros_dni + 1
        self.input_dni.insert(self.contador_numeros_dni, numero)

    def borrar_numero(self):
        tiene_numero = self.input_dni.get()
        if len(tiene_numero) > 0:
            self.input_dni.delete(len(tiene_numero)-1, END)
            self.contador_numeros_dni = self.contador_numeros_dni - 1

    def get_usuarios(self):
        print('get_usuarios')
        self.arreglo_usuarios = self.controller.get_usuarios()
        print(self.arreglo_usuarios)
        self.arreglo_usuarios = self.arreglo_usuarios + ('CON DNI',)
        return self.arreglo_usuarios
    
    def login(self):
        password = self.input_dni.get()
        nombre = self.combo_operario.get()
        self.nombre_operario = self.combo_operario.get()
        if self.nombre_operario == 'CON DNI':
            if len(password) > 0:
                usuario_con_dni = self.controller.crear_usuario_by_dni(password)
                if usuario_con_dni:
                    self.hide_label_error()
                    self.habilitar_btn_start()
                    self.input_dni.config(state=DISABLED)
                    self.combo_operario.config(state=DISABLED)
                else:
                    self.show_label_error('Digite un DNI válido')
            else:
                self.show_label_error('Digite un DNI válido')
        else:
            self.user = self.controller.login(nombre,password)
            if self.user != False:
                self.hide_label_error()
                self.habilitar_btn_start()
                self.input_dni.config(state=DISABLED)
                self.combo_operario.config(state=DISABLED)
                # self.controller.set_user(self.user)
                # self.controller.show_frame("Menu")
                print('login')
            else:
                self.show_label_error('La contraseña es incoreccta')
            
        print(self.user)

    def show_label_error(self, msg):
        self.label_password_icorecto.config(text=msg)
        self.label_password_icorecto.grid(row=4, column=2)
        # self.label_password_icorecto.grid_forget()
    
    def hide_label_error(self):
        self.label_password_icorecto.config(text="")
        self.label_password_icorecto.grid(row=4, column=2)
        # self.label_password_icorecto.grid_forget()
    def habilitar_btn_start(self):
        self.btn_start.config(state=NORMAL)

    def inahabilitar_btn_start(self):
        self.btn_start.config(state=DISABLED)

    def selection_changed(self, event):
        self.nombre_operario = self.combo_operario.get()
        if self.nombre_operario == 'CON DNI':
            self.label_dni.config(text="DNI")
            self.input_dni.config(show='')
        else:
            self.label_dni.config(text="Contraseña")
            self.input_dni.config(show='*')