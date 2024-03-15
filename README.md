
# Palindrome Checking

[![build](../../actions/workflows/build.yml/badge.svg)](../../actions/)
![Platforms: Linux, MacOS, Windows](https://img.shields.io/badge/Platform-Linux%20%7C%20MacOS%20%7C%20Windows-blue.svg)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-blue.svg)](https://github.com/psf/black)
[![Commits: Conventional](https://img.shields.io/badge/Commits-Conventional-blue.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
[![Discord](https://img.shields.io/discord/872320492936257537?logo=discord)](https://discord.gg/kjah8MFYbR)

## Introduction

- Due date: Check Discord or the
  [Course Materials Schedule](https://github.com/allegheny-college-cmpsc-101-spring-2024/course-materials/blob/main/Schedule.md)
- This assignment is graded as
  described in the syllabus section for an Engineering Efforts
  [Assignment Evaluation](https://github.com/allegheny-college-cmpsc-101-spring-2024/course-materials?tab=readme-ov-file#assignment-evaluation)
- Submit this assignment on GitHub following the expectations in the syllabus on
  [Assignment Submission](https://github.com/allegheny-college-cmpsc-101-spring-2024/course-materials#assignment-submission).
- To begin, read this `README` based on the Proactive Programmers' project
  [instructions](https://proactiveprogrammers.com/data-abstraction/engineering-efforts/palindrome-checking/)
- This project has been adapted from Proactive Programmers' material, thus discrepancies are possible.
- Post to the #data-structures Discord channel for questions and clarifications.
- For reference, check the
  [starter repo](https://github.com/allegheny-college-cmpsc-101-spring-2024/palindrome-checker-starter)
- Modifications to the gatorgrade.yml file are not permitted without explicit instruction.

## Learning Objectives

This assignment is about making a Command Line Interface to check
for palindromes.
The learning objectives of this assignment are to:

1. Use Git and GitHub to manage source code file changes
2. Implement recursive and non-recursive palindrome functions
3. Implement test functions for pytest and check test coverage
4. Import modules from packages
5. Demonstrate professional skills in linting and formatting
6. Write clearly about the programming concepts in this assignment.

## Seeking Assistance

Please review the course expectations on the syllabus about
[Seeking Assistance](https://github.com/allegheny-college-cmpsc-101-spring-2024/course-materials#seeking-assistance).
Students are reminded to uphold the Honor Code. Cloning the assignment repository is a
commitment to the latter.

For this assignment, you may use class materials, textbooks, notes, and the
internet. Ensure that your writing is original and based on your own understanding
of the concepts.

To claim that work is your own, it is essential to craft the logic and the
writing together without copying or using the logical structure of another
source. The honor code holds everyone to this standard.

If outside of lab you have questions, the #data-structures Discord channel,
TL office hours, instructor office hours, and GitHub Issues can be utilized.

## Project Details

This engineering effort invites you to implement a program called
`palindromechecker` that can determine whether or not an input word is or is not
a palindrome, or a word that is spelled the same both forwards and backwards.
For instance, the word `civic` is a palindrome because it is spelled the same
both forwards and backwards while `example` is not. Specifically, you will
implement one approach to palindrome checking that uses recursion and another
that reverses the word. In addition to implementing these two approaches for
palindrome checking, you will create a comprehensive command-line interface
using [Typer](https://typer.tiangolo.com/). Along with implementing your own
test cases for the functions that determine whether the word is a palindrome,
you will also add documentation to your `palindromechecker` in the form of
docstrings for both the functions and the module.

### Expected Output

This project invites you to implement a Python program, called
`palindromechecker`, that features different ways determine whether or not a
number is a palindrome. After you finish a correct implementation of all the
program's features, running it with the command `poetry run palindromechecker
--word civic --approach recursive`, it will produce this output. See a later
section for more output examples!

```text
✨ Awesome, using the recursive approach for palindrome checking!

🔖 Going to check to see if the word "civic" is a palindrome!

😆 Is this word a palindrome? Yes, it is!
```

Don't forget that you can display `palindromechecker`'s help menu and learn more
about its features by typing `poetry run palindromechecker --help` to show the
following output. This help menu shows that `palindromechecker` has a
`--approach` flag that enables it to check whether or not a word is a palindrome
through the use of a `reverse`-based or `recursive`-based technique.

```text
╭─ Options ─────────────────────────────────────────────────────────────╮
│ *  --word                    TEXT                [default: None]      │
│                                                  [required]           │
│    --approach                [recursive|reverse  [default: reverse]   │
│                              ]                                        │
│    --install-complet…        [bash|zsh|fish|pow  Install completion   │
│                              ershell|pwsh]       for the specified    │
│                                                  shell.               │
│                                                  [default: None]      │
│    --show-completion         [bash|zsh|fish|pow  Show completion for  │
│                              ershell|pwsh]       the specified shell, │
│                                                  to copy it or        │
│                                                  customize the        │
│                                                  installation.        │
│                                                  [default: None]      │
│    --help                                        Show this message    │
│                                                  and exit.            │
╰───────────────────────────────────────────────────────────────────────╯
```

Please note that the provided source code does not contain all of the
functionality needed to produce the output displayed in this section and later
in the project description. As the next section explains, you should add the
features needed to ensure that `palindromechecker` produces the expected output!
Importantly, this project invites you to add both a recursion-based and
reversal-based algorithm for palindrome checking.

#### Reminder

>Don't forget that if you want to run the `palindromechecker` program you must use
>your terminal window to first go into the GitHub repository containing this
>project and then go into the `palindromechecker` directory that contains the
>project's source code. Finally, remember that before running the program you
>must run `poetry install` to add its dependencies, such as Pyinstrument,
>Pytest, and Rich.

### Adding Functionality

If you study the file `palindromechecker/palindromechecker/main.py` you will see
that it has many `TODO` markers that designate the parts of the program that you
need to implement before `palindromechecker` will produce correct output. Once
you complete a task associated with a `TODO` marker, make sure that you delete
it and revise the prompt associated with the marker into a meaningful comment.
To ensure that the program works correctly, you must implement all of these
functions in the `palindrome` module:

- `def to_chars(word: str) -> str`
- `def is_palindrome(word: str) -> bool`
- `def is_palindrome_recursive(word: str) -> bool`
- `is_palindrome_reverse(word: str) -> bool`

After finishing your implementation of `palindromechecker` you should repeatedly
run the program in different configurations to confirm that it produces the
correct output. Since the `palindromechecker` provides a checking mode based on
reversing the string or recursively checking the string, you should make sure
that both approaches work correctly. You should also confirm that the
`palindromechecker` can correctly determine when a word both is and is not a
palindrome. Here are some examples that show the program's correct execution for
different values for the `--word` and `--approach` arguments. If you correctly
resolve all of the `TODO` markers in the provided source code your program
should produce the same output for each of these commands.

- `poetry run palindromechecker --word civic --approach reverse`

```cmd
✨ Awesome, using the recursive approach for palindrome checking!

🔖 Going to check to see if the word "civic" is a palindrome!

😆 Is this word a palindrome? Yes, it is!
```

- `poetry run palindromechecker --word civic --approach reverse`

```cmd
✨ Awesome, using the reverse approach for palindrome checking!

🔖 Going to check to see if the word "civic" is a palindrome!

😆 Is this word a palindrome? Yes, it is!
```

- `poetry run palindromechecker --word origin --approach recursive`

```cmd
✨ Awesome, using the recursive approach for palindrome checking!

🔖 Going to check to see if the word "origin" is a palindrome!

😆 Is this word a palindrome? No, it is not!
```

- `poetry run palindromechecker --word origin --approach reverse`

```cmd
✨ Awesome, using the reverse approach for palindrome checking!

🔖 Going to check to see if the word "origin" is a palindrome!

😆 Is this word a palindrome? No, it is not!
```

### Running Checks

If you study the source code in the `pyproject.toml` file you will see that it
includes the following section that specifies different executable tasks like
`ruff`. If you are in the `palindromechecker` directory that contains the
`pyproject.toml` file and the `poetry.lock` file, the tasks in this section
make it easy to run commands like `poetry run task ruff` to automatically run
the ruff linter designed to check the Python source code in your program and
its test suite to confirm that your source code adheres to the industry-standard.
You can also use the command `poetry run task fix` to automatically reformat the
source code. `poetry run task ruffdetails` will print out detailed linting errors
that point to exactly what ruff views as a linting error. Make sure to examine
the `pyproject.toml` file for other convenient tasks that you can use to both
check and improve your project!

Along with running tasks like `poetry run task ruff`, you can run the command
`gatorgrade --config config/gatorgrade.yml` to check your work. If your work
meets the baseline requirements and adheres to the best practices that proactive
programmers adopt you will see that all the checks pass when you run
`gatorgrade`. You can study the `config/gatorgrade.yml` file in your repository
to learn how the :material-github:
[GatorGrade](https://github.com/GatorEducator/gatorgrade) program runs
:material-github: [GatorGrader](https://github.com/GatorEducator/gatorgrader)
to automatically check your program and technical writing. If your program has
all of the anticipated functionality, you can run the command `poetry run task
test` and see that the test suite produces output like the following. Can you
add comments to explain how these tests work? What are the key components of
every test case created with Pytest? How do the tests "cover" the source code
the of the program?

```text
tests/test_main.py ....
tests/test_palindrome.py ....
tests/test_util.py ..
```

This project comes with other tasks that you can run once you have used Poetry
to install all of the dependencies. For instance, You
can also run commands like `poetry run task mypy` to check the program's use of
data types and `poetry run task markdownlint` to ensure that your source code
and writing adhere to other established conventions. For this assignment, you
can also use the command `poetry run task coverage` to create a coverage report,
like the one shown below, that reveals how well your tests exercise the source
code in the program `palindromechecker` program. You should try to write test
cases that completely cover the program's source code, producing a report like
this one.

```text
Name                              Stmts   Miss  Cover   Missing
---------------------------------------------------------------
palindromechecker/__init__.py         1      0   100%
palindromechecker/main.py            26      0   100%
palindromechecker/palindrome.py      18      0   100%
palindromechecker/util.py             4      0   100%
---------------------------------------------------------------
TOTAL                                49      0   100%
```

### Project Reflection

Once you have finished both of the previous technical tasks, you can use a text
editor to answer all of the questions in the `writing/reflection.md` file. For
instance, you should provide the output of the Python program in a fenced code
block, explain the meaning of the Python source code segments that you
implemented, and answer all of the other questions about your experiences in
completing this project. A specific goal of the reflection for this project is
to continue to explore how test cases and test coverage information can help a
developer to both establish a confidence in the correctness of and to find bugs
in a Python program. Once you have finished addressing the prompts in the
`writing/reflection.md` file that have `TODO` makers given as reminders, make
sure that you either delete the prompt or carefully integrate a revised version
of it into your writing.

## Project Assessment

Since this project is an engineering effort, it is aligned with the
**evaluating** and **creating** levels of [Bloom's
taxonomy](/proactive-learning/blooms-taxonomy/). You can learn more about how a
proactive programming expert will assess your work by examining the [assessment
strategy](/proactive-learning/assessment-strategy/). From the start to the end
of this project you may make an unlimited number of reattempts at submitting
source code and technical writing that meet all aspects of the project's
specification.

### Project Overview

After cloning this repository to your computer, please take the following
steps:

- Change into the program directory by typing `cd palindromechecker`.
- Install the dependencies for the project by typing `poetry install`.
- Run the program with its different configurations by typing:
  - `poetry run palindromechecker --word civic --approach reverse`
  - `poetry run palindromechecker --word civic --approach recursive`
  - `poetry run palindromechecker --word taylor --approach reverse`
  - `poetry run palindromechecker --word taylor --approach recursive`
- Please note that the program will not work unless you add the required source code
- Make sure to try the main tasks for automated software testing:
  - `poetry run task test`: run the test suite without coverage tracking
  - `poetry run task coverage`: run the test suite with coverage tracking
- Please note that the program will not work unless you add the required
  source code.
- Confirm that the program is producing the expected output described
  below and on the Proactive Programmers web site.
- Run the automated grading checks by typing
  `gatorgrade --config config/gatorgrade.yml`.
- You may also review the output from running GatorGrader in GitHub Actions.
- Don't forget to provide all of the required responses to the technical writing
  prompts in the `writing/reflection.md` file.
- Please make sure that you completely delete the `TODO` markers and their
  labels from all of the provided source code.
- Please make sure that you also completely delete the `TODO` markers and their
  labels from every line of the `writing/reflection.md` file.
