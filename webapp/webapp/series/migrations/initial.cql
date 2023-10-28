CREATE KEYSPACE local_cluster with replication = {'class':'SimpleStrategy'};
CREATE TABLE local_cluster.series  (date date, symbol text, close float, open float, high float, low float, volume float, dividends float, stock_splits float, PRIMARY KEY ((symbol), date)) WITH CLUSTERING ORDER BY (date DESC);
