{% load static %}

var CACHE_NAME = 'static-v1';
var urlsToCache = [
  '/',
  '/static/css/mystyle.css',
  '/static/css/ionicons.min.css',
  '/static/js/myscript.js',
  '/static/js/jquery-3.3.1.min.js',
  'offline/'
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});


self.addEventListener('activate', function(event) {
  console.log('[Service Worker] Activating Service Worker ....', event);
  event.waitUntil(
    caches.keys()
      .then(function(keyList) {
        return Promise.all(keyList.map(function(key) {
          if (key !== CACHE_NAME) {
            console.log('[Service Worker] Removing old cache.', key);
            return caches.delete(key);
          }
        }));
      })
  );
  return self.clients.claim();
});

self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request)
      .then(function(response) {
        if (response) {
          return response;
        } else {
          return fetch(event.request)
            // .then(function(res) {
            //   return caches.open(CACHE_DYNAMIC_NAME)
            //     .then(function(cache) {
            //       //cache.put(event.request.url, res.clone());
            //       //return res;
            //     })
            // })
            .catch(function(err) {
              return caches.open(CACHE_NAME)
                .then(function(cache) {
                  return cache.match({% url 'offline' %});
                });
            });
        }
      })
  );
});
