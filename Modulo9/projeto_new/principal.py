# -*- coding: utf-8 -*-

import menu
import alunos
import util


# nome dos ficheiros
fxAlunos = "fxAlunos.dat"

def ler_ficheiros():
	# adicionar todos ficheiros a ler
	alunos.listaAlunos = util.ler_ficheiro(fxAlunos)


def escrever_ficheiros():
	# adicionar todos ficheiros a guardar
	util.escrever_ficheiro(fxAlunos, alunos.listaAlunos)



# Bloco Principal

ler_ficheiros()

terminar = False
while not terminar:
    op = menu.principal()
    
    if op == '1':
        alunos.gerir()
    elif op == '2':
        salas.gerir()
    elif op == '0':
        terminar = True


escrever_ficheiros()


