import lightgbm as lgb
import pandas as pd
from sklearn.model_selection import train_test_split

def train_model(df):
    X = df.drop('result', axis=1)
    y = df['result']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = lgb.LGBMClassifier()
    model.fit(X_train, y_train)
    print(f'Accuracy: {model.score(X_test, y_test) * 100:.2f}%')
    return model
