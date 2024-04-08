import pymongo  
from nlp_pipeline import * 
import json

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['hadith_database']
collection = db['hadiths1']

# Retrieve data from MongoDB
data = [item['text'] for item in collection.find()]

# Process data through NLP pipeline
processed_data = []
for text in data:
    cleaned_text = clean_text(text)
    tokenized_text = tokenize_text(cleaned_text)
    stemmed_text = stem_tokens(tokenized_text)
    lemmatized1_text = lemmatize1_text(cleaned_text)
    lemmatized2_text = lemmatize2_text(tokenized_text)
    pos_text = pos_tagging(cleaned_text)
    ner_applied_text = ner_text(cleaned_text)
    processed_data.append(ner_applied_text)

# Write processed data to JSON file
with open('C:\\Users\\admin\\Desktop\\NLP\\WebScraping_NLP_Pipeline\\WebScraping_NLP_Pipeline\\outputs\\ner_data_stanza.json', 'w', encoding='utf-8') as f:
    json.dump(processed_data, f, indent=4, ensure_ascii=False)
