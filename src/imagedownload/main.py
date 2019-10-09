from gevent import monkey
monkey.patch_all()
import een
import os
import random
import gevent
from gevent import getcurrent
from gevent.pool import Pool

#login and get camera list
context = een.login("demo@een.com", "bettercloud")
camera_list = context.camera_list()
img_list = []
#seems sometimes there are no images on the camera, let's ensure we get one with at least 20
while len(img_list) < 20:
	#choose a random camera to pull images from (index 1 contains the camera id)
	camera = random.choice(camera_list)[1]
	img_list = context.image_list(esn=camera, asset_type="preview", time=een.timestamp("now"), count=-20)

try:
	os.mkdir("downloads")
except:
	pass

#fetch an image and save it the "downloads" folder, include camera name to identify them
def fetch_image(image):
	print('Task %s started' % id(getcurrent())) #get the thread id so we can see the concurrence at work
	img = context.fetch_image(esn=camera, time=image['s'], asset_type="preview")
	fh  = open("downloads/" + camera + "-" + image['s'] + ".jpeg", "wb")
	fh.write(img)
	fh.close()
	print('Task %s done' % id(getcurrent()))

#fetch them all!
#threads = [gevent.spawn(fetch_image, val, index) for index, val in enumerate(img_list)]
#threads = [gevent.spawn(fetch_image, image) for image in img_list]
#gevent.joinall(threads)

#fetch them using a pool of 5 greenlets
pool = Pool(5)
pool.map(fetch_image, img_list)


context.logout()
