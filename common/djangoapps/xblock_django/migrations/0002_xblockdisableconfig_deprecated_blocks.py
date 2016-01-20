# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xblock_django', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='xblockdisableconfig',
            name='deprecated_blocks',
            field=models.TextField(default=b'', help_text='Adding components in this list will disable the creation of new problem for those components in Studio. Existing problems will work fine and one can edit them in Studio.', blank=True),
        ),
    ]
