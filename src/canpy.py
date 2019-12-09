from lark import Lark, InlineTransformer, Tree, Token
import images

with open('canva.cnv', 'r') as file:
    data = file.read()

grammar = Lark(r"""
?start : feed

?feed  : "feed" ":" name back

?name  : "name:" "'" NAME "'"      -> feed_name

?back  : "background:" "'" DIR "'" -> background

// Terminals
NAME : /[\w]+/
DIR  : /([\w]+[\/])*[\w]+[.][\w]+/
%ignore /\s+/
""")

class CanvaTransformer(InlineTransformer):
    name = str
    dir = str

    def feed(self, *args):
        return ('feed', *args)

    def feed_name(self, name):
        return ('name', str(name))

    def background(self, dir):
        return ('back', str(dir))

def eval_canva(expr):
    head, *args = expr
    
    if head == 'feed':
        info = []
        for arg in args:
            info.append(eval_canva(arg))
        
        name = info[0]
        directory = info[1]

        image = images.loadImage(directory)
        images.saveImage(image, name)
        images.showImage(image)
    elif head == 'name':
        return args[0]
    elif head == 'back':
        return args[0]
    else:
        raise ValueError('argumento inválido para: %r' % head)


tree = grammar.parse(data)
canva = CanvaTransformer().transform(tree)
eval_canva(canva)