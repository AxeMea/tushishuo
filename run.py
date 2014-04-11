import traceback
import sys

from core import app
try:
    app.debug = True
    if ( app.debug ):
        from werkzeug.debug import DebuggedApplication
        app.wsgi_app = DebuggedApplication( app.wsgi_app, True )
    app.run(host='0.0.0.0')
except:
    with open("/home/yuzheng/git/tushishuo/log.txt","w") as file:
        file.write(traceback.format_exc())
