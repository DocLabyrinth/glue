from .css import CssFormat
from .cocos2d import Cocos2dFormat
from .img import ImageFormat
from .html import HtmlFormat
from .jsonformat import JSONFormat
from .caat import CAATFormat
from .phaser import PhaserFormat
from .less import LessFormat
from .scss import ScssFormat

formats = {'css': CssFormat,
           'cocos2d': Cocos2dFormat,
           'img': ImageFormat,
           'html': HtmlFormat,
           'json': JSONFormat,
           'caat': CAATFormat,
           'phaser': PhaserFormat,
           'less': LessFormat,
           'scss': ScssFormat}
