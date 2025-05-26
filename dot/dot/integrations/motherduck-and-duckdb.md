# Motherduck & DuckDB

## Motherduck

1. Get your token on [Motherduck Settings](https://app.motherduck.com/settings)

<figure><img src="../../.gitbook/assets/grafik (34).png" alt=""><figcaption></figcaption></figure>



2.  Compose your connection string

    It follows this pattern. `md:<database_name>?motherduck_token=<your_token>`\
    e.g.: `md:sample_data?motherduck_token=eyABC...`



**Notes**

The Motherduck connector requires DuckDB to be at least v.0.10.2



## DuckDB

If you have your data in a local duckdb file you can either host it yourself (e.g. on S3) or [talk to us](../support.md).
