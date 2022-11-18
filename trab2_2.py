"""
***********************************************************************************
 
                           Trabaho 2 - Sistemas Operacionais
            Um programa crie um processo filho. Utilizando a função fork()
Nomes: Erica Rodrigues, Gabriel, Túlio Moura, João V. O. Ferreira, Raul V. da Silva
 
***********************************************************************************
"""

import os    # importando comandos do sistema operacional
import time  # importando várias funções relacionadas à tempo


# Função FILHO
# Laço de repetição exibe o PID desse processo, e o PPID do respectivo processo pai.
# Com função "sleep", o processo (laço) é suspenso e executado somente a cada 5 segundos

def FILHO():
    while True:
        print(f'\nFILHO - PID: {os.getpid()}. PPID (pai do processo FILHO: {os.getppid()}')
        time.sleep(5)

# Função PAI
# Assim como a função Filho, tem um laço que vai exibir na tela o seu PID
# Com função "sleep", o processo (laço) é suspenso e executado somente a cada 5 segundos

def PAI():
    while True:
        print(f'\nPAI: PID {os.getpid()}. PPID (pai do processo PAI): {os.getppid()}')
        time.sleep(5)

# Início do programa
# Exibir o ID do processo do programa atual.
print(f'\n##### ID do processo PAI — PID: {os.getpid()} ##### \n ')

# Cria o processo FILHO com a função fork()
chamada = os.fork()
# Então, agora ambos os processos pai e filho estão em execução

"""
Atráves da condicional "if" obtida pela variavel 'chamada',
Definimos que se o valor de retorno for maior que 0,
A função "PAI" irá ser executada, caso contrario a função "FILHO" será executada.
"""
if chamada > 0:
    PAI()
else:
    FILHO()


