# -*- coding: utf-8 -*-

#
# Exemplo utilização de array de registos
# Os elementos da lista NÃO são mantidos ordenados
# (a inserção é feita depois da última posição anterior)
# © EPCJC
#

def menu():
    print
    print "1: Inserir novo selo"
    print "2: Listar todos os selos"
    print "3: Alterar dados de um selo"
    print "4: Eliminar selo"
    print "5: Listar todos os selos de nome 'arte'"
    print "6: Listar todos os selos entre 1980 e 2010"
    print
    print "0: Terminar"
    print

    

def inserir():
    num = input("Introduza código: ")
    
    encontrou = False        
    for i in range(len(Selos)):
        if Selos[i].num == num:
            encontrou = True           
            break
        
    
    if encontrou:
        print "Esse codigo é repetido."
        return
    
    # ler os restantes dados do registo
    nome = raw_input("Introduza nome: ")
    serie = raw_input("Introduza série: ")
    ano = raw_input("Introduza ano: ")
    
    
    # Criar o novo registo
    novo_registo = SeloReg(num, nome, serie, ano)

    # Adicionar o registo à lista 
    Selos.append(novo_registo)
    #outra maneira
    #Selos.insert(len(Selos), novo_registo)
    
           

def listar_todos(registo):
    if len(Selos) == 0:
        print "Não existem livros inseridos"
        return
     
    for i in range(len(Selos)):
        print "Código: ", Selos[i].num
        print "  Nome: ", Selos[i].nome
        print " Serie: ", Selos[i].serie
        print "   Ano: ", Selos[i].ano
        print "-------------------------------"
        
        
    

    
def alterar():
    codigo = input("Introduza código do livro: ")

    encontrou = False        
    for i in range(len(Selos)):
        if Selos[i].num == codigo:
            encontrou = True
            pos = i #Posição dentro do array onde está  registo
            break
    
    
    if not encontrou:
        print "Esse codigo não existe"
        return
        
    #ler os novos dados
    novo_nome = raw_input("Introduza novo nome: ")
    novo_serie = raw_input("Introduza nova serie: ")
    novo_ano = raw_input("Novo ano de lançamento: ")

    
    # Substituir o registo
    Selos[pos] = Selos[pos]._replace(nome=novo_nome, serie=novo_serie, ano=novo_ano)

    
    
def eliminar():
    codigo = input("Introduza código do livro: ")

    encontrou = False        
    for i in range(len(Selos)):
        if Selos[i].num == codigo:
            encontrou = True
            pos = i
            break
    
    
    if not encontrou:
        print "Esse codigo não existe"
        return
        
    #Eliminar o registo
    Selos.pop(pos)
    
def pesquisar_arte():       
    for pos in range(len(Selos)):
        if Selos[pos].nome == 'Arte':
            listar_todos(Selos[pos].nome)



##################################

from collections import namedtuple

SeloReg = namedtuple("SeloReg", "num, nome, serie, ano")

Selos = []

	
quero_sair = False
while not quero_sair:
    menu()
    op = raw_input("Introduza opção: ")
    if op == '1':
        inserir()
    elif op == '2':
        listar_todos()		
    elif op == '3':
        alterar()
    elif op == '4':
        eliminar()
    elif op == '5':
        pesquisar_arte()
    elif op == '0': 
        quero_sair = True
    else:
		print "Opção inválida"
        
print 

