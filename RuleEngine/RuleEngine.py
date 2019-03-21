from RuleEngine.Rules.RuleFactory import RuleFactory


class RuleEngine:
    """ This rule engine parses the validation rules from the reference job
    and creates an array with algorithms to be used on the process results """

    def __init__(self, reference_job):
        self.referenceJob = reference_job
        self.functionsList = []
        self.outputFormat = reference_job['job']['output']['format']

    def next_rule(self):
        if len(self.functionsList) > 0:
            next_function = self.functionsList[0]
            self.functionsList.pop(0)
            return next_function
        else:
            return None

    def parse_rules(self):
        """ Parses the reference job for rules and creates a list of rule objects,
            this might be better than parsing them in nextRule as this will allow to throw configuration errors
            beforehand """
        self.functionsList = []
        rule_factory = RuleFactory()
        for rule in self.referenceJob['validation']['rules']:
            newrule = rule_factory.create_rule(self.outputFormat, rule, self.referenceJob['validation']['rules'][rule])
            if newrule:
                self.functionsList.append(newrule)
            else:
                print('The rule: {} does not exist yet'.format(rule))
                print('Skipping rule')