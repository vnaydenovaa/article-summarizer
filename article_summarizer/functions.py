import openai
import streamlit as st
import time
import string
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist


def summarize(prompt):
    augmented_prompt = f"summarize this article in 5-10 sentences: {prompt}"
    try:
        # Track start time
        start_time = time.time()

        # Generate summary using GPT-3-5 "turbo" model
        summary = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": augmented_prompt}],
            temperature=.2,
            max_tokens=2048,
        )["choices"][0]["message"]["content"]

        # Track end time
        end_time = time.time()

        # Calculate summary length
        summary_length = len(summary)

        # Calculate summary statistics using NLTK
        sentences = sent_tokenize(summary)
        words = word_tokenize(summary)
        stop_words = set(stopwords.words("english"))
        words_filtered = [word.lower() for word in words if word.lower() not in stop_words and word not in string.punctuation]
        num_sentences = len(sentences)
        num_words = len(words_filtered)
        unique_words = len(set(words_filtered))
        fdist = FreqDist(words_filtered)
        most_common_words = fdist.most_common(10)

        most_common_words_str = ", ".join([f"{word} ({count})" for word, count in most_common_words])

        # Update session state with statistics
        st.session_state["summary_length"] = summary_length
        st.session_state["summary_time"] = end_time - start_time
        st.session_state["num_sentences"] = num_sentences
        st.session_state["num_words"] = num_words
        st.session_state["unique_words"] = unique_words
        st.session_state["most_common_words_str"] = most_common_words_str

        # Update session state with summary text
        st.session_state["summary"] = summary
    except:
        st.write('There was an error')