from lark import Lark, InlineTransformer, Tree, Token
import images

with open('canva.cnv', 'r') as file:
    data = file.read()

grammar = Lark(r"""
?start : feed

?feed  : "feed" ":" name back elem*

?name  : "name:" NAME               -> feed_name

?back  : "background:" DIR          -> background

?elem  : "text:" text
       | "logo:" logo 

?text  : POS TEXT COLOR                 -> text

?logo  : POS DIR                        -> logo

// Terminals
POS   : /[\w]+[-]?[\w]*/
DIR   : /\'([\w]+[\/])*[\w]+[.][\w]+\'/
NAME  : /\'[\w]{1,32}\'/
TEXT  : /\'[\w\s\!\/\-]+\'/
COLOR : /[#][0-9a-fA-F]{3,6}/
%ignore /\s+/
""")

class CanvaTransformer(InlineTransformer):
    pos = str
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

    def text(self, pos, text, color):
        text = text[1:-1]
        return ('text', str(pos), str(text), str(color))
    
    def logo(self, pos, dir):
        dir = dir[1:-1]
        return ('logo', str(pos), str(dir))

def eval_canva(expr):
    head, *args = expr
    
    if head == 'feed':
        image = images.createImage(1080, 1080, '#000')
        name = None

        for arg in args:
            if (arg[0]=='name'):
                name = arg[1]
            elif (arg[0]=='back'):
                back = arg[1]
                image = images.loadImage(back)
            elif (arg[0]=='text'):
                pos = arg[1]
                text = arg[2]
                text_color = arg[3]
                image = images.textToImage(pos, image, text, 96, text_color, 'Montserrat-Bold')
            elif (arg[0]=='logo'):
                pos = arg[1]
                logo_dir = arg[2]
                logo = images.loadImage(logo_dir)
                logo = images.resizeImage(logo, 96, 96)
                logo = images.imageToImage(pos, logo, image)
            else:
                raise ValueError('Chave inválida')

        images.saveImage(image, name)
        image = images.resizeImage(image, 512, 512)
        images.showImage(image)
    else:
        raise ValueError('argumento inválido para: %r' % head)

tree = grammar.parse(data)
canva = CanvaTransformer().transform(tree)
eval_canva(canva)