# Generated by Django 4.2.6 on 2023-10-29 00:32

from django.conf import settings
from django.db import migrations

from . import create_cassandra_session


def migrate_series(apps, schema_editor):
    session = create_cassandra_session()
    # Create keyspace for Cassandra cluster
    session.execute(
        f"CREATE KEYSPACE {settings.CASS_CLUSTER} with replication = {{'class':'SimpleStrategy'}};"  # NOQA
    )
    # Create series table
    session.execute(
        f"CREATE TABLE {settings.CASS_CLUSTER}.series  (date date, symbol text, close float, open float, high float, low float, volume float, dividends float, stock_splits float, daily_returns float, PRIMARY KEY ((symbol), date)) WITH CLUSTERING ORDER BY (date DESC);"  # NOQA
    )


def reverse_migrate_series(apps, schema_editor):
    session = create_cassandra_session()
    # Drop series table
    session.execute(
        f"DROP TABLE IF EXISTS {settings.CASS_CLUSTER}.series;"
    )
    # Drop keyspace for Cassandra cluster
    session.execute(
        f"DROP KEYSPACE IF EXISTS {settings.CASS_CLUSTER};"
    )


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
            ],
            options={
                'managed': False,
            },
        ),
        migrations.RunPython(
            migrate_series,
            reverse_code=reverse_migrate_series
        ),
    ]
