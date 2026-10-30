function boss:10/face_attack_enable

execute positioned -11830 217 308 run function boss:10/place_tornado
execute positioned -11852 217 330 run function boss:10/place_tornado
execute positioned -11830 217 352 run function boss:10/place_tornado
execute positioned -11808 217 330 run function boss:10/place_tornado
execute positioned -11830 233 330 run function boss:10/place_tornado

function boss:10/faces/shuffle

# Start damage check
setblock -11804 203 351 redstone_block
setblock -11807 203 351 air
