# TODO: provide a descriptive docstring for the module

# TODO: import all of the required packages and modules

# TODO: create the command-line interface object with typer

# TODO: define a PalindromeCheckingApproach enumeration with these options:
# --> "RECURSIVE": use the recursive approach described on page 129
# --> "REVERSE": use the recursive approach described on page 164

# TODO: When you are setting the default values of the --approach variable
# you may need to consider how to extract a value from PalindromeCheckingApproach
# Please refer to this GitHub issue tracker discussion for more details:
# https://github.com/tiangolo/typer/issues/290

# TODO: implement a command-line interface using typer that produces
# output like those examples included in the remainder of this file

# poetry run palindromechecker --help

# Usage: palindromechecker [OPTIONS]
#
#   Use a method to determine if an input string is a palindrome or not.
#
# Options:
#   --word TEXT                     [required]
#   --approach [recursive|reverse]  [default: reverse]
#   --install-completion            Install completion for the current
#                                   shell.
#
#   --show-completion               Show completion for the current shell,
#                                   to copy it or customize the
#                                   installation.
#
#   --help                          Show this message and exit.

# poetry run palindromechecker --word civic --approach recursive

# ✨ Awesome, using the recursive approach for palindrome checking!

# 🔖 Going to check to see if the word "civic" is a palindrome!

# 😆 Is this word a palindrome? Yes, it is!
