# ETL Data Engineering with Airflow and AWS S3 Storage
## Project Overview
### This project focuses on Extract, Transform, Load (ETL) data engineering using Apache Airflow and AWS S3 storage. The primary objective is to extract tweet data from Twitter using Twitter API, transform the extracted data, and store it in AWS S3.

Technologies Used
Python (Version 3 and above)
Apache Airflow
AWS S3
Project Structure
The project repository is organized as follows:

lua
Copy code
etl-twitter-airflow-aws-s3/
│
├── dags/
│   ├── twitter_etl_dag.py
│
├── scripts/
│   ├── Tweet_Airflow_ETL.py
│   ├── Tweeter_Dag.py
│   ├── load.py
│
├── config/
│   ├── twitter_api_config.json
│   ├── aws_s3_config.json
│
├── requirements.txt
├── .gitignore
├── README.md
dags/: Contains the Airflow DAG (Directed Acyclic Graph) file twitter_etl_dag.py that defines the workflow for the ETL process.

scripts/: Includes separate Python scripts for each ETL phase - extract.py, transform.py, and load.py.

config/: Holds configuration files for Twitter API (twitter_api_config.json) and AWS S3 (aws_s3_config.json).

requirements.txt: Lists all the Python dependencies required for the project.

.gitignore: Specifies files and directories to be ignored by version control.
