import json
from nameko.rpc import RpcProxy
from nameko.web.handlers import http

class GatewayService:
    name = 'gateway'

    airports_rpc = RpcProxy('airports_service')
    trips_rpc = RpcProxy('trips_service')

    @http('GET', '/airport/<string:airport_id>')
    def get_airport(self, request, aiport_id):
        airport = self.airports_rpc.get(aiport_id)
        
        return json.dumps({'aiport': airport})

    @http('POST', '/aiport')
    def post_aiport(self, request):
        data = json.loads(request.get_data(as_text=True))
        airport_id = self.airports_rpc.create(data['aiport'])

        return airport_id

    @http('GET', '/trip/<string:trip_id>')
    def get_trip(self, request, trip_id):
        trip = self.trips_rpc.get(trip_id)
        return json.dumps({'trip': trip})

    @http('POST', '/trip')
    def post_trip(self, request):
        data = json.loads(request.get_data(as_text=True))
        
        trip_id = self.trips_rpc.create(
            data['aiport_from'],
            data['aiport_to']
        )

        return trip_id
