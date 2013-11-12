from util import *

init()

count = int(input("How many to queue up?",'0'))

if count == 0:
    raise "Need more than zero, dummy."

App.focus('/Applications/Google Chrome.app')

ph_test()

Settings.MoveMouseDelay = 0

for i in xrange(0,count):
    # aunt_irma, fishfood, deer_musk
    building_regions['provision_house']['product_region'].click(ph_items['deer_musk'])
    building_regions['provision_house']['main'].dragDrop(slider, arrow_right)
    building_regions['provision_house']['main'].click(ok_button)
    sleep(0.5)
    log("Have queued %d stacks so far, %d to go" % (i+1, count-(i+1)))
