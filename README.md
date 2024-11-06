<h1 align="center">
    <samp>Telegram Chanal Copy</samp>
</h1>

<p align="center">
    A script to copy all content from a Telegram channel.  <br />
    It retrieves and saves all messages, including text, images, and links, from a specified Telegram channel for easy backup and access.
</p>

<p align="center">
    <img alt="GitHub License" src="https://img.shields.io/github/license/Warnigo/telegram-chanal-copy?style=flat&label=license&labelColor=%23ffffff&color=%23454545">
</p>

## Telethon Channel Clone

- Clone any telegram channel or group (public & private both)
- You must have member of source channel or group

### Clone this repository

```sh
git clone https://github.com/Warnigo/telegram-chanal-copy.git
```

```sh
cd telegram-chanal-copy
```

### Edit [config.py](./config.py) file before use

- `API_ID` and `API_HASH` - Get those from [my.telegram.org](http://my.telegram.org/)
- `PHONE_NUMBER` - Give phone number with country code (ex. +998901234567)
- `NAME` - Give any name what you want
- `SRC_CHAT_ID` and `DEST_CHAT_ID` - Get those from [@userinfobot](https://telegram.dog/userinfobot)

### Create Virtual Environment

- #### Windows

```sh
python -m venv myenv
```

- #### MacOS and Linux

```sh
python3 -m venv myenv
```

### Activate Virtual Environment

- #### Windows

```sh
.\myenv\Scripts\activate
```

- #### MacOS and Linux

```sh
source myenv/bin/activate
```

### Install module [telethon](https://pypi.org/project/Telethon/)

- #### Windows

```sh
pip install telethon
```

- #### MacOS and Linux

```sh
pip3 install telethon
```

### Run script

- #### Windows

```sh
python bot.py
```

- #### MacOS and Linux

```sh
python3 bot.py
```

> [!NOTE]
> If you want to exit the virtual environment `(venv)`, you can deactivate it by using the following command:

```bash
deactivate
```
