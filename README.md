### lru_cache decorator demo

lru = `Least Recently Used`

It works best when the most recent calls are the best predictors of upcoming calls.

`lru_cache` takes a parameter called `maxsize` - this limits the cache size. If `maxsize` is set
to `None`, the cache will have no limit. LRU performs best when the `maxsize` is a power of two(2)

This can almost be used anywhere, exception is functions with side-effect, functions that need to create
distinct mutable objects, or impure functions such as `time()` or `random()`

demoed with a simple Fibonacci Rescurion function - see [fib_nocache.py](fib_nocache.py)

Example output:

