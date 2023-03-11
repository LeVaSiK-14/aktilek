from django.db import models

from datetime import date

# Create your models here.

class School(models.Model):
    logo= models.ImageField (upload_to="image/",null=True, blank=True)
    whatsapp=models.URLField(verbose_name='Вотсап',null=True, blank=True)
    twitter= models.URLField(verbose_name='Твиттер',null=True, blank=True)
    facebook= models.URLField(verbose_name='Фейсбук',null=True, blank=True)
    name= models.CharField(max_length=120,verbose_name='Название',null=True, blank=True)
    description= models.TextField(verbose_name='Описание',null=True, blank=True)
    admissiontouniversity= models.CharField(max_length=120,verbose_name='Поступлений в Университет',null=True, blank=True)
    staff = models.CharField(max_length=120, verbose_name='Сотрудников',null=True, blank=True)
    students = models.PositiveIntegerField(verbose_name='Количествое учеников',null=True, blank=True)
    successworkyear= models.CharField(max_length=120,verbose_name='Успешных лет',null=True, blank=True)
    mail= models.EmailField(verbose_name='Почта',null=True,blank=True)
    address=models.CharField(max_length=120,verbose_name= 'Адрес')
    number_1=models.CharField(max_length=120,verbose_name='1 Номер телефона')
    number_2=models.CharField(max_length=120,verbose_name='2 Номер телефона')
    number_3=models.CharField(max_length=120,verbose_name='3 Номер телефона')
    description_2=models.TextField(verbose_name='Описание2',null=True, blank=True)
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name='Школа'
        verbose_name_plural='Школы'

class Teacher(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='teachers')
    position= models.CharField(max_length=120,verbose_name='Должность')
    name= models.CharField(max_length=120,verbose_name='Имя')
    photo  = models.ImageField(upload_to="image/",verbose_name='Фото')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name='Учитель'
        verbose_name_plural = 'Учителя'

class Galeria(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name='galeries')
    photo = models.ImageField(upload_to='image/')
    name = models.CharField(max_length=127,verbose_name='название',null=True)
    def ___str__(self):
        return self.name
    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'


class Rewiew(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='rewies')
    photo = models.ImageField(upload_to='image/')
    name = models.CharField(max_length=127,verbose_name='имя',null=True)
    parent = models.CharField(max_length=127,verbose_name='родитель')
    comment = models.TextField(verbose_name='отзывы')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = verbose_name + 'ы'


class New(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name='news')
    author = models.CharField(max_length=127,verbose_name='автор')
    created_at = models.DateField(auto_now_add=True,verbose_name='Дата создание')
    description = models.TextField(verbose_name='описание')
    name = models.CharField(max_length=127,verbose_name='заголовок',null=True)
    profile_pickture = models.ImageField(upload_to='image/')
    photo = models.ImageField(upload_to='image/')


    def __str__(self):
        return self.author
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


    @property
    def add_dates(self, *args, **kwargs):
        return f'новость была создана {(date.today() - self.created_at).days} дней назад'

    
    # def add_date(self):
    #     day= datetime.today
    #     delta= timedelta(self.created_at)
    #     day_before=((day - delta).days)

    #     return f'{day_before} дней назад'