from django.db import models

class WorkPoint(models.Model):
    addres_location = models.TextField(unique=True)
    data_start_work = models.TextField()  #Когда подклюсена точка?
    cards_and_materials = models.BooleanField() #Карты и материалы доставлены?
    last_card_data = models.PositiveIntegerField() #Дата выдачи последней карты в днях
    count_happy_request= models.PositiveBigIntegerField() #Кол-во одобренных заявок
    count_give_card = models.PositiveIntegerField() #Кол-во выданных карт

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name_task = models.TextField()
    level_task = models.PositiveIntegerField() #Уровень работника
    time = models.FloatField() #Время на задачу в часах
    addres_location = models.TextField(unique=True)
    id_location = models.ForeignKey('WorkPoint', on_delete=models.CASCADE)
    id_curier = models.ForeignKey('users.Curier', on_delete=models.CASCADE)
