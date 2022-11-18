# Generated by Django 4.1.3 on 2022-11-18 20:47

from django.db import migrations
import streams.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_articlepagetags_articlepage_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='content',
            field=wagtail.fields.StreamField([('full_richtext', streams.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('cta', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=50, required=True)), ('text', wagtail.blocks.RichTextBlock(features=['bold', 'italic'], required=True)), ('button_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(required=False)), ('button_text', wagtail.blocks.CharBlock(default='Learn more', max_length=40, required=True))]))], blank=True, null=True, use_json_field=None),
        ),
    ]
