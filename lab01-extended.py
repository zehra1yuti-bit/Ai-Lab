from lab01_agent import ThermostatAgent


class LoggingThermostat(ThermostatAgent):
    """A model-based variant: it remembers what it has perceived."""

    def __init__(self, target=22.0, tolerance=1.0):
        super().__init__(target, tolerance)
        self.history = []                      # internal model of the past

    def act(self, temperature):
        action = super().act(temperature)      # reuse the reflex rule
        self.history.append((temperature, action))
        return action


agent = LoggingThermostat()
for t in [15, 21.5, 22, 27, 30]:
    agent.act(t)
print("History:", agent.history)
print("COOL actions:", sum(1 for _, a in agent.history if a == "COOL"))