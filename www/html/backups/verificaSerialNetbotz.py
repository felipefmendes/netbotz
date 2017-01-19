#!/usr/bin/env python
#-*- coding:utf-8 -*-
import serial
import time
import datetime

#now = datetime.datetime.now()


locations=['/dev/ttyUSB0']

while 1:
        #arquivo = open('temperaturaumidade.txt','r')
        #conteudo = arquivo.readlines()
        #now = datetime.datetime.now()
    
    
  
        for device in locations:  
                try:  
                        print "Trying...",device
                        arduino = serial.Serial(device, 9600)
                        break
                except:  
                        print "Failed to connect on",device   

        try:
            time.sleep(10*6)
            umid = arduino.read()[:10]
            #temp = arduino.readline()[33:38]
            print(umid)
            #print(temp)
            #conteudo.append(now.strftime("%Y-%m-%d %H:%M")+' '+arduino.readline())        
            #print arduino.read()
            #conteudo.append('\n')
            #arquivo = openarquivo = open('temperaturaumidade.txt','w')
            #arquivo.writelines(conteudo)

            


        except:  
            print "Failed to read!" 

        #arquivo.close()
