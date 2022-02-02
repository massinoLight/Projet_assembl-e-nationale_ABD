from selenium import webdriver
import random




def _build_query(query: str):
    return f"https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={query}&oq={query}&gs_l=img"

def _get_random_image(mot_cle):
        driver = webdriver.Firefox()

        driver.get(_build_query(mot_cle))
        image_urls = []
        thumbnails = driver.find_elements_by_css_selector("img.Q4LuWd")

        for image in thumbnails:
                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    image_urls.append(image.get_attribute('src'))
        r1 = random.randint(0, len(image_urls))
        retour=image_urls[r1]
        driver.close()
        return retour
