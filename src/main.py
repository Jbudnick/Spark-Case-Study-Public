import pyspark as ps

#keep = ['Marine Le Pen', 'Emmanuel Macron']

#def 

spark = (ps.sql.SparkSession.builder 
        .master("local[4]") 
        .appName("Spark Case Study") 
        .getOrCreate()
        )
sc = spark.sparkContext


french_tweets_df = spark.read.json('data/french_tweets.json')

# french_tweets_df.printSchema()
french_tweets_df_sample = french_tweets_df.sample(withReplacement=False, fraction=0.01, seed=42)
french_tweets_df_sample2 = french_tweets_df_sample.sample(withReplacement=False, fraction=0.01, seed=44)


french_tweets_df_sample2.createOrReplaceTempView("french_tweets_df_sample")
sample_tweets= spark.sql('''
                    SELECT text
                    FROM french_tweets_df_sample
                    ''')
sample_tweets.collect() 

# schema = StructType([StructField('user_id', IntegerType(), True),
#                         StructField('name', StringType(), True),
#                         StructField('email', StringType(), True),
#                         StructField('phone', StringType(), True)])
# df_users = spark.read.csv('data/users.txt', schema = schema, header=None, sep =';')
