import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler

## Set up the Streamlit app
st.set_page_config(page_title = "Text to Math Problem Solver and Data Search Assistant",page_icon="✖️➕➖➗🟰♾️")
st.title("✖️➕➖➗🟰♾️ Math Problem Solver Using Gemma 2 - By Bhaskar Shivaji Kumbhar")

groq_api_key = st.sidebar.text_input(label="Groq API Key",type="password")

if not groq_api_key:
    st.info("Please add your Groq API Key to continue")
    st.stop()

llm = ChatGroq(model = "Gemma2-9b-It",groq_api_key=groq_api_key)

## Initializing the tools
wikipedia_wrapper = WikipediaAPIWrapper()
wikipedia_tools = Tool(
    name = "Wikipedia",
    func = wikipedia_wrapper.run,
    description = "A tool for searching the Internt to find the various information on the topic mentioned."
)
    


## Initialize the MATH Tool
match_chain = LLMMathChain.from_llm(llm=llm)
calculator = Tool(
    name = "Calculator",
    func = match_chain.run,
    description="A tool for answering the math related questions. Only input that is allowed is Mathematical Expressions, otherwise will get the error"
)

prompt = """ 
You are a agent whose task is to solve the mathematical questions for the user. Logically arrive at the solution and the detailed explanation for the expression and display
it point wise for the question asked below.
Question : {question}
Answer : 
"""
prompt_template = PromptTemplate(
    input_variables = ["question"],
    template = prompt
)

## Combine all the tools into the chain
chain = LLMChain(llm=llm,prompt = prompt_template)


reasoning_tool = Tool(
    name = "Reasoning Tool",
    func = chain.run,
    description = "A tool for answering logic-based and reasoning questions."
)

##Initialize the agents

assistant_agent = initialize_agent(
    tools = [wikipedia_tools,calculator,reasoning_tool],
    llm = llm,
    agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose = False,
    handle_parsing_errors = True
)

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"Hi, I'm a MATH Chatbot who can answer all your math problems"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

## LEts start the interaction
question=st.text_area("Enter youe question:","I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes. Then I buy a dozen apples and 2 packs of blueberries. Each pack of blueberries contains 25 berries. How many total pieces of fruit do I have at the end?")

if st.button("find my answer"):
    if question:
        with st.spinner("Generate response.."):
            st.session_state.messages.append({"role":"user","content":question})
            st.chat_message("user").write(question)

            st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
            response=assistant_agent.run(st.session_state.messages,callbacks=[st_cb]
                                         )
            st.session_state.messages.append({'role':'assistant',"content":response})
            st.write('### Response:')
            st.success(response)

    else:
        st.warning("Please enter the question")
