# -*- coding: utf-8 -*-
import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

"""VADER's `SentimentIntensityAnalyzer()` takes in a string and returns a dictionary of scores in each of four categories:
* negative
* neutral
* positive
* compound *(computed by normalizing the scores above, (i.e. aggregated score)*
"""

a = 'This is a good movie ever seen'
sid.polarity_scores(a)

a = 'This was the worst film to ever disgrace the screen'
sid.polarity_scores(a)

from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

import numpy as np
import pandas as pd
df = pd.read_csv('amazonreviews.tsv', sep ='\t')
df.head()

df['label'].value_counts()

df['label'].isnull().sum()

# REMOVE NaN VALUES AND EMPTY STRINGS:
df.dropna(inplace=True)

blanks = []  # start with an empty list
for i,lb,rv in df.itertuples():  # iterate over the DataFrame
    if type(rv)==str:            # avoid NaN values
        if rv.isspace():         # test 'review' for whitespace
            blanks.append(i)     # add matching index numbers to the list

df.drop(blanks, inplace=True)

sid.polarity_scores(df.loc[0]['review'])

df['scores'] = df['review'].apply(lambda review: sid.polarity_scores(review))
df.head()

df['compound'] = df['scores'].apply(lambda score_dict: score_dict['compound'])
df.head()

df['comp_score'] = df['compound'].apply(lambda c: 'pos' if c >= 0 else 'neg')
df.head()

from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

print(classification_report(df['label'],df['comp_score']))

print(confusion_matrix(df['label'],df['comp_score']))

accuracy_score(df['label'],df['comp_score'])

