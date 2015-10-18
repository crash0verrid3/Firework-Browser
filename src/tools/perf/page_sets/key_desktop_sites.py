# Copyright 2014 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
from telemetry.page import page as page_module
from telemetry import story


class KeyDesktopSitesPage(page_module.Page):

  def __init__(self, url, page_set):
    super(KeyDesktopSitesPage, self).__init__(
        url=url, page_set=page_set, credentials_path = 'data/credentials.json')
    self.archive_data_file = 'data/key_desktop_sites.json'

  def RunPageInteractions(self, action_runner):
    with action_runner.CreateGestureInteraction('ScrollAction'):
      action_runner.ScrollPage()


class FacebookPage(KeyDesktopSitesPage):

  def __init__(self, page_set):
    super(FacebookPage, self).__init__(
      url='http://facebook.com',
      page_set=page_set)

    self.credentials = 'facebook'


class GmailPage(KeyDesktopSitesPage):

  def __init__(self, page_set):
    super(GmailPage, self).__init__(
      url='https://mail.google.com/mail/',
      page_set=page_set)

    self.scrollable_element_function = '''
      function(callback) {
        gmonkey.load('2.0', function(api) {
          callback(api.getScrollableElement());
        });
      }'''
    self.credentials = 'google'

  def RunPageInteractions(self, action_runner):
    with action_runner.CreateGestureInteraction('ScrollAction'):
      action_runner.ScrollPage()
    action_runner.WaitForJavaScriptCondition(
        'window.gmonkey !== undefined && '
        'document.getElementById("gb") !== null')


class GoogleCalendarPage(KeyDesktopSitesPage):

  def __init__(self, page_set):
    super(GoogleCalendarPage, self).__init__(
      url='https://www.google.com/calendar/',
      page_set=page_set)

    self.scrollable_element_function = '''
      function(callback) {
        callback(document.getElementById('scrolltimedeventswk'));
      }'''
    self.credentials = 'google'


class GoogleDrivePage(KeyDesktopSitesPage):

  def __init__(self, page_set):
    super(GoogleDrivePage, self).__init__(
      url='https://drive.google.com',
      page_set=page_set)

    self.scrollable_element_function = '''
      function(callback) {
        callback(document.getElementsByClassName('doclistview-list')[0]);
      }'''
    self.credentials = 'google'

  def RunPageInteractions(self, action_runner):
    with action_runner.CreateGestureInteraction('ScrollAction'):
      action_runner.ScrollPage()
    action_runner.WaitForJavaScriptCondition(
        'document.getElementsByClassName("doclistview-list").length')


class GoogleDocPage(KeyDesktopSitesPage):

  def __init__(self, page_set):
    super(GoogleDocPage, self).__init__(
      # pylint: disable=C0301
      url='https://docs.google.com/a/google.com/document/d/1XMAtPiVFZfItsMUOYl39v5YA8bcSPe4LDrVO25OdsCU/edit',
      page_set=page_set)

    self.scrollable_element_function = '''
      function(callback) {
        callback(document.getElementsByClassName('kix-appview-editor')[0]);
      }'''
    self.credentials = 'google'

  def RunPageInteractions(self, action_runner):
    with action_runner.CreateGestureInteraction('ScrollAction'):
      action_runner.ScrollPage()
    action_runner.WaitForJavaScriptCondition(
        'document.getElementsByClassName("kix-appview-editor").length')


class KeyDesktopSitesPageSet(story.StorySet):

  """ Sites of Interest """

  def __init__(self):
    super(KeyDesktopSitesPageSet, self).__init__(
      archive_data_file='data/key_desktop_sites.json',
      cloud_storage_bucket=story.PARTNER_BUCKET)

    self.AddStory(FacebookPage(self))
    self.AddStory(GmailPage(self))
    self.AddStory(GoogleCalendarPage(self))
    self.AddStory(GoogleDrivePage(self))
    self.AddStory(GoogleDocPage(self))

    urls_list = [
      'http://www.google.com/nexus/5/#/',
      'http://youtube.com',
      'http://twitter.com/nbc',
      'http://bbc.co.uk',
      'http://imdb.com',
      'http://espn.go.com',
      'http://cnn.com',
      'http://bbc.co.uk/news/',
      'http://weather.com',
      'http://livejournal.com',
      'http://deviantart.com',
      'http://foxnews.com',
      'http://nbcnews.com',
      'http://scribd.com',
      'http://movies.yahoo.com',
      'http://tv.yahoo.com',
      'http://pandora.com',
      'http://tmz.com',
      'http://hulu.com',
      'http://abcnews.go.com',
      'http://youtube.com/videos',
      'http://ndtv.com',
      'http://money.cnn.com',
      'http://msn.foxsports.com',
      'http://cbsnews.com',
      'http://wired.com',
      'http://cnbc.com',
      'http://sportsillustrated.cnn.com',
      'http://home.disney.go.com',
      'http://urbandictionary.com',
      'http://rottentomatoes.com',
      'http://foodnetwork.com',
      'http://npr.org',
      'http://gawker.com',
      'http://last.fm',
      'http://sky.com',
      'http://eonline.com',
      'http://egotastic.com',
      'http://copyscape.com',
      'http://mtv.com',
      'http://ultimate-guitar.com',
      'http://comcast.com',
      'http://cbc.ca',
      'http://fanfiction.net',
      'http://discovery.com',
      'http://deezer.com',
      'http://metrolyrics.com',
      'http://foxnews.com/entertainment/',
      'http://cartoonnetwork.com',
      'http://paypal.com',
      'http://finance.yahoo.com',
      'http://alibaba.com',
      'http://bankofamerica.com',
      'http://www.chase.com/',
      'http://wellsfargo.com',
      'http://skype.com',
      'http://online.wsj.com',
      'http://indeed.com',
      'http://samsung.com',
      'http://reuters.com',
      'http://ups.com',
      'http://forbes.com',
      'http://clickbank.com',
      'http://target.com',
      'http://att.com',
      'http://cj.com',
      'http://constantcontact.com',
      'http://ezinearticles.com',
      'http://shutterstock.com',
      'http://americanexpress.com',
      'http://freelancer.com',
      'http://istockphoto.com',
      'http://fedex.com',
      'http://verizonwireless.com',
      'http://capitalone.com',
      'http://bloomberg.com',
      'http://monster.com',
      'http://hdfcbank.com',
      'http://fotolia.com',
      'http://thesun.co.uk',
      'http://zillow.com',
      'http://nokia.com',
      'http://tradedoubler.com',
      'http://icicibank.com',
      'http://123rf.com',
      'http://elance.com',
      'http://icbc.com.cn',
      'http://news.cnet.com',
      'http://verizon.com',
      'http://careerbuilder.com',
      'http://sears.com',
      'http://getresponse.com',
      'http://sitesell.com',
      'http://manta.com',
      'http://www.blogger.com/',
      'http://avg.com',
      'http://google.com/analytics/',
      'http://go.com',
      'http://flickr.com',
      'http://aol.com',
      'http://thepiratebay.se',
      'http://zedo.com',
      'http://about.com',
      'http://stackoverflow.com',
      'http://godaddy.com',
      'http://mediafire.com',
      'http://wordpress.org',
      'http://adwords.google.com',
      'http://imgur.com',
      'http://4shared.com',
      'http://vimeo.com',
      'http://play.google.com/',
      'http://badoo.com',
      'http://aweber.com',
      'http://mozilla.org',
      'http://www.stumbleupon.com/stumbler/chimacintosh',
      'http://www.google.com/adsense/',
      'http://my.yahoo.com',
      'http://sourceforge.net',
      'http://answers.com',
      'http://wordpress.org/extend/plugins/',
      'http://photobucket.com',
      'http://clicksor.com',
      'http://google.com/reader/',
      'http://store.apple.com',
      'http://wikia.com',
      'http://statcounter.com',
      'http://fiverr.com',
      'http://slideshare.net',
      'http://salesforce.com',
      'http://myspace.com',
      'http://hootsuite.com',
      'http://domaintools.com',
      'http://rediff.com',
      'http://soundcloud.com',
      'http://download.cnet.com',
      'http://archive.org',
      'http://filestube.com',
      'http://developers.facebook.com',
      'http://hostgator.com',
      'http://battle.net',
      'http://pch.com',
      'http://ign.com',
      'http://pogo.com',
      'http://miniclip.com',
      'http://888.com',
      'http://gamespot.com',
      'http://steampowered.com',
      'http://gamefaqs.com',
      'http://xbox.com',
      'http://games.yahoo.com',
      'http://betfair.com',
      'http://kongregate.com',
      'http://ea.com',
      'http://leagueoflegends.com',
      'http://roblox.com',
      'http://williamhill.com',
      'http://playstation.com',
      'http://wowhead.com',
      'http://king.com',
      'http://minecraft.net',
      'http://chess.com',
      'http://minecraftwiki.net',
      'http://addictinggames.com',
      'http://mmo-champion.com',
      'http://runescape.com',
      'http://travian.com',
      'http://zone.msn.com',
      'http://ubi.com',
      'http://calottery.com',
      'http://freeonlinegames.com',
      'http://games.com',
      'http://n4g.com',
      'http://nvidia.com',
      'http://callofduty.com',
      'http://us.playstation.com',
      'http://bet-at-home.com',
      'http://gametrailers.com',
      'http://teamliquid.net',
      'http://nick.com/games/',
      'http://planetminecraft.com',
      'http://nintendo.com',
      'http://popcap.com',
      'http://gamehouse.com',
      'http://curse.com',
      'http://bulbagarden.net',
      'http://rockstargames.com',
      'http://partycasino.com',
      'http://square-enix.com',
      'http://perfectworld.com',
      'http://nih.gov',
      'http://webmd.com',
      'http://ncbi.nlm.nih.gov/pubmed/',
      'http://focusoncrohnsdisease.com',
      'http://mayoclinic.com',
      'http://mercola.com',
      'http://drugs.com',
      'http://menshealth.com',
      'http://nlm.nih.gov/medlineplus/',
      'http://weightwatchers.com',
      'http://cdc.gov',
      'http://caloriecount.about.com',
      'http://patents.uspto.gov',
      'http://psychologytoday.com',
      'http://nhs.uk',
      'http://medscape.com',
      'http://foxnews.com/health/',
      'http://who.int',
      'http://healthboards.com',
      'http://self.com',
      'http://health.com',
      'http://kidshealth.org',
      'http://fda.gov',
      'http://netdoctor.co.uk',
      'http://prevention.com',
      'http://makeupalley.com',
      'http://stevepavlina.com',
      'http://realage.com',
      'http://fitnessmagazine.com',
      'http://healthcentral.com',
      'http://rxlist.com',
      'http://vitals.com',
      'http://totalbeauty.com',
      'http://nuance.com',
      'http://telegraph.co.uk/health/',
      'http://drbatras.com',
      'http://emedtv.com',
      'http://bmj.com',
      'http://medcohealth.com',
      'http://webmd.com/skin-problems-and-treatments/default.htm',
      'http://tums.ac.ir',
      'http://apa.org',
      'http://cancer.org',
      'http://healthguru.com',
      'http://earthclinic.com',
      'http://curezone.com',
      'http://beauty.about.com',
      'http://www.kaiserpermanente.org/',
      'http://drweil.com',
      'http://24hourfitness.com',
      'http://ehow.com',
      'http://yelp.com',
      'http://groupon.com/san-francisco',
      'http://engadget.com',
      'http://gsmarena.com',
      'http://reviews.cnet.com',
      'http://allrecipes.com',
      'http://autos.yahoo.com',
      'http://shopping.yahoo.com',
      'http://gizmodo.com',
      'http://marketwatch.com',
      'http://babycenter.com',
      'http://nextag.com',
      'http://fixya.com',
      'http://dpreview.com',
      'http://tomshardware.com',
      'http://theverge.com',
      'http://instructables.com',
      'http://cafemom.com',
      'http://google.com/products',
      'http://bbb.org',
      'http://shopping.com',
      'http://irs.gov',
      'http://kbb.com',
      'http://retailmenot.com',
      'http://edmunds.com',
      'http://mobile9.com',
      'http://bankrate.com',
      'http://fatwallet.com',
      'http://fool.com',
      'http://hgtv.com',
      'http://coupons.com',
      'http://apartmenttherapy.com',
      'http://phonearena.com',
      'http://shopzilla.com',
      'http://marthastewart.com',
      'http://consumerreports.org',
      'http://pricegrabber.com',
      'http://epinions.com',
      'http://cooks.com',
      'http://bhg.com',
      'http://mouthshut.com',
      'http://travel.state.gov',
      'http://realsimple.com',
      'http://opendns.com',
      'http://gardenweb.com',
      'http://blu-ray.com',
      'http://thesaurus.com',
      'http://espncricinfo.com',
      'http://weebly.com',
      'http://bbc.co.uk/sport/0/football/',
      'http://y8.com',
      'http://xe.com/ucc/',
      'http://timeanddate.com',
      'http://soccernet.espn.go.com',
      'http://howstuffworks.com',
      'http://en.wikipedia.org/wiki/Main_Page',
      'http://reverso.net',
      'http://timeanddate.com/worldclock/',
      'http://sitepoint.com',
      'http://usopen.org',
      'http://stardoll.com',
      'http://london2012.com',
      'http://lego.com',
      'http://000webhost.com',
      'http://fifa.com',
      'http://uefa.com',
      'http://nick.com',
      'http://girlsgogames.com',
      'http://pbskids.org',
      'http://thestar.com',
      'http://dynamicdrive.com',
      'http://nickjr.com',
      'http://manutd.com',
      'http://earthquake.usgs.gov',
      'http://khanacademy.org',
      'http://barbie.com',
      'http://sciencedaily.com',
      'http://gocomics.com',
      'http://webdeveloper.com',
      'http://www2.warnerbros.com',
      'http://jpl.nasa.gov',
      'http://yola.com',
      'http://bom.gov.au',
      'http://nationalpost.com',
      'http://booking.com',
      'http://tripadvisor.com',
      'http://agoda.com',
      'http://xe.com',
      'http://expedia.com',
      'http://metacafe.com',
      'http://priceline.com',
      'http://southwest.com',
      'http://cracked.com',
      'http://kayak.com',
      'http://travelocity.com',
      'http://united.com',
      'http://delta.com',
      'http://ryanair.com',
      'http://lonelyplanet.com',
      'http://orbitz.com',
      'http://aa.com',
      'http://easyjet.com',
      'http://hilton.com',
      'http://travel.yahoo.com',
      'http://marriott.com',
      'http://couchsurfing.org',
      'http://hotwire.com',
      'http://autoblog.com',
      'http://lufthansa.com',
      'http://theonion.com',
      'http://britishairways.com',
      'http://travelzoo.com',
      'http://ebaumsworld.com',
      'http://emirates.com',
      'http://venere.com',
      'http://wikitravel.org',
      'http://jal.co.jp',
      'http://collegehumor.com',
      'http://ford.com',
      'http://vrbo.com',
      'http://opentable.com',
      'http://hyatt.com',
      'http://klm.com',
      'http://airberlin.com',
      'http://usairways.com',
      'http://skyscanner.net',
      'http://timeout.com',
      'http://homeaway.com',
      'http://lonelyplanet.com/thorntree/',
      'http://virgin-atlantic.com',
      'http://news.yahoo.com',
      'http://huffingtonpost.com',
      'http://news.google.com',
      'http://reddit.com',
      'http://guardian.co.uk',
      'http://timesofindia.indiatimes.com',
      'http://washingtonpost.com',
      'http://usatoday.com',
      'http://drudgereport.com',
      'http://latimes.com',
      'http://wunderground.com',
      'http://accuweather.com',
      'http://examiner.com',
      'http://news.com.au',
      'http://time.com',
      'http://alarabiya.net',
      'http://businessweek.com',
      'http://smh.com.au',
      'http://weather.yahoo.com',
      'http://foxnews.com/politics/',
      'http://economictimes.indiatimes.com',
      'http://nationalgeographic.com',
      'http://ft.com',
      'http://nypost.com',
      'http://sfgate.com',
      'http://topix.com',
      'http://hindustantimes.com',
      'http://chicagotribune.com',
      'http://newsmax.com',
      'http://breitbart.com',
      'http://economist.com',
      'http://theatlantic.com',
      'http://prweb.com',
      'http://theglobeandmail.com',
      'http://answers.yahoo.com',
      'http://wiki.answers.com',
      'http://wordreference.com',
      'http://thefreedictionary.com',
      'http://dict.leo.org',
      'http://w3.org',
      'http://nlm.nih.gov',
      'http://goodreads.com',
      'http://mapquest.com',
      'http://yellowpages.com',
      'http://wiktionary.org',
      'http://dict.cc',
      'http://bing.com/maps/',
      'http://whitepages.com',
      'http://m-w.com',
      'http://classmates.com',
      'http://blackboard.com',
      'http://justanswer.com',
      'http://mit.edu',
      'http://medterms.com',
      'http://stanford.edu',
      'http://brainyquote.com',
      'http://harvard.edu',
      'http://superpages.com',
      'http://mylife.com',
      'http://en.wiktionary.org',
      'http://investopedia.com',
      'http://lumosity.com',
      'http://phoenix.edu',
      'http://berkeley.edu',
      'http://ecollege.com',
      'http://ed.gov',
      'http://yellowpages.sulekha.com',
      'http://wisegeek.com',
      'http://utexas.edu',
      'http://wwp.greenwichmeantime.com',
      'http://cornell.edu',
      'http://psu.edu',
      'http://maps.yahoo.com',
      'http://linkedin.com/answers',
      'http://yahoo.co.jp',
      'http://translate.google.com',
      'http://noaa.gov',
      'http://ncbi.nlm.nih.gov',
      'http://nhc.noaa.gov',
      'http://ted.com',
      'http://jma.go.jp',
      'http://usgs.gov',
      'http://care2.com',
      'http://sciencedirect.com',
      'http://intellicast.com',
      'http://guardian.co.uk/technology',
      'http://nature.com',
      'http://wunderground.com/tropical/',
      'http://ieee.org',
      'http://elsevier.com',
      'http://usda.gov',
      'http://redorbit.com',
      'http://scientificamerican.com',
      'http://nps.gov',
      'http://metoffice.gov.uk',
      'http://space.com',
      'http://foreignpolicy.com',
      'http://bbc.co.uk/news/technology/',
      'http://newscientist.com',
      'http://livescience.com',
      'http://jstor.org',
      'http://mnn.com',
      'http://foxnews.com/scitech/',
      'http://census.gov',
      'http://epa.gov',
      'http://bls.gov',
      'http://metric-conversions.org',
      'http://news.nationalgeographic.com/index.rss',
      'http://bbc.co.uk/news/science_and_environment/',
      'http://colorado.edu',
      'http://popsci.com',
      'http://amazon.com',
      'http://ebay.com',
      'http://netflix.com',
      'http://amazon.co.uk',
      'http://walmart.com',
      'http://ikea.com',
      'http://bestbuy.com',
      'http://multiply.com',
      'http://newegg.com',
      'http://homedepot.com',
      'http://macys.com',
      'http://livingsocial.com',
      'http://gap.com',
      'http://bodybuilding.com',
      'http://kohls.com',
      'http://barnesandnoble.com',
      'http://lowes.com',
      'http://zappos.com',
      'http://overstock.com',
      'http://legacy.com',
      'http://staples.com',
      'http://shutterfly.com',
      'http://nike.com',
      'http://nordstrom.com',
      'http://pixmania.com',
      'http://costco.com',
      'http://bhphotovideo.com',
      'http://hm.com',
      'http://ticketmaster.com',
      'http://jcpenney.com',
      'http://walgreens.com',
      'http://qvc.com',
      'http://autotrader.com',
      'http://tigerdirect.com',
      'http://trademe.co.nz',
      'http://sony.com',
      'http://directv.com',
      'http://buy.com',
      'http://victoriassecret.com',
      'http://cars.com',
      'http://gamestop.com',
      'http://cvs.com',
      'http://dealextreme.com',
      'http://cafepress.com',
      'http://6pm.com',
      'http://facebook.com/home.php#!/OccupyAirForce',
      'http://deviantart.com/#catpath=anthro',
      'http://shine.yahoo.com',
      'http://match.com',
      'http://siteadvisor.com',
      'http://digg.com',
      'http://hi5.com',
      'http://ancestry.com',
      'http://sulekha.com',
      'http://europa.eu',
      'http://biblegateway.com',
      'http://slate.com',
      'http://correios.com.br',
      'http://wonderwall.msn.com',
      'http://change.org',
      'http://state.gov',
      'http://salon.com',
      'http://askmen.com',
      'http://infowars.com',
      'http://wnd.com',
      'http://ec.europa.eu',
      'http://justjared.com',
      'http://sheknows.com',
      'http://slashdot.org',
      'http://newgrounds.com',
      'http://weeklystandard.com',
      'http://royalmail.com',
      'http://snopes.com',
      'http://lds.org',
      'http://dailykos.com',
      'http://complex.com',
      'http://avaaz.org',
      'http://aarp.org',
      'http://theregister.co.uk',
      'http://creativecommons.org',
      'http://jw.org',
      'http://peoplesmart.com',
      'http://uspto.gov',
      'http://uscis.gov',
      'http://whitehouse.gov',
      'http://townhall.com',
      'http://sec.gov',
      'http://sports.yahoo.com',
      'http://nfl.com',
      'http://mlb.mlb.com',
      'http://cbssports.com',
      'http://bleacherreport.com',
      'http://livescore.com',
      'http://espn.go.com/nfl/',
      'http://sports.yahoo.com/nfl',
      'http://espn.go.com/mlb/',
      'http://premierleague.com',
      'http://skysports.com',
      'http://sports.yahoo.com/mlb',
      'http://games.espn.go.com/frontpage',
      'http://uk.eurosport.yahoo.com',
      'http://baseball.fantasysports.yahoo.com',
      'http://baseball.fantasysports.yahoo.com/b1',
      'http://skysports.com/football/',
      'http://nba.com',
      'http://hattrick.org',
      'http://wwe.com',
      'http://telegraph.co.uk/sport/',
      'http://rivals.com',
      'http://sports.yahoo.com/fantasy',
      'http://espn.go.com/nba/',
      'http://scout.com',
      'http://msn.foxsports.com/nfl',
      'http://sports.yahoo.com/nfl/players/',
      'http://guardian.co.uk/football',
      'http://rotoworld.com',
      'http://nascar.com',
      'http://arsenal.com',
      'http://formula1.com',
      'http://yardbarker.com',
      'http://pgatour.com',
      'http://rei.com',
      'http://liverpoolfc.tv',
      'http://deadspin.com',
      'http://sbnation.com',
      'https://www.google.com',
      'https://www.google.com/search?q=barack%20obama',
      'https://maps.google.com',
      'http://reader.google.com',
      'https://plus.google.com/110031535020051778989/posts/2wP4KPPBMG8',
      'https://plus.google.com/110031535020051778989/photos',
      'http://googleblog.blogspot.com/',
      'https://chrome.google.com/webstore/category/home',
      'http://staff.tumblr.com/',
      'http://mashable.com/',
      'http://www.buzzfeed.com/celebrity',
      'http://www.thedailybeast.com/',
      'http://www.theverge.com/',
      'http://techcrunch.com/',
      'http://www.engadget.com/',
      'http://gizmodo.com/',
      'http://thinkprogress.org/?mobile=nc',
      'http://gawker.com/',
      'http://arstechnica.com/',
      'http://boingboing.net/category/featured/',
      'http://thenextweb.com/',
      'http://politicalticker.blogs.cnn.com/',
      'http://deadspin.com/',
      'http://news.yahoo.com/',
      'http://www.cnn.com/',
      'http://www.nbcnews.com/',
      'http://www.bbc.co.uk/news/',
      'http://www.reddit.com/',
      'http://my.yahoo.com/',
      'http://www.foxnews.com/',
      'http://www.guardiannews.com/uk-home',
      'http://timesofindia.indiatimes.com/',
      'http://online.wsj.com/home-page',
      'http://www.forbes.com/home_usa/',
      'http://www.washingtonpost.com/',
      'http://www.usatoday.com/',
      'http://drudgereport.com/',
      'http://abcnews.go.com/',
      'http://www.latimes.com/',
      'http://www.bloomberg.com/',
      'http://money.cnn.com/',
      'http://www.news.com.au/',
      'http://www.cbsnews.com/',
      'http://www.examiner.com/',
      'http://www.cnbc.com/',
      'http://www.alarabiya.net/default.html',
      'http://www.time.com/time/',
      'http://www.foxnews.com/politics/index.html',
      'http://www.smh.com.au/',
      'http://www.businessweek.com/',
      'http://www.nationalgeographic.com/',
      # pylint: disable=C0301
      'http://www.wunderground.com/cgi-bin/findweather/getForecast?query=94035&sp=KCAMOUNT24',
      # pylint: disable=C0301
      'http://www.accuweather.com/en/search-locations?zipcode=mountain%20view,%20ca',
      'http://www.weather.com/weather/right-now/Mountain+View+CA+94043',
      # pylint: disable=C0301
      'http://weather.yahoo.com/united-states/california/mountain-view-12797130/',
      'http://www.yr.no/place/Norway/Oslo/Oslo/Oslo/',
      'http://www.metoffice.gov.uk/',
      'http://www.intellicast.com/Local/Weather.aspx?location=USCA0746',
      # pylint: disable=C0301
      'http://www.shutterstock.com/cat.mhtml?searchterm=google&search_group=&lang=en&search_source=search_form',
      'http://www.flickr.com/search/?q=monkeys&f=hp',
      # pylint: disable=C0301
      'http://www.flickr.com/photos/davidgutierrez/sets/72157604615916402/?page=3',
      # pylint: disable=C0301
      'http://www.flickr.com/photos/davidgutierrez/sets/72157604615916402/show/with/4403158307/',
      'http://www.apple.com/iphone/',
      'http://www.taobao.com/index_global.php',
      'http://hootsuite.com/',
      'http://www.android.com/',
      'https://www.change.org/',
      'http://www.nytimes.com/skimmer/#/Technology',
      'http://www.glennbeck.com/',
      'http://www.pengyou.com/mobile?from=loginAndroid',
      'http://en.wikipedia.org/wiki/Cat',
      'http://en.wikipedia.org/wiki/British_Royal_Family',
      'http://9gag.com/gag/5202885',
      'http://www.wowwiki.com/World_of_Warcraft:_Mists_of_Pandaria',
      'http://twitter.github.com/bootstrap/',
      # pylint: disable=C0301
      'http://reviews.cnet.com/8301-13727_7-57431192-263/disable-elastic-scrolling-in-os-x/',
      'http://mlb.com',
      'http://thenounproject.com/zh-cn/',
      'http://allrecipes.com/recipe/chicken-pot-pie-ix/',
      'http://www.gamespot.com/',
      'http://valleywag.com/',
      # pylint: disable=C0301
      'http://gawker.com/5939683/based-on-a-true-story-is-a-rotten-lie-i-hope-you-never-believe',
      'http://www.imdb.com/title/tt0910970/',
      'http://www.html5rocks.com/en/',
      # pylint: disable=C0301
      'http://athome.kimvallee.com/2010/03/why-to-splurge-on-a-high-end-dishwasher/',
      ('http://mlb.mlb.com/mlb/gameday/index.jsp?gid=2012_08_31_sfnmlb_chnmlb_1'
      '&mode=wrap#gid=2012_08_31_sfnmlb_chnmlb_1&mode=box'),
      'http://nytimes.com',
      'http://arstechnica.com',
      'http://pinterest.com',
      'http://www.theregister.co.uk/',
      'http://forum.xda-developers.com/',
      'http://maps.google.com',
      'https://www.google.com/search?num=10&hl=en&site=&tbm=isch&q=cats',
      'http://code.google.com/p/chromium/issues/list',
      ('http://code.google.com/p/chromium/issues/detail?id=142038'
       '&q=black%20screen%20amd&colspec=ID%20Pri%20Mstone%20ReleaseBlock%20OS'
       '%20Area%20Feature%20Status%20Owner%20Summary'),
      'http://mlb.mlb.com/index.jsp',
      'http://www.nfl.com/',
      'http://airbnb.github.com/infinity/demo-on.html',
      'http://habrahabr.ru/post/149892/#habracut'
    ]

    for url in urls_list:
      self.AddStory(KeyDesktopSitesPage(url, self))
