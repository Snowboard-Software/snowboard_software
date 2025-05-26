# Motherduck & DuckDB

## Motherduck

1. Get your token on [Motherduck Settings](https://app.motherduck.com/settings)

<figure><img src="../../.gitbook/assets/grafik (34).png" alt=""><figcaption></figcaption></figure>



2.  Compose your connection string

    It follows this pattern. `md:<database_name>?motherduck_token=<your_token>`\
    e.g.: `md:sample_data?motherduck_token=eyABC...`



**Notes**

The Motherduck connector requires DuckDB to be at least v.0.10.2



#### How to analyze Motherduck data in Slack in less than 3 minutes

{% embed url="https://file.notion.so/f/f/4fa2dd81-9b45-4042-8978-01056661dbbc/23346161-92c3-43af-b58f-461cdb996a7d/motherduck-demo.mp4?downloadName=motherduck-demo.mp4&expirationTimestamp=1748282400000&id=1ffa3bb6-fe54-80ce-ac01-ee542070ea89&signature=VRq34BLIun_idszr_lSs1eDRROOOA6Z_rZONN9SOdoU&spaceId=4fa2dd81-9b45-4042-8978-01056661dbbc&table=block" fullWidth="true" %}

## DuckDB

If you have your data in a local duckdb file you can either host it yourself (e.g. on S3) or [talk to us](../support.md).
