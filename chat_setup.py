import ipywidgets as widgets
from IPython.display import display, HTML

user_input = widgets.Textarea(
    value='',
    placeholder='Type your question here...',
    description='',
    layout=widgets.Layout(height='200px', width='400px')
)

system_input = widgets.Textarea(
    value='',
    placeholder='Type your system message here...',
    description='',
    layout=widgets.Layout(height='200px', width='400px')
)

send_button = widgets.Button(description="Send")

def send_message(b):

    user_message = user_input.value

    response_dict = pdf_qa({"question": user_message})

    response_text = response_dict['chat_history'][-1].content

    display(HTML(f"<div style='max-width: 800px; word-wrap: break-word;'><b>User question:</b><br>{user_message}<br><br><b>Model response:</b><br>{response_text}</div>"))

send_button.on_click(send_message)

display(user_input, send_button)