import pandas as pd
from chunk import chunked
train_data_path = "/home/suraj/Desktop/Py/my_phrase_extractor/training_data (copy).tsv"
df = pd.read_csv(train_data_path,sep='\t',names=['Sent','Label'])
sent = df["Sent"].values.T.tolist()
label = df["Label"].values.T.tolist()
predictions = []

def process_cnt():
    try:
        count = 0
        for i in range(len(label)):
            if label[i] != "Not Found":
                returned = chunked(sent[i]+'\n')
                if returned != None:
                    if returned.strip() == label[i]:
                        count+=1
        print(count)
    except Exception as e:
        print(str(e))
process_cnt()