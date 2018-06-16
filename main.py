'''
Author : Suraj Tripathy
'''

import pandas as pd
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from my_phrase_extractor.my_model import model_count
##Training and testing data files path
train_data_path = "/home/suraj/Desktop/Py/my_phrase_extractor/training_data.tsv"
test_data_path = "/home/suraj/Desktop/Py/my_phrase_extractor/eval_data.txt"
df = pd.read_csv(train_data_path,sep='\t',names=['Sent','Label'])
##Separating the labels of not found and others
df.loc[df["Label"] == "Not Found","Label"] = 0
df.loc[df["Label"] != 0,"Label"] = 1
df_x = df["Sent"]
df_y = df["Label"]
##init tfidf and svm
cv = TfidfVectorizer(min_df=1,stop_words="english")
x_train, x_test, y_train, y_test = train_test_split(df_x,df_y,test_size=0,random_state=0)
x_traincv = cv.fit_transform(x_train.values.astype('U'))
sv = svm.LinearSVC()
y_train = y_train.astype('int')
sv.fit(x_traincv,y_train)
##Put the trained model for data in eval.txt and pipeline the predicted data to my_model.py
df_test = pd.read_csv(test_data_path,sep='\t',names=['Sent','Label'])
df_test_x = df_test["Sent"]
x_testcv = cv.transform(df_test_x.values.astype('U'))
pred = list(sv.predict(x_testcv))
sentence = []
for i in range(len(pred)):
    if pred[i]!= 0:
        sentence.append(df_test_x[i])

model_count(sentence)