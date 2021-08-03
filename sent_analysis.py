#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from konlpy.tag import Kkma

class sent_analysis:
    
    def __init__(self, sentence, n_gram=1, dictionary='default'):
        
        '''
        args
        sentence: a (preprocessed) sentence
        dictionary: lexicon
        n_gram: n_gram, default=1
        '''
        assert n_gram>0 and type(n_gram)==int, 'n_gram should be positive integer'
        
        kkma = Kkma()
        
        self.sentence = sentence
        if dictionary=='default':
            self.dictionary = pd.read_csv('./subjectivity-polarity.csv')
        self.pos_set = [i+'/'+a for i,a in kkma.pos(self.sentence)]
        if n_gram>1:
            pos_set_ngram = []
            for i in range(len(self.pos_set) - n_gram):
                gram = self.pos_set[i:i+n_gram]
                gram = ';'.join(gram)
                pos_set_ngram.append(gram)
            self.pos_set = pos_set_ngram
            
    def count_pos(self):
        positive,neutral,negative = 0,0,0
        for i,a in enumerate(self.pos_set):
            temp = self.dictionary[self.dictionary['ngram']==a]
            try:
                positive += float(temp['POS'].values)
                neutral += float(temp['NEUT'].values)
                negative += float(temp['NEG'].values)
            except:
                pass

        return {'positive':positive, 
                'neutral':neutral, 
                'negative':negative}

