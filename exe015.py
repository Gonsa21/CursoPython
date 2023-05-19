km = float(input('Quantidade de km rodados: '))
dia = float(input('Quantos dia ficou alugado: '))
vdia = 60 * dia
vkm = .15 * km
print('Pela quantidades de dia alugados será pago R$ {}, e pelos km rodados será pago R$ {:.2f}, dando um total de R$ {} a ser pago.'.format(vdia, vkm, vkm + vdia))
