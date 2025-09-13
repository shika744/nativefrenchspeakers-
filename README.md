# Native French Speakers - Streamlit Application

This is a Streamlit version of the Native French Speakers (NFS) platform for scheduling and managing French lessons.

## Features

- **Book French Lessons**: Integrated Calendly scheduling
- **Virtual Lessons**: Microsoft Teams integration
- **Learning Resources**: Custom learning materials
- **Dashboard**: Track your scheduled lessons and history
- **Secure Payments**: PayPal integration (simulated)

## Installation

1. Clone the repository
2. Install the requirements:

```
pip install -r requirements.txt
```

## Running the Application

Run the following command in the terminal:

```
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## Integrations

- Calendly: `calendly.com/niloafer-chetty0608`
- Microsoft Teams: `https://myaccount.microsoft.com/?ref=MeControl`

## Structure

- `app.py`: Main Streamlit application
- `assets/`: Contains static files like the logo
- `requirements.txt`: Python dependencies

## Customization

- Update the Calendly link in `app.py` to your own Calendly schedule
- Replace Microsoft Teams links with your own
- Modify the styling by editing the CSS in the `local_css()` function
