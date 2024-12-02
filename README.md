# ChatWithExcel: A Retrieval-Augmented Generation (RAG) Model for Financial Data Analysis

## Overview

This project demonstrates the implementation of a Retrieval-Augmented Generation (RAG) pipeline tailored for financial data analysis. The system integrates retrieval and generative capabilities to allow users to query general ledger data using natural language. 

The pipeline is built with advanced tools like FAISS, LLMs and Llama Index for efficient retrieval and paired with a generative model such as Llama, Mixtral, etc. to deliver insightful responses.

---

## Features

1. **Data Integration**:
   - Imports and preprocesses general ledger data from an Excel file.
   - Handles formatting, missing values, and data structuring.

2. **RAG Pipeline**:
   - Combines a retrieval system with a generative model.
   - Ensures the knowledge base accurately reflects ledger data.

3. **Real-Time Search Interface**:
   - Provides an intuitive search bar for querying data.
   - Supports natural language queries like:
     - "What was the total revenue for Q1 2024?"
     - "List the top three expense categories for September 2023."
   - Delivers real-time, meaningful, and accurate responses.

4. **Advanced Query Handling**:
   - Handles complex financial queries, such as:
     - Total orders per year.
     - Top customers by sales.
     - Sales distribution across countries.

5. **Deployment**:
   - Hosted on a local server or cloud platform (e.g., Heroku or AWS).
   - Accessible via a public URL.

---

## Example Queries

- What was the total revenue for Q1 2024?
- List the top three expense categories for September 2023.
- What was the net income for the year 2023?
- Which customer placed the most orders?
- What is the sales distribution across different countries?

---

## How to Run the Application

### Prerequisites

- Python 3.8+
- Required dependencies from `requirements.txt`

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Harsh200112/ChatWithExcel.git
   cd ChatWithExcel
   ```

2. Install Requirements
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application
   ```bash
   streamlit run app.py
   ```

### Project Structure
```bash
ChatWithExcel/
├── data/                   # Dataset folder
├── scripts/                # Data preprocessing and ingestion scripts
├── models/                 # RAG pipeline implementation
├── frontend/               # Frontend interface for user queries
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
└── app.py                  # Main application file
```

### Future Work
- Expand retrieval capabilities for larger datasets.
- Improve response accuracy with fine-tuned models.
- Enhance UI for a better user experience.

