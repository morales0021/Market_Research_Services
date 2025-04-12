PROMPT_REFERENCES = """Follow the next guidelines:
 1 - Identify in the whole text, the references associated to each section
 2 - Provide a small title for each reference
 3 - Structurate the text in a json where you provide the text into a content key, do not include references in the content key, keep newlines.
 4 - The text into the content key should put into tags <important></important> any phrase that is important for the reader to notice in terms of market analysis .
 5 - The references and the generated title should placed in a list, into the key "references."
"""

def prompt_text_plots_subsection(
    industry: str, region: str, subsection: str
    ) -> str:
    """
    Provides a prompt for the given industry and region.
    Args:
        industry (str): The industry to be used for the prompt.
        region (str): The region to be used for the prompt.
        subsection (str): The subsection to be used for the prompt.
    """
    prompt_plot = f"""I have a text that discusses {subsection} for the {industry} in the {region}.
    Based on this text, suggest 2-3 complementary data visualizations that would enhance understanding of the content.
    For each proposed plot, please:
    Describe the plot (e.g., chart showing market growth, chart comparing key drivers, ...).
    Explain in a natural way how the plot complements the text
    Provide mock or estimated data (in table format) that I can use to generate the plot.
    """

    return prompt_plot

def prompt_industry_region_subsection(
    industry: str, region: str, subsection: str, n_words: int = 400
    ) -> str:
    """
    Provides a prompt for the given industry and region.
    Args:
        industry (str): The industry to be used for the prompt.
        region (str): The region to be used for the prompt.
        subsection (str): The subsection to be used for the prompt.
        n_words (int): The number of words to be used for the prompt.
    """

    prompt = f"""Provide an overview of the {industry} industry in {region}, you should focus in \
    {subsection}.

    1. The information of the {subsection} should be a **string** written\
        in the tone of a **market research specialist** and should contain around {n_words} words. 

    2. You should include the url references used to construct the text

    3. Do not include any titles or subtitles, information should only contains paragraphs.
    """

    return prompt