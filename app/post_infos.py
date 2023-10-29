"""
Currently no real markdown posts needed.
To keep the structure and workflow of passing post_infos
while rendering layouts, store all the post_infos here.
"""

# puclication infos
# title, jornal, author, url, coverimg
# {
#     'title': '',
#     'jornal': '',
#     'author': '',
#     'url': '',
#     'coverimg': '',
# },

__publications_infos = [
    {
        'sectionname': '2023',
        'posts': [
            {
                'title': 'Creating Hierarchical Pores in Metal-Organic Frameworks via Post-Synthetic Reactions',
                'jornal': 'Nat. Protoc. 2023, 18, 604-625.',
                'author': 'Wang, K.-Y.; Yang, Z.; Zhang, J.; Banerjee, S.; Joseph, E. A.; Hsu, Y.-C.; Yuan, S.*; Feng, L.*; Zhou, H.-C.*',
                'url': 'https://www.nature.com/articles/s41596-022-00759-7',
                'coverimg': '',
            },
            {
                'title': 'Bioinspired Framework Catalysts: From Enzyme Immobilization to Biomimetic Catalysis',
                'jornal': 'Chem. Rev. 2023, 123, 5347-5420.',
                'author': 'Wang, K.-Y.; Zhang, J.; Hsu. Y.-C.; Lin, H.; Han, Z.; Pang, J.; Yang, Z.; Shi, W.; Zhou, H.-C.*',
                'url': 'https://pubs.acs.org/doi/10.1021/acs.chemrev.2c00879',
                'coverimg': 'https://pubs.acs.org/cms/10.1021/chreay.2023.123.issue-9/asset/chreay.2023.123.issue-9.xlargecover-2.jpg',
            },
            {
                'title': 'Ortho Effects of Tricarboxylate Linkers in Regulating Topologies of Rare-Earth Metal-Organic Frameworks',
                'jornal': 'JACS Au 2023, 3, 1337-1347.',
                'author': 'Li, F.‡; Wang, K.-Y.‡; Liu, Z.; Han, Z.; Kuai, D.; Fan, W.; Feng, L.; Wang, Y.; Wang, X.; Li, Y.; Yang, Z.; Wang, R.; Sun, D.*; Zhou, H.-C.*',
                'url': 'https://pubs.acs.org/doi/10.1021/jacsau.2c00635',
                'coverimg': '',
            },

        ]
    },
]


def get_publication_infos() -> list:
    """
    format the publication infos before sending to jinja

    1. wrap all the author name 'Wang, K.-Y.' with html strong tag
    2. replace ‡ with html escape &Dagger;
    """
    res = []
    for year_posts in __publications_infos:
        year_posts_parsed = {'sectionname': year_posts['sectionname'], 'posts': []}
        for post in year_posts['posts']:
            post_parsed = {}
            for key, val in post.items():
                val_parsed = val.replace('Wang, K.-Y.', '<strong>Wang, K.-Y.</strong>')
                val_parsed = val_parsed.replace('‡', '&Dagger;')
                post_parsed[key] = val_parsed
            year_posts_parsed['posts'].append(post_parsed)
        res.append(year_posts_parsed)
    return res

