playsound minecraft:entity.enderman.teleport hostile @a[tag=mg.flw] -11760 174 -196 2 1
particle dust_color_transition{from_color:[0.000,0.271,0.290],to_color:[0.000,0.933,1.000],scale:2} -11760 174 -196 0.4 0.6 0.4 0 100
tp @n[tag=mind_boss_stand,distance=0..] -11760 169 -196
bossbar set boss:mind_contagion players @a[tag=mg.flw]

schedule function floaty:sched/boss/mini/mind_contagion/attacks/cactus_bomb_start 3s

function music:miniboss

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
