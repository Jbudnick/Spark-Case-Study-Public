import pyspark as ps

spark = (ps.sql.SparkSession.builder 
        .master("local[4]") 
        .appName("sparkSQL exercise") 
        .getOrCreate()
        )
sc = spark.sparkContext


french_tweets_df = spark.read.json('data/french_tweets.json')

french_tweets_df.printSchema()

# schema = StructType([StructField('user_id', IntegerType(), True),
#                         StructField('name', StringType(), True),
#                         StructField('email', StringType(), True),
#                         StructField('phone', StringType(), True)])
# df_users = spark.read.csv('data/users.txt', schema = schema, header=None, sep =';')