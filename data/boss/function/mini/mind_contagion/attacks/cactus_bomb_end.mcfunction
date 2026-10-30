tag @e[tag=mind_boss_rand,distance=0..] remove picked
tag @e[tag=mind_boss_rand,distance=0..] remove 0
fill -11773 171 -209 -11747 176 -183 air replace minecraft:structure_void
fill -11773 172 -209 -11747 172 -183 red_sand replace pink_concrete_powder
fill -11773 172 -209 -11747 172 -183 red_sand replace cyan_concrete_powder
fill -11773 172 -209 -11747 172 -183 red_sand replace light_blue_concrete_powder
fill -11773 172 -209 -11747 172 -183 red_sand replace white_concrete_powder

kill @e[tag=cactus_bomb_arrow,distance=0..]

schedule function floaty:sched/boss/mini/mind_contagion/reveal 1s replace
