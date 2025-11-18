import matplotlib.pyplot as plt

colores = ["#B20707", "#3e2f21", "#101910", "#30F00F"]

clasificacion = ['A','B','C','D','E']
porcentaje = [100,250,340,479,500]

plt.figure(figsize=(4,5))
plt.bar(clasificacion,porcentaje, color=colores)
plt.title('grafica con rodrigo ^_^')
plt.xlabel(clasificacion)
plt.ylabel(porcentaje)
plt.show()

x = [2,34,57,78,89]
y = [3,45,57,80,45]

plt.plot(x,y)
plt.title('grafica ¬_¬ ')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.grid(True)
plt.show()

