import redis

# redis_client.py (or wherever your client lives)
redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True,
)


def get_redis() -> redis.Redis:
    return redis_client
