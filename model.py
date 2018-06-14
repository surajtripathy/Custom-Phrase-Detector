import pandas as pd
from chunk import chunked
train_data_path = "/home/suraj/Desktop/Py/my_phrase_extractor/training_data (copy).tsv"
df = pd.read_csv(train_data_path,sep='\t',names=['Sent','Label'])
sent = df["Sent"].values.T.tolist()
label = df["Label"].values.T.tolist()
predictions = []

def process_cnt():
    predictions_pos = []
    try:
        for i in range(len(label)):
            if label[i] != "Not Found":
                returned = chunked(sent[i]+'\n')
                predictions.append(returned)
                predictions_pos.append(i)
                if returned != None:
                    print(returned.strip())
    except Exception as e:
        print(str(e))
    pred_index = 0
    count_correct = 0
    for i in predictions_pos:
        if predictions[pred_index] != None:
            if label[i] == predictions[pred_index].strip():
                count_correct+=1
        pred_index += 1
    print(count_correct,len(predictions_pos))
process_cnt()