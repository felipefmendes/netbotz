#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial
from time import sleep
import datetime

now = datetime.datetime.now()

port = '/dev/ttyUSB0'
ser = serial.Serial(port, 9600, timeout=0)

while True:
    arquivo = open('temperatura.txt','r')
    conteudo = arquivo.readlines()
    now = datetime.datetime.now()

    data = ser.read(9999)
    if len(data) > 0:
        if 'AD0'in data:
            temp = data[4:7]
            #print 'Got:', data
            #string = str('A temperatura é',temp,'ºC')             
            conteudo.append(now.strftime("%Y-%m-%d %H:%M"))
            conteudo.append(' ')
            conteudo.append('[AD0]A temperatura é')
            conteudo.append(temp)
            conteudo.append('ºC')
            
            print '[AD0]A temperatura é',temp,'ºC'
            #print string 
            conteudo.append('\n')
            arquivo = openarquivo = open('temperatura.txt','w')
            arquivo.writelines(conteudo)
    sleep(1)
    #print 'not blocked'
    arquivo.close()

ser.close()
