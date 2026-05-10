# Python Actorization

## Install the Apify SDK

```bash
pip install apify
```

## Wrap Main Function with Actor Context Manager

```python
import asyncio
from apify import Actor

async def main() -> None:
    async with Actor:
        # ============================================
        # Your existing code goes here
        # ============================================

        # Example: Get input from Apify Console or API
        actor_input = await Actor.get_input()
        print(f'Input