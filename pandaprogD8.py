import pandas as pd

# Sample dataset
data = {
    "text": ["I love this product", "This is bad", "Amazing experience"],
    "label": ["positive", "negative", "positive"]
}

df = pd.DataFrame(data)
print(df)
