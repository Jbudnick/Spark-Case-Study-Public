# from main import french_tweets_df
# from main import cleaned_tweets
# from main import filter_tweets
# from main import list_of_key_words
# from main import get_sparkdf_wordcount
# from datetime import datetime 
# import nltk
# from nltk.corpus import stopwords
import numpy as np
import matplotlib.pyplot as plt
import wordcloud as WordCloud

text = 'These flannel wipes are OK, but in my opinion not worth keeping. I also ordered someImse Vimse Cloth Wipes-Ocean Blue-12 countwhich are larger, had a nicer, softer texture and just seemed higher quality. I use cloth wipes for hands and faces and have been usingThirsties 6 Pack Fab Wipes, Boyfor about 8 months now and need to replace them because they are starting to get rough and have had stink issues for a while t'
cloud= WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
plt.figure()
plt.imshow(WordCloud, interpolation="bilinear")
plt.axis("off")
plt.show()
plt.savefig('images/Name.png')

print(cloud)

    
