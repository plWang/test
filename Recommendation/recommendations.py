from math import sqrt
import urllib2

critics = {
    'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Planet': 3.5, 'Just My Luck': 3.0, 'Superman Returns': 3.5,
                  'You, Me and Dupree': 2.5, 'The Night Listener': 3.0},
    'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Planet': 3.5, 'Just My Luck': 1.5, 'Superman Returns': 5.0,
                     'You, Me and Dupree': 3.5, 'The Night Listener': 3.0},
    'Michael Philips': {'Lady in the Water': 2.5, 'Snakes on a Planet': 3.0, 'Superman Returns': 3.5,
                        'The Night Listener': 4.0},
    'Claudia Puig': {'Lady in the Water': 3.5, 'Just My Luck': 3.0, 'Superman Returns': 4.0, 'You, Me and Dupree': 2.5,
                     'The Night Listener': 4.5},
    'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Planet': 4.0, 'Just My Luck': 2.0, 'Superman Returns': 3.0,
                     'You, Me and Dupree': 2.0, 'The Night Listener': 3.0},
    'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Planet': 4.0, 'Just My Luck': 3.0, 'Superman Returns': 5.0,
                      'You, Me and Dupree': 3.5},
    'Toby': {'Snakes on a Planet': 4.5, 'Superman Returns': 4.0, 'You, Me and Dupree': 1.0}
}


def sim_distance(prefs, person1, person2):
    si = {}
    # get shared item list
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    if len(si) == 0:
        return 0
    sum_of_squares = sum(
        [pow(prefs[person1][item] - prefs[person2][item], 2) for item in prefs[person1] if item in prefs[person2]])
    return 1 / (1 + sqrt(sum_of_squares))


def sim_pearson(prefs, p1, p2):
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    n = len(si)
    if n == 0:
        return 1

    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])

    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    # Calculate pearson
    num = pSum - (sum1 * sum2) / n
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0: return 0

    r = num / den

    return r


if __name__ == "__main__":
    result = sim_pearson(critics, 'Lisa Rose', 'Gene Seymour')
    print result