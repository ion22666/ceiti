# Generated by Django 4.2.2 on 2023-06-21 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apartamente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=100)),
                ('prenume', models.CharField(max_length=100)),
                ('varsta', models.IntegerField(max_length=100000000)),
                ('telefon', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Apartament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etaj', models.IntegerField(max_length=100)),
                ('nrCamere', models.IntegerField(max_length=100)),
                ('pret', models.IntegerField(max_length=100000000)),
                ('metriPatrati', models.IntegerField(max_length=100000)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartamente.agent')),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
