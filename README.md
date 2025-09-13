# BTech3rdYear-Async-Safari-Python
  
## Installation
1. Clone the repository:
	 ```sh
	 git clone <repo-url>
	 cd BTech3rdYear-Async-Safari-Python
	 ```
2. Install dependencies:
	 ```sh
	 pip install -r requirements.txt
	 ```
3. Run the FastAPI app:
	 ```sh
	 uvicorn app.main:app --reload
	 ```

## Seeded Bugs
This project intentionally includes the following bugs for learning and debugging practice:

- **Blocking I/O in async route:**
	- Example: Using `time.sleep()` in an `async def` endpoint, which blocks the event loop.
- **Event-loop misuse:**
	- Example: Calling `loop.run_until_complete()` inside an async route, causing event loop conflicts.
- **Decorator side-effects:**
	- Example: Synchronous decorators that block or interfere with async execution.
- **Context-vars lost:**
	- Example: Context variables set before an `await` may be lost or not preserved after async operations.

Refer to the code and endpoints for examples of each bug. Fixes should be documented after resolving them.