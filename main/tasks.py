
from django.core.mail import send_mail
from main.celery import app

@app.task    
def spam_message():
    send_mail(
        'Hello',
        'Its from us, py24',
        'dcabatar@gmail.com',
        ['dcabatar@gmail.com'],
    )
    