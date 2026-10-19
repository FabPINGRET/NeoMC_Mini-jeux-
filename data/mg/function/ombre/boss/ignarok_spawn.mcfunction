# Ignarok, dragon de feu : apparition (ici)
function mg:ombre/beast/ignarok
tag @e[tag=mg.ollast] add mg.olbn
tag @e[tag=mg.olbn] add mg.olb_ignarok
tag @e[tag=mg.olbn] add mg.olboss
tag @e[tag=mg.olbn] add mg.olm
scoreboard players operation @e[tag=mg.olbn] mg.olses = $olses mg.st
tag @e[tag=mg.olbn] remove mg.olbn
