This project was made to try internship vacancy. It's put a photo on AWS S3 and let you select which one you want to put on your gallery.

======

Getting Started
---------------

- Change directory into your newly created project.

    cd photos_webpage

- Create a Python virtual environment.

    python3 -m venv env

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Intall some dependences to store files
    
    env/bin/pip install pyramid_storage
    env/bin/pip install boto
    
- Configure AWS S3
    Change the infos in the file development.ini to your AWS account security infos.
    Change inthe file view.py in the link found in line 25 to the name of your AWS S3's bucket.
    
- Run your project.

    env/bin/pserve development.ini
