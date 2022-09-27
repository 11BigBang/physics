import matplotlib.pyplot as plt
a = '\\frac{a}{b}'  #notice escaped slash
plt.plot()
plt.text(0.5, 0.5,'$%s$'%a)
plt.show()