# rocketchat-postMsg-cmd

[![tests](https://github.com/ownik/rocketchat_postmessage_cli/actions/workflows/tests.yml/badge.svg)](https://github.com/ownik/rocketchat_postmessage_cli/actions/workflows/tests.yml)

Simple command line utility for sending messages to Rocket.Chat.

### Usage
```
usage: main.py [-h] --user USER --password PASSWORD [--alias ALIAS] url message channel

positional arguments:
  url                  Rocket.Chat server url
  message              Message to post
  channel              Channel to post message

optional arguments:
  -h, --help           show this help message and exit
  --user USER          Rocket.Chat user name
  --password PASSWORD  Rocket.Chat user password
  --alias ALIAS        Rocket.Chat user alias
```

### Example
```
rocketchat_postmessage_cli --user user --password pass --alias Farnsworth https://demo.rocket.chat "good news everyone!" General
```
