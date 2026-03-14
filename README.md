# BuyBuy Complaint Analyzer

This project explores how Large Language Models (LLMs) can be used to analyze customer feedback automatically.

Retail companies receive thousands of customer emails describing product experiences, complaints, and general feedback. Going through all of them manually takes time and effort. The goal of this project is to show how a simple AI pipeline can help identify patterns in that feedback.

In this example, the system reads customer emails and determines:

- which **product category receives the most complaints**
- which **store location has the most customer complaints**

The analysis is done using a **local LLM running through LM Studio** together with a **LangChain pipeline**.



## What this project does

The program takes a collection of customer emails and:

1. Reads the email text
2. Detects messages that contain complaints
3. Groups products into broader categories (for example: couch → furniture)
4. Determines which product category appears most often in complaint emails
5. Identifies which store location receives the most complaints

This shows how LLMs can be used to extract useful insights from **unstructured text data**.


## Technologies used

- Python  
- LangChain  
- LM Studio (local LLM server)  
- Pydantic for structured output  
- JSON dataset  


## Project structure

```
buybuy-complaint-analyzer
│
├── data
│   └── emails.json
│
├── src
│   └── main.py
│
├── generate_dataset.py
│
└── README.md
```

## Dataset

The project uses a **synthetic dataset** of customer emails generated with:


python generate_dataset.py


Each record contains a store location and a short customer message.

Example:

```json
{
  "store_location": "New York",
  "customer_email": "I bought a couch and it arrived damaged. Very disappointed."
}
```



## Example output

```
=== BuyBuy Complaint Analysis ===

Most negative product category: Furniture
Store with most complaints: New York
```



## How to run the project

Make sure **LM Studio is running with a model loaded**.

Install the required packages:

```
pip install langchain-openai langchain-core pydantic
```

Generate the dataset:

```
python generate_dataset.py
```

Run the analyzer:

```
python src/main.py
```



## What I learned

This project helped me explore:

- Prompt engineering
- Building LangChain pipelines
- Running LLMs locally with LM Studio
- Extracting structured insights from unstructured text

---

## Author

Phumudzo Murivhula
