This project is a FastAPI application connected to a Supabase database. It provides a RESTful API for managing data in your Supabase tables.

1. Create and Activate Virtual Environment
python -m venv venv
... Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
install requirements.txt's libraries 

3. Set Up Supabase Database
Create your on account and new project on the supabase 

4. Environment Configuration
Create a .env file in your project root with the following variables:

### SUPABASE_URL=your_supabase_project_url
### SUPABASE_KEY=your_supabase_anon_public_key

6. Run the Application
     uvicorn app.main:app --reload



