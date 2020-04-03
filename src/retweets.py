from main import french_tweets_df
from main import cleaned_tweets
from main import filter_tweets
from main import cand_retweet_df
from main import list_of_key_words
from main import get_sparkdf_wordcount
from datetime import datetime 
import nltk
from nltk.corpus import stopwords
import numpy as np
import matplotlib.pyplot as plt

#Word count of candidates retweets are shown here

if __name__ == '__main__':
    plt.style.use("tableau-colorblind10")

    nltk.download('stopwords')
    french_stopwords_list = stopwords.words('french')

    filt_tweets = cand_retweet_df(list_of_key_words, cleaned_tweets, cleaned_tweets.text)
    objects = ('Tweets before filtering', "Tweets after filtering")
    y_pos = np.arange(len(objects))
    performance = [cleaned_tweets.count(), filt_tweets.count()]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('# of Tweets')
    plt.title('Tweet Filtering')
    plt.savefig('images/filtered_counts.png')

    word_freq = get_sparkdf_wordcount(filt_tweets, 'text', french_stopwords_list)


    word_freq = get_sparkdf_wordcount(filt_tweets, 'text', french_stopwords_list)
    pd_word_freq = word_freq.toPandas()

    fig, ax = plt.subplots(1, 1)

    pd_word_freq['word'].replace(regex=True, inplace=True, to_replace=r'[^0-9.\-A-Za-z]', value=r'')
    pd_word_freq = pd_word_freq.head(15)
    ax = pd_word_freq.plot.bar(x='word', y='count', rot=0)

    # word_freq.show(15)
    plt.xticks(rotation=45)
    plt.savefig('images/candwords.png')