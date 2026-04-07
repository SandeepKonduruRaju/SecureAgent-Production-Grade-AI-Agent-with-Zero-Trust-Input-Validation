# app/security/ensemble.py

def mock_model_1(text):
    return "UNSAFE" if "ignore" in text else "SAFE"

def mock_model_2(text):
    return "UNSAFE" if "bypass" in text else "SAFE"

def mock_model_3(text):
    return "UNSAFE" if "system prompt" in text else "SAFE"


def ensemble_vote(text: str):
    votes = [
        mock_model_1(text),
        mock_model_2(text),
        mock_model_3(text),
    ]

    unsafe_count = votes.count("UNSAFE")

    final = "UNSAFE" if unsafe_count >= 2 else "SAFE"

    return final, votes, unsafe_count / len(votes)