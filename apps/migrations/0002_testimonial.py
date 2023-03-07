# Generated by Django 4.0.3 on 2022-04-15 03:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='')),
                ('type', models.CharField(choices=[('CUSTOMER', 'customer')], max_length=30)),
                ('content', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]