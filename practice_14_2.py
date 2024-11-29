import json 

with open("annotations\image_info_test-dev2017.json") as f:
    date = json.load(f)
    print(f"Len images {len(date["images"])} and categories {len(date["categories"])}")
    im = date["images"]
    dd = 0
    max_ind = None
    for i in im:
        char = i["file_name"]
        if char == "000000000001.jpg":
            print("Image with name 000000000001.jpg")
            print(i["coco_url"])
            print(i["height"], i["width"], i["id"])

        if int(char.replace(".jpg", "")) > dd:
            dd = int(char.replace(".jpg", ""))
            max_ind = char

        else:
            pass
    print("The image with the highest number: ", max_ind)
