import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
train_data_path = "/home/suraj/Desktop/Py/my_phrase_extractor/training_data (copy).tsv"
test_data_path = "/home/suraj/Desktop/Py/my_phrase_extractor/eval_data.txt"
df = pd.read_csv(train_data_path,sep='\t',names=['Sent','Label'])
df.loc[df["Label"] == "Not Found","Label"] = 0
df.loc[df["Label"] != 0,"Label"] = 1
df_x = df["Sent"]
df_y = df["Label"]
cv = TfidfVectorizer(min_df=1,stop_words="english")
x_train, x_test, y_train, y_test = train_test_split(df_x,df_y,test_size=0.2,random_state=0)
x_traincv = cv.fit_transform(x_train.values.astype('U'))
sv = svm.LinearSVC()
y_train = y_train.astype('int')
sv.fit(x_traincv,y_train)
x_testcv = cv.transform(x_test.values.astype('U'))
pred=sv.predict(x_testcv)
act = np.array(y_test)
count_correct = 0
for i in range(len(pred)):
    if pred[i]==act[i]:
        count_correct+=1
print(count_correct/len(pred))