# Generated by Django 3.2 on 2022-06-29 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_slot',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='delivery_slot', to='checkout.deliveryslot'),
        ),
        migrations.AlterUniqueTogether(
            name='deliveryslot',
            unique_together={('date', 'timeslot')},
        ),
        migrations.RemoveField(
            model_name='deliveryslot',
            name='order',
        ),
    ]
