from apiclient.discovery import build

DEVELOPER_KEY = "AIzaSyAyr78u6vi9oZKu4Wugm3lpOdD8xd0cLr0 "
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def get_youtube_obj():
    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)


def youtube_search(search_query, max_results=25):
    youtube = get_youtube_obj()
    search_response = youtube.search().list(q=search_query,
                                            part="id,snippet",
                                            maxResults=max_results
                                            ).execute()
    return search_response
