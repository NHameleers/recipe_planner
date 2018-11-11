# Generated by Django 2.1.3 on 2018-11-11 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_planner', '0004_auto_20181110_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='recipes',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='recipe_planner.Ingredient'),
        ),
    ]