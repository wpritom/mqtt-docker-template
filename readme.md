# How to Use

```
docker compose up
```

Create a password file `passwd` inside `mosquitto` directory. You can set more than 1 passoword.

```
username:password
```

Update the password file. 

```
docker exec mosquitto mosquitto_passwd -U /etc/mosquitto/passwd
```

If password is not updated then just restart the container.

# How to add New Username
Support the container name is `mosquitto`
```
docker exec mosquitto mosquitto_passwd -b /etc/mosquitto/passwd new_user password 
```

It will add a new password. After that we have to send SIGUP signal to the container.

```
docker kill --signal=SIGHUP mosquitto
```
This will restart the configuration without interrupting the existing connections. ( [source](https://stackoverflow.com/a/42246537/8049220) )