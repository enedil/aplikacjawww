# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-04 12:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wwwapp', '0049_auto_20160423_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='modified_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='articlecontenthistory',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wwwapp.Article'),
        ),
        migrations.AlterField(
            model_name='articlecontenthistory',
            name='modified_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='comments',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='end_date',
            field=models.CharField(choices=[('no_idea', 'Nie ogarniam'), ('16', '16 sierpien'), ('17', '17 sierpien'), ('18', '18 sierpien'), ('19', '19 sierpien'), ('20', '20 sierpien'), ('21', '21 sierpien'), ('22', '22 sierpien'), ('23', '23 sierpien'), ('24', '24 sierpien'), ('25', '25 sierpien'), ('26', '26 sierpien'), ('27', '27 sierpien'), ('28', 'Wybierz inną datę')], default='no_idea', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='meeting_point',
            field=models.CharField(choices=[('no_idea', 'Nie ogarniam'), ('wierchomla', 'Wierchomla Wielka'), ('warsaw', 'Warszawa'), ('cracow', 'Kraków')], default='no_idea', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='pesel',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='start_date',
            field=models.CharField(choices=[('no_idea', 'Nie ogarniam'), ('16', '16 sierpien'), ('17', '17 sierpien'), ('18', '18 sierpien'), ('19', '19 sierpien'), ('20', '20 sierpien'), ('21', '21 sierpien'), ('22', '22 sierpien'), ('23', '23 sierpien'), ('24', '24 sierpien'), ('25', '25 sierpien'), ('26', '26 sierpien'), ('27', '27 sierpien'), ('28', 'Wybierz inną datę')], default='no_idea', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='tshirt_size',
            field=models.CharField(choices=[('no_idea', 'Nie ogarniam'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], default='no_idea', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='cover_letter',
            field=models.TextField(blank=True, default='', max_length=100000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Mężczyzna'), ('F', 'Kobieta')], default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='how_do_you_know_about',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_page',
            field=models.TextField(blank=True, default='', max_length=100000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='school',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='qualification_problems',
            field=models.FileField(blank=True, null=True, upload_to='qualification'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='status',
            field=models.CharField(blank=True, choices=[('Z', 'Zaakceptowane'), ('O', 'Odrzucone')], default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='title',
            field=models.CharField(default='EMPTY', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workshop',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wwwapp.WorkshopType'),
        ),
        migrations.AlterField(
            model_name='workshopuserprofile',
            name='status',
            field=models.CharField(blank=True, choices=[('Z', 'Zaakceptowany'), ('O', 'Odrzucony')], default=None, max_length=10, null=True),
        ),
    ]
