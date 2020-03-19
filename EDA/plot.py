def plot(self, some):
    from matplotlib import pyplot

    pyplot.scatter(self.dataset_2017, self.dataset_2018)
    pyplot.show()
    return some
