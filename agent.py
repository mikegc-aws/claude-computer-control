import boto3
import json
from computer import Computer

class AIAgent:
    def __init__(self, region_name='us-west-2'):
        self.bedrock_client = boto3.client('bedrock-runtime', region_name=region_name)
        self.model_id = "anthropic.claude-3-5-sonnet-20241022-v2:0"
        self.messages = []
        self.computer = Computer()

    def invoke_agent(self, content_payload):

        self.messages.append({"role": "user", "content": content_payload})  

        # with open('messages_log.json', 'w') as f:
        #     json.dump(self.messages, f, indent=4)

        with open('system_prompt.txt', 'r') as file:
            system_prompt = file.read().strip()

        # define the tools that the agent can use.  
        tools = [
            { # new
                "type": "computer_20241022", # literal / constant
                "name": "computer", # literal / constant
                "display_height_px": self.computer.display_height_px, # min=1, no max
                "display_width_px": self.computer.display_width_px, # min=1, no max
            },
            { # new
                "type": "bash_20241022", # literal / constant
                "name": "bash", # literal / constant
            },
            { # new
                "type": "text_editor_20241022", # literal / constant
                "name": "str_replace_editor", # literal / constant
            }
        ]

        # format the payload for the anthropic request.
        anthropic_payload = {
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

        # send messages to Bedrock.
        try:
            response = self.bedrock_client.invoke_model(
                modelId=self.model_id,
                body=json.dumps(anthropic_payload)
            )
            
            # get the anthropic response.
            response_body = json.loads(response['body'].read())
            self.process_response(response_body)
        except Exception as e:
            print(f"Error invoking Bedrock model: {str(e)}")

    def process_response(self, response):
        print(f"Response body from model: {json.dumps(response, indent=4)}")

        # Add the response to messages.
        role = response['role']
        content = response['content']
        self.messages.append({"role": role, "content": content})

        print(f"Stop reason: {response['stop_reason']}")
        
        # Perform post processing to the response.
        if response['stop_reason'] == 'tool_use':
            tool_use = next((item for item in content if item['type'] == 'tool_use'), None)
            if tool_use:
                tool_name = tool_use.get('name')
                tool_input = tool_use.get('input', {})
                
                if tool_name == 'computer':
                    action = tool_input.get('action')
                    feedback = None
                    if action == 'screenshot':
                        result = self.computer.screenshot()
                        feedback = {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/png",
                                "data": result
                            }
                        }

                    elif action == 'key':
                        print(f"Key press: {tool_input}")
                        key = tool_input.get('text')
                        self.computer.key(key)
                        feedback = {
                            "type": "text",
                            "text": f"Key press {key} successful"
                        }
                        
                    elif action == 'type':
                        text = tool_input.get('text')
                        self.computer.type(text)
                        feedback = {
                            "type": "text",
                            "text": f"Text input '{text}' successful"
                        }
                    elif action == 'mouse_move':
                        x = tool_input.get('coordinate')[0]
                        y = tool_input.get('coordinate')[1]
                        self.computer.mouse_move(x, y)
                        feedback = {
                            "type": "text",
                            "text": f"Mouse moved to coordinates ({x}, {y})"
                        }
                    elif action == 'left_click':
                        self.computer.left_click()
                        feedback = {
                            "type": "text",
                            "text": "Left click successful"
                        }
                    elif action == 'right_click':
                        self.computer.right_click()
                        feedback = {
                            "type": "text",
                            "text": "Right click successful"
                        }
                    elif action == 'middle_click':
                        self.computer.middle_click()
                        feedback = {
                            "type": "text",
                            "text": "Middle click successful"
                        }
                    elif action == 'double_click':
                        self.computer.double_click()
                        feedback = {
                            "type": "text",
                            "text": "Double click successful"
                        }
                    elif action == 'left_click_drag':
                        x = tool_input.get('coordinate')[0]
                        y = tool_input.get('coordinate')[1]
                        self.computer.left_click_drag(x, y)
                        feedback = {
                            "type": "text",
                            "text": f"Left click drag from to ({x}, {y}) successful"
                        }
                    elif action == 'cursor_position':
                        result = self.computer.cursor_position()
                        feedback = {"x": result[0], "y": result[1]}
                    else:
                        print(f"Unknown computer action: {action}")
                        feedback = f"Unknown action: {action}"
                    
                    tool_results = ({
                        "type": "tool_result",
                        "content": [feedback],
                        "tool_use_id": tool_use['id'],
                        "is_error": False
                    })

                    self.invoke_agent([tool_results])
                
                elif tool_name == 'bash':
                    # TODO: Implement bash tool
                    pass
                elif tool_name == 'str_replace_editor':
                    # TODO: Implement text editor tool
                    pass
                else:
                    print(f"Unknown tool: {tool_name}")
                
                # Invoke the agent with the combined content

        # Send text response to the user.
        # print("Assistant:", response)