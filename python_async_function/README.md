# Python Async Functions

## Async and Await Syntax

Python's `async`/`await` syntax (introduced in Python 3.5) allows writing **asynchronous**, non-blocking code that looks and reads like synchronous code.

- `async def` declares a **coroutine function**
- `await` suspends the coroutine until the awaited result is ready, allowing other tasks to run in the meantime

```python
import asyncio

async def greet(name: str) -> str:
    await asyncio.sleep(1)  # non-blocking pause
    return f"Hello, {name}!"

async def main():
    result = await greet("Alice")
    print(result)
```

> A coroutine alone does nothing — it must be **awaited** or scheduled in an event loop.

---

## Executing an Async Program with asyncio

Use `asyncio.run()` to launch the top-level coroutine and manage the event loop:

```python
import asyncio

async def main():
    print("Start")
    await asyncio.sleep(1)
    print("End")

asyncio.run(main())
```

`asyncio.run()` creates a new event loop, runs the coroutine to completion, then closes the loop. It should be called **once** at the entry point of your program.

---

## Running Concurrent Coroutines

### `asyncio.gather()`

Run multiple coroutines **concurrently** and wait for all of them:

```python
import asyncio

async def task(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name} done"

async def main():
    results = await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 3),
    )
    print(results)  # ['A done', 'B done', 'C done']

asyncio.run(main())
# Total time ~3s instead of 6s
```

### `asyncio.wait()`

Similar to `gather` but returns sets of done/pending tasks, giving more control:

```python
import asyncio

async def main():
    coroutines = [task("A", 2), task("B", 1)]
    done, pending = await asyncio.wait(
        [asyncio.create_task(c) for c in coroutines]
    )
    for t in done:
        print(t.result())

asyncio.run(main())
```

---

## Creating asyncio Tasks

`asyncio.create_task()` schedules a coroutine to run **immediately** in the background without waiting for it:

```python
import asyncio

async def background_job(n: int) -> int:
    await asyncio.sleep(n)
    return n * 2

async def main():
    # Schedule tasks without blocking
    task1 = asyncio.create_task(background_job(2))
    task2 = asyncio.create_task(background_job(1))

    print("Tasks are running in background...")

    result1 = await task1
    result2 = await task2

    print(result1, result2)  # 4 2

asyncio.run(main())
```

### Task vs Coroutine

| | Coroutine | Task |
|---|---|---|
| Created with | `async def` | `asyncio.create_task()` |
| Scheduled immediately | No | Yes |
| Can be awaited | Yes | Yes |
| Can be cancelled | No | Yes (`task.cancel()`) |

---

## Using the `random` Module

The `random` module is commonly used in async programs to simulate variable delays or random values.

### Key functions

```python
import random

random.random()            # float in [0.0, 1.0)
random.uniform(1, 10)      # float in [1.0, 10.0]
random.randint(1, 10)      # int in [1, 10] inclusive
random.choice([1, 2, 3])   # random element from a list
random.shuffle(my_list)    # shuffle list in place
```

### Example: random delay in a coroutine

```python
import asyncio
import random

async def random_delay(max_delay: int) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def main():
    results = await asyncio.gather(*[random_delay(10) for _ in range(5)])
    for i, delay in enumerate(results):
        print(f"Task {i}: waited {delay:.2f}s")

asyncio.run(main())
```

> For cryptographically secure random numbers, use the `secrets` module instead of `random`.

---

## Summary

| Concept | Tool |
|---------|------|
| Declare a coroutine | `async def` |
| Pause and wait | `await` |
| Run the event loop | `asyncio.run()` |
| Run coroutines concurrently | `asyncio.gather()` |
| Schedule a background task | `asyncio.create_task()` |
| Random float `[0, 1)` | `random.random()` |
| Random float in range | `random.uniform(a, b)` |
