# Telethon Channel Clone
- Clone any telegram channel or group (public & private both 😉)
- You must have member of source channel or group

## Quick Start 🔎
### Clone this repository
```sh
git clone https://github.com/Warnigo/channeler.git
```
```sh
cd channeler
```


### Edit [config.py](./config.py) file before use
`API_ID` and `API_HASH` - Get those from [my.telegram.org](http://my.telegram.org/)

`PHONE_NUMBER` - Give phone number with country code (ex. +998901234567)

`NAME` - Give any name what you want

`SRC_CHAT_ID` and `DEST_CHAT_ID` - Get those from [@userinfobot](https://telegram.dog/userinfobot)
(forward any message from those channel or group to [@userinfobot](https://telegram.dog/userinfobot))

### Create Virtual Environment
- #### Windows
```sh
python -m venv myenv
```
- #### macOS and Linux
```sh
python3 -m venv myenv
```

### Activate Virtual Environment
- #### Windows
```sh
.\myenv\Scripts\activate
```
- #### macOS and Linux
```sh
source myenv/bin/activate
```

### Install module [telethon](https://pypi.org/project/Telethon/)
- #### Windows
```sh
pip install telethon
```
- #### macOS and Linux
```sh
pip3 install telethon
```

### Run script
- #### Windows
```sh
python bot.py
```
- #### macOS and Linux
```sh
python3 bot.py
```
