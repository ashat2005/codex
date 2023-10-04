from django.core.mail import send_mail

def send_email(subject, message, recipient_list):
    # Здесь вы можете использовать функцию send_mail из Django для отправки писем
    send_mail(subject, message, 'your_email@example.com', recipient_list, fail_silently=False)
