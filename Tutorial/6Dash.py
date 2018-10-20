#!/home/thomas/anaconda3/bin/python

"""
    # Author : Thomas Neuer (tneuer)
    # File Name : 6Dash.py
    # Creation Date : Fre 19 Okt 2018 23:11:24 CEST
    # Last Modified : Fre 19 Okt 2018 23:52:49 CEST
    # Description : Sentiment analysis
"""
#==============================================================================

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analysis = TextBlob("TextBlob sure looks like it has some interesting features")

print(analysis.translate(to="de"))
print(analysis.sentiment)

"""
####
# TextBlob
####
pos_count = 0
pos_correct = 0

with open("./data/positive.txt","r") as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)
        if analysis.sentiment.subjectivity < 0.3:
            if analysis.sentiment.polarity > 0:
                pos_correct += 1
            pos_count +=1


neg_count = 0
neg_correct = 0

with open("./data/negative.txt","r") as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)
        if analysis.sentiment.subjectivity < 0.3:
            if analysis.sentiment.polarity <= 0:
                neg_correct += 1
            neg_count +=1

print("Positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
print("Negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))
"""

# Using Vader results neutrality -0.5 < polarity < 0.5

pos_count = 0
pos_correct = 0

with open("./data/positive.txt","r") as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)

        if analysis.sentiment.polarity >= 0.5:
            if analysis.sentiment.polarity > 0:
                pos_correct += 1
            pos_count +=1


neg_count = 0
neg_correct = 0

with open("./data/negative.txt","r") as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)
        if analysis.sentiment.polarity <= -0.5:
            if analysis.sentiment.polarity <= 0:
                neg_correct += 1
            neg_count +=1

print("Positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
print("Negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))

####
# Vader
####

"""
analyzer = SentimentIntensityAnalyzer()

pos_count = 0
pos_correct = 0
threshold = 0.5

with open("./data/positive.txt","r") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if vs["compound"] >= threshold or vs["compound"] <=-threshold:
            if vs['compound'] > 0:
                pos_correct += 1
            pos_count +=1


neg_count = 0
neg_correct = 0

with open("./data/negative.txt","r") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if vs["compound"] >= threshold or vs["compound"] <=-threshold:
            if vs['compound'] <= 0:
                neg_correct += 1
            neg_count +=1

print("Positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
print("Negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))
"""

analyzer = SentimentIntensityAnalyzer()

pos_count = 0
pos_correct = 0

with open("./data/positive.txt","r") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if not vs['neg'] > 0.1:
            if vs['pos']-vs['neg'] > 0:
                pos_correct += 1
            pos_count +=1


neg_count = 0
neg_correct = 0

with open("./data/negative.txt","r") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if not vs['pos'] > 0.1:
            if vs['pos']-vs['neg'] <= 0:
                neg_correct += 1
            neg_count +=1

print("Positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
print("Negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))
