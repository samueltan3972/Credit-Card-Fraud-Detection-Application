import pickle

# utils function for loading the trained model for deployment
# save the model to disk
filename = {"lr": "logistic_regression.sav"}

# load the model from disk
def load_logistic_regression():
    return pickle.load(open(filename["lr"], "rb"))

# TODO: complete the code for deployment