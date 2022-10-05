# Contribution Guidelines

This documentation serves as a series of instructions to assist you in adding to this repository.

First of all, I want to thank you for your contribution.

Before contributing, do make sure to read the necessary sections.

We eagerly anticipate your input. 🎉

## Getting started with comtributing?💡

To learn the fundamentals of Git/GitHub and contributing to a repository, refer to the articles below. If you run into trouble when making a contribution, the project maintainers will be happy to assist you:)

* [Basics of git and github](https://towardsdatascience.com/getting-started-with-git-and-github-6fcd0f2d4ac6)
* [Introduction to github Lab](https://github.com/skills/introduction-to-github)
* [Contributing to Open Source for the first time](https://www.youtube.com/watch?v=c6b6B9oN4Vg)


## Contribute to this Project

To contribute to this project, simply follow the workflow described below:

### 1. Find an issue 

- Choose an issue from the existing ones or establish your own to begin contributing.
- You can start working on the issue once a maintainer assigns it to you!

### 2. Fork and clone the repository

- Fork the repository. It makes a copy of this repository and adds it to your personal GitHub repository.
- Clone the forked repository to your own computer. This will create a copy of the repository on your own PC. Copy the forked repository link and run the following command:

```bash
  git clone <cloning URL> 
```

  
- Change your current directory to the directory of the project repository.
  
```bash
cd <project directory>
``` 
 
- To make sure that your local copy is up to date, add a reference to the source repository.
  
```bash
git remote add upstream <source repository URL>  
```

  
### 3. Create a new branch
  Create a new branch. Set a name descriptive of the issue that you are solving. The following command will create and switch to a new branch.
  
```bash
git checkout -b Branch_Name  
```


### 4. Work on your chosen issue!!!
  - Work on the issue(s) assigned to you.
  - After you've completed your work, add changes to your branch using:
  
```bash
# To add all new files to branch Branch_Name  
git add .   

# To add only a few files to Branch_Name
git add <some files>     
```
  
### 5. Commit your changes 
     - Commit your changes to the repository, don't forget to include a note that describes the changes you're making.
      
```bash
git commit -m "message"  
```
 
### 6. Sync the fork with your local copy
      - Before pushing changes, make sure your branch is in sync with the source repository by using the following commands:
 
```bash
git fetch upstream
git checkout Branch_Name
git merge upstream/main 
```
  
### 7. Push your changes 
      - When you think your code is ready to be reviewed, push your changes to your repository
    
```bash
git push -u origin Branch_Name   
```
 
### 8. Pull request
    - Go to your repository in browser and click on compare and pull requests. Then add a title and description to your pull request that explains your contribution.
  
    - Congrats! Your Pull Request has been submitted and will be reviewed by the moderators and merged. 🥳


