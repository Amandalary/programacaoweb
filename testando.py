def chegada():
    print("- Oii, seja bem vindo a minha festinha <3!")

pessoas_desejadas = []

chegada()

pessoas = int(input("Quantos convidados você chamou? "))

for i in range(pessoas):
    nome = input("Digite o nome das pessoas: ")
    idade = int(input("Digite a idade das pessoas: "))

    if idade >= 14:
        print(nome, "- Oii amiga, entre!")
    else:
        print(nome, "só pode entrar acompanhado dos pais (minhas criancinhas).")
    pessoas_desejadas.append(nome)

print("Lista final das pessoas:")
for pessoa in pessoas_desejadas:
    print(pessoa)