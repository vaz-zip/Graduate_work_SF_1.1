from django.db import models
from django.contrib.auth.models import User
# from datetime import datetime


class TechniqueModel(models.Model):
    name = models.CharField(max_length=24, unique=True,
                            verbose_name='Модель техники')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = "Модель техники"

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'default1'        


class EngineModel(models.Model):
    name = models.CharField(max_length=24, unique=True,
                            verbose_name='Модель двигателя')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = "Модель двигателя"


class TransmissionModel(models.Model):
    name = models.CharField(max_length=24, unique=True,
                            verbose_name='Модель трансмиссии')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = "Модель трансмиссии"


class DriveAxleModel(models.Model):
    name = models.CharField(max_length=24, unique=True,
                            verbose_name='Модель ведущего моста')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = "Модель ведущего моста"


class SteerableAxleModel(models.Model):
    name = models.CharField(max_length=24, unique=True,
                            verbose_name='Модель управляемого моста')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = "Модель управляемого моста"


class ServiceCompany(models.Model):
    name = models.CharField(max_length=24, unique=True,
                            verbose_name='Сервисная компания')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = "Сервисная компания"


class Car(models.Model):
    name = models.CharField(max_length=16, unique=True, verbose_name='Имя')
    factory_number = models.CharField(
        max_length=24, unique=True, verbose_name='Заводской номер')
    technique_model = models.ForeignKey(
        TechniqueModel, on_delete=models.CASCADE, verbose_name='Модель техники')
    engine_model = models.ForeignKey(
        EngineModel, on_delete=models.CASCADE, verbose_name='Модель двигателя')
    engine_number = models.CharField(
        max_length=24, verbose_name='Номер двигателя')
    transmission_model = models.ForeignKey(
        TransmissionModel, on_delete=models.CASCADE, verbose_name='Модель трансмиссии')
    transmission_number = models.CharField(
        max_length=24, verbose_name='Номер трансмиссии')
    drive_axle_model = models.ForeignKey(
        DriveAxleModel, on_delete=models.CASCADE, verbose_name='Модель вед. моста')
    drive_axle_number = models.CharField(
        max_length=24, verbose_name='Номер ведущего моста')
    steerable_axle_model = models.ForeignKey(
        SteerableAxleModel, on_delete=models.CASCADE, verbose_name='Модель упр. моста')
    steerable_axle_number = models.CharField(
        max_length=24, verbose_name='Номер управляемого моста')
    supply_contract = models.CharField(
        max_length=24, verbose_name='Договор поставки №, дата.')
    date_of_shipment_from_the = models.DateField(
        verbose_name='Дата отгрузки с завода')
    consignee = models.CharField(max_length=24, verbose_name='Грузополучатель')
    delivery_address = models.CharField(
        max_length=150, verbose_name='Адрес поставки (эксплуатации)')
    equipment = models.CharField(
        max_length=150, verbose_name='Комплектация (доп. опции)')
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Клиент')
    service_company = models.ForeignKey(
        ServiceCompany, on_delete=models.CASCADE, verbose_name='Сервисная компания')

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = 'Машины'

    # def __str__(self):

    #     return self.technique_model.title()


class TypeOfMaintenance(models.Model):
    name = models.CharField(max_length=24, unique=True, verbose_name='Тип ТО')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = "Тип ТО"


# class OrganizationCarriedMaintenance(models.Model):
#     name = models.TextField(unique=True, verbose_name='Организация, проводившая TO')
#     description = models.TextField(verbose_name='Описание')


class TechnicalMintenance(models.Model):
    name = models.CharField(max_length=16, unique=True, verbose_name='Имя')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Mашина')
    type_of_maintenance = models.ForeignKey(TypeOfMaintenance, on_delete=models.CASCADE, verbose_name='Тип ТО')
    date_of_maintenance = models.DateField(verbose_name='Дата проведения ТО')
    оperating_time = models.IntegerField(verbose_name='Наработка, м/час')
    order = models.CharField(max_length=24, verbose_name='№ заказ-наряда')
    date_of_the_order = models.DateField(verbose_name='Дата заказ-наряда')
    service_company = models.ForeignKey(
        ServiceCompany, on_delete=models.CASCADE, verbose_name='Сервисная компания')

    # car = models.ManyToManyField(Car, through='CarTechnicalMintenance', verbose_name='Mашина')

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = "Техническое обслуживание (ТО)"

  


class BrokenUnit(models.Model):
    name = models.CharField(max_length=24, unique=True,
                            verbose_name='Отказавший узел')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = "Отказавший узел"


class RecoveryMethod(models.Model):
    name = models.CharField(
        max_length=124, verbose_name='Способ восстановления')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = "Способ восстановления"


class Complaints(models.Model):
    # рекламации
    name = models.CharField(max_length=16, unique=True, verbose_name='Имя')
    date_of_breakdown = models.DateTimeField(verbose_name='Дата отказа')
    оperating_time = models.IntegerField(verbose_name='Наработка, м/час')
    broken_unit = models.ForeignKey(
        BrokenUnit, on_delete=models.CASCADE, verbose_name='Узел отказа')
    breakdown_description = models.TextField(verbose_name='Описание отказа')
    recovery_method = models.ForeignKey(
        RecoveryMethod, on_delete=models.CASCADE, verbose_name='Способ восстановления')
    spare_parts = models.TextField(
        max_length=200, verbose_name='Используемые запасные части')
    date_restoration = models.DateTimeField(verbose_name='Дата восстановления')
    # downtime = Вычисляемое поле
    service_company = models.ForeignKey(
        ServiceCompany, on_delete=models.CASCADE, verbose_name='Сервисная компания')
    # car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Mашина')

    car = models.ManyToManyField(
        Car, through='CarComplaints', verbose_name='Mашина')

    def downtime(self):
        return (self.date_restoration - self.date_of_breakdown)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = "Рекламации"

    # def downtime(self):
    #     return (self.date_restoration - self.date_of_breakdown)


# class CarTechnicalMintenance(models.Model):
#     # name = models.CharField(max_length=16, unique=True, verbose_name='Имя')
#     car = models.ForeignKey(TechnicalMintenance, on_delete = models.CASCADE)
#     technical_mintenance = models.ForeignKey(Car, on_delete = models.CASCADE)

#     def __str__(self):
#         return '%s' % (self.name)

#     class Meta:
#         verbose_name = "Машина-ТО"


class CarComplaints(models.Model):
    # name = models.CharField(max_length=16, unique=True, verbose_name='Имя')
    car = models.ForeignKey(Complaints, on_delete=models.CASCADE)
    complaints = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = "Машина-рекламации"
