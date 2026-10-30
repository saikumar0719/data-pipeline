# How this connects to my other 3 projects

This small project has 4 steps: read, clean, load into a
database, make reports. My other 3 projects do the SAME 4 steps.
Only the tools are bigger, because the data is bigger or comes live.
They are the same shop story, with bigger tools.

## GCP streaming project - gcp-retail-data-platform

Same shop story, but orders come live, second by second, from an app
- not as one file at the end of the day. Google cloud tools do the steps.

| My step here | Their tool | Simple meaning |
|---|---|---|
| Orders coming in, one file | Streaming with Kafka / Pub/Sub | Orders come live, one by one, and wait in a queue line |
| Step 2: clean the rows | Dataflow | A cleaner that works on live data as it flows past |
| Step 3: load into a database | BigQuery | A very big table in Google cloud where reports are made |
| Step 4: reports with SQL | BigQuery SQL | Same SQL questions, asked on the very big table |

 Kafka and Pub/Sub are both queues: a line where live data waits
its turn, so no order is lost when many orders come at once.

## dbt lakehouse project - dbt-lakehouse-bigquery

Same shop story. Here, steps 2 and 3 are done by a tool called dbt.
dbt is just a tool that runs SQL in a fixed order and tests it.

| My step here | Their tool | Simple meaning |
|---|---|---|
| Step 1: raw orders file | Staging (dbt name) | The raw data, with dbt names for the layers |
| Step 2: clean the rows | dbt models in SQL | Cleaning written in SQL, run in a fixed order by dbt |
| Middle clean-and-join work | Intermediate (dbt name) | Half-way tables between clean and reports |
| Step 4: report tables | Marts (dbt name) | Report-ready tables, like my report CSV files |
| My tests | dbt tests | Automatic checks that run with every dbt run |
| No copy here | SCD Type 2 | Keeping old copies when a customer detail changes, so history is not lost |

So: staging = raw, intermediate = cleaning in the middle,
marts = reports. New names, same idea.

## AWS lakehouse project - aws-data-lakehouse

Same shop story. Here the files live in Amazon cloud (AWS),
not on my laptop. Files first, questions later - that is a lakehouse.

| My step here | Their tool | Simple meaning |
|---|---|---|
| Files in my data/ folder | S3 | Cloud folders that keep the raw and clean files |
| Knowing what each table is | Glue | The list that says what each table is: names and columns |
| Steps 3-4: SQL on a database | Athena | Asking SQL questions directly on files kept in S3 |
| One big orders file | Partitioning | Keeping files in year/month/day folders, so a question reads only the days it needs and costs less |
| My bronze-to-gold naming there | Bronze / silver / gold | Raw, clean, reports - the same layers with metal names |

So S3 is the cupboard, Glue is the label list on the cupboard,
and Athena is asking questions about what is inside.

All these projects are the same idea - messy data in, clean data, trusted reports out.
