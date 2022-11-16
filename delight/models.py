from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='Check out the high quality products that we have.')
    image = models.ImageField(upload_to='uploads/')


    class Meta:
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.name  


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=100, default='$')
    image1 = models.ImageField(upload_to='uploads/')
    image2 = models.ImageField(upload_to='uploads/')
    image3 = models.ImageField(upload_to='uploads/')
    image4 = models.ImageField(upload_to='uploads/')
    date_posted = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name 


class SavingsProduct(models.Model):
    category = models.ForeignKey(Category, related_name='savings_product', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_before = models.CharField(max_length=100, default='$')
    price_now = models.CharField(max_length=100, default='$')
    image1 = models.ImageField(upload_to='uploads/')
    image2 = models.ImageField(upload_to='uploads/')
    image3 = models.ImageField(upload_to='uploads/')
    image4 = models.ImageField(upload_to='uploads/')
    date_posted = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name 
