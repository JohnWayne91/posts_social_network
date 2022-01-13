import json
import requests
from faker import Faker
from random import randint, choice


class Bot:
    user_data = []
    created_users_id = []
    created_posts_id = []

    def __init__(self, users_amount, max_posts_amount, max_likes_amount):
        self.users_amount = users_amount
        self.max_posts_amount = max_posts_amount
        self.max_likes_amount = max_likes_amount
        self.faker = Faker()

    def start_bot(self):
        self.create_users_data()
        self.sign_up_users()
        self.create_posts()
        self.like_posts()

    def create_users_data(self):
        for i in range(self.users_amount):
            user = {
                'username': self.faker.first_name() + self.faker.last_name(),
                'email': self.faker.email(),
                'password': self.faker.pystr(min_chars=15, max_chars=25)
            }
            self.user_data.append(user)

    def sign_up_users(self):
        for user in self.user_data:
            r = requests.post('http://127.0.0.1:8000/auth/users/', data=user)
            self.created_users_id.append(json.loads(r.text)['id'])

    def create_posts(self):
        posts_per_user = randint(0, self.max_posts_amount)
        for id in self.created_users_id:
            for j in range(posts_per_user):
                r = requests.post(
                    'http://127.0.0.1:8000/api/posts/', data={'user': f'{id}',
                                                              'body': self.faker.paragraph(6),
                                                              'title': self.faker.sentence()
                                                              }
                )
                self.created_posts_id.append(json.loads(r.text)['id'])

    def like_posts(self):
        likes_per_user = randint(0, self.max_likes_amount)
        for id in self.created_users_id:
            for j in range(likes_per_user):
                requests.post('http://127.0.0.1:8000/api/likes/',
                              data={'user': id, 'post': {choice(self.created_posts_id)}})

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
    bot.start_bot()