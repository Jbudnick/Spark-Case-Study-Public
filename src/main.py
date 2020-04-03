import pyspark as ps
import pyspark.sql.functions as f  
from datetime import datetime 
from nltk.corpus import stopwords
import nltk



def filter_tweets(txt_lst, df, col):
    '''
    returns entries containing a word in txt_lst
    '''
    res = spark.createDataFrame(sc.emptyRDD(), df.schema)
    for keyword in txt_lst:
            filt_tweets = df.filter(f.lower(col).contains(keyword.lower()))
            res = res.union(filt_tweets).distinct()
    return res


list_of_key_words = ['Le Pen', 'Macron', 'président', 'présidente']

#This function will return a wordcount in the colname of the spark dataframe specified.
def get_sparkdf_wordcount(spark_df, colname, stop_word_list):
    res = spark_df.withColumn('word', f.explode(f.split(f.col(colname), ' ')))\
    .groupBy('word')\
    .count()\
    .sort('count', ascending=False)
    return res.filter(res.word.isin(stop_word_list)==False)
    #Add returning histogram of word count?
    
spark = (ps.sql.SparkSession.builder 
        .master("local[4]") 
        .appName("Spark Case Study") 
        .getOrCreate()
        )

sc = spark.sparkContext

french_tweets_df = spark.read.json('data/french_tweets.json')

french_tweets_df.createOrReplaceTempView("french_tweets_df_sample")

cleaned_tweets = spark.sql('''
                    SELECT
                        id_str,
                        user.screen_name,
                        created_at,
                        text,
                        place.full_name,
                        place.country_code
                    FROM
                        french_tweets_df_sample
                    WHERE
                        place.country_code = "FR"
''')

cand_tweets= spark.sql('''
                    SELECT
                        id_str,
                        user.screen_name,
                        created_at,
                        text,
                        place.full_name,
                        place.country_code
                    FROM
                        french_tweets_df_sample
                    WHERE
                        user.screen_name = "EmmanuelMacron" OR user.screen_name = "MLP_officiel" 
''')


hashtag_df = spark.sql('''
                    SELECT
                        id_str,
                        user.screen_name,
                        hash_tags
                    FROM
                        french_tweets_df_sample
                    LATERAL VIEW explode(entities.hashtags.text) myTable2 AS hash_tags
''')
cand_hashtag_df = spark.sql('''
                    SELECT
                        id_str,
                        user.screen_name,
                        hash_tags
                    FROM
                        french_tweets_df_sample
                    LATERAL VIEW explode(entities.hashtags.text) myTable2 AS hash_tags
                    WHERE
                        user.screen_name = "EmmanuelMacron" OR user.screen_name = "MLP_officiel" 
''')

cand_retweet_df = spark.sql('''
                    SELECT
                        id_str,
                        quoted_status.id_str,
                        quoted_status.text,
                        quoted_status.user.screen_name,
                        quoted_status.retweet_count
                    FROM
                        french_tweets_df_sample
                    WHERE
                        quoted_status.user.screen_name = "EmmanuelMacron" OR quoted_status.user.screen_name = "MLP_officiel" 
''')

user_mentions_df = spark.sql('''
                    SELECT
                        id_str,
                        user_mentions
                    FROM
                        french_tweets_df_sample
                    LATERAL VIEW explode(entities.user_mentions.screen_name) myTable3 AS user_mentions
''')

# def word_cloud(data_frame, name):
#     text = data_frame
#     wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
#     plt.figure()
#     plt.imshow(wordcloud, interpolation="bilinear")
#     plt.axis("off")
#     plt.show()


