#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
from time import sleep
import datetime
import MySQLdb

db = MySQLdb.connect("localhost","monitor","password","temps")

curs=db.cursor()

now = datetime.datetime.now()

port = '/dev/ttyACM0'
ser = serial.Serial(port, 9600, timeout=0)

while True:
    arquivo = open('temperatura.txt','r')
    conteudo = arquivo.readlines()
    now = datetime.datetime.now()
    
    data = ser.read(9999)
    
    print data
            
    conteudo.append(now.strftime("%Y-%m-%d %H:%M"))
    conteudo.append('\n')
    conteudo.append(data)           
    conteudo.append('\n')
    arquivo = openarquivo = open('temperatura.txt','w')
    arquivo.writelines(conteudo)
    #print conteudo
    
    #x = '[AD0:'
    #for x in data:
        #if ((x==':') & (x+1=='0')):
            #print 'Achou'
    
    #if len(data) > 0:
        #if '[AD0:'in data:
            #temp = data[4:7]
            #print 'Got[0]:', data0            
            #conteudo.append(now.strftime("%Y-%m-%d %H:%M"))
            #conteudo.append(' ')
            #conteudo.append('[AD0]A temperatura é')
            #conteudo.append(temp)
            #conteudo.append('ºC')           
            #print '[AD0]A temperatura é',temp,'ºC'
            #conteudo.append('\n')
            #arquivo = openarquivo = open('temperatura.txt','w')
            #arquivo.writelines(conteudo)
            #sleep(1)
        #if '[AD1:'in data:
            #temp2 = data[12:15]
            #print 'Got[1]:', data1             
            #conteudo.append(now.strftime("%Y-%m-%d %H:%M")
            #conteudo.append(' ')
            #conteudo.append('[AD1]A temperatura é')
            #conteudo.append(temp2)
            #conteudo.append('ºC')           
            #print '[AD1]A temperatura é',temp2,'ºC'
            #conteudo.append('\n')
            #arquivo = openarquivo = open('temperatura.txt','w')
            #arquivo.writelines(conteudo)
            #sleep(1)
        #if '[AD4:'in data4:
            #temp = data4[21:26]
            #print 'Got[4]:', data4             
            #conteudo.append(now.strftime("%Y-%m-%d %H:%M"))
            #conteudo.append(' ')
            #conteudo.append('[AD4]A umidade é')
            #conteudo.append(temp)
            #conteudo.append('%')           
            #print '[AD4]A umidade é',temp,'%'
            #conteudo.append('\n')
            #arquivo = openarquivo = open('temperatura.txt','w')
            #arquivo.writelines(conteudo)
            #sleep(1)   

    arquivo.close()        
    sleep(30)       
    #print 'not blocked'
        

ser.close()
