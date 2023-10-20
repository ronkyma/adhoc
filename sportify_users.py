import requests

# Function to get Spotify user statistics
def get_spotify_user_stats(access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    response = requests.get("https://api.spotify.com/v1/users/stats", headers=headers)
    user_stats = response.json()
    return user_stats

# Function to get the first 10 users
def get_first_10_users(access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    params = {
        "limit": 10,
        "offset": 0,
    }
    response = requests.get("https://api.spotify.com/v1/users", headers=headers, params=params)
    first_10_users = response.json()
    return first_10_users

# Function to get the last 10 users
def get_last_10_users(access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    params = {
        "limit": 10,
        "offset": 90,  # Assuming there are 100 users, adjust as needed
    }
    response = requests.get("https://api.spotify.com/v1/users", headers=headers, params=params)
    last_10_users = response.json()
    return last_10_users

def main():
    # Assuming you have already obtained the access token
    access_token = "YOUR_ACCESS_TOKEN"

    # Get total user statistics
    user_stats = get_spotify_user_stats(access_token)
    total_users = user_stats.get("total_users", 0)
    print(f"Total Spotify Users: {total_users}")

    # Get the first 10 users
    first_10_users = get_first_10_users(access_token)
    print("\nFirst 10 Users:")
    for user in first_10_users["users"]:
        print(user)

    # Get the last 10 users
    last_10_users = get_last_10_users(access_token)
    print("\nLast 10 Users:")
    for user in last_10_users["users"]:
        print(user)

if __name__ == "__main__":
    main()
