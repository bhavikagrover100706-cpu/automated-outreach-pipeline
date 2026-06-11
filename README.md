# Automated Outreach Pipeline

## Overview

This project automates the outreach process by integrating lead generation and email outreach tools. It helps streamline prospect identification and communication workflows.

## Features

- Lead discovery using Prospeo API
- Email outreach using Brevo API
- Automated workflow execution
- Configurable settings through environment variables
- Python-based implementation

## Technologies Used

- Python
- Brevo API
- Prospeo API
- Environment Variables (.env)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/bhavikagrover100706-cpu/automated-outreach-pipeline.git
```

2. Navigate into the project folder:

```bash
cd automated-outreach-pipeline
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file and add your API keys:

```env
BREVO_API_KEY=YOUR_BREVO_API_KEY
PROSPEO_API_KEY=YOUR_PROSPEO_API_KEY
```

## Usage

Run the main script:

```bash
python main.py
```

## Project Structure

```text
automated-outreach-pipeline/
├── main.py
├── brevo.py
├── prospeo.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Notes

API keys are not included in this repository. Users must provide their own API credentials through environment variables.

## Author

Bhavika Grover
