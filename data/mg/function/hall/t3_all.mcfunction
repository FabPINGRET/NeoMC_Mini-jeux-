# @s (joueur en ligne) : ses victoires de chaque jeu reportées dans les top 3 (toutes les minutes ; remplit les top 3 au fil des connexions)
execute if score @s mg.wg_spleef matches 1.. run function mg:hall/t3 {k:"spleef",obj:"mg.wg_spleef",lbl:"❄ Spleef",col:"aqua"}
execute if score @s mg.wg_tntrun matches 1.. run function mg:hall/t3 {k:"tntrun",obj:"mg.wg_tntrun",lbl:"✷ TNT Run",col:"red"}
execute if score @s mg.wg_pvp matches 1.. run function mg:hall/t3 {k:"pvp",obj:"mg.wg_pvp",lbl:"⚔ PvP",col:"gold"}
execute if score @s mg.wg_bedwars matches 1.. run function mg:hall/t3 {k:"bedwars",obj:"mg.wg_bedwars",lbl:"🛏 Bedwars",col:"red"}
execute if score @s mg.wg_sheepwar matches 1.. run function mg:hall/t3 {k:"sheepwar",obj:"mg.wg_sheepwar",lbl:"🐑 Sheep War",col:"white"}
execute if score @s mg.wg_mobarena matches 1.. run function mg:hall/t3 {k:"mobarena",obj:"mg.wg_mobarena",lbl:"☠ Mob Arena",col:"dark_green"}
execute if score @s mg.wg_splegg matches 1.. run function mg:hall/t3 {k:"splegg",obj:"mg.wg_splegg",lbl:"❍ Splegg",col:"yellow"}
execute if score @s mg.wg_sumo matches 1.. run function mg:hall/t3 {k:"sumo",obj:"mg.wg_sumo",lbl:"✊ Sumo",col:"gold"}
execute if score @s mg.wg_dropper matches 1.. run function mg:hall/t3 {k:"dropper",obj:"mg.wg_dropper",lbl:"⬇ Dropper",col:"aqua"}
execute if score @s mg.wg_oitc matches 1.. run function mg:hall/t3 {k:"oitc",obj:"mg.wg_oitc",lbl:"➶ One in the Chamber",col:"gold"}
execute if score @s mg.wg_tnttag matches 1.. run function mg:hall/t3 {k:"tnttag",obj:"mg.wg_tnttag",lbl:"✹ TNT Tag",col:"red"}
execute if score @s mg.wg_blockparty matches 1.. run function mg:hall/t3 {k:"blockparty",obj:"mg.wg_blockparty",lbl:"▦ Block Party",col:"light_purple"}
execute if score @s mg.wg_anvil matches 1.. run function mg:hall/t3 {k:"anvil",obj:"mg.wg_anvil",lbl:"⚓ Pluie d'enclumes",col:"gray"}
execute if score @s mg.wg_turf matches 1.. run function mg:hall/t3 {k:"turf",obj:"mg.wg_turf",lbl:"▮ Turf Wars",col:"gold"}
execute if score @s mg.wg_quake matches 1.. run function mg:hall/t3 {k:"quake",obj:"mg.wg_quake",lbl:"⚡ Quakecraft",col:"aqua"}
execute if score @s mg.wg_paintball matches 1.. run function mg:hall/t3 {k:"paintball",obj:"mg.wg_paintball",lbl:"▓ Paintball",col:"gold"}
execute if score @s mg.wg_icerace matches 1.. run function mg:hall/t3 {k:"icerace",obj:"mg.wg_icerace",lbl:"⛵ Course de bateaux",col:"aqua"}
execute if score @s mg.wg_bb matches 1.. run function mg:hall/t3 {k:"bb",obj:"mg.wg_bb",lbl:"✎ Build Battle",col:"green"}
execute if score @s mg.wg_party matches 1.. run function mg:hall/t3 {k:"party",obj:"mg.wg_party",lbl:"★ Mini Party",col:"gold"}
execute if score @s mg.wg_kart matches 1.. run function mg:hall/t3 {k:"kart",obj:"mg.wg_kart",lbl:"🏎 Kart",col:"red"}
execute if score @s mg.wg_elyrace matches 1.. run function mg:hall/t3 {k:"elyrace",obj:"mg.wg_elyrace",lbl:"🪽 Course d'élytres",col:"aqua"}
execute if score @s mg.wg_elytra matches 1.. run function mg:hall/t3 {k:"elytra",obj:"mg.wg_elytra",lbl:"🪽 Élytra (3 modes)",col:"aqua"}
execute if score @s mg.wg_telephone matches 1.. run function mg:hall/t3 {k:"telephone",obj:"mg.wg_telephone",lbl:"📞 Téléphone",col:"gold"}
execute if score @s mg.wg_tron matches 1.. run function mg:hall/t3 {k:"tron",obj:"mg.wg_tron",lbl:"⚡ Tron",col:"aqua"}
execute if score @s mg.wg_koth matches 1.. run function mg:hall/t3 {k:"koth",obj:"mg.wg_koth",lbl:"👑 King of the Hill",col:"gold"}
execute if score @s mg.wg_tower matches 1.. run function mg:hall/t3 {k:"tower",obj:"mg.wg_tower",lbl:"🏰 The Towers",col:"gold"}
execute if score @s mg.wg_convoy matches 1.. run function mg:hall/t3 {k:"convoy",obj:"mg.wg_convoy",lbl:"🚚 Convoi",col:"gold"}
execute if score @s mg.wg_ctf matches 1.. run function mg:hall/t3 {k:"ctf",obj:"mg.wg_ctf",lbl:"🚩 Capture the Flag",col:"red"}
execute if score @s mg.wg_uhc matches 1.. run function mg:hall/t3 {k:"uhc",obj:"mg.wg_uhc",lbl:"⛏ Mini UHC Run",col:"gold"}
execute if score @s mg.wg_hg matches 1.. run function mg:hall/t3 {k:"hg",obj:"mg.wg_hg",lbl:"🏹 Mini Hunger Games",col:"gold"}
execute if score @s mg.wg_prophunt matches 1.. run function mg:hall/t3 {k:"prophunt",obj:"mg.wg_prophunt",lbl:"🎭 Prop Hunt",col:"gold"}
execute if score @s mg.wg_zombies matches 1.. run function mg:hall/t3 {k:"zombies",obj:"mg.wg_zombies",lbl:"🧟 Zombies",col:"dark_green"}
execute if score @s mg.wg_infection matches 1.. run function mg:hall/t3 {k:"infection",obj:"mg.wg_infection",lbl:"🧪 Infection",col:"green"}
execute if score @s mg.wg_bomber matches 1.. run function mg:hall/t3 {k:"bomber",obj:"mg.wg_bomber",lbl:"💣 Bombardier",col:"red"}
execute if score @s mg.wg_chameleon matches 1.. run function mg:hall/t3 {k:"chameleon",obj:"mg.wg_chameleon",lbl:"🦎 Meccha Chameleon",col:"green"}
execute if score @s mg.wg_wii matches 1.. run function mg:hall/t3 {k:"wii",obj:"mg.wg_wii",lbl:"🎾 Wii Sports",col:"aqua"}
execute if score @s mg.wg_soleil matches 1.. run function mg:hall/t3 {k:"soleil",obj:"mg.wg_soleil",lbl:"🔴 1, 2, 3 Soleil",col:"red"}
execute if score @s mg.wg_autotamp matches 1.. run function mg:hall/t3 {k:"autotamp",obj:"mg.wg_autotamp",lbl:"🚗 Autos tamponneuses",col:"aqua"}
execute if score @s mg.wg_slimejump matches 1.. run function mg:hall/t3 {k:"slimejump",obj:"mg.wg_slimejump",lbl:"🟩 Slime Jump",col:"green"}
execute if score @s mg.wg_lab matches 1.. run function mg:hall/t3 {k:"lab",obj:"mg.wg_lab",lbl:"🙈 Labyrinthe aveugle",col:"light_purple"}
execute if score @s mg.wg_master matches 1.. run function mg:hall/t3 {k:"master",obj:"mg.wg_master",lbl:"👑 Master dit",col:"gold"}
execute if score @s mg.wg_murder matches 1.. run function mg:hall/t3 {k:"murder",obj:"mg.wg_murder",lbl:"🔪 Murder Mystery",col:"red"}
execute if score @s mg.wg_bman matches 1.. run function mg:hall/t3 {k:"bman",obj:"mg.wg_bman",lbl:"💣 Bomberman",col:"red"}
execute if score @s mg.wg_maze matches 1.. run function mg:hall/t3 {k:"maze",obj:"mg.wg_maze",lbl:"🌀 Labyrinthe géant",col:"light_purple"}
