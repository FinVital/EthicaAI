import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Download NLTK data
nltk.download('vader_lexicon')

def analyze_dilemma(dilemma):
    """
    Analyze the ethical dilemma using sentiment analysis.
    """
    sia = SentimentIntensityAnalyzer()
    context = dilemma.get('context', '')
    stakeholders = dilemma.get('stakeholders', '')
    decisions = dilemma.get('decisions', '')
    
    # Combine all text inputs for analysis
    combined_text = f"{context} {stakeholders} {decisions}"
    
    # Perform sentiment analysis
    sentiment_scores = sia.polarity_scores(combined_text)
    
    analysis = {
        "negative": sentiment_scores['neg'],
        "neutral": sentiment_scores['neu'],
        "positive": sentiment_scores['pos'],
        "compound": sentiment_scores['compound']
    }
    
    return f"Sentiment Analysis - Negative: {analysis['negative']}, Neutral: {analysis['neutral']}, Positive: {analysis['positive']}, Compound: {analysis['compound']}"

def simulate_scenarios(dilemma):
    """
    Simulate different decision scenarios using clustering.
    """
    decisions = dilemma.get('decisions', '').split('.')
    if len(decisions) <= 1:
        return "Not enough decisions to simulate scenarios."
    
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(decisions)
    
    # Clustering decisions to find patterns
    num_clusters = min(len(decisions), 3)
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(X)
    
    clusters = {i: [] for i in range(num_clusters)}
    for i, label in enumerate(kmeans.labels_):
        clusters[label].append(decisions[i])
    
    simulation_results = "Scenario Simulation Results:\n"
    for cluster, items in clusters.items():
        simulation_results += f"\nCluster {cluster + 1}:\n"
        for item in items:
            simulation_results += f"- {item.strip()}\n"
    
    return simulation_results

def get_recommendations(dilemma):
    """
    Generate recommendations based on ethical theories and cultural norms.
    """
    ethical_theories = dilemma.get('ethical_theories', '').split(',')
    cultural_norms = dilemma.get('cultural_norms', '').split(',')
    
    recommendations = "Recommendations based on Ethical Theories and Cultural Norms:\n"
    
    if ethical_theories:
        recommendations += "\nEthical Theories:\n"
        for theory in ethical_theories:
            recommendations += f"- Apply principles of {theory.strip()}.\n"
    
    if cultural_norms:
        recommendations += "\nCultural Norms:\n"
        for norm in cultural_norms:
            recommendations += f"- Consider the cultural aspect: {norm.strip()}.\n"
    
    return recommendations.strip()
