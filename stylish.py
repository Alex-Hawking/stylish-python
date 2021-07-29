import os
import ast
import textwrap

START = "\033["

RESET = "\033[0m"

DEFAULT = "8;5;0"

COLOURS = {
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


def terminal_width():
    return os.get_terminal_size().columns


def terminal_height():
    return os.get_terminal_size().rows

stylesheet = []
pallette = {}

class sprint:
    # Magic Classes
    def __init__(self, input=""):
        #Set all values to defaults
        self.input = input
        self.color = f"3{DEFAULT}"
        self.background = f"4{DEFAULT}"
        self.font = 0
        self.output = f"{RESET}{self.input}{RESET}"

    def __del__(self):
        #Output styled sentence as class deletes itself
        if self.output:
            print(f"{self.output}{RESET}")
             
#Private functions

    def __rs_style(self):
        #Reset styles
        self.color = f"3{DEFAULT}"
        self.background = f"4{DEFAULT}"
        self.font = 0

    def __hex(self, input):
        #Convert hex to rgb
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        def decimal(input):
            try:
                return int(input)
            except:
                return letters.index(input) + 10
        rgb = []
        input = textwrap.wrap(input[1:], 2)
        for color in input:
            list(color)
            output = decimal(color[0])*16 + decimal(color[1])
            rgb.append(output)
        return tuple(rgb)
    
    def __error(self, errortype, errortext):
        #Throw errors
        print(f"\033[31mError\033[0m")
        if errortype == "style":
            print(f"Style given: {type(errortext)} \"{errortext}\" not found")
        elif errortype == "argument":
            print(
                f"Incorrect argument: {type(errortext)} \"{errortext}\" used")
        elif errortype == "identifier":
            print(
                f"Identifier: {type(errortext)} \"{errortext}\" does not exist")
        elif errortype == "import":
            print(f"Failed to read stylesheet at: \"{errortext}\"")
        elif errortype == "read":
            print(
                f"Failed to apply style, no element exists with id: \"{errortext}\"")
        elif errortype == "apply":
            print(f"Failed to apply style: \"{errortext}\"")
        exit()

    def __color(self, input, layer):
        #Return fore and background colors
        def convert_hex(hex):
            if len(hex) == 7:
                    hex_vals = self.__hex(hex)
                    return f"{layer}8;2;{hex_vals[0]};{hex_vals[1]};{hex_vals[2]}"
            else:
                self.__error("style", f"{hex}")
        
        if type(input) is str:
            if input[0] == "#":
                #If hex
                return convert_hex(input)
            elif input in pallette:
                #If style in pallette
                key = pallette.get(input)
                if type(key) is str:
                    if key[0] == "#":
                        return convert_hex(key)
                elif type(key) is tuple:
                    return f"{layer}8;2;{key[0]};{key[1]};{key[2]}"
            else:
                #If style in standard colors
                if input in COLOURS.keys():
                    return f"{layer}8;5;{COLOURS.get(input)}"
                else:
                    self.__error("style", input)
        elif type(input) is tuple:
            #If rgb
            return f"{layer}8;2;{input[0]};{input[1]};{input[2]}"
        else:
            self.__error("argument", input)

    def __return_style(self, style):
        #Create coloured outputs
        if style[0] == "style":
            #Apply no style
            if style[1] == "none":
                return f"{self.output}{RESET}"
        else: 
            if style[0] == "color":
                self.color = self.__color(style[1], "3")
            elif style[0] == "background":
                self.background = self.__color(style[1], "4")
            elif style[0] == "font": 
                if type(style[1]) is str:
                    # Check if font exists
                    if style[1] in FONTS.keys():
                        self.font = f"{FONTS.get(style[1])}"
                    else:
                        self.__error("style", style[1])
                else:
                    self.__error("argument", style[1])
            else:
                self.__error("identifier", style[0])
            return f"{START}{self.font};{self.color};{self.background}m"

    def pallette(self, input):
        #Import color pallette
        self.output = False
        global pallette
        if type(input) == dict:
            pallette = input
        elif type(input) == str:
            if input[-3:] == "acp":
                try:
                    pallette = open(input,"r").read()
                    pallette = ast.literal_eval(pallette)
                except:
                    self.__error("import", input)
            else:
                self.__error("import", input)

    def stylesheet(self, input):
        self.output = False
        global stylesheet
        if type(input) == str:
            if input[-3:] == "ass":
                try:
                    stylesheet = open(input,"r").read().splitlines()
                    stylesheet = list(filter(None, stylesheet))
                    stylesheet = [ast.literal_eval(style) for style in stylesheet]
                except:
                    self.__error("import", input)
            else:
                self.__error("import", input)
        elif type(input) == list:
            stylesheet = input
        else:
            self.__error("import", input)

    def clear(self):
        if self.input:
            self.__error("apply", "clear()")
        else:
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

    def id(self, identifier):
        self.output = ""
        if stylesheet:
            if type(identifier) == list:
                if type(self.input) == list and len(self.input) == len(identifier):
                    for idx, id in enumerate(identifier):
                        for style in stylesheet:
                            if style.get("id") == id:
                                cropped_style = {key:style[key] for key in style if key!="id"}
                                for style in cropped_style.items():
                                    self.output += self.__return_style(style)
                                self.__rs_style()
                                self.output += f"{self.input[idx]}{RESET}"  
                else:
                    self.__error("apply", "please apply an id for every string in your input list")
            else:
                for style in stylesheet:
                    if style.get("id") == identifier:
                        cropped_style = {key:style[key] for key in style if key!="id"}
                        for style in cropped_style.items():
                            self.output += self.__return_style(style)
                        self.__rs_style()
                        self.output += f"{self.input}{RESET}"  
        else:
            self.__error("import", "no known path (try importing a stylesheet)")

    def style(self, styles):
        self.output = ""
        if type(styles) == list:
            if type(self.input) == list and len(self.input) == len(styles):
                if styles:
                    for idx, nested_ss in enumerate(styles):
                        for style in nested_ss.items():
                            self.output += self.__return_style(style)
                        self.__rs_style()
                        self.output += f"{self.input[idx]}{RESET}"    
            else:
                self.__error("apply", "please apply a style for every string in your input list")

        elif type(styles) == dict:
            if styles:
                for style in styles.items():
                    self.output += f"{self.__return_style(style)}"
                self.output += f"{self.input}"           
