# Document Ranking System

## Overview
The **Document Ranking System** is a Python-based tool that ranks text documents based on their relevance to a user's query. It provides three ranking methods:  
1. **Keyword Matching**  
2. **TF-IDF Scoring**  
3. **Cosine Similarity**

This tool is designed for simple information retrieval tasks and demonstrates fundamental concepts of document ranking.

---

## Features
- **Load Documents**: Reads `.txt` files from a folder, where each document contains a title and content.  
- **Tokenization**: Cleans and tokenizes text, removing special characters and common stop words.  
- **Ranking Techniques**:
  - **Keyword Matching**: Counts query word matches in a document.
  - **TF-IDF Scoring**: Weighs terms based on their frequency and distinctiveness.
  - **Cosine Similarity**: Measures semantic similarity between query and document vectors.
- **Interactive Query Interface**: Allows users to input queries and select a ranking method dynamically.
- **Top Results Display**: Displays ranked documents with scores and snippets.

---

## Prerequisites
- **Python 3.7 or higher**  
- **Basic Text Files**: Place documents in a folder named `Docs` in the project directory. Each file should have the following format:  

```
Title: [Document Title] Content: [Document Content]
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/document-ranking-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd document-ranking-system
   ```
3. Ensure the **Docs** folder exists and contains your **.txt** files.

## Usage
1. Run the program:
   ```bash
    python ranking_system.py
   ```
2. Choose a ranking method:
    ```markdown
    Choose a ranking method:
    1. Keyword Matching
    2. TF-IDF Scoring
    3. Cosine Similarity
    ```
3. Enter a query when prompted:
    ```bash
    Enter your query (or type 'exit' to quit): climate change impacts
    ```

4. View the results:
    * Ranked documents will be displayed with their relevance scores and a snippet of content.