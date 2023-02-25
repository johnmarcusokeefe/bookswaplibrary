# Generated by Django 4.1.6 on 2023-02-24 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookswaplibrary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='books',
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='MemberCatalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalogue_type', models.CharField(max_length=99)),
                ('booklist', models.ManyToManyField(to='bookswaplibrary.bookinstance')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookswaplibrary.address')),
            ],
        ),
    ]
