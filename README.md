# FIAF Cataloguing Manual

Markdown representation of the [FIAF Cataloguing Manual](https://www.fiafnet.org/pages/E-Resources/Cataloguing-Manual.html).

### Build

Building the manual currently requires [Docker](https://www.docker.com). The following commands will render `manual.pdf` to the `src` directory.

```sh
cd src && docker compose up -d
docker exec manual /app/src/build.sh
```

The current develop branch automatically renders [here](https://f003.backblazeb2.com/file/cataloguing-manual/develop-manual.pdf).

### Edit Guide

Required updates should be identified by an "issue" before work begins. The issue list can be found [here](https://github.com/FIAF/fiaf-cataloguing-manual/issues).

From within the issue itself, the editor should assign to themselves (if not already assigned). They should then "Create a branch" for the issue (if not already created).

From the project page, select the appropriate branch and then find the file or files which require editing and make desired edits. The PDF will automatically regenerate on the branch each time (this currently takes a few minutes).

Once edits have resolved the "issue", a "Pull request" can be made to pull the changes into the `develop` branch. These will eventually be versioned by the manual administrator for a major update.

### Formatting Notes

A good general guide to Markdown can be found [here](https://www.markdownguide.org/).      

There are however some specific LaTeX syntax functions which have been used to best achieve the desired outcomes of the project. These are documented [here](SYNTAX.md).
