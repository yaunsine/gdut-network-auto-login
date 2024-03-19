# Auto-Login-Gdut

1. A python program. To solve auto-logout problem on gdut wifi every day. You know, for convinient. 

1. Remember to modify the `config.ini`, which refer to your personal account.

1. Remember to download the `chromedriver.exe` into directory `./chromedriver-win64/`, make sure all of enviornment is set. Good Luck! 

1. In addition, you could make use of [nssm.cc](https://nssm.cc/download) to create your service. And it could be run all the time. 

How to install windows service?

After download `nssm.zip`，unzip it. And come into directory `x64/`, run the commnad line as follow:

```
nssm.exe install [service-name]
```

Filled with all your service info, save it and start the service.

<img src="https://gitee.com/lsir34567/drawing-bed/raw/master/github/imgs/wx_20240319104038.png"  width="200px"/>

Fig. The interface of gdut-login.


