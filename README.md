**LinkedIn Post Generator**

Generate engaging LinkedIn posts using a few-shot LLM prompt, with a simple web UI for choosing topic, length, and language.

## Description

This project helps you quickly create LinkedIn posts based on real example posts and an LLM (Groq + Llama 3.3).  
Raw LinkedIn posts are first enriched with metadata (line count, language, tags) and stored in a processed dataset.  
At runtime, the app:

- Loads processed example posts.
- Filters them by your chosen topic, length, and language.
- Builds a prompt with up to two similar examples.
- Sends the prompt to an LLM to generate a new post.

The current UI is implemented in Python using Streamlit, and the LLM integration uses LangChain with Groq.

## Features / Key Functionalities

- **Interactive web UI (Streamlit)**
  - Dropdowns for:
    - **Topic**: choose from tags extracted from your dataset.
    - **Length**: `Short`, `Medium`, or `Long`.
    - **Language**: `English` or `Neplish` (mix of Nepali + English, but always written in Latin script).
  - One-click **Generate** button to produce a new LinkedIn post.

- **LLM-powered post generation**
  - Uses **Groq** (`llama-3.3-70b-versatile` via `langchain_groq.ChatGroq`).
  - Builds a structured prompt with clear instructions and a few example posts.
  - Returns only the generated post text (no preamble).

- **Few-shot example selection**
  - `FewShotPosts` class (in `few_shot.py`) loads `data/processed_posts.json`.
  - Normalizes JSON into a Pandas DataFrame.
  - Categorizes post length into `Short`, `Medium`, and `Long`.
  - Filters examples by:
    - Selected **tag** (topic).
    - Selected **language**.
    - Selected **length**.

- **Data preprocessing pipeline**
  - `preprocess.py` reads `data/raw_posts.json` and:
    - Sanitizes Unicode artifacts.
    - Uses an LLM to extract:
      - `line_count`
      - `language`
      - `tags` (up to 2 per post)
    - Unifies similar tags (e.g., `"Jobseekers"` and `"Job Hunting"` → `"Job Search"`).
    - Writes enriched posts to `data/processed_posts.json`.

- **Environment-based configuration**
  - Uses `.env.save` for storing `GROQ_API_KEY`.
  - All LLM calls go through `llm_helper.py`, making it easier to swap models/providers later.

## Installation Instructions

### 1. Prerequisites

- **Python**: 3.10+ (3.12 is used in the current virtual environment).
- **pip** or another Python package manager.
- **Groq account & API key** for `GROQ_API_KEY`.

> Note: The repository includes a `.venv` directory, but you can create your own virtual environment instead of using the committed one.

### 2. Clone the repository

```bash
git clone <repo-url>
cd "Linkedin post generator"
```

### 3. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 4. Install Python dependencies

Install packages roughly matching what the code imports:

```bash
pip install streamlit pandas python-dotenv langchain-core langchain-groq
```

You may also need:

```bash
pip install watchdog
```

if you run into file-watching related issues.

### 5. Configure environment variables

Create a `.env.save` file in the project root:

```bash
echo "GROQ_API_KEY=your_groq_api_key_here" > .env.save
```

Replace `your_groq_api_key_here` with your actual Groq API key.

### 6. Prepare the processed dataset

If `data/processed_posts.json` is not already present or you want to regenerate it:

```bash
python preprocess.py
```

This will:

- Read **raw posts** from `data/raw_posts.json`.
- Ask the LLM to extract metadata.
- Normalize tags and write the result to `data/processed_posts.json`.

## Usage Examples

### 1. Run the web app (recommended)

From the project root (with your virtual environment activated):

```bash
streamlit run main.py
```

Then:

1. Open the URL Streamlit prints in your terminal (usually `http://localhost:8501`).
2. Choose:
   - **Topic** (tag) from the dropdown.
   - **Length**: `Short`, `Medium`, or `Long`.
   - **Language**: `English` or `Neplish`.
3. Click **Generate**.
4. A generated LinkedIn post will appear below the button.

### 2. Use the generator directly from Python

You can also call the generator in your own scripts or notebooks:

```python
from post_generator import generate_post

post = generate_post(length="Medium", language="English", tag="Job Search")
print(post)
```

Make sure your environment is set up (virtualenv active, `GROQ_API_KEY` configured, and `data/processed_posts.json` generated).

### 3. Regenerate the processed dataset

If you update `data/raw_posts.json` with new posts, rerun:

```bash
python preprocess.py
```

This will refresh `data/processed_posts.json` with updated metadata and unified tags.

## Technologies / Tech Stack

### Current implementation (this folder)

- **Language**: Python
- **UI**: Streamlit
- **LLM Orchestration**: LangChain (`langchain-core`, `langchain_groq`)
- **Model Provider**: Groq (`llama-3.3-70b-versatile`)
- **Data Processing**: Pandas + JSON files (`data/raw_posts.json`, `data/processed_posts.json`)
- **Environment Management**: `python-dotenv` with `.env.save`

### Target full-stack architecture (as described)

The intended broader architecture for this project includes:

- **Frontend**: React.js
- **Backend**: FastAPI
- **Database**: PostgreSQL
- **Styling**: TailwindCSS
- **Containerization**: Docker

> The current repository primarily contains the Python/Streamlit prototype and data-processing pipeline.  
> React, FastAPI, PostgreSQL, TailwindCSS, and Docker support can be added around this core to provide a full production-ready system.

## API Endpoints / Integration Notes

### Current state (this folder)

- There is **no separate FastAPI service or public HTTP API** defined in this codebase yet.
- All functionality is accessed through:
  - The **Streamlit UI** (`main.py`).
  - Direct Python function calls (e.g., `generate_post` in `post_generator.py`, `FewShotPosts` in `few_shot.py`).

### Suggested future FastAPI design (high level)

If you later wrap this logic in a FastAPI backend, typical endpoints might include:

- `POST /api/posts/generate`
  - **Body**: `{ "length": "Short|Medium|Long", "language": "English|Neplish", "tag": "TopicName" }`
  - **Response**: `{ "post": "Generated LinkedIn post text" }`

- `GET /api/tags`
  - Returns the list of available tags (using `FewShotPosts.get_tags()`).

These endpoints would internally reuse the same functions and classes already present in `post_generator.py` and `few_shot.py`.

## Contribution Guidelines

- **Discuss major changes first**
  - If you plan to add a React frontend, FastAPI backend, or Docker setup, consider opening an issue to describe your design.

- **Set up your environment**
  - Use a virtual environment (`.venv`) and install dependencies as described above.
  - Ensure `preprocess.py` and `main.py` run without errors before submitting changes.

- **Code style & structure**
  - Keep functions small and focused.
  - Prefer reusing existing helpers (`FewShotPosts`, `generate_post`, `llm_helper.llm`) instead of duplicating logic.
  - Add docstrings or inline comments for non-obvious logic, especially around prompt construction and tag unification.

- **Testing**
  - Manually test:
    - Data preprocessing (`python preprocess.py`).
    - Web app interactions (`streamlit run main.py`).
  - If you introduce FastAPI or React, add basic tests or at least manual test steps to the README.

- **Pull Requests**
  - Keep PRs small and focused on a single change or feature.
  - Describe:
    - What you changed.
    - How to test it.
    - Any new environment variables or setup steps.

## License

No explicit license file is currently included in this repository.  
Until a license is added (e.g., `LICENSE` with MIT, Apache 2.0, etc.)


