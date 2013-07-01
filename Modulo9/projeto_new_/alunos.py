# -*- coding: utf-8 -*-

from collections import namedtuple

import menu


alunos = namedtuple("alunos", "numero, nome")
listaAlunos = []



def encontrar_posicao(numer):
    pos = -1
    for i in range (len(listaAlunos)):
        if listaAlunos[i].numero == numer:
            pos = i
            break
                            
    return pos


def inserir_aluno():
    numero = raw_input("Qual o numero do aluno: ")

    pos = encontrar_posicao(numero)

    if pos >= 0:
        print "Numero já existe"
        return

    #ler dados
    nome = raw_input("Qual o nome: ")
    
    registo = alunos(numero, nome)
    listaAlunos.append(registo)


def pesquisar_aluno():
    numero = raw_input("Digite o numero do aluno a pesquisar: ")

    pos = encontrar_posicao(numero)

    if pos == -1:
        print "Não existe aluno com esse código"
        return

    print "numero: ", listaAlunos[pos].numero
    print "Nome: ", listaAlunos[pos].nome
    


def listar_alunos():
    for i in range (len(listaAlunos)):
        print "numero: ", listaAlunos[i].numero
        print "Nome: ", listaAlunos[i].nome
        
  

def eliminar_aluno():
    numero = raw_input ("numero do aluno a eliminar: ")
    pos = encontrar_posicao(numero)

    if pos == -1:
        print "Não existe aluno com esse numero"
        return

    # TODO: Confirmar eliminação
    listaAlunos.pop(pos)


    
def alterar_aluno():
    numero = raw_input ("numero do aluno a alterar: ")
    pos = encontrar_posicao(numero)

    if pos == -1:
        print "Não existe aluno com esse código"
        return

    # só altera o nome
    novonome = raw_input("Digite o novo nome: ")
    listaAlunos[pos] = listaAlunos[pos]._replace(nome=novonome)
    
def aluno_max():
    print max(alunos)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.alunos()

        if op == '1':
            inserir_aluno()
        elif op =='2':
            listar_alunos()
        elif op == '3':
            pesquisar_aluno()
        elif op == '4':
            alterar_aluno()
        elif op == '5':
            eliminar_aluno()
        elif op == '6':
            aluno_max()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"










