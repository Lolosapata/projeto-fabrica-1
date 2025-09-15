
def calcula_media(n1,n2,n3,n4):
    return (n1+n2+n3+n4)/4


def situacao_media(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def programa_terminal():
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))


    media = calcula_media(nota1,nota2,nota3,nota4)
    situacao = situacao_media(media)


    print(f"{nome} está {situacao} com média: {media}")



if __name__ == "__main__":
    programa_terminal()
    