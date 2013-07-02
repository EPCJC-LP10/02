# -*- coding: utf-8 -*-

import menu
import alunos
import salas
import util

from collections import namedtuple

presencaReg = namedtuple("presencaReg", "codAluno, sala, dia, hora, disciplina")
listaPresencas = []


# nome dos ficheiros
fxAlunos = "fxAlunos.dat"
fxSalas = "fxSalas.dat"
fxPresencas = "fxPresencas.dat"

def ler_ficheiros():
    global listaPresencas    
    
    
    # adicionar todos ficheiros a ler
    alunos.listaAlunos = util.ler_ficheiro(fxAlunos)
    salas.listaSalas = util.ler_ficheiro(fxSalas)
    listaPresencas = util.ler_ficheiro(fxPresencas)


def escrever_ficheiros():
    # adicionar todos ficheiros a guardar
    util.escrever_ficheiro(fxAlunos, alunos.listaAlunos)
    util.escrever_ficheiro(fxSalas, salas.listaSalas)
    util.escrever_ficheiro(fxSalas, listaPresencas)
     


def registar_presenca():
    codaluno = raw_input("Código do aluno --> ")
    
    indexAluno = 0
    encontrou = False    
    
    for i in range(len(alunos.listaAlunos)):
        if alunos.listaAlunos[i].numero == codaluno:
            encontrou = True
            indexAluno = i
            break

    if not encontrou:
        print "Aluno não existe"
        return

    print "Aluno", alunos.listaAlunos[indexAluno].nome
    
    indexHorario = 0
    encontrou = False    
    

    sala = raw_input("Sala -->" )    
    dia = raw_input("Dia --> ")    
    hora= raw_input("Hora --> ")
    
    for i in range(len(salas.listaSalas)):
        if salas.listaSalas[i].numero == sala and salas.listaSalas[i].dia == dia and salas.listaSalas[i].hora == hora:
            encontrou = True
            indexHorario = i
            break

    if not encontrou:
        print "Impossível registar"
        return


    registoPresenca = presencaReg(alunos.listaAlunos[indexAluno], 
                                   salas.listaSalas[indexHorario].numero,
                                   salas.listaSalas[indexHorario].dia, 
                                    salas.listaSalas[indexHorario].hora,
                                    salas.listaSalas[indexHorario].disciplina)
                                    


    listaPresencas.append(registoPresenca)
    
    
def ver_todas_presencas():
    for i in range(len(listaPresencas)):
        print "Código aluno", listaPresencas[i].codAluno
        print "Sala: ", listaPresencas[i].sala
        print "Dia: ", listaPresencas[i].dia
        print "Hora: ", listaPresencas[i].hora


# Bloco Principal

ler_ficheiros()

terminar = False
while not terminar:
    op = menu.principal()
    
    if op == '1':
        alunos.gerir()
    elif op == '2':
        salas.gerir()
        
    elif op == '3':
        registar_presenca()
    elif op =='4':
        ver_todas_presencas()
    elif op == '0':
        terminar = True


escrever_ficheiros()


