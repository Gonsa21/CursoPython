go = (input('Digite uma letra ou qualquer numero '))
print('1 - A informação {} é um numero?'.format(go), go.isnumeric())
print('2 - A informação {} é do alfabeto?'.format(go), go.isalpha())
print('3 - A informação {} é alfanumerico sem decimal?'.format(go), go.isalnum())
print('4 - A informação {} é um tem só letra maiuscula?'.format(go), go.isupper())
print('5 - A informação {} é um tem só letra minuscula?'.format(go), go.islower())
print('6 - A informação {} é um tem espaços?'.format(go), go.isspace())
