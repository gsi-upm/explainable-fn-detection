import pandas as pd
from nltk.tokenize import word_tokenize

class DatasetLoader():

    def __init__(self, name, path):
        self.name = name
        self.path = path
    
    def load(self, labels=['text', 'label']):
        self.df = pd.read_csv(self.path)[labels]
        return self.df
    
    def lower(self):
        self.df['text'] = self.df['text'].apply(lambda x: x.lower())

    def tokenize(self):
        self.df['tokenized_text'] = self.df['text'].apply(word_tokenize)

    def concat_dataframe_columns(self, df_concat):
        self.df = pd.concat([self.df, df_concat], axis=1)
        return self.df
    
    def join_dataframe(self, df_join):
        self.df = self.df.join(df_join)
        return self.df