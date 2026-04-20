# 仮名学習 · Kana Study

A beautiful Japanese hiragana & katakana learning app with quiz mode and persistent progress tracking via browser localStorage.

## Features

- **Learn Tab** — Browse all 46+ hiragana and 46+ katakana characters in organized rows, including dakuten (voiced), handakuten (p-sounds), and combination characters
- **Quiz Tab** — Flashcard-style quiz with:
  - Multiple choice mode
  - Type-the-answer mode
  - Filter by script (hiragana / katakana / all / weak chars)
  - Weighted randomization (struggles more = shown more)
- **Progress Tab** — Visual overview of every character with mastery status, accuracy %, and session stats
- **localStorage** — All progress saves directly in the browser; no backend needed
- **Streak tracking** — Daily study streak counter

## Local Development

```bash
pip install streamlit
streamlit run app.py
```

## Deploy to Streamlit Cloud

1. Push this folder to a GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Set **Main file path** to `app.py`
5. Click **Deploy** — that's it!

No secrets or environment variables needed.

## Deploy to Other Platforms

### Railway / Render
```
Start command: streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

### Docker
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]
```

## Characters Covered

| Category | Count |
|----------|-------|
| Basic hiragana (あ〜ん) | 46 |
| Basic katakana (ア〜ン) | 46 |
| Dakuten voiced (が、ざ…) | 40 |
| Handakuten P-sounds | 10 |
| Combination sounds | 66 |
| **Total** | **208** |
