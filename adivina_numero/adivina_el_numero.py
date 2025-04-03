import random

print("--- ADIVINA EL NUMERO ENTRE EL 1 Y EL 10 --- TIENES 4 INTENTOS ---")
numero_A = random.randint(1,10)
usuario = int(input("INGRESE UN NUMERO: "))
intentos = 1



while (intentos != 4):
    if(numero_A == usuario):
        print("GANASTE. ADIVINASTE EL NUMERO")
        break

    elif(usuario > numero_A):
        print("MUY ALTO")
        intentos += 1
        usuario = int(input("INGRESE UN NUMERO: "))
        
    elif(usuario < numero_A):
        print("MUY BAJO")
        intentos += 1
        usuario = int(input("INGRESE UN NUMERO: "))
else:
    print("PERDISTE. INTENTOS AGOTADOS")

        





