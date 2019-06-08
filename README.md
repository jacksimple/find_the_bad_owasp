## What is this?
This repository contains a simple exercise for using Kibana to find something malicious.  Log loading is handled for you, so all you should need to do is use docker compose and then access the Kibana interface.  The data is based on NGINX access logs for a web application.

## Getting started
Assuming you have docker and docker-compose setup:
- docker-compose up

## What just happened?
The docker-compose file sets up Elasticsearch, Kibana and loads the data.  Once the loader is done you should see a message like:
```
loaderowasplab_1         | Starting parse log process
loaderowasplab_1         | Opening log file and reading
loaderowasplab_1         | Loading logs into ES
loaderowasplab_1         | Done
find_the_bad_owasp_loaderowasplab_1 exited with code 0
```

## Now what?
Open your browser and go to localhost:5601 to access Kibana.  I've also provided some Kibana objects to use. To load them:
- Click management in the left menu panel
- Selected "Saved Objects"
- Select Import, and pick the export.json file from the "kibana_dashes" folder.  Import it.
- After successfully importing the dashboards, select "Dashboard" in the left menu panel
- Select the "Access Dashboard" dashboard
- The dashboard should have the time saved, but if it doesn't, the data is on June 2nd.

There is also a screenshots folder that contains pictures of completing these steps.

## Your Challenge
This data is from an access log containing roughly an hour of requests.  Within those, there are three "events" that warrant your attention as a security analyst.  You must find that bad.  In order to be successful you need to answer:
- What was the malicious activity?
- Was it successful?
- What would be your next steps in the context of future mitigations and the rest of your investigation?
