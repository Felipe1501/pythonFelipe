tuple = (('valor', 'chave'), ('nome', 'Igor Guilherme'), ('idade', 18))

print(tuple)
print(tuple[1][1])

dicionario = dict((x,y) for x, y in tuple)

print(dicionario)

print(dicionario['nome'])
print(dicionario['idade'])

print(type(tuple))
print(type(dicionario))