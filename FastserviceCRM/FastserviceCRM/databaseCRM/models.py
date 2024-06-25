from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField
from django import forms


#Компания
class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь')
    companyName = models.CharField(verbose_name='Название компании', max_length=100)
    phone = models.CharField(verbose_name='Телефон', max_length=100)
    address = models.CharField(verbose_name='Адрес', max_length=100)
    site = models.CharField(verbose_name='Сайт', max_length=100)
    email = models.CharField(verbose_name='E-mail', max_length=100)
    currency = models.CharField(verbose_name='Валюта', max_length=100)
    # director =
    bik = models.CharField(verbose_name='БИК банка', max_length=8)
    checkingAccount = models.CharField(verbose_name='Расчетный счет', max_length=24)
    unp = models.CharField(verbose_name='УНП', max_length=100)
    bankName = models.CharField(verbose_name='Банк', max_length=50)
    logo = models.ImageField(verbose_name="Логотип", null=True, upload_to='static/img/company/')

    def __str__(self):
        return f'{self.companyName}'

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


#Мастерские
class Workshop (models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, verbose_name='Название компании')
    workshopName = models.CharField(verbose_name='Название мастерской', max_length=100)
    address = models.CharField(verbose_name='Адрес', max_length=100)
    phone = models.CharField(verbose_name='Телефон', max_length=255)
    email = models.CharField(verbose_name='E-mail', null=True, max_length=100)
    WorkShopColor = ColorField(verbose_name='Цвет', default='#FF0000')

    def __str__(self):
        return f'{self.workshopName} {self.address}'

    class Meta:
        verbose_name = 'Мастерская'
        verbose_name_plural = 'Мастерские'

#Контрагенты
class CustomerOrder (models.Model):
    fio = models.CharField(verbose_name='Имя', max_length=100)
    phone = models.CharField(verbose_name='Телефон', max_length=15)
    address = models.CharField(verbose_name='Адрес', max_length=100)
    email = models.CharField(verbose_name='E-mail', max_length=100, null=True)
    DateOfBirth = models.DateField(verbose_name='Дата рождения')
    # advertisingSource =
    saleCard = models.CharField(verbose_name='Скидочная карта', max_length=15, null=True)
    comments = models.TextField(verbose_name='Примечание', null=True)
    serialNumber = models.CharField(verbose_name='Серия/Номер', max_length=9, null=True)
    identificationNumber = models.CharField(verbose_name='Индефикационный номер', max_length=100, null=True)
    issued = models.CharField(verbose_name='Кем выдан', max_length=100, null=True)
    dateIssued = models.DateField(verbose_name='Дата выдачи')

    def __str__(self):
        return f'{self.fio}'

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'


#Типы устройств
class devices(models.Model):
    device = models.CharField(verbose_name='Тип устройства', null=True, max_length=40)

    def __str__(self):
        return f'{self.device}'

    class Meta:
        verbose_name = 'Тип устройства'
        verbose_name_plural = 'Типы устройств'


#Статусы заказов
class StatusOrder (models.Model):
    nameStatus = models.CharField(verbose_name='Статус', max_length=20)
    colorStatus = ColorField(verbose_name='Цвет', default='#FF0000')
    descriptionStatus = models.TextField(verbose_name='Описание')


    def __str__(self):
        return f'{self.nameStatus}'


    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Positions (models.Model):
    namePosition = models.CharField(verbose_name='Должность', null=True, max_length=100)

    def __str__(self):
        return f'{self.namePosition}'


    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


#Сотрудники
class Employees (models.Model):
    nameEmployees = models.CharField(verbose_name='ФИО', max_length=30, null=True)
    phone = models.CharField(verbose_name='Телефон', max_length=30, null=True)
    email = models.CharField(verbose_name='E-mail', max_length=30, null=True)
    address = models.CharField(verbose_name='Адрес', max_length=30, null=True)
    birthday = models.DateField(verbose_name='Дата рождения', null=True)
    positions = models.ForeignKey(Positions, verbose_name='Должность', on_delete=models.CASCADE,  null=True)
    photo = models.ImageField(verbose_name='Фотография', null=True, upload_to='static/img/company/staff')

    def __str__(self):
        return f'{self.nameEmployees} ({self.positions})'


    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'



#Должности


#Марка устройства
class Brand (models.Model):
    nameBrand = models.CharField(verbose_name='Производитель', null=True, max_length=100)


    def __str__(self):
        return f'{self.nameBrand}'

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

class TypeOrder (models.Model):
    typeOrder = models.CharField(verbose_name='Тип заказа', max_length=100)
    descriptionTypeOrder = models.TextField(verbose_name='Описание', max_length=255)


    def __str__(self):
        return f'{self.typeOrder}'

    class Meta:
        verbose_name = 'Тип заказа'
        verbose_name_plural = 'Типы заказа'


def default_datetime(): return datetime.now()




class Order (models.Model):
    workShop = models.ForeignKey(Workshop, verbose_name='Мастерская', on_delete=models.CASCADE, null=True)
    dateCreate = models.DateTimeField(verbose_name='Дата создания', default=default_datetime, null=True)
    typeOrder = models.ForeignKey(TypeOrder, verbose_name='Тип Заказа', on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(CustomerOrder, verbose_name='Заказчик', on_delete=models.CASCADE, null=True, blank=True)
    comments = models.TextField(verbose_name='Комментарии к заказу', null=True)
    malfunction = models.CharField(verbose_name='Неисправность', max_length=100)
    typeDevice = models.ForeignKey(devices, verbose_name='Тип устройства', null=True, on_delete=models.CASCADE, blank=True)
    brand = models.ForeignKey(Brand, verbose_name='Производитель', on_delete=models.CASCADE, null=True, blank=True)
    modelDevice = models.CharField(verbose_name='Модель устройства', null=True, max_length=100)
    color = models.CharField(verbose_name='Цвет устройства', max_length=100)
    equipment = models.CharField(verbose_name='Комплектация', null=True, max_length=100)
    Appearance = models.CharField(verbose_name='Внешний вид', null=True, max_length=100)
    processor = models.CharField(verbose_name='Процессор', null=True, max_length=100)
    ram = models.CharField(verbose_name='Оперативная память', null=True, max_length=100)
    gpu = models.CharField(verbose_name='Видеокарта', null=True, max_length=100)
    storageDevice = models.CharField(verbose_name='Накопитель', null=True, max_length=100)
    estimatedСost = models.IntegerField(verbose_name='Ориентировочная стоимость', null=True)
    manager = models.ForeignKey(Employees, verbose_name='Менеджер', related_name='manager', on_delete=models.CASCADE, null=True)
    master = models.ForeignKey(Employees, verbose_name='Мастер', related_name='master', on_delete=models.CASCADE, null=True)
    deadline = models.DateField(verbose_name='Крайний срок')
    urgently = models.BooleanField(verbose_name='Срочно', default=False)
    status = models.ForeignKey(StatusOrder, verbose_name='Статус', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

def sum_work(count, price):
    print(count * price)

class akts (models.Model):
    order = models.ForeignKey(Order, verbose_name='Заказ', on_delete=models.CASCADE, null=True)
    work = models.CharField(verbose_name='Работа/услуга', max_length=100, null=True)
    count = models.IntegerField(verbose_name="Колличество")
    price = models.FloatField(verbose_name="Цена")
    summ = models.FloatField(verbose_name="Сумма", default=sum_work(2, 2))

