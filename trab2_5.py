# **************************************************************************************
#
#                           Trabaho 2 - Sistemas Operacionais
#                             Contagem de 1 a 10 em Thread com utilização de semáforos
# Nomes: Erica Rodrigues, Gabriel, Túlio Moura, João V. O. Ferreira, Raul V. da Silva
#
# **************************************************************************************

import threading                                        # Importação da Biblioteca utilizada para iniciar uma nova thread
from time import sleep                                  # Importação da função sleep da biblioteca time, utilizada para adiar a execução do código
sema = threading.Semaphore()                            # Declaração do controlador semáforo para sincronização dos threads

def contagem():                                         # Definição da função que fará a contagem de 1 a 1
    aux_var = 1                                         # Variável auxiliar utilizada na função
    for i in range(10):                                 # laço que iterará sobre os objetos da função range por 10 vezes
        sema.acquire()                                  # Chamada do semáforo controlador que reserva o recurso para a função atual
        sleep(1)                                        # função sleep que adiará em 1 segundo a execução da próxima instrução
        print(f"Thread 1: {aux_var}")                   # função print, imprimirá no terminal o valor da variável auxiliar
        aux_var += 1                                    # incrementação da variável auxiliar para cada iteração do laço
        sema.release()                                  # Chamada do semáforo controlador que libera o recurso anteriormente reservado


def declara():                                          # Definição da função que imprime o anuncio de continuação da contagem
    sema.acquire()                                      # Chamada do semáforo controlador que reserva o recurso para a função atual
    print("Thread 2: Continuação:")                     # Função print que imprimirá no terminal a continuação do programa
    sema.release()                                      # Chamada do semáforo controlador que libera o recurso anteriormente reservado


def finaliza():                                         # Definição da função que imprime o fim da contagem
    sema.acquire()                                      # Chamada do semáforo controlador que reserva o recurso para a função atual
    print("Thread 4: Terminou a contagem.")             # Função print que imprimirá no terminal que o programa finalizou as tarefas
    sema.release()                                      # Chamada do semáforo controlador que libera o recurso anteriormente reservado


def continua():                                         # Definição da função que fará a contagem de 11 a 15
    aux_var = 11                                        # Variável auxiliar utilizada na função
    
    for i in range(5):                                  # Laço que iterará sobre os objetos da função range por 10 vezes
        sema.acquire()                                  # Chamada do semáforo controlador que reserva o recurso para a função atual
        sleep(1)                                        # Função print, imprimirá no terminal o valor da variável auxiliar
        print(f"Thread 3: {aux_var}")                   # função print, imprimirá no terminal o valor da variavel repetição
        aux_var += 1                                    # incrementação da variável auxiliar para cada iteração do laço
        sema.release()                                  # Chamada do semáforo controlador que libera o recurso anteriormente reservado



print('{:=^50}'.format(' INICIANDO CONTAGEM '))         # Impressão das linhas que indicam o início da aplicação

t1= threading.Thread(target=contagem).start()           # Criação de uma nova thread que executará a função contagem previamente definida
                                                        # Atraso de 15 segundos para a aplicação principal até seu fim

t2 = threading.Thread(target=declara).start()           # Criação de uma nova thread que irá imprimir no terminal o que o programa continuará
                                                        # Atraso de 3 segundos para a aplicação seguir para a proxima função

t3 = threading.Thread(target=continua).start()          # Criação de uma nova thread que executará a continuação da função de contagem previamente definida
                                                        # Atraso de 2 segundos para a aplicação seguir para a proxima função

t4 = threading.Thread(target=finaliza).start()          # Criação de uma nova thread que irá imprimir no terminal o que o programa finalizou sua atividade





# ***************************************************************************************
# Nesse caso ao invés de executar todas as threads ao mesmo tempo, utilizamos o         #
# mecanismo de controle semáforo. Através dele, podemos definir a ordem execução do     #
# programa de acordo com o que nos melhor atender. Este o semaforo  determina a ordem   #
# de execução reservando o recurso para a função que primeiro surgir na fila das        #
# threads criadas seguindo a ordem de prioridade FIFO                                   #
# **************************************************************************************
