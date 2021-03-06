# Generated by Django 3.0.6 on 2020-06-07 05:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0002_auto_20200606_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('LKR', 'Language - Kanji Read'), ('LKF', 'Language - Kanji Find'), ('LGR', 'Language - Grammar Rule'), ('LRP', 'Language - Replace'), ('LUF', 'Language - Useful'), ('GE', 'Grammar - Empty'), ('GO', 'Grammar - Order'), ('GL', 'Grammar - Long'), ('RS', 'Reading - Short'), ('RM', 'Reading - Medium'), ('RL', 'Reading - Long'), ('RIU', 'Reading - Integrated understanding'), ('ROU', 'Reading - Opinion understanding'), ('RIS', 'Reading - Information Search'), ('ETC', 'ETC')], default='ETC', max_length=6)),
                ('quiz', models.CharField(blank=True, max_length=255, null=True)),
                ('hangul', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'problem_quiz',
            },
        ),
        migrations.CreateModel(
            name='QuizGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('N1', 'JLPT N1'), ('N2', 'JLPT N2'), ('N3', 'JLPT N3'), ('N4', 'JLPT N4'), ('N5', 'JLPT N5'), ('ETC', 'ETC')], default='ETC', max_length=6)),
                ('type', models.CharField(choices=[('LKR', 'Language - Kanji Read'), ('LKF', 'Language - Kanji Find'), ('LGR', 'Language - Grammar Rule'), ('LRP', 'Language - Replace'), ('LUF', 'Language - Useful'), ('GE', 'Grammar - Empty'), ('GO', 'Grammar - Order'), ('GL', 'Grammar - Long'), ('RS', 'Reading - Short'), ('RM', 'Reading - Medium'), ('RL', 'Reading - Long'), ('RIU', 'Reading - Integrated understanding'), ('ROU', 'Reading - Opinion understanding'), ('RIS', 'Reading - Information Search'), ('ETC', 'ETC')], default='ETC', max_length=6)),
                ('difficult', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'problem_quiz_group',
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('N1', 'JLPT N1'), ('N2', 'JLPT N2'), ('N3', 'JLPT N3'), ('N4', 'JLPT N4'), ('N5', 'JLPT N5'), ('ETC', 'ETC')], default='ETC', max_length=6)),
                ('type', models.CharField(choices=[('N', 'Naming word'), ('V', 'Verb'), ('ADJI', 'adjective I'), ('ADJN', 'adjective N'), ('ADV', 'adverb'), ('ETC', 'ETC')], default='ETC', max_length=6)),
                ('kanji', models.CharField(blank=True, max_length=255, null=True)),
                ('hiragana', models.CharField(blank=True, max_length=255, null=True)),
                ('katakana', models.CharField(blank=True, max_length=255, null=True)),
                ('hangul', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'problem_word',
            },
        ),
        migrations.CreateModel(
            name='WordExample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('example', models.CharField(max_length=255)),
                ('hangul', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Word')),
            ],
            options={
                'db_table': 'problem_word_example',
            },
        ),
        migrations.CreateModel(
            name='QuizUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(blank=True, max_length=255, null=True)),
                ('hangul', models.CharField(blank=True, max_length=255, null=True)),
                ('problem1', models.CharField(max_length=255)),
                ('problem2', models.CharField(max_length=255)),
                ('problem3', models.CharField(max_length=255)),
                ('problem4', models.CharField(max_length=255)),
                ('solve', models.CharField(max_length=255)),
                ('solution', models.CharField(blank=True, max_length=255, null=True)),
                ('point', models.IntegerField(default=0)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Quiz')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'problem_quiz_unit',
            },
        ),
        migrations.CreateModel(
            name='QuizGroupWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.QuizGroup')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Word')),
            ],
            options={
                'db_table': 'problem_quiz_group_word',
            },
        ),
        migrations.CreateModel(
            name='QuizGroupQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Quiz')),
                ('quiz_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.QuizGroup')),
            ],
            options={
                'db_table': 'problem_quiz_group_quiz',
            },
        ),
        migrations.CreateModel(
            name='QuizGroupLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.QuizGroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'problem_quiz_group_like',
            },
        ),
        migrations.AddField(
            model_name='quiz',
            name='quiz_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.QuizGroup'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='PointHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField()),
                ('quiz_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.QuizGroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'problem_point_history',
            },
        ),
    ]
