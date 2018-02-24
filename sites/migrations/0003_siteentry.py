from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_site_add_default_ordering'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('value_a', models.DecimalField(decimal_places=2, max_digits=5)),
                ('value_b', models.DecimalField(decimal_places=2, max_digits=5)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
