# website with pictures of carpets
url  = "https://www.pexels.com/search/fancy%20carpets%2F%5E/"

#download page for parsing
page = request.get(url)
soup = bs(pag.text, 'html.parser')

#locate all elements with image tag
image_tags = soup.findAll('img')

#create directory
