# Twitter Data ETL with Airflow and AWS S3

## Project Overview:
This project orchestrates an end-to-end data pipeline for Twitter data, leveraging Apache Airflow for task scheduling and AWS S3 for data storage. It aims to streamline the process of collecting, processing, and storing Twitter data for analytics and insights.


## Project Architecture:
![Architecture Image](https://camo.githubusercontent.com/749ccbc54ef188421a8b7c237dbb86af89e385d1c3ec73a3a5e3ddc8e22bba06/68747470733a2f2f696d6775722e636f6d2f6d416a444f786c2e706e67)

- **Twitter API**
- **Apache Airflow**
- **Amazon S3**

The Twitter API is utilized to fetch real-time data from Twitter, while Apache Airflow orchestrates the pipeline tasks and AWS S3 serves as the data repository.

## Environment Setup:
### Hardware Used:
- **Local Machine Specifications:**
  - Ubuntu OS
  - 4+ vCores, 4/8+ GB Memory
  - Storage: 32/64+ GB

### Prerequisites:
- Twitter Developer Account and API Key
- AWS Account with S3 Bucket Setup
- Python 3
- Airflow
- tweepy
- pandas
- boto3

## Installation:
1. Clone the repository:
!
Understood! Let's create a README.md with a similar structure but different content:

markdown
Copy code
# Twitter Data Pipeline with Airflow and AWS S3

## Overview:
This project orchestrates an ETL (Extract, Transform, Load) pipeline for Twitter data, utilizing Apache Airflow for task scheduling and AWS S3 for data storage. 

## Project Description:
The aim of this project is to collect Twitter data via the Twitter API, process it, and store it in an AWS S3 bucket in CSV format. Apache Airflow, a powerful workflow management tool, is employed to manage and schedule the pipeline tasks efficiently.

## Architecture:
- Twitter API
- Apache Airflow
- AWS S3

The Twitter API is used to collect data, which is then processed and stored in an AWS S3 bucket. Apache Airflow manages the workflow and ensures smooth execution of the ETL tasks.

## Environment Setup:
### Hardware Used:
- Local Machine Specifications:
  - Ubuntu OS
  - 4 vCores, 4 GiB Memory
  - Storage: 32 GiB

### Prerequisites:
- Twitter Developer Account and API Key
- AWS Account with S3 Bucket Setup
- Python 3
- Airflow
- tweepy
- pandas
- boto3

## Installation:
1. Clone the repository:
git clone https://github.com/itsAniketNow/Twitter-Data-ETL

2. Install the required packages:
```
pip install -r requirements.txt
```
3. Create a `config.py` file in the project's root directory and add the necessary variables.
4. Update the `airflow_etl_key.pem` file to point to your `config.py` file and set the appropriate S3 bucket name.

## Usage:
1. Start the Airflow webserver:
```
airflow standalone
```
2. **Access Airflow UI:**
- Open your browser and navigate to `http://localhost:8080`.

3. **Enable the DAG:**
- Find and enable the `twitter_data_pipeline` DAG in the Airflow UI.

4. **Run the Pipeline:**
- The pipeline will execute based on the defined schedule, extracting and storing data into the specified S3 bucket.


## Conclusion:
This project provides a comprehensive guide on building a robust Twitter data pipeline using Apache Airflow and AWS S3. By following the steps outlined in this README, you can effectively set up and manage the pipeline for your Twitter data needs.

