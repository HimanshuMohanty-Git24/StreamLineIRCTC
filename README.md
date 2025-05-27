# 🚄 IRCTC Real-Time Data Pipeline on Google Cloud

<p align="center">
  <img src="https://github.com/user-attachments/assets/d21ac524-d208-48c3-80a5-3b457b4486f0" alt="Project Logo" width="200"/>
</p>

This project simulates a Change Data Capture (CDC)-like real-time data pipeline for a railway booking system (inspired by IRCTC) using GCP-native services. It demonstrates event publishing, streaming, transformation, and real-time analytics.

![Architecture Diagram](https://github.com/user-attachments/assets/d4b25d4a-d8d6-4913-938b-caf8ee087b38)

---

## 📌 Features

* Stream simulated booking events using Google Pub/Sub
* Transform and enrich data using Apache Beam with Python UDF
* Load transformed records into BigQuery for real-time analytics
* Route failed records to an error table (dead-letter queue)
* Connect to BI tools for live dashboards

---

## 🧰 Tech Stack

| Logo                                                                                              | Service                   | Purpose                                      |
| ------------------------------------------------------------------------------------------------- | ------------------------- | -------------------------------------------- |
| <img src="https://c0.klipartz.com/pngpicture/115/315/gratis-png-plataforma-de-nube-de-google-publicar-suscribir-patrones-de-computacion-en-la-nube-de-bigquery-google.png" alt="PubSub" width="40"/>     | **Google Cloud Pub/Sub**  | Real-time message ingestion                  |
| <img src="https://www.vhv.rs/dpng/d/615-6150272_google-dataflow-logo-hd-png-download.png" alt="Dataflow" width="40"/> | **Google Cloud Dataflow** | Stream processing (Apache Beam + Python UDF) |
| <img src="https://static.cdnlogo.com/logos/g/44/google-bigquery.svg" alt="BigQuery" width="40"/> | **Google BigQuery**       | Analytics-ready data warehouse               |
| <img src="https://w7.pngwing.com/pngs/799/196/png-transparent-google-cloud-platform-google-storage-amazon-s3-cloud-computing-cloud-computing-blue-angle-cloud.png" alt="GCS" width="40"/>       | **Google Cloud Storage**  | Stores UDF Python script                     |
| 🐍                                                                                                | **Python**                | Used for mock data generation and UDF logic  |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/irctc-realtime-pipeline.git
cd irctc-realtime-pipeline
```

### 2. Set GCP Environment Variables

```bash
export PROJECT_ID="your-gcp-project-id"
export TOPIC_ID="irctc-data"
```

### 3. Create Pub/Sub Topic

```bash
gcloud pubsub topics create irctc-data
```

### 4. Upload UDF Script to GCS

```bash
gsutil cp transform_udf.py gs://your-bucket-name/pubsub-to-bigquery/
```

📷 **Screenshot: GCS Bucket**
![GCS Bucket](https://github.com/user-attachments/assets/61542455-821d-4cf9-b969-1ab7d0b0c6de)

### 5. Deploy Dataflow Job (Streaming)

Use the Google Cloud Console or CLI to create a Dataflow job with:

* Input: `irctc-data` topic
* Output: BigQuery table
* UDF location: GCS path to `transform_udf.py`

📷 **Screenshot: Dataflow Job**
![Dataflow Job](https://github.com/user-attachments/assets/7bad43c7-d379-45d4-b5c8-0d8b64794c87)

---

## 🚀 Run the Publisher

```bash
python data_generator.py
```

This script will:

* Generate mock booking activity data
* Encode as JSON
* Publish to `irctc-data` topic on Pub/Sub

📷 **Screenshot: CLI Output**
![CLI Output](https://github.com/user-attachments/assets/fe8e572e-5994-464b-a8df-701173463786)

---

## 🗃️ BigQuery Schema

```sql
CREATE TABLE irctc_dwh.irctc_stream_tb (
  row_key STRING,
  name STRING,
  age INT64,
  email STRING,
  join_date DATE,
  last_login TIMESTAMP,
  loyalty_points INT64,
  account_balance FLOAT64,
  is_active BOOL,
  inserted_at TIMESTAMP,
  updated_at TIMESTAMP,
  loyalty_status STRING,
  account_age_days INT64
);
```

📷 **Screenshots: BigQuery Console**
![BigQuery Preview 1](https://github.com/user-attachments/assets/7a42645f-0b4d-41b2-83ae-233707d53144)
![BigQuery Preview 2](https://github.com/user-attachments/assets/93d502e5-0724-4484-ba5f-48e9d287983d)

---

## 📊 Analytics & Dashboards

Connect BigQuery table to:

* **Looker Studio**
* **Power BI**
* **Tableau**
* Or build a custom UI using BigQuery APIs

---

## 🧪 Test Cases

| Scenario            | Expected Result       |
| ------------------- | --------------------- |
| Valid JSON          | Stored in main table  |
| Malformed JSON      | Stored in error table |
| Points > 500        | Status = Platinum     |
| Missing `join_date` | Age = 0               |

---

## 🧠 Learnings

* Using GCP-native tools for scalable streaming
* Data enrichment with UDFs
* Error handling with fallback strategies

---

## 📎 References

* [Google Cloud Pub/Sub Docs](https://cloud.google.com/pubsub/docs)
* [Google Cloud Dataflow Docs](https://cloud.google.com/dataflow/docs)
* [Google BigQuery Docs](https://cloud.google.com/bigquery/docs)
* [Cloud Storage Docs](https://cloud.google.com/storage/docs)
