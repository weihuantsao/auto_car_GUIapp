from distutils.core import setup
import py2exe
 
setup(
    options = {'py2exe': {
        'bundle_files': 1,
        'compressed': True,
        'includes' : ['sip','main']
    }},
    data_files=[("icon",
                 ["icon/cancel-icon.png",
                  "icon/refresh-page-option.png",
                  "icon/index.ico"]),
                ("help",
                 ["help/about_app"]),
                ("",
                 ["help/wget.exe",
                  "current_version.ini",
                  "checkupdate.bat",
                  "upgrade.bat"])
                ],
    console = [{'script': 'main.py',"icon_resources": [(1, "icon/index.ico")]}],
    windows = [{'script': 'main.py',
                "icon_resources":[(1,"icon/index.ico")],
                "dest_base":"auto_car"
               }],
    zipfile = None
)
