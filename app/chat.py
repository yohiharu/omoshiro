import base64
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

def chatImage(image_path):
  client = OpenAI()

  def encode_image(image_path):
    with open(image_path, "rb") as image_file:
      return base64.b64encode(image_file.read()).decode('utf-8')
  
  base64_image = encode_image(image_path)
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text":"あなたは、入力された画像に対して、面白いことをいうbotです。画像から面白いところを見つけて、それを返答してください。",
          },
          {
            "type": "image_url",
            "image_url": {
              "url":  f"data:image/jpeg;base64,{base64_image}"
            },
          },
        ],
      }
    ],
  )
  return response.choices[0].message.content
