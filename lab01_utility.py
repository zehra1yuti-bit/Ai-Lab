class ThermostatAgent:
    """Perceives temperature and electricity price, using utility to adjust tolerance."""

    def __init__(self, target: float = 20.0, default_tolerance: float = 1.0):
        self.target = target
        self.default_tolerance = default_tolerance
        self.history = []

    def act(self, temperature: float, electricity_price: str) -> str:
        # Utility adjustment: If electricity is expensive, tolerate a wider range (tolerance = 3.0)
        if electricity_price.lower() == "expensive":
            tolerance = 3.0
        else:
            tolerance = self.default_tolerance

        # Condition-action rules based on the utility-adjusted tolerance
        if temperature > 40:
            action = "ALARM"
        elif temperature > self.target + tolerance:
            action = "COOL"
        elif temperature < self.target - tolerance:
            action = "HEAT"
        else:
            action = "IDLE"

        self.history.append((temperature, electricity_price, action))
        return action


if __name__ == "__main__":
    agent = ThermostatAgent(target=20.0, default_tolerance=1.0)
    
    # Testing with varying temperatures and electricity prices
    percepts = [(15, "cheap"), (21.5, "expensive"), (22, "cheap"), (27, "expensive"), (42, "cheap")]
    
    for temp, price in percepts:
        print(f"Temp: {temp:>4}C | Price: {price:<9} -> Action: {agent.act(temp, price)}")

    print(f"\nHistory: {agent.history}")