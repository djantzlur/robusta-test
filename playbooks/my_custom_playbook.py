from robusta.api import *
import json

@action
def my_custom_action(event: PodChangeEvent):
    print("Hello from my custom action!")
    # for o in event.__dict__:
    #     print(o)
    #     print('---')
    # print('add')
    podName=event.obj.name
    podNamespace=event.obj.namespace
    message=json.dumps({'message':f'pod {podName} in {podNamespace} updated - {event.response}'})
    event.add_enrichment([JsonBlock(message)])
    
    res = f'{event.filtered_diffs} - {event.description} - {event.operation}'
    print(f"Custom Action - {res}")

    for o in event.__dict__.obj:
        print(o)
        print('---')
    
    

