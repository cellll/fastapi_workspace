from models.sample_model import SampleBody

class MainClass:
    def __init__(self):
        pass

    def sample_method(self, body: SampleBody):
        return body.dict()
        

