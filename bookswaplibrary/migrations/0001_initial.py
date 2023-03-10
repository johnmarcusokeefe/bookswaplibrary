# Generated by Django 4.1.6 on 2023-02-23 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_no', models.CharField(max_length=9)),
                ('street', models.CharField(max_length=200)),
                ('suburb', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=9)),
                ('country', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text='Enter a brief description of the book', max_length=1000)),
                ('isbn', models.CharField(help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, unique=True, verbose_name='ISBN')),
                ('genre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('condition', models.CharField(blank=True, choices=[('e', 'Excellent'), ('g', 'Good'), ('f', 'Fair'), ('m', 'Missing Pages')], default='e', help_text='Book condition', max_length=1)),
                ('status', models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='m', help_text='Book availability', max_length=1)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='bookswaplibrary.book')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookswaplibrary.address')),
                ('books', models.ManyToManyField(to='bookswaplibrary.bookinstance')),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('date_exchanged', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('r', 'Return'), ('n', 'Return Not Required'), ('e', 'Exchanged'), ('s', 'Sold')], default='r', help_text='Return Requirements', max_length=1)),
                ('books', models.ManyToManyField(to='bookswaplibrary.bookinstance')),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrower', to='bookswaplibrary.member')),
                ('exchange_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookswaplibrary.address')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='bookswaplibrary.member')),
            ],
        ),
    ]
