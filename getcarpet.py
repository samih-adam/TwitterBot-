import os
from os import makedirs

import request
import soup

# website with pictures of carpets
from pygments.formatters import img

url  = "https://www.pexels.com/search/fancy%20carpets%2F%5E/"

# download page for parsing
page = request.get(url)
soup = bs(pag.text, 'html.parser')

# locate all elements with image tag
image_tags = soup.findAll('img')

# create directory for carpet images
if not os.path.exist('carpets'):
    os.makedirs('carpets')

# move to new directory
os.chdir('carpets')

# image file name variable
x = 0

# writing images

for image in image_tags:
    try:
        url = img['src']
        source = request.get(url)
        if source.status_code == 200:
            with open('model -' +str(x) + 'jpg', 'wb') as f:
                f.write(request.get(url).content)
                f.close()
                x += 1
    except:
        pass

