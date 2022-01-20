import json
import requests
from faker import Faker
from random import randint, choice


class Bot:
    __user_data = []
    created_posts_id = []

    def __init__(self, users_amount, max_posts_amount, max_likes_amount):
        self.users_amount = users_amount
        self.max_posts_amount = max_posts_amount
        self.max_likes_amount = max_likes_amount
        self.faker = Faker()

    def run(self):
        self.__create_users_data()
        self.__sign_up_users()
        self.__create_posts()
        self.__like_posts()

    def __create_users_data(self):
        for i in range(self.users_amount):
            user = {
                'username': self.faker.first_name() + self.faker.last_name(),
                'email': self.faker.email(),
                'password': self.faker.pystr(min_chars=15, max_chars=25)
            }
            self.__user_data.append(user)

    def __sign_up_users(self):
        for user in self.__user_data:
            r = requests.post('http://127.0.0.1:8000/api/sign-up/', data=user)
            user['id'] = json.loads(r.text)['id']

    def __create_posts(self):
        url = 'http://127.0.0.1:8000/api/posts/'
        posts_per_user = randint(0, self.max_posts_amount)
        for user in self.__user_data:
            headers = self.get_headers_with_jwt(user['username'], user['password'])
            for j in range(posts_per_user):
                r = requests.post(
                    url=url,
                    data={
                        'user': user['id'],
                        'body': self.faker.paragraph(6),
                        'title': self.faker.sentence()
                    },
                    headers=headers
                )
                self.created_posts_id.append(json.loads(r.text)['id'])

    def __like_posts(self):
        url = 'http://127.0.0.1:8000/api/likes/'
        likes_per_user = randint(0, self.max_likes_amount)
        for user in self.__user_data:
            headers = self.get_headers_with_jwt(user['username'], user['password'])
            for j in range(likes_per_user):
                requests.post(url=url,
                              data={'user': user['id'], 'post': {choice(self.created_posts_id)}},
                              headers=headers)

    @staticmethod
    def get_headers_with_jwt(username, password):
        r = requests.post('http://127.0.0.1:8000/api/token/', data={'username': username, 'password': password})
        jwt = json.loads(r.text)
        headers = {
            "Authorization": f"Bearer {jwt['access']}",
        }
        return headers

    @classmethod
    def bot_from_config(cls):
        with open("bot_config.json", "r") as conf_file:
            config = json.load(conf_file)

        users_amount = int(config["NUMBER_OF_USERS"])
        max_posts_amount = int(config["MAX_POST_PER_USER"])
        max_likes_amount = int(config["MAX_LIKE_PER_USER"])
        bot = Bot(users_amount=users_amount, max_posts_amount=max_posts_amount, max_likes_amount=max_likes_amount)

        return bot


if __name__ == "__main__":
    bot = Bot.bot_from_config()
    bot.run()

