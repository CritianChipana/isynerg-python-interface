
# import matplotlib.pyplot as plt
# import numpy as np
  
# x = np.linspace(0, 10*np.pi, 100)
# y = np.sin(x)
  
# plt.ion()
# fig = plt.figure()
# ax = fig.add_subplot(111)
# line1, = ax.plot(x, y, 'b-')
  
# for phase in np.linspace(0, 10*np.pi, 100):
#     line1.set_ydata(np.sin(0.5 * x + phase))
#     fig.canvas.draw()
#     fig.canvas.flush_events()

# from datetime import datetime

# segundos_transcurridos_verde = (datetime.strptime('00:00:20', '%H:%M:%S') - datetime.strptime('00:00:00', '%H:%M:%S')).total_seconds()
# segundos_transcurridos_amarillo = (datetime.strptime('00:00:10', '%H:%M:%S') - datetime.strptime('00:00:00', '%H:%M:%S')).total_seconds()
# segundos_total_colores = segundos_transcurridos_verde + segundos_transcurridos_amarillo

# hora_actual = (datetime.now().time().strftime("%H:%M:%S"))
# segundos_transcurridos_azul = int((datetime.strptime(hora_actual, '%H:%M:%S') - datetime.strptime('00:00:00', '%H:%M:%S')).total_seconds())
# azul2 = (segundos_transcurridos_azul - segundos_total_colores)
# print('Hora actual: ' + hora_actual)
# print('Segundos del azul: ' + str(segundos_transcurridos_azul))
# print('Segundos del azul calculado: ' + str(azul2))
# print('Segundos del verde: ' + str(segundos_transcurridos_verde))
# print('Segundos del amarillo: ' + str(segundos_transcurridos_amarillo))


from datetime import datetime

date = datetime.now()
print("Before Formatting")
print("DateTime:", date)
print("Date:", date.date())
print("Time:", date.time())
print("After Formatting")
print("DateTime:", date.strftime("%d %B, %Y %H:%M:%S")) # DD Month, YYYY HH:MM:SS
print("Date:", date.date().strftime("%d %B, %Y")) # DD Month, YYYY
print("Time:", date.time().strftime("%H:%M:%S")) # HH:MM:SS
