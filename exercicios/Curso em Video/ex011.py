a = float(input('digite a altura da parede: '))
l = float(input('digite a largura da parede: '))
cores = {'vermelho' : '\033[32m','verde':'\033[32m','amarelo' : '\033[33m','azul': '\033[34m' , 'rosa':'\033[35m', 'peb':'\033[7m','limpa':'\033[m'}
tinta = (a * l)/2
print('a parede tem {}{}{} de altura e {}{}{} de largura, tendo entao uma area de {:.2f}m² logo, precisará de {}{:.2f}{} litros de tinta'.format(cores['verde'],a,cores['limpa'],cores['peb'],l,cores['limpa'],a * l,cores['rosa'],tinta,cores['limpa'],))