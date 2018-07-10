This project was made to try internship vacancy. It's put a photo on AWS S3 and let you select which one you want to put on your gallery.

======

Getting Started
---------------

- Change directory into your newly created project.

    cd photos_webpage

- Create a Python virtual environment.

     virtualenv env
     
- Activate your env
    
    source $PATH_TO_YOUR_ENV$/bin/activate

- Upgrade packaging tools.

    pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    pip install -e ".[testing]"

- Intall some dependences to store files
    
    pip install pyramid_storage
    pip install boto
    
- Intall pymongo
    pip install pymongo

- Configure AWS S3
    Change the infos in the file development.ini to your AWS account security infos.
    Change inthe file view.py in the link found in line 25 to the name of your AWS S3's bucket.
    
- Run your project.

    pserve development.ini
