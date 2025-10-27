import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def thread_check_signal(sender, instance, **kwargs):
    print("Signal thread:", threading.current_thread().name)

def run_test():
    print("Main thread:", threading.current_thread().name)
    User.objects.create(username='thread_test')
