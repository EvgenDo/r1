# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tCompany',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cName', models.CharField(max_length=200)),
                ('cAdress', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tGoods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cName', models.CharField(max_length=200)),
                ('cQty', models.IntegerField()),
                ('cPrice', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cName', models.CharField(max_length=200)),
                ('cSignCode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tWaybill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cDate', models.DateTimeField()),
                ('cTotal', models.IntegerField()),
                ('cCompFromID', models.ForeignKey(related_name='cCompFromID', blank=True, to='src.tCompany', null=True)),
                ('cCompToID', models.ForeignKey(related_name='cCompToID', blank=True, to='src.tCompany', null=True)),
                ('cFromID', models.ForeignKey(related_name='cFromID', blank=True, to='src.tUser', null=True)),
                ('cToID', models.ForeignKey(related_name='cToID', blank=True, to='src.tUser', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='tgoods',
            name='cWaybillID',
            field=models.ForeignKey(blank=True, to='src.tWaybill', null=True),
        ),
    ]
