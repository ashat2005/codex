from celery import shared_task
from .models import ConversionRequest
from .send_email import send_email

@shared_task
def convert_video_to_mp3(conversion_request_id):
    try:
        # Получите объект ConversionRequest по его идентификатору
        conversion_request = ConversionRequest.objects.get(id=conversion_request_id)
        
        # Здесь должен быть код для конвертации видео в MP3
        # Это может потребовать использования библиотеки, например, youtube-dl и ffmpeg
        
        # После успешной конвертации отправьте письмо с результатами
        send_email(conversion_request.email, 'Конвертация завершена', 'Ссылка на MP3 файл: ...')
        
        # Обновите статус задачи в объекте ConversionRequest
        conversion_request.status = 'COMPLETED'
        conversion_request.save()
    except Exception as e:
        # Если возникла ошибка, обработайте её
        print(f'Ошибка при конвертации видео: {e}')

    