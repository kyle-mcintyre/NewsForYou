import pickle, string
from sklearn import svm
from gensim.parsing.preprocessing import remove_stopwords
from gensim.parsing.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.utils import get_stop_words
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lex_rank import LexRankSummarizer

class newsScoringMachine:
    def __init__(self, dummy = ''):
        self.dummy = dummy

    def cleanText(self, textToClean):
        textLower = str(textToClean).lower()
        englishText = "".join([char for char in textLower if char in string.printable])
        textNoPunc = "".join([char for char in englishText if char not in string.punctuation])
        textStop = remove_stopwords(textNoPunc)
        porter = PorterStemmer()
        textStemmed = porter.stem(textStop)
        return(textStemmed.split()) 


    def scoreArticle(self, text):
        filename = 'newsBiasPredictModel.sav'
        vectorFile = 'newsVectorizor.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        loaded_vectorizor = pickle.load(open(vectorFile, 'rb'))

        text_cleaned = self.cleanText(text)
        textVector = loaded_vectorizor.transform(text_cleaned)
        score = loaded_model.predict(textVector)
        score = score[0]

        category = ""
        if(score == 1):
            category = "Liberal"
        elif(score == 3):
            category = "No"
        elif(score == 5):
            category = "Conservative"

        return category

    def summarize(self, text):
        sumReturn = ''
        parser = PlaintextParser.from_string(text,Tokenizer("english"))
        summarizer = LexRankSummarizer()
        summary = summarizer(parser.document, 1)
        for sentence in summary:
            sumReturn = sumReturn + str(sentence)
        return sumReturn


