import json
import re

import pandas as pd


def scrap(username):
    with open('_{}/{}.json'.format(username, username)) as j:
        data = json.load(j)

    df = pd.read_json('incrediblebarcelona.json')

    cols = ['comments_disabled', 'height', 'width', 'display_url', 'edge_media_preview_like', 'caption', 'no_comments',
            'id', 'is_video', 'media_preview', 'shortcode', 'tags', 'taken_at_timestamp', 'urls',
            'username']

    series = []
    for d in data:
        x = [
            d['comments_disabled'],
            d['dimensions']['height'],
            d['dimensions']['width'],
            d['display_url'],
            d['edge_media_preview_like']['count'],
            d['edge_media_to_caption']['edges'][0]['node']['text'],
            d['edge_media_to_comment']['count'],
            d['id'],
            d['is_video'],
            d['media_preview'],
            d['shortcode'],
            ', '.join(d['tags']),
            d['taken_at_timestamp'],
            d['urls'],
            d['username'],
        ]

        dx = pd.DataFrame.from_dict(dict(zip(cols, x)))
        series.append(dx)

    df = pd.concat(series).reset_index().drop(columns=['index'])

    def picture_name(display_url):
        return re.findall('(?:\/e35\/)(\S+).jpg', display_url)[0]

    df['picture_name'] = df['display_url'].apply(picture_name)
