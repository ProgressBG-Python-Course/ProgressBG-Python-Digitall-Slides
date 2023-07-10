from urllib import request
from bs4 import BeautifulSoup



def get_html(url):
	if url.startswith("http"):
		# make the request - change UA to prevent server deny for scripts
		req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

		# get response
		respone = request.urlopen(req)
		return respone.read()
	else:
		with open(url,"r") as f:
		  return f.read()

def scrape_data(page):
	bs_parser = BeautifulSoup(page, 'html.parser')
	products_html = bs_parser.find('ul', 'products')

	for product in products_html.find_all("article"):	
		try:
			name = product.select("div h2")[0].string
		except:
			name = "NoName"

		try:
			price = product.select("div tspan")[0].string
		except:
			price = None
			
		products.append((name,int(price)))

def print_scraped_data(products):
	sorted_by_price = sorted(products, key=lambda p: p[1])
	for i in sorted_by_price:
		# print(i)
		print("{} - {}".format(i[0],i[1]))


start_url = "https://laptop.bg/laptops-lenovo?page="
# start_url = "to_scrape.html"
products = []

for i in range(10,11):
	url = start_url+str(i)
	print("Scraping URL:", url)
	page = get_html(url)
	scrape_data(page)
	
print_scraped_data(products)



