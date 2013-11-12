from util import *

init()

sector, deposit_number, deposit_locations = get_deposit_from_user('meat')

move_to_deposit(sector, deposit_number, deposit_locations)
deposit_region.highlight(5)

count = int(input("How many to add?",'0'))
App.focus('/Applications/Google Chrome.app')

for i in xrange(0,count):
    place_deposit(meat_deposit, meat_spot)
    log("Have placed %d meat deposits so far, %d to go" % (i+1, count-(i+1)))
