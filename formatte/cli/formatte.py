import pandas as pd
from csv import reader
from pathlib import Path
import glob
import os

months_hydro = 'OCT NOV DEC JAN FEB MAR APR MAY JUN JUL AUG SEP'.split()

def add_subcommand_formatte(subparsers):
    parser = subparsers.add_parser('run')
    parser.add_argument('file_name')
    parser.set_defaults(func=formatte)

def get_files(var):
    p = os.getcwd()
    files = []
    dest = f'{p}/{var}'
    for name in glob.glob(dest):
        files.append(name.split('\\')[-1])
    return files

def edit_file(file_name):
    with open(file_name) as opened_file:
        read_file = reader(opened_file)
        data = list(read_file)
    table = [row[0].split() for row in data]
    df = pd.DataFrame(table)
    df.index = df.iloc[:,1]
    df.index.name = None
    df = df.drop([0,1], axis=1)
    df.columns = months_hydro
    df = df.astype(float)

    df.to_csv("outputs/{}.csv".format(file_name.split('.')[0]))

def formatte(file_name):
    file_name = vars(file_name)['file_name']

    dest = Path()/'outputs'
    dest.mkdir(parents=True, exist_ok=True)

    if file_name.startswith('*'):
        files = get_files(file_name)
    else: files = [file_name]

    for file in files:
        edit_file(file)