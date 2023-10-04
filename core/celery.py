# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установите переменную окружения для настройки Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Создайте экземпляр Celery
app = Celery('myproject')

# Загрузите конфигурацию из настроек Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически загрузите задачи из приложений Django
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
