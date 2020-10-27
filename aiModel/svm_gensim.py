import string, sys, pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, svm
from sklearn.metrics import accuracy_score, plot_confusion_matrix
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from gensim.parsing.preprocessing import remove_stopwords
from gensim.parsing.porter import PorterStemmer

newsData = pd.read_csv('summary.csv')
print("Read Data")


def cleanText(text):
    textLower = str(text).lower()
    englishText = "".join([char for char in textLower if char in string.printable])
    textNoPunc = "".join([char for char in englishText if char not in string.punctuation])
    textStop = remove_stopwords(textNoPunc)
    porter = PorterStemmer()
    textStemmed = porter.stem(textStop)
    
    return(textStemmed.split())    


newsData['summary']= [cleanText(entry) for entry in newsData['summary']]
print("Cleaned Data")
newsData['summary']=["".join(text) for text in newsData['summary'].values]



Train_X, Test_X, Train_Y, Test_Y = model_selection.train_test_split(newsData['summary'], newsData['bias-score'],test_size=0.2)


vectorizer = TfidfVectorizer(use_idf = True, max_df=.2, min_df=0, norm='l1')
train_vectors = vectorizer.fit_transform(Train_X)
test_vectors = vectorizer.transform(Test_X)


# fit the training dataset on the classifier
SVMmodel = svm.SVC(C=500, kernel='linear', gamma='scale')
SVMmodel.fit(train_vectors,Train_Y)

### For testing purposes ###
# predictions_SVM = SVMmodel.predict(test_vectors)
# print("SVM Accuracy Score -> ",accuracy_score(predictions_SVM, Test_Y)*100)
# plot_confusion_matrix(SVMmodel, test_vectors, Test_Y)  
# plt.show()

filename = 'newsBiasPredictModel.sav'
vectorFile = 'newsVectorizor.sav'
pickle.dump(SVMmodel, open(filename, 'wb'))
pickle.dump(vectorizer, open(vectorFile, 'wb'))
