def get_user_input(message: str) -> str:
    """Returns user input after prompt message

    Args:
        message (str): Message to prompt. A new line is automatically added at the end.

    Returns:
        (str): user input. Always str formatted.
    """
    return input(message + "\n")