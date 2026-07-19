import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import preprocess


class FAQChatbot:

    def __init__(self):

        with open("faq_data.json", "r") as file:
            self.data = json.load(file)

        self.questions = [preprocess(item["question"]) for item in self.data]

        self.vectorizer = TfidfVectorizer()

        self.question_vectors = self.vectorizer.fit_transform(self.questions)

    def get_response(self, user_question):

        processed_question = preprocess(user_question)

        user_vector = self.vectorizer.transform([processed_question])

        similarity = cosine_similarity(user_vector, self.question_vectors)

        best_index = similarity.argmax()

        score = similarity[0][best_index]

        if score < 0.25:
            return "Sorry, I couldn't understand your question."

        return self.data[best_index]["answer"]
