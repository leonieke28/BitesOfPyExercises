# fmt: off
NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


# fmt: on


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
    each name appears only once"""
    title_cased_names = [name.title() for name in names]
    return list(set(title_cased_names))


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    sorted_names = sorted(names, key=lambda name: name.split()[-1], reverse=True)
    return sorted_names


def shortest_first_name(names):
    """Returns the shortest first name (str).
    You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    first_name = [name.split()[0] for name in names]
    shortest_first_name = sorted(first_name, key=len)
    return shortest_first_name[0]
