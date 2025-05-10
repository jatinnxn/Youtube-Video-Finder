Here's a **README.md** template to deploy your project on GitHub:

---

## **YouTube Video Finder with Gemini AI**

This is a Streamlit-based web application that lets users search for YouTube videos by voice or text input. It filters YouTube search results based on specific criteria, analyzes the video titles using **Gemini AI**, and provides the best video suggestion directly in the web app.

---

### **Features**

* **Voice Input**: Users can search by voice in Hindi or English.
* **Text Input**: Alternatively, users can enter their query as text.
* **Filters**: Videos are filtered based on:

  * **Duration**: Only videos between **4-20 minutes**.
  * **Recency**: Only videos posted in the **last 14 days**.
* **AI Analysis**: The titles of the videos are analyzed by **Gemini AI** to recommend the best video based on clarity, appeal, and relevance.
* **Direct YouTube Embed**: The best video is displayed directly in the app using the `st.video()` component or via a clickable link to YouTube.

---

### **Tech Stack**

* **Frontend**: Streamlit (for the web app)
* **Backend**: Python
* **API Integrations**:

  * **YouTube Data API** (for video search)
  * **Google Gemini API** (for title analysis)
* **Voice Recognition**: SpeechRecognition library (using Google Speech-to-Text API)
* **Audio Input**: `pyaudio` for capturing microphone input

---

### **Getting Started**

#### 1. **Clone the Repository**

```bash
git clone https://github.com/your-username/youtube-video-finder.git
cd youtube-video-finder
```

#### 2. **Install Dependencies**

Make sure you have Python installed. Then, install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

#### 3. **API Keys**

To use the **YouTube Data API** and **Gemini API**, you need to generate your API keys:

* **YouTube API Key**:

  * Go to the [Google Developer Console](https://console.developers.google.com/).
  * Create a new project and enable the **YouTube Data API v3**.
  * Generate an API key and replace it in the `app.py` file.

* **Gemini API Key**:

  * Sign up on [Google Gemini](https://developers.google.com/ai/gemini).
  * Get the API key for Gemini and add it to the `app.py` file.

#### 4. **Run the Streamlit App**

Once the dependencies are installed and API keys are configured:

```bash
streamlit run app.py
```

This will start the Streamlit app, which will be accessible in your browser at `http://localhost:8501`.

---

### **Folder Structure**

```
youtube-video-finder/
│
├── Analysis.py        # Main Streamlit app
├── requirements.txt   # List of dependencies
├── README.md          # Project documentation
```

---

### **Usage**

* Open the app in your browser.
* Choose the input method: **Voice** or **Text**.
* If using **Voice**, click the "Record Voice" button and speak your search query.
* If using **Text**, simply type your search query in the text box.
* Click the "Find Best Video" button to display the most relevant video.
* **Gemini AI** analyzes the video titles, and the best match will be shown either embedded in the app or via a clickable link.

---

### **Contributing**

Feel free to fork this project and submit pull requests. Contributions are welcome to improve the functionality, user interface, or performance of the app.

---

### **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### **Acknowledgments**

* **Google YouTube Data API v3** for video search functionality.
* **Gemini AI** for analyzing the video titles.
* **SpeechRecognition** and **pyaudio** for voice input processing.

---

### **Troubleshooting**

If you're encountering issues with voice recognition or dependencies:

* **pyaudio** may have issues installing on Windows. Try using `pipwin` to install it:

```bash
pip install pipwin
pipwin install pyaudio
```

If you encounter any errors during the execution, feel free to open an issue on the GitHub repository.

---

### **Future Improvements**

* Allow users to refine search results (e.g., by views, language, etc.).
* Improve voice recognition support for multiple languages.
* Provide more robust error handling and user feedback.

---

### **GitHub Deployment**

* This project is fully deployable on **Heroku**, **Streamlit sharing**, or **other cloud platforms**.
* For Heroku, you can create a `Procfile` to specify how the app should run:

  ```bash
  web: streamlit run app.py
  ```

---

### **How to Deploy on GitHub Pages (Optional)**

To host this project on GitHub Pages (via static HTML interface), you can create a **GitHub Pages site** for the repository and link it accordingly.

---

#### **Example `.gitignore` File:**

```gitignore
# Python
*.pyc
*.pyo
__pycache__/

# Environment variables
.env

# Streamlit specific
streamlit_config.toml
```

---

