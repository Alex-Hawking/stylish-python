# stylish-python
A simple way to style python terminal output

## Import
First import the libaray with:
```python
from stylish_py import *
```
## Usage
All output must use `sprint()` (stylish print) as below:
```python
sprint("This will be styled")
```
`sprint()` accepts both strings and integer values.

### The `style()` method

For basic styling use the `style()` method. All styles must be declared in a dictionary where the key is the property and the value is the style you want to apply, sort of like CSS. Below is some basic usage of the `style()` method:
```python
sprint("blue and bold").style({"color": "blue", "font": "bold"})
sprint("hex and rgb is accepted too!").style({"color": "#FFFFFF", "background": (0,0,0)})
```
At the moment the following styles can be applied:
* `"color"`: sets the foreground color
* `"background"`: sets the background color
* `"font"`: can change basic font properties such as weight and slant, dependent on terminal used
* `"style"`: only accepts `"none"` and is used only for nested styles explained later on

Both `"color"` and `"background"` accept rgb values (in 3 element tuple containing ***only*** integers), hex values (in a string beginning with "#") or one of the pre-assigned values explained at end of the README.

### Stylesheets

stylish allows you to use stylesheets to easily apply styles to multiple elements through the use of the `id()` method. A stylesheet can either be imported from a `.ass` (awesome style sheet) file or defined inline as shown below. At the moment only one style sheet can be used at once. Below are two examples of stylesheet usage:
***style.ass***
```
{"id": "title", "color": (255, 255, 255), "font": "bold"}
{"id": "subtitle", "color": (200, 200, 200), "font": "italic"}
```
***file.py***
```
from stylish_py import *

sprint().stylesheet("./style.ass")

sprint("This is a white, bold title").id("title")
sprint("This is a grey, italic subtitle").id("subtitle")
```
As you can see in the above example a stylesheet was imported using the `.stylesheet()` method. Each dictionary in a stylesheet should have an `"id"` tag, this tells stylish what styles should be used where. The `id()` method accepts a string which should match that of the `"id"` value in the dictionary containing the styles you want to apply.
