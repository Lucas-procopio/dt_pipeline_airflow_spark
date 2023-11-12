# Goal
Creating a data pipelines extracting data from Twitter, using apache airflow, passing to Data Lake. Then, use spark for extract raw data from data lake, transforme them and loading in data lake again.

# Data origin
They from Twitter. In other words, it will be necessary to create Twitter developer account for getting access to data.

Website: https://developer.twitter.com/en

### Using Twitter API

    1º Step: Let's go to Twitter developer website. Then, create a user and justify because they are education goals. 

    2° Step: After that, you'll create a new project in Dashboard part - without him, you won't make a new application.
    
    3° Step: Creating an Application, define your app name and getting keys (API key, API key Secret and Bearer Token). Finally, key save your keys.

    note: When you create your keys, that's the only one moment you'll see them. If you forget, you'll need delete your app and create new one. I recommend you creating a .txt file with your keys and save it in your local folder, but don't forget put in gitignore file too.

## Technologies Used
- Twitter API
- Python3
- Apache Aiflow
- Spark 