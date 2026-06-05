# Data Structure & Algorithm - HackerRank Edition

## Goal

To curate a comprehensive collection of essential algorithms and data structures in computer science, using practical challenges and solutions from the HackerRank platform as a learning framework.

## Build and View the Book locally

### Set up Node.js with NVM

GitBook typically requires an older version of Node.js (like v12) to run properly. You can use [Node Version Manager (nvm)](https://github.com/nvm-sh/nvm) to manage this:

```bash
# Install and use Node.js v12
nvm install 12
nvm use 12
```

### Install GitBook CLI

```bash
npm install graceful-fs@4.2.0 -g
npm install gitbook-cli@2.1.2 -g
```

### Start the preview

Navigate to this directory (where `SUMMARY.md` is located) and run:

```bash
gitbook init
gitbook serve
```

This will start a local server, usually at `http://localhost:4000`, where you can preview the book.
