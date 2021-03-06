# Generated by Django 2.2.10 on 2021-06-30 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cdb', '0002_auto_20210629_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalTagStatus',
            fields=[
                ('id', models.BigIntegerField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=80)),
                ('description', models.CharField(db_column='description', max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, db_column='created')),
            ],
            options={
                'db_table': 'GlobalTagStatus',
            },
        ),
        migrations.CreateModel(
            name='GlobalTagType',
            fields=[
                ('id', models.BigIntegerField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=80)),
                ('description', models.CharField(db_column='description', max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, db_column='created')),
            ],
            options={
                'db_table': 'GlobalTagType',
            },
        ),
        migrations.AddField(
            model_name='globaltag',
            name='description',
            field=models.CharField(db_column='description', default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='globaltag',
            name='updated',
            field=models.DateTimeField(auto_now=True, db_column='updated'),
        ),
        migrations.AlterField(
            model_name='globaltag',
            name='name',
            field=models.CharField(db_column='name', max_length=80),
        ),
        migrations.AddField(
            model_name='globaltag',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cdb.GlobalTagStatus'),
        ),
        migrations.AddField(
            model_name='globaltag',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cdb.GlobalTagType'),
        ),
    ]
