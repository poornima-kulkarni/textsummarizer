📝 Extractive Text Summarizer (Django + NLP)
This project is a simple extractive text summarizer built using:

Django (Python Web Framework)
NLTK (Natural Language Toolkit)
HTML & CSS (frontend)
It allows users to paste text and get a summary in bullet points.

🚀 Features
Extractive summarization using NLTK frequency-based method
Output displayed as clean bullet points
Styled with external CSS
User-friendly web interface
Ready to deploy on GitHub / cloud platforms
📂 Project Structure
textsummarizer/
 ├── textsummarizer/        # Django project folder (settings, urls, etc.)
 ├── summary/               # Main app
 │    ├── templates/        # HTML templates
 │    ├── static/summary/   # CSS styles
 │    ├── utils.py          # Summarizer logic
 │    ├── views.py          # Handles requests
 ├── manage.py              # Django entry point
 ├── README.md              # Documentation
⚙️ Installation & Setup
Clone the repo:

git clone https://github.com/your-username/textsummarizer.git
cd textsummarizer
Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
Install dependencies:

pip install -r requirements.txt
Run migrations:

python manage.py migrate
Start the server:

python manage.py runserver
Open in your browser:

http://127.0.0.1:8000/
📦 Dependencies
Django
NLTK
(You can freeze dependencies into requirements.txt using:)

pip freeze > requirements.txt

📜 License
This project is open-source and free to use.
