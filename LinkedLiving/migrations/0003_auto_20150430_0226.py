# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LinkedLiving', '0002_auto_20141125_0044'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthConcern',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelativeInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=75)),
                ('relationship', models.CharField(max_length=2, choices=[(b'CH', b'Child'), (b'GC', b'Grandchild'), (b'SI', b'Sibling'), (b'OR', b'Other Relatives'), (b'FR', b'Friend'), (b'DO', b'Doctor')])),
                ('privacy_dashboard', models.BooleanField(default=True)),
                ('privacy_narrative', models.BooleanField(default=True)),
                ('privacy_hr_chart', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserConcernMapping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('concern', models.ForeignKey(to='LinkedLiving.HealthConcern')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
                ('password', models.CharField(max_length=15)),
                ('user_name', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=1, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('bday', models.DateField()),
                ('height', models.DecimalField(max_digits=5, decimal_places=2)),
                ('weight', models.DecimalField(max_digits=4, decimal_places=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userconcernmapping',
            name='user',
            field=models.ForeignKey(to='LinkedLiving.UserInformation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='relativeinformation',
            name='user',
            field=models.ForeignKey(to='LinkedLiving.UserInformation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gearsensor',
            name='user',
            field=models.ForeignKey(to='LinkedLiving.UserInformation', null=True),
            preserve_default=True,
        ),
    ]
