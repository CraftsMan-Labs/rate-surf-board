import gradio as gr
from openai import OpenAI
from PIL import Image
import os
from io import BytesIO
import base64

# Set your OpenAI API key
client = OpenAI()

def encode_image(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')


def validate_and_rate_images(images, views):
    results = []
    for image, view in zip(images, views):        
        # Prepare the prompt for GPT-4o
        prompt = f"Check if the image at is a {view} of a surfboard and rate it from 0 to 10. If it doesn't match, prompt to get a new image with the correct view."
        
        # Call GPT-4o API
        encoded_image = encode_image(image)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url":{
                                "url": f"data:image/jpeg;base64,{encoded_image}"
                                },
                        },
                    ],
                }
            ],
            max_tokens=100
        )
        
        # Extract the response
        rating = response.choices[0].message.content.strip()
        results.append(f"View: {view}, Rating: {rating}")
    
    return results

# Gradio interface
def upload_images(*images):
    views = [
        "Top View", "Bottom View", "Left Side View", "Right Side View",
        "Front View", "Back View", "Fin Right Side View", "Fin Left Side View",
        "Fin Front View", "Fin Back View"
    ]
    return validate_and_rate_images(images, views[:len(images)])

# Create Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## Surfboard Image Validator")
    image_inputs = [gr.Image(type="pil", label=f"Image {i+1}") for i in range(6)]
    output = gr.Textbox(label="Results")
    submit_button = gr.Button("Validate and Rate")
    submit_button.click(upload_images, inputs=image_inputs, outputs=output)

# Launch the Gradio app
demo.launch()