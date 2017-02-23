# Contributing Guidelines

We love improvements to our documentation! 

## Submitting an issue

The simplest way to tell us about a possible improvement is to open a new issue in the [Workflow repo](https://github.com/datarefuge/workflow/issues).

## Submitting a change through a pull request

Our process for accepting changes has a few steps.

1. If you haven't submitted anything before, and you aren't (yet!) a member of our organization, **fork and clone** the repo:

        $ git clone git@github.com:<your-username>/<repository-name>.git

  Organization members should clone the upsteam repo, instead of working from a personal fork:

      $ git clone git@github.com:datarefuge/workflow.git

2. Create a **new branch** for the changes you want to work on. Choose a topic for your branch name that reflects the change:

        $ git checkout -b <branch-name>

3. **Create or modify the files** with your changes. If you want to show other people work that isn't ready to merge in, commit your changes then create a pull request (PR) with _WIP_ or _Work In Progress_ in the title.

        https://github.com/datarefuge/workflow/pull/new/master

4. Once your changes are ready for final review, commit your changes then modify or **create your pull request (PR)**, assign as a reviewer or ping (using "`@<username>`"). For instance: @khdelphine, @dcwalk, @liblaurie or @titaniumbones.

5. Allow others sufficient **time for review and comments** before merging. We make use of GitHub's review feature to to comment in-line one PRs when possible. There may be some fixes or adjustments you'll have to make based on feedback.

6. Once you have integrated comments, or waited for feedback, your changes should get merged in!

## Incremental changes
Note that it is better to submit incremental bite-size changes that are easier to review. 

If you have in mind heavy changes, especially if they will affect the overall structure of the documentation, please discuss your plans with the other editors first.

## Viewing the final formatting as you edit

Documentation is built with [MkDocs](http://www.mkdocs.org/), a static site generator tailored to writing documentation. 

[Install Mkdocs](http://www.mkdocs.org/#installation) with a package manager or python/pip:

```sh
$ brew install mkdocs
```
or
```sh
$ pip install mkdocs
```

Clone this repo and navigate to it, make changes to the `.md` files. 

You can view changes via your browser at `http://127.0.0.1:8000`, by running the command:

```sh
$ mkdocs serve
```

**Note that Mkdocs enforces the Markdown syntax strictly, please refer to [this Markdown guide](https://guides.github.com/features/mastering-markdown/), as well as [this one](http://www.mkdocs.org/user-guide/writing-your-docs/#markdown-extensions) for details.**

Once a pull request has been merged into master, the gh-pages need to be regenerated. To do that, go to your local master branch at the command line and run: 
```
mkdocs gh-deploy
```

_These guidelines are based on [Toronto Mesh](https://github.com/tomeshnet) and [EDGI's](https://github.com/edgi-govdata-archiving)._
