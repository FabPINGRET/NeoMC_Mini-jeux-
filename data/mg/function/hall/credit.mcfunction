# Vainqueur (@s, tag mg.win) au retour au lobby : classement du jeu + hall des scores
function mg:hall/top {obj:"mg.wins",key:"wins",lbl:"👑 Champion des mini-jeux",col:"gold",unit:" victoire(s)"}
execute if score $game mg.st matches 1 run function mg:hall/game {obj:"mg.wg_spleef",key:"spleef",lbl:"❄ Spleef",col:"aqua"}
execute if score $game mg.st matches 2 run function mg:hall/game {obj:"mg.wg_tntrun",key:"tntrun",lbl:"✷ TNT Run",col:"red"}
execute if score $game mg.st matches 3 run function mg:hall/game {obj:"mg.wg_pvp",key:"pvp",lbl:"⚔ PvP",col:"gold"}
execute if score $game mg.st matches 4 run function mg:hall/game {obj:"mg.wg_bedwars",key:"bedwars",lbl:"🛏 Bedwars",col:"red"}
execute if score $game mg.st matches 5 run function mg:hall/game {obj:"mg.wg_sheepwar",key:"sheepwar",lbl:"🐑 Sheep War",col:"white"}
execute if score $game mg.st matches 7 run function mg:hall/game {obj:"mg.wg_sheepwar",key:"sheepwar",lbl:"🐑 Sheep War",col:"white"}
execute if score $game mg.st matches 6 run function mg:hall/game {obj:"mg.wg_mobarena",key:"mobarena",lbl:"☠ Mob Arena",col:"dark_green"}
execute if score $game mg.st matches 20..21 run function mg:hall/game {obj:"mg.wg_splegg",key:"splegg",lbl:"❍ Splegg",col:"yellow"}
execute if score $game mg.st matches 22 run function mg:hall/game {obj:"mg.wg_sumo",key:"sumo",lbl:"✊ Sumo",col:"gold"}
execute if score $game mg.st matches 23 run function mg:hall/game {obj:"mg.wg_dropper",key:"dropper",lbl:"⬇ Dropper",col:"aqua"}
execute if score $game mg.st matches 64..65 run function mg:hall/game {obj:"mg.wg_dropper",key:"dropper",lbl:"⬇ Dropper",col:"aqua"}
execute if score $game mg.st matches 26 run function mg:hall/game {obj:"mg.wg_oitc",key:"oitc",lbl:"➶ One in the Chamber",col:"gold"}
execute if score $game mg.st matches 27 run function mg:hall/game {obj:"mg.wg_tnttag",key:"tnttag",lbl:"✹ TNT Tag",col:"red"}
execute if score $game mg.st matches 28 run function mg:hall/game {obj:"mg.wg_blockparty",key:"blockparty",lbl:"▦ Block Party",col:"light_purple"}
execute if score $game mg.st matches 29 run function mg:hall/game {obj:"mg.wg_anvil",key:"anvil",lbl:"⚓ Pluie d'enclumes",col:"gray"}
execute if score $game mg.st matches 30 run function mg:hall/game {obj:"mg.wg_turf",key:"turf",lbl:"▮ Turf Wars",col:"gold"}
execute if score $game mg.st matches 31 run function mg:hall/game {obj:"mg.wg_quake",key:"quake",lbl:"⚡ Quakecraft",col:"aqua"}
execute if score $game mg.st matches 36 run function mg:hall/game {obj:"mg.wg_paintball",key:"paintball",lbl:"▓ Paintball",col:"gold"}
execute if score $game mg.st matches 56 run function mg:hall/game {obj:"mg.wg_icerace",key:"icerace",lbl:"⛵ Course de bateaux",col:"aqua"}
execute if score $game mg.st matches 57..58 run function mg:hall/game {obj:"mg.wg_bb",key:"bb",lbl:"✎ Build Battle",col:"green"}
execute if score $game mg.st matches 59..60 run function mg:hall/game {obj:"mg.wg_party",key:"party",lbl:"★ Mini Party",col:"gold"}
execute if score $game mg.st matches 61..63 run function mg:hall/game {obj:"mg.wg_kart",key:"kart",lbl:"🏎 Kart",col:"red"}
execute if score $game mg.st matches 66 run function mg:hall/game {obj:"mg.wg_elyrace",key:"elyrace",lbl:"🪽 Course d'élytres",col:"aqua"}
execute if score $game mg.st matches 75 run function mg:hall/game {obj:"mg.wg_elytra",key:"elytra",lbl:"🪽 Élytra (3 modes)",col:"aqua"}
execute if score $game mg.st matches 83 run function mg:hall/game {obj:"mg.wg_telephone",key:"telephone",lbl:"📞 Téléphone",col:"gold"}
execute if score $game mg.st matches 84..85 run function mg:hall/game {obj:"mg.wg_tron",key:"tron",lbl:"⚡ Tron",col:"aqua"}
execute if score $game mg.st matches 200..201 run function mg:hall/game {obj:"mg.wg_tron",key:"tron",lbl:"⚡ Tron",col:"aqua"}
execute if score $game mg.st matches 86..87 run function mg:hall/game {obj:"mg.wg_koth",key:"koth",lbl:"👑 King of the Hill",col:"gold"}
execute if score $game mg.st matches 206..209 run function mg:hall/game {obj:"mg.wg_koth",key:"koth",lbl:"👑 King of the Hill",col:"gold"}
execute if score $game mg.st matches 88 run function mg:hall/game {obj:"mg.wg_tower",key:"tower",lbl:"🏰 The Towers",col:"gold"}
execute if score $game mg.st matches 89..90 run function mg:hall/game {obj:"mg.wg_convoy",key:"convoy",lbl:"🚚 Convoi",col:"gold"}
execute if score $game mg.st matches 93 run function mg:hall/game {obj:"mg.wg_ctf",key:"ctf",lbl:"🚩 Capture the Flag",col:"red"}
execute if score $game mg.st matches 94 run function mg:hall/game {obj:"mg.wg_uhc",key:"uhc",lbl:"⛏ Mini UHC Run",col:"gold"}
execute if score $game mg.st matches 202 run function mg:hall/game {obj:"mg.wg_uhc",key:"uhc",lbl:"⛏ Mini UHC Run",col:"gold"}
execute if score $game mg.st matches 204 run function mg:hall/game {obj:"mg.wg_uhc",key:"uhc",lbl:"⛏ Mini UHC Run",col:"gold"}
execute if score $game mg.st matches 95 run function mg:hall/game {obj:"mg.wg_hg",key:"hg",lbl:"🏹 Mini Hunger Games",col:"gold"}
execute if score $game mg.st matches 203 run function mg:hall/game {obj:"mg.wg_hg",key:"hg",lbl:"🏹 Mini Hunger Games",col:"gold"}
execute if score $game mg.st matches 205 run function mg:hall/game {obj:"mg.wg_hg",key:"hg",lbl:"🏹 Mini Hunger Games",col:"gold"}
execute if score $game mg.st matches 96 run function mg:hall/game {obj:"mg.wg_prophunt",key:"prophunt",lbl:"🎭 Prop Hunt",col:"gold"}
execute if score $game mg.st matches 97 run function mg:hall/game {obj:"mg.wg_zombies",key:"zombies",lbl:"🧟 Zombies",col:"dark_green"}
execute if score $game mg.st matches 210 run function mg:hall/game {obj:"mg.wg_zombies",key:"zombies",lbl:"🧟 Zombies",col:"dark_green"}
execute if score $game mg.st matches 212 run function mg:hall/game {obj:"mg.wg_zombies",key:"zombies",lbl:"🧟 Zombies",col:"dark_green"}
execute if score $game mg.st matches 98 run function mg:hall/game {obj:"mg.wg_infection",key:"infection",lbl:"🧪 Infection",col:"green"}
execute if score $game mg.st matches 211 run function mg:hall/game {obj:"mg.wg_infection",key:"infection",lbl:"🧪 Infection",col:"green"}
execute if score $game mg.st matches 213 run function mg:hall/game {obj:"mg.wg_infection",key:"infection",lbl:"🧪 Infection",col:"green"}
execute if score $game mg.st matches 217..219 run function mg:hall/game {obj:"mg.wg_infection",key:"infection",lbl:"🧪 Infection",col:"green"}
execute if score $game mg.st matches 99 run function mg:hall/game {obj:"mg.wg_bomber",key:"bomber",lbl:"💣 Bombardier",col:"red"}
execute if score $game mg.st matches 198 run function mg:hall/game {obj:"mg.wg_chameleon",key:"chameleon",lbl:"🦎 Meccha Chameleon",col:"green"}
execute if score $game mg.st matches 214..216 run function mg:hall/game {obj:"mg.wg_wii",key:"wii",lbl:"🎾 Wii Sports",col:"aqua"}
