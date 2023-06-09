# Generated by Django 4.2 on 2023-04-27 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_trip_distance_trip_flight_number_trip_lat_trip_long_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="trip",
            old_name="end_date",
            new_name="endDate",
        ),
        migrations.RenameField(
            model_name="trip",
            old_name="end_location",
            new_name="endLocation",
        ),
        migrations.RenameField(
            model_name="trip",
            old_name="flight_number",
            new_name="flightNumber",
        ),
        migrations.RenameField(
            model_name="trip",
            old_name="start_date",
            new_name="startDate",
        ),
        migrations.RenameField(
            model_name="trip",
            old_name="start_location",
            new_name="startLocation",
        ),
    ]
