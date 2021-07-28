# stylish-python
A simple way to style python terminal output

## Import
First import the libaray with:
```python
from stylish-py import *
```
## Usage
All output must use `sprint()` (stylish print) as below:
```python
sprint("This will be styled")
```
`sprint()` accepts both strings and integers.

For basic styling use the `style()` method. All styles must be declared in a dictionary where the key is the property and the value is the style you want to apply, sort of like CSS. Below is some basic usage of the `style()` method:
```python
sprint("blue and bold").style({"color": "blue", "font": "bold"})
sprint("hex and rgb is accepted too!").style({"color": "#FFFFFF", "background": (0,0,0)})
```
