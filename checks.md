# Checks

Checks control that the data in a table fulfills a defined service level. Checks are mostly used for monitoring data quality dimensions: Completeness, Consistency, Timeliness, Uniqueness, Validity Accuracy.&#x20;

Activated checks are executed on a schedule.



## No-Code Checks

* **Volume** controls row count change is stable. No sudden spikes or drops detected. This is a cheap check that should be enabled for all tables.
* **Schema Change** violates in the case of incompatible changes in the schema, e.g. a column name or data type is changed that down-stream consumers might rely on.
* **Technical Freshness** ensures the data pipeline is running and SQL statements are updating the table. This information is retrieved from the Query-History.&#x20;
  * Parameter: Expected freshness in hours, e.g. 24 hours. This would violate if in the last 24 hours (when checking) the table did not get an update (or the upstream tables in case of a View)
* **Content Freshness** controls that recent rows are added or updated.&#x20;
* **Data Redundancy** checks if there are duplicates in the table according to a set of key columns.
* **Null Values** checks the ratio of null values in a column is in an accepted range.
* **Accepted Categorical Values** checks all categorical columns keep the same values. Only less than 10 distinct values are counted as categorical values and the column shouldn't have more than 30% null values.
* **Stable Numerical Values** checks statistical attributes of numerical columns are stable (min, max, avg, median).



## Custom SQL Checks

Custom checks allow monitoring correctness of business logic, multiple column relationships or validate consistency across tables. An SQL check is considered a failure if it returns rows.

#### Examples

Business Logic: ensure km/h for rows in the car trip table is below 200.  This check would fail if a trip could only take place with an average velocity above 200 km/h.

```sql
SELECT *
FROM db.sh.car_trips
WHERE NOT ( distance_km / duration_h < 200 )
```



Cross Table Consistency: ensure that all model\_id values in car\_trips exist in the car\_models table.

```sql
SELECT *
FROM db.sh.car_trips
WHERE NOT( model_id in (
    SELECT id FROM db.sh.car_models
))
```

##

## Full Table or Delta Check

Most tables in a data warehouse are either fully recreated with each run or only update the most current rows.&#x20;

The timestamp column for checks (at the top) reflects this difference to either check the full table every time or only the last 7 days.&#x20;

The timestamp column should track the creation or update time for records in the table, e.g. created\_at, updated\_at. This column will be used to filter data and compare values over time. If no column is selected, checks are always applied to the full table.



