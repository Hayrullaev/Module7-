class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.caregory = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.caregory}'



class Shop:

    _file_name = 'products.txt'

    def get_products(self):
        with open(self._file_name, 'r') as file:
            products = file.read()
        file.close()
        return products

    def add(self, *products):
        for product in products:
            if not self._product_exists(product):
                with open(self._file_name, 'a') as file:
                    file.write(str(product) + '\n')
            else:
                print('Продукт' , product.name, 'уже есть в магазине')

    def _product_exists(self, product):
        products = self.get_products().split('\n')
        return product.name in [x.split(',')[0] for x in products]


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())