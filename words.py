"""Word data for the Hangman game.

Words are grouped by their starting letter so the player can choose
a category (A-Z) before playing. The flattened `words` list is kept
for convenience when a random word is needed from the full set.
"""

words_per_letter = {
    'A': ['apple', 'amber', 'angel', 'april', 'attic', 'agile', 'alarm'],
    'B': ['bacon', 'badge', 'bagel', 'baker', 'balmy', 'banjo', 'barge'],
    'C': ['cabin', 'cacti', 'candy', 'canoe', 'carve', 'cedar', 'charm'],
    'D': ['daisy', 'dally', 'dance', 'debit', 'decaf', 'deity', 'delta'],
    'E': ['eagle', 'ebony', 'eclat', 'edict', 'egret', 'elbow', 'elope'],
    'F': ['fable', 'facet', 'faint', 'fairy', 'faker', 'fancy', 'farce'],
    'G': ['gable', 'gaffe', 'gamer', 'gauze', 'gecko', 'ghost', 'girly'],
    'H': ['habit', 'harpy', 'haste', 'haven', 'hazel', 'hefty', 'heron'],
    'I': ['icing', 'igloo', 'iliac', 'imply', 'inert', 'inlet', 'ionic'],
    'J': ['jaded', 'janky', 'jaunt', 'jelly', 'jerky', 'jetty', 'jiffy'],
    'K': ['karma', 'kayak', 'kebab', 'khaki', 'kinky', 'kiosk', 'knead'],
    'L': ['label', 'lanky', 'lapel', 'latte', 'leech', 'liege', 'lilac'],
    'M': ['macaw', 'madam', 'mafia', 'mango', 'maple', 'marsh', 'mauve'],
    'N': ['nadir', 'nanny', 'nasal', 'naval', 'nectar', 'neigh', 'nerdy'],
    'O': ['oasis', 'obese', 'occur', 'ocean', 'oddly', 'offal', 'olden'],
    'P': ['pagan', 'palsy', 'pansy', 'pasta', 'patio', 'pecan', 'perky'],
    'Q': ['quack', 'quail', 'quake', 'qualm', 'quart', 'quash', 'quasi'],
    'R': ['rabid', 'radar', 'raggy', 'rajah', 'ralph', 'ramen', 'ranch'],
    'S': ['sable', 'salsa', 'satin', 'sauna', 'savvy', 'scald', 'scoff'],
    'T': ['tabby', 'tacit', 'talon', 'tamer', 'tango', 'taper', 'tarry'],
    'U': ['udder', 'ulcer', 'ultra', 'umbra', 'uncle', 'uncut', 'unfed'],
    'V': ['vague', 'valve', 'vapid', 'vault', 'vegan', 'venom', 'verge'],
    'W': ['wacky', 'wafer', 'wager', 'waist', 'waltz', 'warty', 'weary'],
    'X': ['xenon', 'xerox', 'xylem', 'xylol', 'xebec', 'xenia', 'xeric'],
    'Y': ['yacht', 'yahoo', 'yearn', 'yeast', 'yield', 'yodel', 'yokel'],
    'Z': ['zebra', 'zesty', 'zilch', 'zippy', 'zonal', 'zoned', 'zombie'],
}

# Flattened list of every word, useful for random selection.
words = []
for group in words_per_letter.values():
    words.extend(group)
