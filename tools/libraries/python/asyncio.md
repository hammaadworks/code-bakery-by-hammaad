Asynchronous Programming

Coroutine: pause and play execution
- await <downtime non_blocking request>
- return execution to the event loop 

Task Parallelism
await asyncio.gather(task, task)
