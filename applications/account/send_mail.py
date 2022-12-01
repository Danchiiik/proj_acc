from django.core.mail import send_mail

def send_hello(email):
    send_mail(
        'Hello my friend, its me, cool site!', #title
        'Hi, what is up?', #body
        'dcabatar@gmail.com', #from
        [email] #to   
    )