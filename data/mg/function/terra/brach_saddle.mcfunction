# @s : brachiosaure monté sans selle → sellé (sinon on ne peut pas le diriger)
item replace entity @s saddle with minecraft:saddle
execute on passengers run title @s actionbar {"text":"🦕 Brachiosaure sellé : Z/Q/S/D pour le diriger, espace = élan","color":"yellow"}
