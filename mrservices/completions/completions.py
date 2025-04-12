from pydantic import BaseModel
from typing import Optional, Any

def get_offline_json_completion(
        prompt: str, user_prompt: str, format_json: Any,
        client: Any, model: str
        ):
    """
    Provides a completion for the given prompt and request
    using the specified model and format.
    Args:
        prompt (str): The prompt to be used for the completion.
        user_prompt (str): The user_prompt to be used for the completion.
        format_json (Any): The format for the JSON response.
        client (Any): The openai client.
        model (str): The model to be used for the completion.
    """

    completion = client.beta.chat.completions.parse(
        model=model,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_prompt},
        ],
        response_format=format_json,
    )
    return completion


def get_online_natural_completion(
        prompt: str, user_prompt: str, client: Any,
        model: str
        ):
    """
    Provides a completion for the given prompt and request
    using the specified model.
    Args:
        prompt (str): The prompt to be used for the completion.
        user_prompt (str): The user_prompt to be used for the completion.
        client (Any): The openai client.
        model (str): The model to be used for the completion.
    """
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_prompt}
        ],
        tools=[{"type": "web_search_preview"}],
    )
    return response


def get_offline_natural_completion(
        prompt: str, user_prompt: str, client: Any,
        model: str
        ):
    """
    Provides a completion for the given prompt and request
    using the specified model. Information is provided
    from the internet
    Args:
        prompt (str): The prompt to be used for the completion.
        user_prompt (str): The user_prompt to be used for the completion.
        client (Any): The openai client.
        model (str): The model to be used for the completion.
    """
    response = client.chat.completions.create(
        model=model,
        input=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_prompt}
        ],
    )
    return response
