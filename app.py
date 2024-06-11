import streamlit as st
import requests

st.set_page_config(
    page_title="VidLex - Your Video Lexicon",
    layout="centered",
    initial_sidebar_state="auto",
)

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("vendor/css/styles.css")

st.markdown('<div class="main-title">VidLex</div>', unsafe_allow_html=True)
st.markdown("### Extract and Search Words in YouTube Videos")

video_url = st.text_input(
    "Insert YouTube video link:",
    key="video_url",
    help="Paste the URL of the YouTube video you want to analyze.",
)

words = st.text_area(
    "Enter the words to search for (separated by commas):",
    key="words",
    help="Enter the words you want to search for in the video, separated by commas.",
)

if st.button("Search words", key="search_button"):
    with st.spinner("Processing..."):
        word_list = [word.strip() for word in words.split(",")]
        st.write(
            f"Sending request to backend with URL: {video_url} and words: {word_list}"
        )

        try:
            response = requests.post(
                "http://localhost:8000/transcribe/",
                json={"url": video_url, "words": word_list},
            )
            response.raise_for_status()
            results = response.json().get("results", [])

            st.success("Successfully received response from backend")
            st.markdown('<div class="results">Results:</div>', unsafe_allow_html=True)

            if results:
                for result in results:
                    st.markdown(
                        f"- **Word**: {result['word']} - **Timestamp**: {result['timestamp']} seconds"
                    )
            else:
                st.info("No results found for the given words.")

        except requests.exceptions.RequestException as e:
            st.error(f"Error transcribing the video: {str(e)}")

st.markdown("### Instructions")
st.markdown(
    """
    1. **Insert YouTube video link**: Copy and paste the URL of the YouTube video you want to analyze.
    2. **Enter words**: Type the words you want to search for in the video, separated by commas.
    3. **Click on 'Search words'**: The app will send a request to the backend to transcribe the video and search for the words.
    """
)

st.markdown(
    """
    <footer>
    <p style='text-align: center;'>Made with ❤️ by Felipe Castro</p>
    </footer>
""",
    unsafe_allow_html=True,
)
