import requests
from gradio_client import Client
from dotenv import load_dotenv
import os

# Define a list of casinos with title, query, and image prompt
casinos = [
    {
        'title': "Fitzwilliam Casino & Card Club",
        'address': "Clifton Hall, Lower Fitzwilliam Street, Dublin 2, Ireland",
        'image': 'casino_logo',
        'query': "Fitzwilliam Casino & Card Club - Clifton Hall, Lower Fitzwilliam Street, Dublin 2, Ireland כתוב לי כמה שורות בעברית בלבד  על הקזינו מתי מלא אנשים איך הוא מומלץ או לא",
    },
    {
        'title': "The Sporting Emporium",
        'address': "Anne's Ln, Dublin 2, Ireland",
        'image': 'casino_building',
        'query': "The Sporting Emporium - Anne's Ln, Dublin 2, Ireland כתוב לי כמה שורות על הקזינו מתי מלא אנשים איך הוא מומלץ או לא",
    },
    {
        'title': "Playland Casino",
        'address': "O'Connell Street, Dublin 1, Ireland",
        'image': 'casino_dice',
        'query': "Playland Casino - O'Connell Street, Dublin 1, Ireland כתוב לי כמה שורות על הקזינו מתי מלא אנשים איך הוא מומלץ או לא",
    },
    {
        'title': "Colossus Casino",
        'address': "Lower Liffey Street, Dublin 1, Ireland",
        'image': 'poker_cards',
        'query': "Colossus Casino - Lower Liffey Street, Dublin 1, Ireland כתוב לי כמה שורות על הקזינו מתי מלא אנשים איך הוא מומלץ או לא",
    },
    {
        'title': "D1 Club Casino",
        'address': "N Great George's St, Rotunda, Dublin 1, Ireland",
        'image': 'slot_machines',
        'query': "D1 Club Casino - N Great George's St, Rotunda, Dublin 1, Ireland כתוב לי כמה שורות על הקזינו מתי מלא אנשים איך הוא מומלץ או לא",
    },
    {
        'title': "Empire Casino",
        'address': "Drogheda Street, Balbriggan, Co. Dublin, Ireland",
        'image': 'roulette_wheel',
        'query': "Empire Casino - Drogheda Street, Balbriggan, Co. Dublin, Ireland כתוב לי כמה שורות על הקזינו מתי מלא אנשים איך הוא מומלץ או לא",
    },
    {
        'title': "The Penthouse Casino & Card Club",
        'address': "Lr. Dorset Street, Dublin 1, Ireland",
        'image': 'casino_chips',
        'query': "The Penthouse Casino & Card Club - Lr. Dorset Street, Dublin 1, Ireland כתוב לי כמה שורות על הקזינו מתי מלא אנשים איך הוא מומלץ או לא",
    },
    {
        'title': "Silks Club",
        'address': "Lower Dorset Street, Dublin 1, Ireland",
        'image': 'blackjack_table',
        'query': "Silks Club - Lower Dorset Street, Dublin 1, Ireland כתוב לי כמה שורות על הקזינו מתי מלא אנשים איך הוא מומלץ או לא",
    },
    {
        'title': "Westbury Club",
        'address': "Balfe St, Dublin 2, Ireland",
        'image': 'playing_cards',
        'query': "Westbury Club - Balfe St, Dublin 2, Ireland כתוב לי כמה שורות על הקזינו מתי מלא אנשים איך הוא מומלץ או לא",
    },
    {
        'title': "Amusement City",
        'address': "Westmoreland St, Dublin 2, Ireland",
        'image': 'casino_entrance',
        'query': "Amusement City - Westmoreland St, Dublin 2, Ireland כתוב לי כמה שורות על הקזינו מתי מלא אנשים איך הוא מומלץ או לא",
    },
    {
        'title': "Amber Gaming Club",
        'address': "Moore Street, Dublin 1, Ireland",
        'image': 'money_stack',
        'query': "Amber Gaming Club - Moore Street, Dublin 1, Ireland כתוב לי כמה שורות על הקזינו מתי מלא אנשים איך הוא מומלץ או לא",
    },
    {
        'title': "Club Oasis",
        'address': "Mary Street, Dublin 1, Ireland",
        'image': 'casino_lights',
        'query': "Club Oasis - Mary Street, Dublin 1, Ireland כתוב לי כמה שורות על הקזינו מתי מלא אנשים איך הוא מומלץ או לא",
    },
    {
        'title': "Jackpot Casino",
        'address': "Talbot Street, Dublin 1, Ireland",
        'image': 'poker_chips',
        'query': "Jackpot Casino - Talbot Street, Dublin 1, Ireland כתוב לי כמה שורות על הקזינו מתי מלא אנשים איך הוא מומלץ או לא",
    },
    {
        'title': "Red Cow Casino",
        'address': "Naas Rd, Dublin 22, Ireland",
        'image': 'casino_floor',
        'query': "Red Cow Casino - Naas Rd, Dublin 22, Ireland כתוב לי כמה שורות על הקזינו מתי מלא אנשים איך הוא מומלץ או לא",
    },
    {
        'title': "Royal Casino",
        'address': "Parnell Street, Dublin 1, Ireland",
        'image': 'money_bills',
        'query': "Royal Casino - Parnell Street, Dublin 1, Ireland כתוב לי כמה שורות על הקזינו מתי מלא אנשים איך הוא מומלץ או לא",
    }
]

load_dotenv()

# Define your WordPress username and password
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
wordpress_url = os.getenv('WORDPRESS_URL')
wordpress_url_post = os.getenv('WORDPRESS_URL_POST')
authorization = os.getenv('AUTHORIZATION')
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
headers = {"Authorization": authorization}

# Function to upload the image to WordPress media library
def upload_image_to_wordpress(image_data):
    headers = {
        'Content-Type': 'image/jpeg',
    }
    files = {
        'file': ('image.jpg', image_data, 'image/jpeg'),
    }

    # Send POST request to upload the image
    response = requests.post(wordpress_url, auth=(username, password), files=files)
    if response.status_code == 201:
        image_id = response.json().get('id')
        image_url = response.json()['guid']['rendered']
        return image_url, image_id 
    else:
        print("Failed to upload image to WordPress media library")
        return None, None

# Gradio API interaction
client = Client("dicta-il/dictalm2.0-instruct-demo")

def query_stable_diffusion(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        print("Failed to query Stable Diffusion API:", response.text)
        return None

# Iterate over each casino object
for casino in casinos:
    # Gradio API prediction
    gradio_result = client.predict(message=casino['query'], api_name="/chat")
    print("Gradio Result:", gradio_result)

    # Stable Diffusion API query
    hugging_face_result = query_stable_diffusion({"inputs": casino['image']})
    image_bytes = query_stable_diffusion({"inputs": "ireland flag with famous view"})
    if image_bytes and hugging_face_result:
        image_url, image_id = upload_image_to_wordpress(image_bytes)
        image_url2, _ = upload_image_to_wordpress(hugging_face_result)

        if image_url and image_url2:
            post_data = {
                'title': casino['title'],
                'content': f'<h3>{casino["address"]}</h3> <p>{gradio_result}</p> <img src="{image_url2}" alt="{casino["image"]}">',
                'status': 'publish',
                'categories': [30],  # WordPress categories
                'featured_media': image_id
            }
            
            # Send POST request to create a new post
         
            response = requests.post(wordpress_url_post, auth=(username, password), json=post_data)
            if response.status_code == 201:
                print(f"Post for {casino['title']} successfully created!")
            else:
                print(f"Failed to create post for {casino['title']}: {response.text}")
        else:
            print(f"Failed to upload one or more images for {casino['title']}. Post not created.")
    else:
        print(f"Failed to generate images from APIs for {casino['title']}.")
