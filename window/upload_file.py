import pandas as pd


def upload_file(dir):
    global file_data
    file_data = pd.read_csv (dir)
    return file_data