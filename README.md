# Hadiths-Scrapper-NLP-Pipeline

## Project Description

The HadithScraperNLP project is aimed at scraping Hadiths from various pages of the website https://mawdoo3.com/, storing the raw data in a MongoDB database, and applying Natural Language Processing (NLP) techniques on the scraped text. The NLP pipeline includes processes such as text cleaning, tokenization, stemming, lemmatization using different libraries, Part-of-Speech (POS) tagging, and Named Entity Recognition (NER).

## Technologies Used

The project utilizes the following technologies and libraries:

- Python: The primary programming language used for development.
- Scrapy: A Python framework for web scraping, employed for extracting data from HTML pages.
- MongoDB: A NoSQL database used for storing the raw Hadith data.
- PyMongo - A Python driver for MongoDB.
- NLTK: A natural language processing library for Python, used for text preprocessing tasks such as tokenization and stopwords removal, and yes it worked well!! :)
- Stanza: A Python NLP library for Arabic, utilized for lemmatization, POS tagging, and NER.
- Qalsadi: A Python library for Arabic lemmatization, to compare it with the result of Stanza.
- Regular Expressions (Regex): Used for text pattern matching and cleaning.
- unicodedata: Employed for normalizing Unicode characters.

## Project Structure 

- myspider.py: Contains the Scrapy spider for scraping Hadiths from specified URLs and storing them in MongoDB.
- nlp_pipeline.py: Implements the NLP pipeline including text cleaning, tokenization, stemming, lemmatization, POS tagging, and NER.
- main.py: Retrieves data from MongoDB, applies the NLP pipeline, and stores the processed data in JSON format.
- outputs: Directory containing the output JSON files generated by the main.py script.

## Results and Output Files

Upon completion, the output directory contains the following processed data files:

- Raw Data : The raw data represents the Hadiths attributed to the Prophet Muhammad (peace be upon him), here is an example of a hadith, translated as: "If the Final Hour comes while you have a shoot of a plant in your hands and it is possible to plant it before the Hour comes, you should plant it."
here is the snipet of the hadith : {"text": "قال رسول الله صلى الله عليه وسلم:(إنْ قامَتِ الساعةُ وفي يدِ أحدِكمْ فَسِيلةٌ، فإنِ استطاعَ أنْ لا تقومَ حتى يَغرِسَها فلْيغرِسْهَا)"}

- Cleaned Data : The cleaned data removes unnecessary characters and simplifies the text while preserving its meaning.
The cleaned version of the Hadith is: "قامت الساعة وفي يد أحدكم فسيلة استطاع تقوم يغرسها فليغرسها"

- Tokenized Data : The tokenized data breaks down the cleaned Hadith into individual words.
Here, each word is represented separately, forming the following tokens: ["قامت", "الساعة", "وفي", "يد", "أحدكم", "فسيلة", "استطاع", "تقوم", "يغرسها", "فليغرسها"]

- Stemmed Data : The stemmed data reduces each word to its root form using ISRIStemmer. For example, "قامت" becomes "قمت", ""الساعة becomes "سعة", and "فسيلة" becomes "فسل".

- Lemmatized Data Using Stanza : The lemmatized data using the Stanza library provides the base forms of words. For instance, "قام" represents the lemma of "قامت", and "يغرس" represents the lemma of "يغرسها".

- Lemmatized Data Using Qalsadi : Similarly, the lemmatized data using the Qalsadi library offers the base forms of words. For example, "قام" represents the lemma of "قامت", and "أغرس" represents the lemma of "يغرسها".

Lemmatization proves superior to stemming as it accurately preserves the meaning of words by reducing them to their base forms. This ensures consistency and clarity in understanding the text.

- POS Tagging : The POS tagging assigns grammatical categories to each word in the Hadith. For example, "قامت" is tagged as a verb (VERB), "الساعة" as a noun (NOUN), and "في" as a conjunction (CCONJ).

- Named Entity Recognition (NER) : The NER process identifies named entities in the text. However, the NER using Stanza appears to have limitations as it didn't identify all the entities present in the text. For instance, while it correctly tagged "المغرب" as a location (LOC) and "المسلمون" as a person (PER), it missed other entities present in the text. This suggests that the NER performance using Stanza may not be comprehensive and may require further refinement or additional training data to improve its accuracy.

## Overall Assessment

The processed data showcases successful application of various NLP techniques, including cleaning, tokenization, stemming, lemmatization, POS tagging, and NER. These techniques help in understanding the linguistic structure and semantic content of the Hadith, facilitating further analysis and interpretation. The results appear accurate and provide valuable insights into the text.




