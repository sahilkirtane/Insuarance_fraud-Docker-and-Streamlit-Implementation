# Insuarance_fraud-Docker-and-Streamlit-Implementation

## Problem Description

Insurance fraud has become a significant concern for a major general insurance company, with a substantial number of reported claims being identified as fraudulent. This issue is leading to financial losses and necessitates a proactive approach. To address this challenge, the insurer aims to predict potentially fraudulent claims before processing them. This approach enables the allocation of costs, implementation of thorough investigation procedures, and the development of appropriate action plans for managing claims effectively.

Fraudulent insurance claims encompass any claims filed with the intention of obtaining improper payments from the insurer. This project focuses on the motor and health insurance segments, which have experienced a surge in fraudulent activities. Fraudulent claims can originate from various sources, including policyholders, intermediaries, and internal entities. The latter two sources are particularly critical from an internal control framework perspective. The nature of frauds can be categorized into types such as application fraud, inflation fraud, identity fraud, fabrication, and staged/contrived/induced accidents.

## Project Overview

This repository contains a comprehensive solution to the insurance fraud detection problem. Leveraging machine learning techniques, the project aims to predict potentially fraudulent insurance claims, thereby enabling the insurer to take proactive measures to mitigate losses. The solution is packaged in a Docker container for seamless deployment and ease of use.

## Repository Contents

- `Dockerfile`: A Dockerfile that automates the setup of the environment required to run the fraud detection application.
- `model.pkl`: A trained machine learning model serialized in pickle format. This model is used to make predictions on new insurance claims.
- `model.py`: Python script used to train the machine learning model based on historical insurance claims data.
- `server.py`: Python script that deploys a Streamlit-based user interface for interactive fraud detection. Users can input claim details, and the model will predict the likelihood of fraud.

## Getting Started

To run the fraud detection application locally, follow these steps:

1. Download or clone the repository to your local machine.
2. Navigate to the repository directory using the command line.

### Building and Running the Docker Container

3. Make sure you have Docker installed on your system.
4. Open a terminal window and execute the following command to build the Docker image:
   ```
   docker build -t fraud-detection .
   ```
5. Once the image is built, run the Docker container with the following command:
   ```
   docker run -p 8501:8501 fraud-detection
   ```

### Accessing the User Interface

6. Open a web browser and navigate to `http://localhost:8501` to access the Streamlit-based user interface.
7. Use the user interface to input claim details and receive predictions on the likelihood of fraud.
