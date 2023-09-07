
import os
import streamlit as st
import requests

# Get api key, save it to environment variable and retrieve it as below
NASA_API_KEY = os.environ.get("API_KEY_NASA")
print(NASA_API_KEY)

# NASA url with api key
url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"

# response/request to connect to the url
response = requests.get(url)

# Load the data from the url as json data
json_data = response.json()

# Extract image url from json data and get content from a new requests as
# image data and text data processing different(image needs content, while
# text data needs either text or json etc.)
image_url = json_data['url']
image_data = requests.get(image_url).content

# Converting image data to a jpg file as an image
with open('image2.jpg','wb') as file:
    file.write(image_data)

# Using the above information in the streamlit website
st.title(json_data["title"])
st.image("image2.jpg")
st.write(json_data["explanation"])

########################################################
# url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
# image_url = 'https://api.nasa.gov/assets/img/general/apod.jpg'
#
# response = requests.get(image_url)
# image_data = response.content
# text_data = 'This image is from NASA-Astronomy Picture of the Day '
# with open('image.jpg','wb') as file:
#     file.write(image_data)
#
# st.text("Galaxy by the Lake")
# st.image("image.jpg")
# st.text(text_data)


