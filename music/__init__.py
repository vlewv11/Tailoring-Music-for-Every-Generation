# import requests
import aiohttp
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


CLIENT_ID = "5f4d1ca81cc840eda8aba314c8dac049"
CLIENT_SECRET = "c04ff3a20cab42c7b037c763ee703ec1"
AUTH_URL = "https://accounts.spotify.com/api/token"
BASE_URL = "https://api.spotify.com/v1/"

seeds = [
    [
        "1TT9KfnlL1UoXNdIS4yDGx",
        "5Pn4vgV8SjClq23evnYwO8",
        "1QVc9GZbLH7fxK5CoDqpYq",
        "1OYyVKVaYfv5Ey8AUNuOJb",
        "018LhChoyqoQuBxA9GTD0z",
        "5xychtm5P5Cd7Z5OvJWSBX",
        "6A0XYRVq2qhCm8yuETUzdm",
        "4J4YTyNsoHp8k1qIubMOdl",
        "0E6GFTgOL8lwpRkIYlYpyN",
    ],
    [
        "16CUCqzVir1o0TPnDZRScr",
        "5v1zq6h98LuOM4aaTF6ipE",
        "1k0ILjecibLG3NtBopjblZ",
        "1Vl0uqNbMoOvWxpToBseEa",
        "4IhlY24rPzs32WNEQi98kD",
        "5dmYJY614qmDUl1OK1kxsR",
        "6UsKLhBbbfSf3jOxLjXrTr",
    ],
    [
        "1uRKT2LRANv4baowBWHfDS",
        "64Ny7djQ6rNJspquof2KoX",
        "2QfiRTz5Yc8DdShCxG1tB2",
        "6xNwKNYZcvgV3XTIwsgNio",
        "5ASgsifUe53WvOggVdP844",
        "3oAWTk92mZBxKBOKf8mR5v",
        "452KBpASS5lZLeJWX9Ixub",
        "06PdA0DLgF4BfAeUNZAbFG",
        "4LcrHUkRmXG3c0YD5VYutn",
        "64VP3skE86iTvdOlbzuIcO",
    ],
    [
        "0aym2LBJBk9DAYuHHutrIl",
        "3AhXZa8sUQht0UEdBJgpGc",
        "5Qe7NHxeLAn8KoLTNLSdwe",
        "7s25THrKz86DM225dOYwnr",
        "0hKRSZhUGEhKU6aNSPBACZ",
        "5t9KYe0Fhd5cW6UYT4qP8f",
        "4u9f8hqstB7iITDJNzKhQx",
        "2PzU4IB8Dr6mxV3lHuaG34",
        "18GiV1BaXzPVYpp9rmOg0E",
        "5uvosCdMlFdTXhoazkTI5R",
    ],
    [
        "5CQ30WqJwcep0pYcV4AMNc",
        "7tFiyTwD0nx5a1eklYtX2J",
        "40riOy7x9W7GXjyGp4pjAv",
        "7pKfPomDEeI4TPT6EOYjn9",
        "5ubvP9oKmxLUVq506fgLhk",
        "54flyrjcdnQdco7300avMJ",
        "5XTLMydD8xxGabWEKrX87i",
        "1fDsrQ23eTAVFElUMaf38X",
        "1h2xVEoJORqrg71HocgqXd",
        "0GjEhVFGZW8afUYGChu3Rr",
    ],
    [
        "7J1uxwnxfQLu4APicE5Rnj",
        "1ZPlNanZsJSPK5h9YZZFbZ",
        "1JSTJqkT5qHq8MDJnJbRE1",
        "37ZJ0p5Jm13JPevGcx4SkF",
        "7snQQk1zcKl8gZ92AnueZW",
        "57JVGBtBLCfHw2muk5416J",
        "6ADSaE87h8Y3lccZlBJdXH",
        "4gitetlGHZ9LfuJhwUhEhF",
        "5L6HNuXN71bfeuKXYtRasF",
        "2WfaOiMkCvy7F5fcp2zZ8L",
    ],
    [
        "5ghIJDpPoe3CfHMGu71E6T",
        "4eHbdreAnSOrDDsFfc4Fpm",
        "7ygpwy2qP3NbrxVkHvUhXY",
        "1KGi9sZVMeszgZOWivFpxs",
        "27QvYgBk0CHOVHthWnkuWt",
        "3MjUtNVVq3C8Fn0MP3zhXa",
        "7EsjkelQuoUlJXEw7SeVV4",
        "6qspW4YKycviDFjHBOaqUY",
        "3d9DChrdc6BOeFsbrZ3Is0",
        "0n2SEXB2qoRQg171q7XqeW",
    ],
    [
        "5IVuqXILoxVWvWEPm82Jxr",
        "2PpruBYCo4H7WOBJ7Q2EwM",
        "2yPoXCs7BSIUrucMdK5PzV",
        "1XduhVDrsLuMWk0fT0kbOx",
        "3ZFTkvIE7kyPt6Nu3PEa7V",
        "5rb9QrpfcKFHM1EUbSIurX",
        "2ZBNclC5wm4GtiWaeh0DMx",
        "3xrn9i8zhNZsTtcoWgQEAd",
        "4RCWB3V8V0dignt99LZ8vH",
        "1vrd6UOGamcKNGnSHJQlSt",
    ],
    [
        "1c8gk2PeTE04A1pIDH9YMk",
        "60nZcImufyMA1MKQY3dcCH",
        "7qiZfU4dY1lWllzX7mPBI3",
        "32OlwWuMpZ6b0aN2RZOeMS",
        "1zwMYTA5nlNjZxYrvBB2pV",
        "6habFhsOp2NvshLv26DqMb",
        "7BKLCZ1jbUBVqRi2FVlTVw",
        "34gCuhDGsG4bRPIf9bb02f",
        "2YpeDb67231RjR0MgVLzsG",
        "2VxeLyX666F8uXCJ0dZF8B",
    ],
    [
        "147gCksvDRmjG1pO51ZCcf",
        "6YQ7aPJhk0MGpwoKfFAEbS",
        "2tGgIA04KdLTRRGY5Ndw5w",
        "2beeR72qyVu9RYvqKO3L3R",
        "1neW540exG7Nm22gWhiHDu",
        "1K67iEOeqjAhzwDecSMNXX",
        "0dF7HP4wDwxCtID3mXpdYX",
        "2qKrxtkIuCOyE66TAunMXx",
        "4cNpO3kF8rqcH8G3huFCJp",
        "21LURtt0dELILmz9u99mWK",
    ],
]


def assign_age_range(age):
    age = int(age)
    age_ranges = {
        (0, 9): 9,
        (10, 19): 8,
        (20, 29): 7,
        (30, 39): 6,
        (40, 49): 5,
        (50, 59): 4,
        (60, 69): 3,
        (70, 79): 2,
        (80, 89): 1,
        (90, float("inf")): "0",
    }
    for age_range, folder_name in age_ranges.items():
        if age_range[0] <= age <= age_range[1]:
            print(folder_name)
            return folder_name
    return "Unknown"


async def _get_access_token(client_id, client_secret):
    async with aiohttp.ClientSession() as session:
        auth_data = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        }
        async with session.post(AUTH_URL, data=auth_data) as response:
            auth_response_data = await response.json()
            if "access_token" in auth_response_data:
                access_token = auth_response_data["access_token"]
                return access_token
            else:
                raise Exception(
                    "Failed to retrieve access token",
                    response.status,
                    auth_response_data,
                )


async def _get_recommendations(index, access_token):
    seed_tracks = seeds[index]
    if not access_token:
        print("No access token available")
        return None
    endpoint = "recommendations"
    params = {
        "seed_tracks": seed_tracks,
        "limit": 10,  # Number of recommendations to return
    }
    headers = {"Authorization": f"Bearer {access_token}"}
    async with aiohttp.ClientSession() as session:
        async with session.get(
            BASE_URL + endpoint, params=params, headers=headers
        ) as response:
            recommendations = await response.json()
            if "tracks" in recommendations:
                track_names = [track["id"] for track in recommendations["tracks"]]
                return track_names
            else:
                return None


async def _get_track_info(track_id, access_token):
    if not access_token:
        print("No access token available")
        return None

    endpoint = f"tracks/{track_id}"
    headers = {"Authorization": f"Bearer {access_token}"}
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL + endpoint, headers=headers) as response:
            track_info = await response.json()

            if "name" in track_info:
                return track_info
            else:
                print("Track information not found")
                return None


async def _get_song_demo(song_id):
    print(song_id)
    client_credentials_manager = SpotifyClientCredentials(
        client_id=CLIENT_ID, client_secret=CLIENT_SECRET
    )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    try:
        track_info = sp.track(song_id)
        preview_url = track_info["preview_url"]
        if preview_url:
            print(f"Demo song downloaded successfully")
            return preview_url
        else:
            print("No demo available for this song.", song_id)
    except spotipy.SpotifyException as e:
        print(f"Error: {e}")
    return None


async def _get_song_cover(track_id, access_token):
    urls = []
    endpoint = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(endpoint, headers=headers)
    track_info = response.json()

    # # Print track details
    # print(f"Track Name: {track_info['name']}")
    # print(f"Artist: {', '.join(artist['name'] for artist in track_info['artists'])}")
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(endpoint, headers=headers) as response:
                response.raise_for_status()
                cover_url = (await response.json())["album"]["images"][0]["url"]
                return cover_url
        except aiohttp.ClientResponseError:
            return None


async def fetch_playlist(index, initial=False):
    if not CLIENT_ID or not CLIENT_SECRET:
        raise ValueError(
            "CLIENT_ID and CLIENT_SECRET must be set in the environment variables."
        )
    try:
        access_token = await _get_access_token(CLIENT_ID, CLIENT_SECRET)
    except Exception as e:
        print(e)
        access_token = None
    initial_playlist = []
    track_list = (
        seeds[index]
        if initial == False
        else await _get_recommendations(index, access_token)
    )
    # print(track_list)
    for song in track_list:
        track_info = await _get_track_info(song, access_token)
        track_cover = await _get_song_cover(song, access_token)
        track_demo = await _get_song_demo(song)
        initial_playlist.append(
            {
                "track_id": track_info["id"],
                "track_name": track_info["name"]
                + " - "
                + track_info["artists"][0]["name"],
                "track_cover": track_cover,
                "track_demo": track_demo,
            }
        )
    return initial_playlist
