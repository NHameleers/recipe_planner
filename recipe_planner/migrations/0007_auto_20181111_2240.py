# Generated by Django 2.1.3 on 2018-11-11 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_planner', '0006_recipe_last_in_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='last_in_menu',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
