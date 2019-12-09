from lark import Lark, InlineTransformer, Tree, Token

grammar = Lark(r"""
?start : block

?block : type ":" name back

?type  : "feed"

?name  : "name:" "'" NAME "'"

?back  : "background:" "'" DIR "'"

// Terminals
NAME : /[\w\s]+/
DIR  : /([\w]+[\/])*[\w]+[.][\w]+/
%ignore /\s+/

""")

print_parser = grammar.parse("""
feed:
    name: 'Novo post'
    background: 'img/background.jpg'
""")

print(print_parser)