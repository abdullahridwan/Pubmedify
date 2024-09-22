# PubMedify



[![Streamlit](https://img.shields.io/badge/streamlit-v1.38.0-brightgreen)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/python-v3.8-blue)](https://www.python.org/)
[![NLTK](https://img.shields.io/badge/nltk-v3.9.1-yellow)](https://www.nltk.org/)
[![PubMed API](https://img.shields.io/badge/pubmed--api-v1.0-orange)](https://www.ncbi.nlm.nih.gov/home/develop/api/)
[![Pymed](https://img.shields.io/badge/pymed-v0.8.9-lightgrey)](https://pypi.org/project/pymed/)

## Overview

**PubMedify** is a tool designed to streamline the process of conducting systematic reviews by identifying common words within the titles and abstracts of selected PubMed articles. This app allows researchers to quickly spot key terms shared among a set of articles, facilitating a more efficient review process.


https://github.com/user-attachments/assets/6a735c8f-df2f-47c6-8079-3b74e58dc24f


## Problem

Conducting systematic reviews often involves identifying and synthesizing key terms across multiple research articles. Traditionally, this can be a tedious process of manually reviewing and comparing articles to find commonalities. PubMedify automates this task, saving researchers valuable time and ensuring no critical terms are overlooked.

## How It Works

1. **Input PubMed IDs**: Enter the PubMed IDs of the articles you wish to analyze.
2. **Analyze Text**: The app retrieves the titles and abstracts of the articles using Pymed, built on top of the PubMed API.
3. **Extract Common Words**: PubMedify identifies the most common words in the titles and abstracts.
4. **View Results**: See a list of common words along with a quick reference to the articles that include each word.

## Features

- **Quick Input**: Easily input PubMed IDs of interest.
- **Automated Retrieval**: Automatically fetch titles and abstracts from PubMed.
- **Interactive Results**: View common words and their corresponding articles in an interactive interface.
- **Verify**: For each word, quickly see all relevant Paper title and Abstracts


## Usage

1. Open this app in your browser: [pubmedify.streamlit.app](https://pubmedify.streamlit.app/)
2. Enter the PubMed IDs of the articles you want to analyze.
3. Click "Submit"!

## Contributing

We welcome contributions! Please message me at abdullahridwan73@gmail.com for questions!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please open an issue or contact us at abdullahridwan73@gmail.com.
