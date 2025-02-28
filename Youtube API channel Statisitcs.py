import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
from googleapiclient.discovery import build
from IPython.display import JSON

pd.set_option("display.max_columns", 5000)
pd.set_option("display.width", 5000)
api_key = "AIzaSyC_qbiVvFHq-1TiRgoldOYriBqcixyz0m0"
channel_id = ["UCBJycsmduvYEL83R_U4JriQ"]
# channel_id = ['UCoOae5nYA7VqaXzerajD0lg']
all_data = []
# From Google Developers -> Youtuber API -> Guide -> Referencec -> Channel -> List -> Python -> remove googleapiclient
# .discovery.build from below in line 15 just leave build and in the id change to ",".join(channel_id)
# Replace the credentials with your api_key that is obtained from the new project tab
api_service_name = "youtube"
api_version = "v3"
youtube = build(
    api_service_name, api_version, developerKey=api_key)


# Get credentials and create an API client
def get_channel_stats(youtube, channel_ids):
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=",".join(channel_id)
    )
    response = request.execute()
    print(response)
    print(response["items"])
    for item in response["items"]:
        data = {"Channel Name": item["snippet"]["title"],
                "Subscribers": item["statistics"]["subscriberCount"],
                "Views": item["statistics"]["viewCount"],
                "TotalVideos": item["statistics"]["videoCount"],
                "PlaylistId": item["contentDetails"]["relatedPlaylists"]["uploads"]
                }
        all_data.append(data)
    return pd.DataFrame(all_data)


channel_stats = get_channel_stats(youtube, channel_id)
print(channel_stats)


# request = youtube.playlists().list(
#        part="snippet,contentDetails",
#        playlistId = "UUBJycsmduvYEL83R_U4JriQ"
#    )
# response = request.execute()
# print(response)
# COMMENTS
def get_comments(youtube, video_ids):
    all_comments = []
    for video_id in video_ids:
        request = youtube.comments().list(
            part="snippets,replies",
            videoId=video_id
        )
    response = request.execute()
    comments_in_videos = [{"comment_id": item["id"],
                           "author": item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"],
                           "text": item["snippet"]["topLevelComment"]["snippet"]["textDisplay"],
                           "like_count": item["snippet"]["topLevelComment"]["snippet"]["likeCount"],
                           "published_at": item["snippet"]["topLevelComment"]["snippet"]["publishedAt"]}
                          for item in response["items"]
                          ]
    comments_in_videos_info = {"video_id": video_id, "comments": comments_in_videos}
    all_comments.append(comments_in_videos_info)
    return pd.DataFrame(all_comments)
# comments = get_comments(youtube,video_ids)
# print(comments)
