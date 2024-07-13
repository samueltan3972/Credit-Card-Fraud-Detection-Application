# Credit Card Fraud Detection Application

This is a group assignment project for WQD7006 Machine Learning for Data Science for the Master of Data Science at University of Malaya (UM). This project uses [Credit Card Fraud Detection Dataset 2023](https://www.kaggle.com/datasets/nelgiriyewithana/credit-card-fraud-detection-dataset-2023) from Kaggle. The [report](report/G5_WQD7006_Report.pdf) and [slides](report/G5_WQD7006_Slides.pdf) of this project can be found at the [report folder](report/G5_WQD7006_Report.pdf). 


<img src="img/scam_is_everywhere.png" alt="Scam is Everywhere"/>

---

### Model Result

Logistic Regression, Random Forest, and SVM are the model selected in this project. Random Forest is found to have the best accuracy.

The result of the trained model is presented as follow:

| Models                | Accuracy (Trainig Set)    | Accuracy (Testing Set)    |
| ----------------      | :---------------------:   | :---------------------:   |
| Logistic Regression   | 0.96                      | 0.96                      |
| Random Forest         | 1.0                       | 1.0                       |
| SVM                   | 1.0                       | 1.0                       


---

### Demo

The model is then deployed with streamlit community cloud: [https://ummlassignment-g5.streamlit.app](https://ummlassignment-g5.streamlit.app/). The link may be down as the application enter sleeping mode.

<img src="img/demo.png" alt="Streamlit App Demo" height="750"/>

<img src="img/scam.jpg" alt="Scam" width="680"/>

---

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

5. To run the developed application for deployment.

    ```bash
    streamlit run Credit_Card_Fraud_Detection_App.py
    ```

Dataset Link:
https://www.kaggle.com/datasets/nelgiriyewithana/credit-card-fraud-detection-dataset-2023
