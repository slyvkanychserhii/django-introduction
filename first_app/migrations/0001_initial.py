# Generated by Django 5.0.7 on 2024-08-05 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('published_date', models.DateField()),
            ],
            options={
                'verbose_name': 'fiction book',
                'verbose_name_plural': 'fiction books',
                'db_table': 'library_book_from_first_app',
                'ordering': ['-published_date'],
                'get_latest_by': 'published_date',
                'indexes': [models.Index(fields=['title', 'author'], name='library_boo_title_fb807c_idx'), models.Index(fields=['published_date'], name='published_idx')],
                'unique_together': {('title', 'author')},
                'index_together': {('title', 'author')},
            },
        ),
    ]
