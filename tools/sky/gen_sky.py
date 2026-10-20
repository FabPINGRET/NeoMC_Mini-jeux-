"""Mini-jeu « Élytra » (id de base 74, mode dans $elm mg.st) : génère data/mg/function/sky/*.mcfunction.

  Mode 1 — Course d'anneaux : 20 anneaux lumineux dans un décor aérien (îles suspendues, falaises
           flottantes, arches, tours, nuages), x -200..200 / z 27600..28400 / y 90..250.
  Mode 2 — Course + combat : même parcours, arc + charges de vent, les touchés sont « sonnés ».
  Mode 3 — Survie en vol : arène séparée centrée (0, 29000), rayon <= 100, y 90..220
           (anneau de pics flottants, obstacles, colonnes de vent), zone qui rétrécit.

Construction asynchrone : le décor est découpé en sections (forceload temporaire, attente du
chargement, construction en plusieurs morceaux, forceload retiré). Tout est déterministe (graine fixe).
Lancer depuis la racine du dépôt : python3 tools/sky/gen_sky.py

Façade : le code est réparti dans sky_track (parcours, constantes), sky_vox (voxels -> commandes), sky_shapes (formes du décor),
sky_layout (placement + sections), sky_game (objets, plateformes, préparation / départ) et sky_modes (course, combat, survie,
nettoyage). Ce fichier garde le dictionnaire `files`, l'appel des modules dans l'ordre et l'écriture sur disque.
"""
import os

import sky_game
import sky_layout
import sky_modes

OUT = os.path.join('data', 'mg', 'function', 'sky')
SUB = os.path.join(OUT, 'b')
ADV = os.path.join('data', 'mg', 'advancement', 'sky')

files = {}


def W(name, lines):
    files[name] = '\n'.join(lines) + '\n'


HURT_JSON = '''{
  "criteria": {
    "hit": {
      "trigger": "minecraft:entity_hurt_player",
      "conditions": {
        "damage": {
          "type": {
            "source_entity": {
              "minecraft:entity_type": "minecraft:player"
            },
            "direct_entity": {
              "minecraft:entity_type": [
                "minecraft:arrow",
                "minecraft:wind_charge"
              ]
            }
          }
        }
      }
    }
  },
  "rewards": {
    "function": "mg:sky/hurt_adv"
  }
}
'''


def main():
    features, sec_keys, steps_b, steps_w, stats = sky_layout.build(W, SUB)
    sky_game.game(W, steps_b, steps_w, sec_keys)
    sky_modes.modes(W, OUT)

    # =====================================================================================
    # Écriture
    # =====================================================================================
    for d in (OUT, SUB, os.path.join(OUT, 'rk')):
        os.makedirs(d, exist_ok=True)
        for f in os.listdir(d):
            if f.endswith('.mcfunction'):
                os.remove(os.path.join(d, f))
    for name, txt in files.items():
        with open(os.path.join(OUT, name + '.mcfunction'), 'w', encoding='utf-8') as f:
            f.write(txt)
    os.makedirs(ADV, exist_ok=True)
    with open(os.path.join(ADV, 'hurt.json'), 'w', encoding='utf-8') as f:
        f.write(HURT_JSON)

    tot = sum(s[2] for s in stats)
    print(f'{len(files)} fonctions, {len(features)} éléments de décor, {len(sec_keys)} sections, '
          f'{tot} commandes de construction, {len(steps_b)} étapes')
    for s in stats:
        print('  section', s[0], s[1], 'cmds', s[2], 'morceaux', s[3], 'tronçons', s[4], 'voxels', s[5])
    from collections import Counter
    print(Counter(n for n, _, _ in features))


if __name__ == '__main__':
    main()
