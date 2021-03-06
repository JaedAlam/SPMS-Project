# Generated by Django 3.2.5 on 2021-09-02 21:32

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_alter_user_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment_T',
            fields=[
                ('assessmentID', models.AutoField(primary_key=True, serialize=False)),
                ('assessmentName', models.CharField(max_length=30)),
                ('questionNum', models.IntegerField()),
                ('totalMarks', models.FloatField()),
                ('weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Course_T',
            fields=[
                ('courseID', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('courseName', models.CharField(max_length=50, null=True)),
                ('numOfCredits', models.DecimalField(decimal_places=1, max_digits=2)),
                ('courseType', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Department_T',
            fields=[
                ('departmentID', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('departmentName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_T',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='accounts.user')),
                ('employeeID', models.IntegerField(primary_key=True, serialize=False)),
                ('startDate', models.CharField(default='N/A', max_length=15)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('accounts.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Program_T',
            fields=[
                ('programID', models.AutoField(primary_key=True, serialize=False)),
                ('programName', models.CharField(max_length=70)),
                ('department', models.ForeignKey(default='N/A', on_delete=django.db.models.deletion.CASCADE, to='app.department_t')),
            ],
        ),
        migrations.CreateModel(
            name='School_T',
            fields=[
                ('schoolID', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('schoolName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty_T',
            fields=[
                ('employee_t_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.employee_t')),
                ('rank', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('app.employee_t',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='VC_T',
            fields=[
                ('employee_t_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.employee_t')),
                ('endDate', models.CharField(default='N/A', max_length=15)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('app.employee_t',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Student_T',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='accounts.user')),
                ('studentID', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('enrollmentDate', models.DateField(null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department_t')),
                ('program', models.ForeignKey(default='N/A', on_delete=django.db.models.deletion.CASCADE, to='app.program_t')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('accounts.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Section_T',
            fields=[
                ('sectionID', models.AutoField(primary_key=True, serialize=False)),
                ('sectionNum', models.IntegerField()),
                ('semester', models.CharField(max_length=15)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course_t')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.faculty_t')),
            ],
        ),
        migrations.CreateModel(
            name='Registration_T',
            fields=[
                ('registrationID', models.AutoField(primary_key=True, serialize=False)),
                ('semester', models.CharField(max_length=15)),
                ('year', models.IntegerField(default=2020, null=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.section_t')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student_t')),
            ],
        ),
        migrations.CreateModel(
            name='PrereqCourse_T',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Course', to='app.course_t')),
                ('preReqCourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PreRequisite', to='app.course_t')),
            ],
        ),
        migrations.CreateModel(
            name='PLO_T',
            fields=[
                ('ploID', models.AutoField(primary_key=True, serialize=False)),
                ('ploNum', models.CharField(max_length=5)),
                ('details', models.CharField(max_length=50)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.program_t')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation_T',
            fields=[
                ('evaluationID', models.AutoField(primary_key=True, serialize=False)),
                ('obtainedMarks', models.FloatField()),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.assessment_t')),
                ('registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.registration_t')),
            ],
        ),
        migrations.AddField(
            model_name='department_t',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.school_t'),
        ),
        migrations.AddField(
            model_name='course_t',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.program_t'),
        ),
        migrations.CreateModel(
            name='CO_T',
            fields=[
                ('coID', models.AutoField(primary_key=True, serialize=False)),
                ('coNum', models.CharField(max_length=4)),
                ('thresold', models.FloatField(default=40)),
                ('course', models.ForeignKey(default='N/A', on_delete=django.db.models.deletion.CASCADE, to='app.course_t')),
                ('plo', models.ForeignKey(default='N/A', on_delete=django.db.models.deletion.CASCADE, to='app.plo_t')),
            ],
        ),
        migrations.AddField(
            model_name='assessment_t',
            name='co',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.co_t'),
        ),
        migrations.AddField(
            model_name='assessment_t',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.section_t'),
        ),
        migrations.CreateModel(
            name='Head_T',
            fields=[
                ('faculty_t_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.faculty_t')),
                ('endDate', models.CharField(default='N/A', max_length=15)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('app.faculty_t',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='faculty_t',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department_t'),
        ),
        migrations.CreateModel(
            name='Dean_T',
            fields=[
                ('faculty_t_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.faculty_t')),
                ('endDate', models.CharField(default='N/A', max_length=15)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.school_t')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('app.faculty_t',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
