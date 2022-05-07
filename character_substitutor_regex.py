import re
import pandas as pd

def regex_cleaning(dataframe, columns, pattern, substitute):
    '''Substritute characters inside dataframe using regex pattern'''
    dataframe[columns] = dataframe[columns].apply(lambda x: re.sub(pattern, substitute, x))
    return dataframe