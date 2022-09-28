
from validacoes import *
import pickle
import os
from time import sleep
from random import randint
import PySimpleGUI as sg
from getpass import getpass
from datetime import datetime
from datetime import date



def regcliente():
    os.system("cls")
    while True:
        
            print("=="*39)
            

            print('''   
    | ------------- Bem vindos ao menu cadastro! ------------------- |
    | ------------- Cadastrar novos clientes!          [1] --------- |
    | ------------- Extrato!                           [2] --------- |
    | ------------- Alterar dados dos clientes!        [3] --------- |
    | ------------- Voltar ao menu principal           [4] --------- |
    | ============================================================== |
            ''')
            print("=="*39)
            cliente = ' '
            cliente = input("Escolha uma das opções: ")

            if cliente == "1":
                cadastrobanco()
            elif cliente == "2":
                extratoconta()
            elif cliente == "3":
                editadados()
            elif cliente == "4":
                break
            else:
                print('Opção inválida!')            



# ------------------------------------------------------------------------------------------------------- #
# ============================= Funções da parte de cadastro de clientes ================================ #


def listclient(): # Gravando em arquivos.dat
    try:
        clientesb = open("clientesbanco.dat", "rb")
        diciclientes = pickle.load(clientesb)
        clientesb.close()
    except:
        clientesb = open("clientesbanco.dat", "wb")
        clientesb.close()
    return diciclientes

def gravclientes(diciclientes):
    clientesb = open("clientesbanco.dat", "wb")
    pickle.dump(diciclientes, clientesb)
    clientesb.close()


diciclientes = listclient() # Dicionário com os dados dos clientes


# ------------------------------------------------------------------------------------------------------- #

def cadastrobanco():
    hora_atual = datetime.now()
    hora = hora_atual.strftime('%H:%M')
    data = date.today()# Função de cadastramento
    os.system("cls")
    print("=="*50)
    print(''' 
    | ---------------------  Bem vindos ao cadastro de clientes! -------------------------- |
    | ------- Se você ainda não estiver cadastrado, vamos fazer o seu cadastro! ----------- |
    | ===================================================================================== |
            ''')
    print("=="*50)
    while True:
        nome = input('Digite o seu nome: ').strip() # Nome do cliente + verificação de string.
        if validstring(nome):
            break
        else:
            print("Nome inválido!")
    while True:
        email = input("Digite um email válido: ").strip() # Email + verificação de email.
        if validemail(email):
            break
        else:
            print('Email inválido!')
    endereco = input("Informe o seu endereço: ").strip() # Endereço livre.
    complemento = input("Informe um complemento (opcional): ").strip() # Complemento livre.
    valores = float(input("Quanto você espera depositar em sua conta?: ")) # Local que será usado no módulo saque.
    while True:
        senha = ' '
        senha = getpass('Escolha um senha numérica de qualquer tamanho: ').strip() # Peço uma senha de acesso
        if validnum(senha):
            if senha not in diciclientes: # Vereifico se a mesma já consta no sistema
                break
            else:
                print("Senha já cadastrada!")
        else:
            print("Senha inválida!")
    id = gerandid.gera_id()                         
    print(f"Sua ID é {id}")
    
    while True:
        cpf = input("Digite um CPF válido: ").strip() # Peço um CPF + verificação.
        if cadastrocpf(cpf):
            if cpf not in diciclientes:
                diciclientes[cpf] = [nome, email, endereco, complemento, valores, senha, id]
                print(f'''
                      Bem vindo(a) {diciclientes[cpf][0]} ao time, estamos muito felizes em ver você por aqui!
                      Você foi cadastrado no dia {data} e no horário {hora}
                      ''')
               
                gravclientes(diciclientes)
                break
        else:
            print("CPF inválido!")
    input('Aperte alguma tecla para continuar!')
    os.system("cls")
    


# ------------------------------------------------------------------------------------------------------- #




# ------------------------------------------------------------------------------------------------------- #

def editadados(): # Função para alterar os dados.
    os.system("cls")
    print("=="*50)
    print(''' 
    | -------------------  Vamos alterar os seus dados cadastrados! ----------------------- |
    | ------- Se você estiver cadastrado no sistema, poderá alterar os seus dados! -------- |
    | ===================================================================================== |
            ''')
    print("=="*50)
    while True:
        cpf = input("Digite o cpf cadastrado no sistema: ")

        if cadastrocpf(cpf):
            if cpf not in diciclientes:
                print('Usuário não encontrado!')
                break
            else:
                print("Usuário encontrado no sistema!")
                alterar = ' '
                alterar = input("Qual dado você quer alterar do seu cadastro: ").upper().strip() # Peço as novas informações
                if alterar == "nome".strip().upper():
                    novo_nome = input("Digite seu novo nome: ").strip()
                    diciclientes[cpf][0] = novo_nome # Adiciono o novo nome ao dicionário posição nome
                    print('Nome alterado com sucesso!')
                    gravclientes(diciclientes)
                    break
                if alterar == "email".strip().upper():
                    novo_email = input("Digite seu novo email: ").strip()
                    if validemail(novo_email):
                        diciclientes[cpf][1] = novo_email # Adiciono o novo email ao dicionário posição email
                        print("Email alterado com sucesso!")
                        gravclientes(diciclientes)
                        break
                    else:
                        print("Email inválido!")
                if alterar == "endereco".strip().upper():
                    novo_endereco = input("Digite seu novo endereço: ").strip()
                    diciclientes[cpf][2] = novo_endereco # Adiciono o novo endereço ao dicionário posição endereço
                    print("Endereço atualizado com sucesso!")
                    gravclientes(diciclientes)
                    break
                if alterar == "opicional".strip().upper():
                    novo_opcional = input("Digite seu novo endereço opcional: ").strip()
                    diciclientes[cpf][3] = novo_opcional # Adiciono o novo complementoao dicionário posição complemento
                    print("Endereço opcional atualizado com sucesso!")
                    gravclientes(diciclientes)
                    break
            
                if alterar == "senha".strip().upper():
                    nova_senha = input("Digite sua nova senha: ").strip()
                    if validnum(nova_senha):
                        diciclientes[cpf][5] = nova_senha # Adiciono a nova senha ao dicionário posição senha
                        print('Senha atualizada com sucesso!')
                        gravclientes(diciclientes)
                        break
                    else:
                        print("Senha inválida!")
                else:
                    print("Opção inválida!")
        else:
            print("CPF inválido!")
        
    

def extratoconta():
    hora_atual = datetime.now()
    hora = hora_atual.strftime('%H:%M')
    data = date.today()# Função de visualizar clientes cadastrados.
    os.system("cls")
    print("=="*50)
    print(''' 
    | ---------------- Vamos visualizar os seus dados cadastrados! ----------------------- |
    | ------- Se você estiver cadastrado no sistema, poderá consultar seus dados! -------- |
    | ==================================================================================== |
            ''')
    print("=="*50)
    while True:
        cpf = ' '
        cpf = getpass("Digite o seu CPF: ") # Peço o cpf do cliente
        if cadastrocpf(cpf):
            if cpf in diciclientes:
                os.system("cls") # Faço a verificação.
                print("Usuário encontrado!")
                print(f'''
                | =========================== Extrato ======================== |
                | ------------------------------------------------------------ |
                | Data da verificação: {data}
                | Horário da verificação: {hora}
                | Nome: {diciclientes[cpf][0]}                                    
                | Email: {diciclientes[cpf][1]}                                              
                | Endereço: {diciclientes[cpf][2]}                                 
                | Complemento: {diciclientes[cpf][3]}                             
                | Saldo: {diciclientes[cpf][4]}                                   
                | Senha: {diciclientes[cpf][5]}                                     
                | ID: {diciclientes[cpf][6]}                                       
                |                                                              |
                | ------------------------------------------------------------ |
                | ============================================================ |      
                      
                ''')
                conti = input('Press ENTER for continue...')
                os.system("cls")
                break
            else:
                print("Usuário não encontrado!")
                continuar = ' '
                continuar = str(input('Deseja continuar [S/N]: ')).strip().upper() # Pergunto se ele quer continuar caso não for encontrado
                if continuar == "S".upper():
                    extratoconta()
                elif continuar == "N".upper():
                    print('Saindo...')
                    sleep(2)
                    break
                else:
                    print("Opção inválida!")
        else:
            print("CPF inválido!")
# ------------------------------------------------------------------------------------------------------- #


class gerandid():  # gera uma ID para o cliente
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand

                






