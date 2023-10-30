from cassandra.cqlengine import columns
from django.conf import settings
from django_cassandra_engine.models import DjangoCassandraModel


class Series(DjangoCassandraModel):
    __keyspace__ = settings.CASS_CLUSTER
    __table_name__ = 'series'
    # compound primary key symbol with cluster order by date
    symbol = columns.Text(primary_key=True)
    date = columns.Date(primary_key=True, clustering_order="DESC")
    close = columns.Float()
    open = columns.Float()
    high = columns.Float()
    low = columns.Float()
    volume = columns.Float()
    dividends = columns.Float()
    stock_splits = columns.Float()
    daily_returns = columns.Float()

    class Meta:
        get_pk_field = 'date'

    def validate(self):
        super(Series, self).validate()
