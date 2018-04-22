# Shebang line starts with #! and then the path to python interpreter; path will vary on installation
#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Tell python interpreter to interpret a module from its standard library
# Platform module displays python version when script is run
import platform

# print is a function; requires parentheses and argument(s)
print('This is python version {}'.format(platform.python_version()))
