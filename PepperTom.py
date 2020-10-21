#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#   P A G E B O T  N A N O
#
#   Copyright (c) 2020+ Buro Petr van Blokland + Claudia Mens
#   www.pagebot.io
#   Licensed under MIT conditions
#
#   Supporting DrawBot, www.drawbot.com
# -----------------------------------------------------------------------------
#
#   ThemeSpecimens.py
#
#   This ThemeColors.py shows samples of all standard theme colors,
#   with their closest spot color, CMYK, RGB, CSS hex-color and CSS name.
#
from pagebotnano_060.toolbox.markdown import parseMarkdownFile


PATH = 'PepperTom.md'

pages = parseMarkdownFile(PATH)

print(pages)

page = pages['home']

print(page.elementData)

print('Done')