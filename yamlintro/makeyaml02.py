

import yaml

def main():
    hitchhikers = [{'name': 'zaphod Beeblebrox', 'species': 'Betelgeusian'}, {'name': 'Arthur Dent', 'species': 'Human'}]

    print(hitchhikers)
    yamlstring = yaml.dump(hitchhikers)

    print(yamlstring)


main()
