from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Tag(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=221)
    slug = models.SlugField(unique=True, editable=False,null=True)
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    UNIT = (
        (0, "Kilogram"),
        (1, "Gram"),
        (2, "Litre"),
        (3, "Piece"),
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')    # <modelnanem>_set
    title = models.CharField(max_length=221)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.IntegerField(choices=UNIT, default=1)     # get_<field_name>_display
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


def recipe_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        import random
        instance.slug = slugify(instance.title + str(random.randint(1000, 9999)))


pre_save.connect(recipe_pre_save, sender=Recipe)















