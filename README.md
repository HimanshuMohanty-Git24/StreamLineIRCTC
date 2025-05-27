# 🚄 IRCTC Real-Time Data Pipeline on Google Cloud

This project simulates a Change Data Capture (CDC)-like real-time data pipeline for a railway booking system (inspired by IRCTC) using GCP-native services. It demonstrates event publishing, streaming, transformation, and real-time analytics.

![WhatsApp Image 2025-05-27 at 12 19 38 PM](https://github.com/user-attachments/assets/d4b25d4a-d8d6-4913-938b-caf8ee087b38)


---

## 📌 Features

* Stream simulated booking events using Google Pub/Sub
* Transform and enrich data using Apache Beam with Python UDF
* Load transformed records into BigQuery for real-time analytics
* Route failed records to an error table (dead-letter queue)
* Connect to BI tools for live dashboards

---

## 🧰 Tech Stack

* **Google Cloud Pub/Sub** – Event ingestion
* **Google Dataflow** – Stream processing (Apache Beam + Python UDF)
* **Google BigQuery** – Real-time storage and analytics
* **Google Cloud Storage** – Stores transformation scripts
* **Python** – Data generation and transformation logic

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

**📷 Screenshot: GCS Bucket**
![WhatsApp Image 2025-05-27 at 12 19 52 PM (2)](https://github.com/user-attachments/assets/61542455-821d-4cf9-b969-1ab7d0b0c6de)


### 5. Deploy Dataflow Job (Streaming)

Use the Google Cloud Console or CLI to create a Dataflow job with:

* Input: `irctc-data` topic
* Output: BigQuery table
* UDF location: GCS path to `transform_udf.py`

**📷 Screenshot: Dataflow Job**
![WhatsApp Image 2025-05-27 at 12 19 52 PM](https://github.com/user-attachments/assets/7bad43c7-d379-45d4-b5c8-0d8b64794c87)


---

## 🚀 Run the Publisher

```bash
python data_generator.py
```

This script will:

* Generate mock booking activity data
* Encode as JSON
* Publish to `irctc-data` topic on Pub/Sub

**📷 Screenshot: CLI Output**
![WhatsApp Image 2025-05-27 at 12 19 52 PM (1)](https://github.com/user-attachments/assets/fe8e572e-5994-464b-a8df-701173463786)


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

**📷 Screenshot: BigQuery Console**
![WhatsApp Image 2025-05-27 at 12 19 52 PM (3)](https://github.com/user-attachments/assets/7a42645f-0b4d-41b2-83ae-233707d53144)
![WhatsApp Image 2025-05-27 at 12 19 51 PM](https://github.com/user-attachments/assets/93d502e5-0724-4484-ba5f-48e9d287983d)



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

* [Pub/Sub Docs](https://cloud.google.com/pubsub/docs)
* [Dataflow Docs](https://cloud.google.com/dataflow/docs)
* [BigQuery Docs](https://cloud.google.com/bigquery/docs)
