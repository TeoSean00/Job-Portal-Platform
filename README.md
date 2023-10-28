## Introduction

This is a hybrid Next.js + Python app that uses Next.js as the frontend and FastAPI as the API backend.

## How it works

The Python/FastAPI server is mapped into to Next.js app under /api/.

This is implemented using `next.config.js` rewrites to map any request to /api/:path* to the FastAPI API, which is hosted in the `/api` folder.

On localhost, the rewrite will be made to the `127.0.0.1:8000` port, which is where the FastAPI server is running.

In production, the FastAPI server is hosted as [Python serverless functions](https://vercel.com/docs/functions/serverless-functions/runtimes/python) on Vercel.

Automated Doc with [Swagger UI](https://fastapi.tiangolo.com/features/) has been set up under `/docs` route.

## Getting Started

#### setting up pipenv
##### if using pip as package manager
```bash
pip install pipenv
or
pip3 install pipenv
```
##### if using brew as package manager
```bash
brew install pipenv
```

First, install the dependencies
```bash
# nodejs / js
npm i

# python (additional dependencies needed to be specified as an argument after 'install', pipfile will auto update)
pipenv install 
```

Second, install pre-commit hooks if you are developing 
```
pipenv install pre-commit
pre-commit install
# check that pre-commit file is crated in .git/hooks

# if existing work has not been formatted
pre-commit run --all-files

# if it's been a long time, update hooks to latest ver
pre-commit autoupdate

```

Then, run the development server:
```bash
npm run dev
```

To activate the created venv:
```bash
pipenv shell
```

The FastApi server will be running on http://127.0.0.1:8000 – feel free to change the port in `package.json` (you'll also need to update it in `next.config.js`).

## Fixing Typescript Linting error 

1. Install ESLint extension for VSCode, other helpful extensions are Prettier, Tailwind CSS, and Error Lens.
2. Run `npm run lint:fix` to check for and fix linting errors.
3. If there are errors that cannot be fixed automatically, you will have to check the cli for the errors and fix them manually.

## Staging Commits

Pre-commit offloads some of the work of github CI unit testing to local dev environment for
1. Speed in identifying failed tests
2. Ease of use instead of running unit tests manually each time
3. Security in case bad code is written - tests are broken and user is notified even before committing
4. Standardization of code formatting and linting (for python files)

## Branching and opening pull requests

1. Include **issue ID** in the branch name to link the issue to a Pull/Merge Request. The fastest way to link to issues is to use Linear's branch name feature by clicking on the top right button 'Copy git branch name action' when viewing an issue.

2. Create a branch from main by pasting the branch name copied from the previous step. The branch name should look like `feature/spm-4-connect-github-or-gitlab`.

3. Switch to the new branch locally and make your changes.

4. Commit as you normally would, since we are not tracking commits.

5. When opening or merging a PR, make sure to include the Linear issue ID in the title, e.g. `Completed spm-4: Connect GitHub or GitLab`.

6. An auto-generated URL to the Linear issue should have been automatically added to the PR description. The Linear issue will be automatically updated accordingly with the new timeline and URL to the Github PR too.

## Database Migrations

With Alembic, revisions to models via sqlalchemy can be used to automatically migrate the database, reducing the hassle of manual database reconfiguration 

View current db version
```bash
alembic current
```

After modifying ORM code / models
```bash
alembic revision --autogenerate -m "YOUR MIGRATION MESSAGE"
```

After checking the generated revisions are okay
```bash
alembic upgrade HEAD 
# alternatively specify the revision hash initials to upgrade to a specific version
```

To downgrade to the previous version
```bash
alembic downgrade -1
# alternatively specify the revision hash initials to downgrade to a specific version 
# or alembic downgrade base to reset to initial state
```

## Icons

We are using [Radix icons](https://www.radix-ui.com/icons) or [Lucide](https://lucide.dev/) for our icons.

## Theming System

We are using shadcn's [theme](https://ui.shadcn.com/themes) for convenience.

Refer to `tailwind.config.ts` for list of classes (under `theme.extend.colors`) that can be used to style the components. e.g. `bg-primary`.

Do not use the default tailwind classes (e.g. `bg-blue-500`).
