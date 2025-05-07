# 🧠 Natural Language to SQL Query App

This Streamlit app enables users to ask **natural language questions** and receive **real-time SQL query results** from a MySQL database. It uses **LangChain** and **Google Gemini** to automatically translate questions into SQL.

---

## 🔧 Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python, LangChain
- **LLM Provider:** Google Generative AI (Gemini)
- **Database:** MySQL (via SQLAlchemy)
- **Other:** Pandas, Python `ast`, Dotenv

---

## 🚀 How It Works

1. User types a question in plain English.
2. LangChain + Gemini generates the corresponding SQL.
3. The SQL query is run on the connected MySQL DB.
4. The result is parsed and displayed as a table.

---

## 🛠️ Setup

1. **Clone the repo**:
   ```bash
   git clone https://github.com/your-username/nl-to-sql-streamlit.git
   cd nl-to-sql-streamlit

2.Create .env file:
```bash
GOOGLE_API_KEY=your_google_gemini_api_key
```
3.Install dependencies:

```bash
pip install -r requirements.txt
```

4.Edit DB credentials inside myapp.py:
```bash
db_user = "root"
db_password = "your_password"
db_host = "localhost"
db_name = "retail_sales_db"
Run the app:
```

5. Run the app:
```bash
streamlit run myapp.py

```
![Alt text](images/Capture.png)

💬 Sample Questions
What are the top 5 product categories by sales?

How many orders were placed in March?

Show average order value per customer.
