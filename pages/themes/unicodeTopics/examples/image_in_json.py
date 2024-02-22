import json
import base64

def save_image_bytes_from_json(data_json):

    data = json.loads(data_json)
    image_base64 = data['image']

    # Decode Base64 data
    image_bytes = base64.b64decode(image_base64)

    # Save decoded image to a file
    with open(data['filename'], "wb") as img_file:
        img_file.write(image_bytes)

    print(f'{data["filename"]} saved!')

# JSON data containing image information
data_json = """
{
    "filename": "example_image.jpg",
    "type": "image/png",
    "image": "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAcElEQVR4nGI5y9PLAAOfJ3HB2VeWS8HZH7hmwNlMDCQC2mtgOb/hKJyzIy4Lzrbdpg5nV8Tcp6OTSNbAKMk+Dc7JUV0IZ7+PmwRn34zgpKOTSI8H2QUucE7q329wtv2hWDj7D6sCHZ1EsgZAAAAA//9eCxes6NHYOQAAAABJRU5ErkJggg==",
    "size": 152347,
    "url": "https://yulvil.github.io/gopherjs/02/"
}
"""

save_image_bytes_from_json(data_json)
