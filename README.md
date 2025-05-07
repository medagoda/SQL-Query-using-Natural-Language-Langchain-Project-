# 🧠 Natural Language to SQL Query App

This Streamlit-based web application allows users to ask questions in **natural language** and get answers by automatically converting them into SQL queries using **LangChain** and **Google Gemini API**. It connects to a MySQL database and displays query results in a clean, interactive interface.

---

## 🚀 Features

- ✅ Natural language to SQL conversion using LLMs (Google Gemini)
- ✅ MySQL database integration via SQLAlchemy
- ✅ Automatic SQL generation using LangChain's `create_sql_query_chain`
- ✅ Interactive UI built with Streamlit
- ✅ Secure handling of credentials using `.env` file
- ✅ Query result displayed as a formatted DataFrame

---

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

🛠️ Setup Instructions
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/nl-to-sql-streamlit.git
cd nl-to-sql-streamlit
2. Configure environment variables
Create a .env file in the project root:

ini
Copy
Edit
GOOGLE_API_KEY=your_google_genai_api_key_here
3. Set up your MySQL database
Make sure your MySQL database is running and has a schema named retail_sales_db. Update these credentials in the script if needed:

python
Copy
Edit
db_user = "root"
db_password = "your_password"
db_host = "localhost"
db_name = "retail_sales_db"
▶️ Running the App
Run the app with:

bash
Copy
Edit
streamlit run myapp.py
💡 Example Questions
Try asking:

"What are the top 5 selling product categories?"

"How many orders were made in January?"

"Show total sales grouped by region."
