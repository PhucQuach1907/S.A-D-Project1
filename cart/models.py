from django.db import models 
from product.models import Product 

class CartItem(models.Model): 
    date_added = models.DateTimeField(auto_now_add=True) 
    quantity = models.IntegerField(default=1) 
    product = models.ForeignKey('product.Product', 
                                on_delete=models.CASCADE, unique=False,
                                default=None) 
    
    class Meta: 
        db_table = 'cart_items' 
        ordering = ['date_added'] 
    
    def total(self): 
        return self.quantity * self.product.price   
    
    def name(self): 
        return self.product.name 
    
    def price(self): 
        return self.product.price 
    
    def get_absolute_url(self): 
        return self.product.get_absolute_url() 
    
    def augment_quantity(self, quantity): 
        self.quantity = self.quantity + int(quantity) 
        self.save()