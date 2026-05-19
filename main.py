nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print(f"{nome}, você é maior de idade.")
else:    print(f"{nome}, você é menor de idade.")

def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media   

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = calcular_media(nota1, nota2)
print(f"A média das notas é: {media}")