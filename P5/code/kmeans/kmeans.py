#!/usr/bin/env python

import copy
import numpy as np


class KMeansClassifier(object):
    """ K-Means Classifier Class """

    def __init__(self, K, centers, points):
        """
        Initialize classifier

        :param K: number of clusters
        :param centers: np list of centers (length K)
        :param points: np list of points
        """
        self.K = K
        self.centers = centers
        self.points = points

        # clusters[i] contains all points assigned to it
        self.clusters = [[] for _ in range(K)]

    def fit(self):
        """
        Fit the points to the K clusters
        """
        i = 0
        while True:
            prev_centers = copy.deepcopy(self.centers)
            self.clusters = [[] for _ in range(self.K)]

            self.assign_clusters()
            self.update_centers()

            # Stop once we have converged
            if prev_centers == self.centers:
                break
            i += 1

    def assign_clusters(self):
        """
        TODO

        Assign each point to the closest cluster, based on
        the center position of that cluster.

        Hints: Look into np.linalg.norm and np.subtract
        """
        self.clusters[-1] = self.points
        
    def update_centers(self):
        """
        TODO

        Update the cluster centers based on the mean of all
        points assigned to it.
        """
        pass

    def error(self):
        """
        TODO

        Implement the K-Means error function, sum of squared distance between
        all points and their assigned center.

        Hints: Like assign_cluster, look into np.linalg.norm and np.subtract.
               Make sure to square each distance!
        """
        return 0.0


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    print("computing kmeans for k=3 and k=4 (close the first window to see the second and the second to exit)");
    points = np.load('easy.npy')

    centers = [[1., 1.], [8., 1.], [1., 8.]]

    kmeans = KMeansClassifier(3, centers, points)
    kmeans.fit()
    print('Error: {}'.format(kmeans.error()))

    for cluster in kmeans.clusters:
        try:
            plt.plot(zip(*cluster)[0], zip(*cluster)[1], 'o')
        except:
            continue
    plt.plot(zip(*kmeans.centers)[0], zip(*kmeans.centers)[1], 'x')
    plt.title('KMeans with k=3')
    plt.show()

    centers = [[1., 1.], [8., 1.], [1., 8.], [8., 8.]]

    kmeans = KMeansClassifier(4, centers, points)
    kmeans.fit()
    print('Error: {}'.format(kmeans.error()))

    for cluster in kmeans.clusters:
        try:
            plt.plot(zip(*cluster)[0], zip(*cluster)[1], 'o')
        except:
            continue
    plt.plot(zip(*kmeans.centers)[0], zip(*kmeans.centers)[1], 'x')
    plt.title('KMeans with k=4')
    plt.show()
