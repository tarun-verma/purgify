import spotipy
from spotipy.oauth2 import SpotifyOAuth

SCOPE = "user-library-read user-library-modify"

"""
Plug in your Spotify API credentials
Follow: https://developer.spotify.com/documentation/web-api/tutorials/getting-started
"""
SPOTIPY_CLIENT_ID = ""
SPOTIPY_CLIENT_SECRET = ""
SPOTIPY_REDIRECT_URI = ""

CHUNK_SIZE = 20  # I think the max amount of albums you can purge at once is 50, 20 is a reasonable default

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=SCOPE,
    )
)


def get_all_saved_albums():
    """
    Fetches ALL saved albums in your library by handling pagination.
    """
    print("Starting to fetch all saved albums...")

    results = sp.current_user_saved_albums(limit=50)
    album_uris = []

    while results:
        for item in results["items"]:
            album = item["album"]["name"]
            album_uri = item["album"]["uri"]
            album_uris.append(album_uri)

        if results["next"]:
            print(f"Fetching next page... (Total so far: {len(album_uris)})")
            results = sp.next(results)
        else:
            results = None

    return album_uris


if __name__ == "__main__":
    my_saved_albums = get_all_saved_albums()
    print(f"\nFinished! Total albums found: {len(my_saved_albums)}")
    print(f"Starting the album purge now with a chunk size of {CHUNK_SIZE}...")

    for i in range(0, len(my_saved_albums), CHUNK_SIZE):
        chunk_of_albums = my_saved_albums[i : i + CHUNK_SIZE]
        sp.current_user_saved_albums_delete(chunk_of_albums)
        print("Purged a chunk...")

    print("Done!")
