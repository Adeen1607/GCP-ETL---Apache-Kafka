# News ETL with Kafka and Hive

**Author:** Mohammed Adeen Shaik  
**Review date:** 11 October 2026

## Research question

How can a small news API extraction travel through a streaming broker into a queryable warehouse?

## Data and provenance

Original GCP Kafka Project.docx coursework report and embedded screenshots.

Source materials are linked from the repository README. Input fingerprints are recorded in [the evidence manifest](evidence.json) so a reader can identify the exact committed artifacts used in this review.

## Method and analytical rationale

The report documents API extraction, Kafka producer and consumer, CSV preparation, HDFS upload and Hive queries. It records 16 loaded articles in the demonstrated query.

## Findings and interpretation

The historical report records **16 articles** in the demonstrated Hive table. This verifies the scope of the documented example, not throughput, latency, fault tolerance or production scale. An exposed credential was removed from the current document; old Git history and provider-side validity are separate concerns.


## Limitations

The 16 records are a historical example, not a throughput benchmark. No executable producer, consumer or infrastructure configuration is committed. Latency, replay behavior and exactly-once guarantees were not measured.

## Reproduction

Use the setup commands and input contract in the [repository README](https://github.com/Adeen1607/GCP-ETL---Apache-Kafka#readme). Open the [notebook catalogue](notebooks.html) for annotated code and saved outputs. Keep raw records and model binaries local; public reports contain aggregate results or source-embedded figures.

## Final visual results

No verified numerical result figure is available in the current evidence. This status is shown explicitly rather than substituting fabricated data.
