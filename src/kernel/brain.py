from memory.memory_engine import MemoryEngine
from goals.goal_manager import GoalManager
from decision.decision_engine import DecisionEngine
from learning.learning_engine import LearningEngine
from evolution.evolution_engine import EvolutionEngine
from security.security_engine import SecurityEngine
from world_model.world_model import WorldModel


class GenesisBrain:

    def __init__(self):

        self.memory = MemoryEngine()
        self.goals = GoalManager()
        self.decision = DecisionEngine()
        self.learning = LearningEngine()
        self.evolution = EvolutionEngine()
        self.security = SecurityEngine()
        self.world = WorldModel()

    def think(self):

        print("Genesis Brain Thinking...")

    def learn(self, experience):

        self.learning.learn(experience)

    def evolve(self):

        self.evolution.evolve()

    def status(self):

        return {
            "memory": "active",
            "goals": "active",
            "decision": "active",
            "learning": "active",
            "evolution": "active",
            "security": "active",
            "world_model": "active"
        }


brain = GenesisBrain()

brain.think()
