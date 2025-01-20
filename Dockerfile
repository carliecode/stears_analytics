FROM python:3.9-slim

FROM apache/airflow:2.2.5

WORKDIR /stears_analytics

WORKDIR /opt/airflow

COPY stears_analytics/requirements.txt /opt/airflow/requirements.txt
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt

COPY stears_analytics/ /opt/airflow/stears_analytics/

COPY stears_analytics/dags/ /opt/airflow/dags/
