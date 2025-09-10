# 🚀 Nginx Technical Cheat Sheet (Revision + Startup Ready)

---

## 🔹 1. Reverse Proxy

* Acts as **intermediary** between client ↔ backend.
* Benefits:

  * **Security** → hides backend IP.
  * **Centralization** → SSL/TLS termination, access control.
  * **Load Balancing** → distributes traffic.
* **Key Directive**:

  * `proxy_pass http://<backend-ip>:<port>;`
* **Config Example**:

  ```nginx
  location /api/ {
      proxy_pass http://192.168.1.10:3000;
  }
  ```

---

## 🔹 2. Caching

* **Purpose**: reduce backend load, improve latency.
* **Storage**: FS cache + metadata in shared memory.
* **Cache Key**: request URL (uniquely identifies cached response).
* **Expiration**: `inactive <time>` ; **Size limit**: `max_size <bytes>`.
* **Key Directives**:

  * `proxy_cache_path` → defines cache zone.
  * `proxy_cache` → enables caching in a location.
* **Config Example**:

  ```nginx
  proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m max_size=10g inactive=60m;
  location / {
      proxy_cache my_cache;
      proxy_pass http://my_backend;
  }
  ```

---

## 🔹 3. TLS Termination

* Offloads **SSL/TLS handshake + encryption/decryption** from app server.
* Steps:

  1. Client handshake with Nginx.
  2. Nginx decrypts → forwards HTTP to backend.
  3. Nginx re-encrypts response → client.
* **Key Directives**:

  * `listen 443 ssl;`
  * `ssl_certificate <crt>`
  * `ssl_certificate_key <key>`
* **Config Example**:

  ```nginx
  server {
      listen 443 ssl;
      ssl_certificate /etc/nginx/certs/app.crt;
      ssl_certificate_key /etc/nginx/certs/app.key;
      proxy_pass http://localhost:8000;
  }
  ```

---

## 🔹 4. Load Balancing

* **Upstream Block** → defines backend pool.
* **Algorithms**:

  * **Round Robin (default)**
  * **least\_conn** (lowest connections)
  * **ip\_hash** (sticky sessions).
* **Health Checks**: basic failure detection.
* **Config Example**:

  ```nginx
  upstream my_servers {
      server 192.168.1.10:8000;
      server 192.168.1.11:8000;
      server 192.168.1.12:8000;
  }
  location / {
      proxy_pass http://my_servers;
  }
  ```

---

## 🔹 5. Static File Serving

* **Minimal server block**:

  ```nginx
  server {
      listen 8080;
      root /var/www/static;
  }
  ```
* **Directives**:

  * `root` → appends URI path.
  * `alias` → replaces URI path.
* **try\_files** → file fallback mechanism.

  ```nginx
  location / {
      try_files $uri $uri/ =404;
  }
  ```

---

## 🔹 6. MIME Types

* **`mime.types`** maps extensions → MIME type.
* Example:

  ```nginx
  types {
      text/html  html;
      text/css   css;
      image/png  png;
      image/jpeg jpg jpeg;
      application/javascript js;
  }
  ```

---

## 🔹 7. Managing Nginx

* **Reload config gracefully**:

  ```bash
  nginx -s reload
  ```
* **Syntax check before reload**:

  ```bash
  nginx -t
  ```

---

## 🔹 8. Location Matching

* **Prefix match**: `location /api {}`
* **Regex match**: `location ~ \.php$ {}`
* **root vs alias**:

  * `root /base;` → `/fruits/page.html` → `/base/fruits/page.html`.
  * `alias /base;` → `/fruits/page.html` → `/base/page.html`.

---

## 🔹 9. Essential Directives Recap

* `proxy_pass` → reverse proxy.
* `proxy_cache_path`, `proxy_cache` → caching.
* `ssl_certificate`, `ssl_certificate_key` → TLS termination.
* `upstream` → load balancing pool.
* `root` / `alias` → static files.
* `try_files` → fallback routing.

---

⚡ **Startup/Interview Ready Pointers**:

* Always use **`nginx -t && nginx -s reload`** for safe updates.
* For scalability: combine **reverse proxy + caching + load balancing**.
* For production: **TLS termination** at Nginx + **WAF (modsecurity / rate-limiting)**.
* For microservices: Nginx can serve as **API gateway**.

---
