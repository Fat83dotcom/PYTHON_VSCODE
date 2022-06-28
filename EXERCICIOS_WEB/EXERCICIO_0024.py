'''
Some os preços de uma compra de e-commerce usando list comprehensions, ex:

carrinho.append((produto1, 30))
carrinho.append((produto2, 20))
'''
carrinho = []

carrinho.append(('Produto1', 90))
carrinho.append(('Produto2', 60))
carrinho.append(('Produto3', 70))
carrinho.append(('Produto4', 40))
carrinho.append(('Produto5', 80))
carrinho.append(('Produto6', 190))
carrinho.append(('Produto7', 290))
carrinho.append(('Produto8', 590))

total = sum([produto[1] for produto in carrinho])

print(total)
