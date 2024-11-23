import chainlit as cl
from llm_client.llm_client import LLMProxyChatOpenAI, LLMProxyOpenAIEmbeddings
from config import MODEL_EMBEDDINGS
import tools
import tools.docX

# Initialize the LLM client
llm = LLMProxyChatOpenAI()
embeddings = LLMProxyOpenAIEmbeddings()

@cl.on_message
async def main(message: cl.Message):
    # Get the full conversation history in OpenAI format
    messages = cl.chat_context.to_openai()
    
    # Call LLM with the full conversation history
    response = await llm.agenerate([messages])
    
    # Send the LLM's response
    await cl.Message(
        content=response.generations[0][0].text,
    ).send()
    
    tools.docX.addText(response.generations[0][0].text)
