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
