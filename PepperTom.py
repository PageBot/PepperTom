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
import os

from pagebotnano_060.toolbox.markdown import parseMarkdownFile
from pagebotnano_060.templates.templated import Templated
from pagebotnano_060.themes import BackToTheCity
from pagebotnano_060.publications.website import Website

markdownPath = 'PepperTom.md'
templatePath = 'templates/templated-hielo'

theme = BackToTheCity()

siteName = 'peppertom'

# Create a Website publications with this theme and templates
templates = Templated(templatePath)
website = Website(theme=theme, templates=templates)

# Get dictionary if pages[pageData.id] = pageData
pages = parseMarkdownFile(markdownPath)

# Compose the website with this content.
website.compose(pages)

# Start MAMP to see this website on localhost, port 80
website.export(website.MAMP_PATH + siteName) 
os.system(u'/usr/bin/open %s/%s' % (website.url, siteName))

print('Done')