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

- Run your project.

    env/bin/pserve development.ini
