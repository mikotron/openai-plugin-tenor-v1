# 🎉 OpenAI ChatGPT Tenor GIF Plugin 🎉

This is a sample plugin that enables ChatGPT to find and return GIFs from Tenor

📁 openai-plugin-tenor-v1/  # Main project directory
├── ai-plugin.json  # Plugin configuration JSON file 🧩
├── openapi.yaml  # OpenAPI YAML specification file 📄
├── server.py  # Main Python server file 🐍
├── requirements.txt  # Project dependencies file 📦
├── README.md  # Main project documentation file 📝
├── .gitignore  # Git configuration file for ignored files 🙈
└── LICENSE  # Project license file 📜


File details : 

ai-plugin.json: This file contains the plugin configuration in JSON format.
openapi.yaml: This file contains the OpenAPI specification for the plugin's API endpoints.
server.py: This file is the main server code written in Python using the Flask framework. It includes routes for handling requests and communicating with the TENOR API.
requirements.txt: This file lists the dependencies required for the project, such as Flask and requests.
README.md: This file is the project's README documentation, providing an overview and instructions for using the plugin.
.gitignore: This file specifies which files and directories should be ignored by Git version control.
LICENSE: This file contains the license information for the project.

Remember to get your own TENOR API KEY, here https://tenor.com/gifapi/documentation

## 🚀 Features

- Get random GIFs
- Search for GIFs by keyword

Workflow :

Activation: After installing the TENOR plugin in the chat platform or application, the user activates the plugin. This may involve clicking on a plugin icon or accessing the plugin through a command or menu option.
Plugin Interface: Once activated, the user interface displays the plugin interface within the chat window. This interface provides a search bar or an interactive panel to interact with the plugin's features.
Search Query: The user enters a search query for the GIF they want to find. They can type a specific keyword or phrase related to the desired GIF, such as "cat," "happy," or "celebrate."
Search Results: Upon submitting the search query, the plugin fetches the relevant GIFs from the TENOR API based on the query. The search results are displayed within the plugin interface.
Browsing and Selection: The user can browse through the search results, which typically include a collection of GIF thumbnails or previews. They can scroll through the results to explore different options.
GIF Selection: When the user finds a GIF they want to use, they can click on it or select it using an interactive button within the plugin interface. This action indicates their choice of the selected GIF.
Inserting the GIF: Once the user selects a GIF, it is inserted into the chat conversation or message input field. The GIF appears as an animated image within the chat interface.
Sending the GIF: To share the GIF, the user can proceed to send the chat message containing the GIF. This action shares the selected GIF with the other participants in the chat or conversation.
Further Interactions: The user can repeat the process by entering new search queries to discover and insert additional GIFs into their messages. They can use the plugin's features seamlessly within the chat interface as long as the plugin remains active.

## 🛠 Installation

1. Clone this repository
2. Install the required Python packages: `pip install -r requirements.txt`
3. Run the server: `python server.py`

## 🔍 Usage

- Use the `/tenor_random` endpoint to get a random GIF.
- Use the `/tenor_search` endpoint with a query parameter to search for a GIF by keyword.

## 📜 License

This project is licensed under the terms of the MIT license. 

## 🙌 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

To Do stuff :

API Key: In the server.py file, make sure to replace YOUR_TENOR_API_KEY with your actual TENOR API key. This is necessary to authenticate and make successful requests to the TENOR API.
Error Handling: The code provided does not include extensive error handling. It's recommended to add appropriate error handling mechanisms to handle cases such as failed API requests, invalid inputs, or unexpected responses.
Rate Limiting: Depending on the TENOR API's rate limits, you may need to implement rate limiting on your plugin to ensure you don't exceed the allowed number of requests per minute or per day.
Pagination: The code currently retrieves a fixed number of results (limit=10) for each search query. If the TENOR API supports pagination for retrieving more results, you may consider implementing pagination logic to fetch additional pages of results.
Validation and Sanitization: Validate and sanitize user inputs, such as the search query, to prevent security vulnerabilities or unexpected behavior.
Testing: It's important to thoroughly test the plugin's functionality and handle different scenarios to ensure it behaves as expected. Test cases could include handling different search queries, error responses, and edge cases.

## 👩‍💻 Author

me and ai

Enjoy using the plugin! 🎉

Important notes 

- This plugin has not been tested, it's an AI gpt4 generated plugin code, model did learned first the documentation before it's controlled output
- I've generated it using tips and gpt4 , code join, must be checked but it's a first pattern model to fix