# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

#Dados do eixo Y no gráfico.

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
