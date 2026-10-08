"""Branche la Course d'elytres (id 66) dans le moteur et les menus : python wire_elyrace.py <racine du depot>. Une seule fois
(les ancres ne se retrouvent plus apres le premier passage : relancer s'arrete sur la premiere).
Chaque ancre doit exister EXACTEMENT une fois, sinon le script s'arrete sur un message clair avant d'ecrire dans ce fichier ;
les fins de ligne du fichier (CRLF ou LF) sont conservees. Les fichiers generes (elyrace/**, sub, dialog sub_elyrace,
avancement, tag de degats) viennent de gen_elyrace.py, le hall (plaque, classement) de tools/hall/gen_hall.py.
"""
import json
import os
import sys


def read(path):
    with open(path, encoding='utf-8', newline='') as fh:
        s = fh.read()
    return s, '\r\n' if '\r\n' in s else '\n'


def write(path, s):
    with open(path, 'w', encoding='utf-8', newline='') as fh:
        fh.write(s)


def patch_file(path, old, new):
    s, nl = read(path)
    o, n = old.replace('\n', nl), new.replace('\n', nl)
    if s.count(o) != 1:
        raise SystemExit('ancre trouvee %d fois (1 attendue) dans %s : %s' % (s.count(o), path, old[:70]))
    write(path, s.replace(o, n))


def after(path, anchor, add):
    """Ajoute `add` (des lignes completes) juste apres la ligne `anchor`."""
    patch_file(path, anchor + '\n', anchor + '\n' + add)


def tick_net(f):
    """core/tick : filet qui retire les elytres et fusees de la course aux joueurs qui ne sont pas en course."""
    path = os.path.join(f, 'core', 'tick.mcfunction')
    anchor = 'execute if score $lan mg.t matches 20 run clear @a[tag=!mg.ely] minecraft:firework_rocket[minecraft:custom_data~{mg_ely:1b}]'
    after(path, anchor,
          'execute if score $lan mg.t matches 20 run clear @a[tag=!mg.play] minecraft:elytra[minecraft:custom_data~{mg_elyr:1b}]\n'
          'execute if score $lan mg.t matches 20 run clear @a[tag=!mg.play] minecraft:firework_rocket[minecraft:custom_data~{mg_elyr:1b}]\n')


def request_guard(f):
    """core/request : si prepare a annule la partie (parcours pas construit : core/draw met l'etat a 3), on ne poursuit pas
    le lancement (compte a rebours, gel, titre)."""
    after(os.path.join(f, 'core', 'request.mcfunction'), 'execute if score $game mg.st matches 66 run function mg:elyrace/prepare',
          'execute if score $state mg.st matches 3 run return 0\n')


def wire_all(r):
    f = os.path.join(r, 'data', 'mg', 'function')

    def patch(rel, old, new):
        patch_file(os.path.join(f, rel + '.mcfunction'), old, new)

    def after_fn(rel, anchor, add):
        after(os.path.join(f, rel + '.mcfunction'), anchor, add)

    g = 'execute if score $game mg.st matches %s run function mg:%s\n'
    patch('core/go', 'matches 1..65', 'matches 1..66')
    after_fn('core/request', g.rstrip('\n') % ('65', 'dropadv/c_prepare'), g % ('66', 'elyrace/prepare'))
    request_guard(f)
    patch('core/request', 'execute if score $game mg.st matches 64 run tellraw',
          'execute if score $game mg.st matches 66 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance la ","color":"gray"},'
          '{"text":"🪽 COURSE D\'ÉLYTRES","color":"aqua","bold":true},{"text":" : Canyon du Couchant (18 anneaux, le premier arrivé gagne) !","color":"gray"}]\n'
          'execute if score $game mg.st matches 64 run tellraw')
    after_fn('core/begin', g.rstrip('\n') % ('65', 'dropadv/c_go'), g % ('66', 'elyrace/go'))
    after_fn('core/game_tick', g.rstrip('\n') % ('65', 'dropadv/c_tick'), g % ('66', 'elyrace/tick'))
    after_fn('core/return_lobby', g.rstrip('\n') % ('64..65', 'dropadv/cleanup'), g % ('66', 'elyrace/cleanup'))
    after_fn('core/setup_build', 'schedule function mg:dropadv/build 30s',
             'data remove storage mg:elyrace v1\nschedule function mg:elyrace/build 45s\n')
    after_fn('core/load', 'function mg:core/load_hp', 'function mg:elyrace/objectives\n')
    after_fn('core/load', 'execute if score $setup mg.st matches 1 unless data storage mg:dropadv v3 run schedule function mg:dropadv/build 40s',
             'execute if score $setup mg.st matches 1 unless data storage mg:elyrace v1 run schedule function mg:elyrace/build 60s\n'
             'execute if score $setup mg.st matches 1 unless data storage mg:hall v2 run schedule function mg:hall/build 20s\n')
    patch('desinstaller', 'scoreboard objectives remove mg.erb2', 'scoreboard objectives remove mg.erb2\nfunction mg:elyrace/uninstall')
    tick_net(f)

    # menu d'options : 28 = sous-menu Course d'elytres (meme garde admin que 16..24)
    s, nl = read(os.path.join(f, 'core', 'opt.mcfunction'))
    lock = [l for l in s.split(nl) if l.startswith('execute if score @s mg.opt matches 16..24 unless entity @s[tag=mg.admin] run tellraw')]
    if len(lock) != 1:
        raise SystemExit('core/opt : %d lignes de verrou admin 16..24 (1 attendue)' % len(lock))
    patch('core/opt', lock[0] + '\n', lock[0] + '\n' + lock[0].replace('matches 16..24', 'matches 28', 1) + '\n')
    after_fn('core/opt', 'execute if score @s mg.opt matches 24 if entity @s[tag=mg.admin] run function mg:core/sub/oitc',
             'execute if score @s mg.opt matches 28 if entity @s[tag=mg.admin] run function mg:core/sub/elyrace\n')

    patch('core/menu_chat', 'tellraw @s ["",{"text":" [⬇ The Dropper ▸]"',
          'tellraw @s ["",{"text":" [🪽 Course d\'élytres ▸]","color":"aqua","click_event":{"action":"run_command","command":"trigger mg.opt set 28"},'
          '"hover_event":{"action":"show_text","value":"Plane à travers des anneaux : choisis le parcours."}}]\n'
          'tellraw @s ["",{"text":" [⬇ The Dropper ▸]"')
    patch('aide', 'tellraw @s [{"text":"• Bataille de karts (admins) : ","color":"gray"}',
          'tellraw @s [{"text":"• Course d\'élytres (admins) : ","color":"gray"},{"text":"/trigger mg.go set 66","color":"yellow"},'
          '{"text":" ; Canyon du Couchant, 18 anneaux (reconstruire : /function mg:elyrace/build)","color":"gray"}]\n'
          'tellraw @s [{"text":"• Bataille de karts (admins) : ","color":"gray"}')

    # fenetre du menu : entree « Course d'elytres ▸ » apres « The Dropper ▸ »
    p = os.path.join(r, 'data', 'mg', 'dialog', 'menu.json')
    raw, nl = read(p)
    d = json.loads(raw)
    if json.dumps(d, ensure_ascii=False, indent=2) + '\n' != raw.replace('\r\n', '\n'):
        raise SystemExit('dialog/menu.json : mise en forme inattendue, la reecriture ne serait pas identique')
    idx = [i for i, a in enumerate(d['actions']) if a['label'][0]['text'] == '⬇ The Dropper ▸']
    if len(idx) != 1:
        raise SystemExit('dialog/menu.json : %d entrees « The Dropper » (1 attendue)' % len(idx))
    d['actions'].insert(idx[0] + 1, {
        "label": [{"text": "🪽 Course d'élytres ▸", "color": "aqua"}],
        "tooltip": [{"text": "Plane à travers des anneaux : choisis le parcours.", "color": "gray"}],
        "action": {"type": "minecraft:run_command", "command": "trigger mg.opt set 28"}})
    write(p, (json.dumps(d, ensure_ascii=False, indent=2) + '\n').replace('\n', nl))

    # README et table des IDs
    row = ("| **🪽 Course d'élytres : Canyon du Couchant** (id 66) | Course aérienne en élytres sur un parcours Far West d'environ 1 000 blocs (z 27000) : saut depuis une falaise, "
           "slalom entre cheminées de fée, 3 arches, viaduc ferroviaire, gorge en S, crête à franchir en montée, ville fantôme. **18 anneaux** à franchir dans l'ordre par leur trou de 9 × 9 "
           "(un anneau raté renvoie au dernier point de reprise), **4 points de reprise** (colonnes lumineuses), **3 anneaux d'or** en détour qui donnent chacun une fusée (aucune au départ), "
           "**3 cœurs** (chaque choc contre un mur en retire un ; à zéro, au sol, dans l'eau ou après trop de temps sans planer : retour en l'air au point de reprise). "
           "Le premier arrivé gagne, les autres sont classés pendant 20 s ; au bout de 3 minutes le plus avancé gagne. Parcours vérifié par un pilote automatique simulé. "
           "Générateur : `tools/elyrace/gen_elyrace.py`. | 1+ |\n")
    patch_file(os.path.join(r, 'README.md'), '| **⬇ The Dropper : Aventure** (id 64)', row + '| **⬇ The Dropper : Aventure** (id 64)')
    patch_file(os.path.join(r, 'README.md'), '| `/trigger mg.go set 25` | The Dropper : tube commun | admins |\n',
               '| `/trigger mg.go set 25` | The Dropper : tube commun | admins |\n| `/trigger mg.go set 66` | Course d\'élytres : Canyon du Couchant | admins |\n')
    patch_file(os.path.join(r, 'docs', 'GAMES.md'), '| 65 | `mg:dropadv/c_tick` |\n', '| 65 | `mg:dropadv/c_tick` |\n| 66 | `mg:elyrace/tick` |\n')


def main():
    if len(sys.argv) != 2 or not os.path.isdir(os.path.join(sys.argv[1], 'data', 'mg', 'function')):
        raise SystemExit(__doc__)
    wire_all(sys.argv[1])
    print('ok')


if __name__ == '__main__':
    main()
