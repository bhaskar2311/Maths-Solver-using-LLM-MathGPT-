# ✖️➕➖➗🟰♾️ Math Problem Solver Using Gemma 2 (LangChain + Groq)
An AI-powered math chatbot that can solve arithmetic expressions, calculus queries, and logic-based math problems — all in natural language. This project combines LangChain, Groq’s Gemma2-9b-It, and Streamlit to create a sleek conversational interface with dynamic tool-switching for calculation, reasoning, and knowledge search.

## 📌 Features
* ✍️ Accepts natural language math questions (e.g., "What is the derivative of 5x?")
* 🧮 Uses a dedicated LLM Math Chain for symbolic and numeric problem solving
* 🧠 Includes a reasoning tool for multi-step logical math questions
* 🌐 Integrated Wikipedia search tool to fetch definitions and math concepts on demand
* ⚡ Powered by Groq’s Gemma2-9b-It for ultra-fast and accurate LLM inference
* 🖥️ Clean and user-friendly UI built with Streamlit

## 🧠 Technologies Used
* Streamlit – Web UI for interaction
* Langchain – Agent framework and tool orchestration
* Groq API – High-speed inference using Gemma2-9b-It
* LLMMathChain – LangChain’s math-dedicated reasoning chain
* WikipediaAPIWrapper – Lookup and retrieval for general knowledge support
* PromptTemplate – Customized prompts for solving and explaining math

## 🗂 Project Structure
```
├── app.py               # Main Streamlit app
├── requirements.txt     # Python dependencies
└── .env                 # Store your API keys securely (not included)
```

## ⚙️ Setup Instructions
1. Clone the Repository
```
git clone https://github.com/bhaskar2311/Maths-Solver-using-LLM-MathGPT
cd Maths-Solver-using-LLM-MathGPT
```
2. Create a Virtual Environment (optional but recommended)
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Setup Environment Variables
  * Create a .env file in the root directory and add your API keys like this:
```
# .env
GROQ_API_KEY=your_groq_api_key_here
```
🚨 Warning: Never commit .env files to public repositories.

## 🚀 How to Use
```
streamlit run app.py
```
* Input your Groq API Key in the sidebar
* Type your math or reasoning question in the input box
* Click “Find my answer”
* View the computed result along with explanations and relevant wiki lookups

## 💡 Example Questions
* "What is the derivative of 5x with respect to x?"
* "27 + 3"
* "I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes…"

## 📸 Screenshot
![Output1](https://github.com/user-attachments/assets/ba09cddf-a8cb-422a-a20d-dc20fbf32b5c)

## 📝 Notes
* You must enter math expressions or logic-driven word problems in natural language.
* Wikipedia fallback will auto-trigger if conceptual understanding is required.
* The agent uses ZERO_SHOT_REACT_DESCRIPTION to dynamically select tools based on query intent.

## 📝 Description
This project was fully developed by me. The README was written based on my knowledge and experience, with support from generative AI tools to refine its structure and presentation.

## 📄 License
This project is open source and available under the MIT License.

## 🙋‍♂️ Author
Made with ❤️ by Bhaskar Shivaji Kumbhar
