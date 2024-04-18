
cont = 1
soma = 0
while cont <= 10:
 num = float(input(f"Digite o {cont}° número: "))
 soma += num
 cont += 1

print(f"A soma dos 10 números é igual a {soma:.2f}.")
print(f"A média dos 10 números é igual a {soma/10:.2f}.")
print(f"A média dos 10 números é igual a {soma/(cont-1):.2f}.")


soma=0
while True:
    num = input(f"Digite o numero ou escreva fim para somar: ")
    if num == "fim":
        break
    soma += float(num)
print("Resultado:" , soma)
