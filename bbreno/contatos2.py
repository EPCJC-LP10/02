# -*- coding: utf-8 -*-
# TxR
# :D

def menu():
        print
        print "1: Inserir novo contacto"
        print "2: Listar todos os contactos"
        print "3: Pesquisar contacto por nome"
        print "4: Alterar dados de um contacto"
        print "5: Eliminar contacto"

        
        print "0: Terminar"
        print

def posicao_contacto(codigo):

        for pos in range(len(Contactos)):
                if Contactos[pos].codigo == codigo:
                        return pos
                                        
        return -1
        
        

def inserir():
        codigo = input("Introduza numero: ")
        posicao = posicao_contacto(codigo)
        if posicao != -1:
                print("numero já existente.\n")
                return
        
        titulo = raw_input("Introduza operador : ")
        autor = raw_input("Introduza nome: ")
        email = raw_input("Introduza email: ")

        novo_registo = Contacto(codigo, titulo, autor, email)

        Contactos.append(novo_registo)
        
        
def apresentar_registo(registo):
                print "Numero: ", registo.codigo
                print "Operador: ", registo.titulo
                print " Nome: ", registo.autor
                print "Email: ", registo.email
                print "-------------------------------"


def listar_todos():
        if len(Contactos) == 0:
                print "Não existem contactos inseridos"
                return

        for registo in Contactos:
                apresentar_registo(registo)
                

def listar_todos_alternativa():
        if len(Contactos) == 0:
                print "Não existem contactos inseridos"
                return

        for i in range(len(Contactos)):
                apresentar_registo(Contactos[i])



def pesquisar():
        nome = raw_input("Introduza nome da pessoa: ")
        for pos in range(len(Contactos)):
                if Contactos[pos].autor == nome:
                        apresentar_registo(Contactos[pos])
        
def alterar():
        nome = raw_input("Introduza o nome da pessoa que pretender alterar os registos: ")
        for pos in range(len(Contactos)):
                if Contactos[pos].autor == nome:
                        apresentar_registo(Contactos[pos])
        if pos == -1:
                print "Esse nome não existe."
                return

        print "1. Operador"
        print "2. Nome"
        print "3. email"
        print "4. Todos"
        print "0. Cancelar"
        op = input ("Digite qual dos seguintes registos pretende alterar: ")

        if op == 1:
        
                novo_titulo = raw_input("Introduza novo operador: ")
                Contactos[pos] = Contactos[pos]._replace(titulo=novo_titulo)

        elif op == 2:
                
                novo_autor = raw_input("Introduza novo nome: ")
                Contactos[pos] = Contactos[pos]._replace(autor=novo_autor)

        elif op == 3:

                novo_email = raw_input("Introduza novo email: ")
                Contactos[pos] = Contactos[pos]._replace(email=novo_email)

        elif op == 4:
                novo_titulo = raw_input("Introduza novo operador: ")
                novo_autor = raw_input("Introduza novo nome: ")
                novo_email = raw_input("Introduza novo email: ")
                Contactos[pos] = Contactos[pos]._replace(titulo=novo_titulo, autor=novo_autor, email=novo_email)

        elif op == 0:
                print "Operaçao Cancelada"

        else:
                print "opcao invalida"

                
def eliminar():
        nome = raw_input("Introduza nome da pessoa: ")
        for pos in range(len(Contactos)):
                if Contactos[pos].autor == nome:
                        apresentar_registo(Contactos[pos])

        if pos == -1:
                print "Esse nome não existe."
                return


        apresentar_registo(Contactos[pos])
        opcao = raw_input("Tem a certeza que deseja eliminar este contacto (S/N)? ")
        if opcao.lower() == "s":
                Contactos.pop(pos)
                print "Contacto eliminado"
        else:
                print "Contacto não eliminado"


##################################

from collections import namedtuple

Contacto = namedtuple("Contacto", "codigo, titulo, autor, email")

Contactos = []
        
quero_sair = False
while not quero_sair:
        menu()
        op = raw_input("Introduza opção: ")
        if op == '1':
                inserir()
        elif op == '2':
                listar_todos()          
        elif op == '3':
                pesquisar()
        elif op == '4':
                alterar()
        elif op == '5':
                eliminar()
        elif op == '0': 
                quero_sair = True
        else:
                print "Opção inválida"
                
print 


