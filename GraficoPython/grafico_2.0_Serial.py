# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import serial
from time import sleep
import datetime
import MySQLdb
#import snmptrap_send

db = MySQLdb.connect("localhost","root","password","dados")

curs=db.cursor()

now = datetime.datetime.now()

port = '/dev/ttyACM0'
ser = serial.Serial(port, 9600, timeout=0)

while True:
    arq0 = open('/var/www/html/data.txt','r')
    texto0 = arq0.readlines()

    arq1 = open('/var/www/html/data1.txt','r')
    texto1 = arq1.readlines()
    
    arq2 = open('/var/www/html/data2.txt','r')
    texto2 = arq2.readlines()

    
    now = datetime.datetime.now()
    
    data = ser.read(9999)

    #print data
    
    if len(data) > 0:

        #Temperatura 0
        if'[AD0]'in data:
            info0  = str(data[8:19])
            value0 = str(data[20:25])
            ad0    = str(data[0:5])

            try:
                if (float(value0)>=14) and (float(value0)<=40):
                    texto0.append(now.strftime("%d-%b-%y %H:%M"))
                    texto0.append('\t')
                    texto0.append(value0)
                    texto0.append('\n')
                    arq0 = openarquivo = open('/var/www/html/data.txt','w')
                    arq0.writelines(texto0)
                    print"Gráfico temperatura 1 gerado com sucesso"
                    arq0.close()
                else:
                    print "Erro nos valores capturados pelo sensor 1"
            except:
                print"Erro na leitura dos sensores"
                    
            #print info0
            #print value0
            #print ad0

            #try:
                #if int(value0) > 30:
                   # print'Temperatura Acima do Esperado'
                #else:print'Temperatura Normal'
            #except:'Erro no alerta de temperatura'
                   
            valores0 =  (info0,value0,ad0)

        #Temperatura 1
        if'[AD1]'in data:
            info1  = str(data[33:44])
            value1 = str(data[45:50])
            ad1    = str(data[25:30])
            
            try:
                if (float(value1)>=14) and (float(value1)<=40):
                    texto2.append(now.strftime("%d-%b-%y %H:%M"))
                    texto2.append('\t')
                    texto2.append(value1)
                    texto2.append('\n')
                    arq2 = openarquivo = open('/var/www/html/data2.txt','w')
                    arq2.writelines(texto2)
                    print"Gráfico temperatura 2 gerado com sucesso"
                    arq2.close()
                else:
                    print "Erro nos valores capturados pelo sensor 2"
            except:
                print"Erro na leitura dos sensores"
                
            #print info1
            #print value1
            #print ad1

            #try:
                #if int(value0) > 30:
                   # print'Temperatura Acima do Esperado'
                #else:print'Temperatura Normal'
            #except:'Erro no alerta de temperatura'
            
            valores1 =  (info1,value1,ad1)

        #Umidade    
        if'[AD4]'in data:
           info4  =  str(data[58:65]) #22
           value4 =  str(data[70:75])
           ad4    =  str(data[50:56])

           try:
            
               if (float(value4)>=5) and (float(value4)<=99):
                   texto1.append(now.strftime("%d-%b-%y %H:%M"))
                   texto1.append('\t')
                   texto1.append(value4)
                   texto1.append('\n')
                   arq1 = openarquivo = open('/var/www/html/data1.txt','w')
                   arq1.writelines(texto1)
                   print"Gráfico umidade gerado com sucesso"
                   arq1.close()
               else:
                   print "Erro nos valores capturados pelo sensor 2"
           except:
                print"Erro na leitura dos sensores"
           #arq4 = open('/var/www/umidade0.txt','w')
           #texto4 = []
           #texto4.append(value4)

           #arq4.writelines(texto4)
           #arq4.close()

           #print info4
           #print value4
           #print ad4

           valores4 = (info4,value4,ad4)

        #Potência 1
        if'[AD5]'in data:
           info5  =  str(data[83:91])#47
           value5 =  str(data[95:102])
           ad5    =  str(data[75:80])

           #arq5 = open('/var/www/potencia0.txt','w')
           #texto5 = []
           #texto5.append(value5)

           #arq5.writelines(texto5)
           #arq5.close()

           #print info5
           #print value5
           #print ad5

           valores5 = (info5,value5,ad5)

           #Sensor D'Agua
        if'[AD3]'in data:
           info3  =  str(data[110:116]) #74
           value3 =  str(data[122:123])
           ad3    =  str(data[102:107])


           #arq3 = open('/var/www/agua0.txt','w')
           #texto3 = []
           #texto3.append(value3)

           #arq3.writelines(texto3)
           #arq3.close()

           #print info3
           #print value3
           #print ad3

           valores3 = (info3,value3,ad3)
        
        
           
           #Gravação de dados para o Protocolo Snmp
           arq = open('/var/www/dados.txt','w')
           texto = []
           texto.append("temperatura1,")
           texto.append(value0)
           texto.append("\n")
           texto.append("temperatura2,")
           texto.append(value0)
           texto.append("\n")
           texto.append("umidade,")
           texto.append(value4)
           texto.append("\n")
           texto.append("agua,")
           texto.append(value3)
           texto.append("\n")
           texto.append("potencia,")
           texto.append(value5)

           arq.writelines(texto)
           arq.close()


                  
    try:
        curs.execute("""INSERT INTO dados2 (tdate , ttime, info, value, ad)
                values(CURRENT_DATE(),NOW(),%s,%s,%s)""",valores0)
        curs.execute("""INSERT INTO dados2 (tdate , ttime, info, value, ad)
                values(CURRENT_DATE(),NOW(),%s,%s,%s)""",valores1)
        curs.execute("""INSERT INTO dados2 (tdate , ttime, info, value, ad)
                values(CURRENT_DATE(),NOW(),%s,%s,%s)""",valores3)
        curs.execute("""INSERT INTO dados2 (tdate , ttime, info, value, ad)
                values(CURRENT_DATE(),NOW(),%s,%s,%s)""",valores4)
        curs.execute("""INSERT INTO dados2 (tdate , ttime, info, value, ad)
                values(CURRENT_DATE(),NOW(),%s,%s,%s)""",valores5)
                
        db.commit()
        print"Data Committed"
    
    except:
        print"Error: the database is being rolled back"
        db.rollback()
            
    #print data
 
    #print conteudo
    
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
    #arq0.close()  
    #arq1.close()
    #arq2.close()
    sleep(30)       
    #print 'not blocked'
    #snmptrap_send.sendNotification()


#Dados do eixo Y no gráfico.



ser.close()

dados = (30,40,80,90)

#Cores que são aplicadas nas barras.
#r = red (vermelho).
#g = green (verde).
#00FF33 - Cor hexadecimal que faz referencia a um verde claro.
#como podemos ver é possível utilizar varias formatacoes de cores no matplotlib.

cor = ('r','green','#00FF33','blue')

#Valores que irão aparecer no eixo X(senão irão aparecer 1,2,3).
legenda = (2013,2014,2015,2016)

#Vai contar a variável **dados** como a mesma possui 3 valores
#serão criados 3 pontos no gráfico.

eixox = np.arange(len(dados))

#largura da barra.
largura = 0.50

#Variável **ax** cria o eixo(x e y), usando depois o laço for.

ax=plt.axes()

"""
Cria as barras onde:
eixox = São os pontos (1, 2, 3) do eixo x (que será substituído pela legenda).
dados = Valores do eixo y.
largura = Largura das colunas.
color = A cor que cada barra irá ter.
yerr = margem de erro em y (repare que tem uma linha azul no centro
de cada barra) dependendo do valor digitado essa margem aumenta ou diminui.
align = Alinhamento do gráfico se não utilizar este parâmetro
as barras ficam coladas nas bordas do gráfico.
"""
grafico = plt.bar(eixox, dados, largura, color=cor, yerr=5, align='center')

# Laço for fará a leitura e criará cada uma das barras com os parâmetros que foram passados.
for barras in grafico:

    # barras.get_x() faz com que o valor da variável **dados** fique no topo da barra.
    # barras.get_width() dividido por 2.0 faz com que os dados fiquem no centro da barra.
    # Caso contrario os dados ficam alinhados a esquerda.
    ax.text(barras.get_x() + (barras.get_width() / 2.0),

            # Altura dos dados que ficam acima da linha azul (yerr=5).
            # Podem ser utilizadas outras alturas como + 7, + 8,
            # o que ficar melhor no seu gráfico.
            barras.get_height() + 6,

            # Texto a cima das barras e centralizado.
            barras.get_height(), ha='center')

# Cria os pontos do eixo x (1, 2, 3).
# Sem isso a variável legenda fica alinhada a esquerda
# ao invés de ficar no centro da barra.
ax.set_xticks(eixox)

# Cria a legenda na base das barras.
# 1, 2, 3 = 2013, 2014, 2015.
ax.set_xticklabels(legenda)

# Cria o texto do eixo x.
plt.xlabel('Anos')

# Cria o texto no eixo y.
plt.ylabel('Quantidade')

# Ativa as linhas de grade no gráfico
plt.grid(True)

# Cria a legenda com as cores e o texto que está
# na variável legenda (canto superior direito do gráfico).
plt.legend(grafico, legenda)

# Exibe o gráfico
plt.show()
