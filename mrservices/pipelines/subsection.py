from openai import OpenAI
from mrservices.completions.completions import (
    get_online_natural_completion,
    get_offline_json_completion
    )
from mrservices.prompts.text import PROMPT_REFERENCES
from mrservices.prompts.text import prompt_industry_region_subsection
from mrservices.formats.text_content import TextContentRefs

class GetSubsection:

    def __init__(self, api_key, model="gpt-4o-mini"):

        self.client = OpenAI(
            # This is the default and can be omitted
            api_key=api_key,
        )
        self.model = model
        self.data_raw = None
        self.data_formatted = None

    def get_subsection(self, industry, region, subsection, n_words):

        str_subsection = self.get_text(
            industry=industry,
            region=region,
            subsection=subsection,
            n_words=n_words
        )

        json_subsection = self.format_text(str_subsection)
        return json_subsection

    def get_text(self, industry, region, subsection, n_words=400):
        """
        Get the text for a specific subsection of the industry and region.
        """
        prompt = prompt_industry_region_subsection(
            industry=industry,
            region=region,
            subsection=subsection,
            n_words=n_words
        )

        data = get_online_natural_completion(
            prompt=prompt,
            user_prompt="",
            client=self.client,
            model=self.model
        )

        self.data_raw = data
        return data.output_text
    
    def format_text(self, text):
        """
        Format the text into a JSON object
        that contains the content and references.
        """
        info = get_offline_json_completion(
            prompt=PROMPT_REFERENCES,
            user_prompt=text,
            format_json=TextContentRefs,
            client=self.client,
            model=self.model
        )

        self.data_formatted  = info
        json = self.data_formatted.choices[0].message.parsed
        return json.model_dump()