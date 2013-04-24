# -*- coding: utf-8 -*-

#
# Exemplo utilização de array de registos
# Os elementos da lista NÃO são mantidos ordenados
# (a inserção é feita depois da última posição anterior)
# © EPCJC
#

def menu():
	print
	print "1: Inserir novo contacto"
	print "2: Listar todos os contactos"
	print "3: Pesquisar contacto por nome"
	print "4: Alterar dados de um contacto"
	print "5: Eliminar contacto"
	
	print "0: Terminar"
	print

def posicao_livro(codigo):
	''' Encontra a posicao onde se encontra o livro com o código recebido
	
		Pesquisa por um código de livro nos livros
		já inseridos. Se NÃO encontra o código, devolve o valor -1; 
		caso contrário, devolve a posicão do livro dentro da lista
		
	'''
	
	for pos in range(len(Livros)):
		if Livros[pos].codigo == codigo:
			return pos
					
	return -1   # não encontrou
	
	

def inserir():
	codigo = input("Introduza numero: ")
	posicao = posicao_livro(codigo)
	if posicao != -1:
		print("numero já existente.\n")
		return
	
	# ler os restantes dados do registo
	titulo = raw_input("Introduza operador : ")
	autor = raw_input("Introduza nome: ")
	
	
	# Criar o novo registo
	novo_registo = Livro(codigo, titulo, autor)

	# Adicionar o registo à lista 
	Livros.append(novo_registo)
	
	
def apresentar_registo(registo):
		print "Numero: ", registo.codigo
		print "Operador: ", registo.titulo
		print " Nome: ", registo.autor
		print "-------------------------------"


def listar_todos():
	if len(Livros) == 0:
		print "Não existem contactos inseridos"
		return

	for registo in Livros:
		apresentar_registo(registo)
		

#Outra maneira de fazer a listagem
def listar_todos_alternativa():
	if len(Livros) == 0:
		print "Não existem contactos inseridos"
		return

	for i in range(len(Livros)):
		apresentar_registo(Livros[i])



def pesquisar():
	nome = raw_input("Introduza nome da pessoa: ")
	for pos in range(len(Livros)):
		if Livros[pos].autor == nome:
			apresentar_registo(Livros[pos])
	
def alterar():
	nome = raw_input("Introduza nome da pessoa: ")
	for pos in range(len(Livros)):
		if Livros[pos].autor == nome:
			apresentar_registo(Livros[pos])

	if pos == -1:
		print "Esse nome não existe."
		return

	# A melhorar: perguntar qual o campo que se pretende alterar
	# Assim altera todos os campos com exceção do código

	#ler os novos dados
	novo_titulo = raw_input("Introduza novo operador: ")
	novo_autor = raw_input("Introduza novo nome: ")
	

	# Substituir o registo
	Livros[pos] = Livros[pos]._replace(titulo=novo_titulo, 
		autor=novo_autor)

	
	
def eliminar():
	nome = raw_input("Introduza nome da pessoa: ")
	for pos in range(len(Livros)):
		if Livros[pos].autor == nome:
			apresentar_registo(Livros[pos])

	if pos == -1:
		print "Esse nome não existe."
		return


	apresentar_registo(Livros[pos])
	opcao = raw_input("Tem a certeza que deseja eliminar este contacto (S/N)? ")
	if opcao.lower() == "s":
		#eliminar registo na posição posicao
		Livros.pop(pos)
		print "Contacto eliminado"
	else:
		print "Contacto não eliminado"


##################################

from collections import namedtuple

Livro = namedtuple("Livro", "codigo, titulo, autor")

Livros = []
	
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

