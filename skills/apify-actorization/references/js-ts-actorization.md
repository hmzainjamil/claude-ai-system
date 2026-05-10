# JavaScript/TypeScript Actorization

## Install the Apify SDK

```bash
npm install apify
```

## Wrap Main Code with Actor Lifecycle

```javascript
import { Actor } from 'apify';

// Initialize connection to Apify platform
await Actor.init();

// ============================================
// Your existing code goes here
// ============================================

// Example: Get input from Apify Console or API
const input = await Actor.getInput();
console.log('Input:', input);

// Exampl