# Generated by Django 5.0.6 on 2024-05-20 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0003_autor_livro'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='autores',
            field=models.ManyToManyField(related_name='livros', to='livraria.autor'),
        ),
    ]