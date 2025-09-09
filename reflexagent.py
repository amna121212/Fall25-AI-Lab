# Model-Based Reflex Agent :
# This agent not only checks the current temperature but also remembers the previous 
# action to avoid turning the heater on or off unnecessarily.


class reflex_agent:
    def __init__(self,previous_state = "heater off"):
        self.last_action = previous_state 

    def decide_action(self,temperature):
            if temperature < 20 :
               if self.last_action != " heaater on":
                 self.last_action = "heater on"
                 return "turning heater on"
               else:
                 return "heater is already on"
               
            else:
               if self.last_action !=  "heater off":
                  self.last_action = "heater off"
                  return "turning heater off"
               else:
                    return "heater is already off"

agent = reflex_agent(previous_state="heater off")

            

t = int(input("Enter temperature: "))
print(f"Temperature: {t}°C -> {agent.decide_action(t)}")
        
        