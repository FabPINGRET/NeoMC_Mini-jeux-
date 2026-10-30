function music:end
title @a[tag=mg.flw] actionbar {"text":"The evil has been driven from this place...","italic":true,"color":"yellow"}
tag @a[tag=mg.flw] remove bossroom

scoreboard players set mainstory Story 11
advancement grant @a[tag=mg.flw] only main_quest:tenth_dungeon
scoreboard players set $fla2 mg.fla 1
bossbar set boss:ta players

kill @e[tag=l_soul,distance=0..]
kill @e[tag=a_soul,distance=0..]
kill @e[tag=p_smoke,distance=0..]
kill @e[tag=d_qessk,distance=0..]
kill @e[tag=s_spirit,distance=0..]
kill @e[tag=g_giant,distance=0..]
kill @e[tag=soulguard,distance=0..]


# stop boss tick
setblock -11798 203 351 air


schedule function floaty:sched/boss/10/cutscene/act_three 15s replace
