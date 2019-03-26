import json

with open('incrediblebarcelona/incrediblebarcelona.json') as j:
    data = json.load(j)

keys = data[0].keys())
# dict_keys(['__typename', 'comments_disabled', 'dimensions', 'display_url', 'edge_media_preview_like', 'edge_media_to_caption', 'edge_
# media_to_comment', 'gating_info', 'id', 'is_video', 'location', 'media_preview', 'owner', 'shortcode', 'tags', 'taken_at_timestamp',
# 'thumbnail_resources', 'thumbnail_src', 'urls', 'username'])
