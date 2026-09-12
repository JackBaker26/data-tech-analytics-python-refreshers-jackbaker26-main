# Python Refresher Exercises

## 🔍 Overview
This is a refresher assignment to review previously covered concepts and syntax of Python.
It's also another opportunity to practice using Git and GitHub.

### Emojis Legend
Throughout the assignment instructions, you'll find some emojis that will help you navigate the instructions. Here's what they mean:
- 👨🏻‍💻 - Instructions; Tells you about something specific you need to do.
- 🦉 - Tips; Will tell you about some hints, tips and best practices
- 📜 - Documentations; provides links to documentations
- 🚩 - Checkpoint; marks a good spot for you to commit your code to git
- 🕵️ - Tester; Don't modify code blocks starting with this emoji

This is inspired by `@kentcdodds` workshops.

## 🎯 Objectives
- Refresher on Python and some common libraries such as `numpy`.
- Refresher on Jupyter Notebooks.
- continue practice using git and GitHub.

--------
## 📝 Instructions
### 0. Setup
- Accept the assignment on GitHub Classroom. (looks like you've already done that)
  - This repository is private; only you and the instructors can see it. Please don't change the visibility of the repository in the settings.
- Clone the repository to your computer.
  - You can use GitHub Desktop, the command line, or VSCode to do that.
  - You can view the ["Cloning a Repository - GitHub Docs](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository?tool=webui) for more information.
- Open the assignment root folder in VSCode.
  - If you get a notification asking you to install the recommended extensions, go ahead and do that.
- using the terminal, install the dependencies for this project:
  - if you're using `poetry`, run `poetry install`.
  - If you're using `pipenv`, run `pipenv install`
  - if you're using `pip`, run `pip install -r requirements.txt`
- Open the `python-exercises.ipynb` Notebook in VSCode
- Make sure you have the right kernel selected for the notebook. Use this [guide](https://it4063c.github.io/guides/FAQ/vscode-jupyter) if you need help.

### 1. Complete the exercises
The notebook itself will guide you through the exercises. You'll find instructions regarding each exercise in the notebook.
You'll also find some tips and links to documentations that will help you complete the exercises.

- Make sure you commit often, you'll find this emoji 🚩, signifying suggested spots where you can make a commit of your code.
- Don't forget to push your code to GitHub when you're done.
- If you're doing this assignment, over multiple sessions, make sure you always push your code to GitHub before you close your computer to avoid losing your work.

### 2. Test your code
- Each of the exercises is followed by an automated test in a separate cell, that will check your work.
  - Make sure you run the tests and make sure they pass.

Completely optional and redundant, but you can also run the tests from the terminal:
```bash
pytest --capture=sys
```
if you want to avoid the various warnings, you can run:
```bash
PYDEVD_DISABLE_FILE_VALIDATION=1 JUPYTER_PLATFORM_DIRS=1 pytest --capture=sys
```

### 3. Finalize and Submit your Work
- **Once you've completed all the exercises, come back to this file** and complete the reflection section and the self-evaluation section at the end of this file.
- Submit your work by submitting a link to your repository on Canvas.

## Project Structure
```
.
├── .git                     1️⃣  
├── .vscode                  2️⃣  
│   ├── extensions.json      
│   └── settings.json        
├── .gitignore               3️⃣  
├── makefile                 4️⃣  
├── tests                      
├── Pipfile                  5️⃣  
├── Pipfile.lock             
├── pyproject.toml           6️⃣  
├── poetry.lock              
├── python-exercises.ipynb   7️⃣   
├── python-exercises.py      8️⃣ 
├── README.md                📌 
└── requirements.txt         9️⃣
```
📌 You are here ...
- 1️⃣ DO NOT TOUCH THIS DIRECTORY. Normally, this folder is hidden, but if you can see it, don't touch it. This is what makes your folder a git repo.
- 2️⃣ This directory contains some supporting files for helpful extensions, and VSCode settings 
- 3️⃣ Another git related files. This tells git not to track certain files and folders that you don't want uploaded
- 4️⃣ You can ignore this file and the tests folder. They're being used to facilitate some of the project automation.
- 5️⃣ `Pipfile` and `Pipfile.lock` are used by pipenv to manage dependencies.
- 6️⃣ `Pyproject.toml` and `poetry.lock` is used by poetry to manage dependencies.
- 7️⃣ This is the file you'll need to edit to complete the exercises.
- 8️⃣ The last cell in the notebook will export the notebook as a python file. Providing feedback on Notebooks on GitHub is not great, so this generated file will allow me to provide feedback on your code.
- 9️⃣ if you're not using either `pipenv` or `poetry`, you can use this file to install the dependencies for this project.

---------------
## 💭 Reflection and Self Assessment

**I learned:** (repeat as needed)
- .
A good python refresher along with more indepth learning for numpy.

**I struggled with:** (repeat as needed)
- . Getting numpy to work but changing the kernel fixed it.

**I need the instructor to help me with:** (repeat as needed)
- . Clarification on poetry,

**How long did it take you to complete this assignment? and reflect on that**
[1 ] hours.
It wasn't too difficult as most of it was a refresher
**If I were to do this assignment again, I would:** (repeat as needed)
- . Try to understand the checker cell below each question.

**💯 Self Grade:** For this assignment, based on my work and my reflections I should get [ 20] out of 20.

--------------------
## 📚 References and Citations
**I used the following links, books, and other resources in my work:** (repeat as needed)
- .
  
**I received help from the following people:** (repeat as needed)
- . 

---
## Copyrights and License
IT4063C Data Technologies Analytics by [Yahya Gilany](https://yahyagilany.io). is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
