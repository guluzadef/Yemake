# Generated by Django 2.2.5 on 2019-10-01 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0013_footer_copyright'),
    ]

    operations = [
        migrations.CreateModel(
            name='Texts_Pages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_page', models.CharField(max_length=255)),
                ('addfood_page', models.CharField(max_length=255)),
                ('example_page', models.CharField(max_length=255)),
                ('example_page1_page', models.CharField(max_length=255)),
            ],
        ),
    ]
