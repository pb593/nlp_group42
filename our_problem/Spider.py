import re


from tensor2tensor.data_generators import problem
from tensor2tensor.data_generators import text_problems
from tensor2tensor.utils import registry

@registry.register_problem
class Spider(text_problems.Text2TextProblem):

    @property
    def approx_vocab_size(self):
        return 2**13

    @property
    def is_generate_per_split(self):
        # generate_data will be called for every split (what is the point of #shards then?)
        return True

    @property
    def dataset_splits(self):
        """Splits of data to produce and number of output shards for each."""
        # 10% evaluation data
        return [{
            "split": problem.DatasetSplit.TRAIN,
            "shards": 9,
        }, {
            "split": problem.DatasetSplit.EVAL,
            "shards": 1,
        }, {
            "split": problem.DatasetSplit.TEST,
            "shards": 1,
        }]

    def generate_samples(self, data_dir, tmp_dir, dataset_split):
        if data_dir[-1] != '/':
            data_dir = data_dir+'/'

        # choose the file to process based on dataset_split
        if dataset_split == problem.DatasetSplit.TRAIN:
            QUESTIONS_DIR = '{}train_spider_inputs.txt'.format(data_dir)
            QUERY_DIR = '{}train_spider_targets.txt'.format(data_dir)
        else: # problem.DatasetSplit.TEST or problem.DatasetSplit.EVAL
            QUESTIONS_DIR = '{}dev_inputs.txt'.format(data_dir)
            QUERY_DIR = '{}dev_targets.txt'.format(data_dir)

        with open(QUESTIONS_DIR,'r') as f:
            questions = [line.replace('\n','') for line in f.readlines()]
        with open(QUERY_DIR,'r') as f:
            query = [line.replace('\n','') for line in f.readlines()]
        for i in range(len(questions)):
            yield {
              "inputs" : questions[i],
              "targets" : query[i]
            }

    @property
    def additional_reserved_tokens(self):
      """Additional reserved tokens. Only for VocabType.SUBWORD.

      Returns:
        List of str tokens that will get vocab ids 2+ (0 and 1 are reserved for
        padding and end-of-string).
      """
      return ["tbl", "hdr","qtn"]
