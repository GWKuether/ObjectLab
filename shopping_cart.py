from product import Product


class ShoppingCart():
    def __init__(self, color):
        self.color = color
        self.shopping_carts_products = []
    
    
    
    def add_product_to_cart(self, product_added):
        self.shopping_carts_products.append(product_added)
        


    def how_many_products_inside(self):
        products_inside =  len(self.shopping_carts_products)
        print(f"there are {products_inside} products inside the shopping cart")
    

    def remove_all_products_from_cart(self):
        self.shopping_carts_products.clear()