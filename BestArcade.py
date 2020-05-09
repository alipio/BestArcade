# -*- coding: utf-8 -*-
import sys, os.path
from gui import GUI
from logger import Logger
    
if __name__ == "__main__":
    scriptDir = os.path.abspath(os.path.dirname(sys.argv[0]))
    title = 'BestArcade 1.4'
    logger = Logger()
    logger.log(title)
    logger.log('\nScript path : '+scriptDir)            
    gui = GUI(scriptDir,logger, title) 
    gui.draw()


# TODO
1.4 :
-------
# retest ALL after build -> test new build with

1.5:
----
# add vertical games tab
# strange bug where .ini files got uppercase for naomi and atomiswave, maybe on intellij side, might be a problem on linux
# solve compilation questions and try on an ubuntu VM
# add info to generate dat from mame exe (see my handheld thread on reddit) -> hhhhhhm si if regular xml from mame site work
# allow basicsorter generation without dat / prevents generation without dat ?

