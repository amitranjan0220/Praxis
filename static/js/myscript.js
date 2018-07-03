//service worker
if ('serviceWorker' in navigator) {
  window.addEventListener('load', function() {
    navigator.serviceWorker.register('/sw.js').then(function(registration) {
      // Registration was successful
      console.log('ServiceWorker registration successful with scope: ', registration.scope);
    }, function(err) {
      // registration failed :(
      console.log('ServiceWorker registration failed: ', err);
    });
  });
}


// nav slide drawer
function openNav() {
    document.getElementById("mySidenav").style.width = "330px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}
