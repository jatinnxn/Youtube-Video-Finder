import streamlit as st
import datetime
import isodate
import speech_recognition as sr
import google.generativeai as genai
from googleapiclient.discovery import build

# ================== CONFIG ==================
YOUTUBE_API_KEY = "AIzaSyAS23pGpiq8lVR2c5cxoEladNM4aAHW0e0"
GEMINI_API_KEY = "AIzaSyCwM2cBwHC7u9WGnvIPPYn0IdmW5ufM2fc"
genai.configure(api_key=GEMINI_API_KEY)

# ================== YOUTUBE SETUP ==================
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

def search_youtube(query):
    two_weeks_ago = (datetime.datetime.now() - datetime.timedelta(days=14)).isoformat("T") + "Z"
    response = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=50,
        publishedAfter=two_weeks_ago
    ).execute()
    
    results = []
    for item in response["items"]:
        video_id = item["id"]["videoId"]
        title = item["snippet"]["title"]
        results.append((video_id, title))
    return results

def parse_duration_to_minutes(duration_str):
    duration = isodate.parse_duration(duration_str)
    return duration.total_seconds() / 60

def filter_by_duration(videos):
    filtered = []
    video_ids = [v[0] for v in videos]

    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i+50]
        response = youtube.videos().list(
            part="contentDetails,snippet",
            id=",".join(batch)
        ).execute()

        for item in response["items"]:
            video_id = item["id"]
            title = item["snippet"]["title"]
            duration = item["contentDetails"]["duration"]
            minutes = parse_duration_to_minutes(duration)
            if 4 <= minutes <= 20:
                filtered.append((video_id, title))
    return filtered

def analyze_titles_with_gemini(query, videos):
    titles = [title for _, title in videos]
    prompt = f"""You are an intelligent assistant. A user is searching YouTube for: "{query}". 
Below are some video titles. Choose the best one based on clarity, appeal, and relevance to the query.

Return ONLY the best title and video ID.

Videos:
{chr(10).join([f"{i+1}. {title}" for i, (vid, title) in enumerate(videos)])}
"""

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Speak your search query...")
        audio = recognizer.listen(source, phrase_time_limit=7)
        try:
            text = recognizer.recognize_google(audio, language="hi-IN")
            st.success(f"You said: {text}")  # Show the recognized text immediately
            return text
        except sr.UnknownValueError:
            st.error("Could not understand audio")
            return None
        except sr.RequestError:
            st.error("Speech service unavailable")
            return None

# ================== STREAMLIT UI ==================
st.set_page_config(page_title="YouTube Video Finder", layout="centered")
st.title("🔍 YouTube Video Finder with Gemini AI")
st.markdown("Search YouTube using voice or text. Filtered & ranked with Google's Gemini AI.")

input_method = st.radio("Choose input method:", ["🎤 Voice", "⌨️ Text"])
query = ""

if input_method == "🎤 Voice":
    if st.button("Record Voice"):
        query = get_voice_input()
        if query:
            st.success(f"You said: {query}")  # Show immediately after voice input
else:
    query = st.text_input("Enter your search query")

# This block ensures that the action happens after voice input and button click.
if st.button("Find Best Video") and query:
    with st.spinner("Searching and analyzing..."):
        initial_results = search_youtube(query)
        st.markdown(f"🔍 Found `{len(initial_results)}` initial results from YouTube.")

        if not initial_results:
            st.warning("No results from YouTube search.")
        else:
            filtered_videos = filter_by_duration(initial_results)
            st.markdown(f"✅ `{len(filtered_videos)}` videos matched filters (4–20 mins, last 14 days).")

            if not filtered_videos:
                st.warning("No videos matched your filters.")
            else:
                st.markdown("### 📋 Filtered Video Titles:")
                for i, (vid, title) in enumerate(filtered_videos[:10]):
                    st.markdown(f"{i+1}. {title}")

                best_video_info = analyze_titles_with_gemini(query, filtered_videos)
                st.subheader("🎯 Gemini AI Suggests:")
                st.markdown(best_video_info)

                # Try to match a video by title or fallback
                matched = False
                for vid, title in filtered_videos:
                    if title in best_video_info:
                        matched = True
                        st.video(f"https://www.youtube.com/watch?v={vid}")
                        break

                if not matched:
                    vid, _ = filtered_videos[0]
                    st.markdown("⚠️ Could not match title exactly. Showing top filtered video instead.")
                    st.video(f"https://www.youtube.com/watch?v={vid}")
