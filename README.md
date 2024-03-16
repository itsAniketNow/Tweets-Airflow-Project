# Twitter Data ETL with Apache Airflow and AWS S3

## Project Overview:
This project revolves around the Extract, Transform, Load (ETL) process for Twitter data using Apache Airflow and AWS S3 storage. The primary goal is to fetch tweet data from Twitter API, perform necessary transformations, and then store the transformed data in AWS S3 buckets.

## Project Description:
The project entails the development of an automated ETL pipeline using Apache Airflow. Firstly, data is extracted from Twitter using the Twitter API. Then, the extracted data undergoes transformation steps to prepare it for storage in AWS S3. Apache Airflow orchestrates this entire process, ensuring data integrity and reliability. The project aims to streamline the process of gathering and storing Twitter data for various analytical purposes.

## Technology Stack:
- Python
- Google Colab
- Jupyter Notebook
- Apache Airflow
- AWS S3
- Additional Resources:
  - Stack Overflow
  - Visual Studio Code (VS Code)

## Project Structure:
The project repository is organized as follows:
```
etl-twitter-airflow-aws-s3/
│
├── dags/
│ ├── twitter_etl_dag.py
│
├── scripts/
│ ├── Tweet_Airflow_ETL.py
│ ├── Tweeter_Dag.py
│ ├── load.py
│
├── config/
│ ├── twitter_api_config.json
│ ├── aws_s3_config.json
│
├── requirements.txt
├── .gitignore
├── README.md
```
- **dags/:** Contains the Apache Airflow DAG (Directed Acyclic Graph) file `twitter_etl_dag.py` defining the workflow for the ETL process.
- **scripts/:** Includes separate Python scripts for each phase of the ETL process: `extract.py`, `transform.py`, and `load.py`.
- **config/:** Holds configuration files for Twitter API (`twitter_api_config.json`) and AWS S3 (`aws_s3_config.json`).
- **requirements.txt:** Lists all the Python dependencies required for the project.
- **.gitignore:** Specifies files and directories to be ignored by version control.

This README.md has been customized for the specific project and is original content.
