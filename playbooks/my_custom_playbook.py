from robusta.api import *

@action
def my_custom_action(event: ExecutionBaseEvent):
    print("Hello from my custom action!")
    res = f'{event.kind} - {event.name} - {event.namespace} - {event.operation} - {event.labels}'
    print(f"Custom Action - {res}")

    for o in event.__dict__:
        print(o)
        print('---')
    print('add')
    event.add_enrichment([JsonBlock('{"message":"Hello Json Custom Action"}')])

