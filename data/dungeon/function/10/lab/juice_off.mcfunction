execute unless score ta_lab_step Value matches 7 run scoreboard players set ta_lab_step Value 0
execute if score ta_lab_step Value matches 7 unless blocks -11711 218 306 -11711 218 308 -11711 212 306 all run scoreboard players set ta_lab_step Value 0
execute if score ta_lab_step Value matches 7 if blocks -11711 218 306 -11711 218 308 -11711 212 306 all run scoreboard players set ta_lab_step Value 8


scoreboard players set ta_lab_kablasts Value 0
scoreboard players set ta_lab_pumps Value 0
