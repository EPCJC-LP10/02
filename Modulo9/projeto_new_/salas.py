# -*- coding: utf-8 -*-

from collections import namedtuple

import menu


horariosalas = namedtuple("horariosalas", "numero, dia, hora, disciplina")
listaAlunos = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listaAlunos)):
        if listaAlunos[i].numero == codigo:
            pos = i
            break
                            
    return pos


def inserir_aluno():
    numero = raw_input("Insira novo numero: ")

    pos = encontrar_posicao(numero)

    if pos >= 0:
        print "numero já existe"
        return

    #ler dados
    dia = raw_input("insira o dia: ")
    hora = raw_input("insira a hora: ")
    disciplina = raw_input ("insira a disciplina: ")
    
    registo = horariosalas(numero, dia, hora, disciplina)
    listaAlunos.append(registo)


def pesquisar_aluno():
    novo = raw_input("Insira o numero do aluno a pesquisar: ")

    pos = encontrar_posicao(novo)

    if pos == -1:
        print "Não existe aluno com esse código"
        return

    print "Numero:: ", listaAlunos[pos].numero
    print "Dia: ", listaAlunos[pos].dia
    print "hora: ", listaAlunos[pos].hora
    print "Disciplina: ", listaAlunos[pos].disciplina


def listar_alunos():
    for i in range (len(listaAlunos)):
        print "Numero: ", listaAlunos[i].numero
        print "Dia: ", listaAlunos[i].dia
        print "hora: ", listaAlunos[i].hora
        print "Disciplina: ", listaAlunos[i].disciplina
  

def eliminar_aluno():
    numero = raw_input ("Numero do aluno a eliminar --> ")
    pos = encontrar_posicao(numero)

    if pos == -1:
        print "Não existe aluno com esse numero"
        return

    # TODO: Confirmar eliminação
    listaAlunos.pop(pos)


    
def alterar_aluno():
    numero = raw_input ("Numero do aluno a alterar --> ")
    pos = encontrar_posicao(numero)

    if pos == -1:
        print "Não existe aluno com esse numero"
        return

    # só altera o nome
    novonumero = raw_input("Insira novo numero: ")
    listaAlunos[pos] = listaAlunos[pos]._replace(numero=novonumero)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.salas()

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
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"










