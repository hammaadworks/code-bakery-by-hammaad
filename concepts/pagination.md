there are 2 types of pagination you can implement for your apis
before you do that you need to understand 
1. Limit and offset pagination
+ uses limit and offset in the query
+ supports random access
+ it's stateless, meaning users can navigate to any page
- it's slow as the DB has to get all the rows and throw away the offset records
- for deep pages we need to perform partial joins
+ there can be a drift in records for indeterministic queries
```sql
Select * from user where 

```

2. cursor based pagination
+ Holds the pointer for the next record
+ SQL has to curated to cater the next record pointer
+ Useful for infinite scrolling pagination where we only need the pointer to the next record
+ supports sequential access
