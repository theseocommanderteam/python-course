mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here
from random import choice
data_list = mobile_data.get('data')
ex_rate = mobile_data.get('exchnage_rate')


for data in data_list:
    price_bdt = float(data.get('price').split()[0])

    lines = [

        f"{data.get('name')} is made in {data.get('made')}. The price is {data.get('price')} which is almost equal to {round(price_bdt * ex_rate)} BDT",
        f"In {data.get('made')}, {data.get('name')} is made. {data.get('price')} is the price which is almost equal to BDT {round(price_bdt * ex_rate)}",
        f"{data.get('name')} has the price {data.get('price')} that is equivalent to {round(price_bdt * ex_rate)} BDT. It was manufactured in {data.get('made')}."

    ]

    print(choice(lines))
