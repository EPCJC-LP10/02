# -*- coding: utf-8 -*-
# Bruno Gabriel
# Agenda / Contactos

def menu():
        print
        print "***************MENU*****************"
        print "* 1: Inserir novo contacto         *"
        print "* 2: Listar todos os contactos     *"
        print "* 3: Pesquisar contacto por nome   *"   
        print "* 4: Alterar dados de um contacto  *"  
        print "* 5: Eliminar contacto             *"
        print "************************************"
        print "* 0: Terminar                      *"
        print "************************************"
        print

def posicao_contacto(numero):

        for pos in range(len(Contactos)):
                if Contactos[pos].numero == numero:
                        return pos
                                        
        return -1
        
        

def inserir():
        print "+-----------------------------------"
        numero = input("| Introduza numero: ")

        posicao = posicao_contacto(numero)
        if posicao != -1:
                print("numero já existente.\n")
                return
        print "|-----------------------------------"
        operador = raw_input("| Introduza operador : ")
        print "|-----------------------------------"
        nome = raw_input("| Introduza nome: ")
        print "|-----------------------------------"
        email = raw_input("| Introduza email: ")
        print "+-----------------------------------"

        novo_registo = Contacto(numero, operador, nome, email)

        Contactos.append(novo_registo)
        
        
def apresentar_registo(registo):
                print
                print "+------------------------------+"
                print "| Numero: ", registo.numero
                print "| Operador: ", registo.operador
                print "| Nome: ", registo.nome
                print "| Email: ", registo.email
                print "+------------------------------+"
                print ""
                print ""


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
        print
        nome_pesquisar = raw_input("Introduza nome da pessoa: ")
        print
        for pos in range(len(Contactos)):
                if Contactos[pos].nome == nome_pesquisar:
                        apresentar_registo(Contactos[pos])
        
def alterar():
        print
        nome_alterar = raw_input("Introduza o nome da pessoa que pretender alterar os registos: ")
        for pos in range(len(Contactos)):
                if Contactos[pos].nome == nome_alterar:
                        apresentar_registo(Contactos[pos])
        if pos == -1:
                print "Esse nome não existe."
                return

        print
        print "+-----Menu------+"
        print "|***************|"
        print "|* 1. Operador *|"
        print "|* 2. Nome     *|"
        print "|* 3. email    *|"
        print "|* 4. Todos    *|"
        print "|***************|"
        print "|---------------|"
        print "| 0. Cancelar   |"
        print "+---------------+"
        op = input ("Digite qual dos seguintes registos pretende alterar: ")

        if op == 1:
                print
                novo_operador = raw_input("Introduza novo operador: ")
                print
                Contactos[pos] = Contactos[pos]._replace(operador=novo_operador)

        elif op == 2:
                print
                novo_nome = raw_input("Introduza novo nome: ")
                print
                Contactos[pos] = Contactos[pos]._replace(nome=novo_nome)

        elif op == 3:
                print
                novo_email = raw_input("Introduza novo email: ")
                print
                Contactos[pos] = Contactos[pos]._replace(email=novo_email)

        elif op == 4:
                print "+--------------------------------------------"
                novo_operador = raw_input("| Introduza novo operador: ")
                print "|--------------------------------------------"
                novo_nome = raw_input("| Introduza novo nome: ")
                print "|--------------------------------------------"
                novo_email = raw_input("Introduza novo email: ")
                print "+--------------------------------------------"
                Contactos[pos] = Contactos[pos]._replace(operador=novo_operador, nome=novo_nome, email=novo_email)

        elif op == 0:
                print "Operaçao Cancelada"

        else:
                print "opcao invalida"

                
def eliminar():
        print
        nome_eliminar = raw_input("Introduza nome da pessoa: ")
        print
        for pos in range(len(Contactos)):
                if Contactos[pos].nome == nome_eliminar:
                        apresentar_registo(Contactos[pos])

        if pos == -1:
                print "Esse nome não existe."
                return


        apresentar_registo(Contactos[pos])
        print
        opcao = raw_input("Tem a certeza que deseja eliminar este contacto (S/N)? ")
        print
        if opcao.lower() == "s":
                Contactos.pop(pos)
                print "Contacto eliminado"
        else:
                print "Contacto não eliminado"



from collections import namedtuple

Contacto = namedtuple("Contacto", "numero, operador, nome, email")

Contactos = []
        
quero_sair = False
while not quero_sair:
        menu()
        op = raw_input("Introduza opção: ")
        print
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


