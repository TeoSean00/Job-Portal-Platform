## Introduction
This is a hybrid Next.js + Python app that uses Next.js as the frontend and FastAPI as the API backend.

## How it works

The Python/FastAPI server is mapped into to Next.js app under /api/.

This is implemented using `next.config.js` rewrites to map any request to /api/:path* to the FastAPI API, which is hosted in the `/api` folder.

On localhost, the rewrite will be made to the `127.0.0.1:8000` port, which is where the FastAPI server is running.

In production, the FastAPI server is hosted as [Python serverless functions](https://vercel.com/docs/functions/serverless-functions/runtimes/python) on Vercel.

Automated Doc with [Swagger UI](https://fastapi.tiangolo.com/features/) has been set up under `/docs` route.

## Getting Started

setting up pipenv on Windows
```bash
pip install pipenv
```
for MacOS
```bash
brew install pipenv
```

First, install the dependencies
```bash
npm i
```

Then, run the development server:
```bash
npm run dev
```

The FastApi server will be running on http://127.0.0.1:8000 – feel free to change the port in `package.json` (you'll also need to update it in `next.config.js`).


## Branching and opening pull requests

1. Include **issue ID** in the branch name to link the issue to a Pull/Merge Request. The fastest way to link to issues is to use Linear's branch name feature by clicking on the top right button 'Copy git branch name action' when viewing an issue.

2. Create a branch from main by pasting the branch name copied from the previous step. The branch name should look like `feature/spm-4-connect-github-or-gitlab`.

3. Switch to the new branch locally and make your changes.

4. Commit as you normally would, since we are not tracking commits.

5. When opening or merging a PR, make sure to include the Linear issue ID in the title, e.g. `Completed spm-4: Connect GitHub or GitLab`.

6. An auto-generated URL to the Linear issue should have been automatically added to the PR description. The Linear issue will be automatically updated accordingly with the new timeline and URL to the Github PR too.

## Icons

We are using [Radix icons](https://www.radix-ui.com/icons) or [Lucide](https://lucide.dev/) for our icons.

## Theming System

We are using shadcn's [theme](https://ui.shadcn.com/themes) for convenience.

Refer to `tailwind.config.ts` for list of classes (under `theme.extend.colors`) that can be used to style the components. e.g. `bg-primary`.

Do not use the default tailwind classes (e.g. `bg-blue-500`).
