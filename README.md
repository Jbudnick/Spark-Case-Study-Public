# Politics Makes Strange Bedfellows
In 2017, Emmanuel Macron and Marine Le Pen were the final two candidates in the French Presidential Election.  The two candidates had drastically different approaches to governing, and as such, the election was a major topic of discussion on Twitter.

# Data Cleaning
Our first step was stripping down this dataset to what we considered useful.


## Strip columns
We kept the following columns:
1. Tweet ID,
1. Screen Name,
1. Tweet Timestamp,
1. Tweet Body,
1. Location Name,
1. Location - Country
1. Hashtags
1. Retweets
1. Mentioned Users

<br>

## Strip Rows

After limiting the number of fields we were working with, we worked to strip down the dataset to only tweets involving the French election.

We found there were some tweets made from England (not France?), so we tossed those.

To do this, we chose some keywords. If the tweet didn't contain one of the keywords, we tossed it out.

To start, we chose the following keywords:
1. 'Le Pen'
1. 'Macron'
1. 'président'
1. 'présidente'

This keyword filtering brought out original dataset of **214,936** tweets down to **9,331**.

![Image](images/filtered_counts.png)

From these filtered tweets, we took the word frequency vector:
```bash
+---------------+-----+                                                         
|           word|count|
+---------------+-----+
|         macron| 2851|
|@emmanuelmacron| 1891|
|               | 1294|
|              a| 1236|
|            pen| 1125|
|              !| 1012|
|          c'est|  967|
|        #macron|  865|
|          voter|  662|
|         marine|  586|
|              ?|  554|
|              :|  510|
|           plus|  457|
|             va|  437|
|             ça|  415|
```

Given more time, we would filter whitespace and punctuation. We would also combine words regardles of case (ex. MACRON vs. Macron).

