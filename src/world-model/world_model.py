class WorldModel:
    def __init__(self):
        self.world_state = {}

    def update(self, key, value):
        self.world_state[key] = value

    def get_state(self):
        return self.world_state

    def predict(self):
        return "Prediction generated"
