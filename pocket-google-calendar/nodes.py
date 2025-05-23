from pocketflow import Node
from utils.google_calendar import create_event, list_events, list_calendar_lists
from datetime import datetime, timedelta

class CreateCalendarEventNode(Node):
    def prep(self, shared):
        """Prepara os dados necessários para criar um evento."""
        return {
            'summary': shared.get('event_summary'),
            'description': shared.get('event_description'),
            'start_time': shared.get('event_start_time'),
            'end_time': shared.get('event_end_time')
        }
    
    def exec(self, event_data):
        """Cria um novo evento no calendário."""
        try:
            event = create_event(
                summary=event_data['summary'],
                description=event_data['description'],
                start_time=event_data['start_time'],
                end_time=event_data['end_time']
            )
            return {'success': True, 'event': event}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def post(self, shared, prep_res, exec_res):
        """Armazena o resultado da criação do evento."""
        if exec_res['success']:
            shared['last_created_event'] = exec_res['event']
            return 'success'
        else:
            shared['error'] = exec_res['error']
            return 'error'

class ListCalendarEventsNode(Node):
    def prep(self, shared):
        """Prepara os parâmetros para listar eventos."""
        return {
            'days': shared.get('days_to_list', 7)
        }
    
    def exec(self, params):
        """Lista os eventos do calendário."""
        try:
            events = list_events(days=params['days'])
            return {'success': True, 'events': events}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def post(self, shared, prep_res, exec_res):
        """Armazena a lista de eventos."""
        if exec_res['success']:
            shared['calendar_events'] = exec_res['events']
            return 'success'
        else:
            shared['error'] = exec_res['error']
            return 'error'

class ListCalendarsNode(Node):
    def prep(self, shared):
        """Não precisa de preparação especial para listar calendários."""
        return {}

    def exec(self, params):
        """Lista todos os calendários disponíveis para o usuário."""
        try:
            calendars = list_calendar_lists()
            return {'success': True, 'calendars': calendars}
        except Exception as e:
            return {'success': False, 'error': str(e)}

    def post(self, shared, prep_res, exec_res):
        """Armazena a lista de calendários no shared store."""
        if exec_res['success']:
            shared['available_calendars'] = exec_res['calendars']
            return 'success'
        else:
            shared['error'] = exec_res['error']
            return 'error' 