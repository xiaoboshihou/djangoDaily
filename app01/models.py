from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=30)
    publication_date = models.DateTimeField(auto_now_add=True)


class Employee(models.Model):  # 必须是models.Model的子类
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)
    gender = models.BooleanField(default=1)
    birth = models.DateField()
    department = models.CharField(max_length=30)
    salary = models.DecimalField(max_digits=10, decimal_places=1)
    # 1.1、在模型类Employee里直接新增字段，强调：对于orm来说，新增的字段必须用default指定默认值
    publish = models.CharField(max_length=12, default='人民出版社', null=True)
    # 二：删除字段 2.1 直接注释掉字段
    # 三：修改字段 3.1 将模型类中字段修改


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

