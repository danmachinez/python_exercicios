#um produto com valor X, caso pague a vista tem 10% de desconto, caso parcele tem um aumento de 4%
print("-" * 35)
print(" Lojinha do tio Guedes liberalzao")
print("-" * 35)
valor = float(input("Digite o valor do produto para saber o valor parcelado ou a vista: R$ "))
valor_avista = valor - (valor * 0.10)
print()
print("Caso pague o produto a vista o valor será de R${:.2f}".format(valor_avista))
print()
print("*****Lembre-se que pode parcelar em ate 5x*****")
m = int(input("Em quantas vezes prefere parcelar? "))
valor_parcelado = valor * (1 + 0.04) ** m
print()
print("Caso decida parcelar em {}x o valor será de R${:.2f} com {} parcelas de R${:.2f}".format(m, valor_parcelado, m, (valor_parcelado / m)))
print()
print("*" * 49)
print("Obrigado por visitar nossa lojinha, volte sempre!")
print("*" * 49)