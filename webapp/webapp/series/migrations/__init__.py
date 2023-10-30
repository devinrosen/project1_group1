from cassandra.cluster import Cluster
from django.conf import settings


def create_cassandra_session():
    if not hasattr(settings, 'CASS_CLUSTER') or not settings.CASS_CLUSTER:
        raise Exception('Unexpected exception: settings.CASS_CLUSTER not set')

    cluster = Cluster(
        [settings.CASS_HOST],
    )
    return cluster.connect()
