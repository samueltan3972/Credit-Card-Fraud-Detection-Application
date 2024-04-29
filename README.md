# UM Machine Learning Assignment

This repo contains file and hang bang lang about UM Machine Learning Assignment. Haiyaa, u know what is this la!

## Getting Started

1. Download and Install [Python 3.10](https://www.python.org/downloads/release/python-31011/)

2. Clone this repository

    ```bash
    git clone https://github.com/samueltan3972/ML-Assignment.git
    ```

3. Install necesseray dependency

    ```bash
    cd <bla>
    pip install pipenv # Optional, but recommend using virtual environment
    python3 -m pipenv shell
    pipenv install # if using pipenv, but below method works whether is pipenv
    pip install -r requirements.txt # choose 1 to run only, if above is selected, don't run this
    ```

4. Start Jupyter Lab and open Model_Training.ipynb to see the training process. However, the model has been trained, no further training is required.

    ```bash
    jupyter lab
    ```

5. Refer to deploy.py to run the developed application for deployment.

    ```bash
    streamlit run Credit_Card_Fraud_Detection_App.py
    ```

Dataset Link:
https://www.kaggle.com/datasets/nelgiriyewithana/credit-card-fraud-detection-dataset-2023
