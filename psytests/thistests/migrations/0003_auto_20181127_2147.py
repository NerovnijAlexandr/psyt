# Generated by Django 2.0.9 on 2018-11-27 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thistests', '0002_auto_20181127_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_score', models.IntegerField(verbose_name='Нижняя граница по баллам')),
                ('max_score', models.IntegerField(verbose_name='Верхняя граница по баллам')),
                ('result', models.CharField(max_length=2000, verbose_name='Вердикт')),
                ('test_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thistests.Name', verbose_name='Тест')),
            ],
            options={
                'verbose_name_plural': 'Результаты по тесту',
                'verbose_name': 'Результат по тесту',
            },
        ),
        migrations.RemoveField(
            model_name='game',
            name='description',
        ),
        migrations.AddField(
            model_name='game',
            name='result',
            field=models.CharField(default='', max_length=2000, verbose_name='Вердикт'),
        ),
        migrations.AlterField(
            model_name='ask',
            name='test_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thistests.Name', verbose_name='Тест'),
        ),
        migrations.AlterField(
            model_name='game',
            name='test_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thistests.Name', verbose_name=''),
        ),
    ]
