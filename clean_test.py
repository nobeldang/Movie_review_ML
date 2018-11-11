from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import sys
tokenizer=RegexpTokenizer(r'\w+')
en_stopwords=set(stopwords.words('english'))
ps=PorterStemmer()
def getStemmedReview(review):
    review=review.lower()
    tokens=tokenizer.tokenize(review)
    filtered_tokens=[w for w in tokens if w not in en_stopwords]
    stemmed_tokens=[ps.stem(w) for w in filtered_tokens]
    cleaned_review=' '.join(stemmed_tokens)
    return cleaned_review