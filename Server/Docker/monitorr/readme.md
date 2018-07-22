
# Unraid installation using template

## Add custom template repository

Go to the Docker tab and scroll down to the bottom of the page.

Add `https://github.com/Monitorr/Monitorr/tree/unraid/template` in the `Template repositories box`

Click `Save`

![](https://github.com/gilbN/Nostromo/blob/master/Server/Docker/monitorr/template%20repo.png)


## Add the container

At the bottom of the Docker tab page click on `Add Container` and select the Monitorr template.

![](https://github.com/gilbN/Nostromo/blob/master/Server/Docker/monitorr/template.png)

* Set your `Host Port` (Has to be something else than 80 as unraid uses that)

* Set your `Host Path` for the configuration files.

Click `Apply`


# Custom CSS for Organizr
> This theme will mess with your Monitorr base theme. And it will hide the settings button. Go to /monitorr/settings.php for settings.

> It is created purely for use with Organizr.

Add this in the custom css box:
```css
@import "https://rawgit.com/gilbN/Nostromo/master/Server/Docker/monitorr/custom-organizr-css.css";
```
And add this in custom HTML in Organizr:
```css
<div style="overflow:hidden; height:260px">
<embed style="height:calc(100% + 50px)" width='100%' src='https://domain.com/monitorr/index.min.php' />
</div>
```
## Subfilter
As this theme will change the base theme, you can get around that by using subfilter in Nginx.
Create another reverse proxy for monitorr and add this:
```nginx
		proxy_set_header Accept-Encoding "";
		sub_filter
		'</head>'
		'<link rel="stylesheet" type="text/css" href="https://rawgit.com/gilbN/Nostromo/master/Server/Docker/monitorr/custom-organizr-css.css">
		</head>';
		sub_filter_once on;
```
Here is a complete example:
```nginx
#MONITORR CONTAINER 

# REDIRECT HTTP TRAFFIC TO https://[domain.com]
server {
 	listen 80;
 	server_name monitorr.domain.com; 
 	return 301 https://$server_name$request_uri;
}

server {  
    listen 443 ssl http2;
    server_name monitorr.domain.com;

	#SSL settings
	include /config/nginx/ssl.conf
		
location / {
    proxy_pass http://192.168.1.2:8701;
    include /config/nginx/proxy.conf;
		proxy_set_header Accept-Encoding "";
		sub_filter
		'</head>'
		'<link rel="stylesheet" type="text/css" href="https://rawgit.com/gilbN/Nostromo/master/Server/Docker/monitorr/custom-organizr-css.css">
		</head>';
		sub_filter_once on;
  }
}
```

![](https://i.imgur.com/kX4Qcsj.jpg)

![](https://i.imgur.com/O2fUyTz.jpg)

![](https://i.imgur.com/sJRELOP.jpg)
