import matplotlib.pyplot as plt

host = [13.5, 15.0, 15.0, 15.6, 15.8, 27.1, 27.0, 26.4, 26.8, 29.1, 40.0, 38.5, 40.0, 39.4, 39.3, 52.0, 52.2, 53.0, 51.6, 51.6, 64.3, 64.5, 63.9, 64.3, 65.6]
vm = [26.2, 25.0, 25.1, 25.0, 25.0, 50.0, 50.0, 50.0, 50.2, 50.0, 75.8, 75.0, 75.0, 75.8, 75.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0]

plt.plot(host, 'r', label='Host', marker='o')
plt.plot(vm, 'c', label='VM', marker='o') 
plt.xlabel('N de Processos')
plt.ylabel('Uso da CPU (%)')
plt.ylim(0, 100)
plt.legend()
plt.grid()
plt.show()
