#EMPTY
function game:firelight/exit/all
#THRONE ROOM 1 (Spoom-Ee and Pim)
execute if score firelight_scene Value matches 1 run function game:firelight/enter/spoom_ee4
execute if score firelight_scene Value matches 1 run function game:firelight/enter/pim_the_lesser
execute if score firelight_scene Value matches 1 run tp @n[tag=spoom-ee4,distance=0..] 9899 60 -132 90 0
execute if score firelight_scene Value matches 1 run tp @n[tag=pim_the_lesser,distance=0..] 9899 59 -129 110 0
#THRONE ROOM 2 (Court of the Grengleshoft)
execute if score firelight_scene Value matches 2 run function game:firelight/enter/spoom_ee4
execute if score firelight_scene Value matches 2 run function game:firelight/enter/grengleshoft
execute if score firelight_scene Value matches 2 run function game:firelight/enter/pim_the_lesser
execute if score firelight_scene Value matches 2 run tp @n[tag=spoom-ee4,distance=0..] 9899 60 -132 50 0
execute if score firelight_scene Value matches 2 run tp @n[tag=pim_the_lesser,distance=0..] 9899 59 -135 70 0
execute if score firelight_scene Value matches 2 run tp @n[tag=grengleshoft1,distance=0..] 9899 59 -129 110 0
execute if score firelight_scene Value matches 2 run tp @n[tag=grengleshoft2,distance=0..] 9899 59 -128 110 0
execute if score firelight_scene Value matches 2 run tp @n[tag=grengleshoft3,distance=0..] 9899 59 -127 110 0
#ROAD GATEKEEPER
execute if score firelight_scene Value matches 3 run function game:firelight/enter/spoom_ee4
execute if score firelight_scene Value matches 3 run function game:firelight/enter/guathman
execute if score firelight_scene Value matches 3 run tp @n[tag=spoom-ee4,distance=0..] 9899 59 -133 40 0
execute if score firelight_scene Value matches 3 run tp @n[tag=guathman,distance=0..] 9899 59 -130 130 0
#ROAD NO GATEKEEPER
execute if score firelight_scene Value matches 4 run function game:firelight/enter/spoom_ee4
execute if score firelight_scene Value matches 4 run tp @n[tag=spoom-ee4,distance=0..] 9899 59 -133 40 0
#THRONE ROOM 3 (Exploded Grengleshoft)
execute if score firelight_scene Value matches 5 run function game:firelight/enter/spoom_ee4
execute if score firelight_scene Value matches 5 run function game:firelight/enter/pim_the_lesser
execute if score firelight_scene Value matches 5 run tp @n[tag=spoom-ee4,distance=0..] 9899 60 -132 50 0
execute if score firelight_scene Value matches 5 run tp @n[tag=pim_the_lesser,distance=0..] 9899 59 -135 70 0
#ABDICATE
execute if score firelight_scene Value matches 6 run function game:firelight/enter/spoom_ee4
execute if score firelight_scene Value matches 6 run function game:firelight/enter/grengleshoft
execute if score firelight_scene Value matches 6 run function game:firelight/enter/pim_the_lesser
execute if score firelight_scene Value matches 6 run function game:firelight/enter/prunt
execute if score firelight_scene Value matches 6 run tp @n[tag=spoom-ee4,distance=0..] 9898 59 -131 90 0
execute if score firelight_scene Value matches 6 run tp @n[tag=pim_the_lesser,distance=0..] 9899 59 -135 70 0
execute if score firelight_scene Value matches 6 run tp @n[tag=grengleshoft1,distance=0..] 9899 59 -129 110 0
execute if score firelight_scene Value matches 6 run tp @n[tag=grengleshoft2,distance=0..] 9899 59 -128 110 0
execute if score firelight_scene Value matches 6 run tp @n[tag=grengleshoft3,distance=0..] 9899 59 -127 110 0
execute if score firelight_scene Value matches 6 run tp @n[tag=prunt_older_cousin,distance=0..] 9899 60 -132 90 0
#TUNNEL
execute if score firelight_scene Value matches 7 run function game:firelight/enter/spoom_ee4
execute if score firelight_scene Value matches 7 run tp @n[tag=spoom-ee4,distance=0..] 9899 61 -134 50 0
#BAZAAR
execute if score firelight_scene Value matches 8 run function game:firelight/enter/spoom_ee4
execute if score firelight_scene Value matches 8 run function game:firelight/enter/master_of_faces
execute if score firelight_scene Value matches 8 run tp @n[tag=spoom-ee4,distance=0..] 9898 59 -133 50 0
execute if score firelight_scene Value matches 8 run tp @n[tag=master_of_faces,distance=0..] 9899 59 -129 120 0
#BAZAAR KING
execute if score firelight_scene Value matches 9 run function game:firelight/enter/spoom_ee4
execute if score firelight_scene Value matches 9 run function game:firelight/enter/spoom_ee3
execute if score firelight_scene Value matches 9 run function game:firelight/enter/master_of_faces
execute if score firelight_scene Value matches 9 run tp @n[tag=spoom-ee3,distance=0..] 9898 59 -131 50 0
execute if score firelight_scene Value matches 9 run tp @n[tag=spoom-ee4,distance=0..] 9898 59 -133 50 0
execute if score firelight_scene Value matches 9 run tp @n[tag=master_of_faces,distance=0..] 9899 59 -129 120 0
