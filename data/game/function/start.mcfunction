gamemode adventure @a[tag=mg.flw]
xp set @a[tag=mg.flw] 0 points
xp set @a[tag=mg.flw] 0 levels
tp @a[tag=mg.flw] 152 58 -12 -90 0
particle minecraft:enchant 152 59.5 -12 0.3 0.3 0.3 0 300 normal
clear @a[tag=mg.flw]
give @a[tag=mg.flw] writable_book[custom_name={"bold":true,"color":"aqua","text":"Adventure Notes"},lore=["For writing down","important information","along your journey!"],writable_book_content={pages:[{raw:""}]}] 1
give @a[tag=mg.flw] apple 5

# PING IF MULTIPLAYER
scoreboard players set player_count Value 0
execute as @a[tag=mg.flw] run scoreboard players add player_count Value 1
execute if score player_count Value > 1 Value run item replace entity @a[tag=mg.flw] hotbar.8 with carrot_on_a_stick[custom_name={"bold":true,"color":"white","italic":true,"text":"Ping"},lore=[{"color":"dark_purple","text":"Helps you locate your"},{"color":"dark_purple","text":"fellow adventurers by"},{"color":"dark_purple","text":"making them glow!"}],unbreakable={},tooltip_display={hidden_components:["unbreakable"]},custom_model_data={strings:["18"]}] 1

#Pity Manna Start
setblock -9762 272 429 minecraft:redstone_block
spawnpoint @a[tag=mg.flw] 152 58 -12
scoreboard players set $flsp mg.st 26
tag @a[tag=mg.flw] remove ready
scoreboard players set mainstory Story 0
scoreboard players set @a[tag=mg.flw] DeathCount 0

#Important Scores
scoreboard players set @a[tag=mg.flw] grow_timer -1
scoreboard players set @a[tag=mg.flw] shrink_timer -1
scoreboard players set @a[tag=mg.flw] SoundtrackOverride 0

execute as @a[tag=mg.flw] at @s run playsound minecraft:block.bell.use master @s ~ ~ ~ 1 1 1
schedule function floaty:sched/game/start_music 3s replace
