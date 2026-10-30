execute if score doing_quiz Value matches 0 unless score quiz_question Value matches -1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.cow_moody.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute if score doing_quiz Value matches 1 if score quiz_question Value matches 1 run function game:quiz/1/1
execute if score doing_quiz Value matches 1 if score quiz_question Value matches 2 run function game:quiz/1/2
execute if score doing_quiz Value matches 1 if score quiz_question Value matches 3 run function game:quiz/1/3

execute if score doing_quiz Value matches 2 if score quiz_question Value matches 1 run function game:quiz/2/1
execute if score doing_quiz Value matches 2 if score quiz_question Value matches 2 run function game:quiz/2/2
execute if score doing_quiz Value matches 2 if score quiz_question Value matches 3 run function game:quiz/2/3
execute if score doing_quiz Value matches 2 if score quiz_question Value matches 4 run function game:quiz/2/4

execute if score doing_quiz Value matches 3 if score quiz_question Value matches 1 run function game:quiz/3/1
execute if score doing_quiz Value matches 3 if score quiz_question Value matches 2 run function game:quiz/3/2
execute if score doing_quiz Value matches 3 if score quiz_question Value matches 3 run function game:quiz/3/3
execute if score doing_quiz Value matches 3 if score quiz_question Value matches 4 run function game:quiz/3/4
execute if score doing_quiz Value matches 3 if score quiz_question Value matches 5 run function game:quiz/3/5

execute if score Inventory Amulet matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brainzo","color":"aqua"},{"text":"> I'm sorry, I don't have a","color":"white"},{"text":" quiz ","color":"light_purple"},{"text":"ready yet. Come back after you've","color":"white"},{"text":" helped the Valorites ","color":"gold"},{"text":"and I'll surely have one ready by then!","color":"white"}]

execute if score Inventory Amulet matches 1 if score quiz_1 bool matches 0 if score doing_quiz Value matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brainzo","color":"aqua"},{"text":"> I have a prize for you if you can correctly answer every question in my first quiz! Press the ","color":"white"},{"text":"C","color":"aqua","bold":true},{"text":" button to start it.","color":"white"}]
execute if score Inventory Amulet matches 1 if score quiz_1 bool matches 0 if score doing_quiz Value matches 0 run setblock 10082 59 -245 minecraft:polished_blackstone_button[face=floor,facing=north,powered=false]

execute if score Inventory Amulet matches 1 if score Inventory TomeOfTongues matches 0 if score quiz_1 bool matches 1 if score doing_quiz Value matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brainzo","color":"aqua"},{"text":"> I'm sorry, my next","color":"white"},{"text":" quiz ","color":"light_purple"},{"text":"isn't ready yet. Come back after you've","color":"white"},{"text":" helped the Pygmies ","color":"green"},{"text":"and I'll surely have one ready by then!","color":"white"}]

execute if score Inventory TomeOfTongues matches 1 if score quiz_1 bool matches 1 if score quiz_2 bool matches 0 if score doing_quiz Value matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brainzo","color":"aqua"},{"text":"> I have a prize for you if you can correctly answer every question in my second quiz! Press the ","color":"white"},{"text":"C","color":"aqua","bold":true},{"text":" button to start it.","color":"white"}]
execute if score Inventory TomeOfTongues matches 1 if score quiz_1 bool matches 1 if score quiz_2 bool matches 0 if score doing_quiz Value matches 0 run setblock 10082 59 -245 minecraft:polished_blackstone_button[face=floor,facing=north,powered=false]

execute if score Inventory TomeOfTongues matches 1 if score Inventory Honeyboost matches 0 if score quiz_2 bool matches 1 if score doing_quiz Value matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brainzo","color":"aqua"},{"text":"> I'm sorry, my next","color":"white"},{"text":" quiz ","color":"light_purple"},{"text":"isn't ready yet. Come back after you've","color":"white"},{"text":" helped the Glooblins ","color":"light_purple"},{"text":"and I'll surely have one ready by then!","color":"white"}]

execute if score Inventory Honeyboost matches 1 if score quiz_2 bool matches 1 if score quiz_3 bool matches 0 if score doing_quiz Value matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brainzo","color":"aqua"},{"text":"> I have a prize for you if you can correctly answer every question in my final quiz! Press the ","color":"white"},{"text":"C","color":"aqua","bold":true},{"text":" button to start it.","color":"white"}]
execute if score Inventory Honeyboost matches 1 if score quiz_2 bool matches 1 if score quiz_3 bool matches 0 if score doing_quiz Value matches 0 run setblock 10082 59 -245 minecraft:polished_blackstone_button[face=floor,facing=north,powered=false]

execute if score quiz_3 bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brainzo","color":"aqua"},{"text":"> Thanks for taking my quizzes! I hope they grew your brain!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
