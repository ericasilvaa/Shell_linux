"""
***********************************************************************************
            Um programa que imprima o PID e PPID do processo em execução

***********************************************************************************
"""

import os     #importando comandos do sistema operacional

#A função getppid () retornar o ID do processo ("pai" do processo chamador).
ppid = os.getppid() 
        
#função getpid () retornar o ID do processo chamador .
pid = os.getpid()           


#Imprimir o ID processo atual
print("O PPID (pai do processo) atual é ", ppid)
print ("O PID do processo atual é", pid)

 
