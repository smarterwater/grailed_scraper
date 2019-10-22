import json

def setup():
    print('Setting up ... ')
    brand = input('Brand: ') 
    waist_sz = input('Waist size: ')
    shoe_sz = input('Shoe size (US): ')
    shirt_sz = input('Shirt size (XXS, XS, S, M, L, XL): ')
    price = input('Price limit: ')

    search_terms = {
        'price': price,
        'brand': brand,
        'waist_size': waist_sz,
        'shoe_size': shoe_sz,
        'shirt_size': shirt_sz,
    }

    with open('search_terms.json', 'w') as json_file:
        json.dump(search_terms, json_file)
