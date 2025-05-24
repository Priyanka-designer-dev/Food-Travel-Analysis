Blog Text Analyzer

Overview:
This Python script processes a folder of blog text files to perform basic natural language processing (NLP) tasks. It analyzes word frequency, visualizes the data using bar charts and word clouds, and evaluates overall sentiment using TextBlob.

Features:
- Loads and combines all .txt files from a specified folder
- Cleans and filters stopwords
- Generates and saves:
  - Bar chart of top 10 most frequent words
  - Word cloud visualization
- Performs sentiment analysis (positive, negative, or neutral)

Requirements:
- Python 3.x
- Libraries: os, collections, matplotlib, wordcloud, textblob, nltk

Usage:
1. Place your .txt files inside a folder named 'data' in the same directory as the script.
2. Run the script using: python <script_name>.py
3. Output visualizations (top_words_chart.png, wordcloud.png) will be saved in the directory.

Note:
- Ensure stopwords are available by downloading via nltk.download('stopwords').
