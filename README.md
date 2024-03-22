# Twitter Data ETL with Airflow and AWS S3
This project enables the seamless extraction of Twitter data using the Twitter API and stores it efficiently in an AWS S3 bucket. The orchestration of this data pipeline is managed using Apache Airflow.


## Architecture
![Alt Text](url)


## Key Components:
- Twitter API: Facilitates data collection from Twitter.
- Apache Airflow: Orchestrates and schedules ETL jobs.
- Amazon S3: Acts as the storage destination for the extracted Twitter data.

## Environment Setup
### Hardware Used:
Operating System: Windows/Ubuntu OS
Specifications: 4/8+ vCores, 4+ GB Memory, 32/64 GB Storage

## Prerequisites:
- Twitter developer account and API key
- AWS account with S3 bucket configured
- Python 3
- Required Python packages: tweepy, pandas, boto3

## Installation
1. Clone the repository:
```
git clone [https://github.com/itsAniketNow/Twitter-Data-ETL]
```
2. Install the required packages:
```
pip install -r requirements.txt
```
3. Create a config.py file in the root directory and add the following variables:
```
AccessKey = "[Your Twitter API key]"
AccessSecret = "[Your Twitter API secret key]"
BearerToken = "[Your Twitter API bearer token]"
```

## Process
1. Start the Airflow webserver:
```
airflow standalone
```
2. Access Airflow through your browser using the default port (8080).

3. In the Airflow UI, enable the twitter_data_pipeline DAG.

4. The pipeline will run on the schedule defined in the DAG and load the data into the specified S3 bucket in CSV format.
