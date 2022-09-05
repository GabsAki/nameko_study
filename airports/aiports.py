import uuid
from nameko_redis import Redis
from nameko.rpc import rpc

class AiportsService:
    name = "aiports_service"

    redis = Redis('development')

    @rpc
    def get(self, aiport_id):
        aiport = self.redis.get(aiport_id)
        
        return aiport

    @rpc
    def create(self, aiport):
        aiport_id = uuid.uuid4().hex
        self.redis.set(aiport_id, aiport)

        return aiport_id
