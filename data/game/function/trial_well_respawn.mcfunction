tag @s remove in_trial_well_1
tag @s remove in_trial_well_2
tag @s remove in_trial_well_3

execute unless entity @a[tag=in_trial_well_1,tag=mg.flw] run kill @e[tag=trial_well_monster_1,distance=0..]
execute unless entity @a[tag=in_trial_well_2,tag=mg.flw] run kill @e[tag=trial_well_monster_2,distance=0..]
execute unless entity @a[tag=in_trial_well_3,tag=mg.flw] run kill @e[tag=trial_well_monster_3,distance=0..]

execute unless entity @a[tag=in_trial_well_1,tag=mg.flw] run scoreboard players set trial_well_1_going bool 0
execute unless entity @a[tag=in_trial_well_2,tag=mg.flw] run scoreboard players set trial_well_2_going bool 0
execute unless entity @a[tag=in_trial_well_3,tag=mg.flw] run scoreboard players set trial_well_3_going bool 0

execute unless entity @a[tag=in_trial_well_3,tag=mg.flw] run function boss:mini/attestor_golem/init

stopsound @s music
