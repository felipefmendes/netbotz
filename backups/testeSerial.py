#! /usr/bin/env python
 
import serial
porta = '/dev/ttyUSB0'
baud_rate = 9600
 
 
########################## FUNCAO PARA LER A PORTA #######################
def ler_porta():
 
   try:
 
       Obj_porta = serial.Serial(porta, baud_rate)
       valor = Obj_porta.read()
       print"Valor lido da Serial: ",valor
       Obj_porta.close()
 
   except serial.SerialException:
       print"ERRO: Verifique se ha algum dispositivo conectado na porta!"
 
################################ MAIN ####################################
if __name__=='__main__':
 
 
        ler_porta()
 
 
