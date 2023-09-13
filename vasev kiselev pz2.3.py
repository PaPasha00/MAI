from scipy.optimize import linprog
import time
start = time.time()
c = [-30,-1] #Функция цели
A_ub = [[90,5]] #'1'
b_ub = [10000]#'1'
A_eq = [[3,-1]] #'2'
b_eq = [0] #'2'
print (linprog(c, A_ub, b_ub, A_eq, b_eq))
stop = time.time()
print ("Время :")
print(stop - start)