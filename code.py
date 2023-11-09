import time
import psutil
import multiprocessing
import matplotlib.pyplot as plt

def calc(x, timeout):
    while True:
        if time.time() > timeout: break
        x * x

def monitor(uso_de_cpu, timeout):
    while True:
        if time.time() > timeout: break
        percentual_cpu = psutil.cpu_percent(interval=1)
        uso_de_cpu.append(percentual_cpu)
        time.sleep(1)

n_processos = [1, 2, 3, 4, 5]

if __name__ == '__main__':
    processos = []

    manager = multiprocessing.Manager()
    uso_de_cpu = manager.list()

    timeout = time.time() + 60

    processo_monitor = multiprocessing.Process(target=monitor, args=(uso_de_cpu, timeout))
    processo_monitor.start()
    for x in n_processos:
        processo_calc = multiprocessing.Process(target=calc, args=(x, timeout))
        processo_calc.start()
        processos.append(processo_calc)
        time.sleep(10)
    
    processo_monitor.terminate()
    for processo in processos:
        processo.terminate()
    
    uso_de_cpu = list(uso_de_cpu)

    print(uso_de_cpu)
