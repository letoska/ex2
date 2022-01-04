cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }

def get_shop_list_by_dishes(dishes, person_count):
    order = {}
    for dish, sostav in cook_book.items():
        if dish in dishes:
            for indigrients in sostav:
                i_n = list(indigrients.values())[0]
                q = (int(list(indigrients.values())[1]) * person_count)
                m = list(indigrients.values())[2]
                if dishes[0] == dishes[1]:
                  order[i_n] = {'measure':q*2, 'quantity' :m}
                else:
                  order[i_n] = {'measure':q, 'quantity' :m}
    print(order)
get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)



