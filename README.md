# Surfboard Image Validator

## Project Description

The Surfboard Image Validator is a proof-of-concept application that uses GPT-4o to rate second-hand surfboards and other water sports equipment. The application allows users to upload images of surfboards from different views (top, bottom, sides, etc.) and validates these images, providing a rating from 0 to 10. If an image does not match the expected view, the application prompts the user to upload a new image with the correct view. This project demonstrates the power of AI in automating the review process for second-hand sports equipment, helping people sell their products quickly.

## Dependencies

The project requires the following dependencies:

- `gradio`
- `openai`
- `pillow`

These dependencies are listed in the `requirements.txt` file.

## Installation

To install the required dependencies, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the dependencies using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt