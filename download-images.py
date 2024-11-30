import requests
from urllib.parse import urljoin
from io import BytesIO # convert byte to image
from PIL import Image # show image direct


base_url = "https://codeyad.com"
join_url = "_ipx/w_700&f_svg&q_100/codeyad/assets/images/Courses/2bc08517-909e-4d79-ab61-148413395620.png"

url = urljoin(base_url, join_url)

response = requests.get(url)
content = response.content

# download image
with open('image.jpg', 'wb') as image:
    image.write(content)

# open image and show
image = Image.open(BytesIO(content))
image.show()