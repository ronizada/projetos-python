idade = int(input("Digite sua idade: "))
salario = int(input("Digite seu salário em R$: "))


if idade < 18:
    print("Crédito negado!")
elif idade >= 18 and salario >= 2000:
    print("CRÉDITO APROVADO!")
else:
    print("Crédito sob análise!")