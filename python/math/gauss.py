import matplotlib.pyplot as plt # biblioteca de plotagem
import numpy as np # biblioteca para trabalhos númericos e com vetores e espaços de tempo
from scipy import special # importando funções especiais importantes para trabalhos cientificos com python 

erf = special.erf # pegando apenas a função erro de Gauss, entre todas elas

z = np.linspace(-3,3,100) # criando um espaço amostral de 100 termos de -3 à 3

e = erf(z) # aplicando a função er
plt.style.use('seaborn') # editando o estilo da plotagem
plt.subplots(figsize=(9,5)) # configurando o tamanho do plot pra 3x2
plt.plot(z,e) # colocando os termos das axis y e x

plt.title('função erro de Gauss') # titulo
plt.savefig('gauss_plot.png',dpi=800) # salvando fig com densidade de pixel de 800 dpi