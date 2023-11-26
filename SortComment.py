import json
import os
all_comments = []
dirpath = "data_1125_ch"   
ytblist = os.listdir(dirpath)
print(ytblist)
for ytb in ytblist:
    ytb_path = os.path.join(dirpath, ytb, "video")
    videolist = os.listdir(ytb_path)
    for video in videolist:
        video_path = os.path.join(ytb_path, video)
        with open(video_path, "r", encoding="utf-8") as f:
            json_object = json.load(f)   
            title = json_object["video_info"]["title"]
            comments = list(map(lambda x: x["reply_content"],json_object["comments"]))
            all_comments.append(
                {
                    "title": title,
                    "comments": comments
                }
            )
        
# with open(dir, "r", encoding="utf-8") as f:
#     json_object = json.load(f)
# print(json_object)
with open("comments.json", "+w", encoding="utf-8") as f:
    json.dump(all_comments, f, indent=4, ensure_ascii=False)