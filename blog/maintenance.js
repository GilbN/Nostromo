addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

/**
 * Respond to the request
 * @param {Request} request
 */
async function handleRequest(request) {

let modifiedHeaders = new Headers()
 
  modifiedHeaders.set('Content-Type', 'text/html')
  modifiedHeaders.append('Pragma', 'no-cache')

  return new Response(maintenancepage, {headers: modifiedHeaders})
}
let maintenancepage = `
 
<!doctype html>
<title>Site Maintenance</title>
<style>
  body { 
        text-align: center; 
        padding: 150px; 
        background: url('https://raw.githubusercontent.com/gilbN/Nostromo/master/blog/Senja-death-star.jpg') no-repeat center center fixed; 
        background-size: cover;
        -webkit-background-size: cover;
        -moz-background-size: cover;
        -o-background-size: cover;
      }
 
    .content {
        background-color: rgba(255, 255, 255, 0.75); 
        background-size: 100%;      
        color: inherit;
        padding-top: 1px;
        padding-bottom: 10px;
        padding-left: 100px;
        padding-right: 100px;
        border-radius: 15px;        
    }
 
  h1 { font-size: 40pt;}
  body { font: 20px Helvetica, sans-serif; color: #333; }
  article { display: block; text-align: left; width: 75%; margin: 0 auto; }
  a:hover { color: #333; text-decoration: none; }
</style>
 
<article> 
  <div class="background">
    <div class="content">
      <h1>We&rsquo;ll be right back!</h1>
        <p>We're very sorry for the inconvenience but we&rsquo;re performing maintenance.</p>
        <p>Maintenance is performed between <strong>3AM</strong> to <strong>4AM</strong> <strong>UTC</strong>.</p>
        <p>Please check back soon...</p>
        <p>You can use <span style="color: #000000;"><strong><a style="color: #000000;" href="https://cachedview.com/">https://cachedview.com/</a></strong></span> in the mean time.</p>
        <p>&mdash; <B>GilbN</B></p>
    </div>
  </div>
</article>
`
