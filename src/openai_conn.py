#########################
# Import Packages
#########################
import openai
from openai import OpenAI
import requests
import json
import requests
import warnings
import configparser
warnings.filterwarnings('ignore')

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the config.ini file
config.read(r'src/keys.ini')

model_select = "gpt-3.5-turbo-16k"

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=config['openai']['openai_key'],
)

#########################
# Program Functions     #
#########################
def generate_jobdesc(user_query, 
                      temperature=0.1, 
                      max_tokens=50) -> str:
    
    response = client.chat.completions.create(
        model=model_select,
        messages=[
            {"role": "system", "content": """Take the role of a human resources professional who has expertise with identifying jobs, and specializes in federal descriptions. \
             I will feed you with several job descriptions, and I want you to provide me insight into whether or not that job is good for me."""},
            {"role": "user", "content": user_query}],
        temperature=temperature,
        top_p = 1,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content

def generate_jobtype(user_query, 
                     temperature=0.1, 
                     max_tokens=500) -> str:
    
    response = client.chat.completions.create(
        model=model_select,
        messages=[
            {"role": "system", "content": """Take the role of a human resources professional who has expertise with identifying jobs, and specializes in federal descriptions. \
             I will first feed you a description of my job, and I want you to respond with a list of general job types. For example, if I am interested in engineering and science, 
             please respond with engineer, scientist. Be relatively general, and between 5-10 jobs. Do not provide any other information than this list."""},
            {"role": "user", "content": user_query}],
        temperature=temperature,
        top_p = 1,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content

if __name__ == '__main__':
    print(generate_jobtype(user_query = "I'm interested in math, science, and being a teacher."))
    print(generate_jobdesc(user_query = ""))