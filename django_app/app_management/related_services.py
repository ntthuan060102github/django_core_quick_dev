from django.conf import settings

SERVICES = {
    "mypt_ho_notification":{
        "domain": {
            "local": "http://myptpdx-api-stag.fpt.net",
            "dev": "http://myptpdx-api-stag.fpt.net",
            "staging": "http://myptpdx-api-stag.fpt.net",
            "production": "http://myptpdx-api.fpt.net"
        },
        "functions": {
            "send_noti_by_unit": {
                "path": "send-noti-by-unit",
                "method": "POST"
            }
        }
    }
}


def get_api_info(service_name, function_name):
    env = settings.ENVIRONMENT
    
    if service_name not in SERVICES:
        raise Exception("'service_name' invalid!")
    if function_name not in SERVICES["service_name"]:
        raise Exception("'function_name' invalid!")
    
    domain = SERVICES[service_name]["domain"][env]
    path = SERVICES[service_name]["functions"][function_name]["path"]
    method = SERVICES[service_name]["functions"][function_name]["method"]
    
    return {
        "api": f"{domain}/{path}",
        "method": method
    }
