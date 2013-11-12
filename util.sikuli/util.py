from sikuli import * # include sikuli functionality

import sys
sys.path.append('/Library/Python/2.7/site-packages/')
import yaml
import datetime

import pprint # pretty printing    pprint.pprint(var)

def init():
    log("script starting")
    Settings.MoveMouseDelay = 0.1

star_button_region = Region(662,713,61,187) # 662,713,61,187
star_menu_region = Region(504,462,380,372)
deposit_region = Region(685,406,77,83)
star_button = "star_button.png"
mail_button = "mail_button.png"
mail_window = Region(399,312,587,396)
mail_window_down_arrow = Pattern("1380842794098.png").targetOffset(1,-1)
mail_window_up_arrow = "1380842830987.png"
mail_window_accept_button = Pattern("1380843362797.png").similar(0.90)
mail_window_hit_bottom = Pattern("1380843203943.png").exact()
mail_messages = {
    'explorer_found'  : Pattern("subject_explorer_has.png").similar(0.60),
    'quest_reward'    : Pattern("subject_quest_reward.png").similar(0.60)
                }

slider = Pattern("slider.png").similar(0.80)
arrow_right = Pattern("arrow_right.png").exact()
ok_button = "ok_button.png"

star_menu_down_arrow = Pattern("1378649228044.png").exact()
star_menu_up_arrow   = Pattern("1378649285738.png").exact()
fish_deposit         = Pattern("1377916260565.png").exact()
fish_spot            = Pattern("1377948158588.png").similar(0.60).targetOffset(0,2)
meat_deposit         = Pattern("1377916866502.png").exact()
meat_spot            = Pattern("1377936157136.png").similar(0.60)
resources = {
        'brew'        : Pattern("resource_brew.png").exact(),
#        'balloons'    : Pattern("resource_balloons.png").exact(),
        'gold_ore'    : Pattern("resource_gold_ore.png").exact(),
        'coal'        : Pattern("resource_coal.png").exact(),
        'exotic_logs' : Pattern("resource_exotic_wood.png").exact(),
        'gold_coins'  : Pattern("resource_gold_coins.png").exact(),
        'granite'     : Pattern("resource_granite.png").exact(),
        'guild_coins' : Pattern("resource_guild_coins.png").exact(),
        'map_frags'   : Pattern("resource_map_fragments.png").exact(),
        'iron_swords' : Pattern("resource_iron_swords.png").exact(),
        'longbows'    : Pattern("resource_longbows.png").exact(),
        'marble'      : Pattern("resource_marble.png").exact()
    }

star_menu_tabs = {
        'all'         : "1378669529209.png",
        'specialists' : Pattern("1378669558019.png").similar(0.65),
        'buffs'       : "1378669594187.png",
        'resources'   : "1378669616255.png",
        'misc'        : "1378669629687.png"
    }

ph_items = {
        'fishfood'      : "ph_items-fishfood.png",
        'deer_musk'     : Pattern("ph_items-deer_musk.png").similar(0.65),
        'aunt_irma'     : "ph_items-aunt_irma.png",
        'marbles'       : "ph_items-marbles.png",
        'ropes'         : "ph_items-ropes.png",
        'buckets'       : "ph_items-buckets.png"
    }

building_windows = {
        'provision_house': {
            'top_left'    : Pattern("ph_top_left.png").similar(0.85),
            'bottom': "ph_bottom.png",
            'bottom_halloween': Pattern("ph_bottom_halloween.png").similar(0.60),
            'product_region_top' : Pattern("ph_product_region_top.png").exact(),
            'queue_region_top_left' : Pattern("ph_queue_region_top_left.png").exact()
        }
    }

building_regions = {
        'provision_house' : {
            'main' : None,
            'product_region' : None
        }
    }

def ph_test():
    tl = find(building_windows['provision_house']['top_left'])
    #tl.highlight(1)
    b = find(building_windows['provision_house']['bottom_halloween'])
    #b.highlight(1)

    building_regions['provision_house']['main'] = Region(tl.x, tl.y, (b.x+b.w)-tl.x, (b.y+b.h)-tl.y)
    ph_region = building_regions['provision_house']['main']
    #ph_region.highlight(1)

    product_region_top = ph_region.find(building_windows['provision_house']['product_region_top'])
    #product_region_top.highlight(1)
    range = (ph_region.y+ph_region.h+20)-(product_region_top.y+b.h)

    building_regions['provision_house']['product_region'] = product_region_top.below(range)
    #building_regions['provision_house']['product_region'].highlight(1)

def reset():
    log('reset called')
    type('0')
    mouseMove(getCenter())
    click(getCenter())
    click(getCenter())

def move_to_deposit(sector, number, deposit_list):
    log("move_to_deposit called for sector #%(sector)d deposit #%(number)d" % vars())

    App.focus('/Applications/Google Chrome.app')

    reset() # standardize zoom level

    type(str(sector)) # move to sector

    xstep,ystep = deposit_list[sector][number].values() # extract coords from dataset
    log("starting with xstep=%d, ystep=%d" % (xstep,ystep))

    while xstep != 0 or ystep != 0:
        if abs(xstep) > 200:
            xmove = 200 if xstep > 0 else -200
        else:
            xmove = xstep

        if abs(ystep) > 200:
            ymove = 200 if ystep > 0 else -200
        else:
            ymove = ystep

        move(xmove, ymove)

        xstep -= xmove
        ystep -= ymove

def move(xstep, ystep):
    log("move called with xstep=%s and ystep=%s" % (xstep, ystep))
    dragDrop(getCenter().offset(xstep,ystep),getCenter())

def place_deposit(deposit_type, deposit_spot):
    star_button_region.click(star_button)
    star_menu_region.wait(deposit_type).click(deposit_type)
    # for fish deposits, move mouse to update buff location so we can find the deposit spot
    time.sleep(0.2)
    mouseMove(getCenter().left(100))
    time.sleep(0.4)

    deposit_region.wait(deposit_spot).click(deposit_spot)
    time.sleep(0.3)

def get_deposit_from_user(deposit_type):
   # popup("You are going to be depositing %s" % deposit_type)

    sector = int(input("(%s) Enter the sector" % deposit_type,'0'))
   # sector = 9
    deposit_number = int(input("(%s) Enter the deposit number" % deposit_type,'0'))
   # deposit_number = 1

    if sector == 0 or deposit_number == 0:
        popup("Give some input, jackass!")
        raise Exception('Invalid input entered')

    file_path = "/Users/jasonblank/settlers-online/sikuli-scripts/"

    if deposit_type == 'fish':
        file_to_load = file_path + 'fish_locations.yml'
    elif deposit_type == 'meat':
        file_to_load = file_path + 'meat_locations.yml'
    else:
        popup("Invalid deposit type [%s]" % deposit_type)


    file_handle = open(file_to_load,'r')
    deposit_locations = yaml.safe_load(file_handle)
    file_handle.close()

    return (sector, deposit_number, deposit_locations)

def deposit_resource(res):
    try:
        star_menu_region.click(res)
        sleep(0.3)
        mouseMove(getCenter().left(-100))
        sleep(0.5)
        click(getCenter())
    except Exception, ex:
        log("Exception: " + ex)

def log(message):
    print "[" + str(datetime.datetime.now()) + "] " + message

