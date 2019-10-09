# Image Download

I created a simple python file that does the image fetching from the API, and saves it to a local folder. The actual fetching is done by leveraging gevent.pool to ensure there are 5 downloads ocurring concurrently.

The project was created using python 3.7, pyscaffolding and anaconda (version 3).

The environment.yml file that I used is included so that it can be run anywhere

## Steps to run

    conda env create

ran from within the root folder. default name is `image-download`

    conda activate image-download

and finally run the file (I didn't create a script entry point to save time, but it could be added)

    python src/imagedownload/main.py

## Documentation

I added a pdf file with some documentation here: [EagleEyeNetwork(24hr).pdf](docs/EagleEyeNetwork(24hr).pdf)

## Updated version

This is the first "version" of this skill test (at the 24 hr mark). Since I had a bit more time to the deadline I decided to create a Django web app that consumed the API with the same requirements as this one. The updated one (at the 48 hr mark) can be found here: [https://github.com/loucho/django-een](https://github.com/loucho/django-een)

## Live Preview

A live version of the updated one (running on a EBS instance in AWS) can be found here: [http://django-env.nqzhivpfhv.us-west-2.elasticbeanstalk.com/cameras/](http://django-env.nqzhivpfhv.us-west-2.elasticbeanstalk.com/cameras/)
