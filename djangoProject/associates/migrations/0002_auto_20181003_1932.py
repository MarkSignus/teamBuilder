# Generated by Django 2.1.1 on 2018-10-03 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('associates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assoc_availability',
            name='associate_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='associates.associate_table'),
        ),
        migrations.AlterField(
            model_name='assoc_availability',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.availability_levels'),
        ),
        migrations.AlterField(
            model_name='assoc_availability',
            name='week_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.weeks'),
        ),
        migrations.AlterField(
            model_name='assoc_client_relationship',
            name='associate_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='associates.associate_table'),
        ),
        migrations.AlterField(
            model_name='assoc_client_relationship',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.clients'),
        ),
        migrations.AlterField(
            model_name='assoc_client_relationship',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.client_levels'),
        ),
        migrations.AlterField(
            model_name='assoc_partner_relationship',
            name='associate_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='associates.associate_table'),
        ),
        migrations.AlterField(
            model_name='assoc_partner_relationship',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.partner_levels'),
        ),
        migrations.AlterField(
            model_name='assoc_partner_relationship',
            name='partner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.partners'),
        ),
        migrations.AlterField(
            model_name='assoc_skills',
            name='associate_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='associates.associate_table'),
        ),
        migrations.AlterField(
            model_name='assoc_skills',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.skill_levels'),
        ),
        migrations.AlterField(
            model_name='assoc_skills',
            name='skill_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.skills'),
        ),
    ]
