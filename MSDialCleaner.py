import abc
import os
import pandas as pd

class MSDialCleaner(abc.ABC):
    def __init__(self, args: dict):
        self.args = args

    def load_file(self, filename):
        if not os.path.exists(filename):
            raise FileNotFoundError(f'File {filename} doesn\'t exist')

        with open(filename, 'r') as fin:
            data = pd.read_csv(fin, delimiter='\t', skiprows=4)

        return data

    def save_file(self, data, filename):
        with open(filename, 'w') as fout:
            data.to_csv(fout, index=False, sep='\t')
            fout.flush()

        print(f'Cleaned file saved as {filename}')

    def run(self):
        data = self.load_file(self.args['input'])

        # cut column
        data.drop('EI spectrum', axis=1, inplace=True)

        # save
        output = self.args['input'].replace('.txt', '-cleaned.txt')
        self.save_file(data, output)

        exit(0)
