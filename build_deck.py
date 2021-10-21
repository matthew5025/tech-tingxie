import genanki
import json
import os

data = dict()

if not os.path.isfile("notes.json"):
    # Initialise
    data['tags'] = []
    data['notes'] = []
    with open('notes.json', 'w') as f:
        json.dump(data, f)

else:
    with open('notes.json',) as f:
        data = json.load(f)

my_model = genanki.Model(
    1907366781,  # DO NOT CHANGE THIS, WILL BREAK THE DECK
    'Simple Model',
    fields=[
        {'name': 'engWord'},
        {'name': 'chiWord'},
        {'name': 'pinyin'},
        {'name': 'engEg1'},
        {'name': 'chiEg1'},
        {'name': 'engEg2'},
        {'name': 'chiEg2'},
        {'name': 'comments'},
        {'name': 'Guid'},
    ],
    templates=[
        {
            'name': 'eng2chi',
            'qfmt': '<h1>{{engWord}}</h1><br>Eg1: {{engEg1}}<br>Eg2 :{{engEg2}}<br>{{comments}}',
            'afmt': '{{FrontSide}}<hr id="answer"><h1>{{chiWord}}</h1><br>{{pinyin}}<br>Eg1: {{chiEg1}}<br>Eg2 :{{chiEg2}}',
        },
        {
            'name': 'chi2eng',
            'qfmt': '<h1>{{chiWord}}</h1><br>{{pinyin}}<br>Eg1: {{chiEg1}}<br>Eg2 :{{chiEg2}}<br>{{comments}}',
            'afmt': '{{BackSide}}<hr id="answer"><h1>{{engWord}}</h1><br>Eg1: {{engEg1}}<br>Eg2 :{{engEg2}}',
        }
    ])

my_deck = genanki.Deck(
    1876378956,  # DO NOT CHANGE THIS, WILL BREAK THE DECK!
    'Tech Tingxie')

for note in data['notes']:
    field_vals = list(note.values())[:-1]  # excludes tags
    my_note = genanki.Note(
        model=my_model,
        fields=field_vals,
        tags=note['tags'])
    my_deck.add_note(my_note)

genanki.Package(my_deck).write_to_file('tech-tingxie.apkg')
