# ***************************************************************************************
# 
#                           Trabaho 2 - Sistemas Operacionais
#            Comunicacao entre processo pai e processo filho utilizando pipe
# Nomes: Erica Rodrigues, Gabriel, Túlio Moura, João V. O. Ferreira, Raul V. da Silva
# 
# ***************************************************************************************

import os, time,pty

def child(pipeout):                                                                                     #Função filho, que vai rodar no processo filho que será criado.         
    msg = " Processo com PID {} enviará essa mensagem ao processo pai".format(os.getpid())              #mensagem que utilizaremos o pipe para rodar. 
    msg = msg.encode()                                                                                  #Concatena a mensagem com o pid do processo filho
    os.write(pipeout, msg)                                                                               #Codifica a mensagem para que possa ser passada pelo pipe
    print(" Processo com PID {} enviou uma mensagem para o processo pai".format(os.getpid()))           #imprime na tela 
    os._exit(os.EX_OK)                                                                                  #Sai do processo filho     
 
def parent():
    pipein, pipeout = os.pipe()                                                                         #Cria um pipe

    if os.fork() == 0:
        child(pipeout)                                                                                  #Se não existir o processo filho, cria um 
    
    while os.fork != 0:
        line = os.read(pipein,64)                                                                       #Lê o que está escrito no pipe e escreve na tela enquanto o programa rodar.
        print("\nPID {} Mensagem recebida do processo filho:\n ---> {}".format(os.getpid(), line.decode()))
        os._exit(os.EX_OK)                                                                              #Sai do processo pai apos ler o conteudo do pipe.
parent()                                                                                                #Chamada principal que inicializa o programa.