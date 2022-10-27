# Generated by Django 4.1.2 on 2022-10-27 08:36

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import uuid
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_alter_feedback_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="FooterContent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "translation_key",
                    models.UUIDField(default=uuid.uuid4, editable=False),
                ),
                ("copyright_text", wagtail.fields.RichTextField()),
                (
                    "locale",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="wagtailcore.locale",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "unique_together": {("translation_key", "locale")},
            },
        ),
        migrations.CreateModel(
            name="FooterItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "translation_key",
                    models.UUIDField(default=uuid.uuid4, editable=False),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                ("title", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("link", models.URLField()),
                (
                    "icon",
                    models.CharField(
                        choices=[
                            ("info", "Info"),
                            ("help", "Help"),
                            ("wagtail", "Wagtail"),
                        ],
                        default="info",
                        max_length=7,
                    ),
                ),
                (
                    "locale",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="wagtailcore.locale",
                    ),
                ),
                (
                    "parent_footer",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="footer_items",
                        to="core.footercontent",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "unique_together": {("translation_key", "locale")},
            },
        ),
    ]