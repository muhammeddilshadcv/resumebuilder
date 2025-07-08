# 📝 ResumeBuilder

ResumeBuilder is a Django-based web application that helps users generate professional resumes in PDF format. Users can enter their personal and professional details via a simple web interface, and the system will generate a downloadable PDF resume using `pdfkit` and `wkhtmltopdf`.

---

## 🚀 Features

- Web-based form for inputting resume details
- Generates resume in `.pdf` format using HTML templates
- Supports sections like name, contact, experience, education, and skills
- Clean and customizable code structure
- Lightweight and beginner-friendly

---

## 📁 Project Structure

resumebuilder/
- resume.py
- template.pdf (optional if using a pre-designed layout)
- output/
  - generated_resume.pdf
- README.md

---

## 🛠️ Tech Stack

- **Framework:** Django
- **Language:** Python
- **PDF Generation:** `pdfkit` and `wkhtmltopdf`
- **Form Styling:** django-crispy-forms, crispy-bootstrap4

---

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/muhammeddilshadcv/resumebuilder.git
cd resumebuilder
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
.\venv\Scripts\activate  # On Windows
```

### 3. Install dependencies

```bash
pip install fpdf
pip install -r requirements.txt
```

### 4. Run the development server

```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000/ in your browser to use the resume builder.


### ✅ Requirements

- Python 3.x
- Django
- pdfkit
- wkhtmltopdf (installed separately)
- django-crispy-forms
