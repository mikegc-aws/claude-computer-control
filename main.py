from src.agent.ai_agent import AIAgent
from src.config.settings import load_dotenv
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    load_dotenv()
    agent = AIAgent()

    initial_payload = [{
        "type": 'text',
        "text": """Use Uber Eats, select 2 pepperoni pizzas. Put them in the cart. Then checkout. Use the user that is currently logged in."""
    }]

    # initial_payload = [{
    #     "type": 'text',
    #     "text": """Open Firefox and search for an image of a puppy."""
    # }]


    try:
        agent.invoke_agent(initial_payload)
    except Exception as e:
        logger.error(f"An error occurred while invoking the agent: {str(e)}")

    agent.save_messages_to_file()
    logger.info(f"Finished.")

if __name__ == "__main__":
    main()