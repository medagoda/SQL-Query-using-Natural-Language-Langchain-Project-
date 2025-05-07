import os
import streamlit as st
from langchain.chains import create_sql_query_chain
from langchain_google_genai import GoogleGenerativeAI
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from langchain_community.utilities import SQLDatabase
from urllib.parse import quote_plus
import pandas as pd
from dotenv import load_dotenv
import ast  # <--- Add this import

# Load environment variables
load_dotenv()

# Database connection parameters
db_user = "root"
db_password = quote_plus("DATA2024@@data")  # URL encode special characters
db_host = "localhost"
db_name = "retail_sales_db"

# Create SQLAlchemy engine
engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")

# Initialize SQLDatabase
db = SQLDatabase(engine, sample_rows_in_table_info=3)

# Initialize LLM
llm = GoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=os.environ["GOOGLE_API_KEY"])

# Create SQL query chain
chain = create_sql_query_chain(llm, db)

# Function to generate and execute SQL query
def execute_query(question):
    try:
        # Generate SQL query from natural language
        response = chain.invoke({"question": question})
        
        # Clean markdown from response (if any)
        cleaned_response = response.replace("```sql", "").replace("```", "").strip()

        # Run the SQL query
        result = db.run(cleaned_response)

        return cleaned_response, result
    except ProgrammingError as e:
        st.error(f"SQL error occurred: {e}")
        return None, None
    except Exception as e:
        st.error(f"Unexpected error: {e}")
        return None, None

# Streamlit Interface
st.title("Natural Language to SQL Query App")

# Input from user
question = st.text_input("Enter your question about the database:")

# Execute on button click
if st.button("Execute"):
    if question:
        cleaned_query, query_result = execute_query(question)

        if cleaned_query and query_result is not None:
            st.subheader("Generated SQL Query:")
            st.code(cleaned_query, language="sql")

            st.subheader("Query Result:")

            # If query_result is a string, try to evaluate it safely
            if isinstance(query_result, str):
                try:
                    query_result = ast.literal_eval(query_result)
                except:
                    st.error("Could not parse result. Invalid format.")
                    query_result = []

            # Convert to DataFrame
            if isinstance(query_result, list):
                if len(query_result) > 0 and isinstance(query_result[0], (tuple, list)):
                    columns = [f"Column {i+1}" for i in range(len(query_result[0]))]
                    df = pd.DataFrame(query_result, columns=columns)
                else:
                    df = pd.DataFrame(query_result)
            else:
                df = pd.DataFrame()

            st.dataframe(df)
        else:
            st.warning("No results returned due to an error.")
    else:
        st.warning("Please enter a question.")
