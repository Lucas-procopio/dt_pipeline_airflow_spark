# Goal
Creating a data pipelines extracting data from Twitter, using apache airflow, passing to Data Lake. Then, use spark for extract raw data from data lake, transforme them and loading in data lake again.

# Data origin
They from Twitter. In other words, it will be necessary to create Twitter developer account for getting access to data.

Website: https://developer.twitter.com/en

### Using Twitter API

    1º Step: Let's go to Twitter developer website. Then, create a user and justify because they are 
    education goals. 

    2° Step: After that, you'll create a new project in Dashboard part - without him, you won't 
    make a new application.
    
    3° Step: Creating an Application, define your app name and getting keys (API key, API key 
    Secret and Bearer Token). Finally, key save your keys.

    note: When you create your keys, that's the only one moment you'll see them. If you forget, 
    you'll need delete your app and create new one. I recommend you creating a .txt file with your 
    keys and save it in your local folder, but don't forget put in gitignore file too.

#### Creating APP

![creating_app](./images/creating_app_tt.PNG)

#### Getting API Keys

![api_keys](./images/api_keys_tt.PNG)


### Operation System

     I'll use ubuntu. If your system isn't based in unix 
     like linux or mac and you're using windows. So, it
     will be necessary install VMware for install and config an
     Operation System based on Unix.

Note: 
https://medium.com/thesecmaster/step-by-step-procedure-to-install-ubuntu-linux-on-vmware-workstation-18054864537b


### Installing Python3

    Download: 
        In python.org (https://www.python.org/downloads/), you can see every activate version for languague. Then download now Python-3.10.12.tgz. 
        After that, create new global variables

    Variables:
        export PYTHON_VERSION=3.10.12
        export PÝTHON_MAJOR=3

    Extracting Tgz file:
        tar -xvzf Python-${PYTHON_VERSION}.tgz
        cd Python-${PYTHON_VERSION}

    Configure Installation:
        ./configure \
            --prefix=/opt/python/${PYTHON_VERSION} \
            --enable-shared \
            --enable-optimizations \
            --enable-ipv6 \
            LDFLAGS=-Wl,-rpath=/opt/python/${PYTHON_VERSION}/lib,--disable-new-dtags

    Install:
        make
        sudo make install

    Verify the Installation:
        cd /opt/python/${PYTHON_VERSION}/bin
        sudo ln -s python3.10.12 python
        echo "PATH=/opt/python/3.10.12/bin/:$""PATH" >> ~/.profile
        .~/.profile 

### Installing Airflow



## Technologies Used
- Twitter API
- linux ubuntu 22.04
- Python3.10.12
- Apache Aiflow
- Spark 