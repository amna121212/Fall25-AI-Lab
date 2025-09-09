# Model-Based Reflex Agent :
# This agent not only checks the current temperature but also remembers the previous 
# action to avoid turning the heater on or off unnecessarily.

class ModelBasedReflexAgent:
        def __init__(self, threshold_temp, initial_state="Heater OFF"):
         self.threshold_temp = threshold_temp      

        def sensor(self, temp, room_name):
        
         self.current_temp = temp
         self.room_name = room_name

        def performance(self):
         
          if self.current_temp < self.threshold_temp:   
            if self.last_action != "Heater ON":
                self.last_action = "Heater ON"
                return "Turning ON Heater"
            else:
                return "Heater is already ON"
          else:                                       
            if self.last_action != "Heater OFF":
                self.last_action = "Heater OFF"
                return "Turning OFF Heater"
            else:
                return "Heater is already OFF"

        def actuator(self):
         
          action = self.performance()
          print(f"{self.room_name} | {self.current_temp}°C => {action}")


 
rooms = {
    "Living Room": 18,
    "Drawing Room": 22,
    "Kitchen": 25,
    "Bedroom": 15,
}

 
agent = ModelBasedReflexAgent(20, initial_state="Heater OFF")

 
for room, temp in rooms.items():
    agent.sensor(temp, room)
    agent.actuator()
  

print(" === repeated sensor reading")
agent.sensor(20, "Living Room")
agent.actuator()
agent.sensor(20, "Living room")
agent.actuator()
