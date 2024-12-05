# simple-datalogger
Simple data logger


# Server side


## Get the code
- Get the IP from this server.
- Git clone this repo in local PC or AWS EC2 client.

```bash
git clone https://github.com/jerivasuaq/simple-datalogger
```

- Go to `server-src` folder.

## Install requirements

``` bash
sudo apt install python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run server side

``` bash
uvicorn main:app --reload --host 0.0.0.0
```


# Client side


## Get the code

- Git clone this repo in local PC or AWS EC2 client.

```bash
git clone https://github.com/jerivasuaq/simple-datalogger
```

- Go to `rasp-src` folder.
- Set the `SERVER_IP` value in the `.env` file.

## Make sure client can reach the Server ip

```bash
ping SERVER_IP
```

## Install requirements

``` bash
sudo apt install python3-venv python3-requests
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run client side code

```
python main.py
```


# Check the results

Go to 