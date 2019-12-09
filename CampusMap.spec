# -*- mode: python -*-

block_cipher = None


a = Analysis(['CampusMap.py'],
         pathex=['C:\\Users\\User\\Desktop\\CampusMap'],
         binaries=[],
         datas=[
         ("C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\branca\\*.json","branca"),
         ("C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\branca\\templates","templates"),
         ("C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\folium\\templates","templates"),
         ],
         hiddenimports=[],
         hookspath=[],
         runtime_hooks=[],
         excludes=[],
         win_no_prefer_redirects=False,
         win_private_assemblies=False,
         cipher=block_cipher,
         noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
         cipher=block_cipher)
exe = EXE(pyz,
      a.scripts,
      a.binaries,
      a.zipfiles,
      a.datas,
      [],
      name='CampusMap',
      debug=False,
      bootloader_ignore_signals=False,
      strip=False,
      upx=True,
      runtime_tmpdir=None,
      console=False )