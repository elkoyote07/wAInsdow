# wIAnsdow - Intelligent Voice Assistant for Windows

wIAnsdow is an intelligent voice assistant that allows you to interact with your Windows system using natural language. By leveraging tools like Ollama, the assistant generates responses and commands based on user input and can execute them via the Command Prompt (CMD).

This project integrates voice recognition and synthesis, providing a hands-free method to control your computer.

## Features

- **Voice Recognition**: Capture and interpret voice commands using Google's speech recognition API.
- **Natural Language Processing**: Process commands using AI models such as `command_executer` to convert text to appropriate CMD commands.
- **Text-to-Speech**: Provide spoken feedback to the user using `pyttsx3`.
- **System Control**: Execute system commands directly from voice commands.
- **Model Generation**: Use a custom-trained model for generating CMD commands from natural language.

## Requirements

To run this project, you'll need Python 3.x and the following dependencies:

- `requests`: For sending HTTP requests to create and manage AI models.
- `pyautogui`: For automating key presses in CMD.
- `pyttsx3`: For text-to-speech functionality.
- `speech_recognition`: For converting speech to text.
- `requests`: For handling HTTP requests.

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/wIAnsdow.git
   cd wIAnsdow
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Ensure your microphone is working and accessible by the speech recognition library.

## How to Use

### Running the Assistant

1. To start the assistant, simply run the `main.py` file:

   ```cmd
   python main.py
   ```

2. The assistant will begin listening for your voice commands and attempt to execute the corresponding CMD command.

### Creating a Custom Model

To create a custom AI model that interprets natural language commands into CMD commands, you can use the `create_model.py` script:

1. Make sure the model file (`Modelfile`) is properly formatted and placed in the same directory as `create_model.py`.
2. Run the script to create the model:

   ```cmd
   python create_model.py
   ```

   This will send the request to the API and create the model.

### Stopping the Assistant

To stop the assistant, simply say **"salir"** (exit) and the program will shut down.

## File Structure

```
wIAnsdow/
├── create_model.py       # Script to create a custom model for interpreting commands
├── main.py               # Main script to run the voice assistant
├── Modelfile             # Model file content for the AI to interpret commands
├── requirements.txt      # List of required Python packages
└── README.md             # This file
```

## Dependencies

To install the dependencies, you can create a `requirements.txt` file like this:

```
requests
pyautogui
pyttsx3
speechrecognition
```

Install them using:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **pyautogui**: Used for automating key presses in CMD.
- **pyttsx3**: A text-to-speech conversion library.
- **speech_recognition**: Google Speech Recognition API for converting speech to text.

## Contributing

Feel free to fork this project, open issues, and submit pull requests. Contributions are welcome!
