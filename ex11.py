# calcular area da parede e qntos litros de tinta serão necessários. Cada litro pinta 02m quadrado
h = float(input('Altura da sua parede:'))
l = float(input('Largura da sua parede:'))
a = h * l
t = a / 2
print('A área da sua parede é de {} metros quadrados'.format(a))
print('Serão necessários {} litros de tinta'.format(t))
