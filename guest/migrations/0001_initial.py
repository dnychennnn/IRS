# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('is_banned', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('number', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('Item_text', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('department', models.CharField(max_length=2)),
                ('grade', models.CharField(max_length=1)),
                ('phone', models.CharField(max_length=15)),
                ('start_date', models.DateTimeField(verbose_name='start_time')),
                ('end_date', models.DateTimeField(null=True, verbose_name='end_time')),
                ('number_of_days', models.IntegerField()),
                ('identification', models.CharField(max_length=5)),
                ('person_in_charge', models.CharField(max_length=4)),
                ('is_deleted', models.BooleanField(default=True)),
                ('agent', models.ForeignKey(to='guest.Agent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item',
            name='ItemType',
            field=models.ForeignKey(to='guest.ItemType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='Record',
            field=models.ForeignKey(to='guest.Record'),
            preserve_default=True,
        ),
    ]
