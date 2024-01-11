## Contributing (External)

Welcome to our project! We appreciate your interest in contributing.

You can contribute in many ways:

### How to Contribute

- Fork the 'MathDistOps' repository.

- Clone the forked repository to your local machine.
  
	```
	git@github.com:UBC-MDS/MathDistOps.git
	```

- Install your local copy with Poetry, this is how you set up your fork for local development:

    ``` 
    cd MathDistOps/
    poetry install
    ```

- Create a new branch for your changes: 'git checkout -b feature/new-feature'.

- Make your changes, check that your changes pass the tests by running pytest.

    ```
    poetry run pytest
    ```

- Commit and push your changes to your forked repository

    ```
    git add .
    git commit -m "Your detailed description of your changes."
    git push origin name-of-your-bugfix-or-feature
    ```

- Open a pull request from your forked repository to the original repository.

### Report Bugs

Please submit bug reports on our GitHub repository at https://github.com/UBC-MDS/MathDistOps/issues.

When reporting a bug, kindly provide:

- The name and version of your operating system.
- Any pertinent details about your local setup that could aid in troubleshooting.
- Clear and detailed steps to replicate the bug.

### Resolving Bugs

Review the GitHub issues labeled as "bug" and "help wanted." These are available for anyone interested in addressing and implementing solutions.

### Implementing Features

Browse the GitHub issues related to features. Any item labeled as "enhancement" and "help wanted" is available for implementation by anyone interested.

### Documentation

Your project could benefit from additional documentation, whether integrated into the official documentation, included in docstrings, or shared through various platforms such as blog posts and articles.

### Feedback

The best way to send feedback is to file an issue at https://github.com/UBC-MDS/MathDistOps/issues.


### Pull Request Guidelines
Before you submit a pull request, check that it meets these guidelines:

1. Ensure that the pull request incorporates testing.
2. If the pull request introduces new features, it is essential to update the documentation. Place the new functionality within a function accompanied by a docstring, and include details about the feature in the README.md list.
3. Confirm that the pull request functions correctly for both Python 3.7 and 3.8. Verify the status of the tests for all supported Python versions by checking https://github.com/UBC-MDS/MathDistOps/issues.


### Code of Conduct
Please note that the MathDistOps project is released with this Contributor Code of Conduct. By contributing to this project, you agree to abide by its terms.

## Contributing (Internal)

We build several branches to store functions and a bunch of files like contributing, contributor, readme. If we have issues, will pull it on the github. Some issues come from conflict, some come from code review, like formats. Comments for each pull requests can improve contribution. Team members have different roles which can make pipeline clearly. coomunication through github and weekly meetings also make great improvment to the whole project. 



