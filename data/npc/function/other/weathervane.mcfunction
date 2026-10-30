execute positioned 66 60 -41 run tellraw @a[distance=..10,tag=mg.flw] {"text":"You look foolish trying to talk to a weathervane.","color":"gray","italic":true}

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
