execute positioned 207 40 -14 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"You can just barely make out the words:"},{"text":" Here lies Mortimer Sorrowloo","color":"gray","italic":true}]
scoreboard players set mortimer bool 1

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
