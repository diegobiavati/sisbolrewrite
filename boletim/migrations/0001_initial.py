# Generated by Django 3.1.5 on 2021-01-22 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoBI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=250)),
                ('abreviatura', models.CharField(max_length=250)),
                ('slug', models.SlugField()),
                ('numeroUltimaPagina', models.IntegerField()),
                ('numeroUltimoBI', models.IntegerField()),
                ('iniciaNumeroPagina', models.IntegerField()),
                ('eAditamento', models.BooleanField()),
                ('imprimeBordas', models.BooleanField()),
                ('titulo', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Boletim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paginaInicial', models.IntegerField()),
                ('paginaFinal', models.IntegerField()),
                ('aprovado', models.BooleanField(default=False)),
                ('assinado', models.BooleanField(default=False)),
                ('numeroBI', models.IntegerField()),
                ('assinaConfereBI', models.BooleanField(default=False)),
                ('dataPublicacao', models.DateField()),
                ('slug', models.SlugField()),
                ('tipoPub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boletim.tipobi')),
            ],
        ),
    ]
