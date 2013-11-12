from util import *

init()

sector, deposit_number, deposit_locations = get_deposit_from_user('fish')

move_to_deposit(sector, deposit_number, deposit_locations)
deposit_region.highlight(5)

count = int(input("How many to add?",'0'))
App.focus('/Applications/Google Chrome.app')

for i in xrange(0,count):
    place_deposit(fish_deposit, fish_spot)
    log("Have placed %d fish deposits so far, %d to go" % (i+1, count-(i+1)))
