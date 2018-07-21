
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


# Custom CSS
> This theme will mess with your Monitorr base theme. And it will hide the settings button. Go to /monitorr/settings.php for settings.

> It is created purely for use with Organizr.

Add this in the custom css box:
```css
@import "https://rawgit.com/gilbN/Nostromo/master/Server/Docker/monitorr/custom-organizr-css.css";
```
![](https://i.imgur.com/kX4Qcsj.jpg)

![](https://i.imgur.com/O2fUyTz.jpg)

![](https://i.imgur.com/sJRELOP.jpg)

![](https://i.imgur.com/EB6YZZG.png)
