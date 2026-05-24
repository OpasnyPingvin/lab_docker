##Часть 1

```$ sudo docker build -t flask-lab-web .```
[Вывод](https://gist.github.com/OpasnyPingvin/598064eed0d0ceb2b2300b5e856261fc)
```$ sudo docker run -d -p 5000:5000 --name web_standalone flask-lab-web
92c8644039366e8b9a4d511792f8a6343caa264b9fc9934d32de205c392e5f89```

```$ sudo docker cp README.md web_standalone:/home/
Successfully copied 6.14kB to web_standalone:/home/```

```$ sudo docker exec -it web_standalone sh
_#_ ls -la /home/ 
total 16
drwxr-xr-x 1 root root 4096 May 24 11:58 .
drwxr-xr-x 1 root root 4096 May 24 11:58 ..
-rw-rw-r-- 1 1001 1001 4441 May 24 11:51 README.md
_#_ exit
```
```
$ sudo docker stop web_standalone
web_standalone```
```$ sudo docker rm web_standalone
web_standalone```

##Часть 2

```$ sudo docker compose up --build```
[Вывод](https://gist.github.com/OpasnyPingvin/a1a746278e5161dd5732abb4a076631c)
