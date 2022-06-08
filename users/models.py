from django.db import models


class Role(models.Model):
    Roles = (
        ('Task Operator', 'Оператор задач'),
        ('Regular user', 'Обычный пользователь'),
    )
    role_name = models.CharField(max_length=100, choices=Roles, null=True, blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
