"""
***********************************************************************************
 
                           Trabaho 2 - Sistemas Operacionais
                              Contagem de 1 a 10 em Thread
Nomes: Erica Rodrigues, Gabriel, Túlio Moura, João V. O. Ferreira, Raul V. da Silva
 
***********************************************************************************
"""

import threading                                        # Importação da Biblioteca utilizada para iniciar uma nova thread
from time import sleep                                  # Importação da função sleep da biblioteca time, utilizada para adiar a execução do código


def contagem():                                         # Definição da função que fará a contagem de 1 a 10
    aux_var = 1                                         # Variável auxiliar utilizada na função
    for i in range(10):                                 # laço que iterará sobre os objetos da função range por 10 vezes
        sleep(1)                                        # função sleep que adiará em 1 segundo a execução da próxima instrução
        print(aux_var)                                  # função print, imprimirá no terminal o valor da variável auxiliar
        aux_var += 1                                    # incrementação da variável auxiliar para cada iteração do laço
        

print('{:=^50}'.format(' INICIANDO CONTAGEM '))         # Impressão das linhas que indicam o início da aplicação
sleep(3)                                                # Atraso de 3 segundos até a criação da nova thread

threading.Thread(target=contagem).start()               # Criação de uma nova thread que executará a função contagem previamente definida

sleep(15)                                               # Atraso de 15 segundos para a aplicação principal até seu fim
