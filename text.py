import json

from openai import OpenAI
from pydantic import BaseModel, Field

client = OpenAI()


class Topics(BaseModel):
    main_topic: str = Field(description="The title of the article for the main topic of the podcast.")
    secondary_topic: str = Field(description="The title of the article for the secondary topic of the podcast.")
    tertiary_topic: str = Field(description="The title of the article for the tertiary topic of the podcast.")


class Domain(BaseModel):
    name: str = Field(description="The name of the domain. Can be tech, business, or science.")
    topics: Topics


class Domains(BaseModel):
    domains: list[Domain]


class Phrase(BaseModel):
    phrase: str
    speaker: str = Field(description="Full name of the speaker")


class Script(BaseModel):
    phrases: list[Phrase]


def select_topics_for_domains():
    articles = json.load(open("example_data/content.json"))
    prompt = """
    You are an experienced podcast writer.
    When you receive an unordered list of articles, you need to decide on the three most important ones.
    The main topic should be the most important, followed by the second most important and third most important topic.
    Each article must be referenced with the exact title.
    Example: ‘Are Tesla’s robot prototypes AI marvels or remote-controlled toys?’
    """

    response = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": str(articles)}
        ],
        response_format=Domains,
    )
    message_content = response.choices[0].message.content
    message_json = json.loads(message_content)
    domains = Domains(**message_json)
    json.dump(domains.dict(), open("example_data/domains.json", "w"), indent=2)


def generate_script():
    domains = Domains(**json.load(open("example_data/domains.json")))
    content = json.load(open("example_data/content.json"))
    selected_topics = {}
    for domain in domains.domains:
        selected_topics[domain.name] = []
        for article in content[domain.name]:
            if article["title"] in domain.topics.dict().values():
                selected_topics[domain.name].append(article)

    script = Script(phrases=[])

    for i, domain in enumerate(domains.domains):
        print(f"Generating script for {domain.name}...")

        prompt = f"""
        You are an experienced writer for a podcast script.
        The podcast features two speakers, Gilberto Mathias and Ana Florence.
        The podcast covers tech, business and science news and the script part you generate will cover one of the domains.
        The script part must be readable in 3 minutes (approximately 400 words).

        The script MUST:
            •	Cover all given topics based on the provided information.
            •	Be easy, smooth, and enthusiastically readable.

        Facts, speculations, and trivia are a must! No descriptions—they’re boring!

        Keep it short, highly engaging, and unique.
        If the script part you generate is the first part, you must include an intro. Otherwise, you must not include an intro.
        If the script part you generate is not the first part, you must include a transition from the previous part.
        If the script part you generate is the last part, you must include an outro. Otherwise, you must not include an outro.

        This is part {i + 1} of {len(domains.domains)} of the script for the podcast episode.
        Previous part(s) (if any): {str(script)}
        """
        response = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": str(selected_topics[domain.name])}
            ],
            response_format=Script,
        )
        message_content = response.choices[0].message.content
        message_json = json.loads(message_content)
        script_part = Script(**message_json)
        script.phrases.extend(script_part.phrases)
    json.dump(script.dict(), open("example_data/script.json", "w"), indent=2)


if __name__ == "__main__":
    select_topics_for_domains()
    print(f"Domains: {json.load(open('example_data/domains.json'))}")
    generate_script()
    print(f"Script: {json.load(open('example_data/script.json'))}")
