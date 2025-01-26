def normalize_event(event):
    """
    Normalizes the event object to a single consistent structure.
    Returns a dictionary with:
    - method: The HTTP method (GET, POST, etc.)
    - path: The path of the request
    - path_parameters: Path variables (e.g., /dc/{denom})
    - query_parameters: Query string parameters (e.g., ?denom=7)
    """
    # API Gateway HTTP API (browser or SDK invocation)
    if "requestContext" in event and "http" in event["requestContext"]:
        path = event["requestContext"]["http"]["path"]
        return {
            "method": event["requestContext"]["http"]["method"],
            "path": path,
            "pathParameters": event.get("pathParameters", {}),
            "queryParameters": event.get("queryStringParameters", {}),
        }

    # CLI or direct invocation
    elif "path" in event:
        return {
            "method": event.get("httpMethod", "GET"),  # Assume GET if not provided
            "path": event["path"],
            "pathParameters": event.get("pathParameters", {}),
            "queryParameters": event.get("queryStringParameters", {}),
        }

    # Fallback for unknown formats
    return {
        "method": "",
        "path": "",
        "pathParameters": {},
        "queryParameters": {},
    }
