import os
from abc import ABC



class Rule(ABC):
    def __init__(self, parameters):
        self._parameters = parameters
        self._name_of_rule
        self._directory = ''
        self._results = []

    def apply(self):
        result = self.check_rule(self._results[0], self._results[1], self._results)
        return result

    def check_rule(self, *kwargs):
        pass

    def set_results(self, results):
        """ Sets the process results i.e the output of the back-ends
         :param results Array with Jsons, one for each file in a job
         Example: {'backend': 'GEE', 'job': 'SWISS', 'file': 'mock/GEE/Swiss/86ec0e53-09fb-4436-ac16-09a5df9cead9.png'}
         """
        self._results = results

    def set_directory(self, directory):
        """ Sets the directory path for the report and possible outputs"""
        self._directory = directory

    def get_name_of_rule(self):
        """ This can be used to see which rule is currently processed"""
        return self._name_of_rule

    def create_file_path(self, combination, prepend, ext):
        filename_a = os.path.splitext(combination[0])[0]
        filename_b = os.path.splitext(combination[1])[0]
        file_path = self._directory + prepend + (filename_a + '_' + filename_b).replace('/', '_') + ext
        return file_path
