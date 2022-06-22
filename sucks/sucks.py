# -*- coding: utf-8 -*-
import json
crudData = {}

print("""bem vindo ao sucks, digite "Help" sem aspas pra ajuda

programa em fase beta, pode haver falhas e bugs
""")


def put_data():
	print("Coloque o indentificador (chave): ", end="")
	key = input()
	print("Coloque o valor (value): ", end="")
	value = input()
	crudData[key] = value
def edit_data():
	print("Coloque o a chave correspodente: ", end="")
	key = input()
	print("Coloque o valor para sobrepor: ", end="")
	newValueArg = input()
	crudData[key] = newValueArg
def change_key():
	print("Coloque o valor original da chave: ", end="")
	originalKeyValue = input()
	print("Coloque o valor substituto: ", end="")
	crudData[originalKeyValue]
def delete_data():
	print("Coloque a chave que você deseja deletar: ", end="")
	key = input()
	crudData.pop(key)
def delete_all():
	crudData.clear()
def print_all():
	for x, y in crudData.items():
		print(x,":", y)
def super_put():
	print("Coloque no formato dict o seu Super-Put:")
	dbData = input()
	dbData = json.loads(dbData)
	crudData.update(dbData)
def hyper_put():
	print('Coloque chave e valor no formato: "chave: valor" sem aspas, o ":" será usado como separador (split)')
	print('Quando pressionar enter, poderá inserir mais valores da mesma forma, quando acabar, pressione Ctrl+C apenas UMA VEZ para salvar o conteudo no crud')
	while True:
		try:
			hyperPut = input()
			try:
				hyperPut = hyperPut.strip()
				hyperPut = hyperPut.split(":")
				HyperPutKey = hyperPut[0]
				HyperPutValue = hyperPut[1]
				crudData[HyperPutKey] = HyperPutValue
			except:
				pass
		except KeyboardInterrupt:
			print("\nValores Salvos!\n")
			break


def print_data():
	print(crudData)


while True:
	try:
		print("o que vc deseja fazer?: ", end="")

		commandPut = input()
		commandPut = commandPut.strip()
		#commandPut = commandPut.split()

		if commandPut == "help" or commandPut == "Help":
			print("""
Comandos:

Put-Data: colocar chaves/valores novos no dict

Write-Host-Data: retorna em dict/json o crud

Update-Data: substitui o valor de determinada chave

Delete-Data: deleta a chave com o valor

Delete-All: Deleta todas as chaves com todos os valores

List-All-Data: Lista todos os valores num formato legivel e copiavel

Super-Put: Permite colocar valores em formato json no dict/crud

Exit: sai do programa :)

Hyper-Put: Util para inserir varios valores de uma só vez, usando a notação [chave: valor] (sem as chaves), possibilita inserir mais valores apenas dando enter e inserindo mais, e para finalizar uma requisição de keyboardinterrupt (Ctrl+C) para salvar todos os dados :)
				""")
		elif commandPut == "Put-Data":
			put_data()
		elif commandPut == "Write-Host-Data":
			print_data()
		elif commandPut == "Update-Data":
			edit_data()
		elif commandPut == "Delete-Data":
			delete_data()
		elif commandPut == "Delete-All":
			delete_all()
		elif commandPut == "List-All-Data":
			print_all()
		elif commandPut == "Super-Put":
			super_put()
		elif commandPut == "Hyper-Put":
			hyper_put()
		elif commandPut == "":
			pass
		elif commandPut == "Exit" or commandPut == "exit":
			exit()
			break
		else:
			print("""comando não existente ou digitado incorretamente, tente novamente ou digite "Help" sem aspas para ter ajuda com os comandos""")
	except KeyboardInterrupt:
		print("""\n\nPara sair digite "Exit" ou "exit" na barra de comandos, por favor!\n""")