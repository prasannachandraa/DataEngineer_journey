log_payload = {
    "environment": "Production-EU",
    "events": [
        {"event_id": "E1", "info": {"type": "LOGIN", "severity": "LOW"}},
        {"event_id": "E2", "info": {"type": "TRANSFER", "severity": "HIGH"}},
        {"event_id": "E3", "info": {"type": "PAYMENT", "severity": "MEDIUM"}}
    ]
}



def alert_check(payloads):
    critical_alerts=[]

    req_event=payloads.get('events',[])

    for event in req_event:
        id=event.get('event_id')
        information=event.get('info',{})
        severity_st=information.get('severity')

        if severity_st=='HIGH':
            critical_alerts.append(id)

    print(f"Critical alerts are: {critical_alerts}")
    return critical_alerts

alert_check(log_payload)



