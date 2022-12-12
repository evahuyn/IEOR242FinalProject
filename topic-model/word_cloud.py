from wordcloud import WordCloud
import re
import pandas as pd
import os

data_path = './data/comment_total.csv'
reviews = pd.read_csv(data_path)

# remove punctuation
reviews['review_processed'] = reviews['Comment'].map(lambda x: re.sub('[,\.!?]', '', x))
# convert to lowercase
reviews['review_processed'] = reviews['review_processed'].map(lambda x: x.lower())

long_string = ','.join(list(reviews['review_processed'].values))
wordcloud = WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color='steelblue')
wordcloud.generate(long_string)
wordcloud.to_image()


