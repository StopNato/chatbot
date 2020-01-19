
class RunningDialogStatus(object):
    def __init__(self, priority):
        self.priority = priority

    def get_priority(self):
        return self.priority

    def get_insteadof_rules(self):
        return None

    def get_smalltalk_rules(self):
        return None

    def get_name(self):
        raise NotImplementedError()