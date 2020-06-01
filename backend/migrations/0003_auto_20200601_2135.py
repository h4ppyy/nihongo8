# Generated by Django 3.0.6 on 2020-06-01 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0002_auto_20200531_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jlpt', models.IntegerField(choices=[('N1', 'JLPT N1'), ('N2', 'JLPT N2'), ('N3', 'JLPT N3'), ('N4', 'JLPT N4'), ('N5', 'JLPT N5'), ('N0', '자격증 없음')], default='N0', max_length=6)),
                ('point', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'auth_userprofile',
            },
        ),
        migrations.DeleteModel(
            name='TblCode',
        ),
        migrations.DeleteModel(
            name='TblCommunity',
        ),
        migrations.DeleteModel(
            name='TblCore',
        ),
        migrations.DeleteModel(
            name='TblCoreEx',
        ),
        migrations.DeleteModel(
            name='TblFile',
        ),
        migrations.DeleteModel(
            name='TblIndexJlpt',
        ),
        migrations.DeleteModel(
            name='TblNotification',
        ),
        migrations.DeleteModel(
            name='TblPointHistory',
        ),
        migrations.DeleteModel(
            name='TblProblem',
        ),
        migrations.DeleteModel(
            name='TblProblemCore',
        ),
        migrations.DeleteModel(
            name='TblProblemLike',
        ),
        migrations.DeleteModel(
            name='TblProblemQuiz',
        ),
        migrations.DeleteModel(
            name='TblQuiz',
        ),
        migrations.DeleteModel(
            name='TblReply',
        ),
        migrations.DeleteModel(
            name='TblReport',
        ),
        migrations.DeleteModel(
            name='TblReReply',
        ),
        migrations.DeleteModel(
            name='TblUser',
        ),
        migrations.DeleteModel(
            name='TblUserJlpt',
        ),
    ]
