# Nomes:
# ----------------------------------
# Beatriz Vitoria - RA 02211004
# Flavia de Oliveira - RA 02211017
# João Ruas - RA 02211038
# Lucas Henrique - RA 02211042
# Rafaela Amancio - RA 02211055
# Rodrigo Garcez - RA 02211059
# ----------------------------------

import psutil
import time
from connectdb import *
from bot import mensagem


numCapturas = 0
opcaoMenu = 0
while opcaoMenu != "1" and opcaoMenu != "2":

    print("-"*45, "//", "-"*45)
    print(" "*44, "MENU")
    print("-"*45, "//", "-"*45)
    print("1- Executar o programa em tempo real, sem parada")
    print("2- Executar o programa com limite de capturas")
    opcaoMenu = input("Digite a opção escolhida: ")
    print("-"*45, "//", "-"*45)


if(opcaoMenu == "2"):
    numCapturas = input("Digite o limite de capturas: ")

tempoIntervalo = input("Digite o tempo de intervalo entre as capturas: ")

i = 0
idCaptura = 1;
while i == 0 or i < int(numCapturas):
    # Pega a hora, minutos, segundos e milisegundos atual
    dateTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

    nomeUsuario = psutil.users()[0][0]
    bytesRecebidos = psutil.net_io_counters()[0]
    
    bytesEnviados = psutil.net_io_counters()[1]
    

    percentualCpu1 = psutil.cpu_percent(interval=int(tempoIntervalo))
    percentualDisco1 = psutil.disk_usage('C:/').percent
    percentualMem1 = psutil.virtual_memory().percent

    percentualCpu2 = percentualCpu1 * 1.1	# f(cpu2) = cpu1 * 1.1
    percentualDisco2 = percentualDisco1 * 0.95	# f(disco2) = disco1 * 0.95
    percentualMem2 = percentualMem1 * 1.15	# f(mem2) = mem1 * 1.15
    if(percentualMem2 > 100):
        percentualMem2 = 100

    percentualCpu3 = percentualCpu2 * 0.95	#f(cpu3) = cpu2 * 0.95
    percentualDisco3 = percentualDisco2 * 0.33	#f(disco3) = disco2 * 0.33
    percentualMem3 = percentualMem2 * 1.05	#f(mem3) = mem2 * 1.05
    if(percentualMem3 > 100):
        percentualMem3 = 100

    if(percentualCpu1 >= 100):
        percentualCpu1 = 100
        
    if(percentualCpu2 >= 100):
        percentualCpu2 = 100

    if(percentualCpu3 >= 100):
        percentualCpu3 = 100
    
    if(bytesRecebidos > 0 and bytesEnviados > 0):
        internet = "Conectada"
    else:
        internet = "Desconectada"

    cpu1 = round(float(percentualCpu1), 2)
    ram1 = round(float(percentualMem1), 2)
    disco1 = round(float(percentualDisco1), 2)

    cpu2 = round(float(percentualCpu2), 2)
    ram2 = round(float(percentualMem2), 2)
    disco2 = round(float(percentualDisco2), 2)

    cpu3 = round(float(percentualCpu3), 2)
    ram3 = round(float(percentualMem3), 2)
    disco3 = round(float(percentualDisco3), 2)

    fkTorre = 1;

    if (percentualMem1 > 60):
        mensagem(f"Alerta de RAM para o computador X - Valor: {percentualMem1}%")

    insert_db(idCaptura, 1, fkTorre, nomeUsuario, percentualCpu1, percentualMem1, percentualDisco1, internet)
    # insert_db(idCaptura, 2, fkTorre, "Brandão", percentualCpu2, percentualMem2, percentualDisco2, "Desconectado")
    # insert_db(idCaptura, 3, fkTorre, "Marise", percentualCpu3, percentualMem3, percentualDisco3, internet)

   

    idCaptura += 1

    # Output
    print("\n" * 100)

    print("-"*45, "//", "-"*45)
    print(' '*27, "CAPTURA EM TEMPO REAL - TORRE CONGONHAS")
    print("-"*45, "//", "-"*45)

    print("\t\tUsuário\t\tCPU\t\tRAM\t\tDisco\t\tInternet")
    print(
        f"Máq. 1\t\t{nomeUsuario}\t\t{cpu1}%\t\t{ram1}%\t\t{disco1}%\t\t{internet}\n")
    print(
        f"Máq. 2\t\tBrandão\t\t{cpu2}%\t\t{ram2}%\t\t{disco2}%\t\tDesconectado\n")
    print(
        f"Máq. 3\t\tMarise\t\t{cpu3}%\t\t{ram3}%\t\t{disco3}%\t\t{internet}\n")

    print("-"*45, "//", "-"*45)
    print(" "*20, f"Tempo da última captura: {dateTime}")
    print("-"*45, "//", "-"*45)

    if(opcaoMenu == "2"):
        i += 1
