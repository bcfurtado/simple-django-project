from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='site',
            options={'ordering': ['name']},
        ),
    ]
