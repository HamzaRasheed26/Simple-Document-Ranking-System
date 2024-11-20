import os
import math
from collections import Counter

def load_documents(folder_path):
    """Load text documents from the specified folder."""
    documents = {}
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            with open(os.path.join(folder_path, file_name), 'r', encoding='utf-8') as f:
                documents[file_name] = f.read()
    return documents

def tokenize(text):
    """Convert text into lowercase words, removing special characters and stop words."""
    stop_words = {
        "and", "the", "is", "in", "at", "of", "on", "a", "to", "it", "for", 
        "with", "as", "was", "by", "an", "be", "that", "this", "or", "are", "from", "but"
    }
    return [word.lower() for word in text.split() if word.isalnum() and word.lower() not in stop_words]


# --- Ranking Methods ---

def rank_by_keyword_matching(documents, query):
    """Rank documents based on keyword matching."""
    query_tokens = tokenize(query)
    rankings = []
    for doc_name, content in documents.items():
        doc_tokens = tokenize(content)
        matches = 0
        for word in query_tokens:
            for d_word in doc_tokens:
                if word == d_word:
                    matches+=1
        # matches = sum(1 for word in query_tokens if word in doc_tokens)
        rankings.append((doc_name, matches))
    return sorted(rankings, key=lambda x: x[1], reverse=True)

def calculate_tf(doc):
    """Calculate term frequency for a document."""
    words = tokenize(doc)
    total_terms = len(words)
    tf = Counter(words)
    return {term: freq / total_terms for term, freq in tf.items()}

def calculate_idf(documents):
    """Calculate inverse document frequency for all terms."""
    num_docs = len(documents)
    idf = {}
    all_words = set()
    
    # Collect all unique words from all documents
    for content in documents.values():
        all_words.update(tokenize(content))
    
    # Calculate IDF for each word
    for word in all_words:
        doc_count = sum(1 for content in documents.values() if word in tokenize(content))
        idf[word] = math.log(num_docs / (1 + doc_count))  # Avoid division by zero
    return idf

def calculate_tfidf(doc, idf):
    """Calculate TF-IDF scores for a document."""
    tf = calculate_tf(doc)
    return {term: tf[term] * idf[term] for term in tf if term in idf}

def rank_by_tfidf(documents, query):
    """Rank documents based on TF-IDF scores."""
    idf = calculate_idf(documents)
    query_vector = calculate_tfidf(query, idf)
    doc_vectors = {doc_name: calculate_tfidf(content, idf) for doc_name, content in documents.items()}
    
    rankings = []
    for doc_name, vector in doc_vectors.items():
        score = sum(query_vector.get(term, 0) for term in vector)
        rankings.append((doc_name, score))
    return sorted(rankings, key=lambda x: x[1], reverse=True)

def cosine_similarity(vec1, vec2):
    """Calculate cosine similarity between two vectors."""
    dot_product = sum(vec1[term] * vec2.get(term, 0) for term in vec1)
    magnitude1 = math.sqrt(sum(val ** 2 for val in vec1.values()))
    magnitude2 = math.sqrt(sum(val ** 2 for val in vec2.values()))
    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    return dot_product / (magnitude1 * magnitude2)

def rank_by_cosine_similarity(documents, query):
    """Rank documents based on cosine similarity to the query."""
    idf = calculate_idf(documents)
    query_vector = calculate_tfidf(query, idf)
    doc_vectors = {doc_name: calculate_tfidf(content, idf) for doc_name, content in documents.items()}
    
    rankings = []
    for doc_name, vector in doc_vectors.items():
        similarity = cosine_similarity(query_vector, vector)
        rankings.append((doc_name, similarity))
    return sorted(rankings, key=lambda x: x[1], reverse=True)

# --- Display Results ---
def display_ranked_documents(ranked_docs, documents, top_n=5):
    """Display ranked documents with snippets."""
    print("\nTop Relevant Documents:\n")
    for i, (doc_name, score) in enumerate(ranked_docs[:top_n], start=1):
        print(f"{i}. {doc_name} (Score: {score:.4f})")
        print(f"Snippet: {documents[doc_name][:200]}...\n")  # Display first 200 characters

# --- Main Program ---
def main():
    folder_path = os.path.join(os.getcwd(), "Docs")
    documents = load_documents(folder_path)
    
    if not documents:
        print("No valid documents found in the specified folder.")
        return
    
    print(f"Loaded {len(documents)} documents.")
    
    while True:
        query = input("\nEnter your query (or type 'exit' to quit): ").strip()
        if query.lower() == 'exit':
            print("Exiting Document Ranking System. Goodbye!")
            break
        
        print("\nChoose a ranking method:")
        print("1. Keyword Matching")
        print("2. TF-IDF Scoring")
        print("3. Cosine Similarity")
        method = input("Enter the number of your choice: ").strip()
        
        if method == '1':
            ranked_docs = rank_by_keyword_matching(documents, query)
        elif method == '2':
            ranked_docs = rank_by_tfidf(documents, query)
        elif method == '3':
            ranked_docs = rank_by_cosine_similarity(documents, query)
        else:
            print("Invalid choice. Please try again.")
            continue
        
        display_ranked_documents(ranked_docs, documents)

if __name__ == "__main__":
    main()
