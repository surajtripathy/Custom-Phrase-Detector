'''
Author : Suraj Tripathy
'''

import pandas as pd
from chunk import chunked,check_again_chunk
def model_count(sent):
    #sent_for_pred = []
    #predictions = []
    output_data_path = "/home/suraj/Desktop/Py/my_phrase_extractor/output.txt"
    f = open(output_data_path, 'a')
    def process_cnt():
        try:
            for i in range(len(sent)):
                ##Every sentence is sent to chunk.py to be analysed for keywords
                returned = check_again_chunk(str(sent[i]))
                if returned != '':
                    print(returned.strip())
                    f.write(sent[i]+'\t'+returned.strip()+'\n')
                    #sent_for_pred.append(sent[i])
                    #predictions.append(returned.strip())
            f.close()
            #print(predictions)
        except Exception as e:
            print(str(e))
    process_cnt()