#FIGHT START
fill -10193 70 129 -10197 68 133 air
execute as @n[tag=zalvorn_show_intro,distance=0..] at @s run tp @s ~ ~-5 ~
particle dust{color:[1.000,0.467,0.000],scale:2} -10190 69 131 0.5 1 0.5 1 50 normal
particle minecraft:trial_spawner_detection -10190 69 131 0.5 1 0.5 0 50 normal
playsound minecraft:entity.creaking.spawn master @a[tag=mg.flw] -10190 67 131 1 2
#stop head twitch
setblock -10206 56 136 air

tag @a[tag=mg.flw] remove cutscene

function music:miniboss

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
