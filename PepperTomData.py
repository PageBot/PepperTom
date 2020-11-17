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

from pagebotnano_060.templates.sitedata import SiteData
from pagebotnano_060.toolbox.dating import now
from pagebotnano_060.themes import *
from pagebotnano_060.toolbox.color import color

class PepperTomTheme(HappyHolidays):

	logo1 = color(1)
	logo2 = color(1, 0, 0) # Red
	logo3 = color(0xEC842C)

theme = PepperTomTheme()

siteData = sd = SiteData(id='peppertom', title='Pepper+Tom', theme=theme)
sd.menuName = 'Menu'
sd.year = now().year
sd.copyright = ' | '.join((
	'<a href="https://peppertom.com" target="external">Pepper+Tom</a>',
	'<a href="https://typetr.typenetwork.com">TYPETR</a>',
	'<a href="https://designdesign.space">DesignDesign.Space</a>'))
sd.fontFamily = 'Upgrade'
sd.logo = """<span style="color:#%s;">|</span><span style="color:#%s">d</span><span style="color: #%s;">|</span>""" % (theme.logo2.hex, theme.logo1.hex, theme.logo3.hex)

sd.fontsCss = True
sd.fontFamily = 'Upgrade'
sd.logoFontFamily = 'PepperTom'
sd.monoFontFamily = 'Courier New'
sd.iconFontFamily = 'FontAwesome'
sd.menuLinks = True # Force call to template._menuLinks()

# Page index

p = sd.newPage(id='index', title='Home', template='index')

# Page index, banner

p.bannerSlideShow = True
p.bannerImage_1 = 'images/skirts/static1.squarespace.jpg'
p.bannerTitle_1 = 'Laatste rokken'
p.bannerSubtitle_1 = 'Er zijn er nog een paar'

p.bannerImage_2 = 'images/studio/IMG_9581.jpg'
p.bannerTitle_2 = 'There are still scarfs'
p.bannerSubtitle_2 = 'Get them in the shop'

p.bannerImage_3 = 'images/studio/IMG_9473.jpg'
p.bannerTitle_3 = 'Title 3'
p.bannerSubtitle_3 = 'My Banner 3@'

p.bannerImage_4 = 'images/studio/IMG_9557.jpg'
p.bannerTitle_4 = 'Title 4'
p.bannerSubtitle_4 = 'My Banner 4@'

p.bannerImage_5 = 'images/studio/IMG_9563.jpg'
p.bannerTitle_5 = 'Title 5'
p.bannerSubtitle_5 = 'My Banner 5@'

p.bannerImage_6 = 'images/studio/IMG_9566.jpg'
p.bannerTitle_6 = 'Title 6'
p.bannerSubtitle_6 = 'My Banner 6@'

p.bannerImage_7 = 'images/studio/IMG_9571.jpg'
p.bannerTitle_7 = 'Title 7'
p.bannerSubtitle_7 = 'My Banner 7@'

# Page index, subscriptionForm

p.subscriptionForm = True
p.subscriptionFormHead = 'Yes, I am interested, ...'

# Page index, article 1

p.imagesArticle = True # Trigger the template._imagesArticle call
p.articleImage_1 = 'images/scarfs/groen1-1.jpg'
p.articleSubhead_1 = 'Last ones in stock'
p.articleHead_1 = 'Skirts'
p.article_1 = """Pepper+Tom skirts are perfect basic items that should not be 
missing in your wardrobe. They are designed in various sizes, fabrics (cotton, silk and wool) different lengths and delicately fınished with a colored zipper. The skirts are made from sustainable fabrics. Semi couture by a Dutch Atelier. 

Confıdent women accentuate their individuality with their outfıt. Tough boots under a fashionable skirt. High heels under a loose dress or pants. They combine stylish and tough. They choose for comfort above catwalk, appreciating beautiful and well-made garments. They opt for Pepper+Tom. 

Quote’s by Pepper+Tom customers: ‘It’s a simple style, good model, clear!’ ‘I can wear it all day, all night, everywhere’ ‘Very flattering to many fıgure types’ 

Pepper+Tom would like to say to all women: ‘Just keep dancing!’ 

All skirts have a A-line. There are three different lengths. Skirts with and without waistbands. Iconic, centerpiece items: Last for ever!
"""
p.articleFooter_1 = 'Footer of article 1'

# Page index, article 2

p.articleImage_2 = 'images/scarfs/goud1-1.jpg'
p.articleSubhead_2 = 'Last ones in stock'
p.articleHead_2 = 'Scarves'
p.article_2 = """The scarves are the result of many peoples’ work and creativity from rural Bangladesh to the cities of the Netherlands and the shores of the United States. 
Beautiful women of Bangladesh embroider the scarves by using the traditional Nakshi Kantha technique. The silk of the scarves is made of the best quality, Rajshahi Silk. The fabric is embossed in a workplace in Dhaka and embroidered in Dinajpur, a poor region in the northwest of Bangladesh. 

All under supervision of Kumudini Welfare Trust of Bengal. This NGO is part of the World Fair Trade Forum and Ecota Fair Trade Forum. In 2008 they received the Award of Excellence for Handicrafts South Asia from Unesco. 

Under the name of Generous Gesture, the scarves have won a Bronze Award for the European Design Award 2010 in the category ‘Self Initiated Projects’ 
Generous Gesture has been nominated for the German Design Award 2012. 
Generous Gesture is a people project. Every piece we make is 100% fair trade. The principle op Generous Gesture is creating fair trade with sustainable products. Through an exchange of ideas and skills we create a win-win situation for all concerned parties. 
"""
p.articleFooter_2 = 'Footer of article 2'

# Page index, pullquote

p.pullQuote = True # Trigger the template method
p.pullQuoteImage = 'images/notes/IMG_0929.jpeg'
p.pullQuoteSubhead = 'Pullquote subhead'
p.pullQuoteHead = 'Pullquote heading' 

p.gallery = True # Trigger the template._gallery method call
p.galleryHead = 'Gallery head'
p.gallerySubhead = 'Gallery subhead'
p.galleryImage_1 = 'images/notes/IMG_0926.jpeg'
p.galleryCaption_1 = """Caption of this image. A very long one. Cras aliquet urna ut sapien tincidunt, quis malesuada elit facilisis. Vestibulum sit amet tortor velit. Nam elementum nibh a libero pharetra elementum."""
p.galleryImage_2 = 'images/notes/IMG_0929.jpeg'
p.galleryCaption_2 = 'Short caption of this image.'  
p.galleryImage_3 = 'images/notes/IMG_0933.jpeg'
p.galleryImage_4 = 'images/notes/IMG_0934.jpeg'
p.galleryImage_5 = 'images/notes/IMG_0935.jpeg'
p.galleryImage_6 = 'images/notes/IMG_0936.jpeg'

# Page otherpage

p = sd.newPage('otherpage', 'Other Page', 'article')

p.imagesArticle = False # Ignore these in the template
p.pullQuote = False

p.bannerSlideShow = True
p.bannerImage_1 = 'images/lookbook/IMG_2458.JPG'
p.bannerTitle_1 = 'Laatste rokken'
p.bannerSubtitle_1 = 'Er zijn er nog een paar'

p.bannerImage_2 = 'images/lookbook/IMG_2361.JPG'
p.bannerTitle_2 = 'Title 2'
p.bannerSubtitle_2 = 'My Banner 2@'

p.bannerImage_3 = 'images/lookbook/IMG_0966.jpg'
p.bannerTitle_3 = 'Title 3'
p.bannerSubtitle_3 = 'My Banner 3@'

p.bannerImage_4 = 'images/lookbook/IMG_0861.jpg'
p.bannerTitle_4 = 'Title 4'
p.bannerSubtitle_4 = 'My Banner 4@'

p.bannerImage_5 = 'images/lookbook/IMG_0860.jpg'
p.bannerTitle_5 = 'Title 5'
p.bannerSubtitle_5 = 'My Banner 5@'

p.bannerImage_6 = 'images/lookbook/IMG_7719.jpg'
p.bannerTitle_6 = 'Laatste rokken'
p.bannerSubtitle_6 = 'Er zijn er nog een paar'

p.gallery = True # Trigger the template._gallery method call
p.galleryHead = 'Gallery head'
p.gallerySubhead = 'Gallery subhead'
p.galleryImage_1 = 'images/notes/IMG_0926.jpeg'
p.galleryCaption_1 = """Caption of this image. A very long one. Cras aliquet urna ut sapien tincidunt, quis malesuada elit facilisis. Vestibulum sit amet tortor velit. Nam elementum nibh a libero pharetra elementum."""
p.galleryImage_2 = 'images/notes/IMG_0929.jpeg'
p.galleryCaption_2 = 'Short caption of this image.'  
p.galleryImage_3 = 'images/notes/IMG_0933.jpeg'
p.galleryImage_4 = 'images/notes/IMG_0934.jpeg'
p.galleryImage_5 = 'images/notes/IMG_0935.jpeg'
p.galleryImage_6 = 'images/notes/IMG_0936.jpeg'

# Page thirdpage

p = sd.newPage('thirdpage', 'Third page', 'index')

p.imagesArticle = False
p.pullQuote = False
p.gallery = False

p.bannerSlideShow = True
p.bannerImage_1 = 'images/lookbook/IMG_2458.JPG'
p.bannerTitle_1 = 'Laatste rokken'
p.bannerSubtitle_1 = 'Er zijn er nog een paar'

p.bannerImage_2 = 'images/lookbook/IMG_2361.JPG'
p.bannerTitle_2 = 'Title 2'
p.bannerSubtitle_2 = 'My Banner 2@'

p.bannerImage_3 = 'images/lookbook/IMG_0966.jpg'
p.bannerTitle_3 = 'Title 3'
p.bannerSubtitle_3 = 'My Banner 3@'

p.bannerImage_4 = 'images/lookbook/IMG_0861.jpg'
p.bannerTitle_4 = 'Title 4'
p.bannerSubtitle_4 = 'My Banner 4@'

p.bannerImage_5 = 'images/lookbook/IMG_0860.jpg'
p.bannerTitle_5 = 'Title 5'
p.bannerSubtitle_5 = 'My Banner 5@'

p.bannerImage_6 = 'images/lookbook/IMG_7719.jpg'
p.bannerTitle_6 = 'Laatste rokken'
p.bannerSubtitle_6 = 'Er zijn er nog een paar'
	
# Page fourthpage

p = sd.newPage('fourthpage', 'Fourth page', 'elements')

p.bannerSlideShow = True
p.bannerImage_1 = 'images/lookbook/IMG_2458.JPG'
p.bannerTitle_1 = 'Laatste rokken'
p.bannerSubtitle_1 = 'Er zijn er nog een paar'

p.bannerImage_2 = 'images/lookbook/IMG_2361.JPG'
p.bannerTitle_2 = 'Title 2'
p.bannerSubtitle_2 = 'My Banner 2@'

p.bannerImage_3 = 'images/lookbook/IMG_0966.jpg'
p.bannerTitle_3 = 'Title 3'
p.bannerSubtitle_3 = 'My Banner 3@'

p.bannerImage_4 = 'images/lookbook/IMG_0861.jpg'
p.bannerTitle_4 = 'Title 4'
p.bannerSubtitle_4 = 'My Banner 4@'

p.bannerImage_5 = 'images/lookbook/IMG_0860.jpg'
p.bannerTitle_5 = 'Title 5'
p.bannerSubtitle_5 = 'My Banner 5@'

p.bannerImage_6 = 'images/lookbook/IMG_7719.jpg'
p.bannerTitle_6 = 'Laatste rokken'
p.bannerSubtitle_6 = 'Er zijn er nog een paar'
	
p = sd.newPage(id='article', title='Article', template='article')

# Options in generic templates
#	{{articlePageHeader}}
#	{{article1}}
#	{{pullQuote2}}
#	{{article2}}
# 	{{pullQuote3}}
#	{{article3}}
#	{{gallery}}

p.articlePageHeader = True # Make the call to website._articlePageHeader(siteData, pageData) available.
p.articlePageHeaderSubhead = 'Article page header subhead'
p.articlePageHeaderTitle = 'Article page title'

p.article = True 
p.articleSubhead = 'Article subhead'
p.articleHead = 'Article head'
p.articleText = 'Article text. '*100

p.pullQuote = True # Trigger the template method
p.pullQuoteImage = 'images/notes/IMG_0929.jpeg'
p.pullQuoteSubhead = 'Pullquote subhead 1'
p.pullQuoteHead = 'Pullquote heading 1' 

p.article_1 = True 
p.articleSubhead_1 = 'Article subhead2'
p.articleHead_1 = 'Article head2'
p.articleText_1 = 'Article text2. '*100

p.pullQuote_1 = True # Trigger the template method
p.pullQuoteImage_1 = 'images/notes/IMG_0929.jpeg'
p.pullQuoteSubhead_1 = 'Pullquote subhead 1'
p.pullQuoteHead_1 = 'Pullquote heading 1' 

p.article_2 = False
p.pullQuote_2 = False
p.gallery = False # Ignore the template._gallery method call

p = sd.newPage(id='article1', title='Article', template='article1')

p = sd.newPage(id='gallery', title='Article', template='gallery')

