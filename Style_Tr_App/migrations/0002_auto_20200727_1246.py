# Generated by Django 3.0.3 on 2020-07-27 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Style_Tr_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Style_Tr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_content', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('img_style', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Style_Tr_Form',
        ),
    ]
