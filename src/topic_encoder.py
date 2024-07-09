
from bertopic import BERTopic

test_text = "This is a recipe"

def get_topics(text, model_type="wiki", top_n=1):
    """
    Get the topic(s) for a given text using a pre-trained BERTopic model.

    Parameters:
    text (str): The input text for which the topic(s) need to be identified.
    model_type (str, optional): The type of pre-trained BERTopic model to use. Default is "wiki".
                               Possible values: "wiki" (Wikipedia), "arxiv" (ArXiv).
    top_n (int, optional): The number of top topics to return. Default is 1.

    Returns:
    dict: A dictionary containing the identified topic(s) and their probabilities.

    Example:
    >>> get_topic("This is a sample text.")
    {'topic1': 0.85}
    """
    if model_type == "wiki":
        model = BERTopic.load("MaartenGr/BERTopic_Wikipedia")
    elif model_type == "arxiv":
        model = BERTopic.load("MaartenGr/BERTopic_Arxiv")
    topic_id, prob = model.find_topics(text, top_n=top_n)
    topics = []
    for topic in topic_id:
        topics.append(model.get_topic(topic)[0])
    dict = dict(topics)
    return dict