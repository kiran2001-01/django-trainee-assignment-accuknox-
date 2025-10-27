import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def slow_signal_handler(sender, instance, **kwargs):
    print("Signal started...")
    time.sleep(5)
    print("Signal finished!")

def run_test():
    print("Creating user...")
    User.objects.create(username='sync_test')
    print("User created!")

