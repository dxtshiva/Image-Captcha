from captcha.image import ImageCaptcha
import string,random

def random_string():
    # hash length
    N = 6
    s = string.ascii_uppercase + string.ascii_lowercase + string.digits
    # generate a random string of length 5
    global captcha_text
    captcha_text = ''.join(random.choices(s, k=N))
    image = ImageCaptcha(width = 180, height = 60)
    data = image.generate(captcha_text)
    global path
    path = './' + captcha_text+ '.png'
    image.write(captcha_text, path)


