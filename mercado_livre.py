# Exemplo
# Obtendo produtos do Mercado livre a partir de uma busca realizada pelo usuario


import requests 
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'

produto_nome = input('Qual o produto você deseja ?')
# print(url_base + produto)

response = requests.get(url_base + produto_nome)

#print(response.text)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core ui-search-result--advertisement andes-card--padding-default andes-card--animated'})

for produto in produtos:
    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title ui-search-item__group__element shops__items-group-details shops__item-title'})
    link = produto.find('a', attrs={'class':'ui-search-link'})
    real = produto.find('span', attrs={'class': 'price-tag-fraction'})
    centavos = produto.find('span', attrs={'class': 'price-tag-cents'})

    # print(produto.prettify())
    print('Titulo do Produto: ', titulo.text)
    print('Link do Produto: ', link['href'])
    
    # se nao encontrou os centavos imprime o preco real
    if(centavos):
        print('Preço do Produto: R$', real.text + ',' + centavos.text)
    else:
        print('Preço do Produto: R$', real.text)

    

    print('\n\n')
