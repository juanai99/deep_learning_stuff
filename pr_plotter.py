'''
This short script helps you to plot a precision-recall-curve
and a curve for the F-Beta score depending on the number of positive labeled inputs.
'''

import matplotlib.pyplot as plt

real_labels = [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0]
beta = 0.5

def precision(pred_labels):
    # tp : real_label = 1, pred_label = 1
    tp = float(sum([p == r == 1 for (p, r) in zip(pred_labels, real_labels)]))

    # fp : real_label = 0, pred_label = 1
    fp = float(sum([(r == 0 and p == 1) for (p, r) in zip(pred_labels, real_labels)]))

    return tp / (tp + fp)

def recall(pred_labels):
    # tp : real_label = 1, pred_label = 1
    tp = float(sum([p == r == 1 for (p, r) in zip(pred_labels, real_labels)]))

    # fn : real_label = 1, pred_label = 0
    fn = float(sum([(r == 1 and p == 0) for (r, p) in zip(real_labels, pred_labels)]))

    return tp / (tp + fn)

def get_label_list(number_of_positive_labels): #between 1 and 15
    # returns a sequence of 1 following a sequence of 0. relatio depending on amount_of_positive_labels
    return [1 for _ in range(number_of_positive_labels)] + [0 for _ in range(15-number_of_positive_labels)]

def f_beta_score(p, r):
    return ( 1 + beta**2 ) * ( (p*r) / ((beta**2)*p + r) )

def plot_precision_recall_curve():
    # compute precision and recall for every possible classification limitor between 1 and 15
    prec, rec = [], []
    for i in range(1, 16):
        list = get_label_list(i)
        prec.append(precision(list))
        rec.append(recall(list))

    # plot the results
    plt.plot(rec, prec, 'b-')
    '''
    change last argument of plot() method to change appearance.
    for example,
    'b.' shows blue dots,
    'ro' shows red circles and
    'g+' shows green pluses
    '''

    # set the range of y axis
    ax = plt.gca()
    ax.set_ylim([0.0, 1.1])

    # set labels and show
    plt.ylabel("Precision")
    plt.xlabel("Recall")
    plt.show()


def plot_f_beta_score_gen_x():
    # plot f_beta score depending on the amount of positive predicted inputs
    x = range(1, 16)
    y = []

    # compute f_beta score for every possible classification limitor between 1 and 15
    for i in x:
        pred_labels = get_label_list(i)
        p = precision(pred_labels)
        r = recall(pred_labels)
        y.append(f_beta_score(p, r))

    # plot
    plt.plot(x, y, 'b.')
    plt.ylabel("F-Beta")
    plt.xlabel("x")
    plt.show()


# de-comment to plot the desired curve

#plot_precision_recall_curve()
#plot_f_beta_score_gen_x()
