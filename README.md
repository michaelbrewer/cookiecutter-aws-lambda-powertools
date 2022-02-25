# Cookiecutter AWS Lambda Powertools

This is a [Cookiecutter](https://github.com/audreyr/cookiecutter) template to create a CDK project.

It is important to note that you should not try to `git clone` this project but use `cookiecutter` CLI instead as ``{{cookiecutter.project_slug}}`` will be rendered based on your input and therefore all variables and files will be rendered properly.

## Requirements

Install `cookiecutter` command line:

**Pip users**:

* `pip install cookiecutter`

**Homebrew users**:

* `brew install cookiecutter`

**Windows or Pipenv users**:

* `pipenv install cookiecutter`

**NOTE**: [`Pipenv`](https://github.com/pypa/pipenv) is the new and recommended Python packaging tool that works across multiple platforms and makes Windows a first-class citizen.

## Usage

Generate a new CDK project: `cookiecutter git@github.com:gyft/cdk-cookiecutter.git`.

You'll be prompted a few questions to help this cookiecutter template to scaffold this project and after its completed you should see a new folder at your current path with the name of the project you gave as input.

**NOTE**: After you understand how cookiecutter works (cookiecutter.json, mainly), you can fork this repo and apply your own mechanisms to accelerate your development process and this can be followed for any programming language and OS.

## Options

Option | Description
------------------------------------------------- | ---------------------------------------------------------------------------------
`type` | Which build system to use `cdk` (TODO) or `sam`.
`trigger` | Which lambda trigger to use `s3` or `s3-object-lambda`.

## Credits

* This project has been generated with [Cookiecutter](https://github.com/audreyr/cookiecutter)

## License

Foo Bar
