import sys
import os.path
from gui import GUI
from logger import Logger

if __name__ == "__main__":
    scriptDir = os.path.abspath(os.path.dirname(sys.argv[0]))
    title = 'BestArcade 1.6'
    logger = Logger()
    logger.log(title)
    logger.log('\nScript path: ' + scriptDir)
    gui = GUI(scriptDir, logger, title)
    gui.draw()

# FIXES/ENHANCEMENT
# -----------------
# scaling issue on MacOSX -> needs to externalize font size somehow
#   -> done with slider but slider doesn't appear on MacOS, revert slider ?
# resolution/size/scrollbar for lower resolutions than 1080p (see solution draft on my stackoverflow)
# needs to clean <unknown> in mame gamelist
# pbobblen;pbobble -> pbobble shouldn't be used if pbobblen is found
# prosoccr;cpsoccer -> cpsoccer shouldn't be used if prosoccr is found

# homebrews neogeo à mettre dans neogeo.ini également

# IDEAS
# -----------------
# error detecting is wrong for keepLevel WORKING and Exclusion Type Strict
# allow basicsorter generation without dat / prevents generation without dat ?
# add info to generate dat from mame exe (see my handheld thread on reddit)
#   -> hhhhhhm see if regular xml from mame site work
# mame64.exe -listxml > mame.dat

# allow multiple extractions
# try to handle gracefully placeholder values for all paths -> just use default values
# allow exclusion of games genres (i.e. no Puzzle games)

# NEW SETS/TESTS
# ----------------
# add neogeo MVS games tab
# add vertical games tab

# SET ERRORS & CHECKS
# --------------------
# BAD BROKEN CHD fghtmn for latest Mame

# ddp2 not found in fbneo set when it should

# cave pgm v0.213
# irem m-72 v0.213
# irem m-92 v0.213
# itech32 v0.213
# konami system573 v0.213
# mitchell v0.213
# namco s1 v0.213
# namco s12 v0.213
# namco s2 v0.213
# nmk 16 v0.213
# sega system 1 v0.213
# sega system 16 v0.213
# sega system 18 v0.213
# sega system 24 v0.213
# sega system 32 v0.213
# seta1 v0.213
# sony zn1 zn2 v0.213
# taito f2 v0.213
# taito f3 v0.213
# toaplan v0.213
# williams v0.213
