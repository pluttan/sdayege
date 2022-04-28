from PIL import Image
import pytesseract
img = Image.open('get_text_of_pic/test.png')
thresh = 40
fn = lambda x : 255 if x > thresh else 0
r = img.convert('L').point(fn, mode='1')
thresh = 250
fn = lambda x : 255 if x > thresh else 0
r = r.convert('L').point(fn, mode='1')
r.save('get_text_of_pic/foo.png')
print(pytesseract.image_to_string(Image.open('get_text_of_pic/foo.png')))