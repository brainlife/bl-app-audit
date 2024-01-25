## brainLife login
#!npm install -g brainlife
#!bl login --username "bacaron" --password 'b0B_Swa$#rleyMon26'

import numpy as np
import pandas as pd
import json
import ast
import os 
from ast import literal_eval

## import data
!git clone https://github.com/brainlife/bl-app-audit.git
cd bl-app-audit

## save data to variables
apps = pd.read_csv('apps_df_with_resources.csv')
apps['config'] = [ ast.literal_eval(f) for f in apps['config'] ]
apps['inputs'] = [ ast.literal_eval(f) for f in apps['inputs'] ]
datatypes = pd.read_csv('datatypes_df.csv')
resources = pd.read_csv('resources_df.csv')
sample_data = pd.read_csv('sample_data2.csv')

## funcion to create input and config strings 
def create_strings(app_df, sample_data):

  # get names of inputs and configs
  inputs = [ f for f in app_df.loc['config'].tolist()[0] if app_df.loc['config'].tolist()[0][f]['type'] == 'input' ]
  configs = [ f for f in app_df.loc['config'].tolist()[0] if f not in inputs]

  # creating input string using sample data
  count = 0
  input_str = ''
  for idx in range(len(app_df.loc['inputs'].tolist()[0])):
    dt = app_df.loc['inputs'].tolist()[0][idx]['datatype']
    id = sample_data[sample_data['datatype'] == dt]['_id'].values.tolist()[0]
    if count == 0:
        input_str = '--input ' + app_df.loc['inputs'].tolist()[0][idx]['id'] + ":" + id
        count += 1
    else:
        input_str += ' --input ' + app_df.loc['inputs'].tolist()[0][idx]['id'] + ":" + id

  # creating config dictionary with default values
  config_dic = {}
  for config_name in configs:
    default_value = app_df.loc['config'].tolist()[0][config_name]['default']
    config_dic[config_name] = default_value
  config_str = str(config_dic)

  return input_str, config_str

## main function to run audit through command line 
def main(app_df,sample_df,projectID):
  # make copies to not overwrite inputs
  app_df = app_df.copy()
  sample_df = sample_df.copy()

  app_df['inputs'] = literal_eval(str(app_df['inputs']))
  app_df['config'] = literal_eval(str(app_df['config']))
  app_df['resources'] = literal_eval(str(app_df['resources']))

  # identify input parameters, including input string, config string, app id, github branch, and resources id
  input_string, config_string = create_strings(pd.DataFrame(app_df),sample_df)
  config_string = config_string.replace("'", '"')
  resources = app_df['resources']
  app_id = app_df['_id']
  branch = app_df['github_branch']
  for resource in resources:
    cmd_string = "bl app run --id %s --project %s --preferred-resource %s --branch %s --config '%s' %s" %(app_id,projectID,resource,branch,config_string,input_string)
    # os.system(cmd_string)
    # !cmd_string

for i in range(len(apps)):
  apps_df = apps.iloc[i]
  main(apps_df, sample_data, "5d64733db29ac960ca2e797f");
