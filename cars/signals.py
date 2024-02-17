from django.db.models.signals import pre_save, post_delete, post_save
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import car, CarInventory
from openai_api.client import get_car_ai_bio

def car_inventory_update():
    cars_count = car.objects.all().count()
    cars_value = car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']
    CarInventory.objects.create(
        cars_count= cars_count,
        cars_value= cars_value
    )

@receiver(pre_save, sender=car)
def car_pre_save(sender, instance, **kwargss):
    if not instance.bio:
        ai_bio = get_car_ai_bio(
            instance.model,
            instance.brand,
            instance.model_year
        )
        instance.bio = ai_bio

@receiver(post_save, sender=car)
def car_post_save(sender, instance, **kwargss):
    car_inventory_update()
    

@receiver(post_delete, sender=car)
def car_post_delete(sender, instance, **kwargss):
    car_inventory_update
    

