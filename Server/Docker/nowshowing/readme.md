
# Custom Now Showing frontpage

https://github.com/ninthwalker/NowShowing

In the `style.css` file add the code below to make it look like the blur theme.

Add it in the #Welcome section (Line 89)

I've added a new nowshowing logo that I think looks alot nicer. 
Replace the one that is in the `/img` folder


```
/*--------------------------------------------------------------
# Welcome
--------------------------------------------------------------*/
#hero {
  display: table;
  width: 100%;
  height: 100vh;

/* Enter background image for welcome section below */
    background-image: url(https://raw.githubusercontent.com/leram84/layer.Cake/master/Resources/blur-noise.png), url(https://raw.githubusercontent.com/leram84/layer.Cake/master/Resources/blur-light.png);
    background-repeat: repeat, no-repeat;
    background-attachment: fixed, fixed;
    background-position: center center, center center;
    background-size: auto, cover;
    -webkit-background-size: auto, cover;
}
```
## Email logo

Edit the `advanced.yaml` and add https://raw.githubusercontent.com/gilbN/Nostromo/master/Server/Docker/nowshowing/nowshowing.png instead of the imgur link. 
```
email:
  title: 'New This Week'
  image: 'https://raw.githubusercontent.com/gilbN/Nostromo/master/Server/Docker/nowshowing/nowshowing.png'
  footer: 'Thanks for watching!'
  language: 'en'
  ```

![](nowshowingblur.png)
