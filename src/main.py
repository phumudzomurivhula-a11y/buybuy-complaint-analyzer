import json

from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.runnables import RunnableLambda


class AnalysisResult(BaseModel):
    product_category: str = Field(
        description="Product category most associated with complaints"
    )
    store_location: str = Field(
        description="Store location with the most complaints"
    )


def load_emails():
    with open("data/emails.json", "r", encoding="utf-8") as f:
        return json.load(f)


def build_chain():
    llm = ChatOpenAI(
        base_url="http://127.0.0.1:1234/v1",
        api_key="lm-studio",
        model="llama-3.2-3b-instruct:2",
        temperature=0
    )

    parser = JsonOutputParser(pydantic_object=AnalysisResult)

    prompt = ChatPromptTemplate.from_template(
        """
You are analyzing customer emails for BuyBuy.

Your job:
1. Find the complaint emails.
2. Work out the broad product category linked to the complaints.
3. Find which product category appears most in complaints.
4. Find which store location has the most complaints.

{format_instructions}

Emails:
{emails}
"""
    ).partial(format_instructions=parser.get_format_instructions())

    chain = (
        RunnableLambda(lambda emails: {"emails": json.dumps(emails, indent=2)})
        | prompt
        | llm
        | parser
        | RunnableLambda(
            lambda x: (
                f"Most negative product category: {x['product_category']}\n"
                f"Store with most complaints: {x['store_location']}"
            )
        )
    )

    return chain


def main():
    emails = load_emails()
    chain = build_chain()
    result = chain.invoke(emails)

    print("\n=== BuyBuy Complaint Analysis ===")
    print(result)


if __name__ == "__main__":
    main()