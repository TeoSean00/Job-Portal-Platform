## Introduction
This is a hybrid Next.js + Python app that uses Next.js as the frontend and FastAPI as the API backend.

## How it works

The Python/FastAPI server is mapped into to Next.js app under /api/.

This is implemented using `next.config.js` rewrites to map any request to /api/:path* to the FastAPI API, which is hosted in the `/api` folder.

On localhost, the rewrite will be made to the `127.0.0.1:8000` port, which is where the FastAPI server is running.

In production, the FastAPI server is hosted as [Python serverless functions](https://vercel.com/docs/functions/serverless-functions/runtimes/python) on Vercel.

Automated Doc with [Swagger UI](https://fastapi.tiangolo.com/features/) has been set up under `/docs` route.

## Getting Started

First, install the dependencies
```bash
npm install
```

Then, run the development server:

```bash
npm run dev
```

The FastApi server will be running on http://127.0.0.1:8000 – feel free to change the port in `package.json` (you'll also need to update it in `next.config.js`).
