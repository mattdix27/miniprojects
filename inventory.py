class Product:
    def __init__(self,prod_id,name,price,stock=1):
        self.prod_id = prod_id
        self.name = name
        self.price = price
        self.stock = stock
        
    def prod_id_set(self, x):
        self.prod_id = x
    
    def prod_id_get(self):
        return self.prod_id
    
    def name_set(self, x):
        self.name = x
        
    def name_get(self):
        return self.name
    
    def price_set(self, x):
        self.price = x
        
    def price_get(self):
        return self.price
    
    def stock_set(self, x):
        self.stock = x
        
    def stock_get(self):
        return self.stock
    
    def __repr__(self):
        return '{prod_id: ',self.prod_id,'name: ',self.name,'price: ',self.price,'stock: ',self.stock,'}'
    
    def __str__(self):
        return 'Product(product ID = '+self.prod_id+', name = ' +self.name+', price = '+self.price+', stock = '+self.stock+')'

class Inventory:
    def __init__(self, products=[]):
        self.products = products
    
    def add_product(self, product):
        self.products.append(product)
        
    def stock_value(self, inventory):
        total = 0
        for product in inventory:
            total += (price_get(product) * stock_get(product))
        return total