import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="日本語 · Kana Study",
    page_icon="🗾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit chrome
st.markdown("""
<style>
    #MainMenu, header, footer { visibility: hidden; }
    .block-container { padding: 0 !important; margin: 0 !important; max-width: 100% !important; }
    .stApp { background: #0d0d14; }
</style>
""", unsafe_allow_html=True)

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Kana Study</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@300;400;700&family=Noto+Sans+JP:wght@300;400;500&family=Crimson+Pro:ital,wght@0,300;0,400;0,600;1,300&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0d0d14;
    --surface: #14141f;
    --surface2: #1c1c2e;
    --border: #2a2a42;
    --gold: #c9a84c;
    --gold-dim: #8a6f2e;
    --red: #d94f4f;
    --green: #4fa876;
    --blue: #4f7dd9;
    --text: #e8e0d0;
    --text-dim: #8a8070;
    --text-muted: #4a4438;
    --accent: #7b5cf0;
    --accent-dim: #4a3a8a;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Noto Sans JP', sans-serif;
    min-height: 100vh;
    overflow-x: hidden;
  }

  /* Ink wash background texture */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background:
      radial-gradient(ellipse at 20% 10%, rgba(123,92,240,0.06) 0%, transparent 50%),
      radial-gradient(ellipse at 80% 90%, rgba(201,168,76,0.05) 0%, transparent 50%),
      radial-gradient(ellipse at 50% 50%, rgba(13,13,20,0) 0%, rgba(13,13,20,0.8) 100%);
    pointer-events: none;
    z-index: 0;
  }

  .app { position: relative; z-index: 1; max-width: 1200px; margin: 0 auto; padding: 0 24px 60px; }

  /* Header */
  .header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 28px 0 20px;
    border-bottom: 1px solid var(--border);
    margin-bottom: 32px;
  }
  .logo {
    display: flex;
    flex-direction: column;
    gap: 2px;
  }
  .logo-jp {
    font-family: 'Noto Serif JP', serif;
    font-size: 28px;
    font-weight: 700;
    color: var(--gold);
    letter-spacing: 6px;
    line-height: 1;
  }
  .logo-en {
    font-family: 'Crimson Pro', serif;
    font-size: 12px;
    letter-spacing: 4px;
    color: var(--text-dim);
    text-transform: uppercase;
  }
  .streak-badge {
    display: flex;
    align-items: center;
    gap: 8px;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 8px 16px;
    font-size: 13px;
    color: var(--text-dim);
  }
  .streak-badge .streak-num {
    font-family: 'Crimson Pro', serif;
    font-size: 22px;
    color: var(--gold);
    font-weight: 600;
  }

  /* Nav tabs */
  .nav {
    display: flex;
    gap: 4px;
    margin-bottom: 32px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 4px;
  }
  .nav-btn {
    flex: 1;
    padding: 10px 16px;
    background: none;
    border: none;
    border-radius: 8px;
    color: var(--text-dim);
    cursor: pointer;
    font-family: 'Noto Sans JP', sans-serif;
    font-size: 13px;
    letter-spacing: 1px;
    transition: all 0.2s;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
  }
  .nav-btn:hover { color: var(--text); background: var(--surface2); }
  .nav-btn.active { background: var(--accent-dim); color: #c4b5fd; border: 1px solid var(--accent); }
  .nav-btn .jp { font-family: 'Noto Serif JP', serif; font-size: 15px; }

  /* Section header */
  .section-header {
    display: flex;
    align-items: baseline;
    gap: 16px;
    margin-bottom: 20px;
  }
  .section-title {
    font-family: 'Crimson Pro', serif;
    font-size: 22px;
    font-weight: 300;
    color: var(--text);
    letter-spacing: 2px;
  }
  .section-sub {
    font-family: 'Noto Serif JP', serif;
    font-size: 14px;
    color: var(--gold);
    letter-spacing: 3px;
  }

  /* Character Grid */
  .row-label {
    font-family: 'Crimson Pro', serif;
    font-size: 11px;
    letter-spacing: 3px;
    color: var(--text-muted);
    text-transform: uppercase;
    margin: 20px 0 8px;
  }
  .char-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 4px;
  }
  .char-card {
    width: 80px;
    height: 88px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 4px;
    cursor: pointer;
    transition: all 0.18s;
    position: relative;
    overflow: hidden;
  }
  .char-card::after {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 10px;
    opacity: 0;
    transition: opacity 0.2s;
    background: linear-gradient(135deg, rgba(201,168,76,0.08), transparent);
  }
  .char-card:hover { border-color: var(--gold-dim); transform: translateY(-2px); }
  .char-card:hover::after { opacity: 1; }
  .char-card.mastered { border-color: var(--green); background: rgba(79,168,118,0.08); }
  .char-card.learning { border-color: var(--gold-dim); }
  .char-card.struggling { border-color: var(--red); background: rgba(217,79,79,0.06); }

  .char-glyph {
    font-family: 'Noto Serif JP', serif;
    font-size: 28px;
    font-weight: 400;
    color: var(--text);
    line-height: 1;
  }
  .char-romaji {
    font-family: 'Crimson Pro', serif;
    font-size: 12px;
    letter-spacing: 1px;
    color: var(--text-dim);
  }
  .char-progress-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--border);
    position: absolute;
    top: 6px;
    right: 6px;
  }
  .char-card.mastered .char-progress-dot { background: var(--green); }
  .char-card.learning .char-progress-dot { background: var(--gold); }
  .char-card.struggling .char-progress-dot { background: var(--red); }

  /* Quiz section */
  .quiz-container {
    max-width: 600px;
    margin: 0 auto;
  }
  .quiz-mode-toggle {
    display: flex;
    gap: 8px;
    margin-bottom: 28px;
  }
  .mode-btn {
    flex: 1;
    padding: 10px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    color: var(--text-dim);
    cursor: pointer;
    font-family: 'Noto Sans JP', sans-serif;
    font-size: 12px;
    letter-spacing: 1px;
    transition: all 0.2s;
  }
  .mode-btn.active { background: var(--accent-dim); border-color: var(--accent); color: #c4b5fd; }

  .quiz-set-select {
    display: flex;
    gap: 8px;
    margin-bottom: 24px;
    flex-wrap: wrap;
  }
  .set-btn {
    padding: 6px 14px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 20px;
    color: var(--text-dim);
    cursor: pointer;
    font-size: 12px;
    letter-spacing: 1px;
    transition: all 0.2s;
  }
  .set-btn.active { border-color: var(--gold); color: var(--gold); background: rgba(201,168,76,0.08); }

  /* Row picker */
  .row-picker {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    margin-bottom: 20px;
    overflow: hidden;
    transition: all 0.2s;
  }
  .row-picker-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 14px;
    cursor: pointer;
    user-select: none;
    border-bottom: 1px solid transparent;
    transition: border-color 0.2s;
  }
  .row-picker-header:hover { background: var(--surface2); }
  .row-picker.open .row-picker-header { border-bottom-color: var(--border); }
  .row-picker-label {
    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--text-dim);
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .row-picker-count {
    background: var(--accent-dim);
    color: #c4b5fd;
    border-radius: 10px;
    padding: 2px 8px;
    font-size: 10px;
    letter-spacing: 1px;
    border: 1px solid var(--accent);
  }
  .row-picker-actions {
    display: flex;
    gap: 6px;
    align-items: center;
  }
  .rp-action-btn {
    padding: 3px 10px;
    background: transparent;
    border: 1px solid var(--border);
    border-radius: 8px;
    color: var(--text-muted);
    cursor: pointer;
    font-size: 10px;
    letter-spacing: 1px;
    transition: all 0.15s;
  }
  .rp-action-btn:hover { border-color: var(--text-dim); color: var(--text-dim); }
  .chevron {
    color: var(--text-muted);
    font-size: 10px;
    transition: transform 0.2s;
  }
  .row-picker.open .chevron { transform: rotate(180deg); }
  .row-picker-body {
    display: none;
    padding: 12px 14px;
    flex-wrap: wrap;
    gap: 7px;
  }
  .row-picker.open .row-picker-body { display: flex; }
  .row-chip {
    padding: 5px 12px;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 16px;
    color: var(--text-dim);
    cursor: pointer;
    font-size: 12px;
    letter-spacing: 0.5px;
    transition: all 0.15s;
    white-space: nowrap;
    display: flex;
    align-items: center;
    gap: 5px;
  }
  .row-chip:hover { border-color: var(--text-dim); color: var(--text); }
  .row-chip.selected { border-color: var(--gold); color: var(--gold); background: rgba(201,168,76,0.1); }
  .row-chip .chip-count { font-size: 10px; color: inherit; opacity: 0.6; }

  .quiz-progress-bar {
    height: 3px;
    background: var(--border);
    border-radius: 2px;
    margin-bottom: 32px;
    overflow: hidden;
  }
  .quiz-progress-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--accent), var(--gold));
    border-radius: 2px;
    transition: width 0.4s ease;
  }

  .flashcard {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 48px;
    text-align: center;
    margin-bottom: 28px;
    position: relative;
    min-height: 200px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 8px;
    transition: all 0.3s;
  }
  .flashcard::before {
    content: '';
    position: absolute;
    inset: -1px;
    border-radius: 20px;
    background: linear-gradient(135deg, rgba(123,92,240,0.2), transparent, rgba(201,168,76,0.1));
    opacity: 0;
    transition: opacity 0.3s;
    pointer-events: none;
  }
  .flashcard.correct::before { opacity: 1; background: linear-gradient(135deg, rgba(79,168,118,0.3), transparent); }
  .flashcard.incorrect::before { opacity: 1; background: linear-gradient(135deg, rgba(217,79,79,0.3), transparent); }

  .card-char {
    font-family: 'Noto Serif JP', serif;
    font-size: 96px;
    font-weight: 300;
    color: var(--text);
    line-height: 1;
    text-shadow: 0 0 40px rgba(201,168,76,0.2);
  }
  .card-hint {
    font-family: 'Crimson Pro', serif;
    font-size: 13px;
    letter-spacing: 3px;
    color: var(--text-muted);
    text-transform: uppercase;
  }
  .card-feedback {
    font-family: 'Crimson Pro', serif;
    font-size: 18px;
    color: var(--green);
    letter-spacing: 2px;
    margin-top: 8px;
    opacity: 0;
    transition: opacity 0.3s;
  }
  .flashcard.correct .card-feedback { opacity: 1; color: var(--green); }
  .flashcard.incorrect .card-feedback { opacity: 1; color: var(--red); }

  /* Multiple choice */
  .choices-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-bottom: 20px;
  }
  .choice-btn {
    padding: 16px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    color: var(--text);
    cursor: pointer;
    font-family: 'Crimson Pro', serif;
    font-size: 18px;
    letter-spacing: 2px;
    transition: all 0.15s;
    text-align: center;
  }
  .choice-btn:hover:not(:disabled) { border-color: var(--accent); background: var(--accent-dim); }
  .choice-btn.correct { border-color: var(--green) !important; background: rgba(79,168,118,0.15) !important; color: var(--green); }
  .choice-btn.incorrect { border-color: var(--red) !important; background: rgba(217,79,79,0.12) !important; color: var(--red); }
  .choice-btn:disabled { cursor: default; }

  /* Type input */
  .type-input-wrap {
    display: flex;
    gap: 8px;
    margin-bottom: 20px;
  }
  .type-input {
    flex: 1;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 14px 20px;
    color: var(--text);
    font-family: 'Crimson Pro', serif;
    font-size: 18px;
    letter-spacing: 2px;
    outline: none;
    transition: border-color 0.2s;
  }
  .type-input:focus { border-color: var(--accent); }
  .type-input.correct { border-color: var(--green); }
  .type-input.incorrect { border-color: var(--red); }
  .submit-btn {
    padding: 14px 24px;
    background: var(--accent-dim);
    border: 1px solid var(--accent);
    border-radius: 12px;
    color: #c4b5fd;
    cursor: pointer;
    font-size: 13px;
    letter-spacing: 1px;
    transition: all 0.2s;
  }
  .submit-btn:hover { background: var(--accent); color: white; }

  .next-btn {
    width: 100%;
    padding: 14px;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 12px;
    color: var(--text-dim);
    cursor: pointer;
    font-family: 'Noto Sans JP', sans-serif;
    font-size: 13px;
    letter-spacing: 2px;
    transition: all 0.2s;
    margin-bottom: 20px;
  }
  .next-btn:hover { border-color: var(--text-dim); color: var(--text); }

  /* Stats row */
  .stats-row {
    display: flex;
    gap: 10px;
    justify-content: center;
    margin-bottom: 8px;
  }
  .stat-pill {
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 12px;
    letter-spacing: 1px;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .stat-pill.correct { background: rgba(79,168,118,0.1); border: 1px solid rgba(79,168,118,0.3); color: var(--green); }
  .stat-pill.incorrect { background: rgba(217,79,79,0.1); border: 1px solid rgba(217,79,79,0.3); color: var(--red); }
  .stat-pill.total { background: var(--surface2); border: 1px solid var(--border); color: var(--text-dim); }

  /* Progress page */
  .progress-overview {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
    margin-bottom: 32px;
  }
  .overview-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 24px;
    text-align: center;
  }
  .overview-num {
    font-family: 'Crimson Pro', serif;
    font-size: 48px;
    font-weight: 300;
    line-height: 1;
    margin-bottom: 4px;
  }
  .overview-label {
    font-size: 11px;
    letter-spacing: 3px;
    color: var(--text-dim);
    text-transform: uppercase;
  }
  .overview-card.mastered .overview-num { color: var(--green); }
  .overview-card.learning .overview-num { color: var(--gold); }
  .overview-card.new .overview-num { color: var(--text-dim); }
  .overview-card.accuracy .overview-num { color: var(--accent); }

  .progress-char-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-bottom: 24px;
  }
  .prog-char {
    width: 64px;
    height: 72px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 2px;
    position: relative;
    overflow: hidden;
  }
  .prog-char::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: var(--border);
  }
  .prog-char.mastered::after { background: var(--green); }
  .prog-char.learning::after { background: var(--gold); }
  .prog-char.struggling::after { background: var(--red); }
  .prog-glyph {
    font-family: 'Noto Serif JP', serif;
    font-size: 22px;
    color: var(--text);
  }
  .prog-romaji {
    font-family: 'Crimson Pro', serif;
    font-size: 10px;
    color: var(--text-muted);
    letter-spacing: 0.5px;
  }
  .prog-score {
    font-size: 9px;
    color: var(--text-muted);
    font-family: 'Crimson Pro', serif;
  }

  .reset-btn {
    padding: 10px 20px;
    background: transparent;
    border: 1px solid rgba(217,79,79,0.3);
    border-radius: 8px;
    color: var(--red);
    cursor: pointer;
    font-size: 11px;
    letter-spacing: 2px;
    transition: all 0.2s;
    margin-top: 16px;
  }
  .reset-btn:hover { background: rgba(217,79,79,0.1); border-color: var(--red); }

  .legend {
    display: flex;
    gap: 20px;
    margin-bottom: 16px;
    flex-wrap: wrap;
  }
  .legend-item {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 11px;
    letter-spacing: 1px;
    color: var(--text-dim);
  }
  .legend-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
  }
  .legend-dot.mastered { background: var(--green); }
  .legend-dot.learning { background: var(--gold); }
  .legend-dot.struggling { background: var(--red); }
  .legend-dot.new { background: var(--border); }

  /* Tabs for hiragana/katakana in learn */
  .script-toggle {
    display: flex;
    gap: 8px;
    margin-bottom: 24px;
  }
  .script-btn {
    padding: 8px 20px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    color: var(--text-dim);
    cursor: pointer;
    font-family: 'Noto Serif JP', serif;
    font-size: 14px;
    letter-spacing: 2px;
    transition: all 0.2s;
  }
  .script-btn.active { border-color: var(--gold); color: var(--gold); background: rgba(201,168,76,0.08); }

  .hidden { display: none !important; }

  /* Tip tooltip on hover */
  .char-card-wrap {
    position: relative;
  }

  @keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: none; } }
  .page { animation: fadeIn 0.25s ease; }

  @keyframes pop { 0% { transform: scale(1); } 50% { transform: scale(1.05); } 100% { transform: scale(1); } }
  .flashcard.pop { animation: pop 0.3s ease; }

  /* ====== STROKE ORDER MODAL ====== */
  .stroke-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.75);
    backdrop-filter: blur(6px);
    z-index: 1000;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.25s;
  }
  .stroke-overlay.open { opacity: 1; pointer-events: all; }

  .stroke-modal {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 24px;
    width: min(520px, 92vw);
    max-height: 88vh;
    overflow-y: auto;
    padding: 32px;
    position: relative;
    transform: translateY(16px);
    transition: transform 0.25s;
  }
  .stroke-overlay.open .stroke-modal { transform: none; }

  .stroke-close {
    position: absolute;
    top: 16px; right: 20px;
    background: none;
    border: none;
    color: var(--text-muted);
    font-size: 22px;
    cursor: pointer;
    line-height: 1;
    transition: color 0.15s;
  }
  .stroke-close:hover { color: var(--text); }

  .stroke-header {
    text-align: center;
    margin-bottom: 24px;
  }
  .stroke-glyph {
    font-family: 'Noto Serif JP', serif;
    font-size: 56px;
    color: var(--text);
    line-height: 1;
  }
  .stroke-romaji {
    font-family: 'Crimson Pro', serif;
    font-size: 20px;
    letter-spacing: 3px;
    color: var(--gold);
    margin-top: 4px;
  }
  .stroke-script-label {
    font-size: 10px;
    letter-spacing: 3px;
    color: var(--text-muted);
    text-transform: uppercase;
    margin-top: 2px;
  }

  /* SVG display area */
  .stroke-components {
    display: flex;
    gap: 16px;
    justify-content: center;
    flex-wrap: wrap;
    margin-bottom: 24px;
  }
  .stroke-component {
    flex: 1;
    min-width: 140px;
    max-width: 220px;
  }
  .stroke-component-label {
    font-family: 'Noto Serif JP', serif;
    font-size: 18px;
    text-align: center;
    color: var(--text-dim);
    margin-bottom: 6px;
  }
  .stroke-svg-wrap {
    background: #f8f4ee;
    border-radius: 14px;
    padding: 12px;
    aspect-ratio: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
  }
  .stroke-svg-wrap svg {
    width: 100%;
    height: 100%;
  }
  /* Grid guide lines */
  .stroke-svg-wrap::before {
    content: '';
    position: absolute;
    inset: 0;
    background:
      linear-gradient(#c8bfb0 1px, transparent 1px),
      linear-gradient(90deg, #c8bfb0 1px, transparent 1px),
      linear-gradient(rgba(200,191,176,0.4) 1px, transparent 1px),
      linear-gradient(90deg, rgba(200,191,176,0.4) 1px, transparent 1px);
    background-size: 50% 50%, 50% 50%, 25% 25%, 25% 25%;
    pointer-events: none;
    border-radius: 14px;
  }
  .stroke-loading {
    font-family: 'Crimson Pro', serif;
    font-size: 13px;
    letter-spacing: 2px;
    color: #8a7060;
    text-align: center;
    padding: 20px;
  }
  .stroke-error {
    font-family: 'Crimson Pro', serif;
    font-size: 12px;
    color: #b08070;
    text-align: center;
    padding: 16px;
  }

  /* Stroke number bubbles */
  .stroke-nums-row {
    display: flex;
    gap: 6px;
    justify-content: center;
    flex-wrap: wrap;
    margin-top: 8px;
  }
  .stroke-num-bubble {
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background: var(--border);
    color: var(--text-muted);
    font-family: 'Crimson Pro', serif;
    font-size: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s;
  }
  .stroke-num-bubble.active { background: var(--gold); color: #0d0d14; font-weight: 600; }
  .stroke-num-bubble.done { background: var(--accent-dim); color: #c4b5fd; }

  /* Controls */
  .stroke-controls {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    margin-top: 20px;
    flex-wrap: wrap;
  }
  .stroke-play-btn {
    padding: 10px 28px;
    background: var(--accent-dim);
    border: 1px solid var(--accent);
    border-radius: 12px;
    color: #c4b5fd;
    cursor: pointer;
    font-family: 'Noto Sans JP', sans-serif;
    font-size: 13px;
    letter-spacing: 1px;
    transition: all 0.2s;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .stroke-play-btn:hover { background: var(--accent); color: white; }
  .stroke-speed-group {
    display: flex;
    gap: 4px;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 3px;
  }
  .speed-btn {
    padding: 5px 12px;
    background: none;
    border: none;
    border-radius: 7px;
    color: var(--text-muted);
    cursor: pointer;
    font-size: 11px;
    letter-spacing: 1px;
    transition: all 0.15s;
  }
  .speed-btn.active { background: var(--surface); color: var(--text); }

  .stroke-count-label {
    font-family: 'Crimson Pro', serif;
    font-size: 12px;
    color: var(--text-muted);
    letter-spacing: 2px;
    text-align: center;
    margin-top: 6px;
  }

  /* Stroke button on quiz */
  .stroke-hint-btn {
    width: 100%;
    padding: 10px;
    background: transparent;
    border: 1px solid var(--border);
    border-radius: 10px;
    color: var(--text-muted);
    cursor: pointer;
    font-family: 'Noto Sans JP', sans-serif;
    font-size: 11px;
    letter-spacing: 2px;
    transition: all 0.2s;
    margin-bottom: 12px;
    display: none;
  }
  .stroke-hint-btn:hover { border-color: var(--gold-dim); color: var(--gold); }
</style>
</head>
<body>
<div class="app">

  <!-- Header -->
  <div class="header">
    <div class="logo">
      <div class="logo-jp">仮名学習</div>
      <div class="logo-en">Kana Study · Japanese Script</div>
    </div>
    <div class="streak-badge">
      🔥 <span class="streak-num" id="streakNum">0</span> day streak
    </div>
  </div>

  <!-- Nav -->
  <div class="nav">
    <button class="nav-btn active" onclick="showPage('learn')" id="nav-learn">
      <span class="jp">学</span> Learn
    </button>
    <button class="nav-btn" onclick="showPage('quiz')" id="nav-quiz">
      <span class="jp">問</span> Quiz
    </button>
    <button class="nav-btn" onclick="showPage('progress')" id="nav-progress">
      <span class="jp">進</span> Progress
    </button>
  </div>

  <!-- LEARN PAGE -->
  <div id="page-learn" class="page">
    <div class="section-header">
      <span class="section-title">Character Reference</span>
      <span class="section-sub">五十音</span>
    </div>

    <div class="script-toggle">
      <button class="script-btn active" onclick="switchScript('hiragana')" id="sbtn-hiragana">ひらがな Hiragana</button>
      <button class="script-btn" onclick="switchScript('katakana')" id="sbtn-katakana">カタカナ Katakana</button>
    </div>

    <div id="learn-grid"></div>
  </div>

  <!-- QUIZ PAGE -->
  <div id="page-quiz" class="page hidden">
    <div class="quiz-container">
      <div class="section-header">
        <span class="section-title">Character Quiz</span>
        <span class="section-sub">問題</span>
      </div>

      <div class="quiz-mode-toggle">
        <button class="mode-btn active" onclick="setQuizMode('mc')" id="mode-mc">Multiple Choice</button>
        <button class="mode-btn" onclick="setQuizMode('type')" id="mode-type">Type Answer</button>
      </div>

      <div class="quiz-set-select">
        <button class="set-btn active" onclick="setQuizSet('both')" id="qset-both">All</button>
        <button class="set-btn" onclick="setQuizSet('hiragana')" id="qset-hiragana">ひらがな</button>
        <button class="set-btn" onclick="setQuizSet('katakana')" id="qset-katakana">カタカナ</button>
        <button class="set-btn" onclick="setQuizSet('weak')" id="qset-weak">Weak</button>
      </div>

      <!-- Row picker -->
      <div class="row-picker" id="rowPicker">
        <div class="row-picker-header" onclick="toggleRowPicker()">
          <div class="row-picker-label">
            Rows
            <span class="row-picker-count" id="rowPickerCount">all</span>
          </div>
          <div class="row-picker-actions">
            <button class="rp-action-btn" onclick="event.stopPropagation(); selectAllRows()">All</button>
            <button class="rp-action-btn" onclick="event.stopPropagation(); clearAllRows()">None</button>
            <span class="chevron">▼</span>
          </div>
        </div>
        <div class="row-picker-body" id="rowPickerBody"></div>
      </div>

      <div class="quiz-progress-bar">
        <div class="quiz-progress-fill" id="quizProgressFill" style="width:0%"></div>
      </div>

      <div class="flashcard" id="flashcard">
        <div class="card-char" id="cardChar">あ</div>
        <div class="card-hint" id="cardHint">What is the romaji?</div>
        <div class="card-feedback" id="cardFeedback"></div>
      </div>

      <div id="mc-area">
        <div class="choices-grid" id="choicesGrid"></div>
      </div>

      <div id="type-area" class="hidden">
        <div class="type-input-wrap">
          <input class="type-input" id="typeInput" placeholder="Type romaji..." autocomplete="off" autocorrect="off" spellcheck="false" />
          <button class="submit-btn" onclick="submitType()">Check</button>
        </div>
      </div>

      <button class="next-btn" id="nextBtn" onclick="nextQuestion()" style="display:none">Next →</button>

      <button class="stroke-hint-btn" id="strokeHintBtn" onclick="openStrokeModal(currentChar.g, currentChar.r, currentChar.script)">
        ✍ Show stroke order
      </button>

      <div class="stats-row">
        <div class="stat-pill correct">✓ <span id="qCorrect">0</span></div>
        <div class="stat-pill incorrect">✗ <span id="qIncorrect">0</span></div>
        <div class="stat-pill total">Session: <span id="qTotal">0</span></div>
      </div>
    </div>
  </div>

  <!-- PROGRESS PAGE -->
  <div id="page-progress" class="page hidden">
    <div class="section-header">
      <span class="section-title">Your Progress</span>
      <span class="section-sub">進捗</span>
    </div>

    <div class="progress-overview" id="progressOverview"></div>

    <div class="legend">
      <div class="legend-item"><div class="legend-dot mastered"></div> Mastered (≥80% acc, ≥5 tries)</div>
      <div class="legend-item"><div class="legend-dot learning"></div> Learning</div>
      <div class="legend-item"><div class="legend-dot struggling"></div> Struggling (&lt;40% acc)</div>
      <div class="legend-item"><div class="legend-dot new"></div> Not seen</div>
    </div>

    <div class="section-header" style="margin-top: 8px;">
      <span class="section-title" style="font-size:16px;">Hiragana</span>
    </div>
    <div class="progress-char-grid" id="prog-hiragana"></div>

    <div class="section-header" style="margin-top: 16px;">
      <span class="section-title" style="font-size:16px;">Katakana</span>
    </div>
    <div class="progress-char-grid" id="prog-katakana"></div>

    <button class="reset-btn" onclick="resetProgress()">Reset All Progress</button>
  </div>

</div>

<!-- Stroke Order Modal -->
<div class="stroke-overlay" id="strokeOverlay" onclick="closeStrokeModal(event)">
  <div class="stroke-modal">
    <button class="stroke-close" onclick="closeStrokeModalDirect()">✕</button>
    <div class="stroke-header">
      <div class="stroke-glyph" id="modalGlyph"></div>
      <div class="stroke-romaji" id="modalRomaji"></div>
      <div class="stroke-script-label" id="modalScript"></div>
    </div>
    <div class="stroke-components" id="strokeComponents"></div>
    <div class="stroke-controls">
      <button class="stroke-play-btn" id="strokePlayBtn" onclick="replayAll()">▶ Replay</button>
      <div class="stroke-speed-group">
        <button class="speed-btn" onclick="setSpeed(0.5)" id="spd-slow">slow</button>
        <button class="speed-btn active" onclick="setSpeed(1)" id="spd-normal">normal</button>
        <button class="speed-btn" onclick="setSpeed(2)" id="spd-fast">fast</button>
      </div>
    </div>
  </div>
</div>

<!-- Footer -->
<footer style="
  position: relative;
  z-index: 1;
  text-align: center;
  padding: 32px 24px 40px;
  border-top: 1px solid #2a2a42;
  margin-top: 40px;
">
  <div style="
    font-family: 'Noto Serif JP', serif;
    font-size: 13px;
    letter-spacing: 3px;
    color: #4a4438;
    margin-bottom: 6px;
  ">作成者</div>
  <div style="
    font-family: 'Crimson Pro', serif;
    font-size: 18px;
    font-weight: 300;
    letter-spacing: 4px;
    color: #8a8070;
  ">Created by <span style="color: #c9a84c; font-weight: 400;">Vishnuvardhan Raj</span></div>
</footer>

<script>
// ===================== DATA =====================
const HIRAGANA = [
  { rows: 'Vowels', chars: [
    {g:'あ',r:'a'},{g:'い',r:'i'},{g:'う',r:'u'},{g:'え',r:'e'},{g:'お',r:'o'}
  ]},
  { rows: 'K-row', chars: [
    {g:'か',r:'ka'},{g:'き',r:'ki'},{g:'く',r:'ku'},{g:'け',r:'ke'},{g:'こ',r:'ko'}
  ]},
  { rows: 'S-row', chars: [
    {g:'さ',r:'sa'},{g:'し',r:'shi'},{g:'す',r:'su'},{g:'せ',r:'se'},{g:'そ',r:'so'}
  ]},
  { rows: 'T-row', chars: [
    {g:'た',r:'ta'},{g:'ち',r:'chi'},{g:'つ',r:'tsu'},{g:'て',r:'te'},{g:'と',r:'to'}
  ]},
  { rows: 'N-row', chars: [
    {g:'な',r:'na'},{g:'に',r:'ni'},{g:'ぬ',r:'nu'},{g:'ね',r:'ne'},{g:'の',r:'no'}
  ]},
  { rows: 'H-row', chars: [
    {g:'は',r:'ha'},{g:'ひ',r:'hi'},{g:'ふ',r:'fu'},{g:'へ',r:'he'},{g:'ほ',r:'ho'}
  ]},
  { rows: 'M-row', chars: [
    {g:'ま',r:'ma'},{g:'み',r:'mi'},{g:'む',r:'mu'},{g:'め',r:'me'},{g:'も',r:'mo'}
  ]},
  { rows: 'Y-row', chars: [
    {g:'や',r:'ya'},{g:'ゆ',r:'yu'},{g:'よ',r:'yo'}
  ]},
  { rows: 'R-row', chars: [
    {g:'ら',r:'ra'},{g:'り',r:'ri'},{g:'る',r:'ru'},{g:'れ',r:'re'},{g:'ろ',r:'ro'}
  ]},
  { rows: 'W/N', chars: [
    {g:'わ',r:'wa'},{g:'を',r:'wo'},{g:'ん',r:'n'}
  ]},
  { rows: 'Dakuten (voiced)', chars: [
    {g:'が',r:'ga'},{g:'ぎ',r:'gi'},{g:'ぐ',r:'gu'},{g:'げ',r:'ge'},{g:'ご',r:'go'},
    {g:'ざ',r:'za'},{g:'じ',r:'ji'},{g:'ず',r:'zu'},{g:'ぜ',r:'ze'},{g:'ぞ',r:'zo'},
    {g:'だ',r:'da'},{g:'ぢ',r:'di'},{g:'づ',r:'du'},{g:'で',r:'de'},{g:'ど',r:'do'},
    {g:'ば',r:'ba'},{g:'び',r:'bi'},{g:'ぶ',r:'bu'},{g:'べ',r:'be'},{g:'ぼ',r:'bo'}
  ]},
  { rows: 'Handakuten (P)', chars: [
    {g:'ぱ',r:'pa'},{g:'ぴ',r:'pi'},{g:'ぷ',r:'pu'},{g:'ぺ',r:'pe'},{g:'ぽ',r:'po'}
  ]},
  { rows: 'Combinations', chars: [
    {g:'きゃ',r:'kya'},{g:'きゅ',r:'kyu'},{g:'きょ',r:'kyo'},
    {g:'しゃ',r:'sha'},{g:'しゅ',r:'shu'},{g:'しょ',r:'sho'},
    {g:'ちゃ',r:'cha'},{g:'ちゅ',r:'chu'},{g:'ちょ',r:'cho'},
    {g:'にゃ',r:'nya'},{g:'にゅ',r:'nyu'},{g:'にょ',r:'nyo'},
    {g:'ひゃ',r:'hya'},{g:'ひゅ',r:'hyu'},{g:'ひょ',r:'hyo'},
    {g:'みゃ',r:'mya'},{g:'みゅ',r:'myu'},{g:'みょ',r:'myo'},
    {g:'りゃ',r:'rya'},{g:'りゅ',r:'ryu'},{g:'りょ',r:'ryo'},
    {g:'ぎゃ',r:'gya'},{g:'ぎゅ',r:'gyu'},{g:'ぎょ',r:'gyo'},
    {g:'じゃ',r:'ja'},{g:'じゅ',r:'ju'},{g:'じょ',r:'jo'},
    {g:'びゃ',r:'bya'},{g:'びゅ',r:'byu'},{g:'びょ',r:'byo'},
    {g:'ぴゃ',r:'pya'},{g:'ぴゅ',r:'pyu'},{g:'ぴょ',r:'pyo'}
  ]}
];

const KATAKANA = [
  { rows: 'Vowels', chars: [
    {g:'ア',r:'a'},{g:'イ',r:'i'},{g:'ウ',r:'u'},{g:'エ',r:'e'},{g:'オ',r:'o'}
  ]},
  { rows: 'K-row', chars: [
    {g:'カ',r:'ka'},{g:'キ',r:'ki'},{g:'ク',r:'ku'},{g:'ケ',r:'ke'},{g:'コ',r:'ko'}
  ]},
  { rows: 'S-row', chars: [
    {g:'サ',r:'sa'},{g:'シ',r:'shi'},{g:'ス',r:'su'},{g:'セ',r:'se'},{g:'ソ',r:'so'}
  ]},
  { rows: 'T-row', chars: [
    {g:'タ',r:'ta'},{g:'チ',r:'chi'},{g:'ツ',r:'tsu'},{g:'テ',r:'te'},{g:'ト',r:'to'}
  ]},
  { rows: 'N-row', chars: [
    {g:'ナ',r:'na'},{g:'ニ',r:'ni'},{g:'ヌ',r:'nu'},{g:'ネ',r:'ne'},{g:'ノ',r:'no'}
  ]},
  { rows: 'H-row', chars: [
    {g:'ハ',r:'ha'},{g:'ヒ',r:'hi'},{g:'フ',r:'fu'},{g:'ヘ',r:'he'},{g:'ホ',r:'ho'}
  ]},
  { rows: 'M-row', chars: [
    {g:'マ',r:'ma'},{g:'ミ',r:'mi'},{g:'ム',r:'mu'},{g:'メ',r:'me'},{g:'モ',r:'mo'}
  ]},
  { rows: 'Y-row', chars: [
    {g:'ヤ',r:'ya'},{g:'ユ',r:'yu'},{g:'ヨ',r:'yo'}
  ]},
  { rows: 'R-row', chars: [
    {g:'ラ',r:'ra'},{g:'リ',r:'ri'},{g:'ル',r:'ru'},{g:'レ',r:'re'},{g:'ロ',r:'ro'}
  ]},
  { rows: 'W/N', chars: [
    {g:'ワ',r:'wa'},{g:'ヲ',r:'wo'},{g:'ン',r:'n'}
  ]},
  { rows: 'Dakuten (voiced)', chars: [
    {g:'ガ',r:'ga'},{g:'ギ',r:'gi'},{g:'グ',r:'gu'},{g:'ゲ',r:'ge'},{g:'ゴ',r:'go'},
    {g:'ザ',r:'za'},{g:'ジ',r:'ji'},{g:'ズ',r:'zu'},{g:'ゼ',r:'ze'},{g:'ゾ',r:'zo'},
    {g:'ダ',r:'da'},{g:'ヂ',r:'di'},{g:'ヅ',r:'du'},{g:'デ',r:'de'},{g:'ド',r:'do'},
    {g:'バ',r:'ba'},{g:'ビ',r:'bi'},{g:'ブ',r:'bu'},{g:'ベ',r:'be'},{g:'ボ',r:'bo'}
  ]},
  { rows: 'Handakuten (P)', chars: [
    {g:'パ',r:'pa'},{g:'ピ',r:'pi'},{g:'プ',r:'pu'},{g:'ペ',r:'pe'},{g:'ポ',r:'po'}
  ]},
  { rows: 'Combinations', chars: [
    {g:'キャ',r:'kya'},{g:'キュ',r:'kyu'},{g:'キョ',r:'kyo'},
    {g:'シャ',r:'sha'},{g:'シュ',r:'shu'},{g:'ショ',r:'sho'},
    {g:'チャ',r:'cha'},{g:'チュ',r:'chu'},{g:'チョ',r:'cho'},
    {g:'ニャ',r:'nya'},{g:'ニュ',r:'nyu'},{g:'ニョ',r:'nyo'},
    {g:'ヒャ',r:'hya'},{g:'ヒュ',r:'hyu'},{g:'ヒョ',r:'hyo'},
    {g:'ミャ',r:'mya'},{g:'ミュ',r:'myu'},{g:'ミョ',r:'myo'},
    {g:'リャ',r:'rya'},{g:'リュ',r:'ryu'},{g:'リョ',r:'ryo'},
    {g:'ギャ',r:'gya'},{g:'ギュ',r:'gyu'},{g:'ギョ',r:'gyo'},
    {g:'ジャ',r:'ja'},{g:'ジュ',r:'ju'},{g:'ジョ',r:'jo'},
    {g:'ビャ',r:'bya'},{g:'ビュ',r:'byu'},{g:'ビョ',r:'byo'},
    {g:'ピャ',r:'pya'},{g:'ピュ',r:'pyu'},{g:'ピョ',r:'pyo'}
  ]}
];

// Flatten all chars
const allHiragana = HIRAGANA.flatMap(r => r.chars.map(c => ({...c, script:'hiragana', row: r.rows})));
const allKatakana = KATAKANA.flatMap(r => r.chars.map(c => ({...c, script:'katakana', row: r.rows})));
const allChars = [...allHiragana, ...allKatakana];

// All unique row names (same across scripts)
const ALL_ROW_NAMES = HIRAGANA.map(r => r.rows);

// ===================== STATE =====================
let progress = {}; // {glyph: {correct, total}}
let quizMode = 'mc';
let quizSet = 'both';
let learnScript = 'hiragana';
let currentChar = null;
let sessionCorrect = 0, sessionIncorrect = 0, sessionTotal = 0;
let answered = false;
let streak = 0;
let lastStudyDate = '';
let selectedRows = new Set(ALL_ROW_NAMES); // all selected by default

// ===================== LOCAL STORAGE =====================
function saveProgress() {
  localStorage.setItem('kana_progress', JSON.stringify(progress));
  localStorage.setItem('kana_streak', streak.toString());
  localStorage.setItem('kana_last_date', lastStudyDate);
}

function loadProgress() {
  const p = localStorage.getItem('kana_progress');
  if (p) progress = JSON.parse(p);
  streak = parseInt(localStorage.getItem('kana_streak') || '0');
  lastStudyDate = localStorage.getItem('kana_last_date') || '';
  // Update streak
  const today = new Date().toDateString();
  if (lastStudyDate !== today) {
    const yesterday = new Date(Date.now() - 86400000).toDateString();
    if (lastStudyDate === yesterday) { streak += 1; }
    else if (lastStudyDate !== today) { /* keep if same day */ }
    lastStudyDate = today;
    saveProgress();
  }
  document.getElementById('streakNum').textContent = streak;
}

function resetProgress() {
  if (!confirm('Reset all progress? This cannot be undone.')) return;
  progress = {};
  sessionCorrect = 0; sessionIncorrect = 0; sessionTotal = 0;
  saveProgress();
  updateStatsDisplay();
  renderLearnGrid();
  renderProgressPage();
  alert('Progress reset!');
}

function recordAnswer(glyph, correct) {
  if (!progress[glyph]) progress[glyph] = {correct:0, total:0};
  progress[glyph].total++;
  if (correct) progress[glyph].correct++;
  saveProgress();
}

function getStatus(glyph) {
  const p = progress[glyph];
  if (!p || p.total === 0) return 'new';
  const acc = p.correct / p.total;
  if (acc >= 0.8 && p.total >= 5) return 'mastered';
  if (acc < 0.4) return 'struggling';
  return 'learning';
}

// ===================== PAGE NAV =====================
function showPage(name) {
  ['learn','quiz','progress'].forEach(p => {
    document.getElementById('page-'+p).classList.toggle('hidden', p !== name);
    document.getElementById('nav-'+p).classList.toggle('active', p === name);
  });
  if (name === 'quiz') { nextQuestion(); }
  if (name === 'progress') { renderProgressPage(); }
}

// ===================== LEARN PAGE =====================
function switchScript(script) {
  learnScript = script;
  document.getElementById('sbtn-hiragana').classList.toggle('active', script === 'hiragana');
  document.getElementById('sbtn-katakana').classList.toggle('active', script === 'katakana');
  renderLearnGrid();
}

function renderLearnGrid() {
  const container = document.getElementById('learn-grid');
  const data = learnScript === 'hiragana' ? HIRAGANA : KATAKANA;
  container.innerHTML = '';
  data.forEach(row => {
    const label = document.createElement('div');
    label.className = 'row-label';
    label.textContent = row.rows;
    container.appendChild(label);
    const grid = document.createElement('div');
    grid.className = 'char-grid';
    row.chars.forEach(c => {
      const status = getStatus(c.g);
      const card = document.createElement('div');
      card.className = 'char-card ' + status;
      card.innerHTML = `
        <div class="char-progress-dot"></div>
        <div class="char-glyph">${c.g}</div>
        <div class="char-romaji">${c.r}</div>
      `;
      card.title = `${c.g} = ${c.r} · Click for stroke order`;
      card.onclick = () => openStrokeModal(c.g, c.r, learnScript);
      grid.appendChild(card);
    });
    container.appendChild(grid);
  });
}

// ===================== QUIZ PAGE =====================
function setQuizMode(mode) {
  quizMode = mode;
  document.getElementById('mode-mc').classList.toggle('active', mode === 'mc');
  document.getElementById('mode-type').classList.toggle('active', mode === 'type');
  document.getElementById('mc-area').classList.toggle('hidden', mode !== 'mc');
  document.getElementById('type-area').classList.toggle('hidden', mode !== 'type');
  nextQuestion();
}

function setQuizSet(set) {
  quizSet = set;
  ['both','hiragana','katakana','weak'].forEach(s => {
    document.getElementById('qset-'+s).classList.toggle('active', s === set);
  });
  // Reset row selection to all when switching script set
  selectedRows = new Set(ALL_ROW_NAMES);
  renderRowPicker();
  nextQuestion();
}

// ===================== ROW PICKER =====================
function toggleRowPicker() {
  document.getElementById('rowPicker').classList.toggle('open');
}

function renderRowPicker() {
  const body = document.getElementById('rowPickerBody');
  const picker = document.getElementById('rowPicker');
  const countEl = document.getElementById('rowPickerCount');

  // Hide row picker entirely for 'weak' mode (it already filters by mastery)
  if (quizSet === 'weak') {
    picker.style.display = 'none';
    return;
  }
  picker.style.display = '';

  body.innerHTML = '';

  // Figure out which rows have chars in the current pool (before row filter)
  const basePool = getBasePool();
  // Count chars per row in base pool
  const rowCounts = {};
  basePool.forEach(c => {
    rowCounts[c.row] = (rowCounts[c.row] || 0) + 1;
  });

  ALL_ROW_NAMES.forEach(name => {
    if (!rowCounts[name]) return; // skip rows with no chars in current script
    const count = rowCounts[name];
    const chip = document.createElement('button');
    chip.className = 'row-chip' + (selectedRows.has(name) ? ' selected' : '');
    chip.innerHTML = `${name} <span class="chip-count">${count}</span>`;
    chip.onclick = () => toggleRow(name);
    body.appendChild(chip);
  });

  // Update count badge
  const totalRows = Object.keys(rowCounts).length;
  const selCount = [...selectedRows].filter(r => rowCounts[r]).length;
  countEl.textContent = selCount === totalRows ? 'all' : `${selCount}/${totalRows}`;
}

function toggleRow(name) {
  if (selectedRows.has(name)) {
    // Don't allow deselecting the last row
    const basePool = getBasePool();
    const rowCounts = {};
    basePool.forEach(c => { rowCounts[c.row] = true; });
    const visibleSelected = [...selectedRows].filter(r => rowCounts[r]);
    if (visibleSelected.length <= 1) return;
    selectedRows.delete(name);
  } else {
    selectedRows.add(name);
  }
  renderRowPicker();
  nextQuestion();
}

function selectAllRows() {
  selectedRows = new Set(ALL_ROW_NAMES);
  renderRowPicker();
  nextQuestion();
}

function clearAllRows() {
  // Keep at least the first row
  const basePool = getBasePool();
  const firstRow = basePool[0]?.row;
  selectedRows = new Set(firstRow ? [firstRow] : [ALL_ROW_NAMES[0]]);
  renderRowPicker();
  nextQuestion();
}

// Base pool without row filter (only script filter)
function getBasePool() {
  if (quizSet === 'hiragana') return allHiragana;
  if (quizSet === 'katakana') return allKatakana;
  return allChars;
}

function getQuizPool() {
  let pool;
  if (quizSet === 'weak') {
    pool = allChars.filter(c => {
      const s = getStatus(c.g);
      return s === 'struggling' || s === 'learning' || s === 'new';
    });
    if (pool.length < 4) pool = allChars;
    return pool;
  }

  pool = getBasePool();
  // Apply row filter
  if (selectedRows.size < ALL_ROW_NAMES.length) {
    pool = pool.filter(c => selectedRows.has(c.row));
  }
  // Ensure at least some chars
  if (pool.length === 0) pool = getBasePool();
  return pool;
}

function pickWeighted(pool) {
  // Weight struggling/new chars more
  const weighted = [];
  pool.forEach(c => {
    const s = getStatus(c.g);
    const w = s === 'struggling' ? 4 : s === 'new' ? 3 : s === 'learning' ? 2 : 1;
    for (let i = 0; i < w; i++) weighted.push(c);
  });
  return weighted[Math.floor(Math.random() * weighted.length)];
}

function nextQuestion() {
  answered = false;
  const pool = getQuizPool();
  currentChar = pickWeighted(pool);
  const fc = document.getElementById('flashcard');
  fc.className = 'flashcard';
  document.getElementById('cardChar').textContent = currentChar.g;
  document.getElementById('cardFeedback').textContent = '';
  document.getElementById('cardHint').textContent = currentChar.script === 'hiragana' ? 'Hiragana · What is the romaji?' : 'Katakana · What is the romaji?';
  document.getElementById('nextBtn').style.display = 'none';
  document.getElementById('strokeHintBtn').style.display = 'none';

  // Update progress bar (session)
  const total = sessionCorrect + sessionIncorrect;
  const pct = total === 0 ? 0 : Math.min(100, (total / 20) * 100);
  document.getElementById('quizProgressFill').style.width = pct + '%';

  if (quizMode === 'mc') renderChoices(pool);
  else {
    const inp = document.getElementById('typeInput');
    inp.value = '';
    inp.className = 'type-input';
    inp.disabled = false;
    inp.focus();
  }
}

function renderChoices(pool) {
  // Pick 3 wrong answers
  const wrong = pool.filter(c => c.r !== currentChar.r);
  const shuffledWrong = wrong.sort(() => Math.random() - 0.5).slice(0, 3);
  const options = [...shuffledWrong, currentChar].sort(() => Math.random() - 0.5);
  const grid = document.getElementById('choicesGrid');
  grid.innerHTML = '';
  options.forEach(opt => {
    const btn = document.createElement('button');
    btn.className = 'choice-btn';
    btn.textContent = opt.r;
    btn.onclick = () => handleChoice(opt.r, btn);
    grid.appendChild(btn);
  });
}

function handleChoice(romaji, btn) {
  if (answered) return;
  answered = true;
  const correct = romaji === currentChar.r;
  recordAnswer(currentChar.g, correct);
  if (correct) { sessionCorrect++; } else { sessionIncorrect++; }
  sessionTotal++;
  updateStatsDisplay();

  const fc = document.getElementById('flashcard');
  fc.className = 'flashcard ' + (correct ? 'correct' : 'incorrect');
  document.getElementById('cardFeedback').textContent = correct ? '正解 · Correct!' : `✗ It's "${currentChar.r}"`;

  // Highlight all buttons
  document.querySelectorAll('.choice-btn').forEach(b => {
    b.disabled = true;
    if (b.textContent === currentChar.r) b.classList.add('correct');
    else if (b === btn && !correct) b.classList.add('incorrect');
  });

  document.getElementById('nextBtn').style.display = 'block';
  document.getElementById('strokeHintBtn').style.display = 'block';
  renderLearnGrid();
}

function submitType() {
  if (answered) return;
  const inp = document.getElementById('typeInput');
  const val = inp.value.trim().toLowerCase();
  if (!val) return;
  answered = true;
  const correct = val === currentChar.r;
  recordAnswer(currentChar.g, correct);
  if (correct) { sessionCorrect++; } else { sessionIncorrect++; }
  sessionTotal++;
  updateStatsDisplay();

  const fc = document.getElementById('flashcard');
  fc.className = 'flashcard ' + (correct ? 'correct' : 'incorrect');
  document.getElementById('cardFeedback').textContent = correct ? '正解 · Correct!' : `✗ It's "${currentChar.r}"`;
  inp.className = 'type-input ' + (correct ? 'correct' : 'incorrect');
  inp.disabled = true;

  document.getElementById('nextBtn').style.display = 'block';
  document.getElementById('strokeHintBtn').style.display = 'block';
  renderLearnGrid();
}

function updateStatsDisplay() {
  document.getElementById('qCorrect').textContent = sessionCorrect;
  document.getElementById('qIncorrect').textContent = sessionIncorrect;
  document.getElementById('qTotal').textContent = sessionTotal;
}

// ===================== PROGRESS PAGE =====================
function renderProgressPage() {
  // Overview stats
  const all = allChars;
  let mastered = 0, learning = 0, struggling_count = 0, totalAnswers = 0, totalCorrect = 0;
  all.forEach(c => {
    const s = getStatus(c.g);
    if (s === 'mastered') mastered++;
    else if (s === 'learning') learning++;
    else if (s === 'struggling') struggling_count++;
    const p = progress[c.g];
    if (p) { totalAnswers += p.total; totalCorrect += p.correct; }
  });
  const acc = totalAnswers === 0 ? 0 : Math.round((totalCorrect / totalAnswers) * 100);

  document.getElementById('progressOverview').innerHTML = `
    <div class="overview-card mastered"><div class="overview-num">${mastered}</div><div class="overview-label">Mastered</div></div>
    <div class="overview-card learning"><div class="overview-num">${learning}</div><div class="overview-label">Learning</div></div>
    <div class="overview-card new"><div class="overview-num">${all.length - mastered - learning - struggling_count}</div><div class="overview-label">Not Seen</div></div>
    <div class="overview-card accuracy"><div class="overview-num">${acc}%</div><div class="overview-label">Accuracy</div></div>
  `;

  function renderProgGrid(chars, containerId) {
    const c = document.getElementById(containerId);
    c.innerHTML = '';
    chars.forEach(ch => {
      const s = getStatus(ch.g);
      const p = progress[ch.g];
      const score = p ? `${p.correct}/${p.total}` : '—';
      const el = document.createElement('div');
      el.className = 'prog-char ' + s;
      el.innerHTML = `<div class="prog-glyph">${ch.g}</div><div class="prog-romaji">${ch.r}</div><div class="prog-score">${score}</div>`;
      el.title = `${ch.g} (${ch.r}) · ${score} correct`;
      c.appendChild(el);
    });
  }
  renderProgGrid(allHiragana, 'prog-hiragana');
  renderProgGrid(allKatakana, 'prog-katakana');
}

// ===================== INIT =====================
loadProgress();
renderLearnGrid();
renderRowPicker();
nextQuestion();

// ===================== STROKE ORDER =====================
let strokeSpeed = 1;
let strokeAnimTimers = [];
let currentModalChar = null;

function toKanjiVGHex(char) {
  return char.codePointAt(0).toString(16).padStart(5, '0');
}

function getKanjiVGUrl(char) {
  return `https://cdn.jsdelivr.net/gh/KanjiVG/kanjivg@master/kanji/${toKanjiVGHex(char)}.svg`;
}

function openStrokeModal(glyph, romaji, script) {
  currentModalChar = { glyph, romaji, script };
  document.getElementById('modalGlyph').textContent = glyph;
  document.getElementById('modalRomaji').textContent = romaji;
  document.getElementById('modalScript').textContent = script === 'hiragana' ? 'ひらがな · Hiragana' : 'カタカナ · Katakana';
  document.getElementById('strokeOverlay').classList.add('open');
  document.getElementById('strokeComponents').innerHTML = '<div class="stroke-loading">Loading stroke data…</div>';
  loadAndRenderStrokes(glyph);
}

function closeStrokeModal(e) {
  if (e.target === document.getElementById('strokeOverlay')) closeStrokeModalDirect();
}
function closeStrokeModalDirect() {
  document.getElementById('strokeOverlay').classList.remove('open');
  clearTimers();
}

function clearTimers() {
  strokeAnimTimers.forEach(t => clearTimeout(t));
  strokeAnimTimers = [];
}

function setSpeed(s) {
  strokeSpeed = s;
  ['slow','normal','fast'].forEach(id => {
    document.getElementById('spd-'+id).classList.toggle('active', 
      (id === 'slow' && s === 0.5) || (id === 'normal' && s === 1) || (id === 'fast' && s === 2)
    );
  });
  replayAll();
}

async function loadAndRenderStrokes(glyph) {
  const chars = [...glyph]; // handles multi-char combos like きゃ
  const container = document.getElementById('strokeComponents');
  container.innerHTML = '';
  clearTimers();

  const fetchedSVGs = await Promise.all(chars.map(async ch => {
    try {
      const res = await fetch(getKanjiVGUrl(ch));
      if (!res.ok) throw new Error('Not found');
      return { char: ch, svgText: await res.text() };
    } catch {
      return { char: ch, svgText: null };
    }
  }));

  fetchedSVGs.forEach(({ char, svgText }, idx) => {
    const comp = document.createElement('div');
    comp.className = 'stroke-component';

    if (chars.length > 1) {
      const lbl = document.createElement('div');
      lbl.className = 'stroke-component-label';
      lbl.textContent = char;
      comp.appendChild(lbl);
    }

    const wrap = document.createElement('div');
    wrap.className = 'stroke-svg-wrap';
    wrap.id = `svgwrap-${idx}`;

    if (!svgText) {
      wrap.innerHTML = `<div class="stroke-error">Stroke data<br>unavailable</div>`;
    } else {
      wrap.innerHTML = svgText;
      const svg = wrap.querySelector('svg');
      if (svg) {
        svg.setAttribute('viewBox', '0 0 109 109');
        svg.style.width = '100%';
        svg.style.height = '100%';
        // Style: hide original strokes, show only outlines
        svg.querySelectorAll('path').forEach(p => {
          p.setAttribute('fill', 'none');
          p.setAttribute('stroke', '#d4c5b0');
          p.setAttribute('stroke-width', '3');
          p.setAttribute('stroke-linecap', 'round');
          p.setAttribute('stroke-linejoin', 'round');
        });
        // Hide built-in stroke numbers text
        svg.querySelectorAll('text').forEach(t => t.style.display = 'none');
      }

      // Stroke number bubbles
      const paths = wrap.querySelectorAll('path');
      const bubblesRow = document.createElement('div');
      bubblesRow.className = 'stroke-nums-row';
      bubblesRow.id = `bubbles-${idx}`;
      paths.forEach((_, i) => {
        const b = document.createElement('div');
        b.className = 'stroke-num-bubble';
        b.id = `bubble-${idx}-${i}`;
        b.textContent = i + 1;
        bubblesRow.appendChild(b);
      });

      const countLbl = document.createElement('div');
      countLbl.className = 'stroke-count-label';
      countLbl.textContent = `${paths.length} stroke${paths.length !== 1 ? 's' : ''}`;

      comp.appendChild(wrap);
      comp.appendChild(bubblesRow);
      comp.appendChild(countLbl);
      container.appendChild(comp);

      // Start animation for this component
      animateStrokes(wrap, idx, chars.length > 1 ? idx * 0.4 : 0);
      return;
    }

    comp.appendChild(wrap);
    container.appendChild(comp);
  });
}

function animateStrokes(wrap, compIdx, initialDelay = 0) {
  const paths = Array.from(wrap.querySelectorAll('path'));
  if (!paths.length) return;

  // Reset all
  paths.forEach(p => {
    const len = p.getTotalLength ? p.getTotalLength() : 100;
    p.style.strokeDasharray = len;
    p.style.strokeDashoffset = len;
    p.style.stroke = '#d4c5b0';
    p.style.transition = 'none';
  });
  // Reset bubbles
  paths.forEach((_, i) => {
    const b = document.getElementById(`bubble-${compIdx}-${i}`);
    if (b) { b.className = 'stroke-num-bubble'; }
  });

  let cumDelay = initialDelay;
  paths.forEach((path, i) => {
    const len = path.getTotalLength ? path.getTotalLength() : 80;
    const dur = Math.max(0.3, (len / 120) / strokeSpeed);

    // Activate bubble
    const t1 = setTimeout(() => {
      const b = document.getElementById(`bubble-${compIdx}-${i}`);
      if (b) b.className = 'stroke-num-bubble active';
    }, cumDelay * 1000);
    strokeAnimTimers.push(t1);

    // Animate stroke
    const t2 = setTimeout(() => {
      path.style.stroke = '#c9a84c';
      path.style.strokeWidth = '3.5';
      path.style.transition = `stroke-dashoffset ${dur}s ease, stroke 0s`;
      path.style.strokeDashoffset = '0';
    }, cumDelay * 1000 + 50);
    strokeAnimTimers.push(t2);

    // Mark bubble done after stroke completes
    const t3 = setTimeout(() => {
      const b = document.getElementById(`bubble-${compIdx}-${i}`);
      if (b) b.className = 'stroke-num-bubble done';
    }, (cumDelay + dur) * 1000 + 100);
    strokeAnimTimers.push(t3);

    cumDelay += dur + (0.25 / strokeSpeed);
  });
}

function replayAll() {
  clearTimers();
  const container = document.getElementById('strokeComponents');
  const wraps = container.querySelectorAll('.stroke-svg-wrap');
  wraps.forEach((wrap, idx) => {
    const paths = wrap.querySelectorAll('path');
    if (!paths.length) return;
    animateStrokes(wrap, idx, idx * 0.3);
  });
}

// Escape key closes modal
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') closeStrokeModalDirect();
  if (e.key === 'Enter' && document.getElementById('page-quiz').classList.contains('hidden') === false) {
    if (answered) nextQuestion();
    else if (quizMode === 'type') submitType();
  }
});
</script>
</body>
</html>
"""

components.html(HTML, height=1100, scrolling=True)
