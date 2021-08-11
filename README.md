# obscure-password

[![Python package](https://github.com/Shapedsundew9/obscure-password/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/Shapedsundew9/obscure-password/actions/workflows/python-package.yml)
[![codecov](https://codecov.io/gh/Shapedsundew9/obscure-password/branch/main/graph/badge.svg?token=ZDKW1280KN)](https://codecov.io/gh/Shapedsundew9/obscure-password)

## Overview

obscure-password is a self contained obfuscation library for hardcoded passwords (or other text) in Python scripts. Obfuscation is a technique to prevent the unskilled or casual observer access to sensitive data and provide an impediment to the skilled i.e. requiring explicit effort to circumvent.
Typical use cases are in casual software development or  debugging where a developer may be sharing scripts with field technicians to perform one-off tasks.
## Usage
```python
>>> from obscure_password import obscure, unobscure
>>> obscure('my sensitive information')
>>> print(obscured)
gNA0AlAmAMATBQh7EN8SOs_l1BIBU4tjgbyy28CknMagGogf7JhFHU35GLmzV0AA
>>> unobscure(obscured)
'my sensitive information'
```
obscure_password laces the obscured text with a marker which enables it to avoid unobscuring text that has not been obscured.
```python
>>> from obscure_password import obscure, unobscure
>>> unobscure('my sensitive information')
'my sensitive information'
```
This is helpful when developing a script and wanting to regularly change the password.
obscure-password was designed for password ofuscation and not to obscure large texts (although it can). The marker implementation significantly increases the length of the obscured text.
## Sunburst Code Coverage Chart

 The inner-most circle is the entire project, moving away from the center are folders then, finally, a single file. The size and color of each slice is representing the number of statements and the coverage, respectively.

 ![Sunburst](https://codecov.io/gh/Shapedsundew9/obscure-password/branch/main/graphs/sunburst.svg)
