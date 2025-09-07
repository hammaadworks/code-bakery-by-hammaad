# Operating System Concepts – Notes

## Processes
- A **process** is a program/app getting executed by the processor.
- Processes are isolated from each other.
- Require **heavy context switching** (saving and restoring state).

## Threads
- A **thread** is the unit of execution within a process.
- Threads share the process memory, but each has:
  - Its own registers
  - Its own stack
- A malfunctioning thread can crash the entire process.

---

## Synchronous
- `async def` + **blocking request**

---

## Parallelism (Multiprocessing)
- Multiple processes get executed on different CPU cores.
- Best for **CPU-bound tasks** (e.g., image processing, file processing).
- Types of parallelism:
  - **Data parallelism**: Split data across cores.  
    Example: Finding primes in a long list → split list into 4 parts → 4 cores work in parallel.
  - **Task parallelism**: Split tasks across cores.  
    Example:  
    - Core 1 → find min  
    - Core 2 → find max  
    - Core 3 → compute sum  
- Pattern: `def` + **blocking request**
- IPC is costly

---

## Concurrency (Multithreading)
- Multiple threads of a process execute via switching.
- Multitasking is when multiple process are juggled by CPU
- Classic example: **Apache server**. (Multithreading)
- Controlled by the OS → CPU switches between threads.
- Limited by the **GIL (Global Interpreter Lock)** in some languages like Python.
- Useful for **I/O-bound tasks** (e.g., file or DB read → blocking call).
- Traits:
  - Higher memory usage
  - CPU is idle during I/O, so it switches to other threads
  - Enables **multitasking**
- Examples:
  - **Chrome browser tabs** (Multitasking)
  - **Nginx event loop**
- Pattern: `async def` + **non-blocking request**
- Threads are not isolated so one malfunctioning thread can bring down the process
---

## Key Distinction
> **Concurrency**: Dealing with lots of things at once  
> **Parallelism**: Doing lots of things at once  

Visual analogy:  
- Concurrency → **Striped line** (time-slicing tasks)  
- Parallelism → **Parallel lines** (tasks literally side by side)
