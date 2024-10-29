import json
import boto3
from src.tools.computer import Computer
from src.config.settings import BEDROCK_REGION, MODEL_ID, SYSTEM_PROMPT_PATH
import logging
from typing import List, Dict, Any

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AIAgent:
    """
    AI Agent capable of interacting with a computer system and performing various tasks.
    """

    def __init__(self):
        self.bedrock_client = boto3.client('bedrock-runtime', region_name=BEDROCK_REGION)
        self.model_id = MODEL_ID
        self.messages = []
        self.computer = Computer()

    def invoke_agent(self, content_payload: List[Dict[str, Any]]) -> None:
        """
        Invoke the AI agent with the given content payload.

        Args:
            content_payload (List[Dict[str, Any]]): The input content for the agent.
        """
        self.messages.append({"role": "user", "content": content_payload})

        system_prompt = ""  
        with open(SYSTEM_PROMPT_PATH, 'r') as file:
            system_prompt = file.read().strip()

        tools = self._get_available_tools()

        anthropic_payload = self._prepare_anthropic_payload(system_prompt, tools)

        try:
            response = self._invoke_bedrock_model(anthropic_payload)
            self._process_response(response)
        except Exception as e:
            logger.error(f"Error invoking Bedrock model: {str(e)}")

    def _get_available_tools(self) -> List[Dict[str, Any]]:
        """
        Get the list of available tools for the AI agent.

        Returns:
            List[Dict[str, Any]]: A list of tool configurations.
        """
        return [
            {
                "type": "computer_20241022",
                "name": "computer",
                "display_height_px": self.computer.display_height_px,
                "display_width_px": self.computer.display_width_px,
            },
        ]

    def _prepare_anthropic_payload(self, system_prompt: str, tools: List[Dict[str, Any]]) -> Dict[str, Any]:
        return {
            "anthropic_version": "bedrock-2023-05-31",
            "anthropic_beta": ["computer-use-2024-10-22"],
            "system": system_prompt,
            "max_tokens": 4096,
            "top_k": 250,
            "stop_sequences": [],
            "temperature": 1,
            "messages": self.messages,
            "tools": tools,
        }

    def _invoke_bedrock_model(self, payload):
        response = self.bedrock_client.invoke_model(
            modelId=self.model_id,
            body=json.dumps(payload)
        )
        return json.loads(response['body'].read())

    def _process_response(self, response):
        logger.info(f"Response body from model: {json.dumps(response, indent=4)}")

        self.messages.append({"role": response['role'], "content": response['content']})

        logger.info(f"Stop reason: {response['stop_reason']}")

        if response['stop_reason'] == 'tool_use':
            self._handle_tool_use(response['content'])

    def _handle_tool_use(self, content):
        tool_use = next((item for item in content if item['type'] == 'tool_use'), None)
        if tool_use:
            tool_name = tool_use.get('name')
            tool_input = tool_use.get('input', {})

            if tool_name == 'computer':
                feedback = self._execute_computer_action(tool_input)
                self._send_tool_results(feedback, tool_use['id'])

    def _execute_computer_action(self, tool_input: Dict[str, Any]) -> Dict[str, Any]:
        action = tool_input.get('action')
        action_map = {
            'screenshot': self._handle_screenshot,
            'key': self._handle_key_press,
            'type': self._handle_type,
            'mouse_move': self._handle_mouse_move,
            'left_click': self._handle_left_click,
            'right_click': self._handle_right_click,
            'middle_click': self._handle_middle_click,
            'double_click': self._handle_double_click,
            'left_click_drag': self._handle_left_click_drag,
            'cursor_position': self._handle_cursor_position
        }

        handler = action_map.get(action)
        if handler:
            return handler(tool_input)
        else:
            return {"type": "text", "text": f"Unknown computer action: {action}"}

    def _handle_screenshot(self, tool_input: Dict[str, Any]) -> Dict[str, Any]:
        result = self.computer.take_screenshot()
        return {
            "type": "image", 
            "source": {
                "type": "base64",
                "media_type": "image/png",
                "data": result
            }
        }

    def _handle_key_press(self, tool_input: Dict[str, Any]) -> Dict[str, Any]:
        key = tool_input.get('text')
        self.computer.press_key(key)
        return {"type": "text", "text": f"Pressed key: {key}"}

    def _handle_type(self, tool_input: Dict[str, Any]) -> Dict[str, Any]:
        text = tool_input.get('text')
        self.computer.type_text(text)
        return {"type": "text", "text": f"Typed text: {text}"}

    def _handle_mouse_move(self, tool_input: Dict[str, Any]) -> Dict[str, Any]:
        position = tool_input.get('coordinate')
        self.computer.move_mouse(position[0], position[1])
        return {"type": "text", "text": f"Moved mouse to ({position[0]}, {position[1]})"}

    def _handle_left_click(self, tool_input: Dict[str, Any]) -> Dict[str, Any]:
        self.computer.click_mouse('left')
        return {"type": "text", "text": "Performed left click"}

    def _handle_right_click(self, tool_input: Dict[str, Any]) -> Dict[str, Any]:
        self.computer.click_mouse('right')
        return {"type": "text", "text": "Performed right click"}

    def _handle_middle_click(self, tool_input: Dict[str, Any]) -> Dict[str, Any]:
        self.computer.click_mouse('middle')
        return {"type": "text", "text": "Performed middle click"}

    def _handle_double_click(self, tool_input: Dict[str, Any]) -> Dict[str, Any]:
        self.computer.double_click()
        return {"type": "text", "text": "Performed double click"}

    def _handle_left_click_drag(self, tool_input: Dict[str, Any]) -> Dict[str, Any]:
        start_x, start_y = tool_input.get('start_x'), tool_input.get('start_y')
        end_x, end_y = tool_input.get('end_x'), tool_input.get('end_y')
        self.computer.move_mouse(start_x, start_y)
        self.computer.mouse.press(Button.left)
        self.computer.move_mouse(end_x, end_y)
        self.computer.mouse.release(Button.left)
        return {"type": "text", "text": f"Performed left click drag from ({start_x}, {start_y}) to ({end_x}, {end_y})"}

    def _handle_cursor_position(self, tool_input: Dict[str, Any]) -> Dict[str, Any]:
        x, y = self.computer.mouse.position
        return {"type": "text", "text": f"Cursor position: ({x}, {y})"}

    def _send_tool_results(self, feedback, tool_use_id):
        tool_results = {
            "type": "tool_result",
            "content": [feedback],
            "tool_use_id": tool_use_id,
            "is_error": False
        }
        self.invoke_agent([tool_results])
