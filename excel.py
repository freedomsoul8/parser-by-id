import pandas as pd

def get_column(filename, column_name):
    df = pd.read_excel(filename)
    try:
        column_list = df[column_name]
    except:
        return 'Wrong file format'

    return column_list