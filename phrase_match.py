def is_phrase_match(match: str, body: str) -> bool:
    """
    Check if "match" is in "body".

    This is to solve an issue we are having with checking for keywords in
    peoples profiles. For example, right now, searching for "COO" will
    return true against "Coordinator". We do not want this to be true.

    We do, however, want to match "COO" against "I am the coo".
    """
    return False
