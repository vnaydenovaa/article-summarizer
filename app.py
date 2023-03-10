import streamlit as st
import openai
from article_summarizer.functions import summarize

try:
    openai.api_key_path = 'virtualenv-20.8.1/.streamlit/secrets.toml'

    if "summary" not in st.session_state:
        st.session_state["summary"] = ""

    st.title("Article Summarizer")

    input_text = st.text_area(label="Enter URL of Article:", value="", height=50)
    st.button(
        "Submit",
        on_click=summarize,
        kwargs={"prompt": input_text},
    )

    # Display the summarized text
    output_text = st.text_area(label="Summarized text:", value=st.session_state["summary"], height=250)

    # Display the statistics
    if "summary_length" in st.session_state and "summary_time" in st.session_state:
        st.text(f"Summary generated in {st.session_state['summary_time']:.2f} seconds")
        st.text(f"Summary length: {st.session_state['summary_length']} characters")
        st.text(f"Number of sentences: {st.session_state['num_sentences']} sentences")
        st.text(f"Number of words: {st.session_state['num_words']} words")
        st.text(f"Number of unique words: {st.session_state['unique_words']} words")
        st.text_area(label="Most common words:", value=st.session_state["most_common_words_str"], height=100)

except:
    st.write('There was an error =(')
