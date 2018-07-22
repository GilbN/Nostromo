
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
