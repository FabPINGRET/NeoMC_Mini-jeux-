# Mob Arena — classe NINJA (@s) : vitesse, charges de vent, invisibilité courte
give @s minecraft:iron_sword[unbreakable={},enchantments={sharpness:2}]
give @s minecraft:wind_charge 8
give @s minecraft:potion[potion_contents={custom_color:8356754,custom_effects:[{id:"minecraft:invisibility",duration:160,show_particles:false}]},custom_name=[{"text":"Fumigène (invisibilité 8 s)","color":"blue","italic":false}]] 2
give @s minecraft:cooked_beef 8
item replace entity @s armor.head with minecraft:leather_helmet[unbreakable={},dyed_color=1908001]
item replace entity @s armor.chest with minecraft:chainmail_chestplate[unbreakable={}]
item replace entity @s armor.legs with minecraft:leather_leggings[unbreakable={},dyed_color=1908001]
item replace entity @s armor.feet with minecraft:leather_boots[unbreakable={},dyed_color=1908001]
effect give @s minecraft:speed infinite 1 true
effect give @s minecraft:jump_boost infinite 1 true
