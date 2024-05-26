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
   ```

## Usage

To run the application, follow these steps:

1. Ensure you have set your OpenAI API key in you env variable "OPENAI_API_KEY"

2. Run the application:

   ```bash
   python app.py
   ```

3. The Gradio interface will launch in your default web browser. You can upload images of the surfboard from different views and get them validated and rated by GPT-4o.

## Project Structure

The project directory is structured as follows:

```
surfboard_validator/
├── requirements.txt
├── app.py
```

- `requirements.txt`: Contains the list of dependencies.
- `app.py`: Contains the Python code for the application.

## Approach

The application uses Gradio for the user interface and OpenAI's GPT-4o for image validation and rating. The images are uploaded through the Gradio interface, encoded to base64, and sent to the GPT-4o model for validation. The model checks if the images match the expected views and provides a rating. If an image does not match the expected view, the model prompts the user to upload a new image with the correct view.



## Conclusion

This project demonstrates the potential of using AI to automate the review process for second-hand surfboards and other water sports equipment. By leveraging GPT-4o and Gradio, we can quickly validate and rate images, helping users sell their products more efficiently. This proof-of-concept was implemented within one hour, showcasing the power of AI and modern development tools.