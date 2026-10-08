# Classe NINJA (@s) : vitesse, charges de vent, invisibilité courte
give @s minecraft:iron_sword
give @s minecraft:wind_charge 4
give @s minecraft:potion[potion_contents={custom_color:8356754,custom_effects:[{id:"minecraft:invisibility",duration:160,show_particles:false}]},custom_name=[{"text":"Fumigène (invisibilité 8 s)","color":"blue","italic":false}]] 1
give @s minecraft:golden_apple 1
item replace entity @s armor.head with minecraft:leather_helmet[dyed_color=1908001]
item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=1908001]
item replace entity @s armor.legs with minecraft:leather_leggings[dyed_color=1908001]
item replace entity @s armor.feet with minecraft:leather_boots[dyed_color=1908001]
effect give @s minecraft:speed infinite 0 true
effect give @s minecraft:jump_boost infinite 1 true
