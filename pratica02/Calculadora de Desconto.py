nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

valor_desconto = (porcentagem_desconto / 100) * preco_original

preco_final = preco_original - valor_desconto

print("Produto:", nome_produto)
print("Preço original: R$ {:.2f}".format(preco_original))
print("Desconto: {}%".format(porcentagem_desconto))
print("Valor do desconto: R$ {:.2f}".format(valor_desconto))
print("Preço final com desconto: R$ {:.2f}".format(preco_final))
