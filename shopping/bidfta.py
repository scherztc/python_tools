import webbrowser

def open_urls_in_browser(urls):
    for url in urls:
        webbrowser.open(url)

if __name__ == "__main__":
    urls = [
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=Cane&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=Shaolin&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=Kung&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=Tai&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=chi&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=Buddha&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=martial&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=soccer&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=sport&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=cards&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=game&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=card&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=sports&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=games&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=chinese&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=japanese&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=korean&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=drink dispenser&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=knife&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=gun&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=sword&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=mlb&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",	
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=nfl&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=music&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=european&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=watch&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=art&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=tea&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=golf&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
        "https://www.bidfta.com/items?pageId=1&itemSearchKeywords=remote control&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=adidas&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=nike&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=fifa&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=day bed&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=kayak&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
  	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=ninja&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
     	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=kebab&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
      	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=porch swing&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
       	"https://www.bidfta.com/items?pageId=1&itemSearchKeywords=metal detector&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
           "https://www.bidfta.com/items?pageId=1&itemSearchKeywords=curtain rods&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
           "https://www.bidfta.com/items?pageId=1&itemSearchKeywords=science&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l",
           "https://www.bidfta.com/items?pageId=1&itemSearchKeywords=bedroom furniture&location=24&location=26&location=2&location=520&location=25&location=581&locations=26&locations=24&locations=2&locations=581&l"
    ]
    open_urls_in_browser(urls)
