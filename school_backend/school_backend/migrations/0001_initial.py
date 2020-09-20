# Generated by Django 3.1.1 on 2020-09-20 09:55

from django.db import migrations, models
import django.db.models.deletion
import school_backend.models.student
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('max_student_nb', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('student_identification', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_backend.school', validators=[school_backend.models.student.restrict_amount])),
            ],
        ),
    ]