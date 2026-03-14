import json
import random
from pathlib import Path

store_locations = ["New York", "Dallas", "Chicago", "Los Angeles", "Houston"]

products = {
    "furniture": ["couch", "desk", "chair", "table", "bookshelf"],
    "clothing": ["jacket", "jeans", "shirt", "dress", "hoodie"],
    "electronics": ["phone", "laptop", "tablet", "headphones", "speaker"],
    "kitchen appliances": ["blender", "toaster", "coffee maker", "air fryer", "microwave"]
}

positive_templates = [
    "I bought a {product} and I am very happy with it.",
    "The {product} works perfectly. Great experience.",
    "I recently purchased a {product} and the quality is excellent.",
    "I love the {product} I bought from this store.",
    "The {product} arrived on time and works great."
]

negative_templates = [
    "I bought a {product} and it arrived damaged. Very disappointed.",
    "The {product} stopped working after a few days.",
    "I am unhappy with the quality of the {product}.",
    "The {product} was missing parts and I want a refund.",
    "Very poor experience. The {product} broke almost immediately."
]


def weighted_choice():
    # Make furniture complaints and New York complaints happen more often
    category = random.choices(
        ["furniture", "clothing", "electronics", "kitchen appliances"],
        weights=[4, 2, 2, 2],
        k=1
    )[0]

    store = random.choices(
        ["New York", "Dallas", "Chicago", "Los Angeles", "Houston"],
        weights=[4, 2, 2, 1, 1],
        k=1
    )[0]

    sentiment = random.choices(
        ["negative", "positive"],
        weights=[6, 4],
        k=1
    )[0]

    return category, store, sentiment


def make_email():
    category, store, sentiment = weighted_choice()
    product = random.choice(products[category])

    if sentiment == "positive":
        email_text = random.choice(positive_templates).format(product=product)
    else:
        email_text = random.choice(negative_templates).format(product=product)

    return {
        "store_location": store,
        "customer_email": email_text
    }


def generate_dataset(n=100):
    return [make_email() for _ in range(n)]


def save_dataset(data, filename="data/emails.json"):
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Dataset saved to {filename}")


if __name__ == "__main__":
    dataset = generate_dataset(100)
    save_dataset(dataset)