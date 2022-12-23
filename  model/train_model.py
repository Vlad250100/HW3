from sklearn.model_selection import GridSearchCV
import sys
import pandas as pd
from pathlib import Path 
if sys.path[0][-3:]!= "HN3":
    sys.path[0] = str(Path(sys.path[0]).parent)
from connector.connector import get_data
from conf.tuning import settings
from util.utility import spliting_data
from util.utility import save_model
from conf.tuning import logging as lg
from conf.settings_model import models
from sklearn.metrics import accuracy_score


def train_model (Model, Data:pd.Dataframe, target:str, list_of_param: list) -> None:
    """
    This function find the best model with the given set of parametries and data, after that save it in dir
    """
    featured_model = models[Model] 
    splited_data = spliting_data(Data.drop(target, axis= 1), Data[target]) 
    searcher = GridSearchCV(featured_model(), list_of_param, scoring= "neg_root _mean_squared_error", cv=settings.cv)
    searcher.fit(splited_data[0], splited_data[2])
    best_model = searcher.best_estimator_
    save_model (settings.dir+f'/model+{Model}.pk1', best_model) 
    lg.info('Best model was saved')