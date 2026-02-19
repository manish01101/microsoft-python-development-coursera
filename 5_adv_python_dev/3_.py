"""
Asyncio event loop
awaitable: it's an object that your coroutine can pause for while it's waiting for a result.

awaitable types
- coroutines => are functions defined with “async def” that can pause and resume their execution.
- task => Think of these as wrapped-up coroutines that are managed by the event loop. They allow you to schedule and run coroutines concurrently.
- Futures => These are special objects that represent the eventual result of an asynchronous operation. They act as placeholders for a value that will be available in the future
"""
