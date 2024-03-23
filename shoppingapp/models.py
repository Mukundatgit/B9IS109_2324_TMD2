from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()


from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


SHOP_TYPE = (
    ('1', "Open"),
    ('2', "Closed"),
    ('3', "Coming Soon"),
)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoory"
        verbose_name_plural = "categories"
    

class Shop(models.Model):

    user = models.ForeignKey(User, related_name='User', on_delete=models.CASCADE) 
    title = models.CharField(max_length=300)
    description = RichTextField()
    tags = TaggableManager()
    location = models.CharField(max_length=300)
    shop_type = models.CharField(choices=SHOP_TYPE, max_length=1, verbose_name="Shop Type")
    category = models.ForeignKey(Category,related_name='Category', on_delete=models.CASCADE)
    avg_spend = models.CharField(max_length=30, blank=True, verbose_name="Avg Spend")
    company_name = models.CharField(max_length=300, verbose_name="Branch Name", null=True, blank=True)
    company_description = RichTextField(blank=True, null=True, verbose_name="Branch Description")
    url = models.URLField(max_length=200, verbose_name="Logo")
    last_date = models.DateField(verbose_name="Auto Close Date")
    is_published = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
    picture = models.ImageField(upload_to='images/',null=True)
    
    exclude = ['company_name',]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Shop"
        verbose_name_plural = "Shops"

 

class Applicant(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.shop.title

