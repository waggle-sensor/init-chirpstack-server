# init-chirpstack-server
This is a simple docker image for running a init script for `wes-chirpstack-server`


## Production Deployment
- When deploying an update, initiate a release process.
- init-chirpstack-server is deployed to nodes via a k3s job in waggle-edge-stack: #TODO change the link to the job yaml file
    - [waggle-edge-stack wes-chirpstack-tracker-deployment.yaml](https://github.com/waggle-sensor/waggle-edge-stack/blob/main/kubernetes/wes-chirpstack/wes-chirpstack-tracker-deployment.yaml)
