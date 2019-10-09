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
