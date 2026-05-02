# Real-Time Fraud Detection System

## Overview

This project implements a **Real-time fraud detection system** that mimics how modern fintech companies detect fraudulent transactions at scale.

* Real-time streaming
* ML inference service
* Containerization
* End-to-end pipeline

👉 Designed to reflect **industry-level architecture** used in payments and banking systems.

---

## Problem Statement

Detect fraudulent transactions in **real-time (<100ms latency)** using machine learning and streaming infrastructure.

---

##System Architecture

```
Producer → Kafka → Consumer → ML API → Prediction
```

### Flow:

1. Transaction is generated (Producer)
2. Sent to Kafka topic (`transactions`)
3. Consumer reads transaction
4. Sends to FastAPI model service
5. Model predicts fraud probability
6. Decision returned (ALLOW / REVIEW / BLOCK)

---

## Tech Stack

| Layer            | Technology |
| ---------------- | ---------- |
| API              | FastAPI    |
| ML Model         | XGBoost    |
| Streaming        | Kafka      |
| Containerization | Docker     |
| Language         | Python     |
| Serialization    | JSON       |

---

## Project Structure

```
fraud-detection-system/
│
├── data/                     # Generated dataset
├── models/                   # Trained model (.pkl)
├── src/
│   ├── api/                  # FastAPI app
│   ├── models/               # Training scripts
│   ├── features/             # Feature engineering
│   ├── streaming/            # Kafka producer & consumer
│
├── infra/
│   ├── docker/               # Dockerfile & docker-compose
│
├── requirements.txt
└── README.md
```

---

##  Key Features

### Real-Time Streaming

* Kafka-based ingestion pipeline
* Decoupled architecture

###  ML Inference API

* FastAPI-based low-latency service
* Returns fraud score + decision

### Behavioral Feature Engineering

* Foreign transaction detection
* Deviation from user average
* Transaction-based features

###  Production Concepts

* Dockerized service
* Scalable architecture
* Fault-tolerant design

---

##  Model Details

* Algorithm: **XGBoost**
* Handles class imbalance using `scale_pos_weight`
* Features:

  * Transaction amount
  * Foreign location flag
  * Deviation from user average

---

##  How to Run

### 1️⃣ Start Kafka

```bash
docker compose -f infra/docker/docker-compose.yml up -d
```

---

### 2️⃣ Start API

```bash
docker run -p 8000:8000 fraud-api
```

Check:

```
http://localhost:8000/docs
```

---

### 3️⃣ Start Consumer

```bash
python src/streaming/consumer.py
```

---

### 4️⃣ Start Producer

```bash
python src/streaming/producer.py
```

---

## 🎯 Sample Output

```
Txn: {'amount': 4500, 'location': 'US'}
Prediction: {'fraud_score': 0.87, 'decision': 'BLOCK'}
```

---

##  Current Limitation

> Feature inconsistency between training and inference

* Training uses real user averages
* Inference uses static fallback (`avg = 200`)


---
##  If you like this project

Give it a star and feel free to fork 
