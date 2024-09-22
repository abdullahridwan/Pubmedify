import nltk
import pymed
import re
import streamlit as st
import pandas as pd
from nltk.corpus import stopwords
from pymed import PubMed

# Download stopwords if not already downloaded
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

pubmed = PubMed(tool="MyTool", email="abdullahridwan@gmail.com")

# Helper Functions
def get_articles(lst_aid: [str]) -> dict:
    article_dicts = []
    articles = pubmed._getArticles(lst_aid)
    for article in articles:
        article_dicts.append(article.toDict())
    return article_dicts

def get_set_of_words(text: str):
    words = re.sub('\W+', ' ', text).split(" ")
    no_stop_words = [word.lower() for word in words if word.lower() not in stop_words]
    set_of_words = set(no_stop_words)
    if '' in set_of_words:
        set_of_words.remove('')
    return set_of_words

def get_word_map(ids: [str]) -> dict:
    words = {}
    articles = get_articles(ids)
    for article in articles:
        article_id = article.get("pubmed_id")
        txt = article.get("title") + " " + article.get("abstract")
        word_set = get_set_of_words(txt)
        for word in word_set:
            if word in words:
                words[word].append(article_id)
            else:
                words[word] = [article_id]
    return words, articles

def make_df(wm: dict):
    data = [{"Word": key, "Ids": value} for key, value in wm.items()]
    return pd.DataFrame(data)

def find_article(articles: list, aid: str):
    return next(a for a in articles if a["pubmed_id"] == aid)

# Streamlit app
st.title("Pubmedify")

# Initialize session state variables
if 'df' not in st.session_state:
    st.session_state.df = None
if 'wm' not in st.session_state:
    st.session_state.wm = None
if 'article_dicts' not in st.session_state:
    st.session_state.article_dicts = None

# Input for PubMed article IDs
st.markdown("## 1. 🪪 Input a List of Pubmed IDs")
ids_string = st.text_area(label="Input IDs separated by a comma", placeholder="34175218, 33502370")
st.caption("✨ Try these 2 Pubmed articles: 34175218, 33502370")

# Show the list of IDs
lst_ids = [w.strip() for w in ids_string.split(",") if w.strip()]

# Submit button to process the IDs
if st.button("Submit"):
    if lst_ids:  # Ensure there's input
        st.session_state.wm, st.session_state.article_dicts = get_word_map(lst_ids)
        st.session_state.df = make_df(st.session_state.wm)
        st.session_state.df['Count'] = st.session_state.df['Ids'].apply(len)
        st.session_state.df = st.session_state.df.sort_values(by='Count', ascending=False)

# Always display the DataFrame if it exists
if st.session_state.df is not None:
    st.markdown("## 2. 🌎 See all Words for all Titles and Abstracts")
    st.dataframe(st.session_state.df, use_container_width=True)


    st.markdown("## 3. 🔍 Investigate")
    st.markdown("Choose a word from the table in the dropdown below, to see the title and abstract of papers that contain that word")
    # Create a dropdown for selecting a word
    selected_word = st.selectbox("Select a word:", st.session_state.df['Word'].tolist())

    # Get the IDs for the selected word and display articles
    if selected_word:
        related_article_ids = st.session_state.wm[selected_word]
        articles = [find_article(st.session_state.article_dicts, r) for r in related_article_ids]
        st.markdown(f" ### 🗃️ Seeing related Titles & Abstracts for: :red[{selected_word}]")

        for article in articles:
            container = st.container(border=True)
            container.write("### " + article["title"])
            container.write(f":red[{article['doi']}]")
            container.write(article["abstract"])
