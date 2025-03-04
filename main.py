#Generador que pida una palabra de min 8 caracteres y desordenen las letras dando una contraseña
import random
import string

def main():
    #ASCII Art :3
    print(r"""
            ____                  ____                           _             
            |  _ \ __ _ ___ ___   / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
            | |_) / _` / __/ __| | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
            |  __/ (_| \__ \__ \ | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
            |_|   \__,_|___/___/  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|  
         """)
    while True: 
        user = input("Introduce una palabra de más de 8 caracteres: ")
        if len(user) < 8: #Si la longitud de la palabra es menor a 8
            print("Palabra con menos de 8 caracteres")
            break
        else:
            lista_caracteres = list(user) #Convierte a una lista la palabra
            random.shuffle(lista_caracteres) #Desordena la palabra 
            palabra_desordenada = ''.join(lista_caracteres) #Convierte otra vez de lista a palabra
            print(f"La contraseña generada es: {palabra_desordenada}") 
            add = input("Quieres que le agrege caracteres especiales?: ")
            if add.lower() == "si":
                #Acude a la def de abajo
                num_caracteres_a_agregar = int(input("¿Cuántos caracteres especiales deseas agregar?: "))
                palabra_modificada = agregar_caracteres_random(palabra_desordenada, num_caracteres_a_agregar)
                print(f"La contraseña modificada es: {palabra_modificada}")
            quest = input("Quieres generar otra?: ")
            if quest.lower() == "si": #Acepta "si" esta en minusculas o mayusculas 
                continue 
            else:
                print("Ok :3")
                break


def agregar_caracteres_random(palabra, num_caracteres):
    #Conjunto de caracteres que se pueden agregar
    caracteres = string.ascii_letters + string.digits #Letras y dígitos
    palabra_lista = list(palabra)  #Convertir la palabra a una lista para poder modificarla

    for _ in range(num_caracteres):
        caracter_random = random.choice(caracteres) #Elegir un carácter aleatorio
        posicion_random = random.randint(0, len(palabra_lista)) #Elegir una posición aleatoria en la palabra
        palabra_lista.insert(posicion_random, caracter_random) #Insertar el carácter en la posición aleatoria
    return ''.join(palabra_lista) #Convertir la lista de nuevo a una cadena

main() #Llamar a la funcion main :3