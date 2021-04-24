from django.conf import settings
from django.db import migrations


our_site = {
    "domain": "orchard.cool",
    "name": "Orchard Prototype",
}


def set_site_name(apps, schema_editor):
    Site = apps.get_model("sites", "Site")
    Site.objects.update_or_create(id=settings.SITE_ID, defaults=our_site)


class Migration(migrations.Migration):
    dependencies = [("sites", "0001_initial")]
    operations = [migrations.RunPython(set_site_name)]
