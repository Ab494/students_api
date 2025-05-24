from celery import shared_task
@shared_task
def greet_student(name):
    print(f"Helo {name}, welcome!")