"""Задание

Создать базовый шаблон для интернет-магазина, содержащий общие 
элементы дизайна (шапка, меню, подвал), и дочерние шаблоны для 
страниц категорий товаров и 
отдельных товаров. Например, создать страницы «Одежда», 
«Обувь» и «Куртка», используя базовый шаблон."""



from flask import Flask
from flask import render_template

app = Flask(__name__)


_shoes = [{'model': 'Кросовки',
           'description': 'Лучшие красовки',
           'price': 'цена 5 руб',
           'images': 'http://klublady.ru/uploads/posts/2022-03/1646996122_119-klublady-ru-p-obraz-zhenskie-krossovki-naik-foto-140.jpg'
           },]

_jacket = [{'model': 'Куртка',
            'description': 'Лучшие куртка',
            'price': 'цена 9 руб',
            'images': 'https://b-present.ru/wa-data/public/shop/products/63/30/23063/images/109152/109152.970.jpg'
            },]

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/shoes/')
def shoes():
    return render_template('product.html', shoes=_shoes)

@app.route('/jacket/')
def jacket():
    return render_template('product.html', jacket=_jacket)

if __name__ == '__main__':
    app.run()
