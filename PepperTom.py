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
#   PepperTom.py
#
#   Source builds the PepperTom.com website using PageBotNano the Website 
#   publication class.
#
"""
    >>> theme = BackToTheCity()
    >>> title = randomTitle()
    >>> author = randomName()
    >>> siteName = 'pagebotnano_demo'
    >>> pageData = parseMarkdownFile('../../TestPageContent.md')
    >>> #pageData = parseMarkdownFile('../../PublishingVariables.md')
    >>> templatePath = 'templated-hielo'
    >>> templates = Templated(templatePath)
    >>> website = Website(theme=theme, templates=templates)
    >>> website.templates is templates
    True
    >>> website.compose(pageData)
    >>> # Start MAMP to see this website on localhost, port 80
    >>> website.export(website.MAMP_PATH + siteName)
    >>> url = 'http:localhost:%d/%s' % (website.PORT or 80, siteName) 
    >>> result = os.system(u'/usr/bin/open %s' % url)
"""


import os
from pagebotnano_060.toolbox.loremipsum import loremipsum, randomName, randomTitle
from pagebotnano_060.templates.templated import Templated
from pagebotnano_060.themes import BackToTheCity
from pagebotnano_060.toolbox.markdown import parseMarkdownFile
from pagebotnano_060.publications.website import Website

PORT = 8888
markdownPath = 'PepperTom.md'
templatePath = 'templated-hielo'

theme = BackToTheCity()

siteName = 'peppertom'

# Create a Website publications with this theme and templates
templates = Templated(templatePath)
print(templates.path)
website = Website(theme=theme, templates=templates, port=PORT)

# Get dictionary if pages[pageData.id] = pageData
pageData = parseMarkdownFile(markdownPath)

# Compose the website with this content.
website.compose(pageData)

# Start MAMP to see this website on localhost, port 80
website.export(website.MAMP_PATH + siteName) 
os.system(u'/usr/bin/open %s/%s' % (website.url, siteName))

print('Done')