# -*- coding: utf-8 -*-


#
# Exemplo utilização de array de registos
# Os elementos da lista são mantidos ordenados (por código de artigo)
# © EPCJC
#

def menu():
    print("\n\n")
    print("1: Inserir novo artigo")
    print("2: Pesquisar por um artigo")
    print("3: Modificar quantidade em stock de um artigo")
    print("4: Apresentar dados de todos os artigos\n");
    print("0: Terminar\n");



def encontra_artigo(codigo, apresentar=False):
    ''' Procura por código já existente.
    
        Pesquisa por um código de artigo nos artigos
        já inseridos. Se encontra o código, devolve o valor -1; 
        em caso contrário, devolve a posicão onde vai ser inserido 
        o novo registo
        
    '''
    
    posicao = -1 
    encontrou = False
    
    for i in range(len(Inventario)):
        registo = Inventario[i]
        if registo.codigo == codigo:
            encontrou = True
            if apresentar == True:
                print("Código Artigo     Nome                Quantidade em stock")
                print("%7d           %-20s%11d") % (registo.codigo, registo.nome, registo.stock)
            
            break
        
        if registo.codigo > codigo:
            posicao = i
            break

    if encontrou:
        posicao = -1
    
    if not encontrou and posicao == -1:     # adicionar (append) à lista
        posicao = len(Inventario)
        
    #print posicao
    return posicao
    
    
def posicao_artigo(codigo):
    ''' Encontra a posicao onde se encontra um artigo.
    
        Pesquisa por um código de artigo nos artigos
        já inseridos. Se NÃO encontra o código, devolve o valor -1; 
        caso contrário, devolve a posicão do artigo dentro da lista
        
    '''
    
    
    for posicao in range(len(Inventario)):
        registo = Inventario[posicao]
        if registo.codigo == codigo:
            return posicao
                    
  
    return -1   # não encontrou
    
        
    

def inserir():
    codigo = input("Introduza código do artigo: ")
    posicao = encontra_artigo(codigo)
    if posicao == -1:
        print("Código já existente.\n")
        return
    
    # ler os restantes dados do registo
    nome = raw_input("Introduza nome do artigo: ")
    stock = input("Introduza quantidade em stock inicial: ")
    
    
    # Criar o novo registo
    novo_registo = Artigo(codigo, nome, stock)

    # Adicionar o registo à lista na posição correta (manter a lista ordenada)
    Inventario.insert(posicao, novo_registo)
    
    
    
def listar_todos():
	print("Código Artigo     Nome                Quantidade em stock")
	for registo in Inventario:
		print("%7d           %-20s%11d") % (registo.codigo, registo.nome, registo.stock)
    


def pesquisar():
    codigo = input("Introduza código do artigo: ")
    posicao = encontra_artigo(codigo, apresentar=True)
    if posicao != -1:
        print "Artigo inexistente."
    
    
def alterar_stock():
    codigo = input("Introduza codigo do artigo: ")
    posicao = posicao_artigo(codigo)
    if posicao >= 0:
        alteracao = input("Introduza alteração de stock: ")
        Inventario[posicao] = Inventario[posicao]._replace(stock = alteracao)
    else:
        print("Artigo inexistente.")

    
def alterar2():
    for i in range(len(Inventario)):
        if Inventario[i].codigo == 1:
            print "Alterar registo codigo 1"
            Inventario[i] = Inventario[i]._replace(stock=111, nome="ALICATE")



from collections import namedtuple

Artigo = namedtuple("Artigo", "codigo, nome, stock")

Inventario = []
	
quero_sair = False
while not quero_sair:
    menu()
    op = raw_input("Introduza opção: ")
    if op == '1':
        inserir()
    elif op == '2':
        pesquisar()			
    elif op == '3':
        #alterar_stock()
        alterar2()
    elif op == '4':
        listar_todos()
    elif op == '0': 
        quero_sair = True
    else:
		print("Opção inválida\n");
        
print("\n")



