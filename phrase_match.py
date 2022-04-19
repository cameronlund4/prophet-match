def is_phrase_match(match: str, body: str) -> bool:
    """
    We are searching some profiles on a social media site for some
    keywords.

    We want to check if a given phrase, "match", is in a given
    body of text, "body".

    Currently, our solution is broken. If we are searching for "coo",
    we will get a true return for "coordinator". We only want to look
    for people with "coo" on it's own, such as "I am the COO".

    We want to match case insensitively. So, "coo" and "COO" should be True.

    Once that is working, try and get it to work ignoring non-alpha characters.
    For example, return true with match of "coo" and body of
    "I am the COO: chief operating officer!"
    """
    return match.lower() in body.lower()
