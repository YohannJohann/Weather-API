# Weather-API
A weather API that fetches and returns weather data

# Accessing Redis with Free Data Base Trial
- Visit https://cloud.redis.io/#/login and login with GitHub or Google
- On the left side, click the + sign on the Databases
- Scroll down until you see Database details
- On the left side of Database details, you'll see 30 MB free click it
- Scroll down some more and click Create Database

# Finding the REDIS HOST, PORT, and PASSWORD
- Go to Databases
- Look for Public endpoint, the last numbers you see is the PORT, the first part is the HOST
- Scroll down until you see Security
- Click on it and you will see the Password

# Encrypting the API and PASSWORD
- Create a .txt file in your program directory
- Paste and modify the following:
# .env
REDIS_HOST=(Insert here)

REDIS_PORT=(Insert here)

REDIS_DB=0(Insert here)

REDIS_PASSWORD=(Insert here)

WEATHER_API_KEY=(Insert here)
- Save the file using "Save as" then choose "All files" in "Save as type:"