pre-commit Robot Framework Tidy wrapper
==============================

This is a [pre-commit](https://github.com/pre-commit) hook that will run
Robot Framework's Tidy tool on all of your robot files.

* [pre-commit](https://github.com/pre-commit)
* [Robot Framework](https://robotframework.org)


Add this to your ``.pre-commit-config.yaml`` file

    -   repo: git://github.com/guykisel/pre-commit-robotframework-tidy
        sha: 2ca903f005db8f8d87abe42864070f5b95e0837a
        hooks:
        -   id: robotframework-tidy-wrapper

Available flags:

* ``--use-pipes``: Use pipes as delimiters instead of just spaces. Defaults to
    False.
* ``--space-count``: How many spaces to use as a delimiter. Defaults to 4.

Development: ``pip install -r requirements-dev.txt``
