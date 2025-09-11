# System Design Notes

These structured notes aim to provide a high-level overview of essential system design components, evaluation criteria, infrastructure options, and best practices.

Sources include:
1. Interview Ready GKCS
2. 

---

# Day 1 - 010625

## 🧠 Evaluation Criteria for System Design

1. **Simplicity**  
   - Easy to understand and maintain.
   - Avoid overengineering.

2. **Fidelity**  
   - Accuracy and faithfulness to business logic.
   - Ensures expected outcomes under real-world usage.

3. **Cost Effectiveness**  
   - Evaluate ROI.
   - Choose solutions that provide optimal balance between performance and cost.

---

### 📦 Example: E-Commerce T-Shirt Company

- **Use Existing Sources** *(Don't Repeat Yourself – DRY)*:
  - Sell via platforms like Amazon, Myntra.
  - Use Shopify for hosted store solution.

- **Technical Wrappers**:
  - Create API contracts to integrate and manage external sources efficiently.

---

## 🚀 Deployment Server Options

### 1. Local Machine (On-Premise)
- ✅ Low cost  
- ❌ Low simplicity  
- ❌ Manual scaling, maintenance overhead  

### 2. Cloud Server (IaaS)
- ✅ Cost-effective for scale  
- ✅ More choices, greater customization  
- ❌ Manual deployment  
- ❌ Manual recovery in case of crash  

### 3. Serverless (e.g. AWS Lambda, Vercel, Cloudflare Workers)
- ✅ No manual deployment (CI/CD from GitHub)  
- ✅ Automatic scaling  
- ✅ High abstraction and simplicity  
- ❌ Higher cost  
- ❌ May have latency or responsiveness issues  

---

## 🗂️ Storing Static Content

### 1. Content Delivery Network (CDN)
- Geographically distributed edge servers  
- Used for caching:
  - Images, videos, files, static HTML pages  
- Examples: **Akamai, CloudFront**  
- Consistency is a challenge (eventual consistency)
- CDN watches a folder for updates and spreads the changes to it's edege servers.
- Commonly backed by:
  - AWS S3
  - Azure Blob Storage
  - Hadoop FS
  - Ceph  

### 2. Server or Serverless Hosting
- Better suited for dynamic content  
- Scaling is complex and configuration-intensive  

---

## 🌐 Domain Name System (DNS)

- Maps domain name to server IPs  
- Process flow:
    - Browser ➝ Router ➝ ISP ➝ DNS ➝ IP (CDN/server) ➝ Webpage Response
- DNS caching in browsers improves performance  
- Useful when redirecting domains (e.g., Shopify domain to custom domain)

---

## 🐞 Debugging & Monitoring

### 1. Logging and Monitoring
- Use **CloudWatch**, custom logs with regex parsing  
- Centralized error collection and alerting  

### 2. Observability and Anomaly Detection
- Real-time dashboards:
- **Google Analytics**
- **PowerBI**
- **Tableau**

---

## 🔐 Single Point of Failure (SPOF)

### 1. Redundancy
- Identify critical paths and dependencies  
- Redundant systems minimize downtime  
- Be cautious with external services; they may fail  
- Higher cost and complexity, but increased reliability  
- Cloud platforms offer built-in redundancy  

### 2. Graceful Degradation
- Predefined error messages  
- Inform users of partial failures without crashing  
- Example:  
- If payment service is down, still allow browsing and cart usage  

---

## ✅ Summary

| Component              | Key Takeaways                                                                 |
|------------------------|-------------------------------------------------------------------------------|
| **Evaluation**         | Prioritize simplicity, correctness, and cost balance                         |
| **Deployment**         | Choose between local, cloud, or serverless depending on needs                |
| **Static Content**     | CDN is best for performance; choose correct storage backend                  |
| **DNS**                | Understand routing from domain to content delivery                           |
| **Debugging**          | Use monitoring tools and dashboards for effective issue resolution           |
| **SPOF Handling**      | Build redundancy, and prepare systems to fail gracefully                     |

---

