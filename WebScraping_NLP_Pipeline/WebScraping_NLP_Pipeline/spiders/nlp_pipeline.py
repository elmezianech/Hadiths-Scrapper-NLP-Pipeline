import re
import unicodedata
from nltk.corpus import stopwords
from nltk.stem.isri import ISRIStemmer
import nltk
import stanza
from qalsadi import lemmatizer


# Download the Arabic models for the neural pipeline
nlp = stanza.Pipeline('ar', processors='tokenize,lemma')
nlp1 = stanza.Pipeline('ar', processors='tokenize,ner')
nlp2 = stanza.Pipeline('ar', processors='tokenize,pos')



# Remove Diacritization
def remove_diacritics(text):
    arabic_diacritics = re.compile("""
                             ّ    | # Shadda
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)
    text = re.sub(arabic_diacritics, '', text)
    return text

# Text Cleaning and Preprocessing
def clean_text(text):
    # Remove extra whitespace and punctuation/special characters
    pattern = r"[^\w\s]"  # Matches characters that are not alphanumeric or whitespace
    text = re.sub(pattern, '', text)
    # Remove stopwords
    arabic_stopwords = stopwords.words("arabic")
    text = ' '.join(word for word in text.split() if word not in arabic_stopwords)
    # Remove Diactitics
    text = remove_diacritics(text)
    # Normalize characters for consistent representation (especially for Arabic)
    text = unicodedata.normalize('NFKD', text)
    return text

# Text Tokenization
def tokenize_text(text):
    tokens = nltk.word_tokenize(text)
    return tokens

# Stemming
def stem_tokens(tokens):
  stemmer = ISRIStemmer()
  stemmed_tokens = [stemmer.stem(token) for token in tokens]
  return stemmed_tokens

# Lemmatization using Stanza Library
def lemmatize1_text(text):
    # Process the text
    doc = nlp(text)
    # Lemmatize the tokens
    lemmatized_tokens = [word.lemma for sent in doc.sentences for word in sent.words]
    return lemmatized_tokens

# Lemmatization using Qalsadi Library
def lemmatize2_text(tokens):
    # Create a Lemmatizer object
    lemmatizer_obj = lemmatizer.Lemmatizer()
    # Lemmatize the tokens
    lemmatized_tokens = [lemmatizer_obj.lemmatize(token) for token in tokens]
    return lemmatized_tokens

# POS tagging
def pos_tagging(text):
    # Process the text
    doc = nlp2(text)
    # Extract POS tags
    pos_tags = [(word.text, word.upos) for sent in doc.sentences for word in sent.words]
    return pos_tags

# Named Entity Recognition
def ner_text(text):
    # Process the text
    doc = nlp1(text)
    # Extract entities
    entities = [(ent.text, ent.type) for sent in doc.sentences for ent in sent.ents]
    return entities



