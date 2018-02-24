from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0003_siteentry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
