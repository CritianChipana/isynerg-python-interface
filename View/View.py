from tkinter import *
from tkinter.ttk import Combobox
import os
import time
import datetime
from datetime import datetime, date
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


from Controller.Controller import Controller
from Model.Model import Model

class View(object):

    contador_numeros_dni = 0
    contador_productos_producidos = 0
    contador_piezas_malas = 0

    click_siguiente = True

    arreglo_usuarios = []
    user = ()
    maquina_id = 1
    indicador_color_btn = "verde"
    aux_indicador_color_btn = ""

    # hora_inicio = datetime.now()
    inicio_verde = datetime.now()
    inicio_azul = datetime.now()
    inicio_rojo = datetime.now()
    inicio_amarillo = datetime.now()
    inicio_morado = datetime.now()

    contador_verde = 0
    contador_azul = 0
    contador_rojo = 0
    contador_amarillo = 0
    contador_morado = 0

    aux_contador_verde = 0
    aux_contador_azul = 0
    aux_contador_rojo = 0
    aux_contador_amarillo = 0
    aux_contador_morado = 0

    click_btn_verde = 0
    click_btn_azul = 0
    click_btn_rojo = 0
    click_btn_amarillo = 0
    click_btn_morado = 0

    click_btn_color = 0

    click_btn_stop = False
    click_btn_start = False

    azul_horas = 0
    azul_minutos = 0
    azul_segundos = 0


    # variables para los graficos
    tamano_lineal = []
    nombres_lineal = [1,2,3,4,5,6,7]
    tamano_circular = []
    nombres_circular = ['','','','','']
    colores_circular = ['#00b248', '#0052b2', '#ff0905', '#ffca0a', '#7b00cb']
    explotar_circular = [0.01, 0.01, 0.01, 0.01, 0.01]


    def __init__(self):
        self.controller = Controller()
        self.model = Model()
        self.interface()
        # self.hora_inicio = datetime.now()
        self.INTERVALO_REFRESCO = 500  # En milisegundos


    def interface(self):
        self.raiz = Tk()
        # self.raiz.attributes('-fullscreen', True)
        self.raiz.geometry(str(self.raiz.winfo_screenwidth()) +'x' +  str(self.raiz.winfo_screenheight()) )
        # self.raiz.config(width="1200", height="700")
        # self.raiz.geometry("1200x800")
        self.raiz.config(bg="blue")
        self.raiz.columnconfigure(1, weight=1)
        self.raiz.rowconfigure(1, weight=1)

        self.frame_padre = Frame(self.raiz, padx=10, pady=10, bg="white")
        self.frame_padre.grid(row=1, column=1, sticky="nsew")

        self.frame_padre.rowconfigure(1, weight=1)
        self.frame_padre.columnconfigure(1, weight=1)
        self.frame_padre.columnconfigure(2, weight=1)

        ######################################### PRIMERA COLUMNA #########################################
        self.frame_login = Frame( self.frame_padre,bg="white", padx=10, pady=10)
        self.frame_login.grid(row=1, column=1, sticky="nsew")

        self.frame_login.rowconfigure(1, weight=1)
        self.frame_login.columnconfigure(1, weight=1)
        self.frame_login.rowconfigure(2, weight=1)

        frame_session = Frame(self.frame_login, padx=20, pady=20, bg="white")
        frame_session.grid(row=1, column=1, sticky="nsew")

        frame_session.rowconfigure(1, weight=1)
        frame_session.rowconfigure(2, weight=1)
        frame_session.rowconfigure(3, weight=1)
        frame_session.columnconfigure(1, weight=1)
        frame_session.columnconfigure(2, weight=1)


        # BTN START
        # state=DISABLED,
        self.btn_start = Button(frame_session, text="Start", command=lambda:self.start(), state=DISABLED, padx=100, pady=55, fg="white", bg="green", font=("Arial", 20))
        self.btn_start.grid(row=1, column=1, columnspan=4, padx=50, pady=50, sticky="nsew")

        # BTN STOP
        self.btn_stop = Button(frame_session, text="Stop",command=lambda:self.stop(), padx=100, pady=55, fg="white", bg="red", font=("Arial", 20))
        # self.btn_stop.grid(row=1, column=1, columnspan=4, padx=50, pady=50, sticky="nsew")


        #input NOMBRE
        label_operador = Label(frame_session, text="Nombre:", font=("Arial", 16))
        label_operador.grid(row=2, column=1, padx=1, sticky="w")
        self.combo_operario = Combobox(frame_session, width=20, font=("Arial", 16), values=self.get_usuarios())
        self.combo_operario.bind("<<ComboboxSelected>>", self.selection_changed)
        self.combo_operario.grid(row=2, column=2, padx=1, sticky="we", ipadx=10, ipady=5)

        # #INPUT CONTRASEÑA
        self.label_dni = Label(frame_session, text="Contraseña:", font=("Arial", 16))
        self.label_dni.grid(row=3, column=1, sticky="w")
        self.input_dni = Entry(frame_session, show="*", width=20, font=("Arial", 16))
        self.input_dni.grid(row=3, column=2, sticky="we", padx=10, ipady=5)
        # #INPUT PASSWORD INCORRECTO
        self.label_password_icorecto = Label(frame_session, text="", fg='red', font=("Arial", 13), bg="white")
        self.label_password_icorecto.grid(row=4, column=2, sticky="nsew", padx=10, ipady=5)

        # FRAME CALCULADORA
        frame_calculadora = Frame(self.frame_login, padx=20, pady=20, bg="white")
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

        # CRONOMETRO
        # self.variable_hora_actual = StringVar(self.raiz, value=self.obtener_tiempo_transcurrido_formateado())
        # self.etiqueta = Label(self.raiz, textvariable=self.variable_hora_actual, font=f"Consolas 60")
        # self.etiqueta.grid( row=1, column=1)

        self.interface_contador()
        self.interface_dashboard()
        self.interface_formulario()

        self.frame_padre.mainloop()

    def interface_contador(self):
        # SEGUNDA COLUMNA
        # frame contador
        self.frame_contador = Frame( self.frame_padre, padx=0, pady=0, bg="white")
        self.frame_contador.grid(row=1, column=2, sticky="nsew")
        # frame_contador.grid(row=1, column=2, sticky=W+E+N+S)
        self.frame_contador.rowconfigure(1, weight=1)
        self.frame_contador.columnconfigure(1, weight=1)
        self.frame_contador.columnconfigure(2, weight=1)

        ##* FRAME CONTADOR
        self.frame_cronometro = Frame(self.frame_contador, padx=0, pady=0, bg="#00b248")
        self.frame_cronometro.grid(row=1, column=1, rowspan=5, padx=10, pady=10, sticky="nsew")
        self.frame_cronometro.columnconfigure(1, weight=1)
        self.frame_cronometro.rowconfigure(1, weight=1)

        self.label_contador = Label(self.frame_cronometro, text="00:00:00", font=("Arial", 100),fg="white", bg="#00b248")
        self.label_contador.grid(row=1, column=1, rowspan=5, padx=50, sticky="nsew")

        # FRAME BTN CONTADOR
        self.frame_btn_cronometro = Frame(self.frame_contador, padx=0, pady=0, bg="white")
        self.frame_btn_cronometro.grid(row=1, column=2, rowspan=5, padx=10, pady=10, sticky="nsew")

        self.frame_btn_cronometro.rowconfigure(1, weight=1)
        self.frame_btn_cronometro.rowconfigure(2, weight=1)
        self.frame_btn_cronometro.rowconfigure(3, weight=1)
        self.frame_btn_cronometro.rowconfigure(4, weight=1)
        self.frame_btn_cronometro.rowconfigure(5, weight=1)
        self.frame_btn_cronometro.columnconfigure(1, weight=1)
        #BTN_COLORES:
        self.btn_azul = Button(self.frame_btn_cronometro, text="", command=lambda:self.open_azul('azul'), padx=30, pady=10, fg="white", bg="#0052b2", font=("Arial", 20))
        self.btn_azul.grid(row=1, column=1, padx=10, pady=10)

        self.btn_verde = Button(self.frame_btn_cronometro, text="", command=lambda:self.open_verde('verde'), padx=30, pady=10, fg="white", bg="#00b248", font=("Arial", 20))
        self.btn_verde.grid(row=2, column=1, padx=10, pady=10)

        self.btn_rojo = Button(self.frame_btn_cronometro, text="", command=lambda:self.open_rojo('rojo'), padx=30, pady=10, fg="white", bg="#ff0905", font=("Arial", 20))
        self.btn_rojo.grid(row=3, column=1, padx=10, pady=10)

        self.btn_amarillo = Button(self.frame_btn_cronometro, text="", command=lambda:self.open_amarillo('amarillo'), padx=30, pady=10, fg="white", bg="#ffca0a", font=("Arial", 20))
        self.btn_amarillo.grid(row=4, column=1, padx=10, pady=10)

        self.btn_morado = Button(self.frame_btn_cronometro, text="", command=lambda:self.open_morado('morado'), padx=30, pady=10, fg="white", bg="#7b00cb", font=("Arial", 20))
        self.btn_morado.grid(row=5, column=1, padx=10, pady=10)

    def interface_dashboard(self):
        self.frame_dashboard = Frame( self.frame_padre, padx=0, pady=0, bg="pink")
        # self.frame_dashboard.grid(row=1, column=1, sticky="nsew")
        self.frame_dashboard.rowconfigure(1, weight=1)
        self.frame_dashboard.rowconfigure(2, weight=10)
        self.frame_dashboard.columnconfigure(1, weight=1)

        self.frame_btn_dashboard = Frame(self.frame_dashboard, padx=0, pady=0, bg="black")
        self.frame_btn_dashboard.grid(row=1, column=1, padx=10, pady=9, sticky="nsew")

        #FRAME DASHBOARD DE LOS BOTONOES
        self.frame_btn_dashboard.rowconfigure(1, weight=1)
        self.frame_btn_dashboard.rowconfigure(2, weight=1)
        self.frame_btn_dashboard.columnconfigure(1, weight=1)
        self.frame_btn_dashboard.columnconfigure(2, weight=1)
        self.frame_btn_dashboard.columnconfigure(3, weight=1)

        self.btn_oee = Button(self.frame_btn_dashboard, text="OEE", padx=30, command=lambda:self.open_oee(), pady=13, font=("Arial", 9, "bold"))
        self.btn_oee.grid(row=1, column=1, padx=5, pady=5, sticky=W+E+N+S)

        self.btn_disponibilidad_maquina = Button(self.frame_btn_dashboard, text="Disponibilidad de\n Maquina", padx=30, command=lambda:self.open_disponibilidad_maquina(), pady=5, font=("Arial", 9, "bold"), justify="center")
        self.btn_disponibilidad_maquina.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

        self.btn_disponibilidad_materiales = Button(self.frame_btn_dashboard, text="Disponibilidad de\n Materiales", padx=30, command=lambda:self.open_disponibilidad_materiales(), pady=5, font=("Arial", 9, "bold"), justify="center")
        self.btn_disponibilidad_materiales.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

        self.btn_disponibilidad_operario = Button(self.frame_btn_dashboard, text="Disponibilidad de\n Operario", padx=30, command=lambda:self.open_disponibilidad_materiales (), pady=13, font=("Arial", 9, "bold"))
        self.btn_disponibilidad_operario.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

        self.btn_rendimiento = Button(self.frame_btn_dashboard, text="Rendimiento", padx=30, pady=5, command=lambda:self.open_rendimiento(), font=("Arial", 9, "bold"), justify="center")
        self.btn_rendimiento.grid(row=2, column=2, padx=5, pady=5, sticky=W+E+N+S)

        self.btn_calidad = Button(self.frame_btn_dashboard, text="Calidad", padx=30, command=lambda:self.open_calidad(), pady=5, font=("Arial", 9, "bold"), justify="center")
        self.btn_calidad.grid(row=2, column=3, padx=5, pady=5, sticky=W+E+N+S)

        # FRAME DE LOS GRAFICOS

        self.frame_dashboard_graficos = Frame(self.frame_dashboard, padx=0, pady=0, bg="white")
        self.frame_dashboard_graficos.grid(row=2, column=1, padx=10, pady=9, sticky="nsew")

        self.frame_dashboard_graficos.rowconfigure(1, weight=4)
        self.frame_dashboard_graficos.rowconfigure(2, weight=4)
        self.frame_dashboard_graficos.rowconfigure(3, weight=1)
        self.frame_dashboard_graficos.columnconfigure(1, weight=1)

        # GRAFICO LINEAL
        self.nombres_lineal = [1,2,3,4,5,6,7]
        self.tamano_lineal = ['0%', '20%', '40%', '20%', '80%', '20%', '12%']
        fig, self.axs_lineal = plt.subplots(dpi=80, figsize=(3,3), sharey=True)
        fig.suptitle('OEE')
        self.axs_lineal.plot(self.nombres_lineal, self.tamano_lineal, color='m')
        self.canvas_lineal = FigureCanvasTkAgg(fig, master=self.frame_dashboard_graficos)
        self.canvas_lineal.get_tk_widget().grid(row=1, column=1, sticky="nsew")
        self.canvas_lineal.draw()

        # GRAFICO DE CIRCULAR

        self.nombres_circular = ['','','','','']
        # nombres = ['Q Utilizada','Q Ociosa','Paradas Mtto','Parades LOG','Paradas rr']
        self.colores_circular = ['#00b248', '#0052b2', '#ff0905', '#ffca0a', '#7b00cb']
        self.tamano_circular = [20, 26, 30, 70, 10]
        self.explotar_circular = [0.01, 0.01, 0.01, 0.01, 0.01]

        fig, self.axs_circular = plt.subplots(dpi=100, figsize=(3,3), sharey=True)

        self.axs_circular.pie(self.tamano_circular, explode=self.explotar_circular, labels=self.nombres_circular ,colors=self.colores_circular, autopct='%1.1f%%', pctdistance=0.6, shadow=False, startangle=90, radius=0.7, labeldistance=0.3)
        self.axs_circular.axis('equal')

        self.canvas_circular = FigureCanvasTkAgg(fig, master=self.frame_dashboard_graficos)
        self.canvas_circular.get_tk_widget().grid(row=2, column=1, sticky="nsew")
        self.canvas_circular.draw()

        #FRAME LEYENDA
        self.frame_dashboard_graficos_leyenda = Frame(self.frame_dashboard_graficos, padx=0, pady=0, bg="white")
        self.frame_dashboard_graficos_leyenda.grid(row=3, column=1, padx=10, pady=9, sticky="nsew")

        self.label_color_leyenda_verde = Label(self.frame_dashboard_graficos_leyenda, text="", padx=5, pady=3, font=("Arial", 6, "bold"), bg="#00b248", fg="white")
        self.label_color_leyenda_verde.grid(row=1, column=1, padx=5, pady=3, sticky="nsew")

        self.label_letra_leyenda_verde = Label(self.frame_dashboard_graficos_leyenda, text="Q Utilizada", padx=5, pady=5, font=("Arial", 6, "bold"),  bg="white")
        self.label_letra_leyenda_verde.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

        self.label_color_leyenda_azul = Label(self.frame_dashboard_graficos_leyenda, text="", padx=5, pady=5, font=("Arial", 6, "bold"), bg="#0052b2", fg="white")
        self.label_color_leyenda_azul.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

        self.label_letra_leyenda_azul = Label(self.frame_dashboard_graficos_leyenda, text="Q Ociosa", padx=5, pady=5, font=("Arial", 6, "bold"),  bg="white")
        self.label_letra_leyenda_azul.grid(row=1, column=4, padx=5, pady=5, sticky="nsew")

        self.label_color_leyenda_rojo = Label(self.frame_dashboard_graficos_leyenda, text="", padx=5, pady=5, font=("Arial", 6, "bold"), bg="#ff0905", fg="white")
        self.label_color_leyenda_rojo.grid(row=1, column=5, padx=5, pady=5, sticky="nsew")

        self.label_letra_leyenda_rojo = Label(self.frame_dashboard_graficos_leyenda, text="Paradas MTTO", padx=5, pady=5, font=("Arial", 6, "bold"),  bg="white")
        self.label_letra_leyenda_rojo.grid(row=1, column=6, padx=5, pady=5, sticky="nsew")

        self.label_color_leyenda_amarillo = Label(self.frame_dashboard_graficos_leyenda, text="", padx=5, pady=5, font=("Arial", 6, "bold"), bg="#ffca0a", fg="white")
        self.label_color_leyenda_amarillo.grid(row=1, column=7, padx=5, pady=5, sticky="nsew")

        self.label_letra_leyenda_amarillo = Label(self.frame_dashboard_graficos_leyenda, text="Paradas LOG", padx=5, pady=5, font=("Arial", 6, "bold"),  bg="white")
        self.label_letra_leyenda_amarillo.grid(row=1, column=8, padx=5, pady=5, sticky="nsew")

        self.label_color_leyenda_morado = Label(self.frame_dashboard_graficos_leyenda, text="", padx=5, pady=5, font=("Arial", 6, "bold"), bg="#7b00cb", fg="white")
        self.label_color_leyenda_morado.grid(row=1, column=9, padx=5, pady=5, sticky="nsew")

        self.label_letra_leyenda_morado = Label(self.frame_dashboard_graficos_leyenda, text="Parada RR", padx=5, pady=5, font=("Arial", 6, "bold"),  bg="white")
        self.label_letra_leyenda_morado.grid(row=1, column=10, padx=5, pady=5, sticky="nsew")

    def interface_formulario(self):
        self.frame_formulario = Frame(self.frame_padre, padx=0, pady=0, bg="white")
        # self.frame_formulario.grid(row=1, column=1, padx=10, pady=9, sticky="nsew")

        self.label_formulario_produccion_real = Label(self.frame_formulario, text="Pruduccion real", padx=5, pady=5, font=("Arial", 12, "bold"),  bg="white")
        self.label_formulario_produccion_real.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

        self.input_produccion_real = Entry(self.frame_formulario, width=10, font=("Arial", 10, "bold"))
        self.input_produccion_real.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

        self.label_formulario_piezas_malas = Label(self.frame_formulario, text="Piezas Malas", padx=5, pady=5, font=("Arial", 10, "bold"),  bg="white")
        # self.label_formulario_piezas_malas.grid(row=3, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

        self.input_piezas_malas = Entry(self.frame_formulario, width=10, font=("Arial", 10, "bold"))
        # self.input_piezas_malas.grid(row=4, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

        btn_uno = Button(self.frame_formulario, text="7", command=lambda:self.escribir_numeros_produccion_total(7), padx=23, pady=1, font=("Arial", 12))
        btn_uno.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")
        btn_dos = Button(self.frame_formulario, text="8", command=lambda:self.escribir_numeros_produccion_total(8),padx=23, pady=1, font=("Arial", 12))
        btn_dos.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")
        btn_tres = Button(self.frame_formulario, text="9", command=lambda:self.escribir_numeros_produccion_total(9), padx=23, pady=1, font=("Arial", 12))
        btn_tres.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")
        btn_cuatro = Button(self.frame_formulario, text="4", command=lambda:self.escribir_numeros_produccion_total(4), padx=23, pady=1, font=("Arial", 12))
        btn_cuatro.grid(row=6, column=1, padx=5, pady=5, sticky="nsew")
        btn_cinco = Button(self.frame_formulario, text="5", command=lambda:self.escribir_numeros_produccion_total(5), padx=23, pady=1, font=("Arial", 12))
        btn_cinco.grid(row=6, column=2, padx=5, pady=5, sticky="nsew")
        btn_seis = Button(self.frame_formulario, text="6", command=lambda:self.escribir_numeros_produccion_total(6), padx=23, pady=1, font=("Arial", 12))
        btn_seis.grid(row=6, column=3, padx=5, pady=5, sticky="nsew")
        btn_siete = Button(self.frame_formulario, text="1", command=lambda:self.escribir_numeros_produccion_total(1), padx=23, pady=1, font=("Arial", 12))
        btn_siete.grid(row=7, column=1, padx=5, pady=5, sticky="nsew")
        btn_ocho = Button(self.frame_formulario, text="2", command=lambda:self.escribir_numeros_produccion_total(2), padx=23, pady=1, font=("Arial", 12))
        btn_ocho.grid(row=7, column=2, padx=5, pady=5, sticky="nsew")
        btn_nueve = Button(self.frame_formulario, text="3", command=lambda:self.escribir_numeros_produccion_total(3), padx=23, pady=1, font=("Arial", 12))
        btn_nueve.grid(row=7, column=3, padx=5, pady=5, sticky="nsew")
        btn_cero = Button(self.frame_formulario, text="0", command=lambda:self.escribir_numeros_produccion_total(0), padx=23, pady=1, font=("Arial", 12))
        btn_cero.grid(row=8, column=1, padx=5, pady=5, sticky="nsew")
        btn_punto = Button(self.frame_formulario, text="←", command=lambda:self.borrar_numero_produccion_real(), padx=20, pady=1, font=("Arial", 12, "bold"))
        btn_punto.grid(row=8, column=2, padx=5, pady=5, sticky="nsew")
        btn_igual = Button(self.frame_formulario, text="next", command=lambda:self.change_input_produccion_a_piezas(), padx=20, pady=1, font=("Arial", 12, "bold"), fg="white", bg="#097eeb")
        btn_igual.grid(row=8, column=3, padx=5, pady=5, sticky="nsew")

############################################################### INTERFECE ############################################################################

    def escribir_numeros(self, numero):
        self.contador_numeros_dni = self.contador_numeros_dni + 1
        self.input_dni.insert(self.contador_numeros_dni, numero)

    def borrar_numero(self):
        tiene_numero = self.input_dni.get()
        if len(tiene_numero) > 0:
            self.input_dni.delete(len(tiene_numero)-1, END)
            self.contador_numeros_dni = self.contador_numeros_dni - 1
    
    def escribir_numeros_produccion_total(self, numero):
        if self.click_siguiente:
            self.contador_productos_producidos = self.contador_productos_producidos + 1
            self.input_produccion_real.insert(self.contador_productos_producidos, numero)
        else: 
            self.contador_piezas_malas = self.contador_piezas_malas + 1
            self.input_piezas_malas.insert(self.contador_piezas_malas, numero)

    def borrar_numero_produccion_real(self):
        if self.click_siguiente:
            tiene_numero = self.input_produccion_real.get()

            if len(tiene_numero) > 0:
                self.input_produccion_real.delete(len(tiene_numero)-1, END)
                self.contador_productos_producidos = self.contador_productos_producidos - 1
        else:
            tiene_numero = self.input_piezas_malas.get()
            if len(tiene_numero) > 0:
                self.input_piezas_malas.delete(len(tiene_numero)-1, END)
                self.contador_piezas_malas = self.contador_piezas_malas - 1
    
    
    def change_input_produccion_a_piezas(self):
        if len(self.input_produccion_real.get()) > 0:
            self.click_siguiente = False
            self.label_formulario_produccion_real.grid_forget()
            self.input_produccion_real.grid_forget()
            
            self.label_formulario_piezas_malas.grid(row=3, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")
            self.input_piezas_malas.grid(row=4, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

            if len(self.input_piezas_malas.get()) > 0:
                print('guardar actividad')
                self.save_activiada_user()
                # limpiar usuario
                self.user = ()
                #limpiar inputs y contadores
                self.input_dni.config(state=NORMAL)
                self.combo_operario.config(state=NORMAL)
                self.contador_numeros_dni = 0
                self.contador_productos_producidos = 0
                self.contador_piezas_malas = 0
                # eliminar el contenido de los input
                self.input_dni.delete(0, END)
                self.input_produccion_real.delete(0, END)
                self.input_piezas_malas.delete(0, END)
                # eliminar el contenido del Combobox
                self.combo_operario.delete(0, END)
                # mostrar login
                self.frame_formulario.grid_forget()
                self.frame_login.grid(row=1, column=1, sticky="nsew")

                # MOSTRAR FORMULARIO AGAIN
                self.label_formulario_produccion_real.grid(row=3, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")
                self.input_produccion_real.grid(row=4, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")
                
                self.label_formulario_piezas_malas.grid_forget()
                self.input_piezas_malas.grid_forget()


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
                print('666666666666666666666')
                print(usuario_con_dni)
                print('666666666666666666666')
                if usuario_con_dni:
                    self.user = usuario_con_dni
                    self.hide_label_error()
                    self.controller.create_session(self.user[0])
                    self.habilitar_btn_start()
                    self.input_dni.config(state=DISABLED)
                    self.combo_operario.config(state=DISABLED)

                    #MOSTRAR EK DASHBOARD
                    self.frame_login.grid_forget()
                    self.frame_dashboard.grid(row=1, column=1, sticky="nsew")
                    print('start_timer -> ' + 'verde')
                    self.frame_cronometro.config(bg='#00b248')
                    self.label_contador.config(bg='#00b248')
                    self.indicador_color_btn = 'verde'
                else:
                    self.show_label_error('Digite un DNI válido')
            else:
                self.show_label_error('Digite un DNI válido')
        else:
            self.user = self.controller.login(nombre,password)
            if self.user != False:
                self.hide_label_error()
                self.controller.create_session(self.user[0])

                self.habilitar_btn_start()
                self.input_dni.config(state=DISABLED)
                self.combo_operario.config(state=DISABLED)

                #MOSTRAR EK DASHBOARD
                self.frame_login.grid_forget()
                self.frame_dashboard.grid(row=1, column=1, sticky="nsew")
                print('start_timer -> ' + 'verde')
                self.frame_cronometro.config(bg='#00b248')
                self.label_contador.config(bg='#00b248')
                self.indicador_color_btn = 'verde'
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
        self.btn_start.grid_forget()
        self.btn_azul.config(state=NORMAL)
        self.btn_verde.config(state=NORMAL)
        self.btn_rojo.config(state=NORMAL)
        self.btn_amarillo.config(state=NORMAL)
        self.btn_morado.config(state=NORMAL)
        self.click_btn_start = True
        self.btn_stop.grid(row=1, column=1, columnspan=4, padx=50, pady=50, sticky="nsew")

        self.refrescar_tiempo_transcurrido()

    def segundos_a_segundos_minutos_y_horas(self, segundos):
        horas = int(segundos / 60 / 60)
        segundos -= horas*60*60
        minutos = int(segundos/60)
        segundos -= minutos*60
        return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

    def obtener_tiempo_transcurrido_formateado(self):
        print('====================================================')
        print('contador verde: ' + str(self.contador_verde))
        print('contador azul: ' + str(self.contador_azul))
        print('contador rojo: ' + str(self.contador_rojo))
        print('contador amarillo: ' + str(self.contador_amarillo))
        print('contador morado: ' + str(self.contador_morado))
        print('====================================================')

        if self.indicador_color_btn == 'verde':
            print('verde')
            if (self.contador_verde == 0):
                self.inicio_verde = datetime.now()
            if  self.click_btn_verde > 1:
                ahora = datetime.strptime('00:00:00', '%H:%M:%S')
                ahora2 = datetime.strptime(self.aux_contador_verde, '%H:%M:%S')
                segundos_transcurridos = (datetime.now() - self.inicio_verde + (ahora2 - ahora)).total_seconds()
                tiempo_trancurrido = self.segundos_a_segundos_minutos_y_horas(int(segundos_transcurridos))
                self.contador_verde = tiempo_trancurrido
                return tiempo_trancurrido
            else:
                segundos_transcurridos= (datetime.now() - self.inicio_verde).total_seconds()
                tiempo_trancurrido = self.segundos_a_segundos_minutos_y_horas(int(segundos_transcurridos))
                self.contador_verde = tiempo_trancurrido
                return tiempo_trancurrido
        if self.indicador_color_btn == 'azul':
            print('azul')
            if (self.contador_azul == 0):
                self.inicio_azul = datetime.now()
            if  self.click_btn_azul > 1:
                ahora = datetime.strptime('00:00:00', '%H:%M:%S')
                ahora2 = datetime.strptime(self.aux_contador_azul, '%H:%M:%S')
                segundos_transcurridos = (datetime.now() - self.inicio_azul + (ahora2 - ahora)).total_seconds()
                tiempo_trancurrido = self.segundos_a_segundos_minutos_y_horas(int(segundos_transcurridos))
                self.contador_azul = tiempo_trancurrido
                return tiempo_trancurrido
            else:
                segundos_transcurridos= (datetime.now() - self.inicio_azul).total_seconds()
                tiempo_trancurrido = self.segundos_a_segundos_minutos_y_horas(int(segundos_transcurridos))
                self.contador_azul = tiempo_trancurrido
                return tiempo_trancurrido
        if self.indicador_color_btn == 'rojo':
            print('rojo')
            if (self.contador_rojo == 0):
                self.inicio_rojo = datetime.now()
            if  self.click_btn_rojo > 1:
                ahora = datetime.strptime('00:00:00', '%H:%M:%S')
                ahora2 = datetime.strptime(self.aux_contador_rojo, '%H:%M:%S')
                segundos_transcurridos = (datetime.now() - self.inicio_rojo + (ahora2 - ahora)).total_seconds()
                tiempo_trancurrido = self.segundos_a_segundos_minutos_y_horas(int(segundos_transcurridos))
                self.contador_rojo = tiempo_trancurrido
                return tiempo_trancurrido
            else:
                segundos_transcurridos= (datetime.now() - self.inicio_rojo).total_seconds()
                tiempo_trancurrido = self.segundos_a_segundos_minutos_y_horas(int(segundos_transcurridos))
                self.contador_rojo = tiempo_trancurrido
                return tiempo_trancurrido
        if self.indicador_color_btn == 'amarillo':
            print('amarillo')
            if (self.contador_amarillo == 0):
                self.inicio_amarillo = datetime.now()

            if  self.click_btn_amarillo > 1:
                ahora = datetime.strptime('00:00:00', '%H:%M:%S')
                ahora2 = datetime.strptime(self.aux_contador_amarillo, '%H:%M:%S')
                segundos_transcurridos = (datetime.now() - self.inicio_amarillo + (ahora2 - ahora)).total_seconds()
                tiempo_trancurrido = self.segundos_a_segundos_minutos_y_horas(int(segundos_transcurridos))
                self.contador_amarillo = tiempo_trancurrido
                return tiempo_trancurrido
            else:
                segundos_transcurridos= (datetime.now() - self.inicio_amarillo).total_seconds()
                tiempo_trancurrido = self.segundos_a_segundos_minutos_y_horas(int(segundos_transcurridos))
                self.contador_amarillo = tiempo_trancurrido
                return tiempo_trancurrido
        if self.indicador_color_btn == 'morado':
            print('morado')
            if (self.contador_morado == 0):
                self.inicio_morado = datetime.now()

            if  self.click_btn_morado > 1:
                ahora = datetime.strptime('00:00:00', '%H:%M:%S')
                ahora2 = datetime.strptime(self.aux_contador_morado, '%H:%M:%S')
                segundos_transcurridos = (datetime.now() - self.inicio_morado + (ahora2 - ahora)).total_seconds()
                tiempo_trancurrido = self.segundos_a_segundos_minutos_y_horas(int(segundos_transcurridos))
                self.contador_morado = tiempo_trancurrido
                return tiempo_trancurrido
            else:
                segundos_transcurridos = (datetime.now() - self.inicio_morado).total_seconds()
                tiempo_trancurrido = self.segundos_a_segundos_minutos_y_horas(int(segundos_transcurridos))
                self.contador_morado = tiempo_trancurrido
                return tiempo_trancurrido

    def refrescar_tiempo_transcurrido(self):
        print("Refrescando!")
        nueva_hora = self.obtener_tiempo_transcurrido_formateado()
        print(nueva_hora)
        self.label_contador.config(text=nueva_hora)
        
        tarea = self.raiz.after(500, self.refrescar_tiempo_transcurrido)
        if self.click_btn_stop == True :
            self.raiz.after_cancel(tarea)
            self.mostrar_contador_con_color()




    def open_verde(self, verde):
        # open login
        if self.user == ():
            self.frame_dashboard.grid_forget()
            self.frame_login.grid(row=1, column=1, sticky="nsew")

        print('start_timer -> ' + verde)

        if self.user == () or self.click_btn_color == 0:
            self.frame_cronometro.config(bg='#00b248')
            self.label_contador.config(bg='#00b248')

        self.indicador_color_btn = verde

        if self.user != ():

            self.click_btn_color = self.click_btn_color + 1

            if self.click_btn_color == 1:
                self.refrescar_tiempo_transcurrido()
                self.aux_indicador_color_btn = verde
            if self.click_btn_color == 2:
                self.stop()
                self.frame_dashboard.grid_forget()
    
    def open_azul(self, azul):

        # #open dashboard
        self.frame_login.grid_forget()
        self.frame_dashboard.grid(row=1, column=1, sticky="nsew")

        print('start_timer -> ' + azul)
        if self.user == () or self.click_btn_color == 0:
            self.frame_cronometro.config(bg='#0052b2')
            self.label_contador.config(bg='#0052b2')
        
        self.indicador_color_btn = azul

        if self.user != ():
            self.click_btn_color = self.click_btn_color + 1
            if self.click_btn_color == 1:
                self.refrescar_tiempo_transcurrido()
                self.aux_indicador_color_btn = azul
            if self.click_btn_color == 2:
                self.stop()
                # self.mostrar_contador_con_color()
                self.frame_dashboard.grid_forget()

    
    def open_rojo(self, rojo):

        #open dashboard
        self.frame_login.grid_forget()
        self.frame_dashboard.grid(row=1, column=1, sticky="nsew")

        print('start_timer -> ' + rojo)
        if self.user == () or self.click_btn_color == 0:
            self.frame_cronometro.config(bg='#ff0905')
            self.label_contador.config(bg='#ff0905')

        self.indicador_color_btn = rojo

        if self.user != ():
            self.click_btn_color = self.click_btn_color + 1
            if self.click_btn_color == 1:
                self.refrescar_tiempo_transcurrido()
                self.aux_indicador_color_btn = rojo
            if self.click_btn_color == 2:
                self.stop()
                self.frame_dashboard.grid_forget()

    
    def open_amarillo(self, amarillo):

        #open dashboard
        self.frame_login.grid_forget()
        self.frame_dashboard.grid(row=1, column=1, sticky="nsew")

        print('start_timer -> ' + amarillo)
        if self.user == () or self.click_btn_color == 0:
            self.frame_cronometro.config(bg='#ffca0a')
            self.label_contador.config(bg='#ffca0a')

        self.indicador_color_btn = amarillo

        if self.user != ():
            self.click_btn_color = self.click_btn_color + 1
            if self.click_btn_color == 1:
                self.refrescar_tiempo_transcurrido()
                self.aux_indicador_color_btn = amarillo
            if self.click_btn_color == 2:
                self.stop()
                self.frame_dashboard.grid_forget()

    def open_morado(self, morado):
        #open dashboard
        self.frame_login.grid_forget()
        self.frame_dashboard.grid(row=1, column=1, sticky="nsew")

        print('start_timer -> ' + morado)
        if self.user == () or self.click_btn_color == 0:
            self.frame_cronometro.config(bg='#7b00cb')
            self.label_contador.config(bg='#7b00cb')

        self.indicador_color_btn = morado

        if self.user != ():
            self.click_btn_color = self.click_btn_color + 1
            if self.click_btn_color == 1:
                self.refrescar_tiempo_transcurrido()
                self.aux_indicador_color_btn = morado
            if self.click_btn_color == 2:
                self.stop()
                self.frame_dashboard.grid_forget()

    def mostrar_contador_con_color(self):
        if self.aux_indicador_color_btn == 'verde':

            self.frame_cronometro.config(bg='#00b248')
            self.label_contador.config(bg='#00b248')
            self.label_contador.config(text=self.contador_verde)
        elif self.aux_indicador_color_btn == 'azul':

            self.frame_cronometro.config(bg='#0052b2')
            self.label_contador.config(bg='#0052b2')
            self.label_contador.config(text=self.contador_azul)

        elif self.aux_indicador_color_btn == 'rojo':

            self.frame_cronometro.config(bg='#ff0905')
            self.label_contador.config(bg='#ff0905')
            self.label_contador.config(text=self.contador_rojo)

        elif self.aux_indicador_color_btn == 'amarillo':

            self.frame_cronometro.config(bg='#ffca0a')
            self.label_contador.config(bg='#ffca0a')
            self.label_contador.config(text=self.contador_amarillo)

        elif self.aux_indicador_color_btn == 'morado':

            self.frame_cronometro.config(bg='#7b00cb')
            self.label_contador.config(bg='#7b00cb')
            self.label_contador.config(text=self.contador_morado)


    def stop(self):
        print('stop_timer')
        self.click_btn_stop = True
        self.frame_dashboard.grid_forget()
        self.frame_formulario.grid(row=1, column=1, padx=10, pady=9, sticky="nsew")

    
    def save_activiada_user(self):
        if self.contador_verde != 0:
            segundos_transcurridos_verde = (datetime.strptime(self.contador_verde, '%H:%M:%S') - datetime.strptime('00:00:00', '%H:%M:%S')).total_seconds()
        else:
            segundos_transcurridos_verde = 0
        
        if self.contador_azul != 0:
            segundos_transcurridos_azul = (datetime.strptime(self.contador_azul, '%H:%M:%S') - datetime.strptime('00:00:00', '%H:%M:%S')).total_seconds()
        else:
            segundos_transcurridos_azul = 0

        if self.contador_rojo != 0:
            segundos_transcurridos_rojo = (datetime.strptime(self.contador_rojo, '%H:%M:%S') - datetime.strptime('00:00:00', '%H:%M:%S')).total_seconds()
        else:
            segundos_transcurridos_rojo = 0
        
        if self.contador_morado != 0:
            segundos_transcurridos_morado = (datetime.strptime(self.contador_morado, '%H:%M:%S') - datetime.strptime('00:00:00', '%H:%M:%S')).total_seconds()
        else:
            segundos_transcurridos_morado = 0

        if self.contador_amarillo != 0:
            segundos_transcurridos_amarillo = (datetime.strptime(self.contador_amarillo, '%H:%M:%S') - datetime.strptime('00:00:00', '%H:%M:%S')).total_seconds()
        else:
            segundos_transcurridos_amarillo = 0

        data = {
            'verde': int(segundos_transcurridos_verde),
            'azul': int(segundos_transcurridos_azul),
            'amarillo': int(segundos_transcurridos_amarillo),
            'rojo': int(segundos_transcurridos_rojo),
            'morado': int(segundos_transcurridos_morado),
            'produccion_real' : int(self.input_produccion_real.get()),
            'piezas_malas' : int(self.input_piezas_malas.get())
        }

        print(data)
        response =  self.controller.crear_actividad_user(self.user[0], self.maquina_id, data)
        if response:
            self.label_contador.config(text="00:00:00")
            self.contador_verde = 0
            self.contador_azul = 0
            self.contador_rojo = 0
            self.contador_amarillo = 0
            self.contador_morado = 0
            self.click_btn_verde = 0
            self.click_btn_azul = 0
            self.click_btn_rojo = 0
            self.click_btn_amarillo = 0
            self.click_btn_morado = 0
            self.indicador_color_btn = 'verde'
            self.aux_contador_verde = ''
            self.aux_contador_azul = ''
            self.aux_contador_rojo = ''
            self.aux_contador_amarillo = ''
            self.aux_contador_morado = ''
            self.click_btn_stop = False
            self.click_btn_start = False
            self.btn_stop.grid_forget()
            self.btn_start.grid(row=1, column=1, columnspan=4, padx=50, pady=50, sticky="nsew")
            self.frame_cronometro.config(bg='#00b248')
            self.label_contador.config(bg='#00b248')
            self.click_btn_color = 0
            self.frame_login.grid(row=1, column=1, sticky="nsew")
            self.click_siguiente = True

        else :
            print('Error al guardar la actividad de usuario')
        # self.raiz.after_(self.refrescar_tiempo_transcurrido)


    def open_oee(self):
        self.axs_lineal.clear()
        self.tamano_lineal = self.controller.dashboard_capacidad_oee(self.maquina_id)
        print(self.tamano_lineal)
        self.axs_lineal.plot(self.nombres_lineal,self.tamano_lineal, color='m')
        self.canvas_lineal.draw()
        print('oee')
        # print('semana pasada: ',semana_anterior)

        # self.controller.get_actividad_user_siete_ultimos_dias(self.maquina_id)

    def open_disponibilidad_maquina(self):
        self.axs_lineal.clear()
        self.tamano_lineal = self.controller.dashboard_capacidad_disponibilidad(self.maquina_id)
        print(self.tamano_lineal)
        self.axs_lineal.plot(self.nombres_lineal,self.tamano_lineal, color='m')
        self.canvas_lineal.draw()
        print('open_rendimiento')
        print('open_disponibilidad_maquina')

    def open_disponibilidad_materiales(self):
        self.canvas_lineal.draw()
        print('open_disponibilidad_materiales')

    def open_disponibilidad_materiales(self):
        print('open_disponibilidad_materiales')

    def open_rendimiento(self):
        self.axs_lineal.clear()
        self.tamano_lineal = self.controller.dashboard_rendimiento(self.maquina_id)
        print(self.tamano_lineal)
        self.axs_lineal.plot(self.nombres_lineal,self.tamano_lineal, color='m')
        self.canvas_lineal.draw()
        print('open_rendimiento')

    def open_calidad(self):
        self.axs_lineal.clear()
        self.tamano_lineal = self.controller.dashboard_calidad(self.maquina_id)
        print(self.tamano_lineal)
        self.axs_lineal.plot(self.nombres_lineal,self.tamano_lineal, color='m')
        self.canvas_lineal.draw()
        print('open calidad')

