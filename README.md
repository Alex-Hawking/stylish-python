# stylish-python
An intuitive way to style python terminal output

## Import

I am currently uploading the library to PyPi. For now simply clone or download the `.py` file and place it into your working directory.

First import the libaray with:
```python
from stylish_py import *
```

## Usage

All output must use `sprint()` (stylish print) as below:
```python
sprint("This will be styled")
```
`sprint()` accepts both strings and integer values and will print whatever is passed into it onto the console. It will print styled text if styles are applied as intstructed below.

## The `style()` method

For basic styling use the `style()` method. All styles must be declared in a dictionary where the key is the property and the value is the style you want to apply, sort of like CSS. Below is some basic usage of the `style()` method:
```python
sprint("blue and bold").style({"color": "blue", "font": "italic"})
sprint("hex and rgb is accepted too!").style({"color": "#FFFFFF", "background": (0,0,0)})
```

At the moment the following styles can be applied:
* `"color"`: sets the foreground color
* `"background"`: sets the background color
* `"font"`: can change basic font properties such as weight and slant, dependent on terminal used
* `"style"`: only accepts `"none"` and is used only for nested styles explained later on

Both `"color"` and `"background"` accept rgb values (in 3 element tuple containing ***only*** integers), hex values (in a string beginning with "#") or one of the pre-assigned values explained at end of the README.

## `Init()`

The `init()` method should be called at the start of the file. At the moment the init method accepts the following:
* `stylesheet`: Can either accept a string that points to the path of the `.ass` file or to a variable containing a list of styles (stylesheets are explained below)
* `palette`: Can either accept a string that points to the path of the `.acp` file or to a variable containing a dictionary of custom colors (palettes are explained below)
* `end`: Can accept a boolean, either `True` or `False`. If set to `False` the style applied to the line above will continue on through all lines. Recommend to set to `True`

***file.py***
```python
from stylish_py import *

sprint().init(
    end=True,
    stylesheet="./path/to/stylesheet.ass",
    palette="./path/to/palette.acp"
)
```

## Stylesheets

stylish allows you to use stylesheets to easily apply styles to multiple elements through the use of the `id()` and `stylesheet()` methods. A stylesheet can either be imported from a `.ass` (awesome style sheet) file or defined inline as shown below. At the moment only one style sheet can be used at once. Below are two examples of stylesheet usage:

***style.ass***
```
{"id": "title", "color": (255, 255, 255), "font": "bold"}
{"id": "subtitle", "color": (200, 200, 200), "font": "italic"}
```

***file.py***
```python
from stylish_py import *

sprint().init(
    stylesheet="./style.ass"
)

sprint("This is a white, bold title").id("title")
sprint("This is a grey, italic subtitle").id("subtitle")
```

As you can see in the above example a stylesheet was imported using the `init()` method. Each dictionary in a stylesheet should have an `"id"` tag, this tells stylish what styles should be used where. The `id()` method accepts a string which should match that of the `"id"` value in the dictionary containing the styles you want to apply.

Stylsheets can also be created within the `.py` that they are going to be used as below:

***file.py***
```python
from stylish_py import *

stylesheet = [
    {"id": "title", "color": (255, 255, 255), "font": "bold"},
    {"id": "subtitle", "color": (200, 200, 200), "font": "italic"}
]

sprint().init(
    stylesheet=stylesheet
)

sprint("This is a white, bold title").id("title")
sprint("This is a grey, italic subtitle").id("subtitle")
```

This will produce the same output but instead of passing in a string to the `init()` method a list of dictionaries is instead used.

## Palettes

stylish also allows you to create palettes of custom colors which you can use to set your `"color"` and `"background"`. Palettes function in a similar way to stylesheets in that they can be defined either inline or in a `.acp` (awesome color palette file) as below:

***palette.acp***
```
{
    "turquoise": "#41EAD4",
    "sage": (186, 191, 149)
}
```

***file.py***
```python
from stylish_py import *

sprint().init(
    palette="./palette.acp"
)

sprint("This is a custom color!").style({"color": "turquoise"})
sprint("So is this!").style({"color": "sage"})
```

The below will output the exact same as the above:

```python
from stylish_py import *

palette = {
    "turquoise": "#41EAD4",
    "sage": (186, 191, 149)
}

sprint().init(
    palette=palette
)

sprint("This is a custom color!").style({"color": "turquoise"})
sprint("So is this!").style({"color": "sage"})
```

## Default values

### Colors

Color | RGB
--- | ---
red | (255, 0, 0)
green | (0, 255, 0)
blue | (0, 0, 255)
yellow | (255, 255, 0)
aqua | (0, 255, 255)
magenta | (255, 0, 255)
pink | (255, 105, 180)
chocolate | (255, 105, 30)
white | (255, 255, 255)
black | (0, 0,0 )

### FONTS

* bold
* dim
* italic
* underline
* invisible
