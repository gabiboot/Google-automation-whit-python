import shutil
import psutil

#Funcion que devuelve verdadero si hay mas del 20%
def check_disck_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total * 100
    return free > 20

#"BUEN ESTADO" menos de 75%
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75
#main del script imprimir el mensaje que el usuario vera
if not check_disck_usage("/") or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything is OK!")    
