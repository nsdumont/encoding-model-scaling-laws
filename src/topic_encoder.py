
from bertopic import BERTopic

test_text = "This is a recipe"

def init_model(model_type="wiki"):
    """
    Initialize a pre-trained BERTopic model.

    Parameters:
    model_type (str, optional): The type of pre-trained BERTopic model to use. Default is "wiki".
                               Possible values: "wiki" (Wikipedia), "arxiv" (ArXiv).

    Returns:
    BERTopic: A pre-trained BERTopic model.

    Example:
    >>> model = init_model("wiki")
    """
    if model_type == "wiki":
        model = BERTopic.load("MaartenGr/BERTopic_Wikipedia")
    elif model_type == "arxiv":
        model = BERTopic.load("MaartenGr/BERTopic_Arxiv")
    return model

def get_topics(text, model, top_n=1):
    """
    Retrieves the top N topics for the given text using the specified model.

    Parameters:
        text (str): The input text for which topics need to be retrieved.
        model: The topic model used for topic extraction.
        top_n (int): The number of top topics to retrieve. Default is 1.

    Returns:
        dict: A dictionary containing the top topics and their probabilities.
    """

    topic_id, prob = model.find_topics(text, top_n=top_n)
    topics = []
    topic_dict = dict({'topic_id': topic_id,'probability': prob})
    return topic_dict

