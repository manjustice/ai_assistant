import openai
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

from app.config import OPENAI_API_KEY, FAQ_DATA

openai.api_key = OPENAI_API_KEY


def find_best_match(question):
    best_match_score = 0
    best_match_question = None

    for faq in FAQ_DATA:
        score = calculate_similarity(
            question,
            [faq["Question_short"]]
            + faq["Question_short_alternatives"]
            + faq["Question_original_alternatives"]
            + faq["Keywords"]
        )

        if score > best_match_score:
            best_match_score = score
            best_match_question = faq["Question_short"]
    return best_match_question


def calculate_similarity(question1, questions):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([question1] + questions)
    similarity_scores = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:])
    max_score = similarity_scores.max()
    return max_score


def find_answer(question):
    best_match_question = find_best_match(question)

    if best_match_question:
        faq = next(
            (
                item
                for item in FAQ_DATA
                if item["Question_short"] == best_match_question
            ),
            None
        )

        if faq:
            user_question = f"User: {question}"
            assistant_question = faq["Question_short"]

            messages = [
                {"role": "system", "content": faq["Notes"]},
                {"role": "user", "content": user_question},
                {"role": "assistant", "content": assistant_question},
            ]

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=2500,
                temperature=0.5,
            )

            if response.choices and response.choices[0].message["role"] == "assistant":
                return response.choices[0].message["content"].strip()

    return "No answer found"
