# Claude Sonnet 3.5 v2 - Computer Control Agent

**Note: This project is currently very much work in progress.**


## ⚠️ Important Warning

**CAUTION: Do not run this project on your personal computer or any system containing sensitive information.**

This project is highly experimental and grants extensive control over the computer it runs on. It has the potential to perform unintended actions that could result in data loss, system instability, or security breaches. Only run this on a dedicated, isolated system specifically set up for testing purposes.

By using this software, you acknowledge the risks involved and accept full responsibility for any consequences that may arise from its use.


## Overview

This project implements an AI Agent powered by Claude 3.5 Sonnet v2 that can interact with and control a computer system. The agent uses the AWS Bedrock runtime to process commands and execute various computer control actions through a structured tool system.

### Key Features:

1. **Computer Interaction**: 
   - Mouse control (movement, clicks, dragging)
   - Keyboard input (typing, key combinations)
   - Screen capture capabilities
   - Support for special key commands

2. **AWS Integration**:
   - Uses AWS Bedrock runtime for AI processing
   - Claude 3.5 Sonnet model integration
   - Configurable through environment variables

3. **Flexible Architecture**:
   - Modular tool system
   - Extensible action handling
   - Comprehensive error handling
   - Detailed logging system

4. **Cross-Platform Support**:
   - Built for MacOS (primary)
   - Uses platform-agnostic libraries (pyautogui, pynput)

## Current State

The project has implemented core functionalities including:
- Complete mouse and keyboard control
- Screenshot capabilities
- AWS Bedrock integration
- Basic system prompt handling
- Tool execution framework

## Configuration

The project uses environment variables for configuration:
- `BEDROCK_REGION`: AWS Bedrock region (default: us-west-2)
- `MODEL_ID`: Claude model identifier (default: anthropic.claude-3-5-sonnet-20241022-v2:0)

## Usage (Don't do this)

The project can be run through the `main.py` script, which initializes the AI agent and can process command payloads. Example usage is provided in the main script, demonstrating automated UI interactions.

## Future Development

- Implementation of bash command capabilities
- Text editor integration
- Enhanced error recovery mechanisms
- Expanded tool integrations
- Additional platform-specific optimizations
- Improved safety checks and validations

## Contribution

As this project is in its early stages, contributions, suggestions, and feedback are welcome. Please note that the codebase is subject to significant changes as development progresses.

## Technical Requirements

- Python 3.x
- AWS credentials configured
- Required Python packages (boto3, pyautogui, pynput)
- Access to AWS Bedrock service
