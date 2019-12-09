from lark import Lark, InlineTransformer, Tree, Token
import images

with open('canva.cnv', 'r') as file:
    data = file.read()

grammar = Lark(r"""
?start : feed

?feed  : "feed" ":" name back elem?

?name  : "name:" NAME               -> feed_name

?back  : "background:" DIR          -> background

?elem  : "center:" mode

?mode  : "text" TEXT COLOR          -> text

// Terminals
DIR   : /\'([\w]+[\/])*[\w]+[.][\w]+\'/
NAME  : /\'[\w]+\'/
TEXT  : /\'[\w\s]+\'/
COLOR : /[#][0-9a-fA-F]{3,6}/
%ignore /\s+/
""")

class CanvaTransformer(InlineTransformer):
    dir = str
    name = str
    text = str
    color = str

    def feed(self, *args):
        return ('feed', *args)

    def feed_name(self, name):
        name = name[1:-1]
        return ('name', str(name))

    def background(self, dir):
        dir = dir[1:-1]
        return ('back', str(dir))

    def text(self, text, color):
        text = text[1:-1]
        return ('text', str(text), str(color))

def eval_canva(expr):
    head, *args = expr
    
    if head == 'feed':
        feed_info = []
        for arg in args:
            feed_info.append(eval_canva(arg))

        print(feed_info[2][0])
        
        name = feed_info[0]
        directory = feed_info[1]
        text = feed_info[2][0]
        text_color = feed_info[2][1]

        image = images.loadImage(directory)
        image = images.textToImage('center', image, text, 96, text_color, 'Montserrat-Bold')
        images.saveImage(image, name)
        images.showImage(image)
    elif head == 'name':
        return args[0]
    elif head == 'back':
        return args[0]
    elif head == 'text':
        return args
    else:
        raise ValueError('argumento inválido para: %r' % head)

tree = grammar.parse(data)
canva = CanvaTransformer().transform(tree)
eval_canva(canva)