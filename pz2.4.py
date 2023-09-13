import matplotlib.pyplot as plt #Импортируем библиотеку
import numpy as np

X = [58] #Координаты точек по X
Y = [111] #Координаты точек по Y
plt.scatter(X, Y) #отрисовываем точки

plt.xlim(0,300) #Ограничения по Х
plt.ylim(0,300) #Ограничения по Y
plt.yticks(range(0, 300, 20))
plt.xticks(range(0, 300, 20))


plt.title('График Васев Киселев') #название графика
plt.xlabel('Значение Х') #подпись оси
plt.ylabel('Значение Y') #подпись оси
plt.plot([95, 0], [0, 290]) #наклонная

plt.axhline(y=111, linestyle='--', color='green') #пунктирная
plt.grid()
plt.arrow(1, 1, 30, 30, width=3, color='red') #Координаты стрелки
plt.show() #отрисовываем весь график

