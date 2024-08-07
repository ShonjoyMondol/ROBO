# Voice Assistant Project

This project is a voice-activated assistant named Robo, capable of responding to various commands such as providing the current time and date, information retrieval, and answering predefined questions. The assistant uses speech recognition and text-to-speech technologies to interact with the user.

## Features

- Voice recognition using `speechrecognition`
- Text-to-speech using `pyttsx3`
- Fetching information from the Google Gemini API
- Provides current time and date in Bangladesh
- Responds to predefined questions about the assistant

## Requirements

- Raspberry Pi with Raspbian OS
- Python 3
- Microphone

## Installation

### 1. Update and Upgrade the System

Open the terminal and run the following commands:

```bash
sudo apt-get update
sudo apt-get upgrade
```

### 2. Install Python 3 and pip

If Python 3 is not already installed, run:

```bash
sudo apt-get install python3
sudo apt-get install python3-pip
```

### 3. Install Required Python Packages

Run the following command to install necessary Python packages:

```bash
pip3 install pyttsx3 requests SpeechRecognition pytz
```

### 4. Install espeak for Text-to-Speech

Run the following command to install the `espeak` speech synthesis engine:

```bash
sudo apt-get install espeak
```

### 5. Install portaudio for Speech Recognition

Run the following command to install `portaudio`:

```bash
sudo apt-get install portaudio19-dev
pip3 install pyaudio
```

## Configuration

### Google Cloud API Key

Ensure you have a Google Cloud API key with access to the Google Gemini API. Replace `"Your Google Gemini API key"` in the script with your actual API key.

## Usage

1. Ensure your microphone is connected to the Raspberry Pi.
2. Run the script with the following command:

```bash
python3 your_script.py
```

Replace `your_script.py` with the name of your script file.

## Commands

- **Robo, what time is it?** - Tells the current time in Bangladesh.
- **Robo, what's the date today?** - Provides the current date in Bangladesh.
- **Robo, what is your name?** - Responds with the assistant's name.
- **Robo, who created you?** - Responds with the creator's name.
- **Robo, how old are you?** - Tells the assistant's age.
- **Robo, [any other query]** - Fetches information from the Google Gemini API.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [pytz](https://pypi.org/project/pytz/)
```

