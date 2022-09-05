import uuid
from nameko_redis import Redis
from nameko.rpc import rpc

class TripsService:
    name = "trips_service"

    redis = Redis('development')

    @rpc
    def get(self, trip_id):
        trip = self.redis.get(trip_id)
        
        return trip

    @rpc
    def create(self, aiport_from_id, aiport_to_id):
        trip_id = uuid.uuid4().hex
        
        self.redis.set(
            trip_id,
            {"from": aiport_from_id, "to": aiport_to_id}
        )

        return trip_id
    