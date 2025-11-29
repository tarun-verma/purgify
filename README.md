# Spotify Album Purger

**NOTE:** While I have written this script myself, I did ask Gemini to generate this README.

This script removes all saved albums from your Spotify library. I wrote this because I wanted to give my Spotify library a fresh start. Note that it will NOT affect your playlists.

## Prerequisites

Before running this script, you need to have Python and the `spotipy` library installed.

```bash
pip install spotipy
```

## Setup

1.  **Create a Spotify App:**
    *   Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in.
    *   Click "Create an App".
    *   Give your app a name and description and click "Create".

2.  **Configure Redirect URI:**
    *   In your app's settings, click "Edit Settings".
    *   In the "Redirect URIs" field, add a URI, for example, `http://localhost:8888/callback`.
    *   Click "Save".

3.  **Set Credentials in the Script:**
    *   Open `purger.py`.
    *   You will find your Client ID and Client Secret in your Spotify App's dashboard.
    *   Copy your Client ID and paste it as the value for `SPOTIPY_CLIENT_ID`.
    *   Copy your Client Secret and paste it as the value for `SPOTIPY_CLIENT_SECRET`.
    *   Set `SPOTIPY_REDIRECT_URI` to the same URI you configured in your app settings (e.g., `http://localhost:8888/callback`).

    ```python
    SPOTIPY_CLIENT_ID = "YOUR_CLIENT_ID"
    SPOTIPY_CLIENT_SECRET = "YOUR_CLIENT_SECRET"
    SPOTIPY_REDIRECT_URI = "http://localhost:8888/callback"
    ```

## Usage

Once the setup is complete, run the script from your terminal:

```bash
python purger.py
```

The script will prompt you to log in to your Spotify account in your web browser for authorization the first time it runs.

## Disclaimer

This script will permanently remove all saved albums from your Spotify library. This action cannot be undone. Please be certain before running the script.
