sorting = {
    'newest': ["release_time"],
    'trending': ["trending_group", "trending_mixed"],
    'top': ["effective_amount"]
}


def json_rpc(**kwargs):
    return {
        "jsonrpc": "2.0",
        "method": "claim_search",
        "params": {
            "page_size": 24,
            "page": kwargs['page'],
            "claim_type": ["stream", "repost", "channel"],
            "no_totals": True,
            "not_channel_ids": [],
            "order_by": sorting[kwargs['sorting']],
            "remove_duplicates": True,
            "has_source": True,
            "limit_claims_per_channel":
                1, "channel_ids":
                    kwargs['channel_ids'],
                    "release_time": ">1672164000"
                    }}


def resolve_rpc(*args):
    return {
        "jsonrpc": "2.0",
        "method": "resolve",
        "params": {"urls": args[0]}}


def stream_rpc(**kwargs):
    return {
        "jsonrpc": "2.0",
        "method": "get",
        "params": {"uri": kwargs['canon_url'],
                   "environment": "live"}}
