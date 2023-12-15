from transformers import pipeline
classifier = pipeline("sentiment-analysis", model="stevhliu/my_awesome_model")
def tonal(news):
    data = classifier(news)
    return data[0]['label']

print(tonal("Hello fuck"))
