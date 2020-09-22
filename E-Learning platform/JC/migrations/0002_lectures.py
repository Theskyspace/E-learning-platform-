# Generated by Django 3.0.5 on 2020-07-20 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('JC', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lectures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, unique=True)),
                ('videofile', models.FileField(null=True, upload_to='videos/', verbose_name='')),
                ('publish', models.DateField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='JC.Category')),
            ],
        ),
    ]
