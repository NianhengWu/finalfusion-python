SIMILARITY_ORDER_STUTTGART_10 = [
    "Karlsruhe",
    "Mannheim",
    "München",
    "Darmstadt",
    "Heidelberg",
    "Wiesbaden",
    "Kassel",
    "Düsseldorf",
    "Leipzig",
    "Berlin",
]


SIMILARITY_ORDER = [
    "Potsdam",
    "Hamburg",
    "Leipzig",
    "Dresden",
    "München",
    "Düsseldorf",
    "Bonn",
    "Stuttgart",
    "Weimar",
    "Berlin-Charlottenburg",
    "Rostock",
    "Karlsruhe",
    "Chemnitz",
    "Breslau",
    "Wiesbaden",
    "Hannover",
    "Mannheim",
    "Kassel",
    "Köln",
    "Danzig",
    "Erfurt",
    "Dessau",
    "Bremen",
    "Charlottenburg",
    "Magdeburg",
    "Neuruppin",
    "Darmstadt",
    "Jena",
    "Wien",
    "Heidelberg",
    "Dortmund",
    "Stettin",
    "Schwerin",
    "Neubrandenburg",
    "Greifswald",
    "Göttingen",
    "Braunschweig",
    "Berliner",
    "Warschau",
    "Berlin-Spandau",
]


def test_similarity_berlin_40(similarity_fifu):
    for idx, sim in enumerate(similarity_fifu.similarity("Berlin", 40)):
        assert SIMILARITY_ORDER[idx] == sim.word


def test_similarity_stuttgart_10(similarity_fifu):
    for idx, sim in enumerate(similarity_fifu.similarity("Stuttgart", 10)):
        assert SIMILARITY_ORDER_STUTTGART_10[idx] == sim.word
