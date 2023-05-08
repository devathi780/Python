import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "you are a college enquiry chat bot for the website:https://jyotinivas.org/"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "JNCbot")

demo.launch(share=True)