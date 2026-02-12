# 🚀 LinkedIn Post Generator (Few-Shot LLM)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![LangChain](https://img.shields.io/badge/LangChain-Enabled-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

> An intelligent LinkedIn post generator powered by few-shot learning and large language models. Create engaging, professional LinkedIn content tailored to your topic, length, and language preferences.

---

## 📋 Project Overview

The **LinkedIn Post Generator** is an AI-powered application that generates high-quality LinkedIn posts using a few-shot prompting approach. By leveraging real LinkedIn post examples enriched with metadata, the system intelligently selects similar posts and uses them as context to generate new, engaging content through the Llama 3.3 model via Groq API.

This project demonstrates practical applications of:
- **Few-shot learning** for content generation
- **Metadata-driven filtering** for context-aware AI responses
- **Modern LLM orchestration** using LangChain
- **Interactive web interfaces** with Streamlit

---

## ✨ Features

- 🎯 **Topic-Based Generation**: Select from predefined topics to generate relevant content
- 📏 **Customizable Length**: Choose between short, medium, or long post formats
- 🌍 **Multi-Language Support**: Generate posts in different languages
- 🧠 **Few-Shot Learning**: Uses real LinkedIn post examples to guide AI generation
- 🎨 **Interactive UI**: Clean, user-friendly Streamlit interface
- ⚡ **Fast Processing**: Powered by Groq's high-performance API
- 🔍 **Smart Filtering**: Metadata-based example selection for better context

---

## 🧠 How It Works

The application follows a sophisticated pipeline to generate contextually relevant LinkedIn posts:

### 1️⃣ **Data Collection & Enrichment**
- Raw LinkedIn posts are collected and stored
- Each post is enriched with metadata:
  - **Line count**: Determines post length category
  - **Language**: Identifies the language of the post
  - **Tags**: Categorizes posts by topic/theme

### 2️⃣ **Preprocessing & Storage**
- Enriched posts are processed and stored in a structured format
- Metadata enables efficient filtering and retrieval

### 3️⃣ **Runtime Generation**
When a user requests a new post:
1. **Load** processed example posts from storage
2. **Filter** examples by selected topic, length, and language
3. **Select** up to 2 most similar examples
4. **Build** a few-shot prompt with selected examples
5. **Send** prompt to Llama 3.3 via Groq API
6. **Generate** and display the new LinkedIn post

---

## 🏗️ Architecture Overview

```
┌─────────────────┐
│  Raw LinkedIn   │
│     Posts       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Metadata      │
│   Enrichment    │
│  (Line count,   │
│  Language, Tags)│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Processed     │
│   Dataset       │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────┐
│         User Input (UI)             │
│  Topic | Length | Language          │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────┐
│  Filter & Select│
│  Similar Posts  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Few-Shot       │
│  Prompt Builder │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Groq API       │
│  (Llama 3.3)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Generated      │
│  LinkedIn Post  │
└─────────────────┘
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white) | Core programming language |
| ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) | Web UI framework |
| ![LangChain](https://img.shields.io/badge/-LangChain-121212?style=flat) | LLM orchestration & prompt management |
| ![Groq](https://img.shields.io/badge/-Groq-000000?style=flat) | High-performance LLM API |
| **Llama 3.3** | Large language model |
| **Pandas** | Data processing & filtering |

---

## 📂 Project Structure

```
Linkedin_post_generator/
│
├── main.py                # Streamlit entry point
├── llm_helper.py          # LLM API handler
├── post_generator.py      # Post creation logic
├── preprocess.py          # Data preprocessing
├── few_shot.py            # Few-shot prompt templates
├── data/                  # Raw and processed posts
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Groq API account ([Sign up here](https://groq.com))

### Step 1: Clone the Repository
```bash
git clone https://github.com/anujakhatri/linkedin-post-generator.git
cd linkedin-post-generator
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables (API Key Setup)

> ⚠️ **IMPORTANT**: Never commit your API keys to GitHub!

### Step 1: Create `.env` File
Copy the example environment file:
```bash
cp .env.example .env
```

### Step 2: Add Your Groq API Key
Open `.env` and add your API key:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### Step 3: Obtain Groq API Key
1. Visit [Groq Console](https://console.groq.com)
2. Sign up or log in
3. Navigate to API Keys section
4. Generate a new API key
5. Copy and paste it into your `.env` file

> 💡 **Tip**: The `.env` file is already included in `.gitignore` to prevent accidental commits.

---

## ▶️ Running the Application

### Start the Streamlit App
```bash
streamlit run app/main.py
```

The application will open in your default browser at `http://localhost:8501`

### Using the Application
1. **Select a Topic**: Choose from available categories (e.g., Technology, Marketing, Career)
2. **Choose Length**: Pick short, medium, or long format
3. **Select Language**: Choose your preferred language
4. **Generate**: Click the generate button
5. **Review**: View your AI-generated LinkedIn post
6. **Copy & Post**: Copy the content to LinkedIn

---

## 📸 Example Use Case

### Input
- **Topic**: Artificial Intelligence
- **Length**: Medium
- **Language**: English

### Output
```
The key? Building systems that are:
✅ Transparent
✅ Accountable
✅ Human-centered

#ArtificialIntelligence #TechInnovation #FutureOfWork
```

---

## 📈 Future Improvements

- [ ] **User Authentication**: Allow users to save favorite posts
- [ ] **Custom Training**: Enable users to upload their own post examples
- [ ] **Multi-Model Support**: Add support for GPT-4, Claude, and other LLMs
- [ ] **Analytics Dashboard**: Track generation metrics and popular topics
- [ ] **Tone Customization**: Add options for professional, casual, or inspirational tones
- [ ] **Hashtag Suggestions**: Auto-generate relevant hashtags
- [ ] **Export Options**: Download posts as PDF or share directly to LinkedIn
- [ ] **A/B Testing**: Compare multiple generated versions

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

Please ensure your code follows the existing style and includes appropriate tests.

---


## 🙏 Acknowledgments

- **Groq** for providing high-performance LLM API
- **LangChain** for excellent LLM orchestration tools
- **Streamlit** for the intuitive web framework
- **Meta AI** for the Llama 3.3 model

---


---

<div align="center">
  
**⭐ Star this repo if you find it helpful!**

Made with ❤️ by Anuja Khatri

</div>
