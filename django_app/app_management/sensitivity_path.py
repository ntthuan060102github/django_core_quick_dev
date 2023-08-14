SENSITIVITY_PATHS = {
    # Examples:
    # /survey/<pk> (/survey/1), /survey -> r"^\/survey(\/[0-9]+){0,1}$"
    # /survey/submit -> /survey/submit
    # with specified method: ["GET", "POST"]
    # with all methods: None

    r"^\/survey(\/[0-9]+){0,1}$": ["GET"],
    "/survey/submit": None,
}
