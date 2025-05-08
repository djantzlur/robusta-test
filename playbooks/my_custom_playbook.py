from robusta.api import *

@action
def my_custom_action(event: ExecutionBaseEvent):
    print("Hello from my custom action!")
    prop=event.__dict__
    print(f"Custom Action - {prop}")
    event.add_enrichment([JsonBlock({"message":"Hello Json Custom Action"})])

