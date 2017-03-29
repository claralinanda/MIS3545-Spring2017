from math import log


def tf(term, doc, normalize=True):
    doc = doc.lower().split()
    if normalize:
        return doc.count(term.lower()) / float(len(doc))
    else:
        return doc.count(term.lower()) / 1.0


def idf(term, corpus):
    num_texts_with_term = len([True for text in corpus if term.lower()
                               in text.lower().split()])

    # tf-idf calc involves multiplying against a tf value less than 0, so it's important
    # to return a value greater than 1 for consistent scoring. (Multiplying two values
    # less than 1 returns a value less than each of them)

    try:
        return 1.0 + log(float(len(corpus)) / num_texts_with_term)
    except ZeroDivisionError:
        return 1.0


def tf_idf(term, doc, corpus):
    return tf(term, doc) * idf(term, corpus)


# Score queries by calculating cumulative tf_idf score for each term in query

query_scores = {'1': 0, '2': 0, '3': 0}

QUERY_TERMS = ['class', 'bi', 'babson', 'love']

corpus = \
    {'1': 'This class is so cool love it Babson rock',
     '2': 'I learn a lot in BI class I want to be an BI engineer',
     '3': "One of the best class at Babson I love Babson"}

for term in [t.lower() for t in QUERY_TERMS]:
    for doc in sorted(corpus):
        print('TF(%s): %s' % (doc, term), tf(term, corpus[doc]))
    print('IDF: %s' % (term,), idf(term, corpus.values()))
    print()

    for doc in sorted(corpus):
        score = tf_idf(term, corpus[doc], corpus.values())
        print('TF-IDF(%s): %s' % (doc, term), score)
        query_scores[doc] += score
    print()

print("Overall TF-IDF scores for query '%s'" % (' '.join(QUERY_TERMS),))
for (doc, score) in sorted(query_scores.items()):
    print(doc, score)
