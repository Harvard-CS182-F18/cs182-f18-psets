from math import log

class TextClassifier:
    """
    In this question, you will implement a classifier that predicts
    the number of stars a reviewer gave a movie from the text of the review.

    You will process the reviews in the dataset we provide, then
    implement a Naive Bayes classifier to do the prediction.

    But first, some math!
    """

    def q1(self):
        """
        Suppose you roll a 4-sided die of unknown bias, and you observe
        the following sequence of values:
        3   1   4   4   2   1   2   4   2   1   2   1   1   1   1   4   3   4   4   1
        Given only this information, what are the most likely
        probabilities of rolling each side? (Hardcoding is fine)

        Hint: Think about likelihood here as count probabilities.
        """
        return [0.1, 0.8, 0.2, 0.0]

    def q2(self):
        """
        You just fit a multinomial distribution!

        Now suppose you have a prior belief that the die is fair.
        After some omitted math involving a conjugate Dirichlet distribution,
        you realize that you can encode this prior by simply adding
        some "fake" observations of each side. The number of observations
        is the "strength" of your prior belief.
        Using the same observations as in q1 and a prior with a per-side
        "strength" of 2, what are the probabilities of rolling each side??

        Hint: Should be the same as q1, except you add 2 "fake" observations
        per side.
        """
        return [0.1, 0.8, 0.2, 0.0]

    def q3(self, counts=[1, 1, 3, 8]):
        """
        You might be wondering what dice have to do with NLP.
        We will model each possible rating (one of the five numbers of stars)
        as a die, with each word in the dictionary as a face.

        This is a multinomial Naive Bayes classifier, because the words are
        drawn from a per-rating multinomial distribution and we treat
        each word in a review as independent (conditioned on the rating). That is,
        once the rating has emitted one word to the review, the next word
        has the same distribution over possible values as the first.

        In this question, you will write a function that computes p(word|rating), the
        probability that the rating under question will produce
        each of the words in our dictionary -- in other words the bias of this
        particular rating die.

        Inputted to this function is counts, an array containing the number of
        observations for the first 4 words.

        Hint: This should be very similar to the previous problem.  Think about
        counts as a more compact representation of a string of observations.
        """
        return [0.1, 0.8, 0.2, 0.0]

    def q4(self, infile):
        """
        You'll notice that actual words didn't appear in the last question.
        Array indices are nicer to work with than words, so we typically
        write a dictionary encoding the words as numbers. This turns
        review strings into lists of integers. You will count the occurrences
        of each integer in reviews of each class.

        The infile has one review per line, starting with the rating and then a space.
        Note that the "words" include things like punctuation and numbers. Don't worry
        about this distinction for now; any string that occurs between spaces is a word.

        You must do three things in this question: build the dictionary,
        count the occurrences of each word in each rating and count the number
        of reviews with each rating.
        The words should be numbered sequentially in the order they first appear.
        counts[ranking][word] is the number of times word appears in any of the
        reviews corresponding to ranking
        nrated[ranking] is the total number of reviews with each ranking

        Hint: Make sure to actually set the self.dict, self.counts, and
        self.nrated variables!
        """
        # self.dict = {"compsci": 0, "182": 1, ".": 2}
        # self.counts = [[0,0,0],[0,0,0],[1,1,1],[0,0,0],[0,0,0]]
        # self.nrated = [0,0,1,0,0]

        # Loop through file and fill dict and nrated
        self.dict = {}
        self.nrated = [0] * 5

        # Fill counts
        self.counts = [[0] * len(self.dict) for _ in range(5)]

    def q5(self, alpha=1):
        """
        Now you'll fit the model. For historical reasons, we'll call it F.
        F[rating][word] is -log(p(word|rating)).
        The ratings run from 0-4 to match array indexing.
        Alpha is the per-word "strength" of the prior (as in q2).
        (What might "fairness" mean here?)

        Hint: p(word|rating) =
        (alpha + self.counts[rating][word]) /
          (sum(self.counts[rating]) + (alpha * len(self.counts[rating])))

        Though, you might need to add some float() operators.
        """
        self.F = [[0] * len(self.dict) for _ in range(5)]

    def q6(self, infile):
        """
        Test time! The infile has the same format as it did before. For each review,
        predict the rating. Ignore words that don't appear in your dictionary.
        Are there any factors that won't affect your prediction?
        You'll report both the list of predicted ratings in order and the accuracy.
        """
        return ([2], 0.000000000000182)

    def q7(self, infile):
        """
        Alpha (q5) is a hyperparameter of this model - a tunable option that affects
        the values that appear in F. Let's tune it!
        We've split the dataset into 3 parts: the training set you use to fit the model
        the validation and test sets you use to evaluate the model. The training set
        is used to optimize the regular parameters, and the validation set is used to
        optimize the hyperparameters. (Why don't you want to set the hyperparameters
        using the test set accuracy?)
        Find and return a good value of alpha (hint: you will want to call q5 and q6).
        What happens when alpha = 0?
        """
        return 0

    """
    You did it! If you're curious, the dataset came from (Socher 2013), which describes
    a much more sophisticated model for this task.
    Socher, R., Perelygin, A., Wu, J. Y., Chuang, J., Manning, C. D., Ng, A. Y., and Potts, C. (2013). Recursive deep models for semantic compositionality over a sentiment treebank. In Proceedings of the conference on empirical methods in natural language processing (EMNLP), volume 1631, page 1642. Citeseer.
    """

if __name__ == '__main__':
    c = TextClassifier()
    print "Processing training set..."
    c.q4('mini.train')
    print len(c.dict), "words in dictionary"
    print "Fitting model..."
    c.q5()
    print "Accuracy on validation set:", c.q6('mini.valid')[1]
    print "Good alpha:", c.q7('mini.valid')
