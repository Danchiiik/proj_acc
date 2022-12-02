from django.core.mail import send_mail

def send_hello(email):
    send_mail(
        'Hello my friend, its me, cool site!', #title
        'Hi, what is up?', #body
        'dcabatar@gmail.com', #from
        [email] #to   
    )
    
    
def send_confirmation_email(email, code):
    full_link = f'http://localhost:8000/account/activate/{code}'
    send_mail(
        'User activation',
        full_link,
        'dcabatar@gmail.com',
        [email],
    )