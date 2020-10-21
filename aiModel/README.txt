The "summary.csv" file contains all the data that was used to create the ai model. 

The "url" tab corresponds to the url of the news articles.
The "summary" tab corresponds to the summary of the article.
The "bias-score" tab is the resulting score the news article was given.
A 1 implies it has a liberal bias.
A 3 implies it has no bias.
A 5 implies it has a conservative bias.

The data is then fed through the svm_gensim.py class and the ai model, as well as the vectorizor, is saved.