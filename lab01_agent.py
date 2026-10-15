
class ThermostatAgent:
    """Perceives the temperature ,tracks history,and chooses an action using condition-action rules."""

    def __init__(self, target: float = 20.0, tolerance: float = 2.0):
        self.target = target
        self.tolerance = tolerance
        self.history=[]
    def act(self, temperature: float) -> str:
        if temperature > 40:
            action = "ALARM"
        elif temperature > self.target + self.tolerance:
            action = "COOL"
        elif temperature < self.target - self.tolerance:
            action = "HEAT"
        else:
            action="IDLE"
        self.history.append((temperature, action))    
        return action

if __name__ == "__main__":
    agent = ThermostatAgent(target=20.0, tolerance=2.0)
    for percept in [15, 21.5, 22, 27,45]:
        print(f"Temperature {percept:>5} C -> action: {agent.act(percept)}")

    print(f"\nRecorded percept History: {agent.history}")