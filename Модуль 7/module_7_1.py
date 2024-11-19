
class Product:
    def __init__(self, name:str, weight: float, category: str):
        self.name   = name        # название продукта (строка)
        self.weight = weight      # общий вес товара (дробное число) (5.4, 52.8 и т.п.).
        self.category = category  # категория товара (строка).
    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    __file_name = 'products.txt'
    @staticmethod
    def get_products():
        file = open(Shop.__file_name, 'r')
        file_ = file.read()
        file.close()
        return file_

    def add(*products):
        #file_ = Shop.get_products(self=Shop.__file_name)
        file_ = Shop.get_products()
        file = open(Shop.__file_name, 'a')
        for i in list(products)[1:]:
            if i.name in str(file_):
                print(f'Продукт {i.name} уже есть в магазине')
            else:
              file.write(f'{i}\n')
        file.close()

s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())

# заменить __name_ на __file_name
