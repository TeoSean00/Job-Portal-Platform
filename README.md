<a name="readme-top"></a>
## Introduction

This is a hybrid Next.js + Python app that uses Next.js as the frontend and FastAPI as the API backend.

<h4>Login Credentials</h4>
<table>
<thead>
    <tr>
    <th>Role</th>
    <th>Username</th>
    <th>Password</th>
    </tr>
</thead>
<tbody>
    <tr>
    <td>Staff</td>
    <td>staff</td>
    <td>staff123</td>
    </tr>
    <tr>
    <td>HR</td>
    <td>admin</td>
    <td>admin123</td>
    </tr>
    <tr>
    <td>Manager</td>
    <td>manager</td>
    <td>manager123</td>
    </tr>
</tbody>
</table>

## Table of Contents

1. [How it Works](#how-it-works)
2. [Getting Started](#getting-started)
3. [Running Unit and Integration Tests](#running-unit-and-integration-tests)
4. [Fixing Typescript Linting error](#fixing-typescript-linting-error)
5. [Staging Commits](#staging-commits)
6. [Branching and opening pull requests](#branching-and-opening-pull-requests)
7. [Database Migrations](#database-migrations)
8. [Continous Integration](#continous-integration)
9. [Continous Deployment](#continous-deployment)
10. [Scheduled Telegram PR Reminders](#scheduled-telegram-pr-reminders)
11. [Icons used](#icons)
12. [Theming System](#theming-system)

## How it works

The Python/FastAPI server is mapped into to Next.js app under /api/.

This is implemented using `next.config.js` rewrites to map any request to /api/:path* to the FastAPI API, which is hosted in the `/api` folder.

On localhost, the rewrite will be made to the `127.0.0.1:8000` port, which is where the FastAPI server is running.

In production, the FastAPI server is hosted as [Python serverless functions](https://vercel.com/docs/functions/serverless-functions/runtimes/python) on Vercel.

Automated Doc with [Swagger UI](https://fastapi.tiangolo.com/features/) has been set up under `/docs` route.

The frontend NextJs app is routed by default to the `127.0.0.1:3000` port.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

#### Setting up pipenv
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
or
npm install

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

#### Setting up Environment Variables
Following the `.env.example` file create a `.env` file with the same fields and populate it with the appropriate fields. `Please contact us for our AWS RDS string and credentials`
```
# Clerk RBAC
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=
CLERK_SECRET_KEY=
NEXT_PUBLIC_CLERK_SIGN_IN_URL=/sign-in
NEXT_PUBLIC_CLERK_SIGN_UP_URL=/sign-up
NEXT_PUBLIC_CLERK_AFTER_SIGN_IN_URL=/dashboard
NEXT_PUBLIC_CLERK_AFTER_SIGN_UP_URL=/dashboard

# Database Connection String
AWS_RDS_MYSQL_URL = 
```

Then, run the development server:
```bash
npm run dev
```

To activate the created venv:
```bash
pipenv shell
```

By default the FastApi server will be running on http://127.0.0.1:8000, while the NextJs frontend will be running on http://127.0.0.1:3000.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Running Unit and Integration Tests

Run the command below to run all backend unit and integration tests, -v and -s are optional flags to show more details about the tests and to show print statements respectively. Ensure `pipenv shell` is activated before running the command.
```
pytest . -v -s
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Fixing Typescript Linting error 

1. Install ESLint extension for VSCode, other helpful extensions are Prettier, Tailwind CSS, and Error Lens.
2. Run `npm run lint:fix` to check for and fix linting errors.
3. If there are errors that cannot be fixed automatically, you will have to check the cli for the errors and fix them manually.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Staging Commits

`Pre-commit` offloads some of the work of github CI unit testing to local dev environment for
1. Speed in identifying failed tests
2. Ease of use instead of running unit tests manually each time
3. Security in case bad code is written - tests are broken and user is notified even before committing
4. Standardization of code formatting and linting (for python files)
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Branching and opening pull requests

1. Include **issue ID** in the branch name to link the issue to a Pull/Merge Request. The fastest way to link to issues is to use Linear's branch name feature by clicking on the top right button 'Copy git branch name action' when viewing an issue.

2. Create a branch from main by pasting the branch name copied from the previous step. The branch name should look like `feature/spm-4-connect-github-or-gitlab`.

3. Switch to the new branch locally and make your changes.

4. Commit as you normally would, since we are not tracking commits.

5. When opening or merging a PR, make sure to link the PR on linear.

6. An auto-generated URL to the Linear issue should have been automatically added to the PR description. The Linear issue will be automatically updated accordingly with the new timeline and URL to the Github PR too.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

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
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Continous Integration

We have 2 CI workflows: `on_main.yaml` and `on_pr_open.yaml`. These integrations are run on every push to main and every PR open respectively.

Within each workflow, we run an assortment of checks and tests to ensure that the code is up to standard. These include:
- linting-next
- build-next
- unit-test-next
- linting-fastapi
- build-fastapi
- unit-test-fastapi
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Continous Deployment

We have CD which deploys to preview on every PR open and to production on every push to main. This is done via Vercel's Github integration.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Scheduled Telegram PR Reminders

We have a scheduled telegram reminder that sends a message to the telegram group every 4 hours to remind users to review PRs. This is done via Github Actions and a Telegram bot the script for it can be found in the .github/workflows folder labeled `PR_notif.yaml` and `get-open-prs.js`.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Icons

We are using [Radix icons](https://www.radix-ui.com/icons) or [Lucide](https://lucide.dev/) for our icons.

## Theming System

We are using shadcn's [theme](https://ui.shadcn.com/themes) for convenience.

Refer to `tailwind.config.ts` for list of classes (under `theme.extend.colors`) that can be used to style the components. e.g. `bg-primary`.

Do not use the default tailwind classes (e.g. `bg-blue-500`).
<p align="right">(<a href="#readme-top">back to top</a>)</p>