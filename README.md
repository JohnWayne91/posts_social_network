There are two projects in this repo: 
1. Posts social network - API for users registration, creating posts and liking them.
2. Bot wich reads config file and makes activity on Posts social network (signing up users, creating random amount of posts and randomly liking them)
___

For running Posts social network clone this repo, go to directory with docker-compose.yml and run the command below:

docker-compose up -d && docker exec -i posts_social_network-web python manage.py migrate

You can find postman collection for API in postman_collections.json
___

For running bot go to directory with bot.py and run pip install requests Faker , after installation is complete, you can run bot from cli like below:

python bot.py

in this case bot running using bot_config.json, you can change the parameters of this file manually.

Or you can run bot with options:

python bot.py --users_amount 5 --max_posts_amount 5 --max_likes_amount 5