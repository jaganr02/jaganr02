# AI Resume Analyzer (React + FastAPI + MongoDB)

A beginner-friendly full stack project that compares resume skills with job description skills and calculates an ATS score.

## Project Structure

```text
Ai Resume Analyzer/
  backend/
    app/
      __init__.py
      main.py
      routes.py
      models.py
      skills.py
         file_utils.py
      database.py
    .env.example
    requirements.txt
  frontend/
    src/
      main.jsx
      App.jsx
      index.css
    index.html
    package.json
    vite.config.js
  README.md
```

## Backend Setup (FastAPI)

1. Open terminal in `backend` folder.
2. Create virtual environment:
   - Windows: `python -m venv venv`
3. Activate virtual environment:
   - Windows: `venv\Scripts\activate`
4. Install packages:
   - `pip install -r requirements.txt`
5. Create `.env` file by copying `.env.example`:
   - `copy .env.example .env`
6. Add your Groq key in `.env`:
   - `GROQ_API_KEY=your_key_here`
7. Run backend server:
   - `uvicorn app.main:app --reload`

Backend runs at: `http://127.0.0.1:8000`

## Frontend Setup (React)

1. Open a second terminal in `frontend` folder.
2. Install packages:
   - `npm install`
3. Start frontend:
   - `npm run dev`

Frontend runs at: `http://127.0.0.1:5173`

## MongoDB Setup

1. Install MongoDB Community Edition.
2. Start MongoDB service.
3. Keep default local URL in `.env`:
   - `MONGODB_URL=mongodb://localhost:27017`
4. Database and collection are auto-created on first save.

## Groq AI Setup

The backend now sends the resume text and job description to Groq for semantic ATS analysis.

- SDK: `groq`
- Model: `llama-3.3-70b-versatile`
- API key source: `GROQ_API_KEY` in `.env`

## Resume Upload

The app supports three file types:

- PDF: `.pdf`
- Word: `.docx`
- Text: `.txt`

If a file is uploaded, its extracted text is used instead of the resume textarea.

Backend file extraction uses:

- `pypdf` for PDF files
- `python-docx` for DOCX files

## MongoDB Stored Fields

Each analysis document saves:

- Uploaded file name
- Resume text
- Job description
- Resume skills
- Job skills
- Matched skills
- Missing skills
- Suggestions
- ATS score
- Created timestamp

## API

### `GET /api/`
Health check.

### `POST /api/analyze`
Send `multipart/form-data` from the frontend.

Fields:

- `resume_text` - used when no file is uploaded
- `job_description` - required
- `resume_file` - optional PDF, DOCX, or TXT file

Example request body from the frontend uses `FormData`, not JSON.

Response:

```json
{
  "resume_skills": ["python", "react"],
  "job_skills": ["python", "fastapi", "react"],
  "matched_skills": ["python", "react"],
  "missing_skills": ["fastapi"],
   "match_level": "High",
   "strengths": ["Strong Python foundation"],
   "weaknesses": ["Limited FastAPI depth"],
   "suggestions": ["Learn FastAPI and build a small REST API project."],
  "ats_score": 66.67,
   "uploaded_file_name": "resume.pdf",
  "message": "Analysis completed and saved successfully."
}
```

## How It Works (Simple)

1. Frontend sends resume text + job description to backend.
2. Backend extracts skills using a predefined Python list.
3. Backend compares resume and job skills.
4. ATS score is calculated:
   - `(matched_skills / job_skills) * 100`
5. Full analysis is saved in MongoDB with timestamp.
6. Frontend shows skills, missing skills, suggestions, and ATS progress bar.

## Sample Screenshots

Add your own screenshots here after running the app locally.

- Home screen
- File upload area
- Analysis results with ATS score
- MongoDB saved record example
