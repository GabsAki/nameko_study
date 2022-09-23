import uuid
from nameko_redis import Redis
from nameko.rpc import rpc

class TripsService:
    name = "trips_service"

    redis = Redis('development')

    @rpc
    def get(self, trip_id):
        
        # Since we are retreaving an entry with a dict, hgetall is necessay instead of get.
        trip = self.redis.hgetall(trip_id)
        
        return trip

    @rpc
    def create(self, airport_from_id, airport_to_id):
        trip_id = uuid.uuid4().hex

        # Since we are creating an entry with a dict, hmset is necessay instead of set.
        self.redis.hmset(
            trip_id,
            {"from": airport_from_id, "to": airport_to_id}
        )

        return trip_id
    