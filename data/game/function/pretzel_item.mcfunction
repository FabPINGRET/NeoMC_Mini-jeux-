execute store result score pretzel_item Value run random value 1..19
execute if score Inventory IcelightScepter matches 1 if score has_bundle bool matches 0 store result score pretzel_item Value run random value 0..19
execute if score Inventory IcelightScepter matches 1 if score has_bundle bool matches 1 store result score pretzel_item Value run random value 0..20
execute if score Inventory IcelightScepter matches 0 if score has_bundle bool matches 1 store result score pretzel_item Value run random value 1..20


execute if score pretzel_item Value matches 0 run give @s lapis_lazuli[custom_name={"color":"aqua","text":"Blitzite"},lore=["A shard of","frozen lightning"]] 20
execute if score pretzel_item Value matches 1 run give @s arrow 16
execute if score pretzel_item Value matches 2 run give @s arrow 32
execute if score pretzel_item Value matches 3 run give @s arrow 64
execute if score pretzel_item Value matches 4 run give @s cooked_beef 12
execute if score pretzel_item Value matches 5 run give @s golden_carrot 12
execute if score pretzel_item Value matches 6 run give @s pumpkin_pie 12
execute if score pretzel_item Value matches 7 run give @s golden_apple[custom_name={"color":"light_purple","text":"The Apple of Tastiness"}] 1
execute if score pretzel_item Value matches 8 run give @s carrot_on_a_stick[custom_model_data={strings:["21"]},custom_name={"bold":true,"text":"Shotgun"},lore=["Does what you","think it does.","Consumes arrows."]] 1
execute if score pretzel_item Value matches 9 run give @s turtle_helmet[custom_name={"color":"dark_green","text":"Oogway's Skeleton"}] 1
execute if score pretzel_item Value matches 10 run give @s dragon_head[custom_name={"color":"light_purple","text":"Mascot Head"},lore=["Go Dragons!"]] 1
execute if score pretzel_item Value matches 11 run give @s tipped_arrow[potion_contents={potion:"minecraft:weakness"}] 16
execute if score pretzel_item Value matches 12 run give @s paper[custom_name={"color":"dark_aqua","text":"Hint Note"},lore=["With Knowledge &","Learning in hand,","ring the hostel","bell..."]] 1
execute if score pretzel_item Value matches 13 run give @s spider_eye[custom_name={"color":"red","text":"Pretzel's Extra Eye"},lore=["Hold it for better","night vision. Please","do yourself a favor","and don't eat it."]] 1
execute if score pretzel_item Value matches 14 run give @s feather[custom_name={"color":"aqua","text":"Feather of Speedy Sneakiness"},attribute_modifiers=[{id:"sneaking_speed",type:"sneaking_speed",amount:1,operation:"add_value"}]] 1
execute if score pretzel_item Value matches 15 run give @s beetroot[custom_name={"color":"red","text":"The Noble Beet of Plucky Courage"},attribute_modifiers=[{id:"knockback_resistance",type:"knockback_resistance",amount:1,operation:"add_value"}]] 1
execute if score pretzel_item Value matches 16 run give @s bricks[custom_name={"color":"red","text":"Bricks of Devastating Encumberment"},attribute_modifiers=[{id:"movement_speed",type:"movement_speed",amount:-1,operation:"add_value",slot:"any"}]] 1
execute if score pretzel_item Value matches 17 run give @s netherite_scrap[custom_name={"bold":true,"color":"white","text":"Nothing"},lore=["Nothing hardly has","any properties..."]] 1
execute if score pretzel_item Value matches 18 run give @s potion[custom_name="Potion of Not Being Able to Read",potion_contents={custom_color:1908001,custom_effects:[{id:"minecraft:blindness",amplifier:0,duration:200,show_particles:0b}]}] 1
execute if score pretzel_item Value matches 19 run give @s rotten_flesh[custom_name={"color":"dark_green","text":"Meat of a Horrible Forest Thing"}] 1
execute if score pretzel_item Value matches 20 run give @s red_bundle[custom_name={"color":"red","text":"Pretzelsack"}] 1
