# Data Warehouse Management with Airflow on Google Cloud Platform

![Project Architecture](https://github.com/user-attachments/assets/fe6cf0d0-5856-42dc-b57b-94981b9f5ef8)

## Project Description

This project demonstrates an automated pipeline for managing an Apache Hive data warehouse on Google Cloud Platform (GCP) using Apache Airflow. The pipeline is designed to efficiently handle daily data ingestion, processing, and storage while optimizing costs and ensuring data integrity.

![DAG Execution Status](https://github.com/user-attachments/assets/6e265e65-2a96-4bf1-8fdc-63f2623d14bf)

## Key Features

- Automated data ingestion from GCP Cloud Storage
- Intelligent DAG triggering using Cloud Run Functions
- Cost-effective data archiving
- Robust input validation and error handling
- Secure cluster management
- Partitioned Hive tables for improved query performance

## Technology Stack

- Google Cloud Platform (GCP)
  - Cloud Storage
  - Dataproc
  - Cloud Run Functions
  - Composer (managed Apache Airflow)
- Apache Hive
- Python
- Linux shell scripting

## Implementation Highlights

1. **Smart Triggering**: Cloud Run Functions trigger the Airflow DAG upon file upload, reducing unnecessary sensor costs.
2. **Data Validation**: Input files are validated before DAG execution to minimize pipeline failures.
3. **Secure Configuration**: Cluster details are stored securely in Airflow variables.
4. **Error Notification**: Email alerts (via Sendgrid API) for invalid file uploads.
5. **Optimized Storage**: Processed files are moved to a low-cost archive bucket.
6. **Performance Tuning**: Hive tables are partitioned for faster query execution.

## Setup and Deployment

1. Create GCS buckets for input and archive data
2. Deploy Cloud Run Function for DAG triggering
3. Set up Dataproc cluster for Hive
4. Configure GCP Composer environment for Airflow
5. Develop Airflow DAG with required operators
6. Configure Sendgrid API for email notifications
7. Link Cloud Run Function with Airflow and Sendgrid

## Verification Process

1. Upload a file to the input GCS bucket
2. Confirm DAG triggering or email notification based on file validity
3. Verify data presence in Hive using Dataproc cluster's master node
4. Check successful file archiving

## Further Information

Got the ideas from this Devarapallivamsi, please visit the original project repository:

[Data Warehouse Management using Airflow on GitHub](https://github.com/Devarapallivamsi/DE_projects/tree/master/Data%20Warehouse%20management%20using%20Airflow)

This project showcases effective use of GCP services and Apache Airflow to create a robust, cost-efficient, and automated data warehouse management solution.
