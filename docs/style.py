# The name of the Pygments (syntax highlighting) style to use. https://pygments.org/docs/styles/#creating-own-styles
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic

class SQLStyle(Style):
    default_style = ""
    styles = {
        Comment:                'italic #f88',
        Keyword:                'bold #005',
        Name:                   '#f00',
        Name.Function:          '#0f0',
        Name.Class:             'bold #0f0',
        String:                 'bg:#eee #111'
    }