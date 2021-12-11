import sys
import argparse
from rocketchat_API.rocketchat import RocketChat

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Rocket.Chat server url')
    parser.add_argument('message', help='Message to post')
    parser.add_argument('channel', help='Channel to post message')
    parser.add_argument('--user', help='Rocket.Chat user name')
    parser.add_argument('--password', help='Rocket.Chat user password')
    parser.add_argument('--alias', help='Rocket.Chat user alias')

    args = parser.parse_args()

    rocket = RocketChat(args.user, args.password, server_url=args.url)

    result = rocket.chat_post_message(args.message, channel=args.channel, alias=args.alias)
    if not result.ok:
        print(result)
        sys.exit(1)

    sys.exit(0)