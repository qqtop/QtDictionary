#! /usr/local/bin/python
# -*- coding: utf-8 -*-


import os
import sys
import time
#import codecs
#import operator
#import inspect
#import random
import platform
import subprocess
import json

#import fdb
import MeCab
#import langid

from jcconv import kata2hira
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from termcolor import cprint
from datetime import datetime

#from pprint import pprint

# these imports are for the weblio example function
import requests
from requests import get, RequestException
from bs4 import BeautifulSoup

from dcform import Ui_Dialog  

# imports for vidplayer class
#import mpylayer
from os import listdir
from os.path import isfile, join

# some init strings
Version = '1.00 '
VersionDate = '2014-06-06'

# set some paths
scriptlocationpath = os.path.dirname(os.path.abspath(__file__))
# another way
#img_uri = os.path.join(os.getcwd(), "somedir/some.png")
#print scriptlocationpath
IMAGE_ROOT = scriptlocationpath + "/"


# A dicitionary access program written in python 2.7 and pyqt4
# Future version may allow speaking supporting openJTalk,googleVoice and or espeak





class Icon(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 600, 505)
        #self.setWindowTitle('qtJJ - Python - Loading') # not needed here as startup is fast
        self.setWindowIcon(QtGui.QIcon(IMAGE_ROOT + 'th.jpg'))


class Trayer(QSystemTrayIcon):
    # tray icon with menu

    __instance = None

    @staticmethod
    def new():
        if not Trayer.__instance:
            Trayer.__instance = Trayer()
        return Trayer.__instance

    def __init__(self):
        QSystemTrayIcon.__init__(self)
        # trayiconmenu here
        menu = QtGui.QMenu()
        appAbout = menu.addAction("About")
        qtAbout = menu.addAction("Qt-Info")
        exitAction = menu.addAction("Exit")
        self.setContextMenu(menu)

        self.setIcon(QIcon(IMAGE_ROOT + 'th.jpg'))

        appAbout.triggered.connect(self.showAbout)
        qtAbout.triggered.connect(self.showqtAbout)
        exitAction.triggered.connect(self.appExit)

        self.show()


    def showAbout(self):
        # our trayicon menu function
        mos = "Os   Version  : '%s'" % str(os.name)
        mqt = "Qt   Version   : '%s'" % str(QtCore.QT_VERSION_STR)
        pqt = "PyQt Version : '%s'" % str(QtCore.PYQT_VERSION_STR)
        #mfb = "Fdb  Version : '%s'" % str(fdb.__version__)

        QtGui.QMessageBox.information(QtGui.QWidget(), self.tr("About qtDC-" + Version + VersionDate),
                                      self.tr(mos + "\n" + mqt + "\n" + pqt + "\n" + '' + "\n"), self.tr(
                "A Dicitionary LookUp System \n Glosbe,Kateglo,Kamus Besar KBBI,JDict && Weblio Data\n Google Translate\n\nAll data is for lookup purpose only \nand you should make yourself acquainted with \nlicenses on their respective websites \n\nThis program is freeware .Go Wild\n\nV " + Version + VersionDate))

    def showqtAbout(self):
        QApplication.aboutQt()


    def appExit(self):
        # Just leave ...
        sys.exit(app.exec_())  




class JDic:
    """
    Queries JDic Web API (at csse.monash.edu.au) and returns parsed data
    """

    def __init__(self):
        """Setup request url and default request options"""
        self.url = ('http://www.csse.monash.edu.au/~jwb/cgi-bin/wwwjdic.cgi?' '9MIG%s')

    def lookup(self, sentence):
        """Lookup translations and reading of sentence|word"""
        return self.parse(self.query(sentence))

    def query(self, request):
        """Query JDic to analyze sentence|word"""
        try:
            return BeautifulSoup(get(self.url % request).text, 'lxml')
        except RequestException:
            return None

    def parse(self, response):
        """Parse JDic response as html"""
        try:
            return dict(zip(
                # keys: Items (colorized)
                [item.getText()
                 for item in response.find(id='inp').find_all('font')
                 if 'color' in item.attrs],
                # values: Translations (as list elements)
                [li.getText()
                 for li in response.find(id='inp').find_all('li')]
            ))
        except Exception:
            return None


class Weblio:
    # see weblio.py in dev section
    # here we only use things that worked there
    # note this is based on jpnetkit from which usefull classes where used
    def __init__(self):
        self.examples_url = 'http://ejje.weblio.jp/sentence/content/%s'
        self.stats = {}


    def examples(self, term, number=10, portion=6, tuples=True):
        """
        Fetches examples from Weblio
        :param term:    word or phrase to lookup
        :param number:  number of examples to fetch
        :param portion: portion of examples to use (e.g., 1/2 -> from the middle)
        :returns:       list of tuples (example, translation)
        """
        data = self.process(self.examples_url, term)
        examples = []
        if data:
            #for example in data.find_all('div', 'qotC')[-number:]:
            total = data.find_all('div', 'qotC')
            #print len(total)
            n = len(total) / portion

            for example in total[n: n + number]:
                sentence = example.contents[0].getText()
                source = example.contents[1].span.getText()
                translation = example.contents[1].getText().replace(source, '')
                translation = self.remove_comments(translation, '<!--')

                if tuples:
                    examples.append((source, sentence, translation))  # pp added source so we get the jap text too
                else:
                    examples.append({sentence: translation})

        return examples


    def process(self, url, term):
        try:
            # Use lxml instead of HTMLParser (2.7.2 is bad with malformed tags)
            return BeautifulSoup(requests.get(url % term).text, 'lxml')
        except RequestException:
            return None

    def remove_comments(self, line, sep):
        """Trims comments from string"""
        for s in sep:
            line = line.split(s)[0]
        return line.strip()

        # end of Weblio class





class kbbi:

      def __init__(self):
       
          self.url='http://kbbi.web.id/'
	  
      def getData(self,theWord):
	  r= requests.get('http://kbbi.web.id/%s' % theWord)
	  return r.text
	      
	
      def processData(self,dx):
	  gdx = self.getData(dx)
	  soup = BeautifulSoup(gdx,"lxml")
	  return soup
  

class kateglo:
  
    def __init__(self):
	    self.url='http://kateglo.com/api.php?format=json&phrase='
      
    def getData(self,theWord):
        self.url=self.url+theWord
	r= requests.get(self.url)
	try:
	    
	    jdata = json.loads(r.text)
	    return jdata
	  
	except:
		return -1
	      
	      
    def checkTa(self):	      
	  if os.path.isfile('translate.awk')==True:
	    okt=True
	  else:
	    okt=False
	  return okt  
	      
    def doTranslate(self,zx):
		  
	    tm=''
	    if len(zx)> 1:
		s = 'awk -f translate.awk {=en} %s' % '"' + zx + '"'  # yeah escape like this so we get rid of errors for high comma words like : I'm nice
		p = subprocess.Popen(s, stdout=subprocess.PIPE, shell=True)
		output, err = p.communicate()
		tm = output.rstrip()
		tm = tm.replace('\n', ' ').replace('\r', '')  # \r also catches carriage returns
		tm = tm + '  [G]'  # mark it as google translation
	    return tm

        
    def translator(self,data):
	
	  
	    trResult=[]
	    c=0
	    for x in range(len(data['kateglo']['translations'])):
		  # we only want 1 result usually first is from ebsoft
		  # if not the other result would be from gkamus
		  c+=1
		  if c==2: # in case you want both just change this top c>0 or c==2 for gkamus only
		    trResult.append(data['kateglo']['translations'][x]['ref_source'])  
		    trResult.append(data['kateglo']['translations'][x]['translation'])
	      
		  
	    #print '\nInformation for Phrase : ',data['kateglo']['phrase']
	    #pprint(data)  # uncomment this for all stuff
	    
	    if c==0:
	      trResult.append('None found . Check correct, spelling and root word')

	    return trResult 

      
    def definitor(self,data):
	    # for a nicer output we precalc the max length of the keys
	    # print data['kateglo']['definition']
	    kmax=0
	    dfResult=[]
	    for zd in data['kateglo']['definition']:
		  for k in zd:
		    if len(k) > kmax:
		      kmax=len(k)

	    for zd in data['kateglo']['definition']:
		  for k in zd:
		      #print k,' '*(kmax-len(k)),'  :  ',zd[k] # we show only 2 interesting rows from thsi data block
		      if k=="def_text":
			try:		    
			  dfT=k.capitalize()+' '*(kmax-len(k))+'  :  \n\n'+zd[k]
			  dfResult.append(dfT)
			  if self.checkTa()==True:
			     dfResult.append(doTranslate(zd[k]))
			except:
			    pass
		      if k=='sample':
			try:
			  dfS='\n'+ k.capitalize()+' '*(kmax-len(k))+'  :  \n\n'+zd[k]
			  dfResult.append(dfS)
			  cc=''
			  cc=doTranslate(zd[k])
			  if self.checkTa()==False:
			     dfResult.append(' ')
			  else:
			     dfResult.append(cc)
			except:
			    pass
		  dfResult.append('-'*100)
		  
	    return dfResult
	    


    def proverbor(self,data):
	  prResult=[]
	  for x in range(len(data['kateglo']['proverbs'])):
		  prResult.append(data['kateglo']['proverbs'][x]['meaning'])
		  if self.checkTa()==True:
		     prResult.append(self.doTranslate(data['kateglo']['proverbs'][x]['meaning']))
		  else:
		    prResult.append(' ')
		  
	  if len(prResult)<1:
	      prResult.append('None')
	  prResult.append('-'*100)
	  
	  return prResult
	
	
    def proverbMaster(self,theWord):
	# we try to access http://kateglo.com/?phrase=ikan&mod=proverb
	#r= requests.get('http://kateglo.com/?phrase=%s&mod=proverb' % theWord)
	try:
	    # this wud return the first page of possibly many
	    # but in html which we wud need to parse with beautifulsoup
	    # something for a rainy day.
	    # start with <ul><p>
	    #print(r.text)
	    pass
	  
	except:
		return -1


    def relator(self,data):
	  #print data['kateglo']['all_relation']
	  # for a nicer output we precalc the max length of k
	  kmax=0
	  rlResult=[]
	  try:
	    for zd in data['kateglo']['all_relation']:
	      for k in zd:
		    if len(k) > kmax:
		      kmax=len(k)
	  except:
	    pass
	  
	  
	  rlmax=0
	  try:
	    for zd in data['kateglo']['all_relation']:
		for k in zd:
		      if k=="related_phrase": # comment this out to get the whole data block and prappend k, to below statement
			if len(zd[k]) > rlmax:
			    rlmax=len(zd[k])
	  except:
	    pass
				  
	  
	  
	  
	  try:
	    for zd in data['kateglo']['all_relation']:
		for k in zd:
		      if k=="related_phrase": # comment this out to get the whole data block and prappend k, to below statement
			try:
			  if self.checkTa()==True:	  
			    tm = self.doTranslate(zd[k])
			    rlResult.append(zd[k]+' '*(rlmax-len(zd[k]))+'  -  '+tm.decode('utf8'))
		          else:
			    rlResult.append(zd[k])
			  
			except:
			    raise
			  
	    

	  except:
	      rlResult.append('None')
	      
	  rlResult.append('-'*100)

	  return rlResult



class glosbe:
  
      def __init__(self):
		self.url='http://glosbe.com/'
		
      

      def getData(self,theWord,orglang,destlang):
	    
	  r= requests.get('http://glosbe.com/gapi/translate?from=%s&dest=%s&format=json&phrase=%s&pretty=true' % (orglang,destlang,theWord))
	  try:
	      
	      jdata = json.loads(r.text)
	      return jdata
	    
	  except:
		  return -1
	   		

class QPSQT4(QtGui.QDialog):
    def __init__(self):

        QtGui.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # this sets the taskbar icons and app name
        wT = 'qtDC-' + Version
        self.setWindowTitle(wT)
        self.setWindowIcon(QtGui.QIcon(IMAGE_ROOT + 'th.jpg'))

        #establish connections and cursors , maybe add. feature accessing a
        #local copy of tatoeba..
        
        #self.doCon()

        # Handle Qt's debug output
        # this seems to take care of the console pixl messages, which occure on some systems
        QtCore.qInstallMsgHandler(self.handle_qt_debug_message)

        #global trayer
        trayer = Trayer.new()

        self.ui.pushButton.clicked.connect(self.doGo)
        self.ui.pushButton_4.clicked.connect(self.doClearSearch)
        self.ui.pushButton_2.clicked.connect(self.doClearResults)
        self.ui.pushButton_5.clicked.connect(trayer.showAbout)
        self.ui.pushButton_6.clicked.connect(self.doHelp)
        self.ui.comboBox.currentIndexChanged.connect(self.clearL3)
        self.ui.pushButton_3.clicked.connect(self.shutdown)
        
        
        self.ui.label.setText('qtDC - Dictionary System V. %s - %s' % (Version,VersionDate))
        # we need to load the comboBox
        
        self.ui.comboBox.addItem('GLOSBE')
        self.ui.comboBox.addItem('JDICT')
        self.ui.comboBox.addItem('WEBLIO')
        self.ui.comboBox.addItem('KBBI')
        self.ui.comboBox.addItem('KATEGLO')
        
        self.clearL3()
        
    
    def handle_qt_debug_message(self, level, message_bytes):
        # this helps to take care of some unwanted qt console messages
        ignored_messages = [  # QtWebKit spams this and no one knows why :(
                              "QFont::setPixelSize: Pixel size <= 0 (0)",
        ]
        message = message_bytes.decode('utf-8')
        if message not in ignored_messages:
            print("Qt debug:", message)    
    
    def clearL3(self):
        # on change of dict we put some info into the label_3 and clear textEdit
        self.ui.label_4.clear()
        #self.ui.textEdit.clear() , maybe better not to clear
        
        if self.ui.comboBox.currentText()=='JDICT':
	        
	        self.ui.label_3.setText(' JDICT please input a japanese word/phrase ')
	        
	elif self.ui.comboBox.currentText()=='KATEGLO':
	        
	        self.ui.label_3.setText(' KATEGLO Dictionary , please input a indonesian word')
	                
	elif self.ui.comboBox.currentText()=='KBBI':
	        
	        self.ui.label_3.setText(' Kamus Besar Bahasa Indonesia , please input an Indonesian word')
	        
	elif self.ui.comboBox.currentText()=='WEBLIO':
	        
	        self.ui.label_3.setText(' WEBLIO Japanese examples , please input japanese word/phrase')
	                
        
        elif self.ui.comboBox.currentText()=='GLOSBE':
	        
	        self.ui.label_3.setText(' GLOSBE Dictionary , please select language pair...')
	        
        else:
	     self.ui.label_3.settext('')
    
    
    
    def aline(self):
	# just print a seperator line
	s='-'*100
	self.ui.textEdit_2.append(s)
	
    
    def doHelp(self):
        # help button
        QtGui.QMessageBox.information(QtGui.QWidget(), self.tr("Help for qtDC-" + Version + VersionDate),
                                      self.tr("A Dicitionary LookUp System \n\nEasy to use :\nFirst select a dictionary\nSecond input your word or phrase and press Go\n\nFor Glosbe also select a language pair\n    or write your own into the comboBox,\n\nKateglo - Indonesian/English Dictionary,\n\nKBBI - Kamus Besar Bahasa Indonesia,\n      the Indonesian/Indonesian standard Dictionary,\n\nJDict - Japanese Dictionary Data,\n\nWeblio - Japanese example phrases\n\n For Google Translation in KATEGLO you will\nneed a translate.awk script\n\n V " + Version + VersionDate))


    def doClearSearch(self):
      self.ui.textEdit.clear()
      self.ui.label_3.setText('')

    def doClearResults(self):
      self.ui.textEdit_2.clear()
      self.ui.label_3.setText('')
      
    def lineNumber2(self):

        old_pos = self.ui.textEdit_2.textCursor().blockNumber()
        return old_pos
 
      
    def remove_comments2(self, line, sep):
        """Trims comments from string used in doWeblio"""
        for s in sep:
            line = line.split(s)[0]
        return line.strip()

    def doMecab(self, datax):
        # mecab for weblio data
        try:
            #print 'Datax: ',datax
            mecab = MeCab.Tagger('-Oyomi')
            output = mecab.parse(datax.encode('utf8'))
        except:
            output = ''
            #raise
        return output
    

    def doGo(self):
      #pressing the go button we first see which dict is selected
              
      try:
        theWord=str(self.ui.textEdit.toPlainText())
      except:
	# for JDICT
	theWord=self.ui.textEdit.toPlainText()
      
      if self.ui.comboBox.currentText()=='KATEGLO':
	  start=time.clock()
	  
	  kx=kateglo()
		
	  data=kx.getData(theWord)
	  if data== -1:
	        s='\nHello : '+theWord+'  maybe mispelled or not Indonesian or not the correct root'
		self.ui.textEdit_2.append(s)
		self.ui.textEdit_2.append('Correct and try again')
	  else:	    
		tr=kx.translator(data)
		self.aline()
		s='\nPhrase : '+theWord
		self.ui.textEdit_2.append(s)
		rxc=0
		for rx in tr:
		    if rxc==0:
		        s='Source : '+rx
			self.ui.textEdit_2.append(s)
		    else:
			self.ui.textEdit_2.append(rx)
		    rxc+=1   
		    self.aline()

		df=kx.definitor(data)
		
		self.ui.textEdit_2.append("\nDefinitions\n")
		for rx in df:
		    self.ui.textEdit_2.append(rx)

		pr=kx.proverbor(data)
		      
		self.ui.textEdit_2.append("\nProverbs\n")
		for rx in pr:
		    self.ui.textEdit_2.append(rx)
	      
	      
		rl=kx.relator(data)
	      
		self.ui.textEdit_2.append("\nRelations\n")
		for rx in rl:
		    self.ui.textEdit_2.append(rx)
		    
          self.ui.label_3.setText('Finished KATEGLO request ...')	
          end=time.clock()
	  s='Request duration : '+str(end-start)+' secs'
	  self.ui.label_4.setText(s)
	  

      elif self.ui.comboBox.currentText()=='KBBI':
	  start=time.clock()
	  
          kb=kbbi()
          soup=kb.processData(theWord) 
           
          sxt = soup.get_text()
	  atitle= soup.title.string.split('- definisi kata')
	  s='\n'+atitle[0]
	  self.ui.textEdit_2.append(s)
	  self.aline()
	  s='\nKata : '+atitle[1]
	  self.ui.textEdit_2.append(s)
	  
	  
	  sxts = sxt.split('Pranala (link): http://kbbi.web.id/%s' % theWord )
	  
	  try:
	    sxts2=sxts[1]
	    sxts2= sxts2.split('Tweet')
	    res1 = sxts2[0]
	    res1 = res1.split(';')
	    s=''
	    s=res1[0].strip('-1').strip('-2').strip('-3')
	    self.ui.textEdit_2.append(s)
	    s=''
	    for rx in range(1,len(res1)):
	      rc  = res1[rx]
	      s=rc+'\n'
	      self.ui.textEdit_2.append(s)	  
	  except:
	      self.ui.textEdit_2.append('')
	      s= theWord+' ==>  Tidak ditemukan - KBBI\n\nMaybe incorrect root word'
	      self.ui.textEdit_2.append(s)
	      # we want to get data from the Memuat section , if any
	      sxtch= sxt.split('Memuat')
	      try:
		sxtchz= sxtch[1].split('Pranala')
		self.ui.textEdit_2.append('Try with these suggestions provided by kbbi (if any)  :')
		s= sxtchz[0].replace('1','\n').replace('2','\n').replace('3','\n') # occasionaly there is are subscripts
		self.ui.textEdit_2.append(s)
	      
	      except:
		pass
	      
          self.ui.label_3.setText('Finished KBBI request ...')
          end=time.clock()
	  s='Request duration : '+str(end-start)+' secs'
	  self.ui.label_4.setText(s)
     
      elif self.ui.comboBox.currentText()=='GLOSBE':
	        
	        
	        start=time.clock()
	        lp=str(self.ui.comboBox_2.currentText())
	        al=lp.split('/')
	        orglang=al[0]
	        destlang=al[1]
	        
		gb=glosbe()
		data=gb.getData(theWord,orglang,destlang)
		if data== -1:
		      s='\nHello : '+theWord+'  maybe mispelled or not the correct root word for dicitionary lookup or wrong language code'
		      self.ui.textEdit_2.append(s)
		      s='Correct and try again'
		      self.ui.textEdit_2.append(s)
		else:	 
		      
			  s='From   :  '+data['from']
			  self.ui.textEdit_2.append(s)
			  s='Dest   :  '+data['dest']
			  self.ui.textEdit_2.append(s)
			  s='Result :  '+data['result']
			  self.ui.textEdit_2.append(s)
			  s='Phrases:  '+data['phrase']
			  self.ui.textEdit_2.append(s)
			  self.ui.textEdit_2.append('\n')
			  self.ui.textEdit_2.append('Translations : ')
			  # translation results
			  phr = data['tuc']
			  for item in range(0,len(phr)):
			    try:
				s=data['tuc'][item]['phrase']['text']+' , '
			        self.ui.textEdit_2.append(s)
			    except:
				pass
			  

		self.ui.textEdit_2.append('\n\n\n Translation + Sample Sentence\n\n')
		r2=requests.get('http://glosbe.com/gapi/translate?from=%s&dest=%s&format=json&tm=true&phrase=%s&pretty=true' % (orglang,destlang,theWord))
		try:  
		      data=json.loads(r2.text)
		      # translation results
		      phr = data['tuc']
		      #pprint(phr)
		      if len(phr)==0:
			       self.ui.textEdit_2.append('      Nothing returned from Glosbe')
		      else:
			      # for formatting precalc maxl
			      maxl=0
			      ll=0
			      for item in range(0,len(phr)):
				try:
				  if destlang=='jpn' or destlang=='zh' or destlang =='rus':
				     ll=len(str(phr[item]['phrase']['text']).rstrip(' '))
				  else:   
				     ll=len(str(phr[item]['phrase']['text']).encode('UTF-8').rstrip(' '))
				  if ll > maxl:
				    maxl=ll
				except:
				    ll=10
				    pass

				  
			      try:
				    self.ui.textEdit_2.append('\nPhrase/Meanings :\n')
				    if len(phr)==0:
				       self.ui.textEdit_2.append('      Nothing returned from Glosbe')
				    else:
				      for item in range(0,len(phr)):
					  try:
					    
					    
					       if destlang=='jpn' or destlang=='zh' or destlang=='rus':
						  if phr[item]['phrase']['text'] <> '':
						    s='Phrase   : '+phr[item]['phrase']['text'].replace('&#39;',"'").replace('&rsquo;',"'").replace('&eacute;','`')
						    self.ui.textEdit_2.append(s)
					      
						    for itx in range(0,len(phr[item])):
							try:
							  if phr[item]['meanings'][itx]['text'] <> '':
							      s='Meaning  : '+phr[item]['meanings'][itx]['text'].replace('&#39;',"'").replace('&rsquo;',"'").replace('&eacute;','`')
							      self.ui.textEdit_2.append(s)
							except:
							  pass
						 
					       else: 	 
						  if phr[item]['phrase']['text'].encode('UTF-8') <> '':
						    s='Phrase   : '+phr[item]['phrase']['text'].encode('UTF-8').replace('&#39;',"'").replace('&rsquo;',"'").replace('&eacute;','`')
						    self.ui.textEdit_2.append(s)
					      
						    for itx in range(0,len(phr[item])):
							try:
							  if phr[item]['meanings'][itx]['text'].encode('UTF-8') <> '':
							      s='Meaning  : '+phr[item]['meanings'][itx]['text'].encode('UTF-8').replace('&#39;',"'").replace('&rsquo;',"'").replace('&eacute;','`')
							      self.ui.textEdit_2.append(s)
							except:
							  pass
					       self.aline()
					  except:
					    pass
						
			      except:
				#print 'Error in Phrase/Meanings'
				#raise
				pass	      
			      
			      try:
					    self.ui.textEdit_2.append('\n')
					    if data['tuc'][item]['phrase']['text']  <> ' ':
							  
						for ite in range(0,len(data['examples'])):
						  
						  
						   if destlang=='jpn' or destlang=='zh' or destlang=='rus':
						      ss= data['examples'][ite]['second'].replace('<strong class="keyword">','')
						      ss=ss.replace('</strong>','').replace('#','').replace('|','')
								
						      sf= data['examples'][ite]['first'].replace('<strong class="keyword">','')
						      sf=sf.replace('</strong>','').replace('#','').replace('|','')
						      if sf <> '':
							    s='\nExamples for : '+data['tuc'][item]['phrase']['text'] 
							    self.ui.textEdit_2.append(s)
							    s=sf
							    self.ui.textEdit_2.append(s)
							    self.ui.textEdit_2.append(ss)
							    
						
						   else:
						      ss= data['examples'][ite]['second'].encode('UTF-8').replace('<strong class="keyword">','')
						      ss=ss.replace('</strong>','').replace('#','').replace('|','')
								
						      sf= data['examples'][ite]['first'].replace('<strong class="keyword">','')
						      sf=sf.replace('</strong>','').replace('#','').replace('|','')
						      if sf.encode('utf-8') <> '':
							    s='\nExamples for : '+data['tuc'][item]['phrase']['text'] 
							    self.ui.textEdit_2.append(s)
							    s=sf.encode('utf-8')
							    self.ui.textEdit_2.append(s)
							    self.ui.textEdit_2.append(ss)
							    
			      except:
					      #raise
					      pass

		except:
		  
		  #raise
		  self.ui.textEdit_2.append('JSon Error, maybe no data retrieved')
		  self.ui.textEdit_2.append('Re-try')


		end=time.clock()
		s='Request duration : '+str(end-start)+' secs'
		self.ui.label_4.setText(s)
		self.ui.label_3.setText('Finished GLOSBE request ...')
		    
      elif self.ui.comboBox.currentText()=='WEBLIO':

            start=time.clock()
            
            try:
	        self.oldcurrLine = self.lineNumber2()
                s = Weblio()
                lt = -1
                theText = theWord
                # we need to limit the length: testing with 80
                lt = len(theText)

                #firstLine     =  self.lineNumber2()
                #print 'FirstLine :',firstLine
                #firstPosition =  self.ui.textEdit_3.textCursor().position()
                #print 'Firstpos  :',firstPosition

                if (lt > 0) and (lt < 80):
                    self.ui.textEdit_2.append('\nWeblio Results')
                    self.ui.textEdit_2.append('for:')
                    self.ui.textEdit_2.append(theText)
                    self.ui.textEdit_2.append('---------------------\n')
                    #x = self.ui.spinBox_2.value()  # how many items to fetch
                    # here we hardset to 10 examples max
                    x=10
                    res = s.examples(theText, x)  # ok
                    key = 0
                    for dx in res:
                        rx  = self.remove_comments2(dx[1], '<!--')
                        rx2 = self.remove_comments2(dx[2], '<!--')
                        rx3 = self.doMecab(rx2)
                        key += 1
                        # now we check if we are ascii and print accordingly
                        try:
                            theText.decode('ascii')
                        except:  # we selected a japanese text
                            rx4 = self.doMecab(rx)
                            # oks=str(key)+' : '+rx+'   '+rx2.encode('utf8')+'  '+kata2hira(rx4).decode('utf8')
                            oks = str(key) + ' : ' + rx
                            self.ui.textEdit_2.append(oks)
                            oks = str(key) + ' : ' + rx2.encode('utf8').strip('\n')
                            self.ui.textEdit_2.append(oks)
                            oks = str(key) + ' : ' + kata2hira(rx4).decode('utf8')
                            self.ui.textEdit_2.append(oks)

                        else:  # we selected a english text
                            oks = str(key) + ' : ' + rx.encode('utf8')
                            self.ui.textEdit_2.append(oks)
                            oks = str(key) + ' : ' + rx2
                            self.ui.textEdit_2.append(oks)
                            oks = str(key) + ' : ' + kata2hira(rx3).decode('utf8')
                            self.ui.textEdit_2.append(oks)

                    self.ui.textEdit_2.append('---------------------\n')

                else:
                    if lt > 1:
                        oks = 'Weblio line is too long. Length : %i' % lt
                        self.ui.textEdit_2.append(oks)
                        self.ui.textEdit_2.append('---------------------\n')
            except:


                pass


            # we try jump to the begining of the latest weblio data

            # for time being just jump to bottom
            self.ui.textEdit_2.moveCursor(QTextCursor.End)
            currLine = self.lineNumber2()
            mv = currLine - self.oldcurrLine
            # now move
            #print '\nOldCurrLine :',self.oldcurrLine
            #print 'CurrLine    :',currLine
            #print 'mv          :',mv
            #print '\n'
            for j in range(0, mv):
                self.ui.textEdit_2.moveCursor(QTextCursor.Up)  #,QTextCursor.MoveAnchor)
                nowLine = self.lineNumber2()
                #print 'NowLine : ',nowLine

            self.oldcurrLine = currLine
            self.ui.label_3.setText('Finished Weblio request ....')
            end=time.clock()
   	    s='Request duration : '+str(end-start)+' secs'
	    self.ui.label_4.setText(s)
	     
      elif self.ui.comboBox.currentText()=='JDICT':
	start=time.clock()
	
        # try translate from JDic 
        # while ok it cud be faster
        self.ui.textEdit_2.clear()
        self.JDictToggleFlag=True
        if self.JDictToggleFlag == True:

            try:
                jdictranslations = JDic().lookup(unicode(theWord))
                sl = 0
                jdi = 0
                # nrset used as divider for linefeed inserts below
                nrset = ['(1)', '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', '(8)', '(9)', '(10)', '(11)', '(12)', '(13)',
                         '(14)', '(15)', '(16)', '(17)', '(18)', '(19)', '(20)']

                for key in jdictranslations.keys():
                    sl += 1  # if no key than we never come here
                    if jdi == 0:  # only append once per loop
                        self.ui.textEdit_2.append("\nJDic Info : \n")
                        jdi = 1

                    # this gives a wider view but still messy
                    #self.ui.textEdit_2.append(jdictranslations[key]+"\n")

                    # this gives a more readable view
                    tt = ''
                    for xs in jdictranslations[key]:
                        if xs <> ";":  # only one space or semicolon or we get empty stuff
                            tt = tt + xs
                        else:
                            # below code by trial and error to have a readable representation
                            tt = tt.replace(' 	', ' ')  # note this is a space and a tab
                            tt = tt.replace('\n', '')  # get rid of linefeeds
                            tt = tt.replace('  ', '\n')  # insert a linefeed if there are 2 spaces
                            tt = tt + ';'  # add the semicolon back
                            for nx in nrset:
                                # iterate over our nrset and insert linefeeds for better readability
                                tt = tt.replace(nx, '\n' + nx + '\n')

                            self.ui.textEdit_2.append(tt)
                            tt = ''

                if sl == 0:
                    self.ui.textEdit_2.append('No info from JDict for ' + theWord)

            except:
                # occasional non type objects will occure so we just skip it
                pass

            finally:
                # give a notice if run finished
                self.ui.textEdit_2.append('JDict-Finished')

                #TODO:: try similar wordnet , wordnet has quota so may not work as wanted

        
        end=time.clock()
	s='Request duration : '+str(end-start)+' secs'
	self.ui.label_4.setText(s)


      
    def shutdown(self):

        lastline = '\n\n' + 25 * chr(26) + '         またね !           ' + 25 * chr(26) + '\n\n'
        cprint(lastline, "green", attrs=['bold'])


if __name__ == "__main__":

    myhello = '\n\nHello from   : %s' % str(sys.argv[0])
    cprint(myhello, "white", "on_blue", attrs=['bold', 'underline'])
    cprint("Version      : '%s'" % str(Version), "green", attrs=['bold'])
    cprint("Date         : '%s\n" % str(VersionDate), "green", attrs=['bold'])
    cprint('System       :', "yellow", attrs=['bold', 'underline'])
    cprint("Os   Version : '%s'" % str(os.name), "green", attrs=['bold'])
    cprint("Python       : '%s" % str(sys.version), "green", attrs=['bold'])
    cprint("Qt   Version : '%s'" % str(QtCore.QT_VERSION_STR), "yellow", attrs=['bold'])
    cprint("PyQt Version : '%s'" % str(QtCore.PYQT_VERSION_STR), "green", attrs=['bold'])
    #cprint("Fdb  Version : '%s\n" % str(fdb.__version__), "cyan", attrs=['bold'])
    cprint("Platform Info: ", "yellow", attrs=['bold', 'underline'])
    pfm = platform.uname()
    s = []
    pfmn = ["System", "Node", "Release", "Version", "Machine", "Processor"]
    for x in range(0, len(pfm)):
        s.append(pfmn[x].rjust(9) + ": ".rjust(5) + pfm[x].ljust(5))
    for x in s:
        cprint(" %s" % str(x), "green", attrs=['bold'])
    print '\n'
    cprint('Now lets start !!' + 20 * ' ', 'green', 'on_blue', attrs=['bold', 'underline'])
    # use from console
    # echo`grep QT_VERSION_STR /usr/include/QtCore/qglobal.h | awk '{print $ 3}' | sed -e 's/\"//g'`

    app = QtGui.QApplication(sys.argv)
    #pop up something else before popping up the main
    #window and also magically set the main icon on top left
    icon = Icon()
    icon.show()

    #splash
    pixmap = QPixmap(IMAGE_ROOT + "th.jpg")
    splash = QSplashScreen(pixmap, Qt.WindowStaysOnTopHint)
    splash.setMask(pixmap.mask())
    splash.show()
    app.processEvents()
    # this writes on to our image
    # splash.showMessage(u'Starting...', Qt.AlignRight | Qt.AlignBottom,Qt.yellow)
    # make sure Qt really display the splash screen
    app.processEvents()
    # end of pop up
    myapp = QPSQT4()
    myapp.show()
    # now kill the splashscreen
    #time.sleep(3)
    splash.finish(myapp)
    #close the pop up    
    icon.close()

    sys.exit(app.exec_())

#####################################################################################    
    

