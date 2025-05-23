from pocketflow import Flow
from nodes import CreateCalendarEventNode, ListCalendarEventsNode, ListCalendarsNode
from datetime import datetime, timedelta

def create_calendar_flow():
    """Cria um fluxo para gerenciar eventos do calendário."""
    # Criar os nós
    create_event_node = CreateCalendarEventNode()
    list_events_node = ListCalendarEventsNode()
    
    # Conectar os nós
    create_event_node - "success" >> list_events_node
    create_event_node - "error" >> None
    
    # Criar o fluxo
    return Flow(start=create_event_node)

def list_calendars_flow():
    """Cria um fluxo para listar todos os calendários do usuário."""
    list_calendars_node = ListCalendarsNode()
    return Flow(start=list_calendars_node)

def main():
    # Exemplo: Listar todos os calendários do usuário
    print("=== Listando todos os seus calendários ===")
    flow = list_calendars_flow()
    shared = {}
    flow.run(shared)
    if 'available_calendars' in shared:
        for cal in shared['available_calendars']:
            print(f"- {cal.get('summary')} (ID: {cal.get('id')})")
    else:
        print("Nenhum calendário encontrado ou erro na listagem.")

    # Exemplo anterior: criar evento e listar eventos
    print("\n=== Criando evento e listando eventos ===")
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
        print("Evento criado com sucesso!")
        print(f"ID do evento: {shared['last_created_event']['id']}")

    if 'calendar_events' in shared:
        print("\nEventos dos próximos 7 dias:")
        for event in shared['calendar_events']:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(f"- {event['summary']} ({start})")

if __name__ == "__main__":
    main()