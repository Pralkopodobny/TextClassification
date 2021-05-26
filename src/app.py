from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
if __name__ == '__main__':
    y = pd.read_csv('.\\scale_data\\scaledata\\Dennis+Schwartz\\subj2.Dennis+Schwartz', error_bad_lines=False, delimiter='twuj kutas jebany', header=None)
    vectorizer = CountVectorizer(max_features=20, ngram_range=(2,2))
    X = vectorizer.fit_transform(y[0])
    print(X.toarray())
    print(vectorizer.get_feature_names())
