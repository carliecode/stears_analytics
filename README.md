
Stears Analytics ETL Project
=====================================

Description
---------------
The Stears Analytics ETL Project is designed to automate the extraction, transformation, and loading (ETL) of data for Stears Analytics. The project uses Python scripts to handle the ETL process and Apache Airflow for scheduling and orchestration.

Features
------------
Data Extraction: Extracts data from a Minio bucket containing CSV and JSON files, converts data into a Pandas DataFrame, and passes it to the transformation module.
Data Transformation: Applies data transformation rules, groups data for analysis, and outputs the transformed data into a CSV file stored locally in the data folder.
Data Loading: Reads the transformed data from the CSV file, creates a bar chart for visualization, and stores the chart in the project folder.

Architecture
--------------
The project architecture is illustrated in the architecture_diagram_stears_analytics diagram included in the project folder.

Requirements
---------------
Python 3.x
Apache Airflow (assumed to be running already)
Docker
MinIO

Setup and Installation
---------------------------
- Clone the repository: git clone https://github.com/carliecode/stears_analytics.git
- Install dependencies: pip install -r requirements.txt
- Configure MinIO:
    - Set the following environment variables:
        - MINIO_END_POINT (e.g., 127.0.0.1:9091)
        - MINIO_ACCESS_KEY (e.g., minioadmin)
        - MINIO_SECRET_KEY (e.g., minioadmin)
        - MINIO_BUCKET (e.g., stears)
        - Run Minio on the specified port: minio server --address ":9091" /data
- Create a bucket with the specified name in your Minio instance.
- Upload your data files (in CSV format) to the specified bucket.
- Build the Docker image: docker build -t your-image-name .
- Run the Docker container: docker run -p 8080:8080 your-image-name

Running the ETL Pipeline
------------------------------
- The ETL pipeline is scheduled to run every 30 secs using Apache Airflow. 
- The pipeline is triggered by the main.py script, which orchestrates the extraction, transformation, and loading processes. 
- You can also trigger the DAG manually using the Airflow web interface.
- To verify the pipeline execution, check the application logs in the /logs folder and your project folder location for the generated chart, chart.png.