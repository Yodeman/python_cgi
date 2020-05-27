class FieldMockup:
    def __init__(self, str):
        self.value = str

def formMockup(**kwargs):
    mockup = {}
    for (key, value) in kwargs.items():
        if type(value) != list:
            mockup[key] = FieldMockup(str(value))
        else:
            mockup[key] = []
            for pick in value:
                mockup[key].append(FieldMockup(pick))
    return mockup

