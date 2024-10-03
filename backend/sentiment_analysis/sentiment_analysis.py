from textblob import TextBlob

def sentiment_analysis(text):
    polarity = TextBlob(text).sentiment.polarity
    return polarity