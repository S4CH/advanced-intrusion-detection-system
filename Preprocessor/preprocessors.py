#Import all the modules
from sklearn.preprocessing import LabelEncoder


class Preprocessor:
    
    def __init__(self, data):
        self.data = data

    def removeNullValues(self):
        "This funtion is to remove null values from the dataset"
        
        return self.data.dropna()
    
    def labelEncoder(self, columns):i
        "Label_Encoder converts categorical data"

        le = LabelEncoder()
        for each in columns:
            self.data[str(each)] = le.fit_transform(df[str(each)])

        return self.data
