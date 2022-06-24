from random import randint as rd
quantidade = numero = 0

while True:
    CPU = rd(0,10)
    PLAYER = int(input("Informe um número: "))
    numero = CPU + PLAYER
    Choose = ' '
    while Choose not in 'PpIi':
        Choose = str(input("Você :escolhe impar ou par: ")).strip().upper()[0]
        print(f"Você jogou {PLAYER} e o Computador jogou {CPU}, a soma dos dois valores deu {numero}")
        print("Deu Par" if numero % 2 == 0 else "Deu Impar")

    print('='*50)
    if Choose == "P":
        if numero % 2 == 0: 
            print("Você venceu")
            quantidade += 1
        else:
            print("Você perdeu.")
            print('='*50)
            break
    
    elif Choose == 'I':
        if numero % 2 == 1: 
            print("Você venceu")
            quantidade += 1
        else:
            print("Você perdeu.")
            print('='*50)
            break
print(f"Você venceu {quantidade} vezes")
