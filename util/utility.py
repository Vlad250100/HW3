import pickle
from sklearn.model_selection import train_test_split 
import pandas as pd
import sys
from pathlib import Path 

sys.path[0] = str(Path(sys.path[0]).parent)

from conf.tuning import settings

def spliting_data(X: pd.DataFrame, Y: pd.Series) -> list:
    """
    This metod split the X and Y in train and test datasets, which returns in list.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state = settings.random_state_HW3) 
    return [X_train, X_test, y_train, y_test]

def save_model (dir: str, model) -> None:
    """
    This metod save the the model to the dir
    """
    pickle.dump(model, open(dir, 'wb'))