from agent import AIAgent

# Example usage

agent = AIAgent()

initial_payload = [{
    "type": 'text',
    "text": """Rickroll me! :)"""
}]


# initial_payload = [{
#     "type": 'text',
#     "text": """Take a look at UberEats in the web browser.
# Use the user that is currently logged in.  
# Find breakfast that will deliver to my address. 
# Place it in the cart.
# Proceed to checkout.
# Follow the payment steps with PayPal."""
# }]

# initial_payload = [{
#     "type": 'text',
#     "text": """Create a new Google Doc, and write a short story.
# Use the user that is currently logged in."""
# }]

#     initial_payload = [{
#         "type": 'text',
#         "text": """Start a game of Doom. 
# First click somewhere on the screen to make the game window active.
# Find a barrel and shoot it.
# When moving in the game, consider pressing the movement keys many times so the character moves faster. Concatenate the presses with '+'"""
#     }]

#     initial_payload = [{
#         "type": 'text',
#         "text": """Start a Minecraft game.
# First click somewhere on the screen to make the game window active.
# Look down and dig a hole. 
# When moving in the game, consider pressing the movement keys many times so the character moves faster. 
# Concatenate the presses with '+'
# If you don't move very far, increase the number of key presses.
# Use the mouse to move around and dig and build."""
#     }]

agent.invoke_agent(initial_payload)
