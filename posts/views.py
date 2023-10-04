from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ConversionRequest
from .tasks import convert_video_to_mp3  # Импортируйте функцию для асинхронной конвертации

@csrf_exempt
def convert_video(request):
    if request.method == 'POST':
        video_url = request.POST.get('video_url')
        email = request.POST.get('email')
        
        # Создайте объект ConversionRequest и сохраните его в базе данных
        conversion_request = ConversionRequest.objects.create(video_url=video_url, email=email)
        
        # Запустите задачу на асинхронную конвертацию
        convert_video_to_mp3.apply_async(args=[conversion_request.id])
        
        return JsonResponse({'message': 'Запрос на конвертацию принят.'})
    
    return JsonResponse({'error': 'Метод не поддерживается.'})

# Добавьте представление для проверки статуса и отправки писем, если необходимо

