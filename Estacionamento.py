import math


# Funções a ser utilizadas
def find_car(key, park):
    for item in park:
        if key == item[0]:
            return park.index(item)


# Função para adicionar um ticket


def add_car(ticket, park):
    park.append(ticket)
    print(ticket)
    return park

# Função para remover um ticket
# Rece a chave de busca (matrícula e o park) | Devolve a estrutura modificada


def remove_car(key, park):
    idx = find_car(key, park)
    park.remove(park[idx])
    return park


# Função para listar a matrícula de todos os carros no parque


def list_car(park):
    for item in park:
        print(f"Matricula: {item[0]}")
    print("\n")


# Função para determinar o tempo de permanência no parque
# Recebe o ticket respectivo e a hora de saída
def tempo_estadia(ticket, h_out):
    item = ticket[1]
    hora_in = int(item[0:item.find(":")])
    min_in = int(item[item.find(":")+1:])
    hora_out = int(h_out[0: h_out.find(":")])
    min_out = int(h_out[h_out.find(":")+1:])
    estada = (hora_out*60 + min_out - (hora_in*60 + min_in))
    if estada >= 25:
        return math.ceil(estada/60)
    else:
        return 0


# Função que busca o preço da hora consoante a duração
def unit_price(estada, prices):
    if estada <= 1:
        unit_price = prices["1"]
    elif (2 < estada <= 3):
        unit_price = prices["2-3"]
    else:
        unit_price = prices[">3"]
    return unit_price


def menu():
    # Definição das Variáveis
    # ticket = [matricula, hora_entrada]
    # Estrutura park: lista de tickets
    park = [
        ["12-AB-34", "10:20"],
        ["02-HH-32", "16:20"],
        ["00-YY-34", "8:01"]
    ]
    prices = {"1": 1.5, "2-3": 1, ">3": 0.75}
    comandos = {'e', 's', 'l', 'x', 'c', 'q'}
    caixa = 0
    prices = {"1": 1.5, "2-3": 1, ">3": 0.75}


# Programa

    print("Comandos: \n")
    print("    e<matrícula> <hora de entrada> - para dar entrada no parque")
    print("    s<matrícula> <hora de saída>   - para dar saída do parque")
    print("    l - listar todas as matrículas dos carros dentro do parque")
    print("    x - listar todas as matrículas e reportar o dinheiro em caixa")
    print("    c - reportar o dinheiro em caixa\n")
    print("    q - Sair do programa\n\n")

    comando = "dummy"
    while comando[0].lower() not in comandos:
        comando = input("Comando: >>")
        if comando[0] == 'e':
            matricula = comando[1: comando.find(" ")]
            hora_in = comando[comando.find(" ")+1:]
            print(f"Adicionando carro {matricula} às {hora_in} horas")
            park = add_car([matricula, hora_in], park)
            comando = "dummy"
        elif comando[0] == 's':
            matricula = comando[1: comando.find(" ")]
            hora_out = comando[comando.find(" ")+1:]
            print(f"Sai carro matricula {matricula} às {hora_out}")
            park = remove_car(matricula, park)
            estadia = tempo_estadia([matricula, hora_in], hora_out)
            custo = estadia * unit_price(estadia, prices)
            caixa += custo
            print(
                f"O carro matrícula  {matricula} teve uma estadia de {estadia} horas"
            )
            print(f"O custo da estadia foi de {custo} euros")
            comando = "dummy"
        elif comando[0] == 'l':
            # print("Lista todas as matrículas dos carros dentro do parque")
            list_car(park)
            comando = "dummy"
        elif comando[0] == 'x':
            # print("Lista todas as matrículas e reporta o dinheiro em caixa")
            list_car(park)
            print(f"\nO valor em caixa é de {caixa}")
            comando = "dummy"
        elif comando[0] == 'c':
            print(f"\nO valor em caixa é de {caixa}")
            comando = "dummy"
        elif comando[0] == 'q':
            break
        else:
            print("Comando inválido!")
            comando = "dummy"


# Programa Principal
menu()

