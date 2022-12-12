# citing this tutorial: https://towardsdatascience.com/end-to-end-topic-modeling-in-python-latent-dirichlet-allocation-lda-35ce4ed6b3e0
import re
import pandas as pd
import os

# file
def lda_basic(file, filename, num_topics):
    reviews = pd.read_csv(file)

    # remove punctuation
    reviews['review_processed'] = reviews['Comment'].map(lambda x: re.sub('[,\.!?]', '', x))

    # convert to lowercase
    reviews['review_processed'] = reviews['review_processed'].map(lambda x: x.lower())

    # Prepare data for LDA Analysis
    import gensim
    from gensim.utils import simple_preprocess
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    stop_words = stopwords.words('english')
    # stop_words.extend(['from', 'subject', 're', 'edu', 'use'])
    def sent_to_words(sentences):
        for sentence in sentences:
            # deacc=True removes punctuations
            yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))
    def remove_stopwords(texts):
        return [[word for word in simple_preprocess(str(doc))
                 if word not in stop_words] for doc in texts]
    data = reviews.review_processed.values.tolist()
    data_words = list(sent_to_words(data))
    # remove stop words
    data_words = remove_stopwords(data_words)
    print(data_words[:1][0][:30])

    import gensim.corpora as corpora
    # Create Dictionary
    id2word = corpora.Dictionary(data_words)
    # Create Corpus
    texts = data_words
    # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in texts]
    # View
    print(corpus[:1][0][:30])

    # LDA model training

    from pprint import pprint

    # Build LDA model
    lda_model = gensim.models.LdaMulticore(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=num_topics)
    # Print the Keyword in the 10 topics
    pprint(lda_model.print_topics())
    doc_lda = lda_model[corpus]

    # Analyzinng LDA model results
    import pyLDAvis.gensim_models as gensimvis
    import pickle
    import pyLDAvis
    # Visualize the topics
    # pyLDAvis.enable_notebook()
    LDAvis_data_filepath = os.path.join('./results/ldavis_prepared_'+str(num_topics))
    # # this is a bit time consuming - make the if statement True
    # # if you want to execute visualization prep yourself
    if 1 == 1:
        LDAvis_prepared = gensimvis.prepare(lda_model, corpus, id2word)
        with open(LDAvis_data_filepath, 'wb') as f:
            pickle.dump(LDAvis_prepared, f)
    # load the pre-prepared pyLDAvis data from disk
    with open(LDAvis_data_filepath, 'rb') as f:
        LDAvis_prepared = pickle.load(f)
    pyLDAvis.save_html(LDAvis_prepared, './results/ldavis_'+ filename + '_' + str(num_topics) +'.html')

if __name__ == "__main__":
    # lda_basic("data/sets_comments/total/sgender/sfemale.csv", "sfemale");
    # lda_basic("data/sets_comments/total/sgender/smale.csv", "smale");
    for i in range(2,11):
        lda_basic("data/comment_total.csv", "comment_total", i);