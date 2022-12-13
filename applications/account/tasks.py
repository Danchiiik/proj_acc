
from django.core.mail import send_mail
from main.celery import app

@app.task    
def send_confirmation_email_celery(email, code):
    import time
    time.sleep(10)
    full_link = f'http://localhost:8000/account/activate/{code}'
    send_mail(
        'User activation',
        full_link,
        'dcabatar@gmail.com',
        [email],
    )
    