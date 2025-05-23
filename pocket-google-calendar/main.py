from pocketflow import Flow
from nodes import CreateCalendarEventNode, ListCalendarEventsNode, ListCalendarsNode
from datetime import datetime, timedelta

def create_calendar_flow():
    """Creates a flow to manage calendar events."""
    # Create nodes
    create_event_node = CreateCalendarEventNode()
    list_events_node = ListCalendarEventsNode()
    
    # Connect nodes
    create_event_node - "success" >> list_events_node
    create_event_node - "error" >> None
    
    # Create flow
    return Flow(start=create_event_node)

def list_calendars_flow():
    """Creates a flow to list all user calendars."""
    list_calendars_node = ListCalendarsNode()
    return Flow(start=list_calendars_node)

def main():
    # Example: List all user calendars
    print("=== Listing all your calendars ===")
    flow = list_calendars_flow()
    shared = {}
    flow.run(shared)
    if 'available_calendars' in shared:
        for cal in shared['available_calendars']:
            print(f"- {cal.get('summary')} (ID: {cal.get('id')})")
    else:
        print("No calendars found or error listing calendars.")

    # Previous example: create event and list events
    print("\n=== Creating event and listing events ===")
    flow = create_calendar_flow()

    shared = {
        'event_summary': 'Estudo preliminar <Dayan>',
        'event_description': 'Estudo preliminar sobre o projeto do cliente Dayan',
        'event_start_time': datetime.now() + timedelta(days=1),
        'event_end_time': datetime.now() + timedelta(days=1, hours=1),
        'days_to_list': 20
    }

    flow.run(shared)
    if 'last_created_event' in shared:
        print("Event created successfully!")
        print(f"Event ID: {shared['last_created_event']['id']}")

    if 'calendar_events' in shared:
        print("\nEvents for the next 7 days:")
        for event in shared['calendar_events']:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(f"- {event['summary']} ({start})")

if __name__ == "__main__":
    main()