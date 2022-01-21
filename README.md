There are two projects in this repo: 
1. Posts social network - API for users registration, creating posts and liking them.
2. Bot wich reads config file and makes activity on Posts social newtwork (Signin up users, creating random amount of posts and randomly liking them)

For running Posts social network clone this repo, go to directory with docker-compose and run the command below:

docker-compose up -d && docker exec -i posts_social_network-web python manage.py migrate
