from agent import AIAgent

# Example usage

agent = AIAgent()

# initial_payload = [{
#     "type": 'text',
#     "text": """Search for an image of a cat.  Then copy it, and paste it into a
# new Google Doc.  Then write a short story about the cat in the document.
# Use the user that is currently logged in."""
# }]

# initial_payload = [{
#     "type": 'text',
#     "text": """Take a look at UberEats in the web browser.
# I am already logged in, so use the user that is currently logged in.  
# Find a McDonald's breakfast that will deliver to my address. 
# Place it in the cart.
# Proceed to checkout.
# Follow the payment steps with PayPal."""
# }]

# initial_payload = [{
#         "type": 'text',
#         "text": """Load Doom, navigate the menu until you're playing the game.
# Do not make assumptions about where you are in the menu.  Take screenshots to check.  
# When you are in the game, find a barrel and shoot it.
# You will need to be nice and close to the barrel to make it explode.
# Make sure the barrel is large and in the center of the screen.
# When moving in the game, consider pressing the movement keys many times so the character moves faster. Concatenate the presses with '+'
# Shoot by clicking the mouse."""
#     }]

# initial_payload = [{
#         "type": 'text',
#         "text": """Start a Minecraft game. Play a game and enter a world."""
#     }]

initial_payload = [{
        "type": 'text',
        "text": """Write a quick Python app. Impress me."""
    }]

agent.invoke_agent(initial_payload)
