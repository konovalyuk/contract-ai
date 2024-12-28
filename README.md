# AI-Powered Contract Generator

This project is a web-based application powered by Llama3.2-1B-Instruct, designed to generate personalized contracts based on user input and uploaded PDF templates.

## Features

- **PDF Upload**: Upload contract templates for training.
- **Custom Contract Generation**: Describe the desired contract, and the application will generate it.
- **Downloadable Output**: Receive the generated contract in PDF format.
- **Interactive Web Interface**: User-friendly interface with file upload and result display.

## Project Structure

```
project/
│
├── app/
│   ├── main.py          # Main application logic
│   ├── templates/       # HTML templates
│   │   ├── upload.html  # File upload form
│   │   ├── generate.html # Contract generation interface
│   │   └── result.html  # Result display
│   └── static/          # CSS/JS files
│
├── contracts/           # Uploaded PDF templates
└── models/              # Trained Llama models
```

## Setup and Usage

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app/main.py
   ```
4. Open your browser at `http://127.0.0.1:5000`.

## Requirements

- Python 3.8+
- Llama3.2-1B-Instruct
- Flask or FastAPI (depending on your implementation choice)

## Future Enhancements

- Add multi-language support for contracts.
- Integrate advanced Llama models for better accuracy.
- Improve file management and model training automation.

Contributions and suggestions are welcome!