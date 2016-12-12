import pprint, pickle
class RejectingDict(dict):

    def __setitem__(self, k, v):

        if k in self.keys():

            raise ValueError(k + " is already present")

        else:

            return super(RejectingDict, self).__setitem__(k, v)

import pickle

pkl_file = open('/Users/juanzinser/Documents/MCC/scentic/sentic_dict.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)


pkl_file.close()




# classify in two segments the dict entries, theones with numeric classification and the ones with
# two hashtags of diferent


# search for a way to plot the words for outlier checking
# search for a way to put the words in a plot and compare the words edges with their values
# apparently the sentiment isn't working anymore

import pandas as pn
import numpy as np

"""
Encontrar un conrpues nuevo y comparar los resultados del word_to_vec contra los que tenemos en el

"""
# there are 30394 words

frame_words = pn.DataFrame(columns=['word','hash1','hash2','rel1','rel2','rel3','rel4','rel5'])
frame_numeric = pn.DataFrame(columns=['word','num1','num2','num3','num4','num5','rel1','rel2','rel3','rel4','rel5'])


for word, row in data1.iteritems():
    if len(row)== 7:
        frame_words = frame_words.append(dict(zip(frame_words.columns,[word]+row)), ignore_index=True)
    else:
        frame_numeric = frame_numeric.append(dict(zip(frame_numeric.columns,[word]+row)), ignore_index=True)


frame_words.to_csv('data/frame_words.csv')

frame_numeric.to_csv('data/frame_numeric.csv')