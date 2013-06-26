# -*- coding: utf-8 -*-

def principal():
    print
    print " **** MENU ****** "
    print
    print "   1. Gestão de Alunos"
    print "   2. Registar Presença"
    print 
    print "   0. Sair"
    print 

    op = raw_input("Opção: ")
    return op


def alunos():
    print
    print " *** Menu Alunos **** "
    print
    print "1. Inserir novo aluno"
    print "2. Listar todos alunos"
    print "3. Pesquisar aluno"
    print "4. Alterar dados de um aluno"
    print "5. Eliminar aluno"
    print 
    print "0. Menu Anterior"

    op = raw_input("Opção: ")
    return op

def salas():
    print
    print " *** Menu Alunos **** "
    print
    print "1. Inserir nova Presença"
    print "2. Listar todas as Prensenças"
    print "3. Pesquisar Presença"
    print "4. Alterar dados de uma Precença"
    print "5. Eliminar Presença"
    print 
    print "0. Menu Anterior"

    op = raw_input("Opção: ")
    return op



if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"

