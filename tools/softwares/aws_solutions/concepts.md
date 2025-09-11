region 
availability zone: 
- set of 3+ disaster isolated clusters together form a region
- connected via high bandwidth low latency network
edge locations

aws global services
- WAF (firewall)
- CloudFront (CDN)
- Route 53 (DNS)
- IAM
others are region scoped: region service search list

how to choose AWS region
1. Latency: choose the most geographically closest to your users
2. Cost: choose the cheapest region for the given functionality
3. Compliance: data must reside in the country of origin
4. Functionality: some regions might have advanced features
---
services
# IAM 
1. Identity and Access Management
   - Global Service
   - Groups can only contain users not other groups. Same as WhatsApp chat groups (only users)
   - Root Account only used for account creation and not to be used or shared
   - User -- 0...* -- Group
   - Create an IAM user - assign permission or group - give group permissions - tags
   - How to distinguish Root/IAM user from UI
       - Root only has Account ID
       - IAM has account ID and IAM username
   - Multi session logins:
       - allows to login and use 2 different aws accounts from the same browser window.
       - in the early days we used to open another account in incognito mode for the same.
2. Policies
- Policy: A JSON document for grant permissions to users to use authorised operations (services).
- Policy can be 
      - Group Policy: assigned to groups
      - Inline Policy: assigned to individual users
- Least Privilege Principle
- AdminstrationAccess for admin group
- An IAM policy document consists of
  - Version
  - ID
  - Statement
    - SID
    - Effect: allow/deny
    - Principal: users to whom the policy applies
    - Action: the list of APIs
    - Resource: the service that contains the action
    - Condition: optional