import textwrap

COLORS = {
    "red": 196,
    "green": 46,
    "blue": 21
}

FONTS = {
    "bold": 1,
    "dim": 2,
    "italic": 3,
    "underline": 4,
    "invisible": 8
}

pallette = {}
stylesheet = {}

class sprint:
    def __init__(self, input=""):
        self.input = input
        self.output = ""
        self.end = "\033[0m"
    
    def __del__(self):
        if self.input:
            if self.output:
                print(self.output)
            else:
                print(self.input)
            
    def __hex_to_rgb(self, hex):
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        def decimal(hex):
            try:
                return int(hex)
            except:
                return letters.index(hex) + 10
        rgb = []
        hex = textwrap.wrap(hex[1:], 2)
        for color in hex:
            list(color)
            output = decimal(color[0])*16 + decimal(color[1])
            rgb.append(output)
        return tuple(rgb)        
            
    def __color(self, color, layer):
        if type(color) == str:
            if color in COLORS:
                return f"{layer}8;5;{COLORS[color]}"
            elif color[0] == "#" and len(color) == 7:
                hex_vals = self.__hex_to_rgb(color)
                return f"{layer}8;2;{hex_vals[0]};{hex_vals[1]};{hex_vals[2]}"
        elif type(color) == tuple and len(color) == 3:
            return f"{layer}8;2;{color[0]};{color[1]};{color[2]}"
        
    def __font(self, font):
        if font in FONTS:
            return FONTS[font]
        
    def __append_style(self, styles):
        color = "38;5;0"
        background = "48;5;0"
        font = "0"
        if type(styles) == dict:
                for style in styles:
                    if style == "color":
                        if styles[style] in pallette:
                            color = self.__color(pallette[styles[style]], "3")
                        else:
                            color = self.__color(styles[style], "3")
                    elif style =="background": 
                        if styles[style] in pallette:
                            background = self.__color(pallette[styles[style]], "4")
                        else:
                            background = self.__color(styles[style], "4")
                    elif style == "font":
                        font = self.__font(styles[style])                               
        return f"\033[{font};{color};{background}m"

    def pallette(self, new_palette):
        global pallette
        if type(new_palette) == dict:
            pallette = new_palette
            
    def stylesheet(self, new_stylesheet):
        global stylesheet
        if type(new_stylesheet) == list and all(isinstance(style, dict) for style in new_stylesheet):
            stylesheet = new_stylesheet
            
    def id(self, element_id):
        if type(element_id) == str:
            for style in stylesheet:
                if element_id == style["id"]:
                    del style["id"]
                    self.output += f"{self.__append_style(style)}{self.input}{self.end}"
        elif type(element_id) == list and type(self.input) == list and len(self.input) == len(element_id):
                for loop_id in element_id:
                    for style in stylesheet:
                        try:
                            if loop_id == style["id"]:
                                del style["id"]
                                self.output += f"{self.__append_style(style)}{self.input[element_id.index(loop_id)]}{self.end}"
                        except:
                            pass

    def style(self, styles):
        if type(self.input) == str:
            self.output += f"{self.__append_style(styles)}{self.input}{self.end}"
        elif type(self.input) == list:
            if len(self.input) == len(styles) and type(styles) == list:
                for style in styles:
                    self.output += f"{self.__append_style(style)}{self.input[styles.index(style)]}{self.end}"