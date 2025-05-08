from robusta.api import *

@action
def my_custom_action(event: PodChangeEvent):
    print("Hello from my custom action!")
    for o in event.__dict__:
        print(o)
        print('---')
    print('add')
    event.add_enrichment([JsonBlock('{"message":"Hello Json Custom Action"}')])
    
    res = f'{event.filtered_diffs} - {event.description} - {event.operation}'
    print(f"Custom Action - {res}")

    res = f'{event.response} - {event.obj}'
    print(f"Custom Action - {res}")
    
    

