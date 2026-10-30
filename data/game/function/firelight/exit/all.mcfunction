function game:firelight/exit/grengleshoft
function game:firelight/exit/guathman
function game:firelight/exit/master_of_faces
function game:firelight/exit/pim_the_lesser
function game:firelight/exit/prunt
function game:firelight/exit/spoom_ee3
function game:firelight/exit/spoom_ee4
execute as @e[tag=firelight_actor,distance=0..] run item replace entity @s weapon.mainhand with air
execute as @e[tag=firelight_actor,distance=0..] run item replace entity @s weapon.offhand with air
execute as @e[tag=firelight_actor,distance=0..] run data modify entity @s Pose set value {}
