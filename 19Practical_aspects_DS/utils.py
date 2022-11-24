from xml.sax import default_parser_list
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def load_data():
    # Load the iris dataset
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    # Split the data into a training set and a test set
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0)
    return X_train, X_test, y_train, y_test
