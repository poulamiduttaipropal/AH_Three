from selenium import webdriver
from time import sleep
import json
import traceback
from selenium.webdriver.firefox.options import Options
import googlemaps
from datetime import datetime
import urllib.request


options = Options()
options.headless = True


profile = webdriver.FirefoxProfile()
profile.set_preference('permissions.default.stylesheet', 2) 
profile.set_preference('permissions.default.image', False)
profile.set_preference("javascript.enabled", True)
gmaps_key=googlemaps.Client(key = "")

now = datetime.now()
timestamp = datetime.timestamp(now)

n=1
while(n!=16):
	
	sleep(2)
	browser = webdriver.Firefox(options=options, executable_path = '/home/ubuntu/geckodriver')
	url='https://www.appearhere.us/spaces/search?search_source=home-page&search_medium=link&search_campaign=home-page-space-grid&search_id=uh6r6cemm9&page=' + str(n) + '&type=space'
	
	browser.get(url)
	num=0
	for x in range(1, 7):
		try:
			expected_rent=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[1]/div/span[2]')
			title=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[2]')
			city=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[1]/span')
			area_unit=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[3]/span/span')
			image=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[1]/div/div/div/div/ul/li[1]/a/div/img')
			i=image[num].get_attribute("data-src")
			if '.jpg' in i:
				def download_image(url,path):
					fullname = path + str(timestamp) + ".jpg"
					urllib.request.urlretrieve(url,fullname)
					i="https://appearhererus.s3.eu-central-1.amazonaws.com/appearherepics/"+ str(timestamp) + ".jpg"
				download_image(i,"appearherepics/")
			elif '.png' in i:
				def download_image(url,path):
					fullname = path + str(timestamp) + ".png"
					urllib.request.urlretrieve(url,fullname)
					i="https://appearhererus.s3.eu-central-1.amazonaws.com/appearherepics/"+ str(timestamp) + ".png"
				download_image(i,"appearherepics/")
			elif '.tif' in i:
				def download_image(url,path):
					fullname = path + str(timestamp) + ".tif"
					urllib.request.urlretrieve(url,fullname)
					i="https://appearhererus.s3.eu-central-1.amazonaws.com/appearherepics/"+ str(timestamp) + ".tif"
				download_image(i,"appearherepics/")
			else:
				def download_image(url,path):
					fullname = path + str(timestamp) + ".jpg"
					urllib.request.urlretrieve(url,fullname)
					i="https://appearhererus.s3.eu-central-1.amazonaws.com/appearherepics/"+ str(timestamp) + ".jpg"
				download_image("https://www.skprealtors.com/wp-content/uploads/2016/07/not_available.jpg","appearherepics/")

			country="USA"
			pincode="__NA__"
			e=expected_rent[num].text + str('/day')
			area=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[3]/span/span')
			ae=area[num].text

			t=title[num].text
			c=city[num].text
			au=area_unit[num].text
			street=t[:t.find(",")]
			building_name=t
			landmark="__NA__"
			link=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[1]/div/div/div/div/ul/li[1]/a')
			l=link[num].get_attribute("href")
			print(l)
			geocode_result=gmaps_key.geocode(t)
			lat=geocode_result[0]["geometry"]["location"]["lat"]
			lon=geocode_result[0]["geometry"]["location"]["lng"]
			floor_count="__NA__"
			browser1 = webdriver.Firefox(options=options, executable_path = '/home/ubuntu/geckodriver')
			browser1.get(l)
			description=browser1.find_elements_by_xpath('/html/body/div[2]/div/div[3]/div/div[2]/div[1]/div[2]/div/p')
			d=description[0].text
			browser1.quit()
			dict={"area":ae,"area_unit":au,"building_name":building_name,"city":c,"country":country,"description":d,"expected_rent":e,"floor_count":floor_count,"landmark":landmark,"pincode":pincode,"property_image":[i],"street":street,"title":t,"latitude":lat,"longitude":lon}
			print(dict)
			#with open('/home/ubuntu/Appear_Here_data.json', 'a') as file:
				#file.write(json.dumps(dict))
			num=num+1
			
			print(num)
		except:
			print (traceback.format_exc())
	num=0
	for x in range(1, 25):
		try:
			
			expected_rent=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[1]/div/span[2]')
			title=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[2]')
			city=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[1]/span')
			area_unit=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[3]/span/span')
			image=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[1]/div/div/div/div/ul/li[1]/a/div/img')
			i=image[num].get_attribute("data-src")
			country="USA"
			area=browser.find_elements_by_xpath('')
			e=expected_rent[num].text + str('/day')
			pincode="__NA__"
			landmark="__NA__"
			floor_count="__NA__"
			if '.jpg' in i:
				def download_image(url,path):
					fullname = path + str(timestamp) + ".jpg"
					urllib.request.urlretrieve(url,fullname)
					i="https://appearhererus.s3.eu-central-1.amazonaws.com/appearherepics/"+ str(timestamp) + ".jpg"

				download_image(i,"appearherepics/")
			elif '.png' in i:
				def download_image(url,path):
					fullname = path + str(timestamp) + ".png"
					urllib.request.urlretrieve(url,fullname)
					i="https://appearhererus.s3.eu-central-1.amazonaws.com/appearherepics/"+ str(timestamp) + ".png"
				
				download_image(i,"appearherepics/")
			elif '.tif' in i:
				def download_image(url,path):
					fullname = path + str(timestamp) + ".tif"
					urllib.request.urlretrieve(url,fullname)
					i="https://appearhererus.s3.eu-central-1.amazonaws.com/appearherepics/"+ str(timestamp) + ".tif"
				
				download_image(i,"appearherepics/")
			else:
				def download_image(url,path):
					fullname = path + str(timestamp) + ".jpg"
					urllib.request.urlretrieve(url,fullname)
					i="https://appearhererus.s3.eu-central-1.amazonaws.com/appearherepics/"+ str(timestamp) + ".jpg"
				
				download_image("https://www.skprealtors.com/wp-content/uploads/2016/07/not_available.jpg","appearherepics/")

			area=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[3]/span/span')
			ae=area[num].text
			t=title[num].text
			c=city[num].text
			au=area_unit[num].text
			building_name=t
			street=t[:t.find(",")]
			link=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[1]/div/div/div/div/ul/li[1]/a')
			l=link[num].get_attribute("href")
			print(l)
			geocode_result=gmaps_key.geocode(t)
			lat=geocode_result[0]["geometry"]["location"]["lat"]
			lon=geocode_result[0]["geometry"]["location"]["lng"]
			browser1 = webdriver.Firefox(options=options, executable_path = '/home/ubuntu/geckodriver')
			browser1.get(l)
			description=browser1.find_elements_by_xpath('/html/body/div[2]/div/div[3]/div/div[2]/div[1]/div[2]/div/p')
			d=description[0].text
			num=num+1
			browser1.quit()
			dict={"area":ae,"area_unit":au,"building_name":building_name,"city":c,"country":country,"description":d,"expected_rent":e,"floor_count":floor_count,"landmark":landmark,"pincode":pincode,"property_image":[i],"street":street,"title":t,"latitude":lat,"longitude":lon}
			print(dict)
			#with open('/home/ubuntu/AppearHere2.json', 'a') as file:
				#file.write(json.dumps(dict))
			num=num+1
			print(num)
		except:
			print (traceback.format_exc())
	sleep(2)
	browser.quit()
	n=n+1
sleep(2)
browser = webdriver.Firefox(options=options, executable_path = '/home/ubuntu/geckodriver')
url='https://www.appearhere.us/spaces/search?q=Los%20Angeles%2C%20CA%2C%20USA&destination_id=&place_id=ChIJE9on3F3HwoAR9AhGJW_fL-I&search_id=xc4ru9xi9z9&page=1&type=space'
browser.get(url)
num=0
for x in range(1, 4):
	try:
		expected_rent=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[1]/div/span[2]')
		title=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[2]')
		city=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[1]/span')
		area_unit=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[3]/span/span')
		image=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[1]/div/div/div/div/ul/li[1]/a/div/img')
		i=image[num].get_attribute("data-src")
		country="USA"
		e=expected_rent[num].text + str('/day')
		pincode="__NA__"
		landmark="__NA__"
		floor_count="__NA__"
		area=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[3]/span/span')
		t=title[num].text
		c=city[num].text
		ae=area[num].text
		au=area_unit[num].text
		building_name=t
		street=t[:t.find(",")]
		link=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[1]/div/div/div/div/ul/li[1]/a')
		l=link[num].get_attribute("href")
		print(l)
		if '.jpg' in i:
				def download_image(url,path):
					fullname = path + str(timestamp) + ".jpg"
					urllib.request.urlretrieve(url,fullname)
					i="https://appearhererus.s3.eu-central-1.amazonaws.com/appearherepics/"+ str(timestamp) + ".jpg"
				
				download_image(i,"appearherepics/")
			elif '.png' in i:
				def download_image(url,path):
					fullname = path + str(timestamp) + ".png"
					urllib.request.urlretrieve(url,fullname)
					i="https://appearhererus.s3.eu-central-1.amazonaws.com/appearherepics/"+ str(timestamp) + ".png"

				download_image(i,"appearherepics/")
			elif '.tif' in i:
				def download_image(url,path):
					fullname = path + str(timestamp) + ".tif"
					urllib.request.urlretrieve(url,fullname)
					i="https://appearhererus.s3.eu-central-1.amazonaws.com/appearherepics/"+ str(timestamp) + ".tif"
				
				download_image(i,"appearherepics/")
			else:
				def download_image(url,path):
					fullname = path + str(timestamp) + ".jpg"
					urllib.request.urlretrieve(url,fullname)
					i="https://appearhererus.s3.eu-central-1.amazonaws.com/appearherepics/"+ str(timestamp) + ".jpg"
				download_image("https://www.skprealtors.com/wp-content/uploads/2016/07/not_available.jpg","appearherepics/")

				
		geocode_result=gmaps_key.geocode(t)
		lat=geocode_result[0]["geometry"]["location"]["lat"]
		lon=geocode_result[0]["geometry"]["location"]["lng"]
		browser1 = webdriver.Firefox(options=options, executable_path = '/home/ubuntu/geckodriver')
		browser1.get(l)
		description=browser1.find_elements_by_xpath('/html/body/div[2]/div/div[3]/div/div[2]/div[1]/div[2]/div/p')
		d=description[0].text
		browser1.quit()
		dict={"area":ae,"area_unit":au,"building_name":building_name,"city":c,"country":country,"description":d,"expected_rent":e,"floor_count":floor_count,"landmark":landmark,"pincode":pincode,"property_image":[i],"street":street,"title":t,"latitude":lat,"longitude":lon}
		print(dict)
		#with open('/home/ubuntu/AppearHere2.json', 'a') as file:
			#file.write(json.dumps(dict))
		num=num+1
		print(num)
	except:
		print (traceback.format_exc())
sleep(2)
browser.quit()
sleep(2)
browser = webdriver.Firefox(options=options, executable_path = '/home/ubuntu/geckodriver')
url='https://www.appearhere.us/spaces/search?q=Miami%2C%20FL%2C%20USA&destination_id=&place_id=ChIJEcHIDqKw2YgRZU-t3XHylv8&search_id=vvu0pqbs9la&page=1&type=space'
browser.get(url)
num=0
for x in range(1, 3):
	try:
		expected_rent=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[1]/div/span[2]')
		title=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[2]')
		city=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[1]/span')
		area_unit=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[3]/span/span')
		image=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[1]/div/div/div/div/ul/li[1]/a/div/img')
		i=image[num].get_attribute("data-src")
		country="USA"
		e=expected_rent[num].text + str('/day')
		pincode="__NA__"
		landmark="__NA__"
		floor_count='__NA__'
		if '.jpg' in i:
				def download_image(url,path):
					fullname = path + str(timestamp) + ".jpg"
					urllib.request.urlretrieve(url,fullname)
					i="https://appearhererus.s3.eu-central-1.amazonaws.com/appearherepics/"+ str(timestamp) + ".jpg"

				download_image(i,"appearherepics/")
			elif '.png' in i:
				def download_image(url,path):
					fullname = path + str(timestamp) + ".png"
					urllib.request.urlretrieve(url,fullname)
					i="https://appearhererus.s3.eu-central-1.amazonaws.com/appearherepics/"+ str(timestamp) + ".png"

				download_image(i,"appearherepics/")
			elif '.tif' in i:
				def download_image(url,path):
					fullname = path + str(timestamp) + ".tif"
					urllib.request.urlretrieve(url,fullname)
					i="https://appearhererus.s3.eu-central-1.amazonaws.com/appearherepics/"+ str(timestamp) + ".tif"

				download_image(i,"appearherepics/")
			else:
				def download_image(url,path):
					fullname = path + str(timestamp) + ".jpg"
					urllib.request.urlretrieve(url,fullname)
					i="https://appearhererus.s3.eu-central-1.amazonaws.com/appearherepics/"+ str(timestamp) + ".jpg"
				download_image("https://www.skprealtors.com/wp-content/uploads/2016/07/not_available.jpg","appearherepics/")

		area=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[3]/span/span')
		t=title[num].text
		ae=area[num].text
		c=city[num].text
		au=area_unit[num].text
		building_name=t
		street=t[:t.find(",")]
		link=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[1]/div/div/div/div/ul/li[1]/a')
		l=link[num].get_attribute("href")
		print(l)
		if '.jpg' in i:
				def download_image(url,path):
					fullname = path + str(timestamp) + ".jpg"
					urllib.request.urlretrieve(url,fullname)
					i="https://appearhererus.s3.eu-central-1.amazonaws.com/appearherepics/"+ str(timestamp) + ".jpg"
	
				download_image(i,"appearherepics/")
			elif '.png' in i:
				def download_image(url,path):
					fullname = path + str(timestamp) + ".png"
					urllib.request.urlretrieve(url,fullname)
					i="https://appearhererus.s3.eu-central-1.amazonaws.com/appearherepics/"+ str(timestamp) + ".png"
			
				download_image(i,"appearherepics/")
			elif '.tif' in i:
				def download_image(url,path):
					fullname = path + str(timestamp) + ".tif"
					urllib.request.urlretrieve(url,fullname)
					i="https://appearhererus.s3.eu-central-1.amazonaws.com/appearherepics/"+ str(timestamp) + ".tif"
			
				download_image(i,"appearherepics/")
			else:
				def download_image(url,path):
					fullname = path + str(timestamp) + ".jpg"
					urllib.request.urlretrieve(url,fullname)
					i="https://appearhererus.s3.eu-central-1.amazonaws.com/appearherepics/"+ str(timestamp) + ".jpg"
				download_image("https://www.skprealtors.com/wp-content/uploads/2016/07/not_available.jpg","appearherepics/")

				
		geocode_result=gmaps_key.geocode(t)
		lat=geocode_result[0]["geometry"]["location"]["lat"]
		lon=geocode_result[0]["geometry"]["location"]["lng"]
		browser1 = webdriver.Firefox(options=options, executable_path = '/home/ubuntu/geckodriver')
		browser1.get(l)
		description=browser1.find_elements_by_xpath('/html/body/div[2]/div/div[3]/div/div[2]/div[1]/div[2]/div/p')
		d=description[0].text
		browser1.quit()
		dict={"area":ae,"area_unit":au,"building_name":building_name,"city":c,"country":country,"description":d,"expected_rent":e,"floor_count":floor_count,"landmark":landmark,"pincode":pincode,"property_image":[i],"street":street,"title":t,"latitude":lat,"longitude":lon}
		print(dict)
		#with open('/home/ubuntu/AppearHere2.json', 'a') as file:
			#file.write(json.dumps(dict))
		num=num+1
		print(num)
	except:
		print (traceback.format_exc())
sleep(2)
browser.quit()






	

