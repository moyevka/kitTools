# kitTools
kit = toolbar.addMenu('kitNodes', icon='kitIcon.png')
kit.addCommand('kitLUTLoader', 'nuke.createNode("kitLUTLoader")')
kit.addCommand('kitRGBInvert', 'nuke.createNode("kitRGBInvert")')
kit.addCommand("-", "", "")
kit.addCommand('kitInvReinhard', 'nuke.createNode("kitInvReinhard")')
kit.addCommand('kitReinhard', 'nuke.createNode("kitReinhard")')
kit.addCommand("-", "", "")
kit.addCommand('kitDeflicker', 'nuke.createNode("kitDeflicker")')