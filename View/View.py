from tkinter import *
from tkinter.ttk import Combobox
import os
import time
from datetime import datetime


from Controller.Controller import Controller
from Model.Model import Model

class View(object):

    contador_numeros_dni = 0
    arreglo_usuarios = []
    user = ()

    azul_horas = 0
    azul_minutos = 0
    azul_segundos = 0


    def __init__(self):
        self.controller = Controller()
        self.model = Model()
        self.interface()
        # self.hora_inicio = datetime.now()
        self.INTERVALO_REFRESCO = 500  # En milisegundos


    def interface(self):
        self.raiz = Tk()
        # raiz.attributes('-fullscreen', True)
        self.raiz.geometry(str(self.raiz.winfo_screenwidth()) +'x' +  str(self.raiz.winfo_screenheight()) )
        # raiz.config(width="1200", height="800")
        # self.raiz.geometry("1200x800")
        self.raiz.config(bg="blue")
        self.raiz.columnconfigure(1, weight=1)
        self.raiz.rowconfigure(1, weight=1)

        self.frame_padre = Frame(self.raiz, padx=10, pady=10, bg="yellow")
        self.frame_padre.grid(row=1, column=1, sticky="nsew")

        self.frame_padre.rowconfigure(1, weight=1)
        self.frame_padre.columnconfigure(1, weight=1)
        self.frame_padre.columnconfigure(2, weight=1)

        ######################################### PRIMERA COLUMNA #########################################
        self.frame_login = Frame( self.frame_padre,bg="purple", padx=10, pady=10)
        self.frame_login.grid(row=1, column=1, sticky="nsew")

        self.frame_login.rowconfigure(1, weight=1)
        self.frame_login.columnconfigure(1, weight=1)
        self.frame_login.rowconfigure(2, weight=1)

        frame_session = Frame(self.frame_login, padx=20, pady=20, bg="red")
        frame_session.grid(row=1, column=1, sticky="nsew")

        frame_session.rowconfigure(1, weight=1)
        frame_session.rowconfigure(2, weight=1)
        frame_session.rowconfigure(3, weight=1)
        frame_session.columnconfigure(1, weight=1)
        frame_session.columnconfigure(2, weight=1)


        # btn_start = Button(frame_login, text="Start", padx=100, pady=55, fg="white", bg="green", font=("Arial", 20), command=self.hola)
        # state=DISABLED,
        self.btn_start = Button(frame_session, text="Start",command=lambda:self.start(), padx=100, pady=55, fg="white", bg="green", font=("Arial", 20))
        self.btn_start.grid(row=1, column=1, columnspan=4, padx=50, pady=50, sticky="nsew")



        #input NOMBRE
        label_operador = Label(frame_session, text="Nombre:", font=("Arial", 16))
        label_operador.grid(row=2, column=1, padx=1, sticky="w")
        self.combo_operario = Combobox(frame_session, width=20, font=("Arial", 16), values=self.get_usuarios())
        self.combo_operario.bind("<<ComboboxSelected>>", self.selection_changed)
        self.combo_operario.grid(row=2, column=2, padx=1, sticky="we", padx=10, ipady=5)

        # #INPUT CONTRASEÑA
        self.label_dni = Label(frame_session, text="Contraseña:", font=("Arial", 16))
        self.label_dni.grid(row=3, column=1, sticky="w")
        self.input_dni = Entry(frame_session, show="*", width=20, font=("Arial", 16))
        self.input_dni.grid(row=3, column=2, sticky="we", padx=10, ipady=5)
        # #INPUT PASSWORD INCORRECTO
        self.label_password_icorecto = Label(frame_session, text="", fg='red', font=("Arial", 13))
        self.label_password_icorecto.grid(row=4, column=2, sticky="nsew", padx=10, ipady=5)

        # FRAME CALCULADORA
        frame_calculadora = Frame(self.frame_login, padx=20, pady=20, bg="pink")
        frame_calculadora.grid(row=2, column=1, sticky="nsew")

        frame_calculadora.rowconfigure(1, weight=1)
        frame_calculadora.rowconfigure(2, weight=1)
        frame_calculadora.rowconfigure(3, weight=1)
        frame_calculadora.rowconfigure(4, weight=1)

        frame_calculadora.columnconfigure(1, weight=1)
        frame_calculadora.columnconfigure(2, weight=1)
        frame_calculadora.columnconfigure(3, weight=1)

        btn_uno = Button(frame_calculadora, text="7", command=lambda:self.escribir_numeros(7), padx=23, pady=1, font=("Arial", 12))
        btn_uno.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        btn_dos = Button(frame_calculadora, text="8", command=lambda:self.escribir_numeros(8),padx=23, pady=1, font=("Arial", 12))
        btn_dos.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
        btn_tres = Button(frame_calculadora, text="9", command=lambda:self.escribir_numeros(9), padx=23, pady=1, font=("Arial", 12))
        btn_tres.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")
        btn_cuatro = Button(frame_calculadora, text="4", command=lambda:self.escribir_numeros(4), padx=23, pady=1, font=("Arial", 12))
        btn_cuatro.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
        btn_cinco = Button(frame_calculadora, text="5", command=lambda:self.escribir_numeros(5), padx=23, pady=1, font=("Arial", 12))
        btn_cinco.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
        btn_seis = Button(frame_calculadora, text="6", command=lambda:self.escribir_numeros(6), padx=23, pady=1, font=("Arial", 12))
        btn_seis.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")
        btn_siete = Button(frame_calculadora, text="1", command=lambda:self.escribir_numeros(1), padx=23, pady=1, font=("Arial", 12))
        btn_siete.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
        btn_ocho = Button(frame_calculadora, text="2", command=lambda:self.escribir_numeros(2), padx=23, pady=1, font=("Arial", 12))
        btn_ocho.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
        btn_nueve = Button(frame_calculadora, text="3", command=lambda:self.escribir_numeros(3), padx=23, pady=1, font=("Arial", 12))
        btn_nueve.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")
        btn_cero = Button(frame_calculadora, text="0", command=lambda:self.escribir_numeros(0), padx=23, pady=1, font=("Arial", 12))
        btn_cero.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
        btn_punto = Button(frame_calculadora, text="←", command=lambda:self.borrar_numero(), padx=20, pady=1, font=("Arial", 12, "bold"))
        btn_punto.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
        btn_igual = Button(frame_calculadora, text="✓", command=lambda:self.login(), padx=20, pady=1, font=("Arial", 12, "bold"), fg="white", bg="#097eeb")
        btn_igual.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

        # cronometro
        self.variable_hora_actual = StringVar(self.raiz, value=self.obtener_tiempo_transcurrido_formateado())
        self.raiz.etiqueta = Label(self.raiz, textvariable=self.variable_hora_actual, font=f"Consolas 60")
        self.raiz.etiqueta.grid( row=1, column=1)

        self.interface_contador()


        self.frame_padre.mainloop()

    def interface_contador(self):
        # SEGUNDA COLUMNA
        # frame contador
        self.frame_contador = Frame( self.frame_padre, padx=0, pady=0, bg="pink")
        self.frame_contador.grid(row=1, column=2, sticky="nsew")
        # frame_contador.grid(row=1, column=2, sticky=W+E+N+S)
        self.frame_contador.rowconfigure(1, weight=1)
        self.frame_contador.columnconfigure(1, weight=1)
        self.frame_contador.columnconfigure(2, weight=1)

        ##* FRAME CONTADOR
        frame_cronometro = Frame(self.frame_contador, padx=0, pady=0, bg="black")
        frame_cronometro.grid(row=1, column=1, rowspan=5, padx=10, pady=10, sticky="nsew")
        frame_cronometro.columnconfigure(1, weight=1)
        frame_cronometro.rowconfigure(1, weight=1)

        self.label_contador = Label(frame_cronometro, text="00:00:00", font=("Arial", 100),fg="white", bg="#00b248")
        self.label_contador.grid(row=1, column=1, rowspan=5, padx=50, sticky="nsew")

        # FRAME BTN CONTADOR
        self.frame_btn_cronometro = Frame(self.frame_contador, padx=0, pady=0, bg="#097eeb")
        self.frame_btn_cronometro.grid(row=1, column=2, rowspan=5, padx=10, pady=10, sticky="nsew")

        self.frame_btn_cronometro.rowconfigure(1, weight=1)
        self.frame_btn_cronometro.rowconfigure(2, weight=1)
        self.frame_btn_cronometro.rowconfigure(3, weight=1)
        self.frame_btn_cronometro.rowconfigure(4, weight=1)
        self.frame_btn_cronometro.rowconfigure(5, weight=1)
        self.frame_btn_cronometro.columnconfigure(1, weight=1)
        #BTN_COLORES:
        btn_azul = Button(self.frame_btn_cronometro, text="", command=lambda:self.hide_label_error(), padx=30, pady=10, fg="white", bg="#00b248", font=("Arial", 20))
        btn_azul.grid(row=1, column=1, padx=10, pady=10)

        btn_verde = Button(self.frame_btn_cronometro, text="", command=lambda:self.hide_label_error(), padx=30, pady=10, fg="white", bg="#0052b2", font=("Arial", 20))
        btn_verde.grid(row=2, column=1, padx=10, pady=10)

        btn_rojo = Button(self.frame_btn_cronometro, text="", command=lambda:self.hide_label_error(), padx=30, pady=10, fg="white", bg="#ff0905", font=("Arial", 20))
        btn_rojo.grid(row=3, column=1, padx=10, pady=10)

        btn_naranja = Button(self.frame_btn_cronometro, text="", command=lambda:self.hide_label_error(), padx=30, pady=10, fg="white", bg="#ffca0a", font=("Arial", 20))
        btn_naranja.grid(row=4, column=1, padx=10, pady=10)

        btn_morado = Button(self.frame_btn_cronometro, text="", command=lambda:self.hide_label_error(), padx=30, pady=10, fg="white", bg="#7b00cb", font=("Arial", 20))
        btn_morado.grid(row=5, column=1, padx=10, pady=10)

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

    def start(self):
        # for hora in range(24):
        #     for minuto in range(60):
        #         for segundo in range(60):
        #             os.system('cls')
        #             print(f'{hora}:{minuto}:{segundo}')
        #             hora_completa = str(hora) + ':' + str(minuto) + ':' + str(segundo)
        #             self.label_contador.config(text='hola')
        #             self.azul_segundos = segundo
        #             time.sleep(1)
        self.label_contador.config(text='hola')
        self.refrescar_tiempo_transcurrido()

    def segundos_a_segundos_minutos_y_horas(self, segundos):
        horas = int(segundos / 60 / 60)
        segundos -= horas*60*60
        minutos = int(segundos/60)
        segundos -= minutos*60
        return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

    def obtener_tiempo_transcurrido_formateado(self):
        hora_inicio = datetime.now()
        segundos_transcurridos= (datetime.now() - hora_inicio).total_seconds()
        return self.segundos_a_segundos_minutos_y_horas(int(segundos_transcurridos))


    def refrescar_tiempo_transcurrido(self):
        print("Refrescando!")
        self.variable_hora_actual.set(self.obtener_tiempo_transcurrido_formateado())
        # self.raiz.after(self.INTERVALO_REFRESCO, self.refrescar_tiempo_transcurrido)
        self.raiz.after(500, self.refrescar_tiempo_transcurrido)
