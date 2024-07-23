# Auto Blog Tool

## Overview

Auto Blog Tool is a powerful solution designed to streamline the content creation process for blog owners and website administrators. It automates the insertion of relevant data into blog posts, saving time and improving productivity. This tool integrates with various APIs to generate content and images, and then publishes the results to your WordPress site.

## Features

- **Automated Content Generation:** Automatically generates content for blog posts based on predefined parameters.
- **Image Generation and Upload:** Uses Stable Diffusion API to generate images and uploads them to the WordPress media library.
- **WordPress Integration:** Creates and publishes posts on WordPress with the generated content and images.
- **Customizable Data Sources:** Supports integration with different data sources to pull in relevant information.

## Installation

1. **Clone the Repository:**

2. **Install the Required Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Create a `.env` File:**
   Create a `.env` file in the project directory with the following content:
    ```env
    USERNAME=<your_wordpress_username>
    PASSWORD=<your_wordpress_password>
    WORDPRESS_URL=<your_wordpress_media_url>
    WORDPRESS_URL_POST=<your_wordpress_post_url>
    AUTHORIZATION=<your_huggingface_api_key>
    ```


## my exampele blog that i have used is https://pewcasino.com
Info for casino website

## Configuration

Update the list of casinos in the `auto_blog_tool.py` script with the relevant data. Each casino entry should include the title, address, image prompt, and query for content generation.


   This will perform the following actions:
   - Generate content for each casino using the Gradio API.
   - Generate images using the Stable Diffusion API.
   - Upload images to the WordPress media library.
   - Create and publish a new post on WordPress with the generated content and images.



# Define an api configuration  
get api details 
https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers
