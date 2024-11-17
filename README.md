# Cold Email Generator Bot using LLM, Groq API, LangChain, ChromaDB, and Streamlit
### Overview
This repository hosts a Cold Email Generator Bot designed to create personalized cold emails using powerful language models (LLMs). The project incorporates the Groq API, LangChain, ChromaDB, and Streamlit to deliver an interactive web-based experience for generating high-quality email content.

### Features
- Interactive Streamlit App: A user-friendly web interface for generating and reviewing cold emails.
- LLM Integration: Utilizes advanced language models for crafting emails that sound human-like.
ChromaDB for Context Management: Efficiently retrieves contextual data for tailored email creation.
- LangChain Workflow: Facilitates seamless coordination between LLM components.- 
- Groq API: Ensures fast, reliable processing for language generation.
### Tech Stack
- Python: Core language for the project.
- Streamlit: For building an interactive web interface.
- Groq API: For high-performance LLM integration.
- LangChain: For managing complex LLM workflows.
- ChromaDB: Used as a context database for data-driven personalization.
- pandas: For handling CSV data files.
### Prerequisites
- Python 3.8+
- API keys for Groq API
- Required libraries: `streamlit`, `langchain`, `chromadb`, `pandas`, `dotenv`
### Installation
1. Clone the repository:
```
git clone https://github.com/your-username/cold-email-generator-bot.git
cd cold-email-generator-bot
```
2. Set up a virtual environment:
```
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```
3. Install dependencies:

```
pip install -r requirements.txt
```
4. Set up environment variables: Create a .env file inside the App directory and add your Groq API key:

```
GROQ_API_KEY=your_groq_api_key
```
### Project Structure
```
graphql
cold-email-generator-bot/
│
└── App/
    ├── resources/
    │   ├── myPortfolio.csv    # CSV file containing data for portfolio context
    │   └── vectorstore/       # Directory for ChromaDB vector storage
    ├── .env                   # Environment variable file
    ├── chains.py              # Contains LangChain workflow logic
    ├── Main.py                # Entry point for running the Streamlit app
    ├── portfolio.py           # Portfolio data handling and integration
    ├── test.py                # Script for unit tests and testing functions
    └── utils.py               # Utility functions for data processing and formatting
```
### Usage
##### 1. Running the Streamlit App
To launch the app, navigate to the `App` directory and run:
```
streamlit run Main.py
```
This will open the app in your default web browser where you can input details and generate custom cold emails interactively.

##### 2. Customization
Modify `chains.py` to adapt the logic for different email generation templates or customize `portfolio.py` to handle different context data.

### How It Works
1. User Inputs: The app collects inputs such as target audience, product details, and tone.
2. Context Retrieval: Uses `ChromaDB` to retrieve relevant data from `myPortfolio.csv` and `vectorstore`.
3. Email Generation: `LangChain` orchestrates the process, sending the input data to the LLM via the Groq API.
4. Output Display: The generated email is shown in the Streamlit interface, formatted for review.
### Future Enhancements
- Enhanced Customization: Add more parameters for deeper personalization.
- Performance Metrics: Integrate A/B testing features for analyzing email performance.
- Multi-Language Support: Extend the project to generate emails in different languages.
### Contributing
Contributions are welcome! Please submit pull requests or report issues in the Issues tab.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
