from robusta.api import *

@action
def my_custom_action(event: ExecutionBaseEvent):
    print("Hello from my custom action!")
    event.add_enrichment([JsonBlock("message":"Hello Json Custom Action")])

