import pickle
import os
import pandas as pd
import numpy as np
from datetime import datetime
import sqlalchemy
import sklearn
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def data_preparation(**kwargs):
    driver = 'postgresql'
    address = 'postgres'
    port = 5432
    db_name = 'kenanga_db'
    username = 'api_user'
    password = '!qazZaq1'

    engine = sqlalchemy.create_engine(f'{driver}://{username}:{password}@{address}:{port}/{db_name}')
    statements = f'SELECT * FROM kenanga_schema.history_monthly ORDER BY history_date DESC LIMIT 2'
    data_df = pd.read_sql(statements, engine).sort_values('history_date', ascending = True)
    cols = data_df.columns.difference(['history_date'])
    for col in cols:
        data_df[f'shift_0_{col}'] = data_df[col].shift(0)
        data_df[f'shift_1_{col}'] = data_df[col].shift(1)
    feature_cols = data_df.columns[(data_df.columns.str.startswith('shift'))]
    return data_df.iloc[-1][feature_cols].values.tolist() 
    
def get_prediction(**kwargs):
    model_folder = '/usr/local/airflow/dags/model'
    f1m_list = []
    f2m_list = []
    f3m_list = []
    f1m_preds = 0
    f2m_preds = 0
    f3m_preds = 0
    
    ti = kwargs['ti']
    data = np.asarray(ti.xcom_pull(task_ids='data_preparation'))[np.newaxis, :]
    
    for file in os.listdir(path = model_folder):
        if 'f1m' in file:
            f1m_list.append(model_folder + '/' + file)
        if 'f2m' in file:
            f2m_list.append(model_folder + '/' + file)
        if 'f3m' in file:
            f3m_list.append(model_folder + '/' + file)
            
    for f3m in f3m_list:
        model = pickle.load(open(f3m, 'rb'))
        f3m_preds += np.round((model.predict(data) / len(f3m_list))[0], 2)

    for f2m in f2m_list:
        model = pickle.load(open(f2m, 'rb'))
        f2m_preds += np.round((model.predict(data) / len(f2m_list))[0], 2)

    for f1m in f1m_list:
        model = pickle.load(open(f1m, 'rb'))
        f1m_preds += np.round((model.predict(data) / len(f1m_list))[0], 2)

    return [f1m_preds, f2m_preds, f3m_preds]

dag = DAG(dag_id='forecasting_crude_palm_oil_fob_spot', start_date=datetime(2020, 5, 1), schedule_interval='@monthly')
get_data = PythonOperator(task_id = 'data_preparation', provide_context = True, python_callable = data_preparation, dag = dag)
get_forecast = PythonOperator(task_id = 'get_forecast', provide_context = True, python_callable = get_prediction, dag = dag)

get_data >> get_forecast