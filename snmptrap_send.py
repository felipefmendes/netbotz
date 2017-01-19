# -*- coding: utf-8 -*-
from pysnmp.hlapi import *
errorIndication, errorStatus, errorIndex, varBinds = next(
    sendNotification( #método de notificação
        snmpEngine(), 
        CommunityData('public', mpModel=0),#Passa a community public
        UpdTransportTarget(('demo.snmplabs.com', 162)),#Url de destino + porta
        ContextData(),#Dados
        'trap',
        NotificationType( #Tipo de notificação
            ObjectIdentity('1.3.6.1.6.3.1.1.5.2') #Identidade do Objeto
        ).addVarBinds(#Range de envio
            ('1.3.6.1.6.3.1.1.4.3.0', '1.3.6.1.4.1.20408.4.1.1.2'),
            ('1.3.6.1.2.1.1.1.0', OctetString('my system'))
        )
    )
)

if errorIndication:#Erro 
    print(errorIndication
          )
