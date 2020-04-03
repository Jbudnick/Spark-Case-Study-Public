from main import french_tweets_df
from main import cleaned_tweets
from main import filter_tweets
from main import list_of_key_words
from main import get_sparkdf_wordcount
from datetime import datetime 
import nltk
from nltk.corpus import stopwords
import numpy as np
import matplotlib.pyplot as plt


nltk.download('stopwords')
french_stopwords_list = stopwords.words('french')

filt_tweets = filter_tweets(list_of_key_words, cleaned_tweets, cleaned_tweets.text)
objects = ('Tweets before filtering', "Tweets after filtering")
y_pos = np.arange(len(objects))
performance = [cleaned_tweets.count(), filt_tweets.count()]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('# of Tweets')
plt.title('Tweet Filtering')
plt.savefig('images/filtered_counts.png')

word_freq = get_sparkdf_wordcount(filt_tweets, 'text', french_stopwords_list)
