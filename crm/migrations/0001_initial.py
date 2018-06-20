# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ClassList',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('class_type', models.SmallIntegerField(choices=[(0, '脱产'), (1, '周末'), (2, '网络班')], default=0)),
                ('semester', models.PositiveSmallIntegerField(verbose_name='学期')),
                ('start_date', models.DateField(verbose_name='开班日期')),
                ('graduate_date', models.DateField(null=True, verbose_name='毕业日期', blank=True)),
                ('branch', models.ForeignKey(to='crm.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(unique=True, verbose_name='课程名字', max_length=64)),
                ('price', models.PositiveSmallIntegerField()),
                ('period', models.PositiveSmallIntegerField(default=5, verbose_name='课程周期(月)')),
                ('outline', models.TextField(verbose_name='课程大纲')),
            ],
        ),
        migrations.CreateModel(
            name='CourseRecord',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('day_num', models.PositiveSmallIntegerField(verbose_name='节次')),
                ('title', models.CharField(verbose_name='本节主题', max_length=64)),
                ('content', models.TextField(verbose_name='本节内容')),
                ('has_homework', models.BooleanField(default=True, verbose_name='本节有作业')),
                ('homework', models.TextField(null=True, verbose_name='作业内容', blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('class_grade', models.ForeignKey(to='crm.ClassList', verbose_name='上课班级')),
            ],
        ),
        migrations.CreateModel(
            name='CustomFollowUp',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('content', models.TextField(verbose_name='跟踪内容')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.SmallIntegerField(choices=[(0, '近期无报名计划'), (1, '一个月内报名'), (2, '两个月内报名'), (3, '已报名')])),
            ],
        ),
        migrations.CreateModel(
            name='CustomInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(default=None, verbose_name='姓名', max_length=64)),
                ('contact_type', models.SmallIntegerField(choices=[(0, 'qq'), (1, '微信'), (2, '手机')], default=0)),
                ('contact', models.CharField(unique=True, max_length=64)),
                ('consult_content', models.TextField(verbose_name='咨询内容')),
                ('status', models.SmallIntegerField(choices=[(0, '未报名'), (1, '已报名'), (2, '已退学')])),
                ('source', models.SmallIntegerField(choices=[(0, 'QQ'), (1, '51CTO'), (2, '百度推广'), (3, '知乎'), (4, '转介绍'), (5, '其他')])),
                ('date', models.DateField(auto_now_add=True)),
                ('consult_course', models.ManyToManyField(to='crm.Course', verbose_name='咨询课程')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(unique=True, max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('class_grades', models.ManyToManyField(to='crm.ClassList')),
                ('customer', models.ForeignKey(to='crm.CustomInfo')),
            ],
        ),
        migrations.CreateModel(
            name='StudyRecord',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('score', models.SmallIntegerField(choices=[(100, 'A+'), (90, 'A'), (85, 'B+'), (80, 'B'), (75, 'B-'), (70, 'C+'), (60, 'C'), (40, 'C-'), (-50, 'D'), (0, 'N/A'), (-100, 'COPY')], default=0)),
                ('show_status', models.SmallIntegerField(choices=[(0, '缺勤'), (1, '已签到'), (2, '迟到'), (3, '早退')], default=1)),
                ('note', models.TextField(null=True, verbose_name='成绩备注', blank=True)),
                ('course_record', models.ForeignKey(to='crm.CourseRecord')),
                ('student', models.ForeignKey(to='crm.Student')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(verbose_name='姓名', max_length=64)),
                ('role', models.ManyToManyField(null=True, to='crm.Role', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='custominfo',
            name='consultant',
            field=models.ForeignKey(to='crm.UserProfile', verbose_name='课程顾问'),
        ),
        migrations.AddField(
            model_name='custominfo',
            name='referral_from',
            field=models.ForeignKey(to='crm.CustomInfo', null=True, blank=True, verbose_name='转介绍'),
        ),
        migrations.AddField(
            model_name='customfollowup',
            name='customer',
            field=models.ForeignKey(to='crm.CustomInfo'),
        ),
        migrations.AddField(
            model_name='customfollowup',
            name='user',
            field=models.ForeignKey(to='crm.UserProfile', verbose_name='跟进人'),
        ),
        migrations.AddField(
            model_name='courserecord',
            name='teacher',
            field=models.ForeignKey(to='crm.CustomInfo'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='course',
            field=models.ForeignKey(to='crm.Course'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='teachers',
            field=models.ManyToManyField(to='crm.UserProfile', verbose_name='讲师'),
        ),
        migrations.AlterUniqueTogether(
            name='courserecord',
            unique_together=set([('class_grade', 'day_num')]),
        ),
        migrations.AlterUniqueTogether(
            name='classlist',
            unique_together=set([('branch', 'course', 'class_type', 'semester')]),
        ),
    ]
