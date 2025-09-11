# Caching Notes

Caching is a technique to reduce redundant computation, database queries, and network overhead by reusing previously retrieved or computed data.  

---

## Types of Caching

### 1. Application-Level Cache
- Cache is maintained and served directly from the application layer.
- Typically stored in memory (e.g., Redis, Memcached, local in-process cache).
- Best for speeding up expensive computations or frequently accessed data.

### 2. Request-Level Cache
- Especially useful for **read-heavy** `GET` requests with mostly static or slowly-changing data.
- Commonly applied to **paginated requests** (e.g., `/items?page=2`), since repeated queries often return the same results.
- Often implemented with HTTP caching headers (`Cache-Control`, `Expires`).

### 3. Conditional Caching
- Uses **HTTP headers** to validate freshness of data:
  - `ETag`: Entity Tag (typically a hash of the resource’s `updated_at` timestamp or version).
  - `If-None-Match`: sent by the client to check if its cached resource matches the server’s version.
- Workflow:
  1. Client stores the ETag from the last response.
  2. On the next request, client sends it in `If-None-Match`.
  3. Server checks current resource version and compares:
     - If the ETags match → return **`304 Not Modified`** (no payload).
     - If they differ → fetch new data and return it with a fresh ETag.
- Benefit: Saves **bandwidth** and **response time** when data hasn’t changed.

---

## Cache Invalidation Strategies

### 1. Write-Through
- Write synchronously to **both the cache and the database**.
- Keeps cache and DB always in sync.
- Good for **read-heavy** workloads where cached data must always be fresh.

### 2. Write-Back (a.k.a. Write-Behind)
- Write to the **cache first**, then update the DB asynchronously in the background.
- Reduces write latency and load on the DB.
- Risk: possible data loss if the cache fails before flushing to DB.
- Good for **write-heavy** workloads.

### 3. TTL (Time-To-Live)
- Cached data expires automatically after a set duration.
- Prevents stale data from living forever.
- Simple, but may return slightly outdated data between updates.

---

## Layers of Caching

Caching can exist at multiple levels in a system, forming a **caching hierarchy**:

1. **Browser Cache**  
   - Stores static assets (images, CSS, JS) or API responses locally on the client.  
   - Controlled with headers like `Cache-Control` and `ETag`.

2. **CDN (Content Delivery Network) Cache**  
   - Distributes cached content closer to users geographically.  
   - Reduces latency and load on origin servers.

3. **In-Memory Cache**  
   - Server-side caches like **Redis** or **Memcached**.  
   - Extremely fast (RAM-level speed), used for API responses, session data, query results.

4. **Database Cache**  
   - Query-level caching mechanisms (e.g., Postgres materialized views, MySQL query cache).  
   - Often a fallback when higher-level caches miss.

---

### Key Insight
Caching is all about trade-offs: freshness vs. performance, consistency vs. speed.  
The right strategy depends on whether your workload is **read-heavy** or **write-heavy**, and how much staleness your users can tolerate.
