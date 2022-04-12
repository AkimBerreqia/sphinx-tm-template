class TMConfig:

    title = u"Site interactif d'apprentissage de la cryptologie"
    first_name = 'Akim'
    last_name = 'Berreqia'
    author = f'{first_name} {last_name}'
    year = u'2021'
    month = u'Décembre'
    seminary_title = u'Développement d’outils ou matériel d’enseignement de l’informatique'
    tutor = u"Cédric Donner"
    release = "Version finale"
    repository_url = "https://github.com/{your-docs-url}"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

tmconfig = TMConfig()