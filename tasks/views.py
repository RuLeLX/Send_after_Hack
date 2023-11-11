from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import *
import jwt, datetime

class OutputTasks(APIView):
    def get(self, request):
        if request.method == "GET":
            TasksList = [
                task for task in Task.objects.all()
            ]
            tasksname = []
            curiers_for_tasks = []
            addres_locations = []
            for task in TasksList:
                tasksname.append(getattr(task, 'name_task'))
                curiers_for_tasks.append(getattr(task, 'id_curier'))
                addres_locations.append(getattr(task, 'addres_location'))

            return Response({
                'id': '1',
                'shortNumber': 'OSC-3910990023',
                'taskName': 'Подписание договора',
                'allocatedTime': '24:52',
                'startAddress': 'ул. Зиповская 3/4, 1 к. 192',
                'endAddress': 'ул. Зиповская 3/4, 1 к. 193',
                'clientName': 'Иван Бородачев',
                'steps': [
                {
                    'icon': 'location-exit',
                    'title': 'Адрес отправления',
                    'detail': 'ул. Зиповская 3/4, 1 к. 192',
                },
                {
                    'icon': 'location-enter',
                    'title': 'Адрес доставки',
                    'detail': 'ул. Зиповская 3/4, 1 к. 193',
                },
                {
                    'icon': 'file-document',
                    'title': 'Статус',
                    'detail': 'Подписание договора',
                },
                {
                    'icon': 'check-all',
                    'title': 'Статус',
                    'detail': 'Завершение встречи',
                },
                ],
                'phone': 'phone',
                'sms': 'message-text',
                 },{
                'id': '1',
                'shortNumber': 'OSC-3910990023',
                'taskName': 'Подписание договора',
                'allocatedTime': '24:52',
                'startAddress': 'ул. Зиповская 3/4, 1 к. 192',
                'endAddress': 'ул. Зиповская 3/4, 1 к. 193',
                'clientName': 'Иван Бородачев',
                'steps': [
                {
                    'icon': 'location-exit',
                    'title': 'Адрес отправления',
                    'detail': 'ул. Зиповская 3/4, 1 к. 192',
                },
                {
                    'icon': 'location-enter',
                    'title': 'Адрес доставки',
                    'detail': 'ул. Зиповская 3/4, 1 к. 193',
                },
                {
                    'icon': 'file-document',
                    'title': 'Статус',
                    'detail': 'Подписание договора',
                },
                {
                    'icon': 'check-all',
                    'title': 'Статус',
                    'detail': 'Завершение встречи',
                },
                ],
                'phone': 'phone',
                'sms': 'message-text',
  }
  )


