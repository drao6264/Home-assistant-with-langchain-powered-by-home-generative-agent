# Home Generative Agent for Home Assistant

A custom Home Assistant integration enabling natural language control of smart devices and Temi robot navigation using a local LLaMA 3.2 model via LangChain and Ollama.

---

## ✨ Features

- 🔧 **Smart Device Control**: Toggle lights, switches, and appliances using natural language.
- 🤖 **Temi Robot Navigation**: Send Temi to locations like the kitchen, dining table, or bathroom.
- 🧠 **Local LLM Parsing**: Utilizes LangChain with a locally running `llama3` model via Ollama.
- 📁 **No Cloud Required**: Full offline functionality for local and secure automation.

---

## 📂 Project Structure

```bash
/config
├── automations.yaml                  # NLP-triggered automations
├── configuration.yaml                # Core config including input_text
├── temi_scripts.yaml                 # Movement scripts for Temi
├── python_scripts/
│   └── langchain_handler.py          # Trigger NLP logic
└── custom_components/
    └── home_generative_agent/
        ├── __init__.py
        ├── config/
        │   └── configuration.yaml     # Prompt template for LangChain
        ├── langchain_core/
        │   ├── ha_client.py           # Device control functions
        │   ├── main.py                # LangChain execution logic
        │   └── nlp_parser.py          # LLM prompt and parsing
        ├── manifest.json
        └── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Requirements

- Python 3.9 or later
- [Ollama](https://ollama.com/) with LLaMA 3 installed:

```bash
ollama run llama3
```

Ensure it's running and accessible from Home Assistant at `http://<your_host>:11434`

### 2. Installation

1. Copy the `home_generative_agent` folder to `/config/custom_components/` in your Home Assistant instance.
2. Place the provided `automations.yaml`, `temi_scripts.yaml`, `python_scripts/`, and `configuration.yaml` into your `/config/` folder.
3. Ensure the integration folder structure remains intact.

### 3. Update `configuration.yaml`

```yaml
default_config:

input_text:
  assistant_command:
    name: Assistant Command
    initial: ""
    max: 100

script: !include temi_scripts.yaml
automation: !include automations.yaml
```

---

## 🔊 Example Natural Language Commands

- "Turn on the bedroom light"
- "Switch off the kettle"
- "Temi, go to the kitchen"
- "Temi, return to home base"
- "I want coffee"

The NLP module will parse these instructions, identify actions, and send the correct MQTT/device commands.

---

## 📄 License

MIT License

(c) 2025 Home Generative Agent Development

