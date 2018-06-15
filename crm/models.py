from django.db import models
from django.contrib.auth.models import User


class CustomInfo(models.Model):
    """客户信息表"""
    name = models.CharField(max_length=64, verbose_name='姓名', default=None)


class UserProfile(models.Model):
    """用户信息表"""
    user = models.ForeignKey(User)
    name = models.CharField(max_length=64, verbose_name='姓名')
    role = models.ManyToManyField('Role', blank=True, null=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    """角色表"""
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class CustomFollowUp(models.Model):
    """客户跟踪记录表"""
    pass


class Course(models.Model):
    """课程表"""
    pass


class ClassList(models.Model):
    """班级列表"""
    pass


class Branch(models.Model):
    """校区"""
    pass


class CourseRecord(models.Model):
    """上课记录"""
    pass


class StudyRecord(models.Model):
    """学习记录表"""
    pass
