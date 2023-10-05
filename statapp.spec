# -*- mode: python ; coding: utf-8 -*-
import argparse
import sys
import typing
from pprint import pprint

if typing.TYPE_CHECKING:
    from PyInstaller.building.api import COLLECT, EXE, MERGE, PYZ  # noqa: F401
    from PyInstaller.building.build_main import Analysis  # noqa: F401
    from PyInstaller.building.datastruct import TOC, Target, Tree  # noqa: F401
    from PyInstaller.building.osx import BUNDLE  # noqa: F401
    from PyInstaller.building.splash import Splash  # noqa: F401

from PyInstaller.utils.hooks import copy_metadata

parser = argparse.ArgumentParser()
parser.add_argument("--one-file", action="store_true")
options = parser.parse_args()

datas = [('statapp/ui/images/*', 'ui/images')]
datas += copy_metadata('statapp')


a = Analysis(
    ['statapp/__main__.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

prev_binaries = set(a.binaries)
if sys.platform in ('linux', 'darwin'):
    a.exclude_system_libraries(list_of_exceptions=[])  # glob expression
print('\n\nSTRIPPED SYSTEM LIBS')
pprint(sorted(set(prev_binaries) - set(a.binaries)))

LOCALES = ['ru', 'en']
def remove_unused_translation(item):
    dest = str(item[0])
    if not dest.startswith('PySide2/Qt/translations'):
        return True

    for l in LOCALES:
        if l in dest:
            return True

    return False

a.datas = list(filter(remove_unused_translation, a.datas))

pyz = PYZ(a.pure)

if options.one_file:
    exe = EXE(
        pyz,
        a.scripts,
        a.binaries,
        a.datas,
        [],
        name='statapp',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        upx_exclude=[],
        runtime_tmpdir=None,
        console=False,
        disable_windowed_traceback=False,
        argv_emulation=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
        icon='statapp/ui/images/logo.ico',
    )
else:
    exe = EXE(
        pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name='statapp',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        console=False,
        disable_windowed_traceback=False,
        argv_emulation=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
        icon='statapp/ui/images/logo.ico',
    )
    coll = COLLECT(
        exe,
        a.binaries,
        a.datas,
        strip=False,
        upx=True,
        upx_exclude=[],
        name='statapp',
    )
