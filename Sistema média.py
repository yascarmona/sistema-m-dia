nome = input("Digite o nome do aluno(a): ")
def lernotas():
    n=float(input('Digite uma nota para o aluno(a): '))
    return n

def resultado(n1,n2,n3,):
    media= (n1+n2+n3/3)
    print("Nota 1: ", n1)
    print("Nota 2: ", n2)
    print("Nota 3: ", n3)
    if media>=7:
        print("Resultado: Aprovado")
    else:
        print("Resultado: Reprovado")

print("Nome: %s"%nome)
a = lernotas()
b = lernotas()
c = lernotas()
resultado(a,b,c)

