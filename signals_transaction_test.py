from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group

@receiver(post_save, sender=User)
def create_group_in_signal(sender, instance, **kwargs):
    print("Signal running, creating group...")
    Group.objects.create(name="temp_group")

def run_test():
    try:
        with transaction.atomic():
            user = User.objects.create(username='txn_test')
            raise Exception("Simulate failure!")
    except:
        pass

    print("Groups in DB:", list(Group.objects.values_list('name', flat=True)))

